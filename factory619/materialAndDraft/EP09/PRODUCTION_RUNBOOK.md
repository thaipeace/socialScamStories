# PHIẾU THỰC THI – EP09: Bẫy Cuộc Gọi Nhỡ Lúc Đang Chờ Việc

Lệnh chạy từ thư mục gốc dự án (`c:\projects\socialScamStorys`).

| Gate | Việc | Lệnh | Xong |
| :-: | :--- | :--- | :-: |
| 0 | Kịch bản + Clearance ĐẠT + đủ ảnh `assets/scene1..6.jpg` + `episode.json` | `python factory/_engine/run.py gate0 EP09` | ☐ |
| 1 | Duyệt ảnh (đồng nhất nhân vật, không logo/chữ lạ, không máu me) + xem khung chuyển động | `python factory/_engine/run.py gate EP09 2 --placeholder` rồi `... gate EP09 4 --preview` | ☐ |
| 2 | Sinh giọng thật + **nghe duyệt từng câu** | `python factory/_engine/run.py gate EP09 2` → `... signoff EP09 --listen PASS --by "<tên>"` | ☐ |
| 3 | SFX/BGM + master | `python factory/_engine/run.py gate EP09 3` | ☐ |
| 4 | Timeline + overlay + render video | `python factory/_engine/run.py gate EP09 4` | ☐ |
| 5 | Render staging + QA 8 điểm → xem video → ký duyệt điểm 2, 4, 5 | `... gate EP09 5` → `... signoff EP09 --point 2 4 5 --by "<tên>"` → `... gate EP09 5 --skip-render` | ☐ |
| 6 | Đóng gói phát hành | `python factory/_engine/run.py gate EP09 6` | ☐ |

Ghi chú vòng sửa:
- 

