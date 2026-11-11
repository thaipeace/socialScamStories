# -*- coding: utf-8 -*-
"""
Shared Procedural Audio Library (`03_ENGINE/sfx_library.py`) dùng chung cho cả hai nhà máy `factory619` và `factory196`.
Mọi preset trả về mảng stereo float64 (N, 2) @ 48 kHz, đã chuẩn hóa đỉnh.
"""
from __future__ import annotations

from typing import Callable

import numpy as np

from dsp import (SR, add_reverb, brown_noise, fade_in_out, fft_bandpass, normalize_to_dbfs, pink_noise,
                 stereo_pan)


def _t(n: int) -> np.ndarray:
    return np.arange(n, dtype=np.float64) / SR


def _bell(f0: float, dur: float, rng: np.random.Generator, bright: float = 1.0) -> np.ndarray:
    t = _t(int(SR * dur))
    out = np.zeros_like(t)
    for ratio, dec, amp in [(1.0, 4.0, 1.0), (2.0, 6.0, 0.45 * bright), (2.76, 8.0, 0.3 * bright),
                            (4.07, 12.0, 0.18 * bright), (5.43, 16.0, 0.1 * bright)]:
        out += np.sin(2 * np.pi * f0 * ratio * rng.uniform(0.998, 1.002) * t) * np.exp(-t * dec) * amp
    return out


# ============================================================================
# LAYER 1 – AMBIENCE (bối cảnh)
# ============================================================================

def amb_room_tone(dur: float, seed: int = 11) -> np.ndarray:
    """Phòng khách/nhà ở: nền tĩnh, tiếng tủ lạnh 50Hz khẽ, xe cộ rất xa."""
    rng = np.random.default_rng(seed)
    n = int(SR * dur)
    t = _t(n)
    hum = (np.sin(2 * np.pi * 50 * t) * 0.18 + np.sin(2 * np.pi * 100 * t) * 0.08) * (0.8 + 0.2 * np.sin(2 * np.pi * 0.07 * t))
    air = fft_bandpass(pink_noise(n, rng), 80, 2200) * 0.55
    far = fft_bandpass(brown_noise(n, rng), 40, 400) * 0.35 * (0.6 + 0.4 * np.sin(2 * np.pi * 0.05 * t + 1.0))
    mono = hum + air + far
    st = np.column_stack([mono, fft_bandpass(pink_noise(n, rng), 80, 2200) * 0.55 + hum + far])
    return normalize_to_dbfs(fade_in_out(st, 0.6, 0.6), -20.0)


def amb_night_room(dur: float, seed: int = 12) -> np.ndarray:
    """Phòng đêm: tiếng dế ngoài cửa sổ + đồng hồ tích tắc."""
    rng = np.random.default_rng(seed)
    n = int(SR * dur)
    base = amb_room_tone(dur, seed) * 0.6
    crick = np.zeros(n)
    for c in np.arange(0.2, dur, 0.9):
        idx = int((c + rng.uniform(-0.1, 0.1)) * SR)
        ln = int(0.35 * SR)
        if idx + ln < n:
            tt = _t(ln)
            chirp = np.sin(2 * np.pi * 4300 * tt) * (0.5 + 0.5 * np.sign(np.sin(2 * np.pi * 32 * tt))) * np.sin(np.pi * tt / 0.35)
            crick[idx: idx + ln] += chirp * 0.09
    tick = np.zeros(n)
    for k, c in enumerate(np.arange(0.0, dur, 1.0)):
        idx = int(c * SR)
        ln = int(0.03 * SR)
        if idx + ln < n:
            tick[idx: idx + ln] += fft_bandpass(rng.standard_normal(ln), 1800, 6000) * np.exp(-_t(ln) * 220) * (0.25 if k % 2 else 0.2)
    st = base + stereo_pan(crick, 0.55) + stereo_pan(tick, -0.3)
    return normalize_to_dbfs(fade_in_out(st, 0.6, 0.6), -19.0)


