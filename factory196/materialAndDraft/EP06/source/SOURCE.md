# NGUỒN CẢM HỨNG & HỒ SƠ CHUYỂN HÓA KỊCH BẢN (NỘI BỘ) – 196 EP06

## 1. Chất liệu gốc & phân tích tâm lý
- **Bản nháp ý tưởng gốc:** [`story.txt`](../story.txt) (*Cộng tác viên mua hàng online*) do chủ kênh cung cấp — khai thác góc nhìn tâm lý đời thường cực kỳ tinh tế: sự nhầm lẫn giữa **tiền thật đi ra từ tài khoản ngân hàng** và **con số ảo do người dựng web tự gõ lên màn hình**.
- **Chuẩn hóa nghiệp vụ & cấu trúc theo `LONG_FORMAT_196_SPEC.md`:**
  1. **Khớp chuẩn toán học mồi nhử:** Điều chỉnh vốn cấp sẵn thành `40.000đ` → hoàn thành đơn đầu `30.000đ` nhảy lên `45.000đ` (không tốn 1 đồng tiền túi) → đơn thứ hai `55.000đ` thiếu đúng `10.000đ` (`55.000 - 45.000 = 10.000đ`).
  2. **Hiệu ứng "bù phần chênh lệch thiếu":** Giải thích hợp lý vì sao người tỉnh táo vẫn mất hơn hai triệu mà không giật mình ngay — vì mỗi đơn web đều tính gộp số dư ảo sẵn có, chỉ bắt chuyển thêm phần chênh lệch nhỏ (`10.000đ` → `180.000đ` → `450.000đ` → `1.500.000đ` = `-2.140.000đ` tiền thật), cho đến khi treo ở mốc `3.850.000đ` và đòi bù `2.900.000đ`.
  3. **Cài – trả chi tiết tên miền & nhân vật Người bạn IT giấu mặt:** Giữ trọn yêu cầu trong ghi chú sản xuất của [`story.txt`](../story.txt): cài rõ thông tin trang tự nhận *"Vận hành từ năm 2018"* ngay ở Hồi 1 (`s03`), để người bạn IT giấu mặt tra cứu tuổi tên miền thật (mới mở 6 ngày) ở Hồi 4 (`s09`), đồng thời mở thêm một đầu mút 10 giây ở cuối phim về cụm máy chủ chung đầu mối với các nhánh trước mà không làm ảnh hưởng đến cái kết trọn vẹn của vợ chồng Nam – Thảo.

## 2. Bảng hư cấu hóa 100% (Tuân thủ 5 Nguyên tắc vàng `CONTENT_LEGAL_SAFETY_HARNESS.md`)
| Chi tiết nhạy cảm (KHÔNG ĐƯA VÀO PHIM) | Chi tiết hư cấu hóa trên phim (`196 EP06`) | Lý do an toàn pháp lý |
| :--- | :--- | :--- |
| Tên sàn TMĐT, công ty, ngân hàng hoặc ví điện tử thật | **“Sàn Đối Tác Đơn Hàng”**, **“Ngân hàng của Nam”**, **“TK …6821”** | Sạch 100% `identity_hard_block` & `ACCOUNT_RE` |
| Tên miền cụ thể có đuôi `.com`, `.vn`, `.online`... | Nhãn mô tả **“Ngày đăng ký thật: Thứ Ba tuần trước (6 ngày)”** | Sạch 100% `URL_RE` (tránh trùng tên miền có thật) |
| Nền tảng mạng xã hội / ứng dụng nhắn tin cụ thể | **“Tin nhắn”**, **“Đường dẫn”** | Sạch 100% `identity_soft_warn` |
| Cụm từ nhạy cảm thuật toán (`kiếm tiền online`, `lãi khủng`...) | **“Cộng tác viên đơn hàng”**, **“Bù phần thiếu”**, **“Nhận đơn phụ buổi tối”** | Sạch 100% `asr_ocr_soft_warn` |

## 3. Trạng thái hồ sơ
- **Giai đoạn hiện tại:** Hồ sơ Tầng 1 (`factory196/materialAndDraft/EP06`) đã hoàn chỉnh kịch bản `SCRIPT.md`, `source/build_draft.py`, `episode.json`, `IMAGE_PROMPTS.md`, `clearance/CLEARANCE.md` — sẵn sàng chờ chủ kênh duyệt kịch bản để sinh bộ ảnh `16:9` (`assets/c00.jpg..c12.jpg`), thu TTS Gate 2 và dựng bản Staging Gate 5.
