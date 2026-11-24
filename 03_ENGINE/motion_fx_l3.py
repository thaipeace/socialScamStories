# -*- coding: utf-8 -*-
"""
Shared Visual Motion Level 3 Extensions (`03_ENGINE/motion_fx_l3.py`)
Tối ưu cho Hardware Profile `dual16gb_cpu_l480` (ThinkPad L480 · Intel i5-8250U · 16GB Dual-Channel · UHD 620).

Cung cấp các khối mở rộng gọn nhẹ tăng tốc bằng OpenCV (`cv2`, tự động fallback sang Pillow/NumPy nếu thiếu):
  1. Tăng tốc biến đổi khung hình (`fast_camera_transform`, `fast_gaussian_blur`, `fast_blend`) + hỗ trợ góc nghiêng vi mô (`angle_deg`).
  2. Nhóm 1 — Đạo diễn & Đồ họa bóc trần:
       * `split_screen` (chia đôi màn hình cuộc gọi 2 người, hỗ trợ cả 16:9 dọc & 9:16 ngang, sáng viền & sóng âm theo người đang nói)
       * `phone_waveform` (sóng âm thoại chạy theo file `.wav` thật)
       * `red_circle_draw` (khoanh đỏ / gạch chân / đóng khung vẽ tay chạy nét theo thời gian)
       * `highlighter_sweep` (quẹt bút dạ quang trong suốt không che chữ)
       * `animated_counter` (đồng hồ đếm ngược / biến động số dư nhảy số thực)
       * `typing_indicator` (bong bóng `...` đang nhập trước khi tin nhắn bật ra)
       * Chuyển cảnh điện ảnh: `whip_pan_left`, `whip_pan_right`, `zoom_punch`, `luma_wipe`, `film_burn`
  3. Nhóm 2 — Không khí, Ánh sáng & Màu phim:
       * `rain_layer` (mưa 2 lớp tiền-hậu cảnh cuộn mượt, nhẹ CPU)
       * `ambient_particles` (hạt bụi ánh sáng / bokeh trôi chậm)
       * `light_sweep` (vệt sáng đèn xe / ánh sáng quét ngang mềm ở độ phân giải 1/4)
       * `color_mood` (LUT tông màu điện ảnh + vignette + film grain mịn: warm_daily, cold_suspicion, high_tension, flashback, noir_evidence)
       * `chromatic_pulse` (tách sắc cạnh R/B + zoom blur nhẹ đúng cú sốc climax)
  4. Nhóm 3.7 — Living-Character Level 2.5:
       * `compute_speaker_rms_envelope` (đọc biên độ `.wav` thật cho `split_screen`, `phone_waveform`, `head_micro_tilt`)
       * `compute_mouth_viseme_timeline` (khẩu hình 4 trạng thái phân biệt âm tròn O/Ô/U qua spectral centroid)
       * `eye_gaze` / `expr_swap` được xử lý chung qua ROI khóa pixel của `motion_fx.py`.
"""
from __future__ import annotations

import json
import math
import wave
from pathlib import Path
from typing import Any

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

try:
    import cv2  # type: ignore
    HAS_CV2 = True
except Exception:  # noqa: BLE001
    cv2 = None  # type: ignore
    HAS_CV2 = False


# ----------------------------------------------------------------------------
# Constants & Presets (Level 3)
# ----------------------------------------------------------------------------

L3_TRANSITIONS: tuple[str, ...] = (
    "cut",
    "dissolve",
    "flash_white",
    "flash_red",
    "fade_black",
    "glitch",
    "whip_pan_left",
    "whip_pan_right",
    "zoom_punch",
    "luma_wipe",
    "film_burn",
)

COLOR_MOOD_PRESETS: dict[str, dict[str, Any]] = {
    "warm_daily": {
        "gain": (1.05, 1.01, 0.94),
        "lift": (4.0, 1.5, -3.0),
        "contrast": 1.03,
        "vignette": 0.12,
        "grain": 0.0,
    },
    "cold_suspicion": {
        "gain": (0.91, 0.99, 1.09),
        "lift": (-5.0, 0.0, 7.0),
        "contrast": 1.08,
        "vignette": 0.24,
        "grain": 0.015,
    },
    "high_tension": {
        "gain": (1.06, 0.94, 0.92),
        "lift": (-6.0, -7.0, -5.0),
        "contrast": 1.15,
        "vignette": 0.30,
        "grain": 0.022,
    },
    "flashback": {
        "gain": (1.08, 0.99, 0.84),
        "lift": (10.0, 6.0, -2.0),
        "contrast": 0.94,
        "vignette": 0.32,
        "grain": 0.032,
    },
    "noir_evidence": {
        "gain": (0.94, 0.97, 1.03),
        "lift": (-8.0, -7.0, -4.0),
        "contrast": 1.18,
        "vignette": 0.28,
        "grain": 0.02,
    },
}

_FONT_CACHE_L3: dict[tuple[int, bool], ImageFont.FreeTypeFont] = {}


def _get_font(size: int, bold: bool = True) -> ImageFont.FreeTypeFont:
    key = (size, bold)
    if key in _FONT_CACHE_L3:
        return _FONT_CACHE_L3[key]
    cands = (
        [
            r"C:\Windows\Fonts\segoeuib.ttf",
            r"C:\Windows\Fonts\arialbd.ttf",
            r"C:\Windows\Fonts\tahomabd.ttf",
        ]
        if bold
        else [
            r"C:\Windows\Fonts\segoeui.ttf",
            r"C:\Windows\Fonts\arial.ttf",
            r"C:\Windows\Fonts\tahoma.ttf",
        ]
    )
    f = None
    for c in cands:
        if Path(c).is_file():
            f = ImageFont.truetype(c, size=size)
            break
    _FONT_CACHE_L3[key] = f or ImageFont.load_default()
    return _FONT_CACHE_L3[key]


def _ease(u: float, easing: str = "smoothstep") -> float:
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


# ----------------------------------------------------------------------------
# 1. OpenCV-Accelerated Image Primitives (with transparent Pillow fallback)
# ----------------------------------------------------------------------------

def fast_gaussian_blur(img: Image.Image, radius: float) -> Image.Image:
    radius = max(0.0, float(radius))
    if radius <= 0.1:
        return img
    if HAS_CV2:
        arr = np.asarray(img)
        k = max(3, int(round(radius * 3.0)) * 2 + 1)
        blurred = cv2.GaussianBlur(arr, (k, k), sigmaX=radius, sigmaY=radius, borderType=cv2.BORDER_REPLICATE)
        return Image.fromarray(blurred, mode=img.mode)
    return img.filter(ImageFilter.GaussianBlur(radius=radius))


def fast_blend(img_a: Image.Image, img_b: Image.Image, alpha: float) -> Image.Image:
    a = max(0.0, min(1.0, float(alpha)))
    if a <= 0.002:
        return img_a
    if a >= 0.998:
        return img_b
    if HAS_CV2 and img_a.mode == img_b.mode and img_a.size == img_b.size:
        out = cv2.addWeighted(np.asarray(img_a), 1.0 - a, np.asarray(img_b), a, 0.0)
        return Image.fromarray(out, mode=img_a.mode)
    return Image.blend(img_a, img_b, a)


def fast_camera_transform(
    src: Image.Image,
    W: int,
    H: int,
    scale: float,
    fx: float,
    fy: float,
    dx: float,
    dy: float,
    angle_deg: float = 0.0,
    pivot: tuple[float, float] = (0.5, 0.78),
) -> Image.Image:
    """Fast camera crop/scale/pan + optional micro-rotation around pivot (for head_micro_tilt).
    Uses OpenCV SIMD warpAffine when available (~3-5x faster than Pillow EXTENT), else Pillow fallback."""
    sw, sh = src.size
    sc = max(scale, 1.001)
    cw, ch = sw / sc, sh / sc
    left = max(0.0, min(sw - cw, fx * sw + dx - cw * 0.5))
    top = max(0.0, min(sh - ch, fy * sh + dy - ch * 0.5))

    if HAS_CV2:
        arr = np.asarray(src)
        sx = W / max(cw, 1e-4)
        sy = H / max(ch, 1e-4)
        if abs(angle_deg) < 0.015:
            M = np.array([[sx, 0.0, -left * sx], [0.0, sy, -top * sy]], dtype=np.float32)
        else:
            # Map src -> out space, then apply subtle rotation around normalized pivot in output coordinates
            px_out, py_out = pivot[0] * W, pivot[1] * H
            rad = math.radians(angle_deg)
            ca, sa = math.cos(rad), math.sin(rad)
            # Combine affine: R(pivot) * S_crop
            m00 = ca * sx
            m01 = -sa * sy
            m10 = sa * sx
            m11 = ca * sy
            tx0 = -left * sx - px_out
            ty0 = -top * sy - py_out
            tx = ca * tx0 - sa * ty0 + px_out
            ty = sa * tx0 + ca * ty0 + py_out
            M = np.array([[m00, m01, tx], [m10, m11, ty]], dtype=np.float32)
        bmode = cv2.BORDER_CONSTANT if src.mode == "RGBA" else cv2.BORDER_REPLICATE
        warped = cv2.warpAffine(
            arr, M, (W, H),
            flags=cv2.INTER_LINEAR,
            borderMode=bmode,
            borderValue=(0, 0, 0, 0) if src.mode == "RGBA" else (0, 0, 0),
        )
        return Image.fromarray(warped, mode=src.mode)

    out = src.transform((W, H), Image.Transform.EXTENT, (left, top, left + cw, top + ch), resample=Image.Resampling.BILINEAR)
    if abs(angle_deg) >= 0.02:
        px_out, py_out = pivot[0] * W, pivot[1] * H
        out = out.rotate(-angle_deg, resample=Image.Resampling.BILINEAR, center=(px_out, py_out))
    return out


