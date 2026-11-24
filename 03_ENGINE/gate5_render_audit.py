# -*- coding: utf-8 -*-
"""
Shared GATE 5 Service (`03_ENGINE/gate5_render_audit.py`) – Render MP4 staging & kiểm duyệt 8 điểm
dùng chung cho cả hai nhà máy `factory619` và `factory196`.
"""
from __future__ import annotations

import json
import re
import subprocess
from datetime import datetime
from pathlib import Path

from core import FFMPEG, FFPROBE, Episode, GateError, episode_fingerprint, load_json, rel, save_json
from motion_fx import audit_episode_motion

HUMAN_POINTS = {
    2: "Không hướng dẫn thủ đoạn chi tiết (chỉ bóc trần cơ chế tâm lý & dấu hiệu)",
    4: "Hình ảnh & chuyển động an toàn: không logo/giao diện/sắc phục thật, không máu me, motion mượt đúng nhịp & giữ continuity (QC 11 điểm)",
    5: "Tôn trọng nạn nhân, không kỳ thị vùng miền / dân tộc / nghề nghiệp / tuổi tác",
}

PHONE_RE = re.compile(r"(?<![\d.,])(?:\+?84|0)(?:[\s.\-]?\d){8,10}(?![\d.,]\d)")
URL_RE = re.compile(r"\b(?:https?://|www\.)\S+|\b[\w\-]+\.(?:com|vn|net|org|info|xyz|top|online|site|io|app|me|cc|club)\b", re.I)
ACCOUNT_RE = re.compile(r"(?<![\d.,])\d{9,16}(?![\d.,]?\d)")


def render_staging(ep: Episode) -> None:
    v, a = ep.timeline_video_path, ep.master_audio_path
    for p, g in ((v, 4), (a, 3)):
        if not p.is_file():
            raise GateError(f"Thiếu đầu ra Gate {g}: {rel(p)}")
    print(f" -> Mux video + audio -> {ep.staging_mp4_path.name}")
    subprocess.run([FFMPEG, "-y", "-v", "error", "-i", str(v), "-i", str(a), "-map", "0:v:0", "-map", "1:a:0",
                    "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2", "-movflags", "+faststart",
                    "-shortest", str(ep.staging_mp4_path)], check=True)


def probe(mp4: Path) -> dict:
    if FFPROBE:
        r = subprocess.run([FFPROBE, "-v", "error", "-show_entries",
                            "format=duration,size:stream=codec_name,codec_type,width,height,r_frame_rate,sample_rate,channels",
                            "-of", "json", str(mp4)], check=True, capture_output=True, text=True, encoding="utf-8")
        return json.loads(r.stdout)
    r = subprocess.run([FFMPEG, "-i", str(mp4)], capture_output=True, text=True, encoding="utf-8", errors="replace")
    m = re.search(r"Duration:\s*(\d+):(\d+):(\d+\.\d+)", r.stderr)
    dur = int(m.group(1)) * 3600 + int(m.group(2)) * 60 + float(m.group(3)) if m else 0.0
    return {"format": {"duration": str(dur)}, "raw": r.stderr[-1500:]}


def _contains(text: str, term: str) -> bool:
    return re.search(r"(?<!\w)" + re.escape(term.lower()) + r"(?!\w)", text) is not None


def collect_texts(ep: Episode, tts: dict, tl: dict) -> dict[str, str]:
    on_screen = []
    for ov in tl["overlays"]:
        for k in ("text", "title", "sender"):
            if ov.get(k):
                on_screen.append(str(ov[k]))
        on_screen.extend(ov.get("lines", []) or [])
    pub = ep.cfg.get("publish", {})
    meta = list(pub.get("titles", [])) + [pub.get("description", ""), pub.get("pinned_comment", "")] + pub.get("hashtags", [])
    srt_txt = ""
    if ep.srt_path.is_file():
        srt_txt = "\n".join(ln for ln in ep.srt_path.read_text(encoding="utf-8").splitlines()
                            if ln.strip() and "-->" not in ln and not ln.strip().isdigit())
    return {
        "spoken": "\n".join(ln["text"] for ln in tts["lines"]).lower(),
        "on_screen": "\n".join(on_screen).lower(),
        "srt": srt_txt.lower(),
        "metadata": "\n".join(meta).lower(),
    }


