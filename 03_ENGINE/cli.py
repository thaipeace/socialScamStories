# -*- coding: utf-8 -*-
"""
Shared CLI Runner (`03_ENGINE/cli.py`) dùng chung cho cả hai nhà máy `factory619` và `factory196`.

Có thể gọi qua:
  - `python factory196/_engine/run.py <cmd> ...`
  - `python factory619/_engine/run.py <cmd> ...`
  - `python 03_ENGINE/cli.py --factory 196 <cmd> ...`
"""
from __future__ import annotations

import argparse
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from core import (Episode, GateError, PreventSleep, load_json, rel, resolve_factory_dir, save_json, utf8_stdout)  # noqa: E402

utf8_stdout()


def cmd_new(a) -> None:
    fdir = resolve_factory_dir(a.factory)
    tdir = fdir / "_templates" / "EPISODE"
    dst = fdir / "materialAndDraft" / a.episode
    if dst.exists():
        raise GateError(f"{rel(dst)} đã tồn tại.")
    shutil.copytree(tdir, dst)
    for sub in ("assets", "audio/tts", "audio/sfx", "audio/bgm", "audio/mix", "source"):
        (dst / sub).mkdir(parents=True, exist_ok=True)
    cfg_p = dst / "episode.json"
    cfg = load_json(cfg_p)
    cfg["episode_id"] = a.episode
    if a.slug:
        cfg["slug"] = a.slug
    if a.title:
        cfg["title"] = a.title
    if getattr(a, "duration", None):
        cfg["duration_sec"] = float(a.duration)
    save_json(cfg_p, cfg)
    for md in dst.rglob("*.md"):
        md.write_text(md.read_text(encoding="utf-8").replace("{{EP}}", a.episode)
                      .replace("{{TITLE}}", a.title or "<Tên tập>"), encoding="utf-8")
    print(f"Đã tạo {rel(dst)} [{fdir.name}]. Tiếp theo: viết script/, clearance/, ảnh assets/, rồi chạy gate0.")


def gate0(ep: Episode) -> list[str]:
    """Kiểm tra điều kiện đầu vào theo cấu hình `channel_config.json` của từng nhà máy."""
    errs: list[str] = []
    cfg, fmt = ep.cfg, ep.channel["format"]
    if not (fmt["min_duration_sec"] <= ep.duration <= fmt["max_duration_sec"]):
        errs.append(f"duration_sec {ep.duration}s ngoài khoảng {fmt['min_duration_sec']}–{fmt['max_duration_sec']}s")
    scenes = sorted(cfg.get("scenes", []), key=lambda s: s["start"])
    if not scenes:
        errs.append("Chưa có scenes")
    else:
        if scenes[0]["start"] != 0 or abs(scenes[-1]["end"] - ep.duration) > 0.05:
            errs.append(f"Scenes phải phủ từ 0 đến hết duration ({ep.duration}s)")
        for a_, b_ in zip(scenes, scenes[1:]):
            if abs(a_["end"] - b_["start"]) > 1e-3:
                errs.append(f"Hở/chồng cảnh giữa {a_['id']} và {b_['id']}")
        for sc in scenes:
            has_img = bool(sc.get("image")) and ep.resolve_asset(sc["image"]).is_file()
            has_vid = bool(sc.get("video")) and ep.resolve_asset(sc["video"]).is_file()
            if not (has_img or has_vid):
                errs.append(f"Thiếu ảnh/video {sc.get('image') or sc.get('video')}")
    max_words_line = int(fmt.get("max_words_per_line", 32 if ep.is_landscape else 22))
    for ln in cfg.get("dialogue", []):
        if ln["speaker"] not in ep.cast:
            errs.append(f"Speaker '{ln['speaker']}' chưa có trong 02_CAST/cast.json")
        n_words = len(ln["text"].split())
        if n_words > max_words_line:
            errs.append(f"Câu {ln['id']} quá dài ({n_words} từ) – tối đa ~{max_words_line} từ/câu")
    total_words = sum(len(ln["text"].split()) for ln in cfg.get("dialogue", []))
    if "max_total_words" in fmt:
        max_total = int(fmt["max_total_words"])
    else:
        max_total = int(round((ep.duration / 60.0) * float(fmt.get("max_words_per_min", 170))))
    if total_words > max_total:
        errs.append(f"Tổng thoại {total_words} từ – quá dày cho {ep.duration}s (khuyến nghị ≤ {max_total})")
    rf = cfg.get("red_flags", {})
    if not (fmt["red_flags_min_items"] <= len(rf.get("items", [])) <= fmt["red_flags_max_items"]):
        errs.append(f"Thẻ red_flags cần {fmt['red_flags_min_items']}–{fmt['red_flags_max_items']} dấu hiệu")
    if not rf.get("action"):
        errs.append("Thẻ red_flags thiếu 'action' (việc nên làm)")
    if not cfg.get("hook"):
        errs.append("Thiếu hook")
    scripts = list((ep.material_dir / "script").glob("*.md"))
    if not scripts:
        errs.append("Thiếu kịch bản trong script/")
    clr = ep.clearance_dir / "CLEARANCE.md"
    if not clr.is_file():
        errs.append("Thiếu clearance/CLEARANCE.md")
    else:
        txt = clr.read_text(encoding="utf-8")
        ms = re.findall(r"^\**\s*TRẠNG THÁI TỔNG:\s*\**\s*([^\n*`]+)", txt, re.I | re.M)
        if not ms or ms[-1].strip().upper() != "ĐẠT":
            errs.append("Clearance chưa ở trạng thái 'TRẠNG THÁI TỔNG: ĐẠT'")
    return errs


