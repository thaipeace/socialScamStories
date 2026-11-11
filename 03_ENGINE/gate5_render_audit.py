# -*- coding: utf-8 -*-
"""
Shared GATE 5 Service (`03_ENGINE/gate5_render_audit.py`) – Render MP4 staging & kiểm duyệt 8 điểm
dùng chung cho cả hai nhà máy `factory619` và `factory196`.
"""
from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path

from core import FFMPEG, FFPROBE, Episode, GateError, load_json, rel, save_json

HUMAN_POINTS = {
    2: "Không hướng dẫn thủ đoạn chi tiết (chỉ bóc trần cơ chế tâm lý & dấu hiệu)",
    4: "Hình ảnh an toàn: không máu me/khỏa thân, không logo – giao diện – sắc phục thật",
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

    def human(pid: int) -> tuple[str, str]:
        s = signoff.get(str(pid), {})
        st = s.get("status", "PENDING")
        return ("PASS" if st == "PASS" else "FAIL" if st == "FAIL" else "PENDING_HUMAN",
                f"Người duyệt: {s.get('by', '—')}. {s.get('note', '')}".strip())

    def soft_ack(pid: int, status: str) -> str:
        if status == "WARN" and signoff.get(str(pid), {}).get("status") == "PASS":
            return "PASS"
        return status

    p2, e2 = human(2)
    p4, e4 = human(4)
    p5, e5 = human(5)
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
    report = {
        "episode_id": ep.id,
        "factory": ep.factory_name,
        "gate": "GATE_5_RENDER_AND_QA",
        "staging_mp4_path": rel(ep.staging_mp4_path),
        "file_size_mb": round(ep.staging_mp4_path.stat().st_size / 1048576, 2),
        "stream_probe": info,
        "all_8_points_passed": all_pass,
        "checklist": checklist,
    }
    save_json(ep.qa_json_path, report)
    write_md(ep, report)
    for c in checklist:
        print(f"    [{c['status']:>13}] {c['id']}. {c['name']}")
    print(f" -> {'ĐẠT 8/8' if all_pass else 'CHƯA ĐẠT'} | {rel(ep.qa_json_path)}")
    return report


def write_md(ep: Episode, r: dict) -> None:
    badge = {"PASS": "✅ PASS", "FAIL": "❌ FAIL", "WARN": "⚠️ WARN", "PENDING_HUMAN": "⏳ CHỜ NGƯỜI DUYỆT"}
    rows = "\n".join(f"| {c['id']}. {c['name']} | {badge.get(c['status'], c['status'])} | {c['evidence']} |" for c in r["checklist"])
    md = f"""# BIÊN BẢN KIỂM DUYỆT GATE 5 [{ep.factory_name} · {ep.aspect_label}] – {ep.id}: {ep.title}

- Video staging: [{Path(r['staging_mp4_path']).name}](file:///{(ep.staging_mp4_path).as_posix()}) ({r['file_size_mb']} MB)
- Trạng thái: {"✅ **ĐẠT 8/8 – được chuyển Gate 6**" if r['all_8_points_passed'] else "❌ **CHƯA ĐẠT** – xem các mục chưa PASS"}

| Tiêu chí | Trạng thái | Bằng chứng |
| :--- | :---: | :--- |
{rows}

> Mục ⏳ cần bạn xem video rồi ký duyệt trong `clearance/human_qa_signoff.json`
> (`python {ep.factory_name}/_engine/run.py signoff {ep.id}`), sau đó chạy lại Gate 5 với `--skip-render`.
"""
    (ep.staging_dir / "GATE5_QA_REPORT.md").write_text(md, encoding="utf-8")

