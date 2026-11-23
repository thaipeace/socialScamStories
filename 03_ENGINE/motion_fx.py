# -*- coding: utf-8 -*-
"""
Shared Visual Motion Engine (`03_ENGINE/motion_fx.py`) – Visual Motion Upgrade (Level 2)
với cấu hình an toàn phần cứng (Hardware Safety Profile: ThinkPad L480 · Intel i5-8250U · 8GB RAM · iGPU).

Hỗ trợ 4 cấp xử lý hình ảnh gọn nhẹ, không cài thêm thư viện ngoài Pillow + NumPy + FFmpeg:
  * Level A — Static Cinematic Motion (preset đa dạng + easing + static_hold, bỏ zoom lặp máy móc)
  * Level B — Simple 2.5D Parallax (tối đa 2–3 lớp BG/Subject/FG, blur nhẹ <= 2.0px tính 1 lần khi nạp cảnh)
  * Level C — Lightweight Object / Detail Motion (`detail_reveal`, `screen_glow` cục bộ, `light_shift` 1D LUT,
              `cursor_click`, `focus_highlight`, `detail_layer` vị trí/scale/opacity + `notifications`/`chat_bubbles`)
  * Level D — Optional Pre-rendered External Clip (tuyệt đối KHÔNG chạy AI I2V/diffusion cục bộ; luôn có fallback về ảnh tĩnh)

Các hiệu ứng nặng bị LOẠI TRỪ trên phần cứng CPU/8GB RAM:
  * Particle systems (`rain`), volumetric/full-frame shader sweeps (`shadow_drift`), heavy blur, complex masking,
    optical flow, local AI I2V / diffusion / Blender, render đồng thời nhiều cảnh, giữ toàn bộ ảnh trong RAM.

100% tương thích ngược với mọi tập cũ không khai báo `motion_upgrade` / `motion_level`.
"""
from __future__ import annotations

import gc
import json
import math
import wave
from pathlib import Path
from typing import Any

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

# ----------------------------------------------------------------------------
# Hardware Safety Limits (ThinkPad L480 · i5-8250U · 8GB RAM · iGPU)
# ----------------------------------------------------------------------------

HARDWARE_PROFILE = "low_ram_cpu_l480"
MAX_PARALLAX_LAYERS = 3         # Tối đa 2–3 lớp (BG, Subject, FG)
MAX_PARALLAX_BLUR = 2.0         # Chỉ blur rất nhẹ 1 lần lúc nạp cảnh (tránh heavy blur)
PARALLAX_OVERSAMPLE_CAP = 1.18  # Giảm bộ nhớ & CPU cho lớp 2.5D mà vẫn đủ biên dolly/pan
MAX_REVEAL_FEATHER_PX = 10      # Giới hạn feather đơn giản cho detail_reveal
MAX_GLOW_RADIUS_FRAC = 0.32     # Giới hạn screen_glow ở vùng cục bộ nhỏ (không chạy full-frame)
MAX_BREATHE_AMP_PX = 6.0        # Giới hạn biên độ thở nhẹ trên layer 2.5D (an toàn khung hình)
MAX_BREATHE_SCALE = 0.012       # Giới hạn co giãn nhịp thở nhẹ <= 1.2%

EXCLUDED_HEAVY_FX: dict[str, str] = {
    "rain": (
        "Bị loại trừ theo Hardware Safety Profile (particle system gây tốn CPU/RAM trên i5-8250U/8GB RAM) "
        "-> thay bằng ambience 'rain' + 'light_shift' (tông mát dịu) hoặc lớp ảnh tĩnh 'detail_layer'"
    ),
    "shadow_drift": (
        "Bị loại trừ theo Hardware Safety Profile (hiệu ứng volumetric/quét toàn khung mỗi frame) "
        "-> thay bằng 'light_shift' (1D LUT) hoặc 'focus_highlight' gọn nhẹ"
    ),
}

# ----------------------------------------------------------------------------
# Taxonomy & Presets (Level 2 Standard)
# ----------------------------------------------------------------------------

BEAT_TYPES: tuple[str, ...] = (
    "normal",        # Cảnh bình thường
    "establishing",  # Cảnh thiết lập bối cảnh
    "information",   # Cảnh cung cấp thông tin
    "suspicion",     # Cảnh nghi vấn
    "anomaly",       # Cảnh phát hiện dấu hiệu bất thường
    "climax",        # Cảnh cao trào
    "aftermath",     # Cảnh hậu quả
    "ending",        # Cảnh kết
)

MOTION_LEVELS: tuple[str, ...] = ("A", "B", "C", "D")

LEVEL_A_PRESETS: dict[str, dict[str, Any]] = {
    "static_hold": {
        "scale": [1.02, 1.02],
        "focus": [[0.50, 0.50], [0.50, 0.50]],
        "wobble": "none",
        "easing": "linear",
    },
    "slow_push_in": {
        "scale": [1.02, 1.09],
        "focus": [[0.50, 0.50], [0.50, 0.47]],
        "wobble": "none",
        "easing": "smoothstep",
    },
    "slow_pull_out": {
        "scale": [1.09, 1.02],
        "focus": [[0.50, 0.47], [0.50, 0.50]],
        "wobble": "none",
        "easing": "smoothstep",
    },
    "pan_left": {
        "scale": [1.08, 1.08],
        "focus": [[0.54, 0.50], [0.46, 0.50]],
        "wobble": "none",
        "easing": "smoothstep",
    },
    "pan_right": {
        "scale": [1.08, 1.08],
        "focus": [[0.46, 0.50], [0.54, 0.50]],
        "wobble": "none",
        "easing": "smoothstep",
    },
    "drift_up": {
        "scale": [1.06, 1.08],
        "focus": [[0.50, 0.53], [0.50, 0.46]],
        "wobble": "none",
        "easing": "smoothstep",
    },
    "drift_down": {
        "scale": [1.06, 1.08],
        "focus": [[0.50, 0.46], [0.50, 0.53]],
        "wobble": "none",
        "easing": "smoothstep",
    },
    "subtle_push_left": {
        "scale": [1.03, 1.10],
        "focus": [[0.50, 0.49], [0.44, 0.46]],
        "wobble": "none",
        "easing": "ease_out",
    },
    "subtle_push_right": {
        "scale": [1.03, 1.10],
        "focus": [[0.50, 0.49], [0.56, 0.46]],
        "wobble": "none",
        "easing": "ease_out",
    },
    "tense_push": {
        "scale": [1.04, 1.12],
        "focus": [[0.50, 0.49], [0.50, 0.45]],
        "wobble": "tense",
        "easing": "ease_in",
    },
    "handheld_follow": {
        "scale": [1.04, 1.09],
        "focus": [[0.48, 0.49], [0.52, 0.47]],
        "wobble": "handheld",
        "easing": "smoothstep",
    },
}

PARALLAX_CAMERA_PRESETS: dict[str, dict[str, Any]] = {
    "push_in":    {"dolly": [1.02, 1.08], "shift_x": [0.0, 0.0],    "shift_y": [0.0, -4.0]},
    "pull_out":   {"dolly": [1.08, 1.02], "shift_x": [0.0, 0.0],    "shift_y": [-4.0, 0.0]},
    "pan_right":  {"dolly": [1.05, 1.06], "shift_x": [-14.0, 14.0], "shift_y": [0.0, 0.0]},
    "pan_left":   {"dolly": [1.05, 1.06], "shift_x": [14.0, -14.0], "shift_y": [0.0, 0.0]},
    "drift_push": {"dolly": [1.03, 1.08], "shift_x": [-10.0, 10.0], "shift_y": [3.0, -4.0]},
}

ROLE_DEFAULT_DEPTH: dict[str, float] = {
    "bg": 0.35,
    "background": 0.35,
    "mid": 1.0,
    "subject": 1.0,
    "fg": 1.4,
    "foreground": 1.4,
}