def fast_motion_blur_1d(img: Image.Image, ksize: int, horizontal: bool = True) -> Image.Image:
    k = max(1, int(ksize))
    if k <= 1:
        return img
    if k % 2 == 0:
        k += 1
    if HAS_CV2:
        arr = np.asarray(img)
        kernel = (k, 1) if horizontal else (1, k)
        out = cv2.blur(arr, kernel, borderType=cv2.BORDER_REPLICATE)
        return Image.fromarray(out, mode=img.mode)
    return img.filter(ImageFilter.GaussianBlur(radius=max(1.0, k * 0.25)))


def fast_zoom_blur(img: Image.Image, strength: float = 0.04, steps: int = 3) -> Image.Image:
    """Lightweight multi-tap radial zoom blur using fast affine blends."""
    st = max(0.0, min(0.14, float(strength)))
    if st <= 0.004:
        return img
    W, H = img.size
    if HAS_CV2:
        base = np.asarray(img, dtype=np.float32)
        acc = base.copy()
        w_sum = 1.0
        for i in range(1, steps + 1):
            sc = 1.0 + st * (i / steps)
            cw, ch = W / sc, H / sc
            lx, ty = (W - cw) * 0.5, (H - ch) * 0.5
            M = np.array([[sc, 0.0, -lx * sc], [0.0, sc, -ty * sc]], dtype=np.float32)
            tap = cv2.warpAffine(base, M, (W, H), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
            wt = 0.65 ** i
            acc += tap * wt
            w_sum += wt
        return Image.fromarray(np.clip(acc / w_sum, 0, 255).astype(np.uint8), mode=img.mode)
    return img


# ----------------------------------------------------------------------------
# 2. Cinematic Transitions (Level 3)
# ----------------------------------------------------------------------------

def apply_transition_l3(prev: Image.Image, curr: Image.Image, ttype: str, u: float, W: int, H: int) -> Image.Image | None:
    """Render Level 3 cinematic transitions. Returns None if `ttype` is not a Level 3 transition."""
    u = max(0.0, min(1.0, float(u)))
    su = _ease(u, "smoothstep")

    if ttype in ("whip_pan_left", "whip_pan_right"):
        # Smooth S-curve slide with 1D horizontal motion blur peaking at mid-transition
        direction = -1.0 if ttype == "whip_pan_left" else 1.0
        shift = int(round(W * su))
        blur_k = int(round(math.sin(math.pi * u) * max(18, W // 36)))
        p_arr = np.asarray(prev)
        c_arr = np.asarray(curr)
        canvas = np.empty_like(c_arr)
        if direction < 0:
            # Prev slides out to the left, Curr enters from the right
            rem = W - shift
            if rem > 0:
                canvas[:, :rem] = p_arr[:, shift:]
            if shift > 0:
                canvas[:, rem:] = c_arr[:, :shift]
        else:
            # Prev slides out to the right, Curr enters from the left
            rem = W - shift
            if shift > 0:
                canvas[:, :shift] = c_arr[:, rem:]
            if rem > 0:
                canvas[:, shift:] = p_arr[:, :rem]
        out = Image.fromarray(canvas, mode="RGB")
        return fast_motion_blur_1d(out, blur_k, horizontal=True)

    if ttype == "zoom_punch":
        # Push rapidly into prev (0..0.5), pop smoothly out of zoomed curr (0.5..1.0) with peak zoom blur
        if u < 0.5:
            p_u = _ease(u * 2.0, "ease_in")
            sc = 1.0 + 0.24 * p_u
            img_z = fast_camera_transform(prev, W, H, sc, 0.5, 0.5, 0.0, 0.0)
            blur_amt = 0.065 * p_u
            img_z = fast_zoom_blur(img_z, blur_amt, steps=3)
            if u > 0.35:
                blend_a = (u - 0.35) / 0.15 * 0.5
                c_z = fast_camera_transform(curr, W, H, 1.18, 0.5, 0.5, 0.0, 0.0)
                img_z = fast_blend(img_z, c_z, blend_a)
            return img_z
        c_u = _ease((u - 0.5) * 2.0, "ease_out")
        sc = 1.18 - 0.18 * c_u
        img_z = fast_camera_transform(curr, W, H, sc, 0.5, 0.5, 0.0, 0.0)
        return fast_zoom_blur(img_z, 0.055 * (1.0 - c_u), steps=3)

    if ttype == "luma_wipe":
        # Reveal incoming scene smoothly through a soft luminance threshold mask
        p_arr = np.asarray(prev, dtype=np.float32)
        c_arr = np.asarray(curr, dtype=np.float32)
        luma = (0.299 * c_arr[:, :, 0] + 0.587 * c_arr[:, :, 1] + 0.114 * c_arr[:, :, 2]) * (1.0 / 255.0)
        soft = 0.22
        thresh = (1.0 + soft) * (1.0 - su) - soft * 0.5
        mask = np.clip((luma - thresh) / soft, 0.0, 1.0)[:, :, None]
        out = p_arr * (1.0 - mask) + c_arr * mask
        return Image.fromarray(np.clip(out, 0, 255).astype(np.uint8), mode="RGB")

    if ttype == "film_burn":
        # Warm analog film light-leak sweep peaking mid-cut (great for Chapter transitions & flashbacks)
        base = fast_blend(prev, curr, su)
        peak = math.sin(math.pi * u) ** 1.4
        if peak <= 0.02:
            return base
        lw, lh = max(48, W // 8), max(48, H // 8)
        xx = np.linspace(0.0, 1.0, lw, dtype=np.float32)[None, :]
        yy = np.linspace(0.0, 1.0, lh, dtype=np.float32)[:, None]
        center_x = 0.15 + 0.70 * u
        dist = ((xx - center_x) / 0.42) ** 2 + ((yy - 0.48) / 0.75) ** 2
        leak = np.exp(-dist * 1.8) * peak
        leak_rgb = np.stack([
            np.clip(leak * 1.15, 0.0, 1.0),
            np.clip(leak * 0.62, 0.0, 1.0),
            np.clip(leak * 0.16, 0.0, 1.0),
        ], axis=2)
        if HAS_CV2:
            leak_full = cv2.resize(leak_rgb, (W, H), interpolation=cv2.INTER_LINEAR)
        else:
            leak_full = np.asarray(
                Image.fromarray((leak_rgb * 255).astype(np.uint8), mode="RGB").resize((W, H), Image.Resampling.BILINEAR),
                dtype=np.float32,
            ) / 255.0
        b_f = np.asarray(base, dtype=np.float32) / 255.0
        comp = 1.0 - (1.0 - b_f) * (1.0 - np.clip(leak_full * 0.85, 0.0, 0.92))
        return Image.fromarray(np.clip(comp * 255.0, 0, 255).astype(np.uint8), mode="RGB")

    return None


# ----------------------------------------------------------------------------
# 3. Real-WAV Audio Analyzers (Living-Character 2.5 + Waveform + Head Tilt)
# ----------------------------------------------------------------------------

def compute_speaker_rms_envelope(
    ep,
    sc: dict,
    speaker: str | None = None,
    line_ids: list[str] | None = None,
    fps: int = 24,
) -> np.ndarray:
    """Read normalized RMS speech envelope in [0, 1] directly from Gate 2 TTS WAV files."""
    s_sc, e_sc = float(sc["start"]), float(sc["end"])
    n_steps = max(1, int(math.ceil(max(0.1, e_sc - s_sc) * fps)) + 1)
    env = np.zeros(n_steps, dtype=np.float32)
    tts_p = getattr(ep, "tts_manifest_path", None)
    if not tts_p or not Path(tts_p).is_file():
        return env
    try:
        tts = json.loads(Path(tts_p).read_text(encoding="utf-8"))
    except Exception:
        return env

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
        ref = float(np.percentile(active, 88)) if active.size >= 3 else max(float(rms.max()), 0.05)
        norm = np.clip(rms / max(ref, 1e-4), 0.0, 1.0)
        for wi in range(n_win):
            t_cur = ls + (wi + 0.5) / float(fps)
            if t_cur < s_sc or t_cur >= e_sc:
                continue
            si = int((t_cur - s_sc) * fps)
            if 0 <= si < n_steps and norm[wi] > env[si]:
                env[si] = float(norm[wi])
    return env


def compute_mouth_viseme_timeline(
    ep,
    sc: dict,
    speaker: str | None,
    line_ids: list[str] | None,
    fps: int,
    thresh_mid: float,
    thresh_open: float,
    enable_round: bool = False,
    round_centroid_hz: float = 980.0,
) -> np.ndarray:
    """Compute anime lip-sync viseme states from real TTS WAVs:
       0 = closed, 1 = mid, 2 = open (A/E/I), 3 = round (O/Ô/U when `enable_round=True`).
    100% identical to 3-state behavior when `enable_round=False`."""
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

        centroids = None
        if enable_round:
            win_fn = np.hanning(hop).astype(np.float32)[None, :]
            spec = np.abs(np.fft.rfft(trimmed * win_fn, axis=1)) + 1e-9
            freqs = np.fft.rfftfreq(hop, d=1.0 / sr).astype(np.float32)[None, :]
            # Focus on human vocal band (120 Hz - 4200 Hz)
            band = (freqs[0] >= 120.0) & (freqs[0] <= 4200.0)
            spec_b = spec[:, band]
            freqs_b = freqs[:, band]
            centroids = (spec_b * freqs_b).sum(axis=1) / np.maximum(spec_b.sum(axis=1), 1e-6)

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
                if run_open % 4 == 0:
                    st = 1
                elif enable_round and centroids is not None and float(centroids[wi]) < round_centroid_hz:
                    st = 3
                else:
                    st = 2
            elif v >= thresh_mid:
                run_open = 0
                if enable_round and centroids is not None and v >= (thresh_mid + thresh_open) * 0.5 and float(centroids[wi]) < round_centroid_hz * 0.88:
                    st = 3
                else:
                    st = 1
            else:
                run_open = 0
                st = 0
            if st > states[si]:
                states[si] = st
    return states


# ----------------------------------------------------------------------------
# 4. Group 1 — Split-Screen & Evidence Motion Graphics
# ----------------------------------------------------------------------------

def prepare_split_screen(ep, sc: dict, W: int, H: int, oversample: float,
                         prepare_detail_fn, resolve_motion_fn, fit_crop_fn) -> dict[str, Any] | None:
    """Prepare 2-panel dynamic split-screen scene (e.g., scammer vs victim phone call)."""
    sp = sc.get("split_screen")
    if not sp or not isinstance(sp, dict):
        return None
    raw_panels = sp.get("panels") or []
    if len(raw_panels) != 2:
        sc["_motion_fallback"] = "split_screen cần đúng 2 panels -> hạ cấp về ảnh tĩnh"
        return None

    is_landscape = W > H
    layout = str(sp.get("layout", "vertical" if is_landscape else "horizontal")).lower()
    ratio = max(0.30, min(0.70, float(sp.get("ratio", 0.50))))
    div_w = max(2, min(14, int(sp.get("divider_width", 6))))
    if layout == "vertical":
        w0 = int(round((W - div_w) * ratio))
        w1 = W - div_w - w0
        rects = [(0, 0, w0, H), (w0 + div_w, 0, W, H)]
    else:
        h0 = int(round((H - div_w) * ratio))
        h1 = H - div_w - h0
        rects = [(0, 0, W, h0), (0, h0 + div_w, W, H)]

    panels: list[dict[str, Any]] = []
    for idx, rp in enumerate(raw_panels):
        img_ref = rp.get("image")
        if not img_ref:
            sc["_motion_fallback"] = f"split_screen panel #{idx} thiếu image"
            return None
        p = ep.resolve_asset(img_ref)
        if not p.is_file():
            sc["_motion_fallback"] = f"Thiếu ảnh split_screen '{img_ref}'"
            return None
        x0, y0, x1, y1 = rects[idx]
        pw, ph = x1 - x0, y1 - y0
        po_w, po_h = int(pw * min(oversample, 1.22)), int(ph * min(oversample, 1.22))
        crop_x = rp.get("crop_x")
        crop_y = rp.get("crop_y")
        with Image.open(p) as raw_im:
            rgb_im = raw_im.convert("RGB")
            if crop_x is not None or crop_y is not None:
                iw, ih = rgb_im.size
                if abs(iw / max(ih, 1) - pw / ph) > 0.02:
                    tw = int(ih * pw / ph)
                    if tw <= iw:
                        cx_f = max(0.0, min(1.0, float(crop_x if crop_x is not None else 0.5)))
                        cx0 = max(0, min(iw - tw, int(round(cx_f * iw - tw * 0.5))))
                        rgb_im = rgb_im.crop((cx0, 0, cx0 + tw, ih))
                    else:
                        th = int(iw * ph / pw)
                        cy_f = max(0.0, min(1.0, float(crop_y if crop_y is not None else 0.5)))
                        cy0 = max(0, min(ih - th, int(round(cy_f * ih - th * 0.5))))
                        rgb_im = rgb_im.crop((0, cy0, iw, cy0 + th))
            else:
                rgb_im = fit_crop_fn(rgb_im, pw, ph)
            base_im = rgb_im.resize((po_w, po_h), Image.Resampling.LANCZOS)

        # Mini pseudo-scene dict so panel reuses standard motion + detail_fx (eye_blink, mouth_sync, screen_glow...)
        # Pass _panel_crop so ROI patches align 1:1 with crop_x/crop_y framing!
        psc = {
            "id": f"{sc.get('id', 'sp')}_p{idx}",
            "start": sc["start"],
            "end": sc["end"],
            "motion": rp.get("motion") or {"preset": "slow_push_in" if idx == 0 else "slow_pull_out"},
            "motion_level": "C",
            "detail_fx": rp.get("detail_fx") or [],
            "_panel_crop": (crop_x, crop_y),
        }
        mp = resolve_motion_fn(psc)
        dfx = prepare_detail_fn(ep, psc, pw, ph, min(oversample, 1.22))
        spk = rp.get("speaker")
        line_ids = rp.get("line_ids")
        rms_env = compute_speaker_rms_envelope(ep, sc, speaker=spk, line_ids=line_ids, fps=24) if (spk or line_ids) else None

        panels.append({
            "rect": (x0, y0, x1, y1),
            "pw": pw,
            "ph": ph,
            "img": base_im,
            "motion": mp,
            "detail_fx": dfx,
            "speaker": spk,
            "label": str(rp.get("label", "")),
            "label_rgb": tuple(int(c) for c in rp.get("label_rgb", [235, 65, 65] if idx == 0 else [65, 195, 130])),
            "waveform": bool(rp.get("waveform", bool(spk or line_ids))),
            "waveform_rgb": tuple(int(c) for c in rp.get("waveform_rgb", [255, 110, 95] if idx == 0 else [110, 225, 255])),
            "rms_env": rms_env,
        })

    return {
        "layout": layout,
        "divider_width": div_w,
        "divider_rgb": tuple(int(c) for c in sp.get("divider_rgb", [240, 245, 255])),
        "active_glow_rgb": tuple(int(c) for c in sp.get("active_glow_rgb", [255, 205, 75])),
        "inactive_dim": max(0.0, min(0.45, float(sp.get("inactive_dim", 0.16)))),
        "slide_in_dur": max(0.0, min(1.0, float(sp.get("slide_in_dur", 0.35)))),
        "panels": panels,
        "sc_start": float(sc["start"]),
    }


def _draw_waveform_bars(
    draw: ImageDraw.ImageDraw,
    bx: int,
    by: int,
    bw: int,
    bh: int,
    level: float,
    t: float,
    color: tuple[int, int, int],
    n_bars: int = 11,
    alpha: int = 235,
) -> None:
    """Draw smooth live equalizer bars modulated by real speech RMS level."""
    gap = max(2, bw // (n_bars * 3))
    bar_w = max(3, (bw - gap * (n_bars - 1)) // n_bars)
    cy = by + bh // 2
    for i in range(n_bars):
        # Bell envelope across bars + organic phase ripple when speaking
        pos_f = 1.0 - abs((i - (n_bars - 1) * 0.5) / max(1.0, (n_bars - 1) * 0.5)) * 0.55
        if level > 0.06:
            ripple = 0.55 + 0.45 * abs(math.sin(t * (13.0 + i * 2.1) + i * 0.9))
            h_frac = min(1.0, max(0.14, level * pos_f * ripple * 1.25))
        else:
            h_frac = 0.10 + 0.03 * math.sin(t * 2.5 + i * 0.7)
        half_h = max(2, int(round(bh * 0.48 * h_frac)))
        x0 = bx + i * (bar_w + gap)
        draw.rounded_rectangle([x0, cy - half_h, x0 + bar_w, cy + half_h], radius=max(1, bar_w // 2), fill=(*color, alpha))


def render_split_screen_frame(
    sp_rt: dict[str, Any],
    sc: dict,
    t: float,
    W: int,
    H: int,
    extra_dx: float,
    extra_dy: float,
    apply_pre_fn,
    apply_post_fn,
) -> Image.Image:
    """Render 2-panel split screen with independent motion/Living-Character FX, active speaker border & waveform."""
    s, e = float(sc["start"]), float(sc["end"])
    lt = max(0.0, t - s)
    canvas = Image.new("RGB", (W, H), (12, 14, 20))
    panels = sp_rt["panels"]

    # Sample RMS activity for each panel to highlight active speaker
    levels: list[float] = []
    for pn in panels:
        env = pn["rms_env"]
        if env is not None and env.size > 0:
            si = max(0, min(env.size - 1, int(lt * 24)))
            # Short 3-tap smoothing so highlight doesn't flicker between syllables
            lo_i, hi_i = max(0, si - 2), min(env.size, si + 3)
            levels.append(float(np.mean(env[lo_i:hi_i])))
        else:
            levels.append(0.0)
    any_talking = any(lv > 0.08 for lv in levels)

    slide_dur = sp_rt["slide_in_dur"]
    slide_u = _ease(lt / slide_dur, "ease_out") if (slide_dur > 0.01 and lt < slide_dur) else 1.0

    for idx, pn in enumerate(panels):
        x0, y0, x1, y1 = pn["rect"]
        pw, ph = pn["pw"], pn["ph"]
        mp = pn["motion"]
        u = _ease((max(s, min(e, t)) - s) / max(e - s, 1e-4), mp.get("easing", "smoothstep"))
        s0, s1 = mp["scale"]
        (fx0, fy0), (fx1, fy1) = mp["focus"]
        scale = s0 + (s1 - s0) * u
        fx, fy = fx0 + (fx1 - fx0) * u, fy0 + (fy1 - fy0) * u

        src_im = pn["img"]
        dfx = pn["detail_fx"]
        if dfx:
            src_im = apply_pre_fn(src_im, dfx, t)
        pf = fast_camera_transform(src_im, pw, ph, scale, fx, fy, extra_dx, extra_dy)
        if dfx:
            pf = apply_post_fn(pf, dfx, t, pw, ph)

        # Dim inactive panel gently when the other speaker is talking
        lv = levels[idx]
        is_active = any_talking and lv >= max(levels) * 0.7 and lv > 0.08
        if any_talking and not is_active and sp_rt["inactive_dim"] > 0.01:
            dim = sp_rt["inactive_dim"]
            if HAS_CV2:
                pf = Image.fromarray(cv2.convertScaleAbs(np.asarray(pf), alpha=1.0 - dim, beta=0), mode="RGB")
            else:
                pf = Image.blend(pf, Image.new("RGB", (pw, ph), (6, 8, 12)), dim)

        # Smooth entry offset
        ox, oy = x0, y0
        if slide_u < 0.999:
            off_px = int(round((1.0 - slide_u) * 48))
            if sp_rt["layout"] == "vertical":
                ox += -off_px if idx == 0 else off_px
            else:
                oy += -off_px if idx == 0 else off_px
        canvas.paste(pf, (ox, oy))

        # Draw active border directly onto canvas + tiny local RGBA badges (zero full-panel RGBA allocation!)
        if is_active:
            border_w = max(4, min(W, H) // 240)
            dc_p = ImageDraw.Draw(canvas)
            dc_p.rectangle(
                [x0 + border_w // 2, y0 + border_w // 2, x1 - border_w // 2 - 1, y1 - border_w // 2 - 1],
                outline=sp_rt["active_glow_rgb"], width=border_w,
            )
        base_dim = min(W, H)
        margin = max(18, int(base_dim * 0.024))
        if pn["label"]:
            lf = _get_font(max(18, int(base_dim * 0.023)), bold=True)
            tmp_d = ImageDraw.Draw(Image.new("RGBA", (4, 4)))
            tb = tmp_d.textbbox((0, 0), pn["label"], font=lf)
            tw, th = tb[2] - tb[0], tb[3] - tb[1]
            bw_l, bh_l = tw + 30, th + 16
            lx0 = x0 + (margin if idx == 0 else max(margin, pw - bw_l - 4 - margin))
            ly0 = y0 + margin + (54 if (idx == 0 and sp_rt["layout"] == "vertical" and W > H) else 0)
            ov_l = Image.new("RGBA", (bw_l, bh_l), (0, 0, 0, 0))
            dr_l = ImageDraw.Draw(ov_l)
            dr_l.rounded_rectangle([0, 0, bw_l - 1, bh_l - 1], radius=10,
                                   fill=(12, 16, 24, 195), outline=(*pn["label_rgb"], 230), width=2)
            dr_l.text((15 - tb[0], 8 - tb[1]), pn["label"], font=lf, fill=(255, 255, 255, 250))
            canvas.paste(ov_l.convert("RGB"), (lx0, ly0), ov_l.getchannel("A"))

        if pn["waveform"] and pn["rms_env"] is not None:
            wb_w = min(220, int(pw * 0.34))
            wb_h = max(34, int(base_dim * 0.042))
            wx0 = x0 + (margin if idx == 0 else max(margin, pw - wb_w - margin))
            wy0 = y0 + ph - wb_h - (int(ph * 0.16) if sp_rt["layout"] == "vertical" else margin + 12)
            ov_w = Image.new("RGBA", (wb_w, wb_h), (0, 0, 0, 0))
            dr_w = ImageDraw.Draw(ov_w)
            dr_w.rounded_rectangle([0, 0, wb_w - 1, wb_h - 1], radius=12,
                                   fill=(10, 14, 22, 185), outline=(*pn["waveform_rgb"], 200 if is_active else 95), width=2)
            _draw_waveform_bars(dr_w, 12, 6, wb_w - 24, wb_h - 12, lv, t, pn["waveform_rgb"], n_bars=11)
            canvas.paste(ov_w.convert("RGB"), (wx0, wy0), ov_w.getchannel("A"))

    # Crisp center divider bar
    div_w = sp_rt["divider_width"]
    dc = ImageDraw.Draw(canvas)
    if sp_rt["layout"] == "vertical":
        dx0 = panels[0]["rect"][2]
        dc.rectangle([dx0, 0, dx0 + div_w, H], fill=sp_rt["divider_rgb"])
    else:
        dy0 = panels[0]["rect"][3]
        dc.rectangle([0, dy0, W, dy0 + div_w], fill=sp_rt["divider_rgb"])
    return canvas


def prepare_l3_detail_fx(ep, sc: dict, fx: dict[str, Any], ftype: str, rel_time: bool,
                         W: int, H: int, tw_pre: int, th_pre: int, resolve_time_fn) -> dict[str, Any] | None:
    """Prepare Level 3 post-camera (and pre-camera) detail_fx items."""
    item: dict[str, Any] = dict(fx)
    item["type"] = ftype

    if ftype == "phone_waveform":
        item["_start"] = resolve_time_fn(fx.get("start", sc["start"]), sc, rel_time)
        item["_end"] = resolve_time_fn(fx.get("end", sc["end"]), sc, rel_time)
        item["_fade"] = max(0.05, float(fx.get("fade", 0.25)))
        item["_pos"] = tuple(float(v) for v in fx.get("pos", [0.16, 0.22] if W > H else [0.50, 0.25]))
        item["_size"] = tuple(float(v) for v in fx.get("size", [0.18, 0.058] if W > H else [0.42, 0.042]))
        item["_color"] = tuple(int(c) for c in fx.get("color", [95, 225, 255]))
        item["_label"] = str(fx.get("label", "CUỘC GỌI ĐẾN"))
        item["_bars"] = max(7, min(21, int(fx.get("bars", 13))))
        item["_sc_start"] = float(sc["start"])
        item["_rms_env"] = compute_speaker_rms_envelope(
            ep, sc, speaker=fx.get("speaker"), line_ids=fx.get("line_ids"), fps=24
        )
        item["_stage"] = "post_camera"
        return item

    if ftype == "red_circle_draw":
        reg = fx.get("region")
        if not (reg and len(reg) == 4):
            sc.setdefault("_detail_warnings", []).append("red_circle_draw cần 'region' [x0,y0,x1,y1] -> bỏ qua")
            return None
        item["_region"] = [max(0.0, min(1.0, float(v))) for v in reg]
        item["_at"] = resolve_time_fn(fx.get("at", sc["start"] + 0.3), sc, rel_time)
        item["_dur"] = max(0.12, float(fx.get("dur", 0.55)))
        item["_end"] = resolve_time_fn(fx.get("end", sc["end"]), sc, rel_time)
        item["_fade_out"] = max(0.05, float(fx.get("fade_out", 0.25)))
        item["_color"] = tuple(int(c) for c in fx.get("color", [238, 42, 48]))
        item["_width"] = max(3, min(14, int(fx.get("width", 6))))
        item["_style"] = str(fx.get("style", "circle")).lower()  # circle | underline | box
        item["_stage"] = "post_camera"
        return item

    if ftype == "highlighter_sweep":
        reg = fx.get("region")
        if not (reg and len(reg) == 4):
            sc.setdefault("_detail_warnings", []).append("highlighter_sweep cần 'region' [x0,y0,x1,y1] -> bỏ qua")
            return None
        item["_region"] = [max(0.0, min(1.0, float(v))) for v in reg]
        item["_at"] = resolve_time_fn(fx.get("at", sc["start"] + 0.3), sc, rel_time)
        item["_dur"] = max(0.12, float(fx.get("dur", 0.45)))
        item["_end"] = resolve_time_fn(fx.get("end", sc["end"]), sc, rel_time)
        item["_fade_out"] = max(0.05, float(fx.get("fade_out", 0.25)))
        item["_color"] = tuple(int(c) for c in fx.get("color", [255, 232, 65]))
        item["_opacity"] = max(0.12, min(0.65, float(fx.get("opacity", 0.38))))
        item["_stage"] = "post_camera"
        return item

    if ftype == "animated_counter":
        item["_start"] = resolve_time_fn(fx.get("start", sc["start"] + 0.2), sc, rel_time)
        item["_end"] = resolve_time_fn(fx.get("end", sc["end"]), sc, rel_time)
        item["_count_dur"] = max(0.15, float(fx.get("count_dur", max(0.5, item["_end"] - item["_start"] - 0.4))))
        item["_fade"] = max(0.05, float(fx.get("fade", 0.2)))
        item["_from_val"] = float(fx.get("from_val", 59.0))
        item["_to_val"] = float(fx.get("to_val", 0.0))
        item["_fmt"] = str(fx.get("fmt", "mmss")).lower()  # mmss | vnd | int | pct
        item["_prefix"] = str(fx.get("prefix", ""))
        item["_suffix"] = str(fx.get("suffix", ""))
        item["_label"] = str(fx.get("label", ""))
        item["_pos"] = tuple(float(v) for v in fx.get("pos", [0.82, 0.18] if W > H else [0.50, 0.24]))
        item["_style"] = str(fx.get("style", "danger")).lower()  # danger | warn | safe | info
        item["_easing"] = str(fx.get("easing", "linear"))
        item["_stage"] = "post_camera"
        return item

    if ftype == "typing_indicator":
        item["_start"] = resolve_time_fn(fx.get("start", sc["start"]), sc, rel_time)
        item["_end"] = resolve_time_fn(fx.get("end", item["_start"] + 1.4), sc, rel_time)
        item["_side"] = str(fx.get("side", "left")).lower()
        item["_y"] = fx.get("y")
        item["_pos"] = tuple(float(v) for v in fx.get("pos")) if fx.get("pos") else None
        item["_sender"] = str(fx.get("sender", ""))
        item["_stage"] = "post_camera"
        return item

    if ftype in ("rain_layer", "rain"):
        item["type"] = "rain_layer"
        item["_start"] = resolve_time_fn(fx.get("start", sc["start"]), sc, rel_time)
        item["_end"] = resolve_time_fn(fx.get("end", sc["end"]), sc, rel_time)
        item["_fade"] = max(0.05, float(fx.get("fade", 0.4)))
        item["_opacity"] = max(0.05, min(0.75, float(fx.get("opacity", 0.34))))
        item["_speed"] = max(200.0, min(2600.0, float(fx.get("speed", 1150.0))))
        item["_angle_deg"] = max(-28.0, min(28.0, float(fx.get("angle_deg", -12.0))))
        item["_density"] = max(0.3, min(2.0, float(fx.get("density", 1.0))))
        item["_color"] = tuple(int(c) for c in fx.get("color", [195, 220, 245]))
        # Pre-render 2 seamless tileable half-res rain streak layers (tiny RAM, ultra-fast scroll!)
        rw, rh = max(240, W // 2), max(240, H // 2)
        rng = np.random.default_rng(int(fx.get("seed", 77)))
        tiles = []
        for layer_i, (n_base, length_px, thick, alpha_mul) in enumerate([
            (int(95 * item["_density"]), 22, 1, 0.55),
            (int(55 * item["_density"]), 38, 1, 0.95),
        ]):
            tile = Image.new("L", (rw, rh), 0)
            dr = ImageDraw.Draw(tile)
            rad = math.radians(item["_angle_deg"])
            dx_s = math.sin(rad) * length_px
            dy_s = math.cos(rad) * length_px
            for _ in range(n_base):
                x0 = float(rng.uniform(0, rw))
                y0 = float(rng.uniform(0, rh))
                bri = int(rng.uniform(110, 245) * alpha_mul)
                for ox in (-rw, 0, rw):
                    for oy in (-rh, 0, rh):
                        sx0, sy0 = x0 + ox, y0 + oy
                        if -length_px <= sx0 <= rw + length_px and -length_px <= sy0 <= rh + length_px:
                            dr.line([(sx0, sy0), (sx0 + dx_s, sy0 + dy_s)], fill=bri, width=thick)
            tiles.append(np.asarray(tile, dtype=np.uint8))
        item["_tiles"] = tiles
        item["_stage"] = "post_camera"
        return item

    if ftype == "ambient_particles":
        item["_start"] = resolve_time_fn(fx.get("start", sc["start"]), sc, rel_time)
        item["_end"] = resolve_time_fn(fx.get("end", sc["end"]), sc, rel_time)
        item["_fade"] = max(0.05, float(fx.get("fade", 0.45)))
        item["_opacity"] = max(0.05, min(0.80, float(fx.get("opacity", 0.42))))
        item["_color"] = tuple(int(c) for c in fx.get("color", [220, 235, 255]))
        item["_dir"] = str(fx.get("drift_dir", "up")).lower()  # up | down | float
        count = max(10, min(55, int(fx.get("count", 28))))
        rng = np.random.default_rng(int(fx.get("seed", 101)))
        # Pre-generate deterministic particle trajectories + 3 soft bokeh sprite sizes
        particles = []
        for _ in range(count):
            particles.append((
                float(rng.uniform(0.02, 0.98)),   # x0
                float(rng.uniform(0.02, 0.98)),   # y0
                float(rng.uniform(0.008, 0.026)), # vy frac/sec
                float(rng.uniform(0.004, 0.014)), # vx sway amp
                float(rng.uniform(0.35, 1.1)),    # sway freq
                float(rng.uniform(0.0, 6.28)),    # phase
                int(rng.integers(0, 3)),          # size bucket
                float(rng.uniform(0.45, 1.0)),    # individual alpha
            ))
        base_r = max(4, int(fx.get("size_px", max(5, min(W, H) // 160))))
        sprites = []
        for mult in (0.65, 1.0, 1.55):
            r = max(3, int(round(base_r * mult)))
            sz = r * 2 + 1
            yy, xx = np.mgrid[-r:r + 1, -r:r + 1].astype(np.float32) / max(r, 1)
            fall = np.exp(-(xx * xx + yy * yy) * 3.0) * np.clip(1.0 - (xx * xx + yy * yy), 0.0, 1.0)
            sprites.append(Image.fromarray((fall * 255.0).astype(np.uint8), mode="L"))
        item["_particles"] = particles
        item["_sprites"] = sprites
        item["_sc_start"] = float(sc["start"])
        item["_stage"] = "post_camera"
        return item

    if ftype in ("light_sweep", "shadow_drift"):
        item["type"] = "light_sweep"
        item["_start"] = resolve_time_fn(fx.get("start", sc["start"]), sc, rel_time)
        item["_end"] = resolve_time_fn(fx.get("end", sc["end"]), sc, rel_time)
        item["_fade"] = max(0.05, float(fx.get("fade", 0.35)))
        item["_mode"] = str(fx.get("mode", "shadow" if ftype == "shadow_drift" else "light")).lower()
        item["_color"] = tuple(int(c) for c in fx.get("color", [255, 232, 185] if item["_mode"] == "light" else [8, 12, 22]))
        item["_intensity"] = max(0.05, min(0.65, float(fx.get("intensity", 0.28))))
        item["_width"] = max(0.08, min(0.55, float(fx.get("width", 0.22))))
        item["_angle_deg"] = max(-45.0, min(45.0, float(fx.get("angle_deg", -18.0))))
        item["_from_x"] = float(fx.get("from_x", -0.25))
        item["_to_x"] = float(fx.get("to_x", 1.25))
        item["_repeat"] = max(1, int(fx.get("repeat", 1)))
        # Precompute 1/4-res tilted coordinate grid
        lw, lh = max(64, W // 4), max(64, H // 4)
        xx = np.linspace(0.0, 1.0, lw, dtype=np.float32)[None, :]
        yy = np.linspace(0.0, 1.0, lh, dtype=np.float32)[:, None]
        slope = math.tan(math.radians(item["_angle_deg"])) * (H / max(W, 1))
        item["_coord"] = xx + (yy - 0.5) * slope
        item["_stage"] = "post_camera"
        return item

    if ftype == "color_mood":
        mood_name = str(fx.get("mood", "cold_suspicion")).lower()
        preset = dict(COLOR_MOOD_PRESETS.get(mood_name, COLOR_MOOD_PRESETS["cold_suspicion"]))
        item["_mood"] = mood_name
        item["_start"] = resolve_time_fn(fx.get("start", sc["start"]), sc, rel_time)
        item["_end"] = resolve_time_fn(fx.get("end", sc["end"]), sc, rel_time)
        item["_fade"] = max(0.05, float(fx.get("fade", 0.35)))
        item["_strength"] = max(0.0, min(1.0, float(fx.get("strength", 0.85))))
        item["_gain"] = tuple(float(v) for v in fx.get("gain", preset["gain"]))
        item["_lift"] = tuple(float(v) for v in fx.get("lift", preset["lift"]))
        item["_contrast"] = float(fx.get("contrast", preset["contrast"]))
        item["_vignette"] = max(0.0, min(0.65, float(fx.get("vignette", preset["vignette"]))))
        item["_grain"] = max(0.0, min(0.06, float(fx.get("grain", preset["grain"]))))
        if item["_vignette"] > 0.01:
            lw, lh = max(48, W // 8), max(48, H // 8)
            yy = np.linspace(-1.0, 1.0, lh, dtype=np.float32)[:, None]
            xx = np.linspace(-1.0, 1.0, lw, dtype=np.float32)[None, :]
            r = np.sqrt(xx * xx + yy * yy)
            vig = np.clip((r - 0.58) / 0.85, 0.0, 1.0) ** 1.8
            item["_vig_mask"] = Image.fromarray((vig * 255.0).astype(np.uint8), mode="L").resize((W, H), Image.Resampling.BILINEAR)
        else:
            item["_vig_mask"] = None
        if item["_grain"] > 0.002:
            # Pre-bake a 1/2-res reusable tileable signed int8 grain array (ultra-fast integer add!)
            rng = np.random.default_rng(int(fx.get("seed", 42)))
            gw, gh = max(128, W // 2), max(128, H // 2)
            item["_grain_tile"] = np.clip(rng.normal(0.0, 255.0 * item["_grain"], size=(gh, gw)), -40, 40).astype(np.int16)
        else:
            item["_grain_tile"] = None
        item["_stage"] = "post_camera"
        return item

    if ftype == "chromatic_pulse":
        item["_at"] = resolve_time_fn(fx.get("at", sc["start"]), sc, rel_time)
        item["_dur"] = max(0.08, min(1.2, float(fx.get("dur", 0.28))))
        item["_shift_px"] = max(2, min(18, int(fx.get("shift_px", 6))))
        item["_zoom_blur"] = max(0.0, min(0.08, float(fx.get("zoom_blur", 0.025))))
        item["_stage"] = "post_camera"
        return item

    return None


# ----------------------------------------------------------------------------
# 5. Group 1 & Group 2 Frame Renderers (post-camera)
# ----------------------------------------------------------------------------

def _apply_phone_waveform(frame: Image.Image, fx: dict[str, Any], t: float, W: int, H: int) -> Image.Image:
    env_a = _fade_env(t, fx["_start"], fx["_end"], fx["_fade"])
    if env_a <= 0.01:
        return frame
    rms_arr = fx["_rms_env"]
    lt = max(0.0, t - fx["_sc_start"])
    si = max(0, min(rms_arr.size - 1, int(lt * 24))) if rms_arr.size > 0 else 0
    lo_i, hi_i = max(0, si - 1), min(rms_arr.size, si + 2)
    lv = float(np.mean(rms_arr[lo_i:hi_i])) if rms_arr.size > 0 else 0.0

    bw = max(160, int(fx["_size"][0] * W))
    bh = max(44, int(fx["_size"][1] * H))
    cx, cy = int(fx["_pos"][0] * W), int(fx["_pos"][1] * H)
    x0 = max(10, min(W - bw - 10, cx - bw // 2))
    y0 = max(10, min(H - bh - 10, cy - bh // 2))

    ov = Image.new("RGBA", (bw, bh), (0, 0, 0, 0))
    dr = ImageDraw.Draw(ov)
    col = fx["_color"]
    al_bg = int(200 * env_a)
    al_fg = int(245 * env_a)
    dr.rounded_rectangle([0, 0, bw - 1, bh - 1], radius=min(16, bh // 3),
                         fill=(10, 14, 24, al_bg), outline=(*col, int((230 if lv > 0.08 else 120) * env_a)), width=2)
    label = fx["_label"]
    bx = 14
    if label:
        lf = _get_font(max(13, int(bh * 0.30)), bold=True)
        tb = dr.textbbox((0, 0), label, font=lf)
        tw = tb[2] - tb[0]
        # Pulsing active dot
        dot_r = max(4, bh // 9)
        dot_col = col if lv > 0.08 else (140, 155, 175)
        dr.ellipse([12, bh // 2 - dot_r, 12 + dot_r * 2, bh // 2 + dot_r], fill=(*dot_col, al_fg))
        dr.text((12 + dot_r * 2 + 8, bh // 2), label, font=lf, anchor="lm", fill=(240, 246, 255, al_fg))
        bx = 12 + dot_r * 2 + 8 + tw + 14
    if bw - bx >= 46:
        _draw_waveform_bars(dr, bx, 8, bw - bx - 12, bh - 16, lv, t, col, n_bars=fx["_bars"], alpha=al_fg)

    out = frame.copy()
    out.paste(ov.convert("RGB"), (x0, y0), ov.getchannel("A"))
    return out


def _apply_red_circle_draw(frame: Image.Image, fx: dict[str, Any], t: float, W: int, H: int) -> Image.Image:
    at, dur, end = fx["_at"], fx["_dur"], fx["_end"]
    if t < at or t >= end:
        return frame
    prog = _ease((t - at) / dur, "ease_out")
    fade_out = 1.0 if t < end - fx["_fade_out"] else max(0.0, (end - t) / fx["_fade_out"])
    if prog <= 0.01 or fade_out <= 0.01:
        return frame

    x0, y0, x1, y1 = fx["_region"]
    px0, py0, px1, py1 = x0 * W, y0 * H, x1 * W, y1 * H
    pad = fx["_width"] * 4 + 12
    bx0, by0 = max(0, int(px0 - pad)), max(0, int(py0 - pad))
    bx1, by1 = min(W, int(px1 + pad)), min(H, int(py1 + pad))
    if bx1 <= bx0 + 4 or by1 <= by0 + 4:
        return frame

    ov = Image.new("RGBA", (bx1 - bx0, by1 - by0), (0, 0, 0, 0))
    dr = ImageDraw.Draw(ov)
    col = fx["_color"]
    alpha = int(242 * fade_out)
    w_px = fx["_width"]
    style = fx["_style"]

    lx0, ly0, lx1, ly1 = px0 - bx0, py0 - by0, px1 - bx0, py1 - by0
    if style == "underline":
        n_pts = max(8, int(48 * prog))
        pts = []
        for i in range(n_pts + 1):
            f = (i / 48.0)
            if f > prog:
                break
            ux = lx0 + (lx1 - lx0) * f
            uy = ly1 + math.sin(f * math.pi * 2.5) * 2.5
            pts.append((ux, uy))
        if len(pts) >= 2:
            dr.line(pts, fill=(0, 0, 0, int(110 * fade_out)), width=w_px + 4, joint="curve")
            dr.line(pts, fill=(*col, alpha), width=w_px, joint="curve")
    elif style == "box":
        perim_pts = [
            (lx0, ly0), (lx1, ly0), (lx1, ly1), (lx0, ly1), (lx0, ly0)
        ]
        seg_lens = [math.hypot(b[0] - a[0], b[1] - a[1]) for a, b in zip(perim_pts, perim_pts[1:])]
        tot = sum(seg_lens) or 1.0
        target = tot * prog
        pts = [perim_pts[0]]
        acc = 0.0
        for (a, b), sl in zip(zip(perim_pts, perim_pts[1:]), seg_lens):
            if acc + sl <= target:
                pts.append(b)
                acc += sl
            else:
                frac = max(0.0, (target - acc) / max(sl, 1e-4))
                pts.append((a[0] + (b[0] - a[0]) * frac, a[1] + (b[1] - a[1]) * frac))
                break
        if len(pts) >= 2:
            dr.line(pts, fill=(0, 0, 0, int(105 * fade_out)), width=w_px + 4, joint="curve")
            dr.line(pts, fill=(*col, alpha), width=w_px, joint="curve")
    else:
        # Organic hand-drawn red circle (slightly over-rotates to 1.08 turns for authentic marker look)
        cx, cy = (lx0 + lx1) * 0.5, (ly0 + ly1) * 0.5
        rx, ry = max(6.0, (lx1 - lx0) * 0.5), max(6.0, (ly1 - ly0) * 0.5)
        steps = 72
        max_i = max(2, int(round(steps * prog)))
        pts = []
        for i in range(max_i + 1):
            frac = i / steps
            ang = -math.pi * 0.65 + frac * (2.0 * math.pi * 1.07)
            wob = 1.0 + 0.03 * math.sin(ang * 3.0 + 0.6) + 0.02 * math.cos(ang * 2.0)
            r_end = 1.0 + 0.04 * max(0.0, frac - 0.85) / 0.15
            pts.append((cx + rx * wob * r_end * math.cos(ang), cy + ry * wob * r_end * math.sin(ang)))
        if len(pts) >= 2:
            dr.line(pts, fill=(0, 0, 0, int(105 * fade_out)), width=w_px + 4, joint="curve")
            dr.line(pts, fill=(*col, alpha), width=w_px, joint="curve")

    out = frame.copy()
    out.paste(ov.convert("RGB"), (bx0, by0), ov.getchannel("A"))
    return out


def _apply_highlighter_sweep(frame: Image.Image, fx: dict[str, Any], t: float, W: int, H: int) -> Image.Image:
    at, dur, end = fx["_at"], fx["_dur"], fx["_end"]
    if t < at or t >= end:
        return frame
    prog = _ease((t - at) / dur, "ease_out")
    fade_out = 1.0 if t < end - fx["_fade_out"] else max(0.0, (end - t) / fx["_fade_out"])
    op = fx["_opacity"] * fade_out
    if prog <= 0.01 or op <= 0.01:
        return frame

    x0, y0, x1, y1 = fx["_region"]
    px0, py0 = int(x0 * W), int(y0 * H)
    px1 = int((x0 + (x1 - x0) * prog) * W)
    py1 = int(y1 * H)
    if px1 <= px0 + 2 or py1 <= py0 + 2:
        return frame

    out = frame.copy()
    roi = np.asarray(out.crop((px0, py0, px1, py1)), dtype=np.float32)
    col = np.array(fx["_color"], dtype=np.float32)[None, None, :]
    # Soft feathered edges on top/bottom/right tip
    rh, rw = roi.shape[:2]
    mask = np.ones((rh, rw), dtype=np.float32)
    if rw > 8:
        tip = min(14, rw // 3)
        mask[:, -tip:] *= np.linspace(1.0, 0.0, tip, dtype=np.float32)[None, :]
    if rh > 6:
        edge = min(4, rh // 4)
        mask[:edge, :] *= np.linspace(0.3, 1.0, edge, dtype=np.float32)[:, None]
        mask[-edge:, :] *= np.linspace(1.0, 0.3, edge, dtype=np.float32)[:, None]
    # Adaptive real-marker blend: Multiply on bright paper/phone screens (keeps black text razor-sharp),
    # translucent glow tint on dark-mode backgrounds.
    roi_mean = float(roi.mean())
    if roi_mean >= 115.0:
        eff_op = min(0.88, op * 1.55)
        alpha_m = (mask * eff_op)[:, :, None]
        target = roi * (col * (1.0 / 255.0))
    else:
        alpha_m = (mask * op)[:, :, None]
        target = col
    tinted = roi * (1.0 - alpha_m) + target * alpha_m
    out.paste(Image.fromarray(np.clip(tinted, 0, 255).astype(np.uint8), mode="RGB"), (px0, py0))
    return out


def _format_counter_val(val: float, fmt: str, prefix: str, suffix: str) -> str:
    if fmt == "mmss":
        sec = max(0, int(round(val)))
        return f"{prefix}{sec // 60:02d}:{sec % 60:02d}{suffix}"
    if fmt == "vnd":
        iv = int(round(val))
        sign = "-" if iv < 0 else ""
        s = f"{abs(iv):,}".replace(",", ".")
        return f"{prefix}{sign}{s}{suffix or 'đ'}"
    if fmt == "pct":
        return f"{prefix}{int(round(val))}%{suffix}"
    return f"{prefix}{int(round(val)):,}".replace(",", ".") + suffix


def _apply_animated_counter(frame: Image.Image, fx: dict[str, Any], t: float, W: int, H: int) -> Image.Image:
    s, e = fx["_start"], fx["_end"]
    env = _fade_env(t, s, e, fx["_fade"])
    if env <= 0.01:
        return frame
    u = _ease(min(1.0, max(0.0, (t - s) / fx["_count_dur"])), fx["_easing"])
    val = fx["_from_val"] + (fx["_to_val"] - fx["_from_val"]) * u
    txt = _format_counter_val(val, fx["_fmt"], fx["_prefix"], fx["_suffix"])

    palette = {
        "danger": (235, 48, 52),
        "warn": (255, 196, 20),
        "safe": (45, 205, 125),
        "info": (85, 195, 255),
    }
    accent = palette.get(fx["_style"], (235, 48, 52))
    # Subtle pulse when approaching end of countdown / drop
    pulse = 1.0 + (0.08 * math.sin((t - s) * 14.0) if (u > 0.72 and fx["_style"] == "danger") else 0.0)

    base = min(W, H)
    f_num = _get_font(max(28, int(base * 0.044 * pulse)), bold=True)
    f_lbl = _get_font(max(16, int(base * 0.020)), bold=True)
    tmp = ImageDraw.Draw(Image.new("RGBA", (8, 8)))
    nb = tmp.textbbox((0, 0), txt, font=f_num)
    nw, nh = nb[2] - nb[0], nb[3] - nb[1]
    lbl = fx["_label"]
    lw, lh = (0, 0)
    if lbl:
        lb = tmp.textbbox((0, 0), lbl, font=f_lbl)
        lw, lh = lb[2] - lb[0], lb[3] - lb[1]
    bw = max(nw, lw) + 44
    bh = nh + (lh + 12 if lbl else 0) + 30
    cx, cy = int(fx["_pos"][0] * W), int(fx["_pos"][1] * H)
    x0 = max(12, min(W - bw - 12, cx - bw // 2))
    y0 = max(12, min(H - bh - 12, cy - bh // 2))

    ov = Image.new("RGBA", (bw, bh), (0, 0, 0, 0))
    dr = ImageDraw.Draw(ov)
    dr.rounded_rectangle([0, 0, bw - 1, bh - 1], radius=16,
                         fill=(12, 14, 22, int(218 * env)), outline=(*accent, int(240 * env)), width=3)
    y = 14
    if lbl:
        dr.text((bw // 2, y + lh // 2), lbl, font=f_lbl, anchor="mm", fill=(*accent, int(245 * env)))
        y += lh + 10
    dr.text((bw // 2, y + nh // 2), txt, font=f_num, anchor="mm",
            fill=(255, 255, 255, int(255 * env)), stroke_width=3, stroke_fill=(0, 0, 0, int(220 * env)))

    out = frame.copy()
    out.paste(ov.convert("RGB"), (x0, y0), ov.getchannel("A"))
    return out


def _apply_typing_indicator(frame: Image.Image, fx: dict[str, Any], t: float, W: int, H: int) -> Image.Image:
    s, e = fx["_start"], fx["_end"]
    env = _fade_env(t, s, e, 0.14, 0.12)
    if env <= 0.01:
        return frame
    is_land = W > H
    bw, bh = (128, 56) if is_land else (142, 62)
    if fx["_pos"]:
        x0 = int(fx["_pos"][0] * W) - bw // 2
        y0 = int(fx["_pos"][1] * H) - bh // 2
    else:
        margin_x = 180 if is_land else 80
        x0 = margin_x if fx["_side"] == "left" else (W - margin_x - bw)
        y0 = int(fx["_y"]) if fx["_y"] is not None else (240 if is_land else 540)
    x0 = max(12, min(W - bw - 12, x0))
    y0 = max(12, min(H - bh - 12, y0))

    ov = Image.new("RGBA", (bw, bh), (0, 0, 0, 0))
    dr = ImageDraw.Draw(ov)
    is_right = fx["_side"] == "right"
    bg_col = (0, 132, 255, int(235 * env)) if is_right else (242, 244, 248, int(242 * env))
    dot_col = (240, 248, 255) if is_right else (85, 92, 108)
    dr.rounded_rectangle([0, 0, bw - 1, bh - 1], radius=bh // 2, fill=bg_col)
    dt = t - s
    r = max(5, bh // 9)
    for i in range(3):
        phase = dt * 6.5 - i * 0.9
        bounce = max(0.0, math.sin(phase))
        dx = bw // 2 + (i - 1) * (r * 3 + 2)
        dy = bh // 2 - int(round(bounce * 7.0))
        da = int((135 + 120 * bounce) * env)
        dr.ellipse([dx - r, dy - r, dx + r, dy + r], fill=(*dot_col, da))

    out = frame.copy()
    out.paste(ov.convert("RGB"), (x0, y0), ov.getchannel("A"))
    return out


# ----------------------------------------------------------------------------
# 6. Group 2 — Atmosphere, Lighting & Film Color Grading
# ----------------------------------------------------------------------------

def _apply_rain_layer(frame: Image.Image, fx: dict[str, Any], t: float, W: int, H: int) -> Image.Image:
    env = _fade_env(t, fx["_start"], fx["_end"], fx["_fade"])
    if env <= 0.01:
        return frame
    tiles = fx["_tiles"]
    rh, rw = tiles[0].shape
    rad = math.radians(fx["_angle_deg"])
    speed_half = fx["_speed"] * 0.5
    acc = np.zeros((rh, rw), dtype=np.uint16)
    for tile, sp_mul in zip(tiles, (0.65, 1.15)):
        dy = int(round(t * speed_half * sp_mul * math.cos(rad))) % rh
        dx = int(round(t * speed_half * sp_mul * math.sin(rad))) % rw
        rolled = np.roll(np.roll(tile, dy, axis=0), dx, axis=1)
        acc += rolled
    k_u8 = fx["_opacity"] * env
    mask_h = np.minimum(218, (acc * k_u8)).astype(np.uint8)
    if HAS_CV2:
        mask_u8 = cv2.resize(mask_h, (W, H), interpolation=cv2.INTER_LINEAR)
    else:
        mask_u8 = np.asarray(Image.fromarray(mask_h, mode="L").resize((W, H), Image.Resampling.BILINEAR))
    # Ultra-fast Pillow alpha paste of tinted rain streaks (zero 1080p float32 allocation!)
    out = frame.copy()
    out.paste(fx["_color"], (0, 0, W, H), Image.fromarray(mask_u8, mode="L"))
    return out


def _apply_ambient_particles(frame: Image.Image, fx: dict[str, Any], t: float, W: int, H: int) -> Image.Image:
    env = _fade_env(t, fx["_start"], fx["_end"], fx["_fade"])
    if env <= 0.01:
        return frame
    lt = t - fx["_sc_start"]
    out = frame.copy()
    col = fx["_color"]
    op_base = fx["_opacity"] * env
    sprites = fx["_sprites"]
    drift = fx["_dir"]
    for x0, y0, vy, vx_amp, fq, ph, sb, a_mul in fx["_particles"]:
        if drift == "up":
            yf = (y0 - vy * lt) % 1.0
        elif drift == "down":
            yf = (y0 + vy * lt) % 1.0
        else:
            yf = (y0 + math.sin(lt * fq * 0.7 + ph) * 0.03) % 1.0
        xf = (x0 + math.sin(lt * fq + ph) * vx_amp) % 1.0
        twinkle = 0.65 + 0.35 * math.sin(lt * (fq * 1.6) + ph * 2.0)
        a = op_base * a_mul * twinkle
        if a <= 0.02:
            continue
        sp = sprites[sb]
        sw, sh = sp.size
        px, py = int(xf * W) - sw // 2, int(yf * H) - sh // 2
        if px + sw <= 0 or py + sh <= 0 or px >= W or py >= H:
            continue
        m = sp.point(lambda p, k=a: int(p * k))
        out.paste(col, (px, py, px + sw, py + sh), m)
    return out


def _apply_light_sweep(frame: Image.Image, fx: dict[str, Any], t: float, W: int, H: int) -> Image.Image:
    s, e = fx["_start"], fx["_end"]
    env = _fade_env(t, s, e, fx["_fade"])
    if env <= 0.01:
        return frame
    span = max(0.1, e - s)
    cyc = ((t - s) / span * fx["_repeat"]) % 1.0
    pos = fx["_from_x"] + (fx["_to_x"] - fx["_from_x"]) * _ease(cyc, "smoothstep")
    dist = (fx["_coord"] - pos) / fx["_width"]
    band = np.exp(-dist * dist * 2.2) * (fx["_intensity"] * env * 255.0)
    if float(band.max()) <= 1.5:
        return frame
    b_u8 = np.clip(band, 0, 235).astype(np.uint8)
    if HAS_CV2:
        mask_u8 = cv2.resize(b_u8, (W, H), interpolation=cv2.INTER_LINEAR)
    else:
        mask_u8 = np.asarray(Image.fromarray(b_u8, mode="L").resize((W, H), Image.Resampling.BILINEAR))
    if fx["_mode"] == "shadow":
        out = frame.copy()
        out.paste(fx["_color"], (0, 0, W, H), Image.fromarray(mask_u8, mode="L"))
        return out
    # Fast additive light beam using uint8 saturating cv2.add (zero 1080p float32 allocation!)
    if HAS_CV2:
        c = fx["_color"]
        beam = np.empty((H, W, 3), dtype=np.uint8)
        beam[:, :, 0] = (mask_u8.astype(np.uint16) * c[0] >> 8).astype(np.uint8)
        beam[:, :, 1] = (mask_u8.astype(np.uint16) * c[1] >> 8).astype(np.uint8)
        beam[:, :, 2] = (mask_u8.astype(np.uint16) * c[2] >> 8).astype(np.uint8)
        return Image.fromarray(cv2.add(np.asarray(frame), beam), mode="RGB")
    out = frame.copy()
    out.paste(fx["_color"], (0, 0, W, H), Image.fromarray(mask_u8, mode="L"))
    return out


def _apply_color_mood(frame: Image.Image, fx: dict[str, Any], t: float, W: int, H: int) -> Image.Image:
    env = _fade_env(t, fx["_start"], fx["_end"], fx["_fade"]) * fx["_strength"]
    if env <= 0.01:
        return frame
    con = 1.0 + (fx["_contrast"] - 1.0) * env
    if HAS_CV2:
        v = np.arange(256, dtype=np.float32)
        lut = np.empty((1, 256, 3), dtype=np.uint8)
        for ch in range(3):
            g = 1.0 + (fx["_gain"][ch] - 1.0) * env
            lf = fx["_lift"][ch] * env
            lut[0, :, ch] = np.clip(((v - 128.0) * con + 128.0) * g + lf, 0, 255).astype(np.uint8)
        arr = cv2.LUT(np.asarray(frame), lut)
        # Fast optional integer grain directly on arr before converting back to PIL
        g_tile = fx.get("_grain_tile")
        if g_tile is not None and fx["_grain"] > 0.002:
            fi = int(round(t * 30.0))
            gh, gw = g_tile.shape
            rolled = np.roll(np.roll(g_tile, (fi * 37) % gh, axis=0), (fi * 53) % gw, axis=1)
            # Fast nearest upscale by slice-repeat + signed saturate via int16
            if env < 0.99:
                rolled = (rolled * env).astype(np.int16)
            g_pos = cv2.resize(np.maximum(rolled, 0).astype(np.uint8), (W, H), interpolation=cv2.INTER_NEAREST)
            g_neg = cv2.resize(np.maximum(-rolled, 0).astype(np.uint8), (W, H), interpolation=cv2.INTER_NEAREST)
            arr = cv2.add(arr, g_pos[:, :, None])
            arr = cv2.subtract(arr, g_neg[:, :, None])
        out = Image.fromarray(arr, mode="RGB")
    else:
        lut_l: list[int] = []
        for ch in range(3):
            g = 1.0 + (fx["_gain"][ch] - 1.0) * env
            lf = fx["_lift"][ch] * env
            for vv in range(256):
                val = ((vv - 128.0) * con + 128.0) * g + lf
                lut_l.append(max(0, min(255, int(round(val)))))
        out = frame.point(lut_l)

    # Optional soft vignette
    vig_m = fx.get("_vig_mask")
    if vig_m is not None and fx["_vignette"] > 0.01:
        v_amt = fx["_vignette"] * env
        vm = vig_m.point(lambda p, k=v_amt: int(p * k))
        out.paste((6, 8, 12), (0, 0, W, H), vm)
    return out


def _apply_chromatic_pulse(frame: Image.Image, fx: dict[str, Any], t: float, W: int, H: int) -> Image.Image:
    dt = t - fx["_at"]
    dur = fx["_dur"]
    if dt < 0.0 or dt >= dur:
        return frame
    # Fast attack, smooth exponential decay
    u = dt / dur
    env = (u / 0.18) if u < 0.18 else math.exp(-(u - 0.18) * 3.8)
    off = int(round(fx["_shift_px"] * env))
    if off < 1 and fx["_zoom_blur"] * env < 0.005:
        return frame

    out = fast_zoom_blur(frame, fx["_zoom_blur"] * env, steps=2) if fx["_zoom_blur"] > 0.004 else frame
    if off >= 1:
        arr = np.asarray(out)
        res = arr.copy()
        res[:, off:, 0] = arr[:, :-off, 0]     # Red channel shifted right
        res[:, :-off, 2] = arr[:, off:, 2]     # Blue channel shifted left
        out = Image.fromarray(res, mode="RGB")
    return out


def apply_l3_post_camera_fx(frame: Image.Image, fx: dict[str, Any], t: float, W: int, H: int) -> Image.Image:
    """Dispatch Level 3 post-camera detail_fx."""
    ft = fx["type"]
    if ft == "phone_waveform":
        return _apply_phone_waveform(frame, fx, t, W, H)
    if ft == "red_circle_draw":
        return _apply_red_circle_draw(frame, fx, t, W, H)
    if ft == "highlighter_sweep":
        return _apply_highlighter_sweep(frame, fx, t, W, H)
    if ft == "animated_counter":
        return _apply_animated_counter(frame, fx, t, W, H)
    if ft == "typing_indicator":
        return _apply_typing_indicator(frame, fx, t, W, H)
    if ft == "rain_layer":
        return _apply_rain_layer(frame, fx, t, W, H)
    if ft == "ambient_particles":
        return _apply_ambient_particles(frame, fx, t, W, H)
    if ft == "light_sweep":
        return _apply_light_sweep(frame, fx, t, W, H)
    if ft == "color_mood":
        return _apply_color_mood(frame, fx, t, W, H)
    if ft == "chromatic_pulse":
        return _apply_chromatic_pulse(frame, fx, t, W, H)
    return frame
