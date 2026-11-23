# -*- coding: utf-8 -*-
"""
Reusable Pixel-Locked Face ROI Baker (`03_ENGINE/face_roi_prep.py`)
Chuẩn bị ảnh biến thể cho Living-Character Micro-Motion (A: eye_blink + B: mouth_sync):
  1. Nhận ảnh gốc (`sceneX.jpg`) + ảnh AI image-edit thô (nhắm mắt / ngậm miệng / mở miệng) + vùng ROI pixel.
  2. Tự động căn dịch chuyển (dx, dy trong [-12..+12]) bằng vòng neo xung quanh vùng ROI để lệch = 0px.
  3. Tự động cân màu da cục bộ trên viền 14px quanh ROI để triệt tiêu hoàn toàn viền màu.
  4. Chỉ hòa trộn vùng elip làm mềm biên lên ảnh gốc giữ nguyên 99% khung hình gốc 100% pixel.

Chạy nhanh qua CLI:
    python 03_ENGINE/face_roi_prep.py --orig scene1.jpg --edit raw_blink.jpg --out scene1_blink.jpg --roi 574 694 744 758 --feather 7.0
"""
from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

from motion_fx import fit_aspect_crop


def align_and_bake_roi(
    orig_path: str | Path,
    raw_edit_path: str | Path,
    out_path: str | Path,
    roi_px: tuple[int, int, int, int],
    anchor_pad: int = 56,
    feather_px: float = 8.0,
    search_r: int = 12,
    quality: int = 94,
) -> dict:
    """Align AI-edited face variant to original pixel-for-pixel via anchor ring correlation,
    match local border skin tone, and composite ONLY the elliptical ROI onto untouched original."""
    orig_p, edit_p, out_p = Path(orig_path), Path(raw_edit_path), Path(out_path)
    orig_im = Image.open(orig_p).convert("RGB")
    W, H = orig_im.size
    edit_im = Image.open(edit_p).convert("RGB")
    if edit_im.size != (W, H):
        edit_im = fit_aspect_crop(edit_im, W, H).resize((W, H), Image.Resampling.LANCZOS)

    orig = np.asarray(orig_im, dtype=np.float32)
    edit = np.asarray(edit_im, dtype=np.float32)

    x0, y0, x1, y1 = [int(v) for v in roi_px]
    ax0, ay0 = max(search_r, x0 - anchor_pad), max(search_r, y0 - anchor_pad)
    ax1, ay1 = min(W - search_r, x1 + anchor_pad), min(H - search_r, y1 + anchor_pad)

    ring_mask = np.ones((ay1 - ay0, ax1 - ax0), dtype=bool)
    ring_mask[(y0 - ay0):(y1 - ay0), (x0 - ax0):(x1 - ax0)] = False
    orig_patch = orig[ay0:ay1, ax0:ax1]

    best_dx, best_dy, best_err = 0, 0, 1e18
    for dy in range(-search_r, search_r + 1, 2):
        for dx in range(-search_r, search_r + 1, 2):
            cand = edit[ay0 + dy: ay1 + dy, ax0 + dx: ax1 + dx]
            err = float(np.mean(np.abs(cand[ring_mask] - orig_patch[ring_mask])))
            if err < best_err:
                best_err, best_dx, best_dy = err, dx, dy

    cx, cy = best_dx, best_dy
    for dy in range(max(-search_r, cy - 2), min(search_r, cy + 2) + 1):
        for dx in range(max(-search_r, cx - 2), min(search_r, cx + 2) + 1):
            cand = edit[ay0 + dy: ay1 + dy, ax0 + dx: ax1 + dx]
            err = float(np.mean(np.abs(cand[ring_mask] - orig_patch[ring_mask])))
            if err < best_err:
                best_err, best_dx, best_dy = err, dx, dy

    shifted = np.zeros_like(edit)
    src_y0, src_y1 = max(0, best_dy), min(H, H + best_dy)
    src_x0, src_x1 = max(0, best_dx), min(W, W + best_dx)
    dst_y0, dst_x0 = max(0, -best_dy), max(0, -best_dx)
    shifted[dst_y0: dst_y0 + (src_y1 - src_y0), dst_x0: dst_x0 + (src_x1 - src_x0)] = edit[src_y0:src_y1, src_x0:src_x1]

    pad_c = 14
    cx0, cy0 = max(0, x0 - pad_c), max(0, y0 - pad_c)
    cx1, cy1 = min(W, x1 + pad_c), min(H, y1 + pad_c)
    cmask = np.ones((cy1 - cy0, cx1 - cx0), dtype=bool)
    cmask[(y0 - cy0):(y1 - cy0), (x0 - cx0):(x1 - cx0)] = False
    o_ring = orig[cy0:cy1, cx0:cx1][cmask]
    e_ring = shifted[cy0:cy1, cx0:cx1][cmask]
    diff_mean = np.clip(o_ring.mean(axis=0) - e_ring.mean(axis=0), -18.0, 18.0)
    matched = np.clip(shifted + diff_mean[None, None, :], 0.0, 255.0)

    m_im = Image.new("L", (W, H), 0)
    ImageDraw.Draw(m_im).ellipse([x0, y0, x1, y1], fill=255)
    m_im = m_im.filter(ImageFilter.GaussianBlur(radius=feather_px))
    alpha = np.asarray(m_im, dtype=np.float32)[:, :, None] / 255.0

    comp = orig * (1.0 - alpha) + matched * alpha
    out_p.parent.mkdir(parents=True, exist_ok=True)
    Image.fromarray(np.clip(comp, 0, 255).astype(np.uint8), mode="RGB").save(out_p, quality=quality)

    # Return normalized region with ~10px safety margin ready for episode.json
    pad_norm = 10
    norm_region = [
        round(max(0.0, (x0 - pad_norm) / W), 3),
        round(max(0.0, (y0 - pad_norm) / H), 3),
        round(min(1.0, (x1 + pad_norm) / W), 3),
        round(min(1.0, (y1 + pad_norm) / H), 3),
    ]
    return {
        "out": str(out_p),
        "shift_px": [best_dx, best_dy],
        "ring_l1": round(best_err, 2),
        "color_shift_rgb": [round(float(v), 1) for v in diff_mean],
        "recommended_region": norm_region,
    }