# Hardware-safe lightweight Level C effects ONLY
DETAIL_FX_TYPES: tuple[str, ...] = (
    "detail_reveal",
    "eye_blink",
    "mouth_sync",
    "screen_glow",
    "light_shift",
    "cursor_click",
    "focus_highlight",
    "detail_layer",
)


# ----------------------------------------------------------------------------
# Easing & Geometry Helpers
# ----------------------------------------------------------------------------

def ease_u(u: float, easing: str = "smoothstep") -> float:
    u = max(0.0, min(1.0, float(u)))
    if easing == "linear":
        return u
    if easing == "ease_out":
        return 1.0 - (1.0 - u) ** 2.2
    if easing == "ease_in":
        return u ** 1.8
    if easing == "hold":
        return 0.0
    return u * u * (3.0 - 2.0 * u)


def fit_aspect_crop(img: Image.Image, W: int, H: int) -> Image.Image:
    if abs(img.width / max(img.height, 1) - W / H) > 0.02:
        tw = int(img.height * W / H)
        if tw <= img.width:
            x0 = (img.width - tw) // 2
            img = img.crop((x0, 0, x0 + tw, img.height))
        else:
            th = int(img.width * H / W)
            y0 = (img.height - th) // 2
            img = img.crop((0, y0, img.width, y0 + th))
    return img


def resolve_motion_params(sc: dict) -> dict[str, Any]:
    """Merge Level A preset (if specified) with explicit scene motion overrides.
    100% backward compatible: legacy scenes without preset/motion_level retain default calm wobble."""
    raw = sc.get("motion") or {}
    preset_name = raw.get("preset") or sc.get("motion_preset")
    if preset_name and preset_name in LEVEL_A_PRESETS:
        base = dict(LEVEL_A_PRESETS[preset_name])
        return {
            "scale": list(raw.get("scale", base["scale"])),
            "focus": [list(p) for p in raw.get("focus", base["focus"])],
            "wobble": raw.get("wobble", base["wobble"]),
            "easing": raw.get("easing", base["easing"]),
            "preset": preset_name,
        }
    default_wobble = "none" if sc.get("motion_level") else "calm"
    return {
        "scale": list(raw.get("scale", [1.03, 1.12])),
        "focus": [list(p) for p in raw.get("focus", [[0.5, 0.5], [0.5, 0.5]])],
        "wobble": raw.get("wobble", default_wobble),
        "easing": raw.get("easing", "smoothstep"),
        "preset": preset_name,
    }


def _fade_env(t: float, s: float, e: float, fade_in: float, fade_out: float | None = None) -> float:
    if t < s or t >= e:
        return 0.0
    fo = fade_in if fade_out is None else fade_out
    a = 1.0
    if fade_in > 1e-4:
        a = min(a, (t - s) / fade_in)
    if fo > 1e-4:
        a = min(a, (e - t) / fo)
    return max(0.0, min(1.0, a))


def _resolve_time(val: float, sc: dict, relative: bool) -> float:
    return float(sc["start"]) + float(val) if relative else float(val)


def unload_scene_runtime(sc: dict, collect: bool = False) -> None:
    """Release decoded bitmaps & video reader for a scene to keep RAM strictly bounded on 8GB machines."""
    had_heavy = bool(sc.get("_parallax") or sc.get("_vreader"))
    vr = sc.pop("_vreader", None)
    if vr is not None:
        try:
            vr.close()
        except Exception:
            pass
    sc.pop("_img", None)
    sc.pop("_parallax", None)
    sc.pop("_detail_fx", None)
    sc["_loaded"] = False
    if collect or had_heavy:
        gc.collect()


# ----------------------------------------------------------------------------
# Level B — Lightweight 2.5D Parallax (Max 2–3 Layers)
# ----------------------------------------------------------------------------

def prepare_parallax(ep, sc: dict, W: int, H: int, oversample: float) -> dict[str, Any] | None:
    """Pre-load & prepare validated 2–3 layers for lightweight Level B parallax.
    Enforces MAX_PARALLAX_LAYERS=3, MAX_PARALLAX_BLUR=2.0, PARALLAX_OVERSAMPLE_CAP=1.18.
    Returns None (graceful fallback to Level A) if layers are missing or invalid."""
    px = sc.get("parallax")
    if not px or not isinstance(px, dict):
        return None
    raw_layers = px.get("layers") or []
    if len(raw_layers) < 2:
        sc["_motion_fallback"] = "Level B cần tối thiểu 2 lớp ảnh (bg + subject) -> hạ cấp về Level A"
        return None
    if len(raw_layers) > MAX_PARALLAX_LAYERS:
        sc.setdefault("_detail_warnings", []).append(
            f"Level B giới hạn tối đa {MAX_PARALLAX_LAYERS} lớp (phần cứng 8GB RAM) -> chỉ nạp {MAX_PARALLAX_LAYERS} lớp đầu"
        )
        raw_layers = raw_layers[:MAX_PARALLAX_LAYERS]

    px_os = min(float(oversample), PARALLAX_OVERSAMPLE_CAP)
    ow, oh = int(W * px_os), int(H * px_os)
    loaded: list[dict[str, Any]] = []
    for idx, ly in enumerate(raw_layers):
        rel_p = ly.get("image")
        if not rel_p:
            sc["_motion_fallback"] = f"Layer #{idx} thiếu đường dẫn ảnh -> hạ cấp về Level A"
            return None
        p = ep.resolve_asset(rel_p)
        if not p.is_file():
            sc["_motion_fallback"] = f"Thiếu file layer 2.5D '{rel_p}' -> hạ cấp về Level A"
            return None
        role = str(ly.get("role", "bg" if idx == 0 else ("fg" if idx == len(raw_layers) - 1 else "subject"))).lower()
        mode = "RGB" if idx == 0 and role in ("bg", "background") else "RGBA"
        with Image.open(p) as raw_im:
            img = fit_aspect_crop(raw_im.convert(mode), W, H).resize((ow, oh), Image.Resampling.BILINEAR)
        blur = min(MAX_PARALLAX_BLUR, max(0.0, float(ly.get("blur", 0.0))))
        if blur > 0.1:
            img = img.filter(ImageFilter.GaussianBlur(radius=blur))
        depth = max(0.1, min(1.6, float(ly.get("depth", ROLE_DEFAULT_DEPTH.get(role, 1.0)))))
        opacity = max(0.0, min(1.0, float(ly.get("opacity", 1.0))))
        off = ly.get("offset", [0.0, 0.0])
        breathe_y = max(-MAX_BREATHE_AMP_PX, min(MAX_BREATHE_AMP_PX, float(ly.get("breathe_y", 0.0))))
        breathe_scale = max(0.0, min(MAX_BREATHE_SCALE, float(ly.get("breathe_scale", 0.0))))
        breathe_period = max(1.2, float(ly.get("breathe_period", 3.8)))
        breathe_phase = float(ly.get("breathe_phase", 0.0))
        loaded.append({
            "role": role,
            "img": img,
            "depth": depth,
            "opacity": opacity,
            "offset": (float(off[0]), float(off[1])),
            "breathe_y": breathe_y,
            "breathe_scale": breathe_scale,
            "breathe_period": breathe_period,
            "breathe_phase": breathe_phase,
        })

    cam_preset = PARALLAX_CAMERA_PRESETS.get(str(px.get("camera", "push_in")), PARALLAX_CAMERA_PRESETS["push_in"])
    dolly = list(px.get("dolly", cam_preset["dolly"]))
    shift_x = list(px.get("shift_x", cam_preset["shift_x"]))
    shift_y = list(px.get("shift_y", cam_preset["shift_y"]))
    strength = max(0.0, min(1.25, float(px.get("strength", 1.0))))
    easing = str(px.get("easing", "smoothstep"))
    focus = px.get("focus", [0.5, 0.5])

    max_depth = max(ly["depth"] for ly in loaded)
    max_by = max(abs(ly["breathe_y"]) for ly in loaded)
    max_sx = max(abs(float(shift_x[0])), abs(float(shift_x[1]))) * max_depth * strength
    max_sy = max(abs(float(shift_y[0])), abs(float(shift_y[1]))) * max_depth * strength + max_by
    need_scale = max(
        1.02,
        1.0 / max(0.80, 1.0 - 2.0 * (max_sx / W) - 0.01),
        1.0 / max(0.80, 1.0 - 2.0 * (max_sy / H) - 0.01),
    )
    d0 = max(float(dolly[0]), need_scale)
    d1 = max(float(dolly[1]), need_scale)

    return {
        "layers": loaded,
        "dolly": (d0, d1),
        "shift_x": (float(shift_x[0]), float(shift_x[1])),
        "shift_y": (float(shift_y[0]), float(shift_y[1])),
        "strength": strength,
        "easing": easing,
        "focus": (float(focus[0]), float(focus[1])),
        "oversample": px_os,
    }


