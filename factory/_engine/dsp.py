# -*- coding: utf-8 -*-
"""
Pure-NumPy DSP helpers (48 kHz). Ported 1:1 from borderWarSW779 Gate 3
(generate_sfx_bgm_gate3.py), with paths made project-relative.
"""
from __future__ import annotations

import math
import subprocess
import wave
from pathlib import Path

import numpy as np

from core import FFMPEG, rel

SR = 48000


def fft_convolve_1d(x: np.ndarray, h: np.ndarray) -> np.ndarray:
    n = len(x) + len(h) - 1
    n_fft = 1 << (n - 1).bit_length()
    Y = np.fft.rfft(x, n_fft) * np.fft.rfft(h, n_fft)
    return np.fft.irfft(Y, n_fft)[: len(x)]


def one_pole_lowpass(x: np.ndarray, cutoff_hz: float, sr: int = SR) -> np.ndarray:
    rc = 1.0 / (2.0 * math.pi * max(cutoff_hz, 1.0))
    dt = 1.0 / sr
    kernel_len = min(len(x), int(sr * min(0.25, 6.0 / max(cutoff_hz, 10.0))))
    if kernel_len < 4:
        return x.copy()
    t_k = np.arange(kernel_len, dtype=np.float64) / sr
    kernel = (1.0 / rc) * np.exp(-t_k / rc) * dt
    kernel /= np.sum(kernel)
    return fft_convolve_1d(x, kernel)


def fft_bandpass(x: np.ndarray, low_hz: float, high_hz: float, sr: int = SR, roll_width: float = 0.2) -> np.ndarray:
    """Smooth frequency-domain bandpass with raised-cosine transitions."""
    n = len(x)
    freqs = np.fft.rfftfreq(n, d=1.0 / sr)
    X = np.fft.rfft(x)
    mask = np.zeros_like(freqs)
    low_w = max(low_hz * roll_width, 8.0)
    high_w = max(high_hz * roll_width, 20.0)
    mask[(freqs >= low_hz) & (freqs <= high_hz)] = 1.0
    lt = (freqs >= max(0.0, low_hz - low_w)) & (freqs < low_hz)
    if np.any(lt):
        mask[lt] = 0.5 * (1.0 - np.cos(np.pi * (freqs[lt] - (low_hz - low_w)) / low_w))
    ht = (freqs > high_hz) & (freqs <= high_hz + high_w)
    if np.any(ht):
        mask[ht] = 0.5 * (1.0 + np.cos(np.pi * (freqs[ht] - high_hz) / high_w))
    return np.fft.irfft(X * mask, n=n)


def pink_noise(n: int, rng: np.random.Generator, sr: int = SR) -> np.ndarray:
    X = np.fft.rfft(rng.standard_normal(n))
    freqs = np.fft.rfftfreq(n, d=1.0 / sr)
    scale = np.ones_like(freqs)
    nz = freqs > 1.0
    scale[nz] = 1.0 / np.sqrt(freqs[nz])
    scale[0] = 0.0
    y = np.fft.irfft(X * scale, n=n)
    return y / (np.max(np.abs(y)) + 1e-9)


def brown_noise(n: int, rng: np.random.Generator, sr: int = SR) -> np.ndarray:
    X = np.fft.rfft(rng.standard_normal(n))
    freqs = np.fft.rfftfreq(n, d=1.0 / sr)
    scale = np.zeros_like(freqs)
    nz = freqs > 15.0
    scale[nz] = 1.0 / freqs[nz]
    y = np.fft.irfft(X * scale, n=n)
    return y / (np.max(np.abs(y)) + 1e-9)


def stereo_pan(mono: np.ndarray, pan: float = 0.0) -> np.ndarray:
    """Equal-power panner, pan in [-1, 1]. Returns (N, 2)."""
    angle = (pan + 1.0) * 0.25 * math.pi
    return np.column_stack([mono * math.cos(angle), mono * math.sin(angle)])


