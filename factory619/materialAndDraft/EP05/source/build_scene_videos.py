# -*- coding: utf-8 -*-
"""Render 6 file video `assets/scene1.mp4 .. scene6.mp4` (1080x1920 @ 30fps, H.264) cho EP05
(`ViecNheLuongCao`) theo chuẩn Multi-Keyframe + Split-Screen & Glitch AI Mask Shatter:
  - Scene 1 (0.0–5.5s):  scene1.jpg -> scene1_b.jpg (split-screen dual reality reveal @ 2.65s)
  - Scene 2 (5.5–16.0s): scene2.jpg -> scene2_b.jpg (split-screen phone pressure @ 5.60s local = 11.1s)
  - Scene 3 (16.0–28.5s): scene3.jpg -> scene3_b.jpg (Chị Ba giật máy bật cam @ 6.55s local = 22.55s)
  - Scene 4 (28.5–41.8s): 3-beat climax!
        Beat A (0.00–2.30s = 28.5–30.8s): scene4.jpg (mặt AI mỹ nam nguyên vẹn giơ tay)
        Beat B (2.30–6.20s = 30.8–34.7s): scene4_b.jpg (RGB glitch vỡ mặt nạ AI ngay lúc quơ tay!)
        Beat C (6.20–13.30s = 34.7–41.8s): scene4_c.jpg (split-screen cúp máy tháo chạy & Bé Na bàng hoàng)
  - Scene 5 (41.8–49.5s): scene5.jpg -> scene5_b.jpg (ẩn dụ hoa hồng lưỡi câu -> hang ổ lừa đảo @ 3.85s)
  - Scene 6 (49.5–56.0s): scene6.jpg -> scene6_b.jpg (lưu bằng chứng -> bình tâm trình báo @ 2.20s)

Chạy:
    python factory619/materialAndDraft/EP05/source/build_scene_videos.py
"""
from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw

EP_DIR = Path(__file__).resolve().parent.parent
PROJECT_ROOT = EP_DIR.parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "03_ENGINE"))

from core import FFMPEG  # noqa: E402

W, H, FPS = 1080, 1920, 30
OVERSCAN = 1.28
OW, OH = int(round(W * OVERSCAN)), int(round(H * OVERSCAN))


def smoothstep(x: float) -> float:
    x = max(0.0, min(1.0, x))
    return x * x * (3.0 - 2.0 * x)


def load_overscan(path: Path) -> Image.Image:
    img = Image.open(path).convert("RGB")
    arr = np.asarray(img)
    row_mean = arr.mean(axis=(1, 2))
    col_mean = arr.mean(axis=(0, 2))
    row_std = arr.std(axis=(1, 2))
    col_std = arr.std(axis=(0, 2))
    max_y_trim = int(img.height * 0.04)
    max_x_trim = int(img.width * 0.04)
    y0, y1 = 0, img.height
    while y0 < max_y_trim and (row_mean[y0] > 248 or row_mean[y0] < 7) and row_std[y0] < 6:
        y0 += 1
    while (img.height - y1) < max_y_trim and (row_mean[y1 - 1] > 248 or row_mean[y1 - 1] < 7) and row_std[y1 - 1] < 6:
        y1 -= 1
    x0, x1 = 0, img.width
    while x0 < max_x_trim and (col_mean[x0] > 248 or col_mean[x0] < 7) and col_std[x0] < 6:
        x0 += 1
    while (img.width - x1) < max_x_trim and (col_mean[x1 - 1] > 248 or col_mean[x1 - 1] < 7) and col_std[x1 - 1] < 6:
        x1 -= 1
    if (x0, y0, x1, y1) != (0, 0, img.width, img.height):
        img = img.crop((x0, y0, x1, y1))

    aspect = W / H
    if img.width / img.height > aspect:
        tw = int(round(img.height * aspect))
        ox = (img.width - tw) // 2
        img = img.crop((ox, 0, ox + tw, img.height))
    else:
        th = int(round(img.width / aspect))
        oy = (img.height - th) // 2
        img = img.crop((0, oy, img.width, oy + th))
    return img.resize((OW, OH), Image.Resampling.LANCZOS)