def _transform_layer(src: Image.Image, W: int, H: int, scale: float, fx: float, fy: float,
                     dx: float, dy: float) -> Image.Image:
    sw, sh = src.size
    cw, ch = sw / max(scale, 1.001), sh / max(scale, 1.001)
    left = max(0.0, min(sw - cw, fx * sw + dx - cw * 0.5))
    top = max(0.0, min(sh - ch, fy * sh + dy - ch * 0.5))
    return src.transform((W, H), Image.Transform.EXTENT, (left, top, left + cw, top + ch),
                         resample=Image.Resampling.BILINEAR)


def render_parallax_frame(px_rt: dict[str, Any], sc: dict, t: float, W: int, H: int,
                          extra_dx: float = 0.0, extra_dy: float = 0.0,
                          fx_list: list[dict[str, Any]] | None = None) -> Image.Image:
    """Composite 2–3 depth layers with differential dolly, lateral shift, subtle breathing, and layer-locked FX."""
    s, e = sc["start"], sc["end"]
    lt = max(0.0, t - s)
    lin_u = (max(s, min(e, t)) - s) / max(e - s, 1e-4)
    u = ease_u(lin_u, px_rt["easing"])
    d0, d1 = px_rt["dolly"]
    d_min = min(d0, d1)
    d_cur = d0 + (d1 - d0) * u
    excess = max(0.0, d_cur - d_min)
    sx0, sx1 = px_rt["shift_x"]
    sy0, sy1 = px_rt["shift_y"]
    cur_sx = sx0 + (sx1 - sx0) * u
    cur_sy = sy0 + (sy1 - sy0) * u
    strength = px_rt["strength"]
    fx, fy = px_rt["focus"]
    os_mul = px_rt["oversample"]

    out: Image.Image | None = None
    for idx, ly in enumerate(px_rt["layers"]):
        depth = ly["depth"]
        depth_scale_mul = 0.40 + 0.60 * depth
        sc_l = max(1.01, d_min + excess * depth_scale_mul * strength)
        dx_l = (cur_sx * depth * strength + ly["offset"][0]) * os_mul + extra_dx * depth_scale_mul
        dy_l = (cur_sy * depth * strength + ly["offset"][1]) * os_mul + extra_dy * depth_scale_mul
        if ly["breathe_y"] or ly["breathe_scale"]:
            b_wave = math.sin(2.0 * math.pi * lt / ly["breathe_period"] + ly["breathe_phase"])
            dy_l += ly["breathe_y"] * b_wave * os_mul
            sc_l *= 1.0 + ly["breathe_scale"] * (0.5 + 0.5 * b_wave)

        layer_src = ly["img"]
        if fx_list:
            role = ly["role"]
            layer_fx = [
                f for f in fx_list
                if f.get("_stage") == "pre_camera"
                and (f.get("_layer") == role or f.get("_layer") == idx)
            ]
            if layer_fx:
                layer_src = apply_pre_camera_fx(layer_src, layer_fx, t)

        warped = _transform_layer(layer_src, W, H, sc_l, fx, fy, dx_l, dy_l)
        if out is None:
            out = warped.convert("RGB") if warped.mode != "RGB" else warped
        else:
            rgba = warped if warped.mode == "RGBA" else warped.convert("RGBA")
            al = rgba.getchannel("A")
            if ly["opacity"] < 0.99:
                op = ly["opacity"]
                al = al.point(lambda p, o=op: int(p * o))
            out.paste(rgba, (0, 0), al)
    return out if out is not None else Image.new("RGB", (W, H))


# ----------------------------------------------------------------------------
# Level C — Lightweight Object / Detail Motion
# ----------------------------------------------------------------------------

def _make_radial_glow(bw: int, bh: int, color: tuple[int, int, int]) -> np.ndarray:
    """Pre-compute smooth elliptical glow mask (bh, bw, 3) in [0, 1] for fast ROI screen-blend."""
    yy = np.linspace(-1.0, 1.0, max(1, bh), dtype=np.float32)[:, None]
    xx = np.linspace(-1.0, 1.0, max(1, bw), dtype=np.float32)[None, :]
    r2 = xx * xx + yy * yy
    falloff = np.exp(-r2 * 2.8) * np.clip(1.0 - r2, 0.0, 1.0)
    col = np.array(color, dtype=np.float32) / 255.0
    return falloff[:, :, None] * col[None, None, :]


