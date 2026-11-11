# -*- coding: utf-8 -*-
"""
Shared GATE 2 Service (`03_ENGINE/gate2_tts.py`) – Sinh giọng thoại (TTS) & kiểm tra kỹ thuật giọng
dùng chung cho cả `factory619` và `factory196`.

Quy tắc bắt buộc:
  * Đọc danh sách câu thoại từ episode.json -> "dialogue".
  * Khóa cố định model + voice + style + af từ 02_CAST/cast.json cho từng nhân vật (không tự đổi model giữa chừng).
  * Thu độc lập từng câu (1 request/câu), CẤM nối gộp câu bằng " ... ... ", CẤM dùng asetrate/atempo.
  * Có chế độ --placeholder (không gọi API) để chạy thử toàn pipeline.
"""
from __future__ import annotations

import base64
import json
import math
import os
import re
import subprocess
import tempfile
import time
import urllib.error
import urllib.request
import wave
from pathlib import Path

import numpy as np

from core import FFMPEG, Episode, GateError, load_json, rel, save_json

DEFAULT_AF = "highpass=f=80,acompressor=threshold=-18dB:ratio=2.5:attack=8:release=100:makeup=2dB"
AF_ALIASES = {
    "phone": "highpass=f=320,lowpass=f=3400,equalizer=f=1800:width_type=o:width=1.0:g=4,"
             "acompressor=threshold=-20dB:ratio=4:attack=5:release=80:makeup=3dB,aecho=0.8:0.6:12:0.15",
    "memory": "highpass=f=180,lowpass=f=6000,aecho=0.8:0.7:60|120:0.35|0.2,"
              "acompressor=threshold=-18dB:ratio=2.5:attack=10:release=120:makeup=2dB",
    "default": DEFAULT_AF,
}


def resolve_af(af: str) -> str:
    chain = AF_ALIASES.get(af, af) if af else DEFAULT_AF
    if "asetrate" in chain or "atempo" in chain:
        raise GateError(f"CẤM dùng asetrate/atempo trong filter âm thanh: {chain}")
    return chain


def load_api_keys(ep: Episode) -> list[str]:
    tts_cfg = ep.channel["tts"]
    keys: list[str] = []
    env_key = os.environ.get(tts_cfg.get("env_var", "GEMINI_API_KEY"), "").strip()
    if env_key:
        keys.append(env_key)
    kf = Path(tts_cfg.get("keys_file", ""))
    if kf.is_file():
        try:
            data = load_json(kf)
            raw = (data.get("keys") or data.get("api_keys") or []) if isinstance(data, dict) else (data if isinstance(data, list) else [])
            for item in raw:
                k = item.strip() if isinstance(item, str) else str(item.get("key", "")).strip() if isinstance(item, dict) else ""
                if k and k not in keys:
                    keys.append(k)
        except Exception:
            pass
    try:
        import sys as _sys
        from core import HAIZFLOW_ROOT
        src = HAIZFLOW_ROOT / "src"
        if src.is_dir() and str(src) not in _sys.path:
            _sys.path.insert(0, str(src))
        from haizflow.services import secure_credentials  # type: ignore
        if kf.is_file():
            idx = load_json(kf)
            active_id = str(idx.get("active") or "")
            all_ids = ([active_id] if active_id else []) + ["legacy"] + [
                str(e.get("id", "")) for e in idx.get("keys", []) if isinstance(e, dict)
            ]
            for kid in all_ids:
                if not kid:
                    continue
                target = "HaizFlow/Gemini/APIKey" if kid == "legacy" else f"HaizFlow/Gemini/APIKey/{kid}"
                sec = secure_credentials.read_secret(target).strip()
                if sec and sec not in keys:
                    keys.append(sec)
    except Exception as exc:
        print(f"    [warn load_api_keys]: {exc}")
    for env_path in (
        Path("C:/projects/vfc/vfc-ai-diagnose/.env"),
        Path("C:/projects/optisign/kb-delta-indexer/.env"),
        Path("C:/projects/vfc/vfc-fs/.env.local"),
        Path("C:/projects/vfc/vnmadministrative/.env.local"),
        Path("C:/projects/779/.env"),
    ):
        if env_path.is_file():
            try:
                for m in re.findall(r'(AIzaSy[A-Za-z0-9_\-]{33})', env_path.read_text(encoding="utf-8", errors="ignore")):
                    if m and m not in keys:
                        keys.append(m)
            except Exception:
                pass
    # Chấp nhận cả key cũ "AIzaSy…" và key định dạng mới "AQ.…" của Google AI Studio.
    keys = [k for k in keys if k.startswith(("AIzaSy", "AQ."))]
    print(f" -> Đã nạp {len(keys)} API key để tổng hợp TTS.")
    return keys


