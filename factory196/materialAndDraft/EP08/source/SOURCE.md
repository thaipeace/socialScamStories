# NGUỒN CẢM HỨNG & HỒ SƠ CHUYỂN HÓA KỊCH BẢN (NỘI BỘ) – 196 EP08

## 1. Chất liệu tham khảo & định hướng sáng tạo độc lập (v2-draft)
- **Cơ chế cảnh báo thực tế:** Thủ đoạn lừa đảo kiểu **"người đứng giữa" (Man-in-the-Middle)** lợi dụng tài khoản nhắn tin bị xâm nhập để đọc lén lịch sử trò chuyện giữa hai người quen có độ tin cậy cao, sau đó lập tài khoản mạo danh điều phối cả hai tự gọi điện cho nhau và chuyển tiền đường vòng sang tài khoản lạ.
- **Chuyển hóa sáng tạo độc lập 100% cho `factory196 EP08`:**
  1. **Thay mới hoàn toàn nhân vật, bối cảnh, vật phẩm, mốc tiền và tình tiết nghi ngờ:** Tuyến nhân vật hư cấu **Anh Đạt (38t, chủ xưởng nội thất nhỏ) – Khang (26t, kỹ thuật viên 3 năm) – Chị Quyên (vợ Đạt) – Hân (đồng nghiệp)**; mồi câu là *đặt đồng hồ kỷ niệm 10 năm ngày cưới* với lý do *tài khoản gia đình báo biến động số dư chung*; mốc tiền `45 triệu` (lần 1) và `30 triệu` (lần 2); loại bỏ hoàn toàn từ khóa cờ bạc/cá độ.
  2. **Sửa điểm khó theo dõi ở v2 (chuyển giải thích chữ thành thoại sống):** Bỏ sạch 2 bong bóng giải thích dài ở `s03`, thay bằng 4 câu đối thoại gọn sắc giữa **Kẻ đứng giữa** và **Đàn em kỹ thuật** (cả hai giấu mặt) để người xem chỉ cần nghe là hiểu trọn 100% cơ chế.
  3. **Tăng độ thuyết phục thực tế bằng 2 lớp xác thực giả:** (a) Bắt chước **đúng phong cách nói chuyện đặc trưng** của Anh Đạt (*"cu Khang"*, *"chị nhà"*, *"lộ bài"*, *"làm gọn giùm anh, anh tính"*) thay vì chỉ biết thông tin khô cứng; (b) Bổ sung **cuộc gọi video hình/giọng ghép 3 giây chập chờn** rồi cúp đổ tại mạng yếu ở `s04` để giải thích thuyết phục lý do nạn nhân tin tài khoản mới.
  4. **Kết thúc mở tâm lý ("Xin bằng chứng của nhau"):** Không mở rộng thành đường dây ngầm ở cuối phim. Hậu quả của 45 triệu đánh thẳng vào lòng tin giữa hai anh em ngay trên bàn cà phê quen, cắt đen đột ngột tạo dư âm lặng.
  5. **Cầu nối tinh tế sang `EP08b` (không đổi nội dung hay kết thúc `EP08`):** Cài 1 câu điện thoại ngắn của `Đầu dây lạ` (`l22b_long_p`, voice `Algieba` – khớp Long của `EP08b`) và bóng mờ xe máy tay ga + bìa đỏ tại góc màn hình phòng tối `c08` lúc `12:05`, cùng dải sáng chuyển tiền `cyan-amber` ở `c09` làm điểm nối hài hòa cho khung hình mở màn `EP08b`.

## 2. Bảng hư cấu hóa 100% (Tuân thủ 5 Nguyên tắc vàng `CONTENT_LEGAL_SAFETY_HARNESS.md`)
| Yếu tố nhạy cảm (KHÔNG ĐƯA LÊN PHIM) | Chi tiết hư cấu hóa trên phim (`196 EP08`) | Lý do an toàn pháp lý & thuật toán |
| :--- | :--- | :--- |
| Tên người thật / nhân vật trong clip mạng xã hội | **Anh Đạt – Khang – Chị Quyên – Hân** (100% hư cấu) | Tránh định danh & tránh trùng lặp bản quyền |
| Tên ứng dụng nhắn tin, mạng xã hội cụ thể (`Zalo`, `Facebook`, `Messenger`…) | **“Tài khoản nhắn tin”**, **“Nick mới”**, **“Tin thoại cũ”** | Sạch 100% `identity_soft_warn` & yêu cầu không thương hiệu |
| Tên ngân hàng, tiệm vàng, thương hiệu đồng hồ, cửa hàng thật | **“Ngân hàng của Đạt”**, **“Ngân hàng của Khang”**, **“Cửa hàng”**, **`TK ••••`** | Sạch 100% `identity_hard_block` & `ACCOUNT_RE` |
| Số điện thoại, đường dẫn web, số tài khoản 9–16 chữ số | Không hiển thị bất kỳ chuỗi SĐT, URL hay dãy số TK thật nào | Sạch 100% `PHONE_RE`, `URL_RE`, `ACCOUNT_RE` |
| Từ khóa nhạy cảm (`cá độ`, `cờ bạc`, `chết`, sắc phục công an…) | *"Mày vướng chuyện gì nói thiệt anh coi"*; không vẽ sắc phục | Sạch 100% `asr_ocr_hard_block`, `asr_ocr_soft_warn` & Nguyên tắc 4 |
| Thao tác kỹ thuật hack tài khoản / công cụ làm hình-giọng ghép | Tuyệt đối không mô tả cách hack hay nêu phần mềm/quy trình tạo hình ghép; chỉ nêu đúng cảnh báo *hình ghép 3 giây + bỏ qua báo đăng nhập lạ* | Tuân thủ Nguyên tắc 3 (**Không dạy lừa**) |

## 3. Trạng thái hồ sơ
- **Giai đoạn hiện tại:** Hồ sơ Tầng 1 (`factory196/materialAndDraft/EP08` – v2-draft) đã hoàn chỉnh `story.txt`, `source/SOURCE.md`, `source/build_draft.py`, `episode.json`, `script/SCRIPT.md`, `IMAGE_PROMPTS.md`, `clearance/CLEARANCE.md`, `PRODUCTION_RUNBOOK.md` — sẵn sàng chờ chủ kênh duyệt kịch bản để sinh bộ ảnh `16:9` (`assets/c00.jpg..c15.jpg`), thu TTS Gate 2 và dựng bản Staging Gate 5.
