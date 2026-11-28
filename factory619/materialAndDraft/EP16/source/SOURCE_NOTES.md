# GHI CHÚ NGUỒN CẢM HỨNG (NỘI BỘ — KHÔNG PHÁT HÀNH CÔNG KHAI)

- **Nguồn báo chí quốc tế & trong nước tham khảo (chỉ dùng làm chất liệu gốc, hư cấu hóa 100%):**
  1. **Vụ creator Dolores Cachola-Tapia (`@doloresdaexplorer`, 11/2021 — *CBS 8 San Diego*, *Business Insider*):**
     - Nhà sáng tạo nội dung trẻ dùng tài khoản cá nhân gắn liền với vòng bạn bè thật; bị kẻ gian (mạo danh hợp tác quảng bá) dụ thêm một địa chỉ email đối tác vào phần cài đặt tài khoản, rồi trong 3 phút chiếm quyền kiểm soát, đòi tiền chuộc (**\$500**) và dùng chính trang cá nhân của nạn nhân nhắn tin/đăng bài báo gặp nạn khiến người quen/người theo dõi tin thật chuyển tiền (**\$300**).
  2. **Vụ Nicola Markus (*The Guardian*, 10/6/2024) & Najwa Cagnin (*CBC News*, 12/8/2025):**
     - Phản ánh hệ lụy kép của việc gộp chung **kênh nội dung/kinh doanh** vào cùng **trang cá nhân** dùng nhiều năm: khi bị tấn công hoặc khóa tài khoản, nạn nhân không chỉ mất nguồn thu nhập mà còn mất trắng 5–15 năm ảnh gia đình, kỷ niệm và liên lạc đời thực.
  3. **Bối cảnh thực tế tại Việt Nam (*VnExpress*, *Báo Lao Động*, *CafeF*):**
     - Nhiều người làm nội dung bật chế độ chuyên nghiệp ngay trên trang cá nhân dùng lâu năm; khi bị chiếm trang lập tức dẫn tới vạ lây người thân bị nhắn tin mượn tiền và dễ sập bẫy lần 2 từ các dịch vụ giả mạo "nhận lấy lại tài khoản".

- **Định hướng hư cấu hóa & dựng phim riêng cho `factory619/EP16` (V3):**
  - Hư cấu hóa 100% bằng dàn Cast cố định (`02_CAST/cast.json`) với 6 voice tách biệt hoàn toàn: **Chị Ba (`chi_ba` · `Kore`)**, **Anh Hai (`anh_hai` · `Orus`)**, **Chị Tư (`chi_tu` · `Zephyr`)**, **Đại diện nhãn hàng giả (`ke_ngot_ngao_nu` · `Aoede` · `phone`)**, **Kẻ cướp trang phòng tối (`ke_gia_danh` · `Fenrir` · `phone`)**, và **Người Bóc Trần (`nguoi_boc_tran` · `Charon`)**.
  - **Nâng cấp V3 theo chỉ đạo chủ kênh:**
    1. **Loại bỏ hoàn toàn kiểu "hối hối lẹ lẹ / dọa mất suất" lộ liễu và giọng la hét gây áp lực.** Kẻ giả đại diện nhãn hàng nói năng cực kỳ chuyên nghiệp, điềm đạm, giải thích hợp logic từng bước và còn chủ động khuyên *"Cứ thong thả đọc kỹ!"* — đánh trúng điểm mù tâm lý mới (người xem mặc định *"không hối thì chắc không phải lừa"*).
    2. **Bỏ kết mở** để dồn trọn không gian cho cao trào **2 nấc nghi ngờ – hỏi lại – tự hạ phòng vệ bấm xác nhận**:
       - **Nấc 1:** Thêm email kế toán → máy bắt nhập mật khẩu xác nhận chính chủ → Chị Ba thấy kỳ hỏi lại → đối phương đáp điềm tĩnh *"hệ thống bắt chính chủ xác nhận, bên em đâu đụng máy chị được!"* → bấm bước 1.
       - **Nấc 2:** **Hộp thư email chính** báo đổi quyền quản trị → Chị Ba giật mình hỏi lần 2 → đối phương vẫn nhã nhặn *"mẫu mặc định, nhận tiền xong chị gỡ liền! Cứ thong thả đọc kỹ!"* → Chị Ba tự hạ phòng vệ (*"Chẳng hối gì, nghe cũng hợp lý... chắc quy trình thật!"*) → bấm nốt bước cuối và mất sạch trang!
    3. **Lật mặt lạnh tĩnh (không la hét):** Giọng nam lạnh, đều như một giao dịch thường ngày (*"Trang mười năm ảnh gia đình tôi đang giữ. Hai mươi triệu nhận lại."*) rồi cắt sang hậu quả đời sống thật (bạn thân mất 10 triệu, họ hàng đồng nghiệp gọi tới tấp).
  - Khóa chuẩn pháp lý & thuật toán (`HRN-LEGAL-SCAM-V1` + `policy_wordlists.json`): không nêu tên nền tảng thật, không dùng từ nhạy cảm, không hướng dẫn chi tiết kỹ thuật chiếm quyền (`L2`).

- **Mục tiêu Thư viện Cảnh giác (`STRAT-VIGILANCE-LIB-V1`):**
  - Bổ sung mã biến thể mới **`VAR-ACC-01`** (kịch bản lừa đảo siêu chuyên nghiệp không hối thúc, chủ động bảo đọc kỹ để dẫn chủ trang tự vượt qua 2 nấc xác nhận chính chủ & email chính báo đổi quyền) theo góc quan sát **`D/B`**, đồng thời lấp khoảng trống Lớp 3 về **ứng phó chặn vạ lây khi mất trang cá nhân**.
