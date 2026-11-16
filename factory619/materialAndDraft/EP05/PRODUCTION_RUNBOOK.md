# PHIẾU THỰC THI – EP05: Bẫy Tình Ái Kết Hợp Nhiệm Vụ Chốt Đơn (`v5` — 13 Keyframes + 6 clip `30fps`)

Lệnh chạy từ thư mục gốc dự án (`c:\projects\socialScamStories`).

| Gate | Việc | Lệnh | Xong |
| :-: | :--- | :--- | :-: |
| 0 | Kịch bản + Clearance ĐẠT + đủ 13 ảnh keyframe + 6 clip `assets/scene1..6.mp4` + `episode.json` | `python factory619/_engine/run.py gate0 EP05` | ☑ |
| 1 | Duyệt ảnh (đồng nhất nhân vật, không logo/chữ lạ, không máu me) + xem khung chuyển động & chia màn hình | `python factory619/materialAndDraft/EP05/source/build_scene_videos.py` | ☑ |
| 2 | Sinh giọng thật (`gemini-3.8-flash-tts`) + **nghe duyệt từng câu** (`l1..l9`) | `python factory619/_engine/run.py gate EP05 2` → `... signoff EP05 --listen PASS` | ☑ |
| 3 | SFX/BGM + master (`-14 LUFS`, `-1.5 dBTP`) | `python factory619/_engine/run.py gate EP05 3` | ☑ |
| 4 | Timeline + overlay (boxless subtitle + callout tránh che mặt) + render video | `python factory619/_engine/run.py gate EP05 4` | ☑ |
| 5 | Render staging + QA 8 điểm → xem khung Safe Zone → ký duyệt điểm 2, 4, 5 (`8/8 PASS`) | `... gate EP05 5` → `... signoff EP05 --point 2 4 5` → `... gate EP05 5 --skip-render` | ☑ |
| 6 | Đóng gói phát hành (`factory619/production/EP05/` + `06_RENDERED_SHORTS/`) | `python factory619/_engine/run.py gate EP05 6` | ☑ |

Ghi chú vòng sửa:
- `v5`: Nâng cấp kiến trúc chuyển động đa keyframe giống `EP01`/`EP06` với 13 keyframe `9:16` và 6 đoạn video `30fps` (`scene1.mp4 .. scene6.mp4`), kết hợp bố cục chia đôi màn hình đúng cao trào đối lập (`scene1_b`, `scene2_b`, `scene4_c`) và cú lật 3 nhịp RGB glitch xé mặt nạ AI ngay khoảnh khắc quơ tay (`scene4 -> scene4_b -> scene4_c`).
