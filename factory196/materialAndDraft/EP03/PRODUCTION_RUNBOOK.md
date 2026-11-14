# PHIẾU THỰC THI (16:9 LONG-FORM 4–5+ PHÚT) – EP03: 120 ngàn – Phút thứ 89

Lệnh chạy từ thư mục gốc dự án (`/Users/thainguyendev/projects/socialScamStories`).

| Gate | Việc | Lệnh | Xong |
| :-: | :--- | :--- | :-: |
| 0 | Kịch bản 4–5+ phút (≥ 240s, phản biện pháp lý & logic) + Clearance ĐẠT + đủ ảnh 16:9 + `episode.json` | `python3 factory196/_engine/run.py gate0 EP03` | ☐ |
| 1 | Duyệt ảnh 16:9 (không viền letterbox, không chữ/logo/biển số, cảnh lên hình trước thoại 0.3s) + xem khung QA | `python3 factory196/_engine/run.py gate EP03 4 --preview` | ☐ |
| 2 | Sinh giọng thật (tách rõ âm sắc các nhân vật cùng giới) + căn lại timeline theo WAV thật + **nghe duyệt `.mp3`** | `python3 factory196/_engine/run.py gate EP03 2` → `python3 factory196/materialAndDraft/EP03/source/build_episode.py` → `... signoff EP03 --listen PASS --by "Chủ kênh"` | ☐ |
| 3 | SFX/BGM + master (≥ 240s) | `python3 factory196/_engine/run.py gate EP03 3` | ☐ |
| 4 | Timeline 1920x1080 + Chapter cards + Subtitle + Render video | `python3 factory196/_engine/run.py gate EP03 4` | ☐ |
| 5 | Render staging + QA 8 điểm → **DỪNG CHỜ CHỦ KÊNH DUYỆT STAGING** → ký duyệt điểm 2, 4, 5 | `python3 factory196/_engine/run.py gate EP03 5` | ☐ |
| 6 | Đóng gói phát hành (chỉ chạy sau khi chủ kênh duyệt Staging) | `python3 factory196/_engine/run.py gate EP03 6` | ☐ |

Ghi chú vòng sửa:
- `episode.json` được sinh từ `source/build_episode.py`.
- **Real-TTS Retiming:** sau Gate 2 chạy lại `python3 factory196/materialAndDraft/EP03/source/build_episode.py` để dàn lại toàn bộ timeline theo độ dài WAV thật.

