# PHIẾU THỰC THI – EP08: Biên lai báo nghẽn mạng – Chỉ bấm "nhận lương" mà trắng tay

Lệnh chạy từ thư mục gốc dự án (`c:\projects\socialScamStories`).

| Gate | Việc | Lệnh | Xong |
| :-: | :--- | :--- | :-: |
| 0 | Kịch bản + Clearance ĐẠT + đủ ảnh `assets/scene1..6.jpg` + `episode.json` | `python factory619/_engine/run.py gate0 EP08` | ☑ |
| 1 | Duyệt ảnh (đồng nhất nhân vật, không logo/chữ/số) + xem khung chuyển động | `python factory619/_engine/run.py gate EP08 4 --preview` | ☑ |
| 2 | Sinh giọng thật + **nghe duyệt từng câu** + dàn lại timeline WAV thật | `python factory619/_engine/run.py gate EP08 2` → `python factory619/materialAndDraft/EP08/source/build_episode.py` | ☑ |
| 3 | SFX/BGM + master | `python factory619/_engine/run.py gate EP08 3` | ☑ |
| 4 | Timeline + overlay + render video | `python factory619/_engine/run.py gate EP08 4` | ☑ |
| 5 | Render staging + QA 8 điểm → xem video → chờ chủ kênh duyệt | `python factory619/_engine/run.py gate EP08 5` | ☑ |
| 6 | Đóng gói phát hành (chỉ chạy sau khi chủ kênh duyệt Staging) | `python factory619/_engine/run.py gate EP08 6` | ☑ |