def _extract_audio_b64(resp: dict) -> tuple[str, str]:
    """Find the last audio block in an Interactions response (steps[].content[])."""
    found = None
    for step in resp.get("steps", []) or []:
        for c in step.get("content", []) or []:
            if c.get("type") == "audio" and c.get("data"):
                found = (c["data"], c.get("mime_type", "audio/wav"))
    if not found and resp.get("output_audio"):
        oa = resp["output_audio"]
        found = (oa["data"], oa.get("mime_type", "audio/wav"))
    if not found:
        raise RuntimeError(f"Không có audio trong phản hồi: {json.dumps(resp)[:400]}")
    return found


def synthesize(ep: Episode, text: str, voice: str, style: str, keys: list[str], out_raw: Path,
               preferred_model: str | None = None) -> tuple[str, str]:
    tts_cfg = ep.channel["tts"]
    model_name = preferred_model or tts_cfg["model"]
    content: dict = {"type": "text", "text": text}
    if style:
        content["annotations"] = [{"type": "speech_metadata", "style": style}]
    last_err: Exception | None = None
    payload = {
        "model": model_name,
        "input": [{"type": "user_input", "content": [content]}],
        "response_format": {"type": "audio"},
        "generation_config": {"speech_config": [{"voice": voice}]},
    }
    body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    for key in keys:
        attempt = 0
        while attempt < 5:
            attempt += 1
            req = urllib.request.Request(tts_cfg["endpoint"], data=body,
                                         headers={"Content-Type": "application/json", "x-goog-api-key": key})
            try:
                with urllib.request.urlopen(req, timeout=90) as r:
                    resp = json.loads(r.read().decode("utf-8"))
                data_b64, mime = _extract_audio_b64(resp)
                raw = base64.b64decode(data_b64)
                if "l16" in mime.lower() or "pcm" in mime.lower():
                    rate = 24000
                    for part in mime.split(";"):
                        if part.strip().startswith("rate="):
                            rate = int(part.split("=")[1])
                    with wave.open(str(out_raw), "wb") as wf:
                        wf.setnchannels(1)
                        wf.setsampwidth(2)
                        wf.setframerate(rate)
                        wf.writeframes(raw)
                else:
                    out_raw.write_bytes(raw)
                return mime, model_name
            except urllib.error.HTTPError as exc:
                msg = exc.read().decode("utf-8", "replace")
                last_err = RuntimeError(f"HTTP {exc.code} ({model_name}): {msg[:300]}")
                if exc.code == 429:
                    if "per day" in msg.lower() or "requests per day" in msg.lower():
                        print(f"    (Key hiện tại chạm giới hạn ngày cho {model_name} – chuyển key tiếp theo...)")
                        break
                    m = re.search(r"retry in (\d+(?:\.\d+)?)s", msg)
                    wait = float(m.group(1)) + 2.0 if m else 25.0
                    if wait > 90.0:
                        print("    (Thời gian chờ quá dài – chuyển sang API key tiếp theo...)")
                        break
                    print(f"    (giới hạn tốc độ API – chờ {wait:.0f}s rồi thử lại)")
                    time.sleep(wait)
                    continue
                if exc.code in {400, 401, 403} and ("api_key_invalid" in msg.lower() or "key not valid" in msg.lower()):
                    print("    (Key không hợp lệ – chuyển sang API key tiếp theo...)")
                    break
                if attempt >= 2:
                    break
                time.sleep(1.5)
            except Exception as exc:  # noqa: BLE001
                last_err = exc
                if attempt >= 2:
                    break
                time.sleep(1.5)
    raise GateError(f"TTS thất bại trên mọi API key cho model {model_name}: {last_err}")