def make_face_qc_sheet(
    rows: list[tuple[str, tuple[int, int, int, int], list[Path]]],
    out_path: str | Path,
    cell_size: int = 360,
) -> Path:
    """Build side-by-side zoomed Face QC contact sheet (ORIG | BLINK | MOUTH_CLOSED | MOUTH_OPEN)."""
    max_cols = max(len(r[2]) for r in rows)
    sheet = Image.new("RGB", (cell_size * max_cols, cell_size * len(rows)), (18, 20, 26))
    d = ImageDraw.Draw(sheet)
    for ri, (tag, box, paths) in enumerate(rows):
        for ci, p in enumerate(paths):
            crop = Image.open(p).convert("RGB").crop(box).resize((cell_size, cell_size), Image.Resampling.LANCZOS)
            sheet.paste(crop, (ci * cell_size, ri * cell_size))
            d.rectangle([ci * cell_size, ri * cell_size, ci * cell_size + 240, ri * cell_size + 26], fill=(0, 0, 0))
            d.text((ci * cell_size + 6, ri * cell_size + 6), f"{tag}: {Path(p).name}", fill=(255, 240, 120))
    out_p = Path(out_path)
    out_p.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(out_p, quality=92)
    return out_p


def main() -> None:
    ap = argparse.ArgumentParser(description="Bake pixel-locked elliptical eye/mouth ROI variants onto original scene.")
    ap.add_argument("--orig", required=True, help="Original approved scene image")
    ap.add_argument("--edit", required=True, help="Raw AI-edited blink/mouth image")
    ap.add_argument("--out", required=True, help="Output pixel-locked scene variant path")
    ap.add_argument("--roi", type=int, nargs=4, required=True, metavar=("X0", "Y0", "X1", "Y1"), help="Tight pixel ROI box")
    ap.add_argument("--feather", type=float, default=8.0, help="Elliptical feather radius in px (default 8.0)")
    ap.add_argument("--search", type=int, default=12, help="Max alignment shift search in px (default 12)")
    args = ap.parse_args()
    res = align_and_bake_roi(args.orig, args.edit, args.out, tuple(args.roi), feather_px=args.feather, search_r=args.search)
    print(f"OK -> {res['out']} | shift={res['shift_px']} ring_L1={res['ring_l1']} color={res['color_shift_rgb']} region={res['recommended_region']}")


if __name__ == "__main__":
    main()
