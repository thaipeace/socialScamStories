# PHIẾU THỰC THI – EP07: Mạo danh Ngày hội & Đêm văn hóa – Lộ tẩy ở tên tài khoản nhận

Lệnh chạy từ thư mục gốc dự án (`c:\projects\socialScamStories`).

| Gate | Việc | Lệnh | Xong |
| :-: | :--- | :--- | :-: |
| 0 | Kịch bản + Clearance ĐẠT + đủ ảnh `assets/scene1..6.jpg` + `episode.json` | `python factory619/_engine/run.py gate0 EP07` | ☑ |
| 1 | Duyệt ảnh (đồng nhất nhân vật, không logo/chữ/biểu trưng nhà nước) + xem khung chuyển động | `python factory619/_engine/run.py gate EP07 4 --preview` | ☑ |
| 2 | Sinh giọng thật + **nghe duyệt từng câu** + dàn lại timeline WAV thật | `python factory619/_engine/run.py gate EP07 2` → `python factory619/materialAndDraft/EP07/source/build_episode.py` | ☑ |
| 3 | SFX/BGM + master | `python factory619/_engine/run.py gate EP07 3` | ☑ |
| 4 | Timeline + overlay + render video | `python factory619/_engine/run.py gate EP07 4` | ☑ |
| 5 | Render staging + QA 8 điểm → xem video → ký duyệt điểm 2, 4, 5 | `python factory619/_engine/run.py gate EP07 5` → `signoff EP07` → `gate EP07 5 --skip-render` | ☑ |
| 6 | Đóng gói phát hành | `python factory619/_engine/run.py gate EP07 6` | ☑ |