def _check_signoff_stale(entry: dict, fp: dict) -> str | None:
    """Return a clear reason string if a prior human signoff is stale relative to the current build/render."""
    if not entry or entry.get("status") != "PASS":
        return None
    saved_ver = entry.get("episode_version")
    cur_ver = fp.get("episode_version", "")
    if saved_ver is not None and saved_ver != cur_ver:
        return f"version cũ '{saved_ver}' ≠ '{cur_ver}'"
    saved_sha = entry.get("config_sha256")
    cur_sha = fp.get("config_sha256", "")
    if saved_sha and cur_sha and saved_sha != cur_sha:
        return f"episode.json đã thay đổi ({saved_sha[:8]} → {cur_sha[:8]})"
    cur_tl = fp.get("timeline_mtime")
    saved_tl = entry.get("timeline_mtime")
    if cur_tl is not None and saved_tl is not None and abs(float(cur_tl) - float(saved_tl)) > 2.0:
        return "video Gate 4 đã render lại sau lần ký trước"
    # Legacy signoffs (before fingerprint fields existed): compare ISO timestamp vs Gate 4 render mtime
    if saved_ver is None and cur_tl is not None and entry.get("at"):
        try:
            signed_ts = datetime.fromisoformat(str(entry["at"])).timestamp()
            if float(cur_tl) > signed_ts + 5.0:
                return f"ký từ bản dựng cũ ({str(entry['at'])[:16]}) trước lần render Gate 4 mới"
        except Exception:  # noqa: BLE001
            pass
    return None


