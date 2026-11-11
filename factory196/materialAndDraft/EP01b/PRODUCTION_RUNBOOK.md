# PHIẾU THỰC THI (16:9 LONG-FORM ≥ 5 PHÚT) – EP01b: Cái giá của một mã OTP – Bẫy đáo hạn thẻ tín dụng qua máy POS

Lệnh chạy từ thư mục gốc dự án (`c:\projects\socialScamStories`).

| Gate | Việc | Lệnh | Xong |
| :-: | :--- | :--- | :-: |
| 0 | Kịch bản ≥ 5 phút (300s+) + Clearance ĐẠT + đủ ảnh 16:9 `assets/scene01..10.jpg` + `episode.json` | `python factory196/_engine/run.py gate0 EP01b` | ☐ |
| 1 | Duyệt ảnh 16:9 (đồng nhất nhân vật, không chữ/logo/biển số, bố cục ngang chuẩn) + xem khung QA | `python factory196/_engine/run.py gate EP01b 2 --placeholder` rồi `... gate EP01b 4 --preview` | ☐ |
| 2 | Sinh giọng thật + **nghe duyệt từng câu `.mp3`** | `python factory196/_engine/run.py gate EP01b 2` → `... signoff EP01b --listen PASS --by "<tên>"` | ☐ |
| 3 | SFX/BGM + master (≥ 300s) | `python factory196/_engine/run.py gate EP01b 3` | ☐ |
| 4 | Timeline 1920x1080 + Chapter cards + Subtitle + Render video | `python factory196/_engine/run.py gate EP01b 4` | ☐ |
| 5 | Render staging + QA 8 điểm → **DỪNG CHỜ CHỦ KÊNH DUYỆT STAGING** → ký duyệt điểm 2, 4, 5 | `... gate EP01b 5` → `... signoff EP01b --point 2 4 5 --by "<tên>"` → `... gate EP01b 5 --skip-render` | ☐ |
| 6 | Đóng gói phát hành (chỉ chạy sau khi chủ kênh duyệt Staging) | `python factory196/_engine/run.py gate EP01b 6` | ☐ |

Ghi chú vòng sửa:
- 

