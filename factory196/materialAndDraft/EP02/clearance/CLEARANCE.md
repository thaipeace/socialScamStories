# HỒ SƠ THẨM ĐỊNH (CLEARANCE 16:9 LONG-FORM) – EP02: Chữ ma – 80 triệu và một cú click

> Gate 0 chỉ mở khi dòng dưới cùng ghi đúng `TRẠNG THÁI TỔNG: ĐẠT`.
> Đối chiếu [CONTENT_LEGAL_SAFETY_HARNESS.md](../../../../00_HARNESS_GUIDELINES/CONTENT_LEGAL_SAFETY_HARNESS.md).

| # | Rào cản | Câu hỏi kiểm tra | Kết quả | Ghi chú |
| :-: | :--- | :--- | :---: | :--- |
| 1 | Không định danh | Có tên/ảnh/giọng/SĐT/STK/biển số/địa chỉ/tên doanh nghiệp/app có thật nào không? | ☑ ĐẠT | "Ngân hàng X" hư cấu. Tên miền chỉ hiện phần tên `nganhangx` / `nganhаngx` **không kèm đuôi** (.com/.vn) → không trỏ tới tên miền có thật, không vướng bộ lọc URL Gate 5. Số TK chỉ hiện `…8826`. Ảnh không chữ/logo. |
| 2 | Không vu khống | Có ám chỉ một người, công ty, địa phương cụ thể đang lừa đảo không? | ☑ ĐẠT | Kẻ gian không lộ mặt, không gắn vùng miền; ngân hàng hư cấu. |
| 3 | Không dạy lừa | Chi tiết thủ đoạn có dừng ở mức nhận biết, không thành hướng dẫn thực hành? | ☑ ĐẠT | Chỉ nêu nguyên lý ký tự giống nhau (a/а, rn/m) – kiến thức phòng vệ phổ biến. **Không** mô tả cách đăng ký tên miền, cách dựng web giả, cách vượt PAD/sinh trắc học; bỏ tiêu đề mang sắc thái "Cách kẻ gian chuyển đi...". |
| 4 | Không giả mạo | Không logo, giao diện app, sắc phục, con dấu, giấy tờ thật? | ☑ ĐẠT | Màn hình điện thoại chỉ là khối màu trừu tượng; thẻ ngân hàng trơn; chữ do engine chèn. |
| 5 | Tôn trọng nạn nhân | Không chế giễu, không đổ lỗi? | ☑ ĐẠT | Minh bị lừa vì áp lực thời gian và tiền tạm ứng ca mổ theo lịch của mẹ, không bị mô tả là cả tin/ngu. Kết phim hướng tới bảo vệ người thân. |
| 6 | Không kỳ thị | Không gắn lừa đảo với vùng miền, dân tộc, quốc tịch, nghề nghiệp, giới tính? | ☑ ĐẠT | Đã bỏ hẳn việc nhắc tên quốc gia khi giải thích hệ chữ Kirin; 0% yếu tố vùng miền hay quốc tịch. |
| 7 | Khuyến nghị đúng | Lời khuyên có đúng, an toàn? | ☑ ĐẠT | Khớp thực tế Thông tư 50/2024/TT-NHNN: (1) đăng nhập máy lạ hay chuyển tiền vượt hạn mức cài đặt (>5tr/>10tr/tùy cài đặt) đều vướng sinh trắc học – không đóng đinh số tiền dễ lỗi thời; (2) kể cả SMS hiện đúng tên ngân hàng cũng không bấm link; (3) giữ nguyên tin nhắn/cuộc gọi, trình báo công an ngay (không đợi sáng mai), không hứa hẹn thu hồi được tiền. |
| 8 | Thuật toán | Đã quét từ cấm theo policy_wordlists.json? | ☑ ĐẠT | 0 từ cấm cứng; đã gỡ tên ứng dụng nhắn tin khỏi thẻ cảnh báo. Chỉ còn 1 WARN mềm danh từ chung `"bệnh viện"` (không nêu tên cơ sở y tế), chờ chủ kênh ký `--point 1`. |
| 9 | Nguồn cảm hứng (nội bộ) | Đã ghi nguồn cảm hứng vào `source/`? | ☑ ĐẠT | Xem `source/SOURCE.md`. |

**Người thẩm định:** Chủ kênh / Ban Biên Tập VCH  **Ngày:** 12/11/2026

**TRẠNG THÁI TỔNG: ĐẠT**