def run(ep: Episode, skip_render: bool = False) -> dict:
    print(f"=== GATE 5: RENDER & 8-POINT QA [{ep.factory_name} · {ep.aspect_label}] – {ep.id} ===")
    tts = load_json(ep.tts_manifest_path)
    audio = load_json(ep.audio_manifest_path)
    tl = load_json(ep.timeline_manifest_path)
    if tl.get("preview_only"):
        raise GateError("Gate 4 mới chạy chế độ preview. Chạy lại gate 4 đầy đủ trước.")
    if not skip_render:
        render_staging(ep)
    info = probe(ep.staging_mp4_path)
    texts = collect_texts(ep, tts, tl)
    all_text = "\n".join(texts.values())
    pol = ep.policy
    fmt = ep.channel["format"]
    signoff = load_json(ep.human_signoff_path) if ep.human_signoff_path.is_file() else {}
    fp = episode_fingerprint(ep)
    ma = audit_episode_motion(ep)

    # --- 1. Không định danh người/tổ chức thật ---
    id_hard = [t for t in pol.get("identity_hard_block", []) + ep.cfg.get("forbidden_terms", []) if _contains(all_text, t)]
    id_soft = [t for t in pol.get("identity_soft_warn", []) if _contains(all_text, t)]
    phones = PHONE_RE.findall(all_text)
    urls = [u for u in URL_RE.findall(all_text) if u.lower() not in [w.lower() for w in pol.get("allowed_domains", [])]]
    accts = [a for a in ACCOUNT_RE.findall(all_text) if not PHONE_RE.fullmatch(a)]
    p1_fail = bool(id_hard or phones or urls or accts)
    p1 = "FAIL" if p1_fail else ("WARN" if id_soft else "PASS")

    # --- 3. ASR/OCR ---
    asr_hard = [w for w in pol.get("asr_ocr_hard_block", []) if _contains(all_text, w)]
    asr_soft = [w for w in pol.get("asr_ocr_soft_warn", []) if _contains(all_text, w)]
    p3 = "FAIL" if asr_hard else ("WARN" if asr_soft else "PASS")

    # --- 6. Audio ---
    mm = audio["master"]
    lo, hi = ep.channel["audio"]["master_peak_range_dbfs"]
    tts_ok = all(ln["qa_status"] == "PASS" for ln in tts["lines"])
    listened = all(ln.get("human_listen_check") == "PASS" for ln in tts["lines"])
    p6_auto = tts_ok and lo <= mm["peak_dbfs"] <= hi and abs(mm["duration_sec"] - ep.duration) < 0.1
    if tts.get("placeholder_mode"):
        p6 = "FAIL"
    elif not p6_auto:
        p6 = "FAIL"
    else:
        p6 = "PASS" if listened else "PENDING_HUMAN"

    # --- 7. Safe zone + disclaimer + red flags ---
    ovs = tl["overlays"]
    disc = [o for o in ovs if o["type"] == "disclaimer"]
    rfs = [o for o in ovs if o["type"] == "red_flags"]
    rf_items = ep.cfg.get("red_flags", {}).get("items", [])
    p7_ok = (tl["safe_zone_rules"]["all_overlays_compliant"]
             and len(disc) == 1 and disc[0]["end_sec"] - disc[0]["start_sec"] >= fmt["disclaimer_min_sec"] - 1e-6
             and disc[0]["end_sec"] >= ep.duration - 0.05
             and len(rfs) >= 1 and fmt["red_flags_min_items"] <= len(rf_items) <= fmt["red_flags_max_items"])
    p7 = "PASS" if p7_ok else "FAIL"

    # --- 8. Pacing & hook ---
    hooks = [o for o in ovs if o["type"] == "text_hook"]
    try:
        real_dur = float(info["format"]["duration"])
    except Exception:  # noqa: BLE001
        real_dur = -1.0
    p8_ok = (len(hooks) == 1 and hooks[0]["start_sec"] <= fmt["hook_must_start_before_sec"]
             and fmt["min_duration_sec"] <= ep.duration <= fmt["max_duration_sec"]
             and abs(real_dur - ep.duration) < 0.35)
    p8 = "PASS" if p8_ok else "FAIL"

    stale_reasons: dict[str, str] = {}

    def human(pid: int) -> tuple[str, str]:
        s = signoff.get(str(pid), {})
        st = s.get("status", "PENDING")
        stale = _check_signoff_stale(s, fp)
        if stale:
            stale_reasons[str(pid)] = stale
            return ("PENDING_HUMAN", f"Chữ ký cũ bị hủy hiệu lực ({stale}) -> cần xem bản dựng mới & ký lại.")
        return ("PASS" if st == "PASS" else "FAIL" if st == "FAIL" else "PENDING_HUMAN",
                f"Người duyệt: {s.get('by', '—')}. {s.get('note', '')}".strip())

    def soft_ack(pid: int, status: str) -> str:
        s = signoff.get(str(pid), {})
        if status == "WARN" and s.get("status") == "PASS" and not _check_signoff_stale(s, fp):
            return "PASS"
        return status

    p2, e2 = human(2)
    p4, e4 = human(4)
    p5, e5 = human(5)
    # Hard block Point 4 whenever Cumulative Inheritance Check 2/3 has errors!
    if ma["errors"]:
        p4 = "FAIL"
        e4 = "KHÔNG ĐẠT TIẾN TRÌNH CHECK 1–2–3: " + "; ".join(ma["errors"][:3])
    p1 = soft_ack(1, p1)
    p3 = soft_ack(3, p3)

    pts = [
        (1, "Không định danh người / tổ chức / số thật", p1,
         f"Cấm cứng: {id_hard or 0}; cảnh báo: {id_soft or 0}; SĐT: {phones or 0}; URL: {urls or 0}; dãy số TK: {accts or 0}"),
        (2, HUMAN_POINTS[2], p2, e2),
        (3, "Sạch từ khóa thuật toán (ASR/OCR/metadata)", p3, f"Cấm cứng: {asr_hard or 0}; cảnh báo: {asr_soft or 0}"),
        (4, HUMAN_POINTS[4], p4, e4),
        (5, HUMAN_POINTS[5], p5, e5),
        (6, "Âm thanh: thoại rõ, master đúng chuẩn, đã nghe duyệt", p6,
         f"Master peak {mm['peak_dbfs']} dBFS / {mm['duration_sec']}s; thoại vừa cửa sổ: {tts_ok}; đã nghe duyệt: {listened}"
         + ("; ĐANG DÙNG GIỌNG PLACEHOLDER" if tts.get("placeholder_mode") else "")),
        (7, f"Safe Zone ({ep.aspect_label}) + Disclaimer + Thẻ Dấu hiệu nhận biết", p7,
         f"Overlay trong Safe Zone: {tl['safe_zone_rules']['all_overlays_compliant']}; disclaimer: {len(disc)}; "
         f"thẻ dấu hiệu: {len(rf_items)} ý"),
        (8, "Nhịp & Hook", p8,
         f"Hook bắt đầu {hooks[0]['start_sec'] if hooks else '—'}s; thời lượng {ep.duration}s (file {real_dur:.2f}s)"),
    ]
    checklist = [{"id": i, "name": n, "status": s, "evidence": e} for i, n, s, e in pts]
    all_pass = all(c["status"] == "PASS" for c in checklist)

    # --- Visual Motion Upgrade (Check 1-2-3 Cumulative Inheritance) QC Summary ---
    ms = tl.get("motion_summary") or {}
    eff = ms.get("effective_level_counts") or ma["level_counts"]
    fallbacks = ms.get("fallbacks") or []
    zoom_streaks = ms.get("zoom_streaks") if "zoom_streaks" in ms else ma["zoom_streaks"]
    sfx_sync = ms.get("sfx_sync") or ma["sfx_sync"]
    c1_pass = all(st == "PASS" for st in (p1, p3, p7, p8)) and p6 != "FAIL"
    stage_checks = {
        "check1": {"status": "PASS" if c1_pass else "FAIL"},
        **(ma.get("stage_checks") or {}),
    }
    motion_qc = {
        "motion_version": ma.get("motion_version", "level2"),
        "hardware_profile": ma.get("hardware_profile", "dual16gb_cpu_l480"),
        "is_level2": ma["is_level2"],
        "is_level3": ma.get("is_level3", False),
        "effective_level_counts": eff,
        "declared_level_counts": ma["level_counts"],
        "feature_counts": ma.get("feature_counts") or {},
        "min_requirements": ma.get("min_requirements") or {},
        "l3_feature_total": ma.get("l3_feature_total", 0),
        "stage_checks": stage_checks,
        "waivers_used": ma.get("waivers_used") or {},
        "stale_signoff_reasons": stale_reasons,
        "fingerprint": fp,
        "has_highlights": (eff.get("B", 0) + eff.get("C", 0) + eff.get("D", 0) > 0) or bool(ep.cfg.get("chat_bubbles")) or bool(ep.cfg.get("notifications")),
        "zoom_repetition_streaks": zoom_streaks,
        "shake_scenes": ma["shake_scenes"],
        "fallbacks": fallbacks,
        "sfx_sync": sfx_sync,
        "errors": ma["errors"],
        "warnings": ma["warnings"],
        "point4_human_signed": p4 == "PASS",
        "render_stats": tl.get("render_stats"),
    }

    report = {
        "episode_id": ep.id,
        "factory": ep.factory_name,
        "gate": "GATE_5_RENDER_AND_QA",
        "staging_mp4_path": rel(ep.staging_mp4_path),
        "file_size_mb": round(ep.staging_mp4_path.stat().st_size / 1048576, 2),
        "stream_probe": info,
        "all_8_points_passed": all_pass,
        "checklist": checklist,
        "motion_qc": motion_qc,
    }
    save_json(ep.qa_json_path, report)
    write_md(ep, report)
    for c in checklist:
        print(f"    [{c['status']:>13}] {c['id']}. {c['name']}")
    fc = motion_qc["feature_counts"]
    c2s = (stage_checks.get("check2") or {}).get("status", "—")
    c3s = (stage_checks.get("check3") or {}).get("status", "—")
    print(f" -> Tiến trình Check 1-2-3: CHECK 1={stage_checks['check1']['status']} | CHECK 2={c2s} | CHECK 3={c3s}")
    print(
        f" -> Motion QC: A={eff.get('A', 0)} · B={eff.get('B', 0)} · C={eff.get('C', 0)} · D={eff.get('D', 0)} | "
        f"2.5D={fc.get('parallax_scenes', 0)} · Blink={fc.get('eye_blink', 0)} · Mouth={fc.get('mouth_sync', 0)} · "
        f"L3={motion_qc['l3_feature_total']}"
        + (f" | lặp zoom-in: {len(zoom_streaks)}" if zoom_streaks else " | nhịp camera sạch")
        + (f" | fallback: {len(fallbacks)}" if fallbacks else "")
    )
    if stale_reasons:
        print(f" -> [STALE SIGNOFF] Đã tự hủy hiệu lực chữ ký cũ cho điểm {sorted(stale_reasons)} -> cần xem & ký lại bản dựng mới!")
    print(f" -> {'ĐẠT 8/8' if all_pass else 'CHƯA ĐẠT'} | {rel(ep.qa_json_path)}")
    return report


