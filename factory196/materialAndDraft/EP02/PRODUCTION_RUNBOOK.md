# PHIẾU THỰC THI (16:9 LONG-FORM 4–5+ PHÚT) – EP02: Chữ ma – 80 triệu và một cú click

Lệnh chạy từ thư mục gốc dự án (`c:\projects\socialScamStories`).

| Gate | Việc | Lệnh | Xong |
| :-: | :--- | :--- | :-: |
| 0 | Kịch bản 4–5+ phút (≥ 240s, phản biện pháp lý & logic) + Clearance ĐẠT + đủ ảnh 16:9 + `episode.json` | `python factory196/_engine/run.py gate0 EP02` | ☐ |
| 1 | Duyệt ảnh 16:9 (không viền letterbox, không chữ/logo/biển số, cảnh lên hình trước thoại 0.3s) + xem khung QA | `python factory196/_engine/run.py gate EP02 2 --placeholder` rồi `... gate EP02 4 --preview` | ☐ |
| 2 | Sinh giọng thật (tách rõ âm sắc các nhân vật cùng giới) + căn lại timeline theo WAV thật + **nghe duyệt `.mp3`** | `python factory196/_engine/run.py gate EP02 2` → `... signoff EP02 --listen PASS --by "<tên>"` | ☐ |
| 3 | SFX/BGM + master (≥ 240s) | `python factory196/_engine/run.py gate EP02 3` | ☐ |
| 4 | Timeline 1920x1080 + Chapter cards + Subtitle + Render video | `python factory196/_engine/run.py gate EP02 4` | ☐ |
| 5 | Render staging + QA 8 điểm → **DỪNG CHỜ CHỦ KÊNH DUYỆT STAGING** → ký duyệt điểm 2, 4, 5 | `... gate EP02 5` → `... signoff EP02 --point 2 4 5 --by "<tên>"` → `... gate EP02 5 --skip-render` | ☐ |
| 6 | Đóng gói phát hành (chỉ chạy sau khi chủ kênh duyệt Staging) | `python factory196/_engine/run.py gate EP02 6` | ☐ |

Ghi chú vòng sửa:
- `episode.json` được sinh từ `source/build_episode.py` – **không sửa tay**; sửa thoại/cảnh trong builder rồi chạy lại.
- **Real-TTS Retiming:** sau Gate 2 chạy lại `python factory196/materialAndDraft/EP02/source/build_episode.py` → builder đọc `tts_manifest_gate2.json`, dàn lại toàn bộ timeline, chapters, mốc YouTube và thumbnail theo WAV thật. Sau đó chạy lại Gate 2 (chỉ cập nhật window, không tổng hợp lại) rồi mới qua Gate 3.
- Tên miền chỉ hiện phần tên (`nganhangx` / `nganhаngx`), không đuôi → không vướng bộ lọc URL Gate 5.
- Dự kiến WARN mềm điểm 1 ở Gate 5 ("bệnh viện", "zalo", "messenger") → xem xong ký `--point 1`.


