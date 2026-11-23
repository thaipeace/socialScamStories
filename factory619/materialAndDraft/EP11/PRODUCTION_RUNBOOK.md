# PHIẾU THỰC THI – EP11: Đám đông – Một cú va chạm, mất sạch dây chuyền

Lệnh chạy từ thư mục gốc dự án (`c:\projects\socialScamStories`).

| Gate | Việc | Lệnh | Xong |
| :-: | :--- | :--- | :-: |
| 0 | Kịch bản + **Visual Motion Plan (Level 2: `beat_type`, `motion_level` A/B/C/D)** + Clearance ĐẠT + đủ ảnh `assets/scene1..6.jpg` + `episode.json` | `python factory619/_engine/run.py motion-check EP11` rồi `... gate0 EP11` | ☐ |
| 1 | Duyệt ảnh (đồng nhất nhân vật, không logo/chữ lạ, không máu me) + chuẩn bị biến thể **Living-Character A/B/C** (`eye_blink`/`mouth_sync` qua `03_ENGINE/face_roi_prep.py`, duyệt bảng QC cận mặt), lớp Level B + `breathing`, ảnh đồng khung Level C + xem khung QA | `python factory619/_engine/run.py gate EP11 2 --placeholder` rồi `... gate EP11 4 --preview` | ☐ |
| 2 | Sinh giọng thật + **nghe duyệt từng câu** | `python factory619/_engine/run.py gate EP11 2` → `... signoff EP11 --listen PASS --by "<tên>"` | ☐ |
| 3 | SFX/BGM + khớp foley với chuyển động Level C (`click`/`notification`/`light_switch`/`low_accent`) + master | `python factory619/_engine/run.py gate EP11 3` | ☐ |
| 4 | Timeline + Visual Motion Level 2 (A/B/C/D) + overlay + render video | `python factory619/_engine/run.py gate EP11 4` | ☐ |
| 5 | Render staging + QA 8 điểm + **Visual Motion QC 11 điểm** (`GATE5_QA_REPORT.md`; hạ cấp về Level A nếu hiệu ứng lỗi) → **DỪNG CHỜ DUYỆT STAGING** → ký duyệt điểm 2, 4, 5 | `... gate EP11 5` → `... signoff EP11 --point 2 4 5 --by "<tên>"` → `... gate EP11 5 --skip-render` | ☐ |
| 6 | Đóng gói phát hành (chỉ chạy sau khi chủ kênh duyệt Staging) | `python factory619/_engine/run.py gate EP11 6` | ☐ |

Ghi chú vòng sửa:
- 

