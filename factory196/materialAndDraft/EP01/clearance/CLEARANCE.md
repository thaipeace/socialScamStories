# HỒ SƠ THẨM ĐỊNH (CLEARANCE 16:9 LONG-FORM) – EP01: Bẫy rút tiền và đáo hạn thẻ tín dụng qua máy POS khống

> Gate 0 chỉ mở khi dòng dưới cùng ghi đúng `TRẠNG THÁI TỔNG: ĐẠT`.
> Đối chiếu [CONTENT_LEGAL_SAFETY_HARNESS.md](../../../../00_HARNESS_GUIDELINES/CONTENT_LEGAL_SAFETY_HARNESS.md).

| # | Rào cản | Câu hỏi kiểm tra | Kết quả | Ghi chú |
| :-: | :--- | :--- | :---: | :--- |
| 1 | Không định danh | Có tên/ảnh/giọng/SĐT/STK/biển số/địa chỉ/tên doanh nghiệp/app có thật nào không? | ☑ ĐẠT | Hoàn toàn dùng danh từ chung ("ngân hàng", "máy POS", "cơ quan chức năng") |
| 2 | Không vu khống | Có ám chỉ một người, công ty, địa phương cụ thể đang lừa đảo không? | ☑ ĐẠT | Tình huống hư cấu hóa hoàn toàn với dàn nhân vật VCH |
| 3 | Không dạy lừa | Chi tiết thủ đoạn trong phim dài có dừng ở mức nhận biết cơ chế tâm lý, không thành hướng dẫn thực hành? | ☑ ĐẠT | Chỉ giải thích rủi ro lộ CVV/OTP và tính bất hợp pháp của giao dịch khống |
| 4 | Không giả mạo | Không logo, giao diện app, sắc phục, con dấu, giấy tờ thật? | ☑ ĐẠT | Prompt ảnh khóa cứng không chữ/số/logo/sắc phục |
| 5 | Tôn trọng nạn nhân | Không chế giễu, không đổ lỗi “ngu nên bị lừa”? | ☑ ĐẠT | Đồng cảm với áp lực tài chính của người lao động, hướng dẫn giải pháp đúng |
| 6 | Không kỳ thị | Không gắn lừa đảo với vùng miền, dân tộc, quốc tịch, nghề nghiệp, giới tính? | ☑ ĐẠT | Không kỳ thị bất kỳ nhóm nào |
| 7 | Khuyến nghị đúng | Lời khuyên ở thẻ dấu hiệu có đúng, an toàn, không gây hại nếu làm theo? | ☑ ĐẠT | Khuyến nghị làm việc trực tiếp với ngân hàng, bảo mật CVV/OTP |
| 8 | Thuật toán | Đã quét từ cấm theo policy_wordlists.json (thoại, chữ, tiêu đề)? | ☑ ĐẠT | Sạch 100% cả hard_block và soft_warn |
| 9 | Nguồn cảm hứng (nội bộ) | Đã ghi nguồn cảm hứng vào `source/` (không bắt buộc công bố)? | ☑ ĐẠT | Lấy cảm hứng từ cảnh báo báo chí về triệt phá nhóm quẹt máy POS khống |

**Người thẩm định:** Ban Biên Tập VCH  **Ngày:** 09/11/2026

**TRẠNG THÁI TỔNG: ĐẠT**