def amb_office(dur: float, seed: int = 13) -> np.ndarray:
    """Văn phòng/quán cà phê máy lạnh: tiếng máy lạnh + gõ phím xa xa."""
    rng = np.random.default_rng(seed)
    n = int(SR * dur)
    ac = fft_bandpass(pink_noise(n, rng), 150, 3500) * 0.6
    keys = np.zeros(n)
    tcur = 0.3
    while tcur < dur - 0.1:
        idx = int(tcur * SR)
        ln = int(0.025 * SR)
        keys[idx: idx + ln] += fft_bandpass(rng.standard_normal(ln), 1500, 7000) * np.exp(-_t(ln) * 260) * rng.uniform(0.05, 0.12)
        tcur += rng.uniform(0.08, 0.25) if rng.random() > 0.08 else rng.uniform(0.8, 2.0)
    st = np.column_stack([ac, fft_bandpass(pink_noise(n, rng), 150, 3500) * 0.6]) + stereo_pan(keys, -0.45)
    return normalize_to_dbfs(fade_in_out(st, 0.6, 0.6), -20.0)


def amb_street(dur: float, seed: int = 14) -> np.ndarray:
    """Đường phố Việt Nam: nền xe máy, thỉnh thoảng một chiếc chạy ngang, còi xa."""
    rng = np.random.default_rng(seed)
    n = int(SR * dur)
    bed = fft_bandpass(brown_noise(n, rng), 50, 900) * 0.7 + fft_bandpass(pink_noise(n, rng), 300, 3000) * 0.25
    passes_l = np.zeros(n)
    passes_r = np.zeros(n)
    for c in np.arange(rng.uniform(0.5, 2.0), dur, rng.uniform(2.5, 4.5)):
        ln = int(3.0 * SR)
        idx = int(c * SR)
        if idx + ln >= n:
            break
        tt = _t(ln)
        f = 95 + 25 * np.sin(np.pi * tt / 3.0)
        eng = np.sign(np.sin(2 * np.pi * np.cumsum(f) / SR)) * 0.3 + fft_bandpass(rng.standard_normal(ln), 200, 1600) * 0.5
        env = np.exp(-((tt - 1.5) / 0.6) ** 2)
        pan = np.linspace(-1, 1, ln) if rng.random() > 0.5 else np.linspace(1, -1, ln)
        sig = fft_bandpass(eng * env, 80, 2500) * 0.6
        passes_l[idx: idx + ln] += sig * np.cos((pan + 1) * np.pi / 4)
        passes_r[idx: idx + ln] += sig * np.sin((pan + 1) * np.pi / 4)
    for c in rng.uniform(1.0, max(1.5, dur - 1.0), size=max(1, int(dur / 8))):
        idx = int(c * SR)
        ln = int(0.35 * SR)
        if idx + ln < n:
            honk = (np.sin(2 * np.pi * 420 * _t(ln)) + 0.6 * np.sin(2 * np.pi * 520 * _t(ln))) * np.sin(np.pi * _t(ln) / 0.35)
            passes_l[idx: idx + ln] += honk * 0.06
            passes_r[idx: idx + ln] += honk * 0.04
    st = np.column_stack([bed + passes_l, bed * 0.95 + passes_r])
    return normalize_to_dbfs(fade_in_out(st, 0.8, 0.8), -18.0)


def amb_crowd(dur: float, seed: int = 15) -> np.ndarray:
    """Đám đông/hội trường/chợ: tiếng người nói lao xao không rõ chữ."""
    rng = np.random.default_rng(seed)
    n = int(SR * dur)
    t = _t(n)
    layers = np.zeros((n, 2))
    for i in range(10):
        voice = fft_bandpass(pink_noise(n, rng), 250 + 30 * i, 2600)
        syll = 0.5 + 0.5 * np.sin(2 * np.pi * rng.uniform(3.0, 5.5) * t + rng.uniform(0, 6.28))
        phrase = 0.5 + 0.5 * np.sin(2 * np.pi * rng.uniform(0.15, 0.4) * t + rng.uniform(0, 6.28))
        layers += stereo_pan(voice * syll * phrase, rng.uniform(-0.8, 0.8))
    st = add_reverb(layers, wet=0.35, rt60=1.0, seed=seed)
    return normalize_to_dbfs(fade_in_out(st, 0.8, 0.8), -19.0)


