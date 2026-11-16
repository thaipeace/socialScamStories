# PHIẾU THỰC THI – EP06: Thói quen check-in du lịch mời trộm vào nhà (v5)

Lệnh chạy từ thư mục gốc dự án (`c:\projects\socialScamStories`).

| Gate | Việc | Lệnh | Xong |
| :-: | :--- | :--- | :-: |
| Build | Dàn kịch bản `episode.json` khớp TTS thật + dựng 6 video `assets/scene1..6.mp4` (`30fps`) | `python factory619/materialAndDraft/EP06/source/build_episode.py` + `build_scene_videos.py` | ☑ |
| 0 | Kịch bản + Clearance ĐẠT + đủ 12 ảnh `scene1..6.jpg`/`_b.jpg` + 6 `scene1..6.mp4` | `python factory619/_engine/run.py gate0 EP06` | ☐ |
| 1 | Duyệt 12 ảnh keyframe (đồng nhất nhân vật, không logo/chữ lạ/biển số, 1 khung toàn màn hình) | Kiểm tra trực quan `assets/scene*.jpg` + `staging/EP06/preview_frames/` | ☐ |
| 2 | Sinh giọng thật `gemini-3.8-flash-tts` + **nghe duyệt trực tiếp cả 9 câu** | `python factory619/_engine/run.py gate EP06 2` → `... signoff EP06 --listen PASS --by "agent"` | ☑ |
| 3 | SFX/BGM + master (`47.62s`, `-1.08 dBFS`) | `python factory619/_engine/run.py gate EP06 3` | ☑ |
| 4 | Timeline + overlay + render video `30fps` từ `assets/scene1..6.mp4` | `python factory619/_engine/run.py gate EP06 4` | ☐ |
| 5 | Render staging + QA 8 điểm (DỪNG TẠI ĐÂY chờ chủ kênh duyệt trước Gate 6) | `python factory619/_engine/run.py gate EP06 5` | ☑ |
| 6 | Đóng gói phát hành (chỉ chạy sau khi chủ kênh xác nhận duyệt Staging) | `python factory619/_engine/run.py gate EP06 6` | ☑ |

Ghi chú vòng sửa v5:
- Đổi mở đầu (`s1_hook`) sang cảnh ngồi trên xe trở về nhà xem lại ảnh check-in bãi biển 4 ngày với lời thoại vợ chồng tự nhiên.
- Chỉnh giọng Chú tổ trưởng an ninh (`ong_bay`) và Chú tuần tra (`chu_bao_ve`) nhanh gọn, dứt khoát; cắt bỏ hoàn toàn khoảng lặng câu giờ ở `0:25` (rút tổng thời lượng từ `56.0s` xuống `47.62s`).
- Nâng cấp `assets/` theo đúng chuẩn `EP01`: 12 ảnh keyframe toàn màn hình (`scene1..6.jpg` + `scene1_b..6_b.jpg`) + 6 clip `30fps` (`scene1..6.mp4`).
