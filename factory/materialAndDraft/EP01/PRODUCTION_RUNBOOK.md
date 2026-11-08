# PHIẾU THỰC THI – EP01: Người lạ chìa tiền ở cổng trường

Lệnh chạy từ thư mục gốc dự án (`c:\projects\socialScamStorys`).

| Gate | Việc | Lệnh | Xong |
| :-: | :--- | :--- | :-: |
| 0 | Kịch bản + Clearance ĐẠT + đủ ảnh `assets/scene1..6.jpg` + `episode.json` | `python factory/_engine/run.py gate0 EP01` | ☐ |
| 1 | Duyệt ảnh (đồng nhất nhân vật, không logo/chữ lạ, không máu me) + xem khung chuyển động | `python factory/_engine/run.py gate EP01 2 --placeholder` rồi `... gate EP01 4 --preview` | ☐ |
| 2 | Sinh giọng thật + **nghe duyệt từng câu** | `python factory/_engine/run.py gate EP01 2` → `... signoff EP01 --listen PASS --by "<tên>"` | ☐ |
| 3 | SFX/BGM + master | `python factory/_engine/run.py gate EP01 3` | ☐ |
| 4 | Timeline + overlay + render video | `python factory/_engine/run.py gate EP01 4` | ☐ |
| 5 | Render staging + QA 8 điểm → xem video → ký duyệt điểm 2, 4, 5 | `... gate EP01 5` → `... signoff EP01 --point 2 4 5 --by "<tên>"` → `... gate EP01 5 --skip-render` | ☐ |
| 6 | Đóng gói phát hành | `python factory/_engine/run.py gate EP01 6` | ☐ |

Ghi chú vòng sửa:
- 