def amb_rain(dur: float, seed: int = 16) -> np.ndarray:
    rng = np.random.default_rng(seed)
    n = int(SR * dur)
    st = np.column_stack([fft_bandpass(pink_noise(n, rng), 400, 9000), fft_bandpass(pink_noise(n, rng), 400, 9000)])
    drops = np.zeros(n)
    for c in rng.uniform(0, dur - 0.05, size=int(dur * 25)):
        idx = int(c * SR)
        ln = int(0.02 * SR)
        drops[idx: idx + ln] += fft_bandpass(rng.standard_normal(ln), 2000, 8000) * np.exp(-_t(ln) * 300) * rng.uniform(0.1, 0.4)
    st = st * 0.5 + stereo_pan(drops, 0.2)
    return normalize_to_dbfs(fade_in_out(st, 0.8, 0.8), -19.0)


# ============================================================================
# LAYER 2 – FOLEY (điểm nhấn hành động, đặt chính xác theo giây)
# ============================================================================

def fx_phone_ring(dur: float = 4.0, seed: int = 21) -> np.ndarray:
    """Chuông điện thoại di động (2 hồi): giai điệu ngắn 4 nốt lặp."""
    rng = np.random.default_rng(seed)
    n = int(SR * dur)
    out = np.zeros(n)
    notes = [1318.5, 1568.0, 1318.5, 1975.5]
    cycle = 2.0
    for c0 in np.arange(0.0, dur - 0.2, cycle):
        for k, f in enumerate(notes):
            idx = int((c0 + k * 0.16) * SR)
            note = _bell(f, 0.32, rng, bright=0.6) * 0.5
            end = min(n, idx + len(note))
            out[idx:end] += note[: end - idx]
    st = add_reverb(stereo_pan(fft_bandpass(out, 600, 7000), 0.1), wet=0.15, rt60=0.4, seed=seed)
    return normalize_to_dbfs(fade_in_out(st, 0.005, 0.1), -6.0)


def fx_phone_vibrate(dur: float = 2.4, seed: int = 22) -> np.ndarray:
    """Điện thoại rung trên mặt bàn: 2-3 cụm rung."""
    n = int(SR * dur)
    t = _t(n)
    gate = ((t % 1.0) < 0.55).astype(float)
    buzz = np.sign(np.sin(2 * np.pi * 172 * t)) * 0.4 + np.sin(2 * np.pi * 344 * t) * 0.3
    rattle = fft_bandpass(np.random.default_rng(seed).standard_normal(n), 900, 4000) * 0.15
    sig = fft_bandpass((buzz + rattle) * gate, 120, 4000)
    return normalize_to_dbfs(fade_in_out(stereo_pan(sig, -0.05), 0.01, 0.05), -8.0)


def fx_notification(dur: float = 0.8, seed: int = 23) -> np.ndarray:
    """Thông báo tin nhắn đến: 'ding' 2 nốt."""
    rng = np.random.default_rng(seed)
    out = np.zeros(int(SR * dur))
    for k, f in enumerate([1760.0, 2349.3]):
        idx = int(k * 0.11 * SR)
        b = _bell(f, dur - 0.11 * k, rng, 0.5) * 0.6
        out[idx: idx + len(b)] += b[: len(out) - idx]
    return normalize_to_dbfs(add_reverb(stereo_pan(out, 0.05), 0.12, 0.35, seed), -7.0)


def fx_bank_ting(dur: float = 1.4, seed: int = 24) -> np.ndarray:
    """'Ting ting' biến động số dư – âm thanh nhận diện của kênh."""
    rng = np.random.default_rng(seed)
    out = np.zeros(int(SR * dur))
    for k, f in enumerate([2093.0, 2637.0]):
        idx = int(k * 0.18 * SR)
        b = _bell(f, dur - 0.18 * k, rng, 0.9) * 0.7
        out[idx: idx + len(b)] += b[: len(out) - idx]
    return normalize_to_dbfs(add_reverb(stereo_pan(out, 0.0), 0.2, 0.6, seed), -6.0)


def fx_message_send(dur: float = 0.5, seed: int = 25) -> np.ndarray:
    """Gửi tin nhắn/chuyển khoản thành công: whoosh ngắn + pop."""
    rng = np.random.default_rng(seed)
    n = int(SR * dur)
    t = _t(n)
    sweep = fft_bandpass(pink_noise(n, rng), 600, 6000) * np.sin(np.pi * np.minimum(t / 0.3, 1.0)) * np.exp(-t * 6)
    pop = np.sin(2 * np.pi * (900 + 900 * t) * t) * np.exp(-np.maximum(t - 0.22, 0) * 40) * (t > 0.22) * 0.6
    st = np.column_stack([sweep * 0.7 + pop, sweep * 0.5 + pop])
    return normalize_to_dbfs(fade_in_out(st, 0.005, 0.05), -9.0)


