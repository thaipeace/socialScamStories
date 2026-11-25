# PHIẾU THỰC THI (16:9 LONG-FORM 4–5+ PHÚT) – EP05: Tờ năm trăm và sáu giây nhìn thẳng

Lệnh chạy từ thư mục gốc dự án (`c:\projects\socialScamStories`).

| Gate | Việc | Lệnh | Xong |
| :-: | :--- | :--- | :-: |
| 0 | Kịch bản 4–5+ phút (`262.1s` ≥ 240s, phản biện nghiệp vụ ngân hàng & pháp lý 2026, kết mở cắt đúng `04:15`) + Clearance ĐẠT + `source/build_draft.py` → `episode.json` + đủ ảnh 16:9 | `python factory196/materialAndDraft/EP05/source/build_draft.py` rồi `python factory196/_engine/run.py gate0 EP05` | ☑ |
| 1 | Duyệt ảnh 16:9 (14 ảnh `c00..c13.jpg` `1920x1080`, Anh Hai đồng nhất xuyên suốt, `c02` Tom ôm hộp cam + Anh Hai ngập ngừng rút ví, `c04` đứng sát bên chỉ tay né cam trước, `c12` kết mở xe đen đêm mưa, không viền letterbox, không chữ/logo/biển số, bubble không đè mặt) | Đã kiểm tra trực quan 14 ảnh & khung `preview_frames/*_safezone.jpg` | ☑ |
| 2 | Sinh giọng thật (`33/33` câu `gemini-3.8-flash-tts`, 9 tuyến nhân vật = 9 voice tách biệt) + căn timeline theo WAV thật (`262.08s`) + nghe rà soát cả 33 file `.mp3` | `python factory196/_engine/run.py gate EP05 2` + `--listen PASS` | ☑ |
| 3 | SFX/BGM + master (`262.08s`, peak `-2.58 dBFS`, rms `-20.27 dBFS`) | `python factory196/_engine/run.py gate EP05 3` | ☑ |
| 4 | Timeline `1920x1080 @ 30fps` (`7862 frames`) + Chapter cards + Boxless Subtitle + Safe Zone QA | `python factory196/_engine/run.py gate EP05 4` | ☑ |
| 5 | Render staging (`EP05_ToNamTramVaSauGiayNhinThang_262s_staging.mp4`) + QA 8/8 điểm PASS | `python factory196/_engine/run.py gate EP05 5` | ☑ |
| 6 | Đóng gói phát hành (`production/EP05/EP05_ToNamTramVaSauGiayNhinThang_262s.mp4` + `youtube_upload/`) | `python factory196/_engine/run.py gate EP05 6` | ☑ |

Ghi chú vòng sửa:
- **18/11/2026 – v1-draft:** Hoàn thành trọn bộ hồ sơ Tầng 1 và push lên Git (`5356f90`).
- **18/11/2026 – v1-staging (`257.35s`):** Xuất bản dựng Staging v1 gửi chủ kênh review.
- **18/11/2026 – v2-staging (`269.76s`):** Cập nhật 4 góp ý đạo diễn (`c02`, `c04`, `c08`, kết mở `c12`).
- **19/11/2026 – v3-staging (`262.08s` / `04:22`):** Cắt gọn kết mở ngay mốc `04:15` (cắt đen đột ngột ngay sau câu *"Mấy đồng bạc lẻ đó… thả cho nhánh ngoài thử phản ứng thôi."*) để giữ trọn chất bí ẩn mà không lộ trước ý tưởng hay tự trói kịch bản về sau.
- **25/11/2026 – v5-level3-full-abc (`262.08s` / `04:22` · Production Released):** Nâng cấp trọn vẹn chuẩn **HRN-MOTION-L3.0** vượt đủ **CHECK 1 → 2 → 3** (`A=3 · B=4 · C=10 · D=0`; `4` cảnh 2.5D Parallax + Rack Focus `s00, s01, s06, s10b`; `27` rig `eye_blink` + `19` rig `mouth_sync` gồm `6` cảnh 4 trạng thái `round_image` khóa pixel qua `face_roi_prep.py`; `split_screen` `s10a` có chớp mắt & chép miệng trực tiếp trên panel; `36` foley sync `18/18`; đồng bộ `source/build_draft.py` + `source/face_rois.json`). Render 4 worker `cv2` trong `561.08s` (~14.0 fps), chủ kênh duyệt Staging `8/8 PASS` và xuất Gate 6 Production (`SHA-256: 565fcff863f16633...`).
