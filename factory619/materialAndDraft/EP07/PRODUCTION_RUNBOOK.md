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

Ghi chú vòng nâng cấp:
- `v3-level2-abc` (`52.31s`, `HRN-MOTION-L2.1`): Nâng cấp toàn tập với 23 mảnh mặt sống (`eye_blink` + `mouth_sync` 3 trạng thái khớp WAV, `overlap = 0` trên `s2` song thoại Cô Tư ↔ Bé Na, `s3` song thoại Ông Bảy ↔ Bé Na, `s4` tam thoại Ông Bảy → Bé Na → Cô Tư) + 2 cảnh 2.5D (`s4` 3 lớp có quầy nước tiền cảnh đứng vững & mặt nhân vật khóa cứng layer `subject`; `s5` 2 lớp kính lúp/xu vàng trên nền mạch xanh). `A=1 · B=2 · C=3 · D=0`, Gate 5 đạt `8/8 PASS`, xuất bản Gate 6 (thumbnail `35.38s` sạch không phụ đề, giữ nguyên `EP07_Uploaded`).