def _make_focus_mask(W: int, H: int, cx: float, cy: float, rx: float, ry: float) -> Image.Image:
    """Pre-compute lightweight low-res radial mask (0 inside focus, 255 outside focus)."""
    lw, lh = max(48, W // 6), max(48, H // 6)
    yy = (np.linspace(0.0, 1.0, lh, dtype=np.float32)[:, None] - cy) / max(ry, 0.08)
    xx = (np.linspace(0.0, 1.0, lw, dtype=np.float32)[None, :] - cx) / max(rx, 0.08)
    dist = np.sqrt(xx * xx + yy * yy)
    outer = np.clip((dist - 0.65) / 0.85, 0.0, 1.0)
    outer = outer * outer * (3.0 - 2.0 * outer)
    m = Image.fromarray((outer * 255.0).astype(np.uint8), mode="L")
    return m.resize((W, H), Image.Resampling.BILINEAR)


def _make_roi_patch(ep, img_ref: str, region: list[float], feather_frac: float,
                    W: int, H: int, tw: int, th: int, shape: str = "rounded") -> tuple[tuple[int, int, int, int], Image.Image, Image.Image] | None:
    """Load an image, extract ONLY a tiny feathered ROI patch at (tw, th), and immediately release full bitmap."""
    p = ep.resolve_asset(img_ref)
    if not p.is_file():
        return None
    x0, y0, x1, y1 = [max(0.0, min(1.0, float(v))) for v in region]
    px0, py0, px1, py1 = int(x0 * tw), int(y0 * th), int(x1 * tw), int(y1 * th)
    if px1 <= px0 + 2 or py1 <= py0 + 2:
        return None
    feather = max(2, min(MAX_REVEAL_FEATHER_PX, int(float(feather_frac) * min(tw, th))))
    bx0, by0 = max(0, px0 - feather * 2), max(0, py0 - feather * 2)
    bx1, by1 = min(tw, px1 + feather * 2), min(th, py1 + feather * 2)
    with Image.open(p) as raw_im:
        timg = fit_aspect_crop(raw_im.convert("RGB"), W, H).resize((tw, th), Image.Resampling.BILINEAR)
        roi_img = timg.crop((bx0, by0, bx1, by1))
        del timg
    mask = Image.new("L", (bx1 - bx0, by1 - by0), 0)
    drw = ImageDraw.Draw(mask)
    if shape == "ellipse":
        drw.ellipse([px0 - bx0, py0 - by0, px1 - bx0, py1 - by0], fill=255)
    else:
        drw.rounded_rectangle([px0 - bx0, py0 - by0, px1 - bx0, py1 - by0], radius=max(4, feather), fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(radius=feather))
    return (bx0, by0, bx1, by1), roi_img, mask


def _compute_mouth_timeline(ep, sc: dict, speaker: str | None, line_ids: list[str] | None,
                            fps: int, thresh_mid: float, thresh_open: float) -> np.ndarray:
    """Compute lightweight anime-cadence lip-sync states (0=closed, 1=mid, 2=open) directly from real TTS WAVs."""
    s_sc, e_sc = float(sc["start"]), float(sc["end"])
    n_steps = max(1, int(math.ceil(max(0.1, e_sc - s_sc) * fps)) + 1)
    states = np.zeros(n_steps, dtype=np.uint8)
    tts_p = getattr(ep, "tts_manifest_path", None)
    if not tts_p or not Path(tts_p).is_file():
        return states
    try:
        tts = json.loads(Path(tts_p).read_text(encoding="utf-8"))
    except Exception:
        return states

    wanted_ids = set(line_ids) if line_ids else None
    for ln in tts.get("lines", []):
        if wanted_ids is not None and ln.get("line_id") not in wanted_ids:
            continue
        if speaker and ln.get("speaker") != speaker:
            continue
        ls = float(ln.get("timeline_start_sec", 0.0))
        le = float(ln.get("timeline_end_sec", ls))
        if le <= s_sc or ls >= e_sc:
            continue
        wp = ep.resolve_asset(ln.get("wav_path", "")) if ln.get("wav_path") else None
        if not wp or not wp.is_file():
            wp = ep.tts_dir / f"{ln.get('line_id', '')}.wav"
        if not wp.is_file():
            continue
        try:
            with wave.open(str(wp), "rb") as wf:
                sr = wf.getframerate()
                nch = wf.getnchannels()
                raw = wf.readframes(wf.getnframes())
            samples = np.frombuffer(raw, dtype=np.int16).astype(np.float32) / 32768.0
            if nch > 1:
                samples = samples.reshape(-1, nch).mean(axis=1)
        except Exception:
            continue
        if samples.size < 64:
            continue

        hop = max(1, int(round(sr / float(fps))))
        n_win = max(1, samples.size // hop)
        trimmed = samples[: n_win * hop].reshape(n_win, hop)
        rms = np.sqrt(np.mean(trimmed * trimmed, axis=1) + 1e-10)
        active = rms[rms > 0.012]
        ref = float(np.percentile(active, 86)) if active.size >= 3 else max(float(rms.max()), 0.05)
        norm = rms / max(ref, 1e-4)

        run_open = 0
        for wi in range(n_win):
            t_cur = ls + (wi + 0.5) / float(fps)
            if t_cur < s_sc or t_cur >= e_sc:
                continue
            si = int((t_cur - s_sc) * fps)
            if not (0 <= si < n_steps):
                continue
            v = float(norm[wi])
            if v >= thresh_open:
                run_open += 1
                # Organic anime articulation: avoid frozen jaw on long steady vowels
                st = 1 if (run_open % 4 == 0) else 2
            elif v >= thresh_mid:
                run_open = 0
                st = 1
            else:
                run_open = 0
                st = 0
            if st > states[si]:
                states[si] = st
    return states


def prepare_detail_fx(ep, sc: dict, W: int, H: int, oversample: float) -> list[dict[str, Any]]:
    """Pre-load and prepare hardware-safe Level C detail FX for the currently active scene."""
    raw_list = sc.get("detail_fx") or []
    if not raw_list:
        return []
    ow, oh = int(W * oversample), int(H * oversample)
    px_os = min(float(oversample), PARALLAX_OVERSAMPLE_CAP)
    px_ow, px_oh = int(W * px_os), int(H * px_os)
    has_px = bool(sc.get("parallax"))
    prepared: list[dict[str, Any]] = []

    for idx, fx in enumerate(raw_list):
        if not isinstance(fx, dict):
            continue
        ftype = str(fx.get("type", "")).strip().lower()
        if ftype in EXCLUDED_HEAVY_FX:
            sc.setdefault("_detail_warnings", []).append(f"Bỏ qua '{ftype}': {EXCLUDED_HEAVY_FX[ftype]}")
            continue
        if ftype not in DETAIL_FX_TYPES:
            continue
        rel_time = bool(fx.get("relative", False))
        item: dict[str, Any] = dict(fx)
        item["type"] = ftype
        item["_idx"] = idx
        target_layer = fx.get("layer")
        item["_layer"] = str(target_layer).lower() if isinstance(target_layer, str) else target_layer
        tw_pre, th_pre = (px_ow, px_oh) if (has_px and item["_layer"] is not None) else (ow, oh)

        if ftype == "detail_reveal":
            img_ref = fx.get("image")
            if not img_ref:
                continue
            p = ep.resolve_asset(img_ref)
            if not p.is_file():
                sc.setdefault("_detail_warnings", []).append(f"Thiếu ảnh detail_reveal '{img_ref}' -> bỏ qua hiệu ứng")
                continue
            item["_at"] = _resolve_time(fx.get("at", sc["start"]), sc, rel_time)
            item["_dur"] = max(0.05, float(fx.get("dur", 0.35)))
            item["_revert_at"] = _resolve_time(fx["revert_at"], sc, rel_time) if fx.get("revert_at") is not None else None
            item["_revert_dur"] = max(0.05, float(fx.get("revert_dur", item["_dur"])))
            region = fx.get("region")
            if region and len(region) == 4:
                patch = _make_roi_patch(ep, img_ref, region, float(fx.get("feather", 0.015)), W, H, tw_pre, th_pre, "rounded")
                if patch is None:
                    continue
                item["_roi_box"], item["_roi_img"], item["_roi_mask"] = patch
            else:
                with Image.open(p) as raw_im:
                    item["_full_img"] = fit_aspect_crop(raw_im.convert("RGB"), W, H).resize((tw_pre, th_pre), Image.Resampling.BILINEAR)
            item["_stage"] = "pre_camera"
            prepared.append(item)

        elif ftype == "eye_blink":
            img_ref = fx.get("image")
            region = fx.get("region")
            if not img_ref or not (region and len(region) == 4):
                sc.setdefault("_detail_warnings", []).append("eye_blink cần 'image' và 'region' [x0,y0,x1,y1] -> bỏ qua")
                continue
            patch = _make_roi_patch(ep, img_ref, region, float(fx.get("feather", 0.010)), W, H, tw_pre, th_pre, "ellipse")
            if patch is None:
                sc.setdefault("_detail_warnings", []).append(f"Thiếu ảnh eye_blink '{img_ref}' -> bỏ qua hiệu ứng")
                continue
            item["_roi_box"], item["_roi_img"], item["_roi_mask"] = patch
            item["_close_dur"] = max(0.03, float(fx.get("close_dur", 0.055)))
            item["_hold_dur"] = max(0.02, float(fx.get("hold_dur", 0.045)))
            item["_open_dur"] = max(0.04, float(fx.get("open_dur", 0.085)))
            raw_times = fx.get("times")
            if raw_times:
                btimes = sorted(_resolve_time(bt, sc, rel_time) for bt in raw_times)
            else:
                interval = max(1.8, float(fx.get("interval", 3.6)))
                t_cur = float(sc["start"]) + float(fx.get("first_offset", 1.35))
                btimes = []
                k = 0
                while t_cur < float(sc["end"]) - 0.45:
                    btimes.append(round(t_cur, 3))
                    jitter = ((k * 37) % 11 - 5) * 0.09
                    t_cur += max(1.8, interval + jitter)
                    k += 1
            item["_blink_times"] = btimes
            item["_stage"] = "pre_camera"
            prepared.append(item)

        elif ftype == "mouth_sync":
            open_ref = fx.get("open_image") or fx.get("image")
            region = fx.get("region")
            if not open_ref or not (region and len(region) == 4):
                sc.setdefault("_detail_warnings", []).append("mouth_sync cần 'open_image' và 'region' [x0,y0,x1,y1] -> bỏ qua")
                continue
            feather_f = float(fx.get("feather", 0.010))
            p_open = _make_roi_patch(ep, open_ref, region, feather_f, W, H, tw_pre, th_pre, "ellipse")
            if p_open is None:
                sc.setdefault("_detail_warnings", []).append(f"Thiếu ảnh mouth_sync '{open_ref}' -> bỏ qua hiệu ứng")
                continue
            item["_roi_box"], item["_open_img"], item["_roi_mask"] = p_open
            closed_ref = fx.get("closed_image")
            mid_ref = fx.get("mid_image")
            if closed_ref:
                p_cl = _make_roi_patch(ep, closed_ref, region, feather_f, W, H, tw_pre, th_pre, "ellipse")
                if p_cl is not None:
                    item["_closed_img"] = p_cl[1]
            if mid_ref:
                p_md = _make_roi_patch(ep, mid_ref, region, feather_f, W, H, tw_pre, th_pre, "ellipse")
                if p_md is not None:
                    item["_mid_img"] = p_md[1]
            mfps = max(6, min(20, int(fx.get("fps", 12))))
            item["_fps"] = mfps
            item["_sc_start"] = float(sc["start"])
            item["_states"] = _compute_mouth_timeline(
                ep, sc,
                speaker=fx.get("speaker"),
                line_ids=fx.get("line_ids"),
                fps=mfps,
                thresh_mid=float(fx.get("thresh_mid", 0.16)),
                thresh_open=float(fx.get("thresh_open", 0.46)),
            )
            item["_stage"] = "pre_camera"
            prepared.append(item)

        elif ftype == "screen_glow":
            space = str(fx.get("space", "scene")).lower()
            tw, th = (ow, oh) if space == "scene" else (W, H)
            pos = fx.get("pos", [0.5, 0.55])
            rad = fx.get("radius", [0.22, 0.22])
            rfx = min(MAX_GLOW_RADIUS_FRAC, max(0.04, float(rad[0])))
            rfy = min(MAX_GLOW_RADIUS_FRAC, max(0.04, float(rad[1])))
            cx, cy = int(float(pos[0]) * tw), int(float(pos[1]) * th)
            rx, ry = max(12, int(rfx * tw)), max(12, int(rfy * th))
            x0, y0 = max(0, cx - rx), max(0, cy - ry)
            x1, y1 = min(tw, cx + rx), min(th, cy + ry)
            if x1 <= x0 or y1 <= y0:
                continue
            col = tuple(int(c) for c in fx.get("color", [130, 195, 255]))
            item["_box"] = (x0, y0, x1, y1)
            item["_glow"] = _make_radial_glow(x1 - x0, y1 - y0, col)
            item["_start"] = _resolve_time(fx.get("start", sc["start"]), sc, rel_time)
            item["_end"] = _resolve_time(fx.get("end", sc["end"]), sc, rel_time)
            item["_fade"] = max(0.05, float(fx.get("fade", 0.35)))
            item["_intensity"] = max(0.0, min(0.80, float(fx.get("intensity", 0.36))))
            item["_mode"] = str(fx.get("mode", "turn_on")).lower()
            item["_stage"] = "pre_camera" if space == "scene" else "post_camera"
            prepared.append(item)

        elif ftype == "light_shift":
            item["_at"] = _resolve_time(fx.get("at", sc["start"]), sc, rel_time)
            item["_dur"] = max(0.04, float(fx.get("dur", 0.25)))
            item["_end"] = _resolve_time(fx["end"], sc, rel_time) if fx.get("end") is not None else None
            item["_end_dur"] = max(0.04, float(fx.get("end_dur", item["_dur"])))
            item["_brightness"] = max(0.45, min(1.45, float(fx.get("brightness", 1.16))))
            item["_tint_rgb"] = tuple(int(c) for c in fx["tint_rgb"]) if fx.get("tint_rgb") else None
            item["_tint_strength"] = max(0.0, min(0.35, float(fx.get("tint_strength", 0.12))))
            item["_stage"] = "post_camera"
            prepared.append(item)

        elif ftype == "cursor_click":
            item["_start"] = _resolve_time(fx.get("start", sc["start"] + 0.4), sc, rel_time)
            item["_click_at"] = _resolve_time(fx.get("click_at", item["_start"] + 1.0), sc, rel_time)
            item["_end"] = _resolve_time(fx.get("end", item["_click_at"] + 0.9), sc, rel_time)
            item["_from"] = tuple(float(v) for v in fx.get("from", [0.65, 0.72]))
            item["_to"] = tuple(float(v) for v in fx.get("to", [0.50, 0.54]))
            item["_scale"] = max(0.6, min(2.0, float(fx.get("scale", 1.0))))
            item["_ripple_rgb"] = tuple(int(c) for c in fx.get("ripple_rgb", [255, 220, 110]))
            item["_stage"] = "post_camera"
            prepared.append(item)

        elif ftype == "focus_highlight":
            pos = fx.get("pos", [0.5, 0.5])
            rad = fx.get("radius", [0.26, 0.26])
            item["_mask"] = _make_focus_mask(W, H, float(pos[0]), float(pos[1]), float(rad[0]), float(rad[1]))
            item["_start"] = _resolve_time(fx.get("start", sc["start"]), sc, rel_time)
            item["_end"] = _resolve_time(fx.get("end", sc["end"]), sc, rel_time)
            item["_fade"] = max(0.05, float(fx.get("fade", 0.4)))
            item["_dim_outer"] = max(0.0, min(0.50, float(fx.get("dim_outer", 0.26))))
            item["_stage"] = "post_camera"
            prepared.append(item)

        elif ftype == "detail_layer":
            img_ref = fx.get("image")
            if not img_ref:
                continue
            p = ep.resolve_asset(img_ref)
            if not p.is_file():
                sc.setdefault("_detail_warnings", []).append(f"Thiếu ảnh detail_layer '{img_ref}' -> bỏ qua hiệu ứng")
                continue
            with Image.open(p) as raw_im:
                item["_img"] = raw_im.convert("RGBA")
            item["_start"] = _resolve_time(fx.get("start", sc["start"]), sc, rel_time)
            item["_end"] = _resolve_time(fx.get("end", sc["end"]), sc, rel_time)
            item["_fade"] = max(0.0, float(fx.get("fade", 0.25)))
            item["_from_pos"] = tuple(float(v) for v in fx.get("from_pos", [0.5, 0.55]))
            item["_to_pos"] = tuple(float(v) for v in fx.get("to_pos", item["_from_pos"]))
            sc_pair = fx.get("scale", [1.0, 1.0])
            item["_scale"] = (float(sc_pair[0]), float(sc_pair[1])) if isinstance(sc_pair, (list, tuple)) else (float(sc_pair), float(sc_pair))
            item["_opacity"] = max(0.0, min(1.0, float(fx.get("opacity", 1.0))))
            item["_easing"] = str(fx.get("easing", "ease_out"))
            item["_stage"] = "post_camera"
            prepared.append(item)

    return prepared


def _apply_screen_glow_roi(img: Image.Image, fx: dict[str, Any], t: float) -> Image.Image:
    s, e = fx["_start"], fx["_end"]
    env = _fade_env(t, s, e, fx["_fade"])
    if env <= 0.005:
        return img
    mode = fx["_mode"]
    dt = t - s
    mod = 1.0
    if mode == "pulse":
        mod = 0.65 + 0.35 * (0.5 + 0.5 * math.sin(2.0 * math.pi * 0.85 * dt))
    elif mode == "flicker":
        mod = 0.72 + 0.28 * (0.5 + 0.5 * math.sin(2.0 * math.pi * 6.5 * dt + math.sin(dt * 17.0)))
    elif mode == "turn_on":
        mod = ease_u(min(1.0, dt / max(fx["_fade"], 0.12)), "ease_out")
    k = fx["_intensity"] * env * mod
    if k <= 0.004:
        return img

    out = img.copy()
    x0, y0, x1, y1 = fx["_box"]
    roi = np.asarray(out.crop((x0, y0, x1, y1)), dtype=np.float32) * (1.0 / 255.0)
    glow = np.clip(fx["_glow"] * k, 0.0, 0.92)
    blended = 1.0 - (1.0 - roi) * (1.0 - glow)
    out.paste(Image.fromarray(np.clip(blended * 255.0, 0, 255).astype(np.uint8), mode="RGB"), (x0, y0))
    return out


def _paste_roi_preserve_alpha(img: Image.Image, roi_img: Image.Image, mask: Image.Image,
                              box: tuple[int, int, int, int], alpha: float) -> None:
    """Paste RGB ROI onto RGB or RGBA image while strictly preserving original RGBA transparency."""
    if alpha <= 0.004:
        return
    m = mask if alpha >= 0.995 else mask.point(lambda p, a=alpha: int(p * a))
    bx0, by0 = box[0], box[1]
    if img.mode == "RGBA":
        orig_a = img.crop(box).getchannel("A")
        img.paste(roi_img, (bx0, by0), m)
        patched = img.crop(box)
        patched.putalpha(orig_a)
        img.paste(patched, (bx0, by0))
    else:
        img.paste(roi_img, (bx0, by0), m)


def apply_pre_camera_fx(base_img: Image.Image, fx_list: list[dict[str, Any]], t: float) -> Image.Image:
    """Apply scene-space Level C effects BEFORE camera transform so they stay 100% camera-locked."""
    img = base_img
    copied = False
    for fx in fx_list:
        if fx.get("_stage") != "pre_camera":
            continue
        ftype = fx["type"]
        if ftype == "detail_reveal":
            at, dur = fx["_at"], fx["_dur"]
            if t < at:
                continue
            alpha = ease_u((t - at) / dur, "smoothstep")
            rev = fx["_revert_at"]
            if rev is not None and t >= rev:
                alpha *= 1.0 - ease_u((t - rev) / fx["_revert_dur"], "smoothstep")
            if alpha <= 0.004:
                continue
            if "_roi_box" in fx:
                if not copied:
                    img = img.copy()
                    copied = True
                _paste_roi_preserve_alpha(img, fx["_roi_img"], fx["_roi_mask"], fx["_roi_box"], alpha)
            else:
                if alpha >= 0.995:
                    img = fx["_full_img"]
                    copied = False
                else:
                    img = Image.blend(img, fx["_full_img"], alpha)
                    copied = True

        elif ftype == "eye_blink":
            c_dur, h_dur, o_dur = fx["_close_dur"], fx["_hold_dur"], fx["_open_dur"]
            tot = c_dur + h_dur + o_dur
            alpha = 0.0
            for bt in fx["_blink_times"]:
                dt = t - bt
                if 0.0 <= dt <= tot:
                    if dt < c_dur:
                        alpha = ease_u(dt / c_dur, "ease_in")
                    elif dt < c_dur + h_dur:
                        alpha = 1.0
                    else:
                        alpha = 1.0 - ease_u((dt - c_dur - h_dur) / o_dur, "ease_out")
                    break
            if alpha > 0.004:
                if not copied:
                    img = img.copy()
                    copied = True
                _paste_roi_preserve_alpha(img, fx["_roi_img"], fx["_roi_mask"], fx["_roi_box"], alpha)

        elif ftype == "mouth_sync":
            states = fx["_states"]
            mfps = fx["_fps"]
            fpos = (t - fx["_sc_start"]) * mfps
            if fpos < 0.0:
                st = 0
            else:
                si = min(len(states) - 1, int(fpos))
                st = int(states[si])
            patch_img = None
            patch_alpha = 1.0
            if st == 0:
                patch_img = fx.get("_closed_img")
            elif st == 1:
                if "_mid_img" in fx:
                    patch_img = fx["_mid_img"]
                else:
                    patch_img = fx["_open_img"]
                    patch_alpha = 0.52
            else:
                patch_img = fx["_open_img"]
            if patch_img is not None:
                if not copied:
                    img = img.copy()
                    copied = True
                _paste_roi_preserve_alpha(img, patch_img, fx["_roi_mask"], fx["_roi_box"], patch_alpha)

        elif ftype == "screen_glow":
            img = _apply_screen_glow_roi(img, fx, t)
            copied = True
    return img


def _apply_light_shift(frame: Image.Image, fx: dict[str, Any], t: float) -> Image.Image:
    at, dur = fx["_at"], fx["_dur"]
    if t < at:
        return frame
    u = ease_u((t - at) / dur, "smoothstep")
    end_t = fx["_end"]
    if end_t is not None and t >= end_t:
        u *= 1.0 - ease_u((t - end_t) / fx["_end_dur"], "smoothstep")
    if u <= 0.005:
        return frame
    br = 1.0 + (fx["_brightness"] - 1.0) * u
    tint = fx["_tint_rgb"]
    ts = fx["_tint_strength"] * u if tint else 0.0
    if abs(br - 1.0) < 0.005 and ts < 0.004:
        return frame
    lut: list[int] = []
    for ch in range(3):
        t_val = tint[ch] if tint else 0
        for v in range(256):
            val = v * br
            if ts > 0.0:
                val = val * (1.0 - ts) + t_val * ts
            lut.append(max(0, min(255, int(round(val)))))
    return frame.point(lut)


def _apply_cursor_click(frame: Image.Image, fx: dict[str, Any], t: float, W: int, H: int) -> Image.Image:
    s, click_t, e = fx["_start"], fx["_click_at"], fx["_end"]
    if t < s or t >= e:
        return frame
    fade = _fade_env(t, s, e, 0.16, 0.22)
    if fade <= 0.01:
        return frame

    move_dur = max(0.08, click_t - s)
    u = ease_u((t - s) / move_dur, "ease_out") if t < click_t else 1.0
    fx0, fy0 = fx["_from"]
    fx1, fy1 = fx["_to"]
    cx = (fx0 + (fx1 - fx0) * u) * W
    cy = (fy0 + (fy1 - fy0) * u) * H

    sc = fx["_scale"] * (min(W, H) / 1080.0)
    dt_click = t - click_t
    press = 0.88 if (0.0 <= dt_click <= 0.12) else 1.0
    cur_sz = 38.0 * sc * press

    pad = int(round(86 * sc))
    x0 = max(0, int(cx) - pad)
    y0 = max(0, int(cy) - pad)
    x1 = min(W, int(cx) + pad)
    y1 = min(H, int(cy) + pad)
    if x1 <= x0 or y1 <= y0:
        return frame

    ov = Image.new("RGBA", (x1 - x0, y1 - y0), (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)
    lx, ly = cx - x0, cy - y0

    if 0.0 <= dt_click <= 0.48:
        rp = dt_click / 0.48
        r = (8.0 + ease_u(rp, "ease_out") * 44.0) * sc
        ra = int((1.0 - rp) * 195 * fade)
        if ra > 6:
            d.ellipse([lx - r, ly - r, lx + r, ly + r], outline=(*fx["_ripple_rgb"], ra), width=max(2, int(3 * sc)))

    pts = [
        (lx, ly),
        (lx, ly + cur_sz),
        (lx + cur_sz * 0.28, ly + cur_sz * 0.74),
        (lx + cur_sz * 0.48, ly + cur_sz * 1.05),
        (lx + cur_sz * 0.63, ly + cur_sz * 0.97),
        (lx + cur_sz * 0.43, ly + cur_sz * 0.67),
        (lx + cur_sz * 0.76, ly + cur_sz * 0.67),
    ]
    sh_pts = [(px + 2, py + 3) for px, py in pts]
    d.polygon(sh_pts, fill=(0, 0, 0, int(110 * fade)))
    d.polygon(pts, fill=(250, 252, 255, int(245 * fade)), outline=(18, 22, 30, int(245 * fade)))

    out = frame.copy()
    out.paste(ov, (x0, y0), ov.getchannel("A"))
    return out


def _apply_focus_highlight(frame: Image.Image, fx: dict[str, Any], t: float) -> Image.Image:
    """Zero-extra-RGB-buffer peripheral dim using constant-color paste + precomputed L mask."""
    env = _fade_env(t, fx["_start"], fx["_end"], fx["_fade"])
    if env <= 0.01:
        return frame
    dim = fx["_dim_outer"] * env
    if dim <= 0.005:
        return frame
    mask = fx["_mask"]
    if dim < 0.99:
        mask = mask.point(lambda p, d_=dim: int(p * d_))
    out = frame.copy()
    out.paste((8, 10, 16), (0, 0, out.width, out.height), mask)
    return out


def _apply_detail_layer(frame: Image.Image, fx: dict[str, Any], t: float, W: int, H: int) -> Image.Image:
    s, e = fx["_start"], fx["_end"]
    env = _fade_env(t, s, e, fx["_fade"])
    if env <= 0.01:
        return frame
    u = ease_u((t - s) / max(e - s, 1e-4), fx["_easing"])
    px0, py0 = fx["_from_pos"]
    px1, py1 = fx["_to_pos"]
    cx = (px0 + (px1 - px0) * u) * W
    cy = (py0 + (py1 - py0) * u) * H
    s0, s1 = fx["_scale"]
    sc = s0 + (s1 - s0) * u
    src: Image.Image = fx["_img"]
    nw, nh = max(2, int(round(src.width * sc))), max(2, int(round(src.height * sc)))
    placed = src.resize((nw, nh), Image.Resampling.BILINEAR) if (nw != src.width or nh != src.height) else src
    al = placed.getchannel("A")
    op = fx["_opacity"] * env
    if op < 0.99:
        al = al.point(lambda p, o=op: int(p * o))
    out = frame.copy()
    out.paste(placed, (int(round(cx - nw / 2)), int(round(cy - nh / 2))), al)
    return out


def apply_post_camera_fx(frame: Image.Image, fx_list: list[dict[str, Any]], t: float, W: int, H: int) -> Image.Image:
    """Apply lightweight frame-space Level C effects AFTER camera transform."""
    out = frame
    for fx in fx_list:
        if fx.get("_stage") != "post_camera":
            continue
        ftype = fx["type"]
        if ftype == "screen_glow":
            out = _apply_screen_glow_roi(out, fx, t)
        elif ftype == "light_shift":
            out = _apply_light_shift(out, fx, t)
        elif ftype == "focus_highlight":
            out = _apply_focus_highlight(out, fx, t)
        elif ftype == "detail_layer":
            out = _apply_detail_layer(out, fx, t, W, H)
        elif ftype == "cursor_click":
            out = _apply_cursor_click(out, fx, t, W, H)
    return out


def collect_fx_qa_timestamps(scenes: list[dict]) -> list[float]:
    """Compute QA highlight timestamps directly from scene metadata (no decoded bitmaps required)."""
    pts: list[float] = []
    for sc in scenes:
        s, e = float(sc["start"]), float(sc["end"])
        for fx in sc.get("detail_fx") or []:
            if not isinstance(fx, dict):
                continue
            ft = str(fx.get("type", "")).lower()
            if ft not in DETAIL_FX_TYPES:
                continue
            rel_t = bool(fx.get("relative", False))
            if ft == "detail_reveal":
                at = _resolve_time(fx.get("at", s), sc, rel_t)
                dur = max(0.05, float(fx.get("dur", 0.35)))
                pts.append(min(e - 0.1, at + dur + 0.15))
            elif ft == "cursor_click":
                st = _resolve_time(fx.get("start", s + 0.4), sc, rel_t)
                ct = _resolve_time(fx.get("click_at", st + 1.0), sc, rel_t)
                pts.append(min(e - 0.08, ct + 0.08))
            elif ft == "screen_glow":
                st = _resolve_time(fx.get("start", s), sc, rel_t)
                fd = max(0.05, float(fx.get("fade", 0.35)))
                pts.append(min(e - 0.1, st + fd + 0.2))
            elif ft == "light_shift":
                at = _resolve_time(fx.get("at", s), sc, rel_t)
                dur = max(0.04, float(fx.get("dur", 0.25)))
                pts.append(min(e - 0.1, at + dur + 0.15))
    return [round(p, 2) for p in pts if p > 0]


# ----------------------------------------------------------------------------
# Visual Motion Plan Audit (Gate 0, `motion-check`, Gate 5 QC)
# ----------------------------------------------------------------------------

def classify_camera_pattern(sc: dict) -> str:
    if sc.get("video") and sc.get("video_enabled", True):
        return "video_clip"
    if sc.get("parallax") and len((sc["parallax"] or {}).get("layers", [])) >= 2:
        return f"parallax_{sc['parallax'].get('camera', 'push_in')}"
    mp = resolve_motion_params(sc)
    s0, s1 = float(mp["scale"][0]), float(mp["scale"][1])
    (fx0, fy0), (fx1, fy1) = mp["focus"]
    ds = s1 - s0
    dfx, dfy = fx1 - fx0, fy1 - fy0
    if abs(ds) < 0.012 and abs(dfx) < 0.015 and abs(dfy) < 0.015:
        return "static_hold"
    if abs(ds) < 0.015:
        if abs(dfx) >= abs(dfy):
            return "pan_right" if dfx > 0 else "pan_left"
        return "drift_down" if dfy > 0 else "drift_up"
    return "push_in" if ds > 0 else "pull_out"


def infer_motion_level(sc: dict) -> str:
    explicit = str(sc.get("motion_level", "")).strip().upper()
    if explicit in MOTION_LEVELS:
        return explicit
    if sc.get("video") and sc.get("video_enabled", True):
        return "D"
    if sc.get("parallax") and len((sc["parallax"] or {}).get("layers", [])) >= 2:
        return "B"
    if sc.get("detail_fx"):
        return "C"
    return "A"


def audit_episode_motion(ep) -> dict[str, Any]:
    """Audit episode Visual Motion Plan against Level 2 + Hardware Safety (L480 8GB RAM) standards."""
    cfg = ep.cfg
    is_level2 = str(cfg.get("motion_upgrade", "")).lower() in ("level2", "v2", "2") or bool(cfg.get("motion_plan"))
    scenes = sorted(cfg.get("scenes", []), key=lambda s: float(s.get("start", 0.0)))
    errors: list[str] = []
    warnings: list[str] = []
    level_counts = {lv: 0 for lv in MOTION_LEVELS}
    scene_rows: list[dict[str, Any]] = []

    foley_times = [float(f["at"]) for f in cfg.get("audio", {}).get("foley", []) if "at" in f]
    synced_cues: list[str] = []
    unsynced_cues: list[str] = []

    def check_sfx_near(label: str, t_event: float) -> None:
        if any(abs(ft - t_event) <= 0.65 for ft in foley_times):
            synced_cues.append(f"{label}@{t_event:.2f}s")
        else:
            unsynced_cues.append(f"{label}@{t_event:.2f}s")

    shake_scenes = 0
    for sc in scenes:
        sid = sc.get("id", "?")
        explicit_lv = str(sc.get("motion_level", "")).strip().upper()
        beat = str(sc.get("beat_type", "")).strip().lower()
        lv = infer_motion_level(sc)
        level_counts[lv] += 1
        pat = classify_camera_pattern(sc)
        mp = resolve_motion_params(sc)
        wobble = mp["wobble"]
        shakes = sc.get("shakes") or []
        if shakes:
            shake_scenes += 1
            for sh in shakes:
                check_sfx_near(f"{sid}:shake", float(sh.get("at", sh.get("t", sc.get("start", 0.0)))))

        if explicit_lv and explicit_lv not in MOTION_LEVELS:
            errors.append(f"Cảnh {sid}: motion_level '{explicit_lv}' không hợp lệ (chỉ nhận A/B/C/D)")
        if beat and beat not in BEAT_TYPES:
            errors.append(f"Cảnh {sid}: beat_type '{beat}' không hợp lệ (chọn trong {', '.join(BEAT_TYPES)})")
        if is_level2:
            if not explicit_lv:
                errors.append(f"Cảnh {sid}: thiếu 'motion_level' (A/B/C/D) theo chuẩn Visual Motion Upgrade Level 2")
            if not beat:
                errors.append(f"Cảnh {sid}: thiếu 'beat_type' theo quy tắc phân tích Visual Beat trước render")

        # Validate Level B parallax + Hardware Safety caps (max 2–3 layers, light blur)
        px = sc.get("parallax")
        if px:
            layers = px.get("layers") or []
            if len(layers) < 2:
                warnings.append(f"Cảnh {sid}: parallax có < 2 lớp -> sẽ tự hạ cấp về Level A")
            if len(layers) > MAX_PARALLAX_LAYERS:
                errors.append(
                    f"Cảnh {sid}: parallax có {len(layers)} lớp (vượt giới hạn an toàn phần cứng tối đa {MAX_PARALLAX_LAYERS} lớp BG/Subject/FG)"
                )
            for idx, ly in enumerate(layers[:MAX_PARALLAX_LAYERS]):
                lp = ly.get("image")
                if not lp or not ep.resolve_asset(lp).is_file():
                    errors.append(f"Cảnh {sid}: thiếu file layer 2.5D '{lp}' (hoặc hạ cảnh xuống Level A)")
                if float(ly.get("blur", 0.0)) > MAX_PARALLAX_BLUR:
                    warnings.append(f"Cảnh {sid}: layer #{idx} blur={ly.get('blur')} vượt ngưỡng nhẹ {MAX_PARALLAX_BLUR}px -> sẽ tự giới hạn về {MAX_PARALLAX_BLUR}px")
        elif explicit_lv == "B":
            warnings.append(f"Cảnh {sid}: gắn motion_level='B' nhưng chưa khai báo 'parallax.layers' -> sẽ chạy Level A")

        # Validate Level C detail_fx + Hardware Safety exclusions
        dfx_list = sc.get("detail_fx") or []
        for fx in dfx_list:
            ft = str(fx.get("type", "")).lower()
            if ft in EXCLUDED_HEAVY_FX:
                warnings.append(f"Cảnh {sid}: detail_fx '{ft}' {EXCLUDED_HEAVY_FX[ft]}")
                continue
            if ft not in DETAIL_FX_TYPES:
                errors.append(f"Cảnh {sid}: detail_fx type '{ft}' không hỗ trợ (hỗ trợ: {', '.join(DETAIL_FX_TYPES)})")
                continue
            rel_t = bool(fx.get("relative", False))
            if ft in ("detail_reveal", "detail_layer", "eye_blink"):
                ip = fx.get("image")
                if not ip or not ep.resolve_asset(ip).is_file():
                    errors.append(f"Cảnh {sid}: detail_fx '{ft}' thiếu ảnh '{ip}'")
            elif ft == "mouth_sync":
                op = fx.get("open_image") or fx.get("image")
                if not op or not ep.resolve_asset(op).is_file():
                    errors.append(f"Cảnh {sid}: detail_fx 'mouth_sync' thiếu ảnh mở miệng '{op}'")
                for k_opt in ("closed_image", "mid_image"):
                    vp_opt = fx.get(k_opt)
                    if vp_opt and not ep.resolve_asset(vp_opt).is_file():
                        errors.append(f"Cảnh {sid}: detail_fx 'mouth_sync' thiếu ảnh {k_opt} '{vp_opt}'")
            if ft == "cursor_click":
                ct = _resolve_time(fx.get("click_at", sc.get("start", 0.0)), sc, rel_t)
                check_sfx_near(f"{sid}:cursor_click", ct)
            elif ft == "detail_reveal":
                at = _resolve_time(fx.get("at", sc.get("start", 0.0)), sc, rel_t)
                check_sfx_near(f"{sid}:detail_reveal", at)
            elif ft == "light_shift":
                at = _resolve_time(fx.get("at", sc.get("start", 0.0)), sc, rel_t)
                check_sfx_near(f"{sid}:light_shift", at)
            elif ft == "screen_glow" and str(fx.get("mode", "turn_on")).lower() == "turn_on":
                st = _resolve_time(fx.get("start", sc.get("start", 0.0)), sc, rel_t)
                check_sfx_near(f"{sid}:screen_glow", st)

        # Validate Level D video clip (external pre-rendered clip ONLY, always with fallback image)
        if explicit_lv == "D":
            vp = sc.get("video")
            if sc.get("video_enabled", True) and vp:
                if not ep.resolve_asset(vp).is_file():
                    if sc.get("image") and ep.resolve_asset(sc["image"]).is_file():
                        warnings.append(f"Cảnh {sid}: thiếu clip Level D '{vp}', sẽ fallback về ảnh tĩnh '{sc['image']}'")
                    else:
                        errors.append(f"Cảnh {sid}: Level D thiếu cả clip '{vp}' lẫn ảnh fallback")
            elif not (sc.get("image") and ep.resolve_asset(sc["image"]).is_file()):
                errors.append(f"Cảnh {sid}: Level D chưa có clip hoặc ảnh fallback hợp lệ")

        if beat in ("ending", "establishing", "normal") and wobble in ("tense", "handheld"):
            warnings.append(f"Cảnh {sid} ({beat}): dùng wobble='{wobble}' – cân nhắc giảm xuống 'none'/'calm'")

        scene_rows.append({
            "id": sid,
            "start": float(sc.get("start", 0.0)),
            "end": float(sc.get("end", 0.0)),
            "beat_type": beat or "unspecified",
            "motion_level": lv,
            "camera_pattern": pat,
            "wobble": wobble,
            "shakes": len(shakes),
            "detail_fx": [str(f.get("type", "")) for f in dfx_list],
            "intent": sc.get("motion_intent", ""),
        })

    for i, cb in enumerate(cfg.get("chat_bubbles", [])):
        check_sfx_near(f"chat{i + 1}", float(cb.get("start", 0.0)))
    for i, nt in enumerate(cfg.get("notifications", [])):
        check_sfx_near(f"notif{i + 1}", float(nt.get("start", 0.0)))

    zoom_streaks: list[list[str]] = []
    cur_streak: list[str] = []
    for r in scene_rows:
        if r["camera_pattern"] == "push_in":
            cur_streak.append(r["id"])
        else:
            if len(cur_streak) >= 3:
                zoom_streaks.append(cur_streak)
            cur_streak = []
    if len(cur_streak) >= 3:
        zoom_streaks.append(cur_streak)

    for st in zoom_streaks:
        warnings.append(
            f"Lặp pattern zoom-in liên tiếp {len(st)} cảnh ({' -> '.join(st)}): "
            f"nên xen kẽ pull_out, pan, static_hold hoặc Level B/C để đổi nhịp thị giác"
        )

    if len(scenes) >= 4 and shake_scenes > max(2, int(len(scenes) * 0.35)):
        warnings.append(f"Lạm dụng camera shake ({shake_scenes}/{len(scenes)} cảnh có shake) – chỉ dùng ở điểm nhấn có chủ đích")

    has_highlights = (
        level_counts["B"] + level_counts["C"] + level_counts["D"] > 0
        or bool(cfg.get("chat_bubbles"))
        or bool(cfg.get("notifications"))
    )
    if is_level2 and not has_highlights and len(scenes) >= 4:
        warnings.append("Chưa có visual highlight Level B/C/D nào – cân nhắc đầu tư 1–3 điểm nhấn nhẹ nếu nguồn hình phù hợp")

    if not is_level2:
        warnings.append("Tập cũ chưa khai báo 'motion_upgrade: level2' (tương thích ngược: giữ nguyên pipeline cũ)")

    return {
        "hardware_profile": HARDWARE_PROFILE,
        "is_level2": is_level2,
        "level_counts": level_counts,
        "total_scenes": len(scenes),
        "has_highlights": has_highlights,
        "zoom_streaks": zoom_streaks,
        "shake_scenes": shake_scenes,
        "sfx_sync": {"synced": synced_cues, "unsynced": unsynced_cues},
        "scenes": scene_rows,
        "errors": errors,
        "warnings": warnings,
    }
