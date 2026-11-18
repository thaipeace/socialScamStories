# PHIẾU THỰC THI (16:9 LONG-FORM 4–5+ PHÚT) – EP06: Ba triệu tám trên màn hình

Lệnh chạy từ thư mục gốc dự án (`c:\projects\socialScamStories`).

| Gate | Việc | Lệnh | Xong |
| :-: | :--- | :--- | :-: |
| 0 | Kịch bản 4–5 phút (`~260s–285s` ≥ 240s, chuẩn hóa từ `story.txt`) + Clearance ĐẠT + `source/build_draft.py` → `episode.json` *(chờ sinh đủ ảnh `c00..c12.jpg` khi lên Staging)* | `python factory196/materialAndDraft/EP06/source/build_draft.py` rồi `python factory196/_engine/run.py gate0 EP06` | ⏳ Đã xong kịch bản & `episode.json` Tầng 1 |
| 1 | Sinh & duyệt ảnh 16:9 (13 ảnh `c00..c12.jpg` `1920x1080`, Nam cạo râu nhẵn xuyên suốt, `c09` & `c11` người bạn IT cố ý không lộ mặt 100%, không viền letterbox, không chữ/logo/URL) | Kiểm tra trực quan từng ảnh & khung `preview_frames/*_safezone.jpg` | ☐ |
| 2 | Sinh giọng thật (`30/30` câu `gemini-3.8-flash-tts`, 7 tuyến nhân vật = 7 voice tách biệt) + căn timeline theo WAV thật + nghe rà soát cả 30 file `.mp3` | `python factory196/_engine/run.py gate EP06 2` | ☐ |
| 3 | SFX/BGM + master | `python factory196/_engine/run.py gate EP06 3` | ☐ |
| 4 | Timeline `1920x1080 @ 30fps` + Chapter cards + Boxless Subtitle + Safe Zone QA | `python factory196/_engine/run.py gate EP06 4` | ☐ |
| 5 | Render staging + QA 8 điểm → **DỪNG CHỜ CHỦ KÊNH DUYỆT STAGING** | `python factory196/_engine/run.py gate EP06 5` | ☐ |
| 6 | Đóng gói phát hành (chỉ chạy sau khi chủ kênh duyệt Staging) | `python factory196/_engine/run.py signoff EP06 --listen PASS --point 2 4 5 --by "Chủ kênh"` → `... gate EP06 5 --skip-render` → `... gate EP06 6` | ☐ |

Ghi chú vòng sửa:
- **19/11/2026 – v1-draft:** Chuẩn hóa bản nháp `story.txt` sang trọn bộ hồ sơ Tầng 1 `factory196/EP06` (15 cảnh, 30 câu thoại ngắn gọn `≤ 25 từ`, Người Bóc Trần 1 câu `< 9s`, giữ nguyên nhân vật Người bạn IT giấu mặt + cài chi tiết "Từ năm 2018" + kết mở cụm máy chủ ngầm).
