# HARNESS KIỂM DUYỆT KỊCH BẢN & SẢN XUẤT (STORY & PRODUCTION HARNESS)

Bộ tiêu chí ngắn gọn, tổng quát dùng để kiểm tra bắt buộc cho **mọi tập phim mới** trước và trong khi dựng:

---

## I. HARNESS CỐT TRUYỆN & TÂM LÝ (STORYTELLING HARNESS)

1. **Độ mới & tính thực chiến:** Tình huống phải lấy từ chất liệu thực tế, không cũ kỹ, không lộ kết cục ngay từ 3 giây đầu và không mang tính giáo điều một chiều.
2. **Logic không gian, thời gian & quan hệ nhân vật tự nhiên (kể cả khi dùng ước lệ Short):**
   - Dùng ước lệ hình ảnh (chia khung hình lưới nhiều ô khi gọi hàng loạt, chia đôi màn hình cho hai phản ứng trái ngược ở hai nơi khác nhau) thay vì ép các nhân vật không liên quan đứng chung một chỗ phi lý.
   - Các nhân vật gặp nhau kể lại chuyện phải ở bối cảnh hợp lý tự nhiên (như cổng trường giờ đón con, quán nước quen...). Nếu hai nhân vật chỉ là phụ huynh/đồng nghiệp/hàng xóm tâm sự, an ủi nhau mà không đặt vấn đề quan hệ nam-nữ hay vợ-chồng, ưu tiên dùng hai nhân vật cùng giới (hai bà mẹ, hai người bạn) để tự nhiên, tránh gây hiểu lầm ngoài lề.
3. **Đúng bản chất hành vi & công cụ của kẻ lừa đảo:**
   - **Loại câu kéo 1-1 (phỏng vấn, đầu tư):** Nói nhiều, thả mồi lớn, hối thúc dồn dập và cáu gắt khi bị trì hoãn.
   - **Loại tung lưới hàng loạt (gọi báo cấp cứu, giả danh hàng loạt):** Gọi đồng loạt hàng chục người cùng một kịch bản dựa trên dữ liệu thu thập từ mạng xã hội (tên con, lớp, giấy khen...), kết hợp đòn tâm lý công nghệ cao (nhá video Deepfake giả cảnh con la khóc đau đớn) để đánh gục sự tỉnh táo.
4. **Sự nao núng thật, phân hóa phản ứng & kết cục có điểm tựa phòng vệ gốc:**
   - Đặt song song **người vì quá hoảng loạn trước đòn công nghệ cao đã lỡ chuyển tiền** bên cạnh **người kịp nhận ra dấu hiệu bất thường và gọi kiểm chứng xác thực**.
   - Kết thúc vừa có sự sẻ chia đời thường (*"con bình an không sao là may rồi"*), vừa xoáy thẳng vào **nguyên nhân gốc và nguyên tắc bất di bất dịch** (không đăng thông tin cá nhân/trường lớp của con lên mạng; chưa kiểm chứng xác thực thì tuyệt đối không chuyển tiền).
5. **Điểm bẻ lái / Ý nghĩ cứu cánh hợp lý (Saving Hook):** Khoảnh khắc thoát bẫy hoặc phát hiện sự thật phải xuất phát từ một chi tiết thực tế hợp lý, dẫn đến hành động kiểm chứng an toàn (không làm lố, không tự đi "bắt cướp" phi thực tế hoặc dễ bị tố ngược).
6. **Giải thích cơ chế bằng ẩn dụ bình dân:** Mọi thủ đoạn phức tạp phải được chuyển thành hình ảnh biểu tượng trực quan và lời thoại đời thường để khán giả phổ thông hiểu ngay trong 1 lần nghe.

---

## II. HARNESS KỸ THUẬT & KIỂM DUYỆT (TECHNICAL & QA HARNESS)

1. **Hình ảnh (`Gate 1`):** Chuẩn khung dọc `9:16`, ánh sáng đúng thời gian bối cảnh, nhân vật đồng nhất ngoại hình với `02_CAST/cast.json`, tuyệt đối không có chữ/số/logo/giao diện thật/máu me, dành trống 25% đáy khung hình cho phụ đề.
2. **Giọng đọc TTS (`Gate 2`):**
   - Bắt buộc dùng model đầy đủ (`gemini-3.8-flash-tts`), cấm dùng filter bẻ cao độ/tốc độ (`asetrate`, `atempo`).
   - Từ vựng trong lời thoại phải đồng nhất phương ngữ miền Nam với `style` của nhân vật để AI không bị lệch giọng giữa các câu.
   - Bắt buộc **nghe kiểm tra từng file `.mp3`** (đúng giọng, đúng cảm xúc, không bị cắt mất chữ cuối, vừa khít `window`) trước khi qua `Gate 3`.
3. **Nhịp dựng & Kỷ luật xuất bản (`Gate 3 → Gate 5`):**
   - Tổng từ thoại `≤ 115 từ / 56s`, mỗi câu vừa cửa sổ thời gian, có khoảng thở và điểm nhấn âm thanh ở cú lật (`34.0s`).
   - Luôn dừng ở **Staging (`Gate 5`)**, kiểm tra đủ 8 điểm QA và các khung hình `preview_frames` trước khi trình duyệt.