def crop_cam(src: Image.Image, u: float, scale: tuple[float, float],
             focus: tuple[tuple[float, float], tuple[float, float]],
             wobble: str, t: float) -> Image.Image:
    e = smoothstep(u)
    sc = scale[0] + (scale[1] - scale[0]) * e
    fx = focus[0][0] + (focus[1][0] - focus[0][0]) * e
    fy = focus[0][1] + (focus[1][1] - focus[0][1]) * e

    wx = wy = 0.0
    if wobble == "calm":
        wx = math.sin(t * 1.4) * 4.0
        wy = math.cos(t * 1.1) * 3.0
    elif wobble == "handheld":
        wx = math.sin(t * 3.1) * 7.5 + math.cos(t * 5.3) * 3.0
        wy = math.cos(t * 2.7) * 6.0 + math.sin(t * 4.7) * 2.5
    elif wobble == "tense":
        wx = math.sin(t * 4.6) * 8.5 + math.cos(t * 7.9) * 3.5
        wy = math.cos(t * 3.9) * 7.0 + math.sin(t * 6.4) * 3.0

    cw = min(OW, W * OVERSCAN / max(1.0, sc))
    ch = min(OH, H * OVERSCAN / max(1.0, sc))
    cx = fx * OW + wx
    cy = fy * OH + wy
    x0 = max(0.0, min(OW - cw, cx - cw / 2.0))
    y0 = max(0.0, min(OH - ch, cy - ch / 2.0))
    return src.crop((x0, y0, x0 + cw, y0 + ch)).resize((W, H), Image.Resampling.BICUBIC)


def draw_motes(frame: Image.Image, t: float, color: tuple[int, int, int], count: int = 16, seed: int = 7) -> Image.Image:
    ov = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)
    for i in range(count):
        ph = (i * 1.618 + seed * 0.73) % 1.0
        x = ((ph * 997 + t * (16 + (i % 5) * 6) + math.sin(t * 1.3 + i) * 22) % W)
        y = (H - ((ph * 1543 + t * (22 + (i % 4) * 8)) % H))
        r = 3 + (i % 4) * 2
        alpha = int(55 + 65 * (0.5 + 0.5 * math.sin(t * 2.6 + i * 1.1)))
        d.ellipse([x - r * 2, y - r * 2, x + r * 2, y + r * 2], fill=(*color, alpha // 3))
        d.ellipse([x - r, y - r, x + r, y + r], fill=(*color, alpha))
    return Image.alpha_composite(frame.convert("RGBA"), ov).convert("RGB")


def draw_pulse_rings(frame: Image.Image, t: float, cx: float, cy: float,
                     rgb: tuple[int, int, int] = (235, 45, 55), speed: float = 1.0) -> Image.Image:
    ov = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)
    for k in range(2):
        p = (t * speed + k * 0.5) % 1.0
        r = 34 + p * 165
        alpha = int((1.0 - p) * 145)
        if alpha > 8:
            d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=(*rgb, alpha), width=4)
    return Image.alpha_composite(frame.convert("RGBA"), ov).convert("RGB")


def rgb_glitch_blend(fa: Image.Image, fb: Image.Image, p: float, seed_t: float) -> Image.Image:
    """Digital RGB chromatic-split + horizontal slice glitch for AI face-swap shatter."""
    base = fa if p < 0.5 else fb
    arr = np.array(base, dtype=np.uint8)
    strength = 1.0 - abs(p - 0.5) * 2.0
    shift = max(2, int(round(28 * strength)))
    out = arr.copy()
    # Red/Cyan channel horizontal offset
    out[:, shift:, 0] = arr[:, :-shift, 0]
    out[:, :-shift, 2] = arr[:, shift:, 2]
    # 6 horizontal digital tear bands
    rng = np.random.default_rng(int(seed_t * 1000) + 17)
    for _ in range(6):
        y0 = int(rng.integers(200, H - 260))
        bh = int(rng.integers(14, 58))
        dx = int(rng.integers(-48, 49) * max(0.35, strength))
        out[y0:y0 + bh] = np.roll(out[y0:y0 + bh], dx, axis=1)
    return Image.fromarray(out)