def write_md(ep: Episode, r: dict) -> None:
    badge = {
        "PASS": "✅ PASS",
        "FAIL": "❌ FAIL",
        "WARN": "⚠️ WARN",
        "PENDING_HUMAN": "⏳ CHỜ NGƯỜI DUYỆT",
        "PASS_WITH_WAIVER": "⚠️ PASS (CÓ WAIVER)",
        "BLOCKED": "🚫 BỊ CHẶN",
        "LEGACY_SKIP": "➖ LEGACY",
        "NOT_APPLICABLE": "➖ N/A",
    }
    rows = "\n".join(f"| {c['id']}. {c['name']} | {badge.get(c['status'], c['status'])} | {c['evidence']} |" for c in r["checklist"])
    mq = r.get("motion_qc") or {}
    eff = mq.get("effective_level_counts") or {"A": 0, "B": 0, "C": 0, "D": 0}
    fc = mq.get("feature_counts") or {}
    req = mq.get("min_requirements") or {}
    sc_chk = mq.get("stage_checks") or {}
    c1_st = (sc_chk.get("check1") or {}).get("status", "—")
    c2_st = (sc_chk.get("check2") or {}).get("status", "—")
    c3_st = (sc_chk.get("check3") or {}).get("status", "—")
    streaks = mq.get("zoom_repetition_streaks") or []
    fallbacks = mq.get("fallbacks") or []
    ss = mq.get("sfx_sync") or {"synced": [], "unsynced": []}
    waivers = mq.get("waivers_used") or {}
    stale_r = mq.get("stale_signoff_reasons") or {}
    chk = "x" if mq.get("point4_human_signed") else " "
    zoom_note = "Không có chuỗi ≥ 3 cảnh zoom-in liên tiếp" if not streaks else f"⚠️ Phát hiện {len(streaks)} chuỗi lặp: " + "; ".join(" → ".join(s) for s in streaks)
    hl_note = f"Level B={eff.get('B', 0)}, Level C={eff.get('C', 0)}, Level D={eff.get('D', 0)}"
    fb_note = "Không có cảnh fallback lỗi" if not fallbacks else f"Đã hạ cấp an toàn {len(fallbacks)} cảnh: " + "; ".join(f"{f['scene_id']}" for f in fallbacks)
    sfx_note = f"Khớp foley: {len(ss.get('synced', []))} · Chưa có foley gần mốc: {len(ss.get('unsynced', []))}"
    motion_errs = "\n".join(f"- ❌ {e}" for e in (mq.get("errors") or []))
    motion_warns = "\n".join(f"- ⚠️ {w}" for w in (mq.get("warnings") or []))
    waiver_md = "\n".join(f"- ⚠️ **WAIVER `{k}`:** {v}" for k, v in waivers.items())
    stale_md = "\n".join(f"- 🔒 **Điểm {k} (chữ ký cũ bị hủy):** {v}" for k, v in stale_r.items())
    engine_notes = "\n".join(p for p in (motion_errs, waiver_md, stale_md, motion_warns) if p) or "- Không có cảnh báo motion tự động."
    fp = mq.get("fingerprint") or {}

    md = f"""# BIÊN BẢN KIỂM DUYỆT GATE 5 [{ep.factory_name} · {ep.aspect_label}] – {ep.id}: {ep.title}

- Video staging: [{Path(r['staging_mp4_path']).name}](file:///{(ep.staging_mp4_path).as_posix()}) ({r['file_size_mb']} MB)
- Phiên bản dựng: `{fp.get('episode_version', '')}` · `motion_upgrade: {fp.get('motion_upgrade', 'legacy')}` · `sha256: {fp.get('config_sha256', '')}`
- Trạng thái: {"✅ **ĐẠT 8/8 – được chuyển Gate 6**" if r['all_8_points_passed'] else "❌ **CHƯA ĐẠT** – xem các mục chưa PASS"}

## TIẾN TRÌNH CHECK 1 → 2 → 3 (LUẬT KẾ THỪA CỘNG DỒN: `Level 3 ⊃ Level 2 ⊃ Level 1`)

| Tầng Check | Trạng thái | Thông số thực đo |
| :--- | :---: | :--- |
| **CHECK 1 — Nền Level 1** *(Cốt truyện · TTS · Safe Zone · Pháp lý)* | {badge.get(c1_st, c1_st)} | Điểm tự động 1, 3, 7, 8 + master âm thanh Gate 3 |
| **CHECK 2 — Kế thừa Level 2** *(2.5D + Breathing + Chớp mắt + Chép miệng)* | {badge.get(c2_st, c2_st)} | `2.5D`: **{fc.get('parallax_scenes', 0)}** *(≥{req.get('parallax_scenes', 1)})* · `Breathing`: **{fc.get('breathing_layers', 0)}** *(≥{req.get('breathing_layers', 1)})* · `eye_blink`: **{fc.get('eye_blink', 0)}** *(≥{req.get('eye_blink', 2)})* · `mouth_sync`: **{fc.get('mouth_sync', 0)}** *(≥{req.get('mouth_sync', 2)}; 4-state: {fc.get('mouth_sync_4state', 0)})* |
| **CHECK 3 — Nâng cấp Level 3** *(Đạo diễn · Không khí · Living-Char 2.5)* | {badge.get(c3_st, c3_st)} | `split_screen`: **{fc.get('split_screen_scenes', 0)}** · `RackFocus`: **{fc.get('rack_focus_layers', 0)}** · `HeadTilt`: **{fc.get('head_tilt_layers', 0)}** · `Gaze/Expr`: **{fc.get('eye_gaze', 0) + fc.get('expr_swap', 0)}** · `L3_FX`: **{fc.get('l3_fx', 0)}** · `L3_Trans`: **{fc.get('l3_transitions', 0)}** |

## BẢNG KIỂM DUYỆT 8 ĐIỂM GATE 5

| Tiêu chí | Trạng thái | Bằng chứng |
| :--- | :---: | :--- |
{rows}

## KIỂM DUYỆT CHUYỂN ĐỘNG HÌNH ẢNH — VISUAL MOTION QC ({str(mq.get('motion_version', 'level2')).upper()})
*Phân bổ thực thi: **Level A = {eff.get('A', 0)} · Level B = {eff.get('B', 0)} · Level C = {eff.get('C', 0)} · Level D = {eff.get('D', 0)}** · Profile: `{mq.get('hardware_profile', 'dual16gb_cpu_l480')}` · Chuẩn đối chiếu: [VISUAL_MOTION_HARNESS.md](../../../00_HARNESS_GUIDELINES/VISUAL_MOTION_HARNESS.md)*

- [{chk}] Motion có phục vụ câu chuyện không?
- [{chk}] Có cảnh nào bị zoom/pan lặp lại quá máy móc không? *(Tự động: {zoom_note})*
- [{chk}] Có ít nhất một vài visual highlight đáng nhớ nếu nguồn hình phù hợp không? *(Tự động: {hl_note})*
- [{chk}] 2.5D có tạo chiều sâu tự nhiên, không méo hình không? *(Level B: {eff.get('B', 0)} cảnh · Breathing: {fc.get('breathing_layers', 0)} lớp)*
- [{chk}] Object motion & Living-Character (`eye_blink`={fc.get('eye_blink', 0)}, `mouth_sync`={fc.get('mouth_sync', 0)}) có đúng nội dung, đúng giọng nhân vật nói và không lộ viền màu da không? *(Level C: {eff.get('C', 0)} cảnh · không đổi text/UI/số tiền)*
- [{chk}] Có chi tiết AI bị biến dạng không? *(Level D: {eff.get('D', 0)} cảnh)*
- [{chk}] Motion có gây distraction khỏi voice-over không? *(Số cảnh shake: {mq.get('shake_scenes', 0)})*
- [{chk}] Có giữ được continuity giữa các cảnh không?
- [{chk}] Có sound effect nào không cần thiết không? *(Tự động: {sfx_note})*
- [{chk}] Render có smooth, không flicker, không jump frame, không lỗi layer hoặc mask không?
- [{chk}] Các cảnh không phù hợp motion nâng cao có được giữ xử lý đơn giản không? *(Tự động: {fb_note})*

**Ghi nhận tự động từ Engine:**
{engine_notes}

> **Nguyên tắc kế thừa & hạ cấp:** Level 3 bắt buộc kế thừa đủ Level 1 + Level 2 (không nhảy cóc bỏ chép miệng / chớp mắt / 2.5D). Nếu bất kỳ hiệu ứng nào không đạt chất lượng, hãy sửa tài nguyên hoặc hạ cấp có lý do rõ ràng — tuyệt đối không lờ đi.
>
> Mục ⏳ cần bạn xem video rồi ký duyệt trong `clearance/human_qa_signoff.json`
> (`python {ep.factory_name}/_engine/run.py signoff {ep.id} --point 2 4 5 --by "<tên>"`), sau đó chạy lại Gate 5 với `--skip-render`.
"""
    (ep.staging_dir / "GATE5_QA_REPORT.md").write_text(md, encoding="utf-8")