def add_reverb(stereo: np.ndarray, wet: float = 0.2, rt60: float = 0.6, seed: int = 7, sr: int = SR,
               band: tuple[float, float] = (120.0, 5000.0)) -> np.ndarray:
    """Noise-IR room/outdoor reverb with early reflections."""
    rng = np.random.default_rng(seed)
    ir_len = max(16, int(sr * rt60))
    t = np.arange(ir_len, dtype=np.float64) / sr
    decay = np.exp(-6.91 * t / rt60)
    ir_l = pink_noise(ir_len, rng, sr) * decay
    ir_r = pink_noise(ir_len, rng, sr) * decay
    for delay_ms, gain in [(11, 0.5), (23, 0.35), (41, 0.22), (67, 0.14)]:
        idx = int(sr * delay_ms / 1000.0)
        if idx < ir_len:
            ir_l[idx] += gain
            ir_r[min(ir_len - 1, idx + int(sr * 0.003))] += gain * 0.95
    ir_l = fft_bandpass(ir_l, band[0], band[1], sr)
    ir_r = fft_bandpass(ir_r, band[0], band[1], sr)
    ir_l /= np.sqrt(np.sum(ir_l ** 2)) + 1e-9
    ir_r /= np.sqrt(np.sum(ir_r ** 2)) + 1e-9
    wl = fft_convolve_1d(stereo[:, 0], ir_l)
    wr = fft_convolve_1d(stereo[:, 1], ir_r)
    return stereo * (1.0 - wet) + np.column_stack([wl, wr]) * wet


def normalize_to_dbfs(audio: np.ndarray, target_peak_db: float = -6.0) -> np.ndarray:
    peak = float(np.max(np.abs(audio))) if audio.size else 0.0
    if peak < 1e-9:
        return audio
    return audio * (10.0 ** (target_peak_db / 20.0) / peak)


def fade_in_out(audio: np.ndarray, fade_in_sec: float = 0.05, fade_out_sec: float = 0.05, sr: int = SR) -> np.ndarray:
    out = audio.copy()
    n = len(out)
    n_in, n_out = min(n, int(sr * fade_in_sec)), min(n, int(sr * fade_out_sec))
    if n_in > 1:
        env = 0.5 * (1.0 - np.cos(np.pi * np.linspace(0.0, 1.0, n_in)))
        out[:n_in] *= env[:, None] if out.ndim == 2 else env
    if n_out > 1:
        env = 0.5 * (1.0 + np.cos(np.pi * np.linspace(0.0, 1.0, n_out)))
        out[-n_out:] *= env[:, None] if out.ndim == 2 else env
    return out


def to_stereo(x: np.ndarray) -> np.ndarray:
    return np.column_stack([x, x]) if x.ndim == 1 else x[:, :2]


