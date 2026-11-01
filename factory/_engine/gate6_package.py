# -*- coding: utf-8 -*-
"""
GATE 6 – Đóng gói phát hành: master MP4, SRT, thumbnail, manifest SHA-256,
PUBLISH_PACKAGE.md (tiêu đề, description, bình luận ghim, checklist khai báo AI).
Kế thừa package_release_gate6.py của 779, nội dung xuất bản lấy từ episode.json -> "publish".
"""
from __future__ import annotations

import hashlib
import shutil
import subprocess
from datetime import datetime

from core import FFMPEG, RENDERED_DIR, Episode, GateError, file_link, load_json, rel, save_json


def sha256(path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def run(ep: Episode) -> dict:
    print(f"=== GATE 6: PACKAGING & RELEASE – {ep.id} ===")
    if not ep.qa_json_path.is_file():
        raise GateError("Chưa có báo cáo Gate 5.")
    qa = load_json(ep.qa_json_path)
    if not qa.get("all_8_points_passed"):
        pend = [f"{c['id']}:{c['status']}" for c in qa["checklist"] if c["status"] != "PASS"]
        raise GateError(f"Gate 5 chưa đạt 8/8 ({', '.join(pend)}). Không đóng gói.")
    prod = ep.production_dir
    prod.mkdir(parents=True, exist_ok=True)
    RENDERED_DIR.mkdir(parents=True, exist_ok=True)

    mp4 = prod / f"{ep.file_stem}.mp4"
    shutil.copy2(ep.staging_mp4_path, mp4)
    shutil.copy2(ep.staging_mp4_path, RENDERED_DIR / mp4.name)
    srt = prod / f"{ep.file_stem}.srt"
    if ep.srt_path.is_file():
        shutil.copy2(ep.srt_path, srt)
    thumb_t = float(ep.cfg.get("publish", {}).get("thumbnail_sec", 1.5))
    thumb = prod / f"{ep.id}_Thumbnail_9x16.jpg"
    subprocess.run([FFMPEG, "-y", "-v", "error", "-ss", f"{thumb_t:.3f}", "-i", str(mp4), "-frames:v", "1", "-q:v", "2",
                    str(thumb)], check=True)

    pub = ep.cfg.get("publish", {})
    chcfg = ep.channel["publish"]
    hashtags = " ".join(dict.fromkeys(pub.get("hashtags", []) + chcfg["default_hashtags"]))
    description = "\n\n".join(x for x in [
        pub.get("description", "").strip(),
        chcfg["dramatized_label"] + "\nNhân vật, tên gọi, số điện thoại, số tiền trong phim đều là hư cấu nhằm mục đích cảnh báo.",
        chcfg["ai_label"],
        hashtags,
    ] if x)
    checksum = sha256(mp4)
    manifest = {
        "episode_id": ep.id,
        "title": ep.title,
        "gate": "GATE_6_PRODUCTION_RELEASE",
        "status": "PRODUCED_READY_FOR_PUBLISH",
        "released_at": datetime.now().astimezone().isoformat(),
        "master_video": {"path": rel(mp4), "mirror": rel(RENDERED_DIR / mp4.name), "srt": rel(srt), "thumbnail": rel(thumb),
                         "size_mb": round(mp4.stat().st_size / 1048576, 2), "sha256": checksum},
        "gate5_reference": rel(ep.qa_json_path),
        "compliance_flags": {"no_real_identity": True, "no_how_to_detail": True, "red_flags_card": True,
                             "dramatized_disclaimer": True, "ai_disclosure_required": True},
    }
    save_json(prod / "release_manifest_gate6.json", manifest)

    titles = "\n".join(f"{i + 1}. `{t}`" for i, t in enumerate(pub.get("titles", [ep.title])))
    md = f"""# GÓI XUẤT BẢN – {ep.id}: {ep.title}

- Master MP4: [{mp4.name}]({file_link(mp4)}) ({manifest['master_video']['size_mb']} MB, SHA-256 `{checksum[:16]}…`)
- Phụ đề: [{srt.name}]({file_link(srt)}) · Thumbnail: [{thumb.name}]({file_link(thumb)})
- Gate 5: ✅ 8/8 PASS

## I. Tiêu đề đề xuất
{titles}

## II. Description (copy nguyên văn)
```text
{description}
```

## III. Bình luận ghim
```text
{pub.get('pinned_comment', '').strip()}
```

## IV. Checklist trước khi bấm Public
| Hạng mục | Thao tác | Trạng thái |
| :--- | :--- | :---: |
| Khai báo nội dung AI – YouTube | Studio → *Altered or synthetic content* → **Yes** | ☐ |
| Khai báo AI – TikTok / Reels | Bật **AI-generated content** | ☐ |
| Description có đủ nhãn hư cấu + AI | Copy mục II | ☐ |
| Đăng chế độ *Unlisted* xem lại 1 lần trên điện thoại | Kiểm tra phụ đề không bị UI che | ☐ |
| Không gắn thẻ/nhắc tên người, doanh nghiệp, app thật trong bình luận | Xem 00_HARNESS_GUIDELINES/CONTENT_LEGAL_SAFETY_HARNESS.md | ☐ |
"""
    (prod / f"PUBLISH_PACKAGE_{ep.id}.md").write_text(md, encoding="utf-8")
    print(f" -> Master: {rel(mp4)}")
    print(f" -> Gói xuất bản: {rel(prod / f'PUBLISH_PACKAGE_{ep.id}.md')}")
    return manifest