def fx_typing(dur: float = 2.0, seed: int = 26) -> np.ndarray:
    """Gõ phím điện thoại liên tục (soạn tin)."""
    rng = np.random.default_rng(seed)
    n = int(SR * dur)
    out = np.zeros(n)
    c = 0.02
    while c < dur - 0.04:
        idx = int(c * SR)
        ln = int(0.03 * SR)
        tap = fft_bandpass(rng.standard_normal(ln), 1200, 6500) * np.exp(-_t(ln) * 300) + np.sin(2 * np.pi * 260 * _t(ln)) * np.exp(-_t(ln) * 200) * 0.4
        out[idx: idx + ln] += tap * rng.uniform(0.6, 1.0)
        c += rng.uniform(0.07, 0.16)
    return normalize_to_dbfs(stereo_pan(out, 0.1), -10.0)


def fx_door_knock(dur: float = 1.2, seed: int = 27) -> np.ndarray:
    """Gõ cửa gỗ dồn dập."""
    rng = np.random.default_rng(seed)
    n = int(SR * dur)
    out = np.zeros(n)
    for k, kt in enumerate([0.02, 0.22, 0.41, 0.60]):
        idx = int(kt * SR)
        ln = int(0.17 * SR)
        tt = _t(ln)
        wood = (np.sin(2 * np.pi * 118 * tt) * np.exp(-tt * 32) * 0.88 + np.sin(2 * np.pi * 245 * tt) * np.exp(-tt * 42) * 0.7
                + np.sin(2 * np.pi * 490 * tt) * np.exp(-tt * 58) * 0.45)
        knuckle = fft_bandpass(rng.standard_normal(ln), 500, 2600) * np.exp(-tt * 90) * 0.65
        out[idx: idx + ln] += np.tanh((wood + knuckle) * (1.25 + 0.1 * k))
    return normalize_to_dbfs(add_reverb(stereo_pan(out, -0.05), 0.18, 0.45, seed), -5.0)


def fx_footsteps(dur: float = 2.0, seed: int = 28) -> np.ndarray:
    """Bước chân trong nhà (dép) đều nhịp."""
    rng = np.random.default_rng(seed)
    n = int(SR * dur)
    out = np.zeros((n, 2))
    for i, c in enumerate(np.arange(0.05, dur - 0.15, 0.48)):
        idx = int(c * SR)
        ln = int(0.14 * SR)
        tt = _t(ln)
        step = np.sin(2 * np.pi * 90 * tt) * np.exp(-tt * 40) * 0.5 + fft_bandpass(pink_noise(ln, rng), 300, 3000) * np.exp(-tt * 30) * 0.5
        out[idx: idx + ln] += stereo_pan(step, -0.15 if i % 2 else 0.15)
    return normalize_to_dbfs(add_reverb(out, 0.15, 0.4, seed), -9.0)


def fx_heartbeat(dur: float = 4.0, seed: int = 29, bpm: float = 96.0) -> np.ndarray:
    """Nhịp tim dồn dập (lúc nạn nhân hoảng sợ)."""
    n = int(SR * dur)
    out = np.zeros(n)
    period = 60.0 / bpm
    for c in np.arange(0.05, dur - 0.3, period):
        for off, amp in [(0.0, 1.0), (0.22, 0.6)]:
            idx = int((c + off) * SR)
            ln = int(0.2 * SR)
            if idx + ln < n:
                tt = _t(ln)
                out[idx: idx + ln] += np.sin(2 * np.pi * (60 - 90 * tt) * tt) * np.exp(-tt * 22) * amp
    return normalize_to_dbfs(stereo_pan(out, 0.0), -7.0)


