# PHIẾU THỰC THI – EP04: Mã QR ảo dán đè tại quán nước, bãi giữ xe

Lệnh chạy từ thư mục gốc dự án (`c:\projects\socialScamStories`).

| Gate | Việc | Lệnh | Xong |
| :-: | :--- | :--- | :-: |
| 0 | Kịch bản + Clearance ĐẠT + đủ ảnh `assets/scene1..6.jpg` + `episode.json` | `python factory/_engine/run.py gate0 EP04` | ☑ |
| 1 | Duyệt ảnh (đồng nhất nhân vật, không logo/chữ lạ, không máu me) + xem khung chuyển động | `python factory/_engine/run.py gate EP04 4 --preview` | ☑ |
| 2 | Sinh giọng thật + **nghe duyệt từng câu** | `python factory/_engine/run.py gate EP04 2` → `... signoff EP04 --listen PASS --by "<tên>"` | ☑ |
| 3 | SFX/BGM + master | `python factory/_engine/run.py gate EP04 3` | ☑ |
| 4 | Timeline + overlay + render video | `python factory/_engine/run.py gate EP04 4` | ☑ |
| 5 | Render staging + QA 8 điểm → xem video → ký duyệt điểm 2, 4, 5 | `... gate EP04 5` → `... signoff EP04 --point 2 4 5 --by "<tên>"` → `... gate EP04 5 --skip-render` | ☑ |
| 6 | Đóng gói phát hành *(Chỉ chạy sau khi chủ kênh duyệt Staging)* | `python factory/_engine/run.py gate EP04 6` | ☐ |