def subtle_ai_mesh_flicker(frame: Image.Image, t: float) -> Image.Image:
    """Subtle periodic digital scan-bar flicker on phone screen while AI filter is breaking."""
    phase = math.sin(t * 19.0) * math.cos(t * 11.0)
    if phase < 0.55:
        return frame
    arr = np.array(frame, dtype=np.uint8)
    # Confine glitch flicker to phone region (center-lower area y=780..1540, x=320..760)
    y0 = 820 + int((t * 430) % 620)
    bh = 24
    arr[y0:y0 + bh, 330:750, 0] = np.roll(arr[y0:y0 + bh, 330:750, 0], 10, axis=1)
    arr[y0:y0 + bh, 330:750, 2] = np.roll(arr[y0:y0 + bh, 330:750, 2], -10, axis=1)
    return Image.fromarray(arr)


def blend_transition(fa: Image.Image, fb: Image.Image, p: float, kind: str, t: float) -> Image.Image:
    if kind == "flash_white":
        base = fa if p < 0.5 else fb
        flash = 1.0 - abs(p - 0.5) * 2.0
        return Image.blend(base, Image.new("RGB", (W, H), (255, 250, 244)), min(0.82, flash * 0.85))
    if kind == "flash_red":
        base = fa if p < 0.5 else fb
        flash = 1.0 - abs(p - 0.5) * 2.0
        return Image.blend(base, Image.new("RGB", (W, H), (225, 28, 42)), min(0.68, flash * 0.72))
    if kind == "rgb_glitch":
        return rgb_glitch_blend(fa, fb, p, t)
    return Image.blend(fa, fb, p)


def open_ffmpeg(out_mp4: Path) -> subprocess.Popen:
    cmd = [
        FFMPEG, "-y", "-v", "error",
        "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
        "-an", "-c:v", "libx264", "-preset", "medium", "-crf", "18",
        "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(out_mp4),
    ]
    return subprocess.Popen(cmd, stdin=subprocess.PIPE)