def fx_impact(dur: float = 2.0, seed: int = 30) -> np.ndarray:
    """Cú 'BÙM' điện ảnh khi lộ mặt kẻ lừa."""
    rng = np.random.default_rng(seed)
    n = int(SR * dur)
    tt = _t(n)
    f_sub = 40 + 50 * np.exp(-tt * 14)
    sub = np.sin(2 * np.pi * np.cumsum(f_sub) / SR) * np.exp(-tt * 2.8)
    body = np.sin(2 * np.pi * np.cumsum(90 + 60 * np.exp(-tt * 20)) / SR) * np.exp(-tt * 7) * 0.6
    crack = fft_bandpass(pink_noise(n, rng), 200, 5000) * np.exp(-tt * 25) * 0.6
    sig = np.tanh((sub + body + crack) * 1.4)
    return normalize_to_dbfs(add_reverb(stereo_pan(sig, 0), 0.3, 1.4, seed), -3.5)


def fx_riser(dur: float = 3.0, seed: int = 31) -> np.ndarray:
    """Riser căng dần dẫn vào khoảnh khắc 'bóc trần'."""
    rng = np.random.default_rng(seed)
    n = int(SR * dur)
    t = _t(n)
    u = t / dur
    f = 180 * (2 ** (u * 2.5))
    tone = np.sin(2 * np.pi * np.cumsum(f) / SR) * 0.35 + np.sin(2 * np.pi * np.cumsum(f * 1.5) / SR) * 0.2
    noise = fft_bandpass(pink_noise(n, rng), 800, 9000) * 0.5
    env = u ** 2.2
    st = np.column_stack([(tone + noise) * env, (tone * 0.9 + fft_bandpass(pink_noise(n, rng), 800, 9000) * 0.5) * env])
    return normalize_to_dbfs(fade_in_out(st, 0.1, 0.02), -6.0)


def fx_glitch(dur: float = 0.9, seed: int = 32) -> np.ndarray:
    """Glitch kỹ thuật số – dùng cho deepfake / màn hình giả bị lộ."""
    rng = np.random.default_rng(seed)
    n = int(SR * dur)
    out = np.zeros(n)
    c = 0.0
    while c < dur - 0.02:
        ln = int(rng.uniform(0.01, 0.06) * SR)
        idx = int(c * SR)
        kind = rng.integers(0, 3)
        tt = _t(ln)
        if kind == 0:
            seg = np.sign(np.sin(2 * np.pi * rng.uniform(200, 3000) * tt))
        elif kind == 1:
            seg = rng.standard_normal(ln)
        else:
            seg = np.round(np.sin(2 * np.pi * rng.uniform(60, 600) * tt) * 4) / 4
        out[idx: idx + ln] += seg[: n - idx] * rng.uniform(0.3, 0.8)
        c += ln / SR + rng.uniform(0.0, 0.03)
    st = np.column_stack([out, np.roll(out, int(0.004 * SR))])
    return normalize_to_dbfs(fade_in_out(st, 0.003, 0.02), -8.0)


def fx_call_end(dur: float = 1.6, seed: int = 33) -> np.ndarray:
    """Tút... tút... tút – cuộc gọi bị cúp."""
    n = int(SR * dur)
    out = np.zeros(n)
    for c in [0.0, 0.5, 1.0]:
        idx = int(c * SR)
        ln = int(0.28 * SR)
        if idx + ln <= n:
            out[idx: idx + ln] += np.sin(2 * np.pi * 425 * _t(ln)) * 0.6
    sig = fft_bandpass(out, 300, 3400)
    return normalize_to_dbfs(fade_in_out(stereo_pan(sig, 0.0), 0.005, 0.02), -10.0)


def fx_whistle(dur: float = 1.6, seed: int = 34) -> np.ndarray:
    """Còi bảo vệ (còi bi): 2 hồi tuýt ngắn có rung bi."""
    rng = np.random.default_rng(seed)
    n = int(SR * dur)
    t = _t(n)
    out = np.zeros(n)
    for s0, ln in [(0.02, 0.35), (0.5, 0.9)]:
        m = (t >= s0) & (t < s0 + ln)
        tt = t[m] - s0
        trill = 1.0 + 0.04 * np.sign(np.sin(2 * np.pi * 28 * tt))
        env = np.minimum(1.0, tt / 0.02) * np.minimum(1.0, (ln - tt) / 0.05)
        out[m] = np.sin(2 * np.pi * np.cumsum(2900 * trill) / SR) * env * 0.7
    out += fft_bandpass(rng.standard_normal(n), 2500, 6000) * (np.abs(out) > 0.01) * 0.12
    st = add_reverb(stereo_pan(out, 0.15), 0.25, 0.9, seed)
    return normalize_to_dbfs(st, -7.0)


