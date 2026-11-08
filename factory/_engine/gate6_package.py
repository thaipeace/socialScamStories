# -*- coding: utf-8 -*-
"""
GATE 6 – Đóng gói phát hành: master MP4, SRT, thumbnail 9:16 + 16:9, manifest SHA-256,
PUBLISH_PACKAGE_<EP>.md và thư mục youtube_upload/ gồm các file .txt sẵn sàng copy-paste
để upload thủ công lên YouTube Studio.
"""
from __future__ import annotations

import hashlib
import shutil
import subprocess
from datetime import datetime

from core import FFMPEG, RENDERED_DIR, Episode, GateError, file_link, load_json, rel, save_json

DEFAULT_YT_TAGS = [
    "bóc trần lừa đảo",
    "cảnh giác lừa đảo",
    "kỹ năng thoát hiểm",
    "an toàn đời thực",
    "phim hoạt hình cảnh báo",
    "vạn chuyện",
    "shorts",
]


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
    yt_dir = prod / "youtube_upload"
    yt_dir.mkdir(parents=True, exist_ok=True)

    mp4 = prod / f"{ep.file_stem}.mp4"
    shutil.copy2(ep.staging_mp4_path, mp4)
    shutil.copy2(ep.staging_mp4_path, RENDERED_DIR / mp4.name)
    srt = prod / f"{ep.file_stem}.srt"
    if ep.srt_path.is_file():
        shutil.copy2(ep.srt_path, srt)
    thumb_t = float(ep.cfg.get("publish", {}).get("thumbnail_sec", 1.5))
    thumb_9x16 = prod / f"{ep.id}_Thumbnail_9x16.jpg"
    subprocess.run([FFMPEG, "-y", "-v", "error", "-ss", f"{thumb_t:.3f}", "-i", str(mp4), "-frames:v", "1", "-q:v", "2",
                    str(thumb_9x16)], check=True)
    thumb_16x9 = prod / f"{ep.id}_Thumbnail_16x9.jpg"
    subprocess.run([
        FFMPEG, "-y", "-v", "error", "-i", str(thumb_9x16),
        "-vf",
        "split=2[bg][fg];[bg]scale=1280:720:force_original_aspect_ratio=increase,crop=1280:720,boxblur=28:4[b];"
        "[fg]scale=-1:720[f];[b][f]overlay=(W-w)/2:0",
        "-q:v", "2", str(thumb_16x9),
    ], check=True)

    pub = ep.cfg.get("publish", {})
    chcfg = ep.channel["publish"]
    titles_list = pub.get("titles") or [ep.title]
    primary_title = titles_list[0]
    alt_titles = titles_list[1:]
    hashtags_list = list(dict.fromkeys(pub.get("hashtags", []) + chcfg["default_hashtags"]))[:3]
    hashtags = " ".join(hashtags_list)
    description = "\n\n".join(x for x in [
        pub.get("description", "").strip(),
        chcfg["dramatized_label"] + "\nNhân vật, tên gọi, số điện thoại, số tiền trong phim đều là hư cấu nhằm mục đích cảnh báo.",
        chcfg["ai_label"],
        hashtags,
    ] if x)
    pinned_comment = pub.get("pinned_comment", "").strip()
    tags_list = list(dict.fromkeys((pub.get("tags") or []) + DEFAULT_YT_TAGS))
    tags_csv = ", ".join(tags_list)
    category = pub.get("category", "Education (Giáo dục)")
    playlist = pub.get("playlist", "Bóc Trần Lừa Đảo – Kỹ Năng Cảnh Giác & An Toàn Đời Thực")

    # Xuất các file plain-text sẵn sàng Ctrl+A -> Ctrl+C trong youtube_upload/
    f_title = yt_dir / "1_TITLE.txt"
    f_desc = yt_dir / "2_DESCRIPTION.txt"
    f_tags = yt_dir / "3_TAGS.txt"
    f_pin = yt_dir / "4_PINNED_COMMENT.txt"
    f_guide = yt_dir / "5_YOUTUBE_STUDIO_SETTINGS.md"

    title_txt = primary_title
    if alt_titles:
        title_txt += "\n\n--- TIÊU ĐỀ DỰ PHÒNG (A/B TEST) ---\n" + "\n".join(alt_titles)
    f_title.write_text(title_txt + "\n", encoding="utf-8")
    f_desc.write_text(description + "\n", encoding="utf-8")
    f_tags.write_text(tags_csv + "\n", encoding="utf-8")
    f_pin.write_text(pinned_comment + "\n", encoding="utf-8")

    studio_settings_md = f"""# HƯỚNG DẪN CÀI ĐẶT YOUTUBE STUDIO KHI UPLOAD BẰNG TAY ({ep.id})

## 1. File tải lên (Upload files)
- **File Video chính (9:16 MP4)**: [{mp4.name}]({file_link(mp4)})
- **File Phụ đề (SRT)**: [{srt.name}]({file_link(srt)})
- **Ảnh Thumbnail 9:16 (chọn trên điện thoại)**: [{thumb_9x16.name}]({file_link(thumb_9x16)}) (mốc `{thumb_t:.1f}s`)
- **Ảnh Thumbnail 16:9 (nếu YouTube Studio Web yêu cầu)**: [{thumb_16x9.name}]({file_link(thumb_16x9)})

## 2. Các ô nội dung Copy – Paste nhanh
- **Title (Tiêu đề — {len(primary_title)}/100 ký tự)**: Mở [{f_title.name}]({file_link(f_title)}) (dòng đầu tiên)
- **Description (Mô tả)**: Mở [{f_desc.name}]({file_link(f_desc)}) (`Ctrl+A` → `Ctrl+C`)
- **Tags (Thẻ từ khóa — {len(tags_csv)}/500 ký tự)**: Mở [{f_tags.name}]({file_link(f_tags)}) (`Ctrl+A` → `Ctrl+C`)
- **Pinned Comment (Bình luận ghim sau khi đăng)**: Mở [{f_pin.name}]({file_link(f_pin)}) (`Ctrl+A` → `Ctrl+C`)

## 3. Cấu hình chi tiết từng mục trong YouTube Studio
| Mục trong YouTube Studio | Giá trị cần chọn | Lý do / Lưu ý quan trọng |
| :--- | :--- | :--- |
| **Playlist (Danh sách phát)** | `{playlist}` | Gom nhóm chủ đề giúp tăng xem nối tiếp |
| **Audience (Đối tượng người xem)** | **No, it's not made for kids** *(Không, nội dung này không dành cho trẻ em)* | **BẮT BUỘC chọn "Không"** để YouTube không khóa phần Bình luận ghim và phân phối đúng tới phụ huynh/người lớn |
| **Age restriction (Giới hạn độ tuổi)** | **No, don't restrict my videos to viewers over 18 only** | Nội dung giáo dục cảnh giác an toàn cho mọi lứa tuổi |
| **Altered content (Nội dung đã chỉnh sửa / tổng hợp AI)** | **Yes** *(Có)* | Tuân thủ chính sách minh bạch AI của YouTube |
| **Automatic chapters & concepts** | **Bật (Allow)** | Đã có sẵn mốc thời gian `00:00` trong Description |
| **Shorts remixing** | **Allow video and audio remixing** | Cho phép khán giả remix tăng lan tỏa |
| **Category (Danh mục)** | `{category}` | Phù hợp nội dung kỹ năng sống & cảnh báo lừa đảo |
| **Video language (Ngôn ngữ)** | **Vietnamese (Tiếng Việt)** | Tối ưu phân phối người xem Việt Nam + nạp file `{srt.name}` |
| **Comments (Bình luận)** | **On** *(Hold potentially inappropriate comments for review)* | Ngay sau khi đăng, dán nội dung từ `4_PINNED_COMMENT.txt` và bấm **Pin (Ghim)** |
| **Visibility (Chế độ hiển thị)** | **Unlisted (Không công khai)** → kiểm tra trên điện thoại → **Public (Công khai)** | Kiểm tra âm thanh & phụ đề trên màn hình dọc trước khi mở Public |
"""
    f_guide.write_text(studio_settings_md, encoding="utf-8")

    checksum = sha256(mp4)
    manifest = {
        "episode_id": ep.id,
        "title": ep.title,
        "gate": "GATE_6_PRODUCTION_RELEASE",
        "status": "PRODUCED_READY_FOR_PUBLISH",
        "released_at": datetime.now().astimezone().isoformat(),
        "master_video": {
            "path": rel(mp4),
            "mirror": rel(RENDERED_DIR / mp4.name),
            "srt": rel(srt),
            "thumbnail_9x16": rel(thumb_9x16),
            "thumbnail_16x9": rel(thumb_16x9),
            "thumbnail_sec": thumb_t,
            "size_mb": round(mp4.stat().st_size / 1048576, 2),
            "sha256": checksum,
        },
        "youtube_upload": {
            "primary_title": primary_title,
            "primary_title_length": len(primary_title),
            "alternative_titles": alt_titles,
            "description": description,
            "tags_csv": tags_csv,
            "tags_list": tags_list,
            "hashtags": hashtags_list,
            "pinned_comment": pinned_comment,
            "studio_settings": {
                "playlist": playlist,
                "made_for_kids": False,
                "age_restricted": False,
                "altered_or_synthetic_content": True,
                "category": category,
                "video_language": "vi",
                "subtitles_file": rel(srt),
                "comments": "ON_MODERATION_BASIC",
            },
            "copy_paste_files": {
                "title_txt": rel(f_title),
                "description_txt": rel(f_desc),
                "tags_txt": rel(f_tags),
                "pinned_comment_txt": rel(f_pin),
                "studio_settings_md": rel(f_guide),
            },
        },
        "gate5_reference": rel(ep.qa_json_path),
        "compliance_flags": {
            "no_real_identity": True,
            "no_how_to_detail": True,
            "red_flags_card": True,
            "dramatized_disclaimer": True,
            "ai_disclosure_required": True,
        },
    }
    save_json(prod / "release_manifest_gate6.json", manifest)

    titles = "\n".join(f"{i + 1}. `{t}` ({len(t)}/100 ký tự)" for i, t in enumerate(titles_list))
    md = f"""# GÓI XUẤT BẢN YOUTUBE – {ep.id}: {ep.title}

## 📦 1. Các File Cần Dùng Khi Upload
- **Video Master (MP4 9:16)**: [{mp4.name}]({file_link(mp4)}) ({manifest['master_video']['size_mb']} MB, SHA-256 `{checksum[:16]}…`)
- **Phụ đề chuẩn thời gian (SRT)**: [{srt.name}]({file_link(srt)})
- **Thumbnail dọc (9:16 — mốc `{thumb_t:.1f}s`)**: [{thumb_9x16.name}]({file_link(thumb_9x16)})
- **Thumbnail ngang (16:9 — dùng trên YouTube Studio Web)**: [{thumb_16x9.name}]({file_link(thumb_16x9)})
- **Bộ file `.txt` sẵn sàng Copy–Paste nhanh**:
  - Tiêu đề: [{f_title.name}]({file_link(f_title)})
  - Mô tả (Description): [{f_desc.name}]({file_link(f_desc)})
  - Thẻ từ khóa (Tags): [{f_tags.name}]({file_link(f_tags)})
  - Bình luận ghim (Pinned Comment): [{f_pin.name}]({file_link(f_pin)})
  - Hướng dẫn cài đặt YouTube Studio: [{f_guide.name}]({file_link(f_guide)})

---

## 🏷️ 2. Tiêu đề đề xuất (Title — tối đa 100 ký tự)
{titles}

**Copy nhanh tiêu đề chính:**
```text
{primary_title}
```

---

## 📝 3. Mô tả video (Description — copy nguyên văn)
```text
{description}
```

---

## 🔎 4. Thẻ từ khóa (YouTube Studio → Show more → Tags)
```text
{tags_csv}
```

---

## 📌 5. Bình luận ghim (Pinned Comment — dán và ghim ngay sau khi đăng)
```text
{pinned_comment}
```

---

## ⚙️ 6. Bảng Cài Đặt Nhanh Trong YouTube Studio
| Hạng mục | Thao tác chọn trên YouTube Studio | Trạng thái |
| :--- | :--- | :---: |
| **Danh sách phát (Playlist)** | `{playlist}` | ☐ |
| **Đối tượng (Audience – Made for kids)** | Chọn **No, it's not made for kids** *(Không dành cho trẻ em – để mở bình luận ghim & tiếp cận phụ huynh)* | ☐ |
| **Khai báo nội dung AI (Altered content)** | Chọn **Yes** *(Có sử dụng hình ảnh/âm thanh tổng hợp)* | ☐ |
| **Ngôn ngữ & Phụ đề (Language & Subtitles)** | Ngôn ngữ: **Tiếng Việt** · Tải lên file `{srt.name}` | ☐ |
| **Danh mục (Category)** | `{category}` | ☐ |
| **Kiểm tra trước khi Public** | Đăng **Unlisted** → xem thử trên điện thoại → ghim bình luận → bật **Public** | ☐ |
"""
    (prod / f"PUBLISH_PACKAGE_{ep.id}.md").write_text(md, encoding="utf-8")
    print(f" -> Master: {rel(mp4)}")
    print(f" -> Gói xuất bản: {rel(prod / f'PUBLISH_PACKAGE_{ep.id}.md')}")
    print(f" -> Thư mục YouTube Upload Kit: {rel(yt_dir)}")
    return manifest