def fit_length(x: np.ndarray, n: int, loop_xfade_sec: float = 0.5) -> np.ndarray:
    """Trim or loop (with crossfade) a stereo clip to exactly n samples."""
    x = to_stereo(x)
    if len(x) >= n:
        return x[:n].copy()
    xf = min(int(loop_xfade_sec * SR), len(x) // 4)
    out = x.copy()
    while len(out) < n:
        if xf > 0:
            ramp = np.linspace(0.0, 1.0, xf)[:, None]
            head = out[-xf:] * (1.0 - ramp) + x[:xf] * ramp
            out = np.concatenate([out[:-xf], head, x[xf:]])
        else:
            out = np.concatenate([out, x])
    return out[:n].copy()


def save_wav(audio: np.ndarray, wav_path: Path, mp3: bool = False, sr: int = SR) -> dict:
    """Save float [-1,1] array as 16-bit PCM WAV (+ optional 192k MP3). Returns metrics."""
    wav_path = Path(wav_path)
    wav_path.parent.mkdir(parents=True, exist_ok=True)
    clipped = np.clip(audio, -0.999, 0.999)
    pcm16 = (clipped * 32767.0).astype(np.int16)
    n_ch = 1 if pcm16.ndim == 1 else pcm16.shape[1]
    with wave.open(str(wav_path), "wb") as wf:
        wf.setnchannels(n_ch)
        wf.setsampwidth(2)
        wf.setframerate(sr)
        wf.writeframes(pcm16.tobytes())
    mp3_path = None
    if mp3:
        mp3_path = wav_path.with_suffix(".mp3")
        subprocess.run([FFMPEG, "-y", "-v", "error", "-i", str(wav_path), "-c:a", "libmp3lame", "-b:a", "192k",
                        str(mp3_path)], check=True)
    return {
        "wav_path": rel(wav_path),
        "mp3_path": rel(mp3_path) if mp3_path else None,
        **metrics(clipped, sr),
    }


def metrics(audio: np.ndarray, sr: int = SR) -> dict:
    peak = float(np.max(np.abs(audio))) if audio.size else 0.0
    rms = float(np.sqrt(np.mean(audio ** 2))) if audio.size else 0.0
    return {
        "duration_sec": round(len(audio) / sr, 3),
        "channels": 1 if audio.ndim == 1 else audio.shape[1],
        "sample_rate": sr,
        "peak_dbfs": round(20.0 * math.log10(max(peak, 1e-9)), 2),
        "rms_dbfs": round(20.0 * math.log10(max(rms, 1e-9)), 2),
    }


def read_wav_stereo(wav_path: Path, target_sr: int = SR) -> np.ndarray:
    """Read WAV as float stereo. Non-48k or non-16-bit files are converted via ffmpeg first."""
    wav_path = Path(wav_path)
    with wave.open(str(wav_path), "rb") as wf:
        n_ch, sw, fr, nf = wf.getnchannels(), wf.getsampwidth(), wf.getframerate(), wf.getnframes()
        raw = wf.readframes(nf) if (sw == 2 and fr == target_sr) else None
    if raw is None:
        return read_any_audio(wav_path, target_sr)
    s = np.frombuffer(raw, dtype=np.int16).astype(np.float64) / 32768.0
    return to_stereo(s) if n_ch == 1 else s.reshape(-1, n_ch)[:, :2]


def read_any_audio(path: Path, target_sr: int = SR) -> np.ndarray:
    """Decode any audio file (mp3/wav/ogg...) to float stereo @ target_sr using ffmpeg."""
    res = subprocess.run(
        [FFMPEG, "-v", "error", "-i", str(path), "-f", "s16le", "-ac", "2", "-ar", str(target_sr), "-"],
        check=True, capture_output=True,
    )
    s = np.frombuffer(res.stdout, dtype=np.int16).astype(np.float64) / 32768.0
    return s.reshape(-1, 2)


def place_clip(canvas: np.ndarray, clip: np.ndarray, start_sec: float, gain_db: float = 0.0) -> None:
    idx = int(round(start_sec * SR))
    if idx >= len(canvas) or idx < 0:
        return
    avail = min(len(clip), len(canvas) - idx)
    if avail > 0:
        canvas[idx: idx + avail] += to_stereo(clip)[:avail] * (10.0 ** (gain_db / 20.0))


def duck_envelope(total_samples: int, windows: list[tuple[float, float, float]],
                  attack_sec: float = 0.25, release_sec: float = 0.45) -> np.ndarray:
    """Linear gain envelope ducking by duck_db during each (start, end, duck_db) window."""
    env_db = np.zeros(total_samples, dtype=np.float64)
    t = np.arange(total_samples, dtype=np.float64) / SR
    total_dur = total_samples / SR
    for start_s, end_s, duck_db in windows:
        w = np.zeros(total_samples, dtype=np.float64)
        s0, s1, e0, e1 = max(0.0, start_s - attack_sec), start_s, end_s, min(total_dur, end_s + release_sec)
        att = (t >= s0) & (t < s1)
        hold = (t >= s1) & (t <= e0)
        relm = (t > e0) & (t <= e1)
        if np.any(att):
            w[att] = 0.5 * (1.0 - np.cos(np.pi * (t[att] - s0) / max(s1 - s0, 1e-4))) * duck_db
        w[hold] = duck_db
        if np.any(relm):
            w[relm] = 0.5 * (1.0 + np.cos(np.pi * (t[relm] - e0) / max(e1 - e0, 1e-4))) * duck_db
        env_db = np.minimum(env_db, w)
    return 10.0 ** (env_db / 20.0)


def soft_limit(x: np.ndarray, knee: float = 0.72, headroom: float = 0.17) -> np.ndarray:
    """Transparent soft-knee limiter (ceiling ≈ knee+headroom ≈ -1 dBFS)."""
    a = np.abs(x)
    return np.where(a > knee, np.sign(x) * (knee + headroom * np.tanh((a - knee) / headroom)), x)