def fx_school_bell(dur: float = 3.0, seed: int = 35) -> np.ndarray:
    """Trống/chuông tan trường xa xa (3 tiếng ngân)."""
    rng = np.random.default_rng(seed)
    out = np.zeros(int(SR * dur))
    for c in [0.0, 0.7, 1.4]:
        b = _bell(880.0, dur - c, rng, 0.8) * 0.5
        idx = int(c * SR)
        out[idx: idx + len(b)] += b[: len(out) - idx]
    return normalize_to_dbfs(add_reverb(stereo_pan(out, -0.3), 0.45, 1.6, seed), -10.0)


def fx_chapter_sting(dur: float = 2.2, seed: int = 36) -> np.ndarray:
    """Âm hiệu chuyển Hồi / Chapter: tiếng trầm ấm + chuông trầm ngân vang."""
    rng = np.random.default_rng(seed)
    n = int(SR * dur)
    tt = _t(n)
    low = np.sin(2 * np.pi * 110.0 * tt) * np.exp(-tt * 2.5) * 0.7
    chime = _bell(440.0, dur, rng, bright=0.45) * 0.5 + _bell(659.25, dur, rng, bright=0.35) * 0.35
    st = add_reverb(stereo_pan(low + chime, 0.0), wet=0.35, rt60=1.3, seed=seed)
    return normalize_to_dbfs(fade_in_out(st, 0.01, 0.25), -6.5)


# ============================================================================
# LAYER 3 – BGM (nhạc nền)
# ============================================================================

def bgm_investigative_story(dur: float, seed: int = 40, bpm: float = 84.0) -> np.ndarray:
    """Nhạc nền dẫn chuyện điều tra sâu lắng (A minor) cho các Hồi mở đầu phim dài."""
    rng = np.random.default_rng(seed)
    n = int(SR * dur)
    t = _t(n)
    out = np.zeros((n, 2))
    for f, pan in [(110.0, -0.2), (164.81, 0.2), (220.0, -0.1), (261.63, 0.15)]:
        w = np.sin(2 * np.pi * f * t + rng.uniform(0, 6.28)) * (0.6 + 0.4 * np.sin(2 * np.pi * 0.09 * t)) * 0.12
        out += stereo_pan(w, pan)
    notes = [440.0, 523.25, 659.25, 587.33, 493.88, 392.0, 440.0, 329.63]
    step = 60.0 / bpm
    arp = np.zeros(n)
    for k, c in enumerate(np.arange(0.3, dur - 0.6, step)):
        idx = int(c * SR)
        b = _bell(notes[k % len(notes)], min(1.1, dur - c), rng, bright=0.3) * 0.18
        end = min(n, idx + len(b))
        arp[idx:end] += b[: end - idx]
    out += add_reverb(stereo_pan(arp, 0.15), wet=0.35, rt60=1.1, seed=seed)
    return normalize_to_dbfs(fade_in_out(out, 1.0, 1.5), -16.0)


def bgm_tension_drone(dur: float, seed: int = 41) -> np.ndarray:
    """Drone trầm căng thẳng (D minor) + nhịp tim ngầm."""
    rng = np.random.default_rng(seed)
    n = int(SR * dur)
    t = _t(n)
    l = np.zeros(n)
    r = np.zeros(n)
    for freq, amp, lfo_hz, pan in [(36.71, 0.45, 0.07, 0.0), (73.42, 0.65, 0.11, -0.3), (73.58, 0.55, 0.13, 0.3),
                                   (110.0, 0.42, 0.09, -0.45), (146.83, 0.3, 0.15, 0.45), (174.61, 0.22, 0.08, -0.2)]:
        vib = 1.0 + 0.0025 * np.sin(2 * np.pi * 4.2 * t + rng.uniform(0, 6.28))
        ph = 2 * np.pi * np.cumsum(freq * vib) / SR
        lfo = 0.65 + 0.35 * np.sin(2 * np.pi * lfo_hz * t + rng.uniform(0, 6.28))
        w = (np.sin(ph) + 0.35 * np.sin(2 * ph) * lfo + 0.15 * np.sin(3 * ph) * (1 - lfo)) * amp
        p = stereo_pan(w, pan)
        l += p[:, 0]
        r += p[:, 1]
    arc = np.linspace(0.5, 1.0, n)
    pulse = np.zeros(n)
    for pt in np.arange(1.5, dur - 1.0, 1.1):
        for off, amp in [(0.0, 0.3), (0.24, 0.17)]:
            idx = int((pt + off) * SR)
            ln = int(0.18 * SR)
            if idx + ln < n:
                tt = _t(ln)
                pulse[idx: idx + ln] += np.sin(2 * np.pi * (58 - 110 * tt) * tt) * np.exp(-tt * 24) * amp
    st = np.column_stack([fft_bandpass(l, 32, 480) * arc + pulse, fft_bandpass(r, 32, 480) * arc + pulse])
    return normalize_to_dbfs(fade_in_out(st, 0.8, 1.2), -15.0)