def cmd_gate0(a) -> None:
    ep = Episode(a.episode, a.factory)
    errs = gate0(ep)
    if errs:
        print(f"GATE 0 [{ep.factory_name}] – CHƯA ĐẠT:")
        for e in errs:
            print("  -", e)
        sys.exit(1)
    print(f"GATE 0 [{ep.factory_name} · {ep.aspect_label} · {ep.duration:.0f}s] – ĐẠT. Có thể chạy Gate 2 → 5.")


def run_gate(ep: Episode, g: int, a) -> None:
    if g == 2:
        import gate2_tts
        gate2_tts.run(ep, placeholder=getattr(a, "placeholder", False), force=getattr(a, "force", False))
    elif g == 3:
        import gate3_audio
        gate3_audio.run(ep)
    elif g == 4:
        import gate4_timeline
        gate4_timeline.run(ep, preview_only=getattr(a, "preview", False))
    elif g == 5:
        import gate5_render_audit
        gate5_render_audit.run(ep, skip_render=getattr(a, "skip_render", False))
    elif g == 6:
        import gate6_package
        gate6_package.run(ep)
    else:
        raise GateError("Gate hợp lệ: 2–6 (Gate 0: lệnh gate0; Gate 1 là duyệt ảnh thủ công + preview gate 4).")


def cmd_gate(a) -> None:
    run_gate(Episode(a.episode, a.factory), int(a.number), a)


def cmd_all(a) -> None:
    ep = Episode(a.episode, a.factory)
    if not a.skip_gate0:
        errs = gate0(ep)
        if errs:
            print(f"GATE 0 [{ep.factory_name}] – CHƯA ĐẠT:\n  - " + "\n  - ".join(errs))
            sys.exit(1)
    for g in range(int(a.frm), int(a.to) + 1):
        run_gate(ep, g, a)