def render_two_beat(idx: int, dur_sec: float, split_sec: float, trans: str, dur_tr: float,
                    cam_a: dict, cam_b: dict) -> Path:
    assets = EP_DIR / "assets"
    img_a = load_overscan(assets / f"scene{idx}.jpg")
    img_b = load_overscan(assets / f"scene{idx}_b.jpg")
    out_mp4 = assets / f"scene{idx}.mp4"
    n_frames = max(2, int(round(dur_sec * FPS)))
    tr_half = dur_tr / 2.0

    proc = open_ffmpeg(out_mp4)
    assert proc.stdin is not None
    for fi in range(n_frames):
        t = fi / FPS
        ua = max(0.0, min(1.0, t / max(split_sec + tr_half, 1e-3)))
        ub = max(0.0, min(1.0, (t - (split_sec - tr_half)) / max(dur_sec - (split_sec - tr_half), 1e-3)))
        if t <= split_sec - tr_half:
            fr = crop_cam(img_a, ua, cam_a["scale"], cam_a["focus"], cam_a["wobble"], t)
            beat = "a"
        elif t >= split_sec + tr_half:
            fr = crop_cam(img_b, ub, cam_b["scale"], cam_b["focus"], cam_b["wobble"], t)
            beat = "b"
        else:
            p = smoothstep((t - (split_sec - tr_half)) / max(dur_tr, 1e-4))
            fa = crop_cam(img_a, ua, cam_a["scale"], cam_a["focus"], cam_a["wobble"], t)
            fb = crop_cam(img_b, ub, cam_b["scale"], cam_b["focus"], cam_b["wobble"], t)
            fr = blend_transition(fa, fb, p, trans, t)
            beat = "b" if p >= 0.5 else "a"

        # Scene-specific 2D anime FX
        if idx == 1:
            fr = draw_motes(fr, t, (255, 165, 200) if beat == "a" else (110, 220, 255), count=15, seed=11)
        elif idx == 2:
            if beat == "a":
                fr = draw_pulse_rings(fr, t, W * 0.52, H * 0.69, rgb=(240, 40, 50), speed=1.1)
            else:
                fr = draw_pulse_rings(fr, t, W * 0.78, H * 0.32, rgb=(245, 50, 60), speed=1.35)
        elif idx == 3:
            if beat == "b":
                fr = draw_pulse_rings(fr, t, W * 0.54, H * 0.34, rgb=(70, 240, 140), speed=1.25)
        elif idx == 5:
            fr = draw_motes(fr, t, (255, 95, 130) if beat == "a" else (95, 225, 250), count=16, seed=51)
        elif idx == 6:
            fr = draw_motes(fr, t, (255, 232, 170), count=16, seed=61)

        proc.stdin.write(fr.tobytes())

    proc.stdin.close()
    if proc.wait() != 0:
        raise RuntimeError(f"FFmpeg lỗi khi xuất {out_mp4.name}")
    return out_mp4


def render_scene4_climax(dur_sec: float) -> Path:
    """3-keyframe climax (28.5s -> 41.8s = 13.3s):
       Beat A (0.00 -> 2.30s): scene4.jpg (intact AI handsome boyfriend raising hand)
       Beat B (2.30 -> 6.20s): scene4_b.jpg (RGB glitch @ 2.30s = 30.8s global, AI polygon face shattered!)
       Beat C (6.20 -> 13.30s): scene4_c.jpg (flash_red @ 6.20s = 34.7s global after call_end, split-screen aftermath!)
    """
    assets = EP_DIR / "assets"
    img_a = load_overscan(assets / "scene4.jpg")
    img_b = load_overscan(assets / "scene4_b.jpg")
    img_c = load_overscan(assets / "scene4_c.jpg")
    out_mp4 = assets / "scene4.mp4"
    n_frames = max(2, int(round(dur_sec * FPS)))

    t1, tr1 = 2.30, 0.30   # 30.80s global: hand wave breaks AI filter!
    t2, tr2 = 6.20, 0.28   # 34.70s global: right after call_end (34.1s), before l7 (35.2s)!

    cam_a = {"scale": (1.04, 1.13), "focus": ((0.50, 0.52), (0.50, 0.56)), "wobble": "tense"}
    cam_b = {"scale": (1.16, 1.04), "focus": ((0.50, 0.60), (0.50, 0.50)), "wobble": "tense"}
    cam_c = {"scale": (1.03, 1.11), "focus": ((0.50, 0.50), (0.50, 0.48)), "wobble": "handheld"}

    proc = open_ffmpeg(out_mp4)
    assert proc.stdin is not None
    for fi in range(n_frames):
        t = fi / FPS
        ua = max(0.0, min(1.0, t / (t1 + tr1 / 2)))
        ub = max(0.0, min(1.0, (t - (t1 - tr1 / 2)) / (t2 - t1 + tr1)))
        uc = max(0.0, min(1.0, (t - (t2 - tr2 / 2)) / (dur_sec - (t2 - tr2 / 2))))

        if t <= t1 - tr1 / 2:
            fr = crop_cam(img_a, ua, cam_a["scale"], cam_a["focus"], cam_a["wobble"], t)
        elif t < t1 + tr1 / 2:
            p = smoothstep((t - (t1 - tr1 / 2)) / tr1)
            fa = crop_cam(img_a, ua, cam_a["scale"], cam_a["focus"], cam_a["wobble"], t)
            fb = crop_cam(img_b, ub, cam_b["scale"], cam_b["focus"], cam_b["wobble"], t)
            fr = blend_transition(fa, fb, p, "rgb_glitch", t)
        elif t <= t2 - tr2 / 2:
            fr = crop_cam(img_b, ub, cam_b["scale"], cam_b["focus"], cam_b["wobble"], t)
            fr = subtle_ai_mesh_flicker(fr, t)
        elif t < t2 + tr2 / 2:
            p = smoothstep((t - (t2 - tr2 / 2)) / tr2)
            fb = crop_cam(img_b, ub, cam_b["scale"], cam_b["focus"], cam_b["wobble"], t)
            fc = crop_cam(img_c, uc, cam_c["scale"], cam_c["focus"], cam_c["wobble"], t)
            fr = blend_transition(fb, fc, p, "flash_red", t)
        else:
            fr = crop_cam(img_c, uc, cam_c["scale"], cam_c["focus"], cam_c["wobble"], t)
            fr = draw_motes(fr, t, (140, 195, 255), count=12, seed=43)

        proc.stdin.write(fr.tobytes())

    proc.stdin.close()
    if proc.wait() != 0:
        raise RuntimeError("FFmpeg lỗi khi xuất scene4.mp4")
    return out_mp4


