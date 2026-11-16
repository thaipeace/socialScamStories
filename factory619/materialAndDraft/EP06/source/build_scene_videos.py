# -*- coding: utf-8 -*-
"""Render 6 file video `assets/scene1.mp4 .. scene6.mp4` (1080x1920 @ 30fps, H.264) cho EP06
theo đúng chuẩn Action-Keyframe 2 nhịp (`sceneX.jpg` -> `sceneX_b.jpg`) của `EP01`.

Chạy:
    python factory619/materialAndDraft/EP06/source/build_scene_videos.py
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
    # Trim accidental thin solid white/black letterbox bars (< 4% per edge) if AI left any
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

    cw = W / max(1.0, sc) * (OW / W)
    ch = H / max(1.0, sc) * (OH / H)
    # Simpler & exact: src is OW x OH (= 1.28 * W x 1.28 * H).
    # At scale=1.0, crop window is W x H; wait: if scale > 1.0, we zoom in further so crop is smaller!
    cw = min(OW, W * OVERSCAN / max(1.0, sc))
    ch = min(OH, H * OVERSCAN / max(1.0, sc))
    cx = fx * OW + wx
    cy = fy * OH + wy
    x0 = max(0.0, min(OW - cw, cx - cw / 2.0))
    y0 = max(0.0, min(OH - ch, cy - ch / 2.0))
    return src.crop((x0, y0, x0 + cw, y0 + ch)).resize((W, H), Image.Resampling.BICUBIC)


def draw_motes(frame: Image.Image, t: float, color: tuple[int, int, int], count: int = 18, seed: int = 7) -> Image.Image:
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


def draw_danger_pulses(frame: Image.Image, t: float, cx: float, cy: float) -> Image.Image:
    ov = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)
    for k in range(2):
        p = (t * 0.95 + k * 0.5) % 1.0
        r = 36 + p * 175
        alpha = int((1.0 - p) * 145)
        if alpha > 8:
            d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=(235, 45, 50, alpha), width=4)
    return Image.alpha_composite(frame.convert("RGBA"), ov).convert("RGB")


def draw_whistle_waves(frame: Image.Image, t: float, cx: float, cy: float) -> Image.Image:
    ov = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)
    # Expanding acoustic arcs pointing left (from right-side patrol toward left-side burglars)
    for k in range(3):
        p = (t * 1.35 + k * 0.33) % 1.0
        r = 45 + p * 240
        alpha = int((1.0 - p) * 165)
        if alpha > 10:
            d.arc([cx - r, cy - r, cx + r, cy + r], start=135, end=225, fill=(255, 245, 190, alpha), width=5)
    # Subtle anime action diagonal streaks
    for i in range(10):
        px = ((i * 173 - t * 620) % (W + 300)) - 150
        py = 260 + (i * 137) % 1250
        d.line([(px, py), (px + 95, py + 18)], fill=(255, 250, 220, 48), width=2)
    return Image.alpha_composite(frame.convert("RGBA"), ov).convert("RGB")


SCENE_SPECS = {
    1: {
        "trans": "dissolve",
        "dur_tr": 0.30,
        "a": {"scale": (1.03, 1.11), "focus": ((0.50, 0.50), (0.48, 0.48)), "wobble": "calm"},
        "b": {"scale": (1.04, 1.13), "focus": ((0.50, 0.52), (0.50, 0.47)), "wobble": "calm"},
    },
    2: {
        "trans": "flash_white",
        "dur_tr": 0.24,
        "a": {"scale": (1.04, 1.14), "focus": ((0.52, 0.50), (0.48, 0.48)), "wobble": "tense"},
        "b": {"scale": (1.12, 1.04), "focus": ((0.50, 0.47), (0.50, 0.50)), "wobble": "handheld"},
    },
    3: {
        "trans": "dissolve",
        "dur_tr": 0.28,
        "a": {"scale": (1.04, 1.13), "focus": ((0.50, 0.48), (0.50, 0.45)), "wobble": "tense"},
        "b": {"scale": (1.03, 1.11), "focus": ((0.52, 0.50), (0.49, 0.47)), "wobble": "calm"},
    },
    4: {
        "trans": "flash_white",
        "dur_tr": 0.26,
        "a": {"scale": (1.12, 1.03), "focus": ((0.52, 0.48), (0.48, 0.50)), "wobble": "handheld"},
        "b": {"scale": (1.03, 1.10), "focus": ((0.50, 0.50), (0.50, 0.47)), "wobble": "calm"},
    },
    5: {
        "trans": "dissolve",
        "dur_tr": 0.32,
        "a": {"scale": (1.03, 1.12), "focus": ((0.50, 0.50), (0.50, 0.46)), "wobble": "calm"},
        "b": {"scale": (1.03, 1.10), "focus": ((0.50, 0.50), (0.50, 0.48)), "wobble": "calm"},
    },
    6: {
        "trans": "dissolve",
        "dur_tr": 0.35,
        "a": {"scale": (1.02, 1.08), "focus": ((0.50, 0.50), (0.50, 0.48)), "wobble": "none"},
        "b": {"scale": (1.03, 1.08), "focus": ((0.50, 0.50), (0.50, 0.48)), "wobble": "none"},
    },
}


def render_one_scene(idx: int, dur_sec: float, split_sec: float) -> Path:
    assets = EP_DIR / "assets"
    pa = assets / f"scene{idx}.jpg"
    pb = assets / f"scene{idx}_b.jpg"
    out_mp4 = assets / f"scene{idx}.mp4"
    if not pa.is_file() or not pb.is_file():
        raise FileNotFoundError(f"Thiếu {pa.name} hoặc {pb.name}")

    img_a = load_overscan(pa)
    img_b = load_overscan(pb)
    spec = SCENE_SPECS[idx]
    n_frames = max(2, int(round(dur_sec * FPS)))
    split_sec = max(0.6, min(dur_sec - 0.6, split_sec))
    tr_half = spec["dur_tr"] / 2.0

    cmd = [
        FFMPEG, "-y", "-v", "error",
        "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
        "-an", "-c:v", "libx264", "-preset", "medium", "-crf", "18",
        "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(out_mp4),
    ]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    assert proc.stdin is not None

    for fi in range(n_frames):
        t = fi / FPS
        ua = max(0.0, min(1.0, t / max(split_sec + tr_half, 1e-3)))
        ub = max(0.0, min(1.0, (t - (split_sec - tr_half)) / max(dur_sec - (split_sec - tr_half), 1e-3)))

        if t <= split_sec - tr_half:
            fr = crop_cam(img_a, ua, spec["a"]["scale"], spec["a"]["focus"], spec["a"]["wobble"], t)
            beat = "a"
        elif t >= split_sec + tr_half:
            fr = crop_cam(img_b, ub, spec["b"]["scale"], spec["b"]["focus"], spec["b"]["wobble"], t)
            beat = "b"
        else:
            p = smoothstep((t - (split_sec - tr_half)) / max(spec["dur_tr"], 1e-4))
            fa = crop_cam(img_a, ua, spec["a"]["scale"], spec["a"]["focus"], spec["a"]["wobble"], t)
            fb = crop_cam(img_b, ub, spec["b"]["scale"], spec["b"]["focus"], spec["b"]["wobble"], t)
            if spec["trans"] == "flash_white":
                base = fa if p < 0.5 else fb
                flash = 1.0 - abs(p - 0.5) * 2.0
                white = Image.new("RGB", (W, H), (255, 252, 242))
                fr = Image.blend(base, white, min(0.82, flash * 0.85))
            else:
                fr = Image.blend(fa, fb, p)
            beat = "b" if p >= 0.5 else "a"

        # Subtle EP01-style 2D anime FX overlays per scene & beat
        if idx == 1:
            fr = draw_motes(fr, t, (255, 232, 175) if beat == "a" else (255, 165, 185), count=14, seed=11)
        elif idx == 2:
            if beat == "a":
                fr = draw_danger_pulses(fr, t, W * 0.31, H * 0.58)
            elif t < split_sec + 0.45:
                # Subtle discovery impact jitter right after smash transition
                dt = t - split_sec
                jx = int(math.sin(dt * 45.0) * 10.0 * max(0.0, 1.0 - dt / 0.45))
                jy = int(math.cos(dt * 38.0) * 7.0 * max(0.0, 1.0 - dt / 0.45))
                if jx or jy:
                    shifted = Image.new("RGB", (W, H), (15, 15, 18))
                    shifted.paste(fr, (jx, jy))
                    fr = shifted
        elif idx == 3:
            if beat == "b":
                fr = draw_motes(fr, t, (150, 240, 190), count=12, seed=31)
        elif idx == 4:
            if beat == "a":
                fr = draw_whistle_waves(fr, t, W * 0.71, H * 0.50)
            else:
                fr = draw_motes(fr, t, (255, 235, 175), count=15, seed=41)
        elif idx == 5:
            if beat == "a":
                fr = draw_motes(fr, t, (255, 95, 75), count=16, seed=51)
            else:
                fr = draw_motes(fr, t, (130, 245, 180), count=16, seed=52)
        elif idx == 6:
            fr = draw_motes(fr, t, (255, 230, 165), count=16, seed=61)

        proc.stdin.write(fr.tobytes())

    proc.stdin.close()
    rc = proc.wait()
    if rc != 0:
        raise RuntimeError(f"FFmpeg lỗi khi xuất {out_mp4.name} (code {rc})")
    return out_mp4


def main() -> None:
    cfg = json.loads((EP_DIR / "episode.json").read_text(encoding="utf-8"))
    splits = cfg.get("scene_splits_sec", {})
    for i, sc in enumerate(cfg["scenes"], start=1):
        dur = float(sc["end"]) - float(sc["start"])
        sp = float(splits.get(f"scene{i}", dur * 0.5))
        out = render_one_scene(i, dur, sp)
        mb = out.stat().st_size / 1048576
        print(f" -> Đã dựng {out.name}: {dur:.2f}s ({int(round(dur * FPS))} frames @ {FPS}fps, split={sp:.2f}s) · {mb:.2f} MB")


if __name__ == "__main__":
    main()