def cmd_signoff(a) -> None:
    ep = Episode(a.episode, a.factory)
    stamp = datetime.now().astimezone().isoformat(timespec="seconds")
    if a.listen:
        p = ep.tts_manifest_path
        m = load_json(p)
        for ln in m["lines"]:
            ln["human_listen_check"] = a.listen
            ln["listen_by"] = a.by
            ln["listen_at"] = stamp
        save_json(p, m)
        print(f"Đã ghi nghe duyệt thoại = {a.listen}")
    if a.point:
        p = ep.human_signoff_path
        data = load_json(p) if p.is_file() else {}
        for pt in a.point:
            data[str(pt)] = {"status": a.status, "by": a.by, "note": a.note or "", "at": stamp}
        save_json(p, data)
        print(f"Đã ký duyệt điểm {a.point} = {a.status} vào {rel(p)}")


def cmd_status(a) -> None:
    ep = Episode(a.episode, a.factory)
    rows = [
        (f"Gate 0 đầu vào ({ep.aspect_label}, {ep.duration:.0f}s)", not gate0(ep)),
        ("Gate 2 TTS", ep.tts_manifest_path.is_file()),
        ("Gate 3 Mix", ep.audio_manifest_path.is_file()),
        ("Gate 4 Timeline", ep.timeline_video_path.is_file()),
        ("Gate 5 QA 8/8", ep.qa_json_path.is_file() and load_json(ep.qa_json_path).get("all_8_points_passed", False)),
        ("Gate 6 Release", (ep.production_dir / "release_manifest_gate6.json").is_file()),
    ]
    print(f"[{ep.factory_name}] {ep.id} – {ep.title} ({ep.duration:.0f}s)")
    for name, ok in rows:
        print(f"  [{'x' if ok else ' '}] {name}")


def cmd_presets(_a) -> None:
    import sfx_library
    for k, v in sfx_library.list_presets().items():
        print(f"{k:9}: {', '.join(v)}")


def main(default_factory: str | Path | None = None) -> None:
    p = argparse.ArgumentParser(description="VCH Bóc Trần Lừa Đảo – Shared Production Engine Service (03_ENGINE)")
    p.add_argument("--factory", default=default_factory, help="Nhà máy: 196 (16:9 dài) hoặc 619 (9:16 short)")
    sp = p.add_subparsers(dest="cmd", required=True)

    s = sp.add_parser("new"); s.add_argument("episode"); s.add_argument("--slug"); s.add_argument("--title")
    s.add_argument("--duration", type=float); s.set_defaults(f=cmd_new)
    s = sp.add_parser("gate0"); s.add_argument("episode"); s.set_defaults(f=cmd_gate0)
    s = sp.add_parser("gate"); s.add_argument("episode"); s.add_argument("number")
    s.add_argument("--placeholder", action="store_true"); s.add_argument("--force", action="store_true")
    s.add_argument("--preview", action="store_true"); s.add_argument("--skip-render", action="store_true"); s.set_defaults(f=cmd_gate)
    s = sp.add_parser("all"); s.add_argument("episode"); s.add_argument("--from", dest="frm", default=2); s.add_argument("--to", default=5)
    s.add_argument("--placeholder", action="store_true"); s.add_argument("--force", action="store_true")
    s.add_argument("--skip-gate0", action="store_true"); s.set_defaults(f=cmd_all)
    s = sp.add_parser("signoff"); s.add_argument("episode"); s.add_argument("--point", type=int, nargs="*")
    s.add_argument("--status", default="PASS", choices=["PASS", "FAIL", "PENDING"]); s.add_argument("--by", required=True)
    s.add_argument("--note"); s.add_argument("--listen", choices=["PASS", "FAIL"]); s.set_defaults(f=cmd_signoff)
    s = sp.add_parser("status"); s.add_argument("episode"); s.set_defaults(f=cmd_status)
    s = sp.add_parser("presets"); s.set_defaults(f=cmd_presets)

    a = p.parse_args()
    try:
        if a.cmd in ("gate", "all"):
            with PreventSleep():
                a.f(a)
        else:
            a.f(a)
    except GateError as e:
        print(f"\n[DỪNG] {e}")
        sys.exit(2)


if __name__ == "__main__":
    main()