def main() -> None:
    cfg = json.loads((EP_DIR / "episode.json").read_text(encoding="utf-8"))
    scenes = cfg["scenes"]

    specs = {
        1: (2.65, "dissolve", 0.34,
            {"scale": (1.03, 1.11), "focus": ((0.50, 0.52), (0.50, 0.48)), "wobble": "calm"},
            {"scale": (1.04, 1.12), "focus": ((0.50, 0.50), (0.50, 0.47)), "wobble": "tense"}),
        2: (5.60, "flash_red", 0.26,
            {"scale": (1.04, 1.13), "focus": ((0.50, 0.50), (0.50, 0.47)), "wobble": "handheld"},
            {"scale": (1.10, 1.03), "focus": ((0.50, 0.48), (0.50, 0.50)), "wobble": "tense"}),
        3: (6.55, "flash_white", 0.24,
            {"scale": (1.03, 1.12), "focus": ((0.50, 0.50), (0.50, 0.47)), "wobble": "handheld"},
            {"scale": (1.11, 1.03), "focus": ((0.48, 0.46), (0.50, 0.50)), "wobble": "tense"}),
        5: (3.85, "rgb_glitch", 0.30,
            {"scale": (1.03, 1.11), "focus": ((0.50, 0.50), (0.50, 0.46)), "wobble": "calm"},
            {"scale": (1.04, 1.11), "focus": ((0.50, 0.50), (0.50, 0.48)), "wobble": "calm"}),
        6: (2.20, "dissolve", 0.35,
            {"scale": (1.02, 1.08), "focus": ((0.50, 0.48), (0.50, 0.48)), "wobble": "none"},
            {"scale": (1.03, 1.08), "focus": ((0.50, 0.48), (0.50, 0.48)), "wobble": "none"}),
    }

    for i, sc in enumerate(scenes, start=1):
        dur = float(sc["end"]) - float(sc["start"])
        if i == 4:
            out = render_scene4_climax(dur)
            print(f" -> Đã dựng {out.name} (3-keyframe climax): {dur:.2f}s ({int(round(dur * FPS))} frames) · {out.stat().st_size / 1048576:.2f} MB")
        else:
            sp, tr, dtr, ca, cb = specs[i]
            out = render_two_beat(i, dur, sp, tr, dtr, ca, cb)
            print(f" -> Đã dựng {out.name}: {dur:.2f}s ({int(round(dur * FPS))} frames, split={sp:.2f}s) · {out.stat().st_size / 1048576:.2f} MB")


if __name__ == "__main__":
    main()
