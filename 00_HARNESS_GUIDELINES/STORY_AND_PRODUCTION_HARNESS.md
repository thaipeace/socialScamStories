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
5. **Điểm bẻ lái / Ý nghĩ cứu cánh hợp lý (Saving Hook):** Khoảnh khắc thoát bẫy hoặc phát hiện sự thật phải xuất phát từ một chi tiết thực tế hợp lý, dẫn đến hành động kiểm chứng an toàn (không làm lố, không tự đi "bắt cướp" phi thực tế, không dùng việc dọa báo công an làm đòn mặc cả khi bản thân nhân vật cũng vi phạm).
6. **Giải thích cơ chế bằng ẩn dụ bình dân & tỷ lệ 80/20 cho phim dài (`factory196`):**
   - Mọi thủ đoạn phức tạp phải chuyển thành hình ảnh trực quan và lời thoại đời thường, ngắn gọn, không giảng bài nghiệp vụ.
   - Với **phim dài 16:9 (`4 – 5+ phút`, `≥ 240s`)**: giữ **`~80%` thời lượng cho câu chuyện đời thực của 1 nhân vật trung tâm** (đầu tư chiều sâu đời tư, tính cách, sĩ diện, hoàn cảnh gia đình) và **`~20%` cho sơ đồ minh họa + đúc kết của Người Bóc Trần ở cuối phim**. Không cưỡng ép tình tiết "lừa giật một lần" vào tiệm quen có địa chỉ cố định; phải phản biện đa chiều cả logic đời sống lẫn độ chính xác pháp lý/tài chính trước khi dựng.

---

## II. HARNESS KỸ THUẬT & KIỂM DUYỆT (TECHNICAL & QA HARNESS)

1. **Hình ảnh (`Gate 1`) & Khớp chuyển cảnh:**
   - Chuẩn khung dọc `9:16` (`factory619`) hoặc khung ngang `16:9` không viền đen letterbox (`factory196`), nhân vật đồng nhất ngoại hình, tuyệt đối không có chữ/số/logo/giao diện thật/máu me.
   - **Cảnh phải lên hình trước tiếng (`0.25–0.4s`):** Khi đổi bối cảnh sang nhân vật mới, cảnh mới phải cắt vào trước khi giọng nhân vật đó cất lên, tránh tiếng đi trước hình.
2. **Giọng đọc TTS (`Gate 2`) & Phân tách âm sắc:**
   - Bắt buộc dùng model đầy đủ (`gemini-3.8-flash-tts`), cấm dùng filter bẻ cao độ/tốc độ (`asetrate`, `atempo`).
   - **Phân biệt rõ giọng nhân vật cùng giới:** Khi có 2–3 nhân vật nam (hoặc nữ) trong cùng tập, phải chọn `voice` và `style` khác hẳn nhau về độ trầm/sáng và tốc độ nói để nghe phân biệt được ngay.
   - Từ vựng trong lời thoại phải đồng nhất phương ngữ miền Nam; câu thoại gọn, súc tích (`≤ 26 từ/câu`, mật độ phim dài `~120–140 từ/phút`).
   - Bắt buộc **nghe kiểm tra từng file `.mp3`** và dàn lại timeline theo thời lượng WAV thực tế sau `Gate 2`.
3. **Nhịp dựng & Kỷ luật xuất bản (`Gate 3 → Gate 5`):**
   - Short `9:16`: `≤ 115 từ / 56s`. Phim dài `16:9`: linh hoạt **`4 – 5+ phút` (`240s – 330s`)**, không kéo dài câu chữ lê thê cho đủ phút.
   - Luôn dừng ở **Staging (`Gate 5`)**, kiểm tra đủ 8 điểm QA và các khung hình `preview_frames`, chờ chủ kênh duyệt mới chạy `Gate 6`.
