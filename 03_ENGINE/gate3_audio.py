# -*- coding: utf-8 -*-
"""
Shared GATE 3 Service (`03_ENGINE/gate3_audio.py`) – Ambience / Foley / BGM + trộn master có auto-ducking
dùng chung cho cả `factory619` và `factory196`.

Tối ưu cho cả Short (56s) lẫn Phim dài (≥ 300s):
  * Các đoạn ambience / BGM procedural dài hơn 60 giây được tổng hợp ở 60 giây rồi nối lặp mượt (crossfade 1.5s).
"""
from __future__ import annotations

import numpy as np

import sfx_library as lib
from core import PROJECT_ROOT, Episode, GateError, load_json, rel, save_json
from dsp import SR, duck_envelope, fade_in_out, fit_length, normalize_to_dbfs, place_clip, read_any_audio, \
    read_wav_stereo, save_wav, soft_limit

XFADE = 0.45
MAX_SYNTH_CHUNK_SEC = 60.0


def _render_cue(ep: Episode, cue: dict, layer: str, idx: int, dur: float) -> np.ndarray:
    if cue.get("file"):
        path = ep.resolve_asset(cue["file"])
        if not path.is_file():
            raise GateError(f"Không thấy file âm thanh: {cue['file']}")
        clip = read_any_audio(path)
        if layer != "foley":
            clip = fit_length(clip, int(dur * SR), loop_xfade_sec=1.5)
        elif cue.get("dur"):
            clip = clip[: int(float(cue["dur"]) * SR)]
        return clip
    preset = cue.get("preset")
    table = {"ambience": lib.AMBIENCE, "foley": lib.FOLEY, "bgm": lib.BGM}[layer]
    if preset not in table:
        raise GateError(f"Preset {layer} '{preset}' không tồn tại. Có: {sorted(table)}")
    seed = int(cue.get("seed", 100 + idx))
    params = cue.get("params", {})
    if layer in ("ambience", "bgm") and dur > MAX_SYNTH_CHUNK_SEC:
        base_clip = table[preset](MAX_SYNTH_CHUNK_SEC, seed=seed, **params)
        return fit_length(base_clip, int(round(dur * SR)), loop_xfade_sec=1.5)
    return table[preset](dur, seed=seed, **params)


def run(ep: Episode) -> dict:
    print(f"=== GATE 3: SFX, BGM & MIX [{ep.factory_name} · {ep.aspect_label}] – {ep.id} ===")
    if not ep.tts_manifest_path.is_file():
        raise GateError("Chưa có manifest Gate 2. Chạy gate 2 trước.")
    tts = load_json(ep.tts_manifest_path)
    audio = ep.cfg.get("audio", {})
    total = ep.duration
    N = int(round(total * SR))
    for d in (ep.sfx_dir, ep.bgm_dir, ep.mix_dir):
        d.mkdir(parents=True, exist_ok=True)

    stems = {k: np.zeros((N, 2)) for k in ("dialogue", "ambience", "foley", "bgm")}
    manifest: dict = {
        "episode_id": ep.id,
        "factory": ep.factory_name,
        "gate": "GATE_3_SFX_BGM_MIX",
        "sample_rate": SR,
        "total_duration_sec": total,
        "layers": {"ambience": [], "foley": [], "bgm": []},
    }

    for ln in tts["lines"]:
        place_clip(stems["dialogue"], read_wav_stereo(PROJECT_ROOT / ln["wav_path"]), ln["timeline_start_sec"])

    for layer, out_dir in (("ambience", ep.sfx_dir), ("bgm", ep.bgm_dir)):
        for i, cue in enumerate(audio.get(layer, [])):
            s, e = float(cue["start"]), min(float(cue["end"]), total)
            s0 = max(0.0, s - (XFADE / 2 if s > 0 else 0))
            e0 = min(total, e + (XFADE / 2 if e < total else 0))
            clip = _render_cue(ep, cue, layer, i, e0 - s0)
            clip = fade_in_out(fit_length(clip, int((e0 - s0) * SR)), XFADE if s > 0 else 0.35, XFADE if e < total else 0.7)
            name = f"{layer}_{i + 1:02d}_{cue.get('preset') or 'file'}"
            info = save_wav(clip, out_dir / f"{name}.wav", mp3=True)
            place_clip(stems[layer], clip, s0, float(cue.get("gain_db", 0.0)))
            manifest["layers"][layer].append({"name": name, "window_sec": [s, e], **cue, **info})

    for i, cue in enumerate(audio.get("foley", [])):
        preset = cue.get("preset", "file")
        dur = float(cue.get("dur", lib.FOLEY_DEFAULT_DUR.get(preset, 1.5)))
        clip = _render_cue(ep, cue, "foley", i, dur)
        name = f"foley_{i + 1:02d}_{preset}"
        info = save_wav(clip, ep.sfx_dir / f"{name}.wav", mp3=True)
        place_clip(stems["foley"], clip, float(cue["at"]), float(cue.get("gain_db", 0.0)))
        manifest["layers"]["foley"].append({"name": name, **cue, **info})

    duck_bgm_db = float(audio.get("duck_bgm_db", ep.channel["audio"]["duck_bgm_db"]))
    duck_amb_db = float(audio.get("duck_ambience_db", ep.channel["audio"]["duck_ambience_db"]))
    win_bgm = [(ln["timeline_start_sec"] - 0.1, ln["timeline_end_sec"], duck_bgm_db) for ln in tts["lines"]]
    win_amb = [(ln["timeline_start_sec"] - 0.1, ln["timeline_end_sec"], duck_amb_db) for ln in tts["lines"]]
    for d in audio.get("duck_extra", []):
        win_bgm.append((float(d["start"]), float(d["end"]), float(d.get("bgm_db", duck_bgm_db))))
        win_amb.append((float(d["start"]), float(d["end"]), float(d.get("amb_db", duck_amb_db))))
    stems["bgm"] *= duck_envelope(N, win_bgm)[:, None]
    stems["ambience"] *= duck_envelope(N, win_amb)[:, None]
    manifest["ducking"] = {"bgm_windows": win_bgm, "ambience_windows": win_amb}

    manifest["stems"] = {k: save_wav(v, ep.mix_dir / f"stem_{k}.wav") for k, v in stems.items()}
    master = soft_limit(sum(stems.values()))
    pk = float(np.max(np.abs(master)))
    if pk > 0.95 or pk < 0.3:
        master = normalize_to_dbfs(master, -1.5)
    master = fade_in_out(master, 0.03, 0.4)
    manifest["master"] = save_wav(master, ep.master_audio_path, mp3=True)
    save_json(ep.audio_manifest_path, manifest)
    m = manifest["master"]
    print(f" -> Master {m['duration_sec']}s | peak {m['peak_dbfs']} dBFS | rms {m['rms_dbfs']} dBFS")
    print(f" -> Manifest: {rel(ep.audio_manifest_path)}")
    return manifest

