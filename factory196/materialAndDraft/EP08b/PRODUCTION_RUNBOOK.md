# PHIẾU THỰC THI (16:9 LONG-FORM ~5 PHÚT) – EP08b: Tiền nổi rồi, tên lại khác

Lệnh chạy từ thư mục gốc dự án (`socialScamStories`).

| Gate | Việc | Lệnh | Xong |
| :-: | :--- | :--- | :-: |
| 0 | Kịch bản ~5 phút (`~320s–330s`, đạt chuẩn `240s–330s`, giấu twist gọn đến Hồi 3 `s08a` rồi bùng nổ mặt & giọng Khang từ `EP08`, kết mở hội tụ toàn bộ mắt xích `EP08` & `EP08b` dưới chỉ đạo Người đàn bà bí mật) + Clearance ĐẠT + `source/build_draft.py` → `episode.json` *(chờ sinh đủ 21 ảnh `c00a, c00..c07, c08a, c08..c15, c16a, c16b, c17.jpg`)* | `python3 factory196/materialAndDraft/EP08b/source/build_draft.py` rồi `python3 factory196/_engine/run.py gate0 EP08b` | ⏳ Đã xong kịch bản v1 & `episode.json` Tầng 1 |
| 1 | Sinh & duyệt ảnh 16:9 (21 ảnh `c00a..c17.jpg` `1920x1080`: `c00a` chia đôi màu `cyan-amber` giấu mặt; `c08a` hiện rõ mặt Khang & Anh Đạt hồi ức `EP08 c12` nổ twist Hồi 3; phòng công chứng đông đúc `c04/c05`; xe tay ga xám bạc không logo/biển số `c02/c06`; `c16a` lưới 4 ô hội tụ Kẻ đứng giữa + Đàn em `EP08`, Long, Người mua hộ nữ & bàn tay cổ tay áo xanh ngọc lục bảo; `c16b` Người phụ nữ bí ẩn **giấu mặt 100%** chỉ lộ bóng tóc bob đen & áo xanh ngọc lục bảo gợi mờ Chị Hai `EP04`; cắt đen `c17`) | Kiểm tra trực quan từng ảnh & khung `preview_frames/*_safezone.jpg` | ☐ |
| 2 | Sinh giọng thật (`42/42` câu `gemini-3.8-flash-tts`, 10 tuyến nhân vật = 10 voice tách biệt, đồng bộ `Puck` cho câu hồi ức Khang ở `s08a`, `Fenrir` của `EP08`/`EP04`, `Algieba` cho Long khớp `EP08 s08` + kết mở, `Aoede` cho người mua hộ nữ, `Kore` liên đới Chị Hai `EP04`) + chạy lại `build_draft.py` căn timeline theo WAV thật + nghe rà soát cả 42 file `.mp3` | `python3 factory196/_engine/run.py gate EP08b 2` | ☐ |
| 3 | SFX/BGM + master | `python3 factory196/_engine/run.py gate EP08b 3` | ☐ |
| 4 | Timeline `1920x1080 @ 30fps` + Chapter cards + Boxless Subtitle + Safe Zone QA | `python3 factory196/_engine/run.py gate EP08b 4` | ☐ |
| 5 | Render staging + QA 8 điểm → **DỪNG CHỜ CHỦ KÊNH DUYỆT STAGING** | `python3 factory196/_engine/run.py gate EP08b 5` | ☐ |
| 6 | Đóng gói phát hành (chỉ chạy sau khi chủ kênh duyệt Staging) | `python3 factory196/_engine/run.py signoff EP08b --listen PASS --point 2 4 5 --by "Chủ kênh"` → `... gate EP08b 5 --skip-render` → `... gate EP08b 6` | ☐ |

Ghi chú vòng sửa:
- **21/11/2026 – v1-draft (`EP08b`):** Chuyển đổi từ nháp `EP09` sang **`EP08b`** nối trực tiếp dòng tiền **`45.000.000đ` lúc `12:05 trưa`** từ **Khang (`EP08`)** sang tài khoản **Anh Minh** bán **xe máy tay ga `45 triệu`** tại phòng công chứng đông đúc; bịt kín hoàn toàn lỗ hổng truy vết "đồng bọn tự báo nhầm" bằng thế 2 nạn nhân thật (rửa tiền bẩn đổi thẳng sang xe công chứng); giữ nhịp phòng công chứng kiệm lời có 1 hook tên `"Khang"` ở `s05` và kết mở nhân vật nữ bí mật chỉ đạo chuyển tỉnh sang kèo đất ở `s17–s18`.
