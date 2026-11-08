# PHIẾU THỰC THI – EP05: Bẫy việc nhẹ lương cao thả tim chốt đơn ảo

Lệnh chạy từ thư mục gốc dự án (`c:\projects\socialScamStorys`).

| Gate | Việc | Lệnh | Xong |
| :-: | :--- | :--- | :-: |
| 0 | Kịch bản + Clearance ĐẠT + đủ ảnh `assets/scene1..6.jpg` + `episode.json` | `python factory/_engine/run.py gate0 EP05` | ☐ |
| 1 | Duyệt ảnh (đồng nhất nhân vật, không logo/chữ lạ, không máu me) + xem khung chuyển động | `python factory/_engine/run.py gate EP05 2 --placeholder` rồi `... gate EP05 4 --preview` | ☐ |
| 2 | Sinh giọng thật + **nghe duyệt từng câu** | `python factory/_engine/run.py gate EP05 2` → `... signoff EP05 --listen PASS --by "<tên>"` | ☐ |
| 3 | SFX/BGM + master | `python factory/_engine/run.py gate EP05 3` | ☐ |
| 4 | Timeline + overlay + render video | `python factory/_engine/run.py gate EP05 4` | ☐ |
| 5 | Render staging + QA 8 điểm → xem video → ký duyệt điểm 2, 4, 5 | `... gate EP05 5` → `... signoff EP05 --point 2 4 5 --by "<tên>"` → `... gate EP05 5 --skip-render` | ☐ |
| 6 | Đóng gói phát hành | `python factory/_engine/run.py gate EP05 6` | ☐ |

Ghi chú vòng sửa:
- 

