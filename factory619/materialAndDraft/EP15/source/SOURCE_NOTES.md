# GHI CHÚ NGUỒN CẢM HỨNG (NỘI BỘ — KHÔNG PHÁT HÀNH CÔNG KHAI)

- **Nguồn báo chí / truyền hình tham khảo:**
  - Phóng sự VTV24 — *Thật - Giả, Kiểm chứng: Cảnh báo tình trạng làm giả biên lai chuyển khoản* (`https://www.youtube.com/watch?v=QZ0jBQiQyk0`, thời lượng 3:55).
- **Tóm tắt các điểm chính từ phóng sự VTV24:**
  1. **Trục 1 — Ứng dụng ngân hàng giả mạo (`Fake Banking App`, `00:00–01:55` — CHỌN LÀM TRỤC CHÍNH CHO `EP15`):**
     - Trước đây kẻ gian chủ yếu chỉnh sửa ảnh chụp màn hình giao dịch (bill photoshop). Hiện nay xuất hiện hẳn các **ứng dụng ngân hàng giả mạo** mô phỏng giao diện và các bước thao tác thanh toán giống gần như tuyệt đối (~99,99%), được rao bán công khai trên mạng xã hội.
     - Kẻ gian tự nhập số tiền (từ đơn hàng chợ đến hàng trăm triệu / gần tỷ đồng), ngày giờ, tên người nhận, ngân hàng thụ hưởng, nội dung giao dịch rồi cho hiển thị thông báo **“Thành công”** ngay trên điện thoại của chúng trước mặt tiểu thương/người bán — nhưng thực tế tài khoản người bán không hề nhận được tiền.
  2. **Trục 2 — Mã QR giả dẫn sang web phishing ngân hàng (`01:55–02:55` — KHÔNG NHỒI VÀO `EP15`):**
     - Quét mã QR giả dẫn đến trang web giao diện nhái ngân hàng yêu cầu nhập PIN, mật khẩu, OTP để chiếm đoạt tài khoản. Đã chủ động tách bỏ khỏi `EP15` để giữ Short tập trung 1 trục duy nhất và tránh giẫm chân lên cơ chế phishing/OTP ở `EP08` & dán đè QR ở `EP04`.
  3. **Khuyến cáo & góc nhìn pháp lý trong phóng sự (`02:55–03:35`):**
     - Nguyên tắc vàng: **“Kiểm trước, tin sau”** — tuyệt đối không chỉ nhìn màn hình của người gửi mà phải kiểm tra trực tiếp biến động số dư trên tài khoản của chính mình (hoặc thiết bị loa báo chuyển khoản).
     - Lưu ý pháp lý nội bộ: hành vi dùng chứng từ giả / ứng dụng ngân hàng giả chiếm đoạt tài sản có dấu hiệu cấu thành tội lừa đảo chiếm đoạt tài sản (tham chiếu Điều 174 BLHS trong phóng sự — không đọc số điều luật trong thoại phim theo `L7`). Ngoài ra, việc tải/cài các ứng dụng giả mạo còn tiềm ẩn nguy cơ mã độc đánh cắp dữ liệu.
- **Định hướng hư cấu hóa & dựng phim riêng cho `factory619/EP15`:**
  - Hư cấu hóa 100% qua dàn Cast cố định (`02_CAST/cast.json`) gói gọn trong 1 bối cảnh sạp chợ buổi sáng duy nhất (không nhân vật phụ thừa): **Cô Tư (`co_tu`)**, **Bé Na (`be_na`)**, **Khách nam lịch sự (`ke_ngot_ngao_nam`, ghi đè `af: "default"`)** và **Người Bóc Trần (`nguoi_boc_tran`)**.
  - Khai thác đỉnh cao kịch tính đời thực: để chính người trẻ (`be_na`) suýt tin vì *“đứng nhìn tận mắt bấm chuyển trên app chứ đâu phải hình chụp”*, sau đó kẻ gian đẩy cao trào bằng đòn kì kèo tâm lý *“đã trừ tiền rồi, trả tiền mặt nữa thành hai lần sao?!”* khiến Na nao núng → **Cô Tư** phá thế bí bằng 2 lựa chọn sòng phẳng tuyệt đối (sạp cố định nhận tiền mặt ký giấy hẹn hoàn lại khi tiền về, hoặc mở lịch sử trừ số dư / đứng chờ tiền nổi) khiến kẻ gian cứng họng bỏ hàng vọt mất (tự chứng minh không hề chuyển tiền thật).
  - Cài–trả âm thanh: toàn bộ phần kịch không dùng `bank_ting` để nhấn sự im lặng bất thường của máy/loa Cô Tư; chỉ bật đúng 1 tiếng `bank_ting` thật ở Kết mở câm thoại 2.5D (`Khung 9`).
  - Khóa chuẩn pháp lý & thuật toán (`HRN-LEGAL-SCAM-V1` + `policy_wordlists.json`): không nêu nơi mua app giả, không hướng dẫn nhập trường giả lập (`L2`), không logo/tên/màu giao diện ngân hàng thật (`L4`), 0 từ khóa nhạy cảm.
- **Mục tiêu Thư viện Cảnh giác (`STRAT-VIGILANCE-LIB-V1`):**
  - Lấp khoảng trống **`VAR-COM-02`** (mua bán trực tiếp — biên lai/app ngân hàng giả + đòn kì kèo hối giao hàng ngay) theo góc quan sát **`D/B`** trên nhà máy `factory619`.