def placeholder_voice(text: str, out_raw: Path) -> str:
    """Giọng giả (chuỗi âm 'bíp' theo nhịp âm tiết) để test pipeline khi chưa gọi API."""
    sr = 24000
    syllables = max(1, len(text.split()))
    seg = 0.20
    out = []
    for i in range(syllables):
        t = np.arange(int(sr * seg)) / sr
        f = 180 + 40 * math.sin(i * 1.7)
        tone = np.sin(2 * np.pi * f * t) * np.sin(np.pi * t / seg) * 0.4
        out.append(tone)
        if text.count("...") and i == syllables // 2:
            out.append(np.zeros(int(sr * 0.35)))
    pcm = (np.concatenate(out) * 32767).astype(np.int16)
    with wave.open(str(out_raw), "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sr)
        wf.writeframes(pcm.tobytes())
    return "placeholder/wav"


def master_line(in_wav: Path, out_wav: Path, af_chain: str, peak_db: float) -> dict:
    """EQ/compress in FFmpeg -> trim outer silence (non-destructive) -> fades -> peak normalize -> pads."""
    subprocess.run([FFMPEG, "-y", "-v", "error", "-i", str(in_wav), "-af", af_chain or DEFAULT_AF,
                    "-ac", "1", "-ar", "48000", "-c:a", "pcm_s16le", str(out_wav)], check=True)
    with wave.open(str(out_wav), "rb") as wf:
        sr = wf.getframerate()
        s = np.frombuffer(wf.readframes(wf.getnframes()), dtype=np.int16).astype(np.float32)
    thr = 32768.0 * (10.0 ** (-65.0 / 20.0))
    active = np.where(np.abs(s) > thr)[0]
    if len(active):
        s = s[max(0, int(active[0]) - int(0.08 * sr)): min(len(s), int(active[-1]) + int(0.32 * sr))]
    fi, fo = min(len(s), int(0.025 * sr)), min(len(s), int(0.06 * sr))
    if fi:
        s[:fi] *= np.linspace(0, 1, fi, dtype=np.float32)
    if fo:
        s[-fo:] *= np.linspace(1, 0, fo, dtype=np.float32)
    pk = float(np.max(np.abs(s))) if len(s) else 0.0
    if pk > 0:
        s = np.clip(s * (32767.0 * 10 ** (peak_db / 20.0) / pk), -32768, 32767)
    full = np.concatenate([np.zeros(int(0.06 * sr), np.float32), s, np.zeros(int(0.12 * sr), np.float32)]).astype(np.int16)
    with wave.open(str(out_wav), "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sr)
        wf.writeframes(full.tobytes())
    return measure(out_wav)


def measure(wav_path: Path) -> dict:
    with wave.open(str(wav_path), "rb") as wf:
        sr = wf.getframerate()
        f = np.frombuffer(wf.readframes(wf.getnframes()), dtype=np.int16).astype(np.float32) / 32768.0
    pk = float(np.max(np.abs(f))) if len(f) else 0.0
    rms = float(np.sqrt(np.mean(f ** 2))) if len(f) else 0.0
    return {"sample_rate": sr, "channels": 1, "duration_sec": round(len(f) / sr, 3),
            "peak_dbfs": round(20 * math.log10(max(pk, 1e-7)), 2), "rms_dbfs": round(20 * math.log10(max(rms, 1e-7)), 2)}


def run(ep: Episode, placeholder: bool = False, force: bool = False, only: list[str] | None = None) -> dict:
    print(f"=== GATE 2: TTS VOICE [{ep.factory_name} · {ep.aspect_label}] – {ep.id} ===")
    lines = ep.cfg.get("dialogue", [])
    if not lines:
        raise GateError("episode.json chưa có 'dialogue'.")
    ep.tts_dir.mkdir(parents=True, exist_ok=True)
    keys = [] if placeholder else load_api_keys(ep)
    if not placeholder and not keys:
        raise GateError("Không tìm thấy Gemini API key (biến GEMINI_API_KEY hoặc file keys của HaizFlow). "
                        "Dùng --placeholder để chạy thử không cần API.")
    peak_db = float(ep.channel["audio"]["dialogue_peak_dbfs"])
    out_lines = []
    prev = load_json(ep.tts_manifest_path) if ep.tts_manifest_path.is_file() else {"lines": []}
    prev_by_id = {ln["line_id"]: ln for ln in prev.get("lines", [])}

    with tempfile.TemporaryDirectory(prefix="gate2_tts_") as tmpd:
        tmp = Path(tmpd)
        mode = "placeholder" if placeholder else ep.channel["tts"]["model"]
        for item in lines:
            lid = item["id"]
            spk = ep.speaker(item["speaker"])
            voice = item.get("voice", spk["voice"])
            style = item.get("style", spk.get("style", ""))
            spk_model = item.get("model", spk.get("model"))
            line_mode = "placeholder" if placeholder else (spk_model or mode)
            af = resolve_af(item.get("af", spk.get("af", DEFAULT_AF)))
            final_wav = ep.tts_dir / f"{lid}.wav"
            old = prev_by_id.get(lid, {})
            text_changed = (
                old.get("text") != item["text"]
                or old.get("voice") != voice
                or old.get("style") != style
                or old.get("af") != af
            )
            mode_changed = old.get("engine") != line_mode
            must_synth = force or item.get("force") or not final_wav.is_file() or text_changed or mode_changed
            if only and lid not in only:
                must_synth = False
            if must_synth:
                raw = tmp / f"{lid}_raw.wav"
                print(f" -> Tổng hợp {lid} [{voice} @ {line_mode}] : {item['text']}")
                if placeholder:
                    placeholder_voice(item["text"], raw)
                else:
                    _, used_model = synthesize(ep, item["text"], voice, style, keys, raw, preferred_model=spk_model)
                    line_mode = used_model
                m = master_line(raw, final_wav, af, peak_db)
                subprocess.run([FFMPEG, "-y", "-v", "error", "-i", str(final_wav), "-c:a", "libmp3lame", "-b:a", "192k",
                                str(final_wav.with_suffix(".mp3"))], check=True)
            else:
                print(f" -> Giữ nguyên {lid} (không đổi)")
                m = measure(final_wav)
            window = float(item.get("window", 99))
            fits = m["duration_sec"] <= window
            out_lines.append({
                "line_id": lid,
                "speaker": item["speaker"],
                "speaker_label": item.get("speaker_label", spk.get("label", item["speaker"])),
                "label_short": item.get("label_short", spk.get("label_short", "")),
                "voice": voice,
                "style": style,
                "af": af,
                "engine": line_mode,
                "text": item["text"],
                "subtitle": item.get("subtitle"),
                "timeline_start_sec": float(item["start"]),
                "timeline_end_sec": round(float(item["start"]) + m["duration_sec"], 3),
                "timeline_window_sec": window,
                "fits_timeline_window": fits,
                "wav_path": rel(final_wav),
                "metrics": m,
                "qa_status": "PASS" if fits and m["duration_sec"] > 0.4 else "WARN_DURATION",
                "human_listen_check": "PENDING" if must_synth else old.get("human_listen_check", "PENDING"),
            })
            print(f"    {lid}: {m['duration_sec']}s / cửa sổ {window}s, peak {m['peak_dbfs']} dBFS -> {out_lines[-1]['qa_status']}")
            done = {ln["line_id"] for ln in out_lines}
            _save(ep, placeholder, peak_db, out_lines + [ln for ln in prev.get("lines", []) if ln["line_id"] not in done],
                  partial=True)

    manifest = _save(ep, placeholder, peak_db, out_lines, partial=False)
    warn = [ln["line_id"] for ln in out_lines if ln["qa_status"] != "PASS"]
    if warn:
        print(f" !! Câu vượt cửa sổ thời gian: {warn} – rút ngắn thoại hoặc nới 'window'.")
    print(f" -> Manifest: {rel(ep.tts_manifest_path)}")
    return manifest


def _save(ep: Episode, placeholder: bool, peak_db: float, lines: list, partial: bool) -> dict:
    manifest = {
        "episode_id": ep.id,
        "factory": ep.factory_name,
        "gate": "GATE_2_TTS_VOICE",
        "engine": "placeholder" if placeholder else ep.channel["tts"]["model"],
        "placeholder_mode": placeholder,
        "partial": partial,
        "target_peak_dbfs": peak_db,
        "lines": lines,
        "note": "Bắt buộc nghe lại từng câu (dấu thanh, cảm xúc). Đặt human_listen_check = PASS sau khi duyệt.",
    }
    save_json(ep.tts_manifest_path, manifest)
    return manifest

