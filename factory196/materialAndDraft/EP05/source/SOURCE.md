# NGUỒN CẢM HỨNG & HỒ SƠ CHUYỂN HÓA KỊCH BẢN (NỘI BỘ) – 196 EP05

## 1. Chất liệu thực tế tham khảo
- **Cảnh báo tuyên truyền thực tế:** Video cảnh báo phòng chống tội phạm công nghệ cao trên mạng xã hội (Facebook Reel `1403473041900815` – tháng 10/2026) cùng chuỗi cảnh báo của cơ quan chức năng về thủ đoạn **lợi dụng lòng tốt ngoài đời thực để thu thập dữ liệu khuôn mặt/giọng nói** kết hợp **bẫy "giải ngân mồi" của tín dụng đen trực tuyến**.
- **Phản biện nghiệp vụ tài chính & pháp lý 2026 trước khi xây dựng kịch bản (`LONG_FORMAT_196_SPEC.md` – Nguyên tắc 5):**
  1. **Không hù dọa sai cơ chế ngân hàng chính thống:** Theo quy định hiện hành của Ngân hàng Nhà nước (xác thực sinh trắc học đối chiếu dữ liệu Căn cước gắn chip qua NFC), kẻ gian **không thể** chỉ quay lén gương mặt một người đi đường bất kỳ mà tự mở được tài khoản hay khoản vay tại ngân hàng chính thống (vốn không biết họ tên, số căn cước và không có thẻ chip vật lý để quét NFC).
  2. **Khớp nối thành dây chuyền 2 chốt sát thực tế 100%:**
     - **Chốt 1 (Lấy thông tin định danh tĩnh):** Quầy tặng quà nhỏ miễn phí (bình nước cho trẻ em) xin chụp 2 mặt thẻ căn cước + số điện thoại để "xác nhận mỗi người một phần quà". Nạn nhân chủ quan vì nghĩ *"chỉ là tấm hình chụp, giờ giao dịch đều phải quét mặt sống"*. Chính **chiếc hộp quà màu cam** trở thành dấu hiệu nhận diện mục tiêu vừa lộ căn cước.
     - **Chốt 2 (Lấy số tài khoản + 6 giây khuôn mặt sống & giọng nói):** Cách đó vài chục mét ở bãi xe, đồng bọn đóng vai phụ nữ trung niên mắt mờ, **đưa tờ 500.000đ tiền mặt thật trước** nhờ chuyển khoản hộ (thu được họ tên + số tài khoản thật và làm nạn nhân tắt hẳn cảnh giác), sau đó nhờ cầm điện thoại ngang mặt đọc dòng chữ xác nhận để bấm thoát màn hình đơ (thu trọn 6 giây khuôn mặt nhìn thẳng + giọng nói khớp khẩu hình).
  3. **Bản chất hậu quả & bẫy tâm lý kép:** Kẻ gian chuyển `3.500.000 VND` tiền "giải ngân mồi" vào tài khoản nạn nhân rồi tung ảnh căn cước kèm clip 6 giây quay lén ra đòi `6.000.000 VND`, đánh vào nỗi sợ mất danh dự tại nơi làm việc để ép nạn nhân tự bù tiền túi "trả cho êm chuyện".

## 2. Bảng hư cấu hóa 100% (Tuân thủ 5 Nguyên tắc vàng `CONTENT_LEGAL_SAFETY_HARNESS.md`)
| Chi tiết đời thực (KHÔNG ĐƯA VÀO PHIM) | Chi tiết hư cấu hóa trên phim (`196 EP05`) | Lý do an toàn pháp lý |
| :--- | :--- | :--- |
| Tên cán bộ, trang cá nhân hoặc vụ việc cụ thể | Gia đình hư cấu **Anh Hai – Chị Hai – Bé Tom** và nhân vật **Cô Lành** (`co_hanh`) | Tuân thủ Nguyên tắc 1 – Không định danh người thật |
| Tên ngân hàng, ví điện tử, ứng dụng vay, cửa hàng | **“Ngân hàng X”**, **“TK …9104”**, nhà sách & xưởng làm việc chung chung | Sạch 100% `identity_hard_block` & `ACCOUNT_RE` |
| Tên nền tảng nhắn tin / đơn vị công an địa phương | **“Nhóm tin nhắn”**, **“Cơ quan công an”** | Sạch 100% `identity_soft_warn` |
| Thao tác phần mềm quay ngầm / ghép AI / làm hồ sơ | Chỉ hiển thị 2 bong bóng tin nhắn trung tính ở cảnh câm `s06` | Tuân thủ Nguyên tắc 3 – Không dạy lừa |

## 3. Trạng thái hồ sơ
- **Giai đoạn hiện tại:** Hồ sơ Tầng 1 (`factory196/materialAndDraft/EP05`) đã hoàn chỉnh kịch bản, `source/build_draft.py`, `episode.json`, `IMAGE_PROMPTS.md`, `clearance/CLEARANCE.md` — sẵn sàng sinh bộ ảnh `16:9` (`assets/c00.jpg..c11.jpg`), thu TTS Gate 2 và căn lại timeline theo WAV thật.
