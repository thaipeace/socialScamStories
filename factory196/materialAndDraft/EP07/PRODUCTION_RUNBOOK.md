# PHIẾU THỰC THI (16:9 LONG-FORM ~7 PHÚT) – EP07: Sau hai trăm triệu *(v5)*

Lệnh chạy từ thư mục gốc dự án (`socialScamStories`).

| Gate | Việc | Lệnh | Xong |
| :-: | :--- | :--- | :-: |
| 0 | Kịch bản v5 đã căn theo WAV thật (`463.6s = 07:43`, `49 câu`, `1031 từ`, `133 từ/phút`) + Clearance `ĐẠT` + đủ 23 ảnh `1920x1080` | `python factory196/materialAndDraft/EP07/source/build_draft.py` rồi `python factory196/_engine/run.py gate0 EP07` | ☑ |
| 1 | Sinh & duyệt ảnh 16:9 (**23 ảnh** `c00..c09, c09b, c10..c19, c19b, c20.jpg` `1920x1080`: đồng nhất Ông Thành 65t, Trang 26t, Bé Bo 5t, Ông Tám 60t + lắc bạc, đồng hồ/vệt da cổ tay trái, giao diện app trừu tượng đồng nhất giữa `c04` & `c19b`, cán bộ áo sơ mi trắng trơn, Khoa giấu mặt) | Đã kiểm tra trực quan 23/23 ảnh & `preview_frames/*_safezone.jpg` | ☑ |
| 2 | Sinh giọng thật (`49/49` câu `PASS`, 100% `gemini-3.8-flash-tts`, **8 tuyến = 8 voice độc lập**) + căn timeline theo WAV thật | `python factory196/_engine/run.py gate EP07 2` | ☑ |
| 3 | SFX/BGM + master (`463.61s · peak -2.57 dBFS · rms -20.45 dBFS`) | `python factory196/_engine/run.py gate EP07 3` | ☑ |
| 4 | Timeline `1920x1080 @ 30fps` (`13.908 frames`) + Chapter cards + Màn hình đen chữ trắng + Boxless Subtitle + `29` khung Safe Zone QA | `python factory196/_engine/run.py gate EP07 4` | ☑ |
| 5 | Render staging (`EP07_SauHaiTramTrieu_464s_staging.mp4`) + QA 8 điểm (**ĐẠT 8/8 PASS** sau khi Chủ kênh ký duyệt) | `python factory196/_engine/run.py gate EP07 5` | ☑ |
| 6 | Đóng gói phát hành Production (`EP07_SauHaiTramTrieu_464s.mp4`, SRT, Thumbnail 16:9 & 9:16, `PUBLISH_PACKAGE_EP07.md`, `youtube_upload/`, bản sao `06_RENDERED_VIDEOS/`) | `python factory196/_engine/run.py signoff EP07 --listen PASS --point 2 4 5 --by "Chủ kênh"` → `... gate EP07 5 --skip-render` → `... gate EP07 6` | ☑ |

Ghi chú vòng sửa:
- **19/11/2026 – v1-draft:** Hoàn chỉnh trọn bộ hồ sơ Tầng 1 `factory196/EP07` (24 cảnh, 48 câu thoại).
- **19/11/2026 – v2-draft:** Sửa theo phản biện pháp lý (11 điểm): bỏ "anh hùng mạng/hiệp sĩ/pháp lý/tài sản số", bạn cũ không truy tìm được ai, cán bộ có hành động thật với khoản mới, sửa mốc ngày và lần chặn trùng, chốt bằng "nỗi xấu hổ", thêm bước gọi ngân hàng. Clearance chuyển về CHỜ DUYỆT.
- **19/11/2026 – v3-draft:** Thoát mô-típ vợ–chồng–con; chuyển trục nhân vật sang **Ông Thành (65t, vừa về hưu) – Trang (26t, con gái) – Bé Bo (5t, cháu trai)**.
- **19/11/2026 – v4-draft:** Làm mờ quá trình lừa lần 1 kéo dài 3 tuần (`s04`); nâng **Ông Tám** thành **nhân vật bí ẩn**; nâng cấp Hồi 3 sang **nhử từng đợt nhỏ `1tr → 2tr → 7tr → 15tr → 30tr`** kèm cảnh mới `s09b` (`c09b`) với bằng chứng mồi & ghi âm cũ của Ngọc (`Aoede`).
- **19/11/2026 – v5-draft:** Bỏ lời chọc tức ở `s12` sang chốt dứt khoát lạnh băng (`l32_khoa`) rồi chặn ngay; tối giản cảnh kết mở `s21b` (`c19b`) hoàn toàn câm (không thoại, không bong bóng) — chỉ bóng lưng quen thuộc (áo đen, lắc bạc) của Ông Tám vẫy chào bạn già mới ở quán cà phê ven biển (địa bàn khác) cùng giao diện app quen thuộc đã sập trên bàn; đổi câu cán bộ `l39a_cb` sang cách nói chuẩn mực nghiệp vụ an toàn nhất.
