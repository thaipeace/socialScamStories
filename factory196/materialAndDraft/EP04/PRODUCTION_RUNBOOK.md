# PHIẾU THỰC THI (16:9 LONG-FORM 4–5+ PHÚT) – EP04: Bẫy vé nội bộ – 300 triệu gom hộ và người đứng mũi chịu sào

Lệnh chạy từ thư mục gốc dự án (`c:\projects\socialScamStories`).

| Gate | Việc | Lệnh | Xong |
| :-: | :--- | :--- | :-: |
| 0 | Kịch bản 4–5+ phút (≥ 240s, phản biện pháp lý & logic) + Clearance ĐẠT + đủ ảnh 16:9 + `episode.json` | `python factory196/_engine/run.py gate0 EP04` | ☐ |
| 1 | Duyệt ảnh 16:9 (không viền letterbox, không chữ/logo/biển số, cảnh lên hình trước thoại 0.3s) + xem khung QA | `python factory196/_engine/run.py gate EP04 2 --placeholder` rồi `... gate EP04 4 --preview` | ☐ |
| 2 | Sinh giọng thật (tách rõ âm sắc các nhân vật cùng giới) + căn lại timeline theo WAV thật + **nghe duyệt `.mp3`** | `python factory196/_engine/run.py gate EP04 2` → `... signoff EP04 --listen PASS --by "<tên>"` | ☐ |
| 3 | SFX/BGM + master (≥ 240s) | `python factory196/_engine/run.py gate EP04 3` | ☐ |
| 4 | Timeline 1920x1080 + Chapter cards + Subtitle + Render video | `python factory196/_engine/run.py gate EP04 4` | ☐ |
| 5 | Render staging + QA 8 điểm → **DỪNG CHỜ CHỦ KÊNH DUYỆT STAGING** → ký duyệt điểm 2, 4, 5 | `... gate EP04 5` → `... signoff EP04 --point 2 4 5 --by "<tên>"` → `... gate EP04 5 --skip-render` | ☐ |
| 6 | Đóng gói phát hành (chỉ chạy sau khi chủ kênh duyệt Staging) | `python factory196/_engine/run.py gate EP04 6` | ☐ |

Ghi chú vòng sửa:
- 

