# PHIẾU THỰC THI – EP10: Hai Mạng Wi-Fi Trùng Tên & Kết Mở Tiệm Đối Diện

Lệnh chạy từ thư mục gốc dự án (`/Users/thainguyendev/projects/socialScamStories`).

| Gate | Việc | Lệnh | Xong |
| :-: | :--- | :--- | :-: |
| 0 | Kịch bản + Clearance ĐẠT + đủ ảnh `assets/scene1..8.jpg` & `scene9_black.jpg` + `episode.json` | `python3 factory619/_engine/run.py gate0 EP10` | ☑ |
| 1 | Duyệt ảnh (đồng nhất nhân vật, không logo/chữ lạ, không che mặt) + xem khung chuyển động | `python3 factory619/_engine/run.py gate EP10 2 --placeholder` rồi `... gate EP10 4 --preview` | ☑ |
| 2 | Sinh giọng thật (`gemini-3.8-flash-tts`) + **nghe duyệt từng câu** | `python3 factory619/_engine/run.py gate EP10 2` → `... signoff EP10 --listen PASS --by "Thai Nguyen"` | ☑ |
| 3 | SFX/BGM + master | `python3 factory619/_engine/run.py gate EP10 3` | ☑ |
| 4 | Timeline + overlay + render video | `python3 factory619/_engine/run.py gate EP10 4` | ☑ |
| 5 | Render staging + QA 8 điểm → xem video → ký duyệt điểm 2, 4, 5 | `... gate EP10 5` → `... signoff EP10 --point 2 4 5 --by "Thai Nguyen"` → `... gate EP10 5 --skip-render` | ☑ |
| 6 | Đóng gói phát hành | `python3 factory619/_engine/run.py gate EP10 6` | ☑ |

Ghi chú vòng sửa:
- Đã hoàn tất bản V7 (`57.6s` WAV thật), đạt **8/8 Gate 5** và xuất gói **Gate 6 Production** ngày 19/11/2026.