def bgm_suspense_pulse(dur: float, seed: int = 42, bpm: float = 110.0) -> np.ndarray:
    """Nhạc nền 'thao túng tâm lý': đồng hồ tích tắc + bass pulse đều, tạo áp lực thời gian."""
    rng = np.random.default_rng(seed)
    n = int(SR * dur)
    t = _t(n)
    out = np.zeros((n, 2))
    beat = 60.0 / bpm
    for k, c in enumerate(np.arange(0.0, dur - 0.2, beat / 2)):
        idx = int(c * SR)
        ln = int(0.04 * SR)
        tick = fft_bandpass(rng.standard_normal(ln), 2500, 8000) * np.exp(-_t(ln) * 180) * (0.35 if k % 2 == 0 else 0.22)
        out[idx: idx + ln] += stereo_pan(tick, 0.35 if k % 2 else -0.35)
    for k, c in enumerate(np.arange(0.0, dur - 0.5, beat)):
        idx = int(c * SR)
        ln = int(0.4 * SR)
        tt = _t(ln)
        f = 55.0 if (k // 8) % 2 == 0 else 51.9
        b = np.sin(2 * np.pi * f * tt) * np.exp(-tt * 6) * 0.8
        out[idx: idx + ln] += stereo_pan(b[: n - idx], 0)
    pad = np.zeros(n)
    for f in [220.0, 261.6, 329.6]:
        pad += np.sin(2 * np.pi * f * t + rng.uniform(0, 6.28)) * 0.08
    pad = fft_bandpass(pad * (0.5 + 0.5 * np.sin(2 * np.pi * 0.08 * t)), 150, 1200)
    out += stereo_pan(pad, 0)
    out *= np.linspace(0.6, 1.0, n)[:, None]
    return normalize_to_dbfs(fade_in_out(out, 0.5, 1.0), -15.0)


def bgm_action_climax(dur: float, seed: int = 44, bpm: float = 136.0) -> np.ndarray:
    """Nhạc cao trào kịch tính & bứt phá (A minor -> C major)."""
    rng = np.random.default_rng(seed)
    n = int(SR * dur)
    out = np.zeros((n, 2))
    beat = 60.0 / bpm
    for k, c in enumerate(np.arange(0.0, dur - 0.15, beat / 2)):
        idx = int(c * SR)
        if k % 2 == 0:
            ln = int(0.28 * SR)
            tt = _t(ln)
            kick = np.sin(2 * np.pi * np.cumsum(52 + 95 * np.exp(-tt * 28)) / SR) * np.exp(-tt * 9) * 0.95
            out[idx: idx + ln] += stereo_pan(kick[: n - idx], 0.0)
        else:
            ln = int(0.18 * SR)
            tt = _t(ln)
            sn = (fft_bandpass(pink_noise(ln, rng), 400, 6500) * np.exp(-tt * 24) * 0.65
                  + np.sin(2 * np.pi * 185 * tt) * np.exp(-tt * 30) * 0.4)
            out[idx: idx + ln] += stereo_pan(sn[: n - idx], 0.08 if (k // 2) % 2 else -0.08)
        for sub in (0.0, beat / 4):
            hidx = int((c + sub) * SR)
            hln = int(0.04 * SR)
            if hidx + hln < n:
                hh = fft_bandpass(rng.standard_normal(hln), 5000, 12000) * np.exp(-_t(hln) * 140) * 0.25
                out[hidx: hidx + hln] += stereo_pan(hh, 0.25)
    prog = [220.0, 261.63, 293.66, 329.63]
    for k, c in enumerate(np.arange(0.0, dur - 0.4, beat * 2)):
        idx = int(c * SR)
        ln = int(min(0.65, dur - c) * SR)
        tt = _t(ln)
        f0 = prog[k % len(prog)]
        stab = (np.tanh((np.sin(2 * np.pi * f0 * tt) + 0.6 * np.sin(2 * np.pi * f0 * 1.5 * tt)
                         + 0.4 * np.sin(2 * np.pi * f0 * 2.0 * tt)) * 1.8)
                * np.exp(-tt * 4.5) * 0.45)
        out[idx: idx + ln] += add_reverb(stereo_pan(stab, -0.15 if k % 2 else 0.15), 0.25, 0.7, seed + k)
    return normalize_to_dbfs(fade_in_out(out, 0.05, 0.8), -12.0)


def bgm_warm_outro(dur: float, seed: int = 43) -> np.ndarray:
    """Nhạc ấm, sáng (C major) cho phần 'Dấu hiệu nhận biết'."""
    rng = np.random.default_rng(seed)
    n = int(SR * dur)
    t = _t(n)
    pad = np.zeros(n)
    for f in [130.81, 196.0, 261.63, 329.63, 392.0]:
        pad += (np.sin(2 * np.pi * f * t) + 0.3 * np.sin(4 * np.pi * f * t)) * 0.1
    pad = fft_bandpass(pad, 100, 2500)
    arp = np.zeros(n)
    notes = [523.25, 659.25, 783.99, 659.25, 587.33, 698.46, 880.0, 698.46]
    step = 0.3
    for k, c in enumerate(np.arange(0.2, dur - 0.5, step)):
        idx = int(c * SR)
        b = _bell(notes[k % len(notes)], 0.9, rng, bright=0.4) * 0.22
        end = min(n, idx + len(b))
        arp[idx:end] += b[: end - idx]
    st = stereo_pan(pad, -0.1) + add_reverb(stereo_pan(arp, 0.2), 0.35, 1.2, seed)
    return normalize_to_dbfs(fade_in_out(st, 0.8, 1.5), -15.0)


AMBIENCE: dict[str, Callable[..., np.ndarray]] = {
    "room_tone": amb_room_tone,
    "night_room": amb_night_room,
    "office": amb_office,
    "street": amb_street,
    "crowd": amb_crowd,
    "rain": amb_rain,
}

FOLEY: dict[str, Callable[..., np.ndarray]] = {
    "phone_ring": fx_phone_ring,
    "phone_vibrate": fx_phone_vibrate,
    "notification": fx_notification,
    "bank_ting": fx_bank_ting,
    "message_send": fx_message_send,
    "typing": fx_typing,
    "door_knock": fx_door_knock,
    "footsteps": fx_footsteps,
    "heartbeat": fx_heartbeat,
    "impact": fx_impact,
    "riser": fx_riser,
    "glitch": fx_glitch,
    "call_end": fx_call_end,
    "whistle": fx_whistle,
    "school_bell": fx_school_bell,
    "chapter_sting": fx_chapter_sting,
}

BGM: dict[str, Callable[..., np.ndarray]] = {
    "investigative_story": bgm_investigative_story,
    "tension_drone": bgm_tension_drone,
    "suspense_pulse": bgm_suspense_pulse,
    "action_climax": bgm_action_climax,
    "warm_outro": bgm_warm_outro,
}

FOLEY_DEFAULT_DUR = {
    "phone_ring": 4.0, "phone_vibrate": 2.4, "notification": 0.8, "bank_ting": 1.4, "message_send": 0.5,
    "typing": 2.0, "door_knock": 1.2, "footsteps": 2.0, "heartbeat": 4.0, "impact": 2.0, "riser": 3.0,
    "glitch": 0.9, "call_end": 1.6, "whistle": 1.6, "school_bell": 3.0, "chapter_sting": 2.2,
}


def list_presets() -> dict[str, list[str]]:
    return {"ambience": sorted(AMBIENCE), "foley": sorted(FOLEY), "bgm": sorted(BGM)}

