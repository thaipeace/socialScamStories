# HỒ SƠ THẨM ĐỊNH (CLEARANCE 16:9 LONG-FORM) – EP27: Sau khoản nợ cuối cùng

> Gate 0 chỉ mở khi dòng dưới cùng ghi đúng `TRẠNG THÁI TỔNG: ĐẠT`.
> Đối chiếu [CONTENT_LEGAL_SAFETY_HARNESS.md](../../../../00_HARNESS_GUIDELINES/CONTENT_LEGAL_SAFETY_HARNESS.md).

| # | Rào cản | Câu hỏi kiểm tra | Kết quả | Ghi chú |
| :-: | :--- | :--- | :---: | :--- |
| 1 | Không định danh | Có tên/ảnh/giọng/SĐT/STK/biển số/địa chỉ/tên doanh nghiệp/app có thật nào không? | ☑ ĐẠT (nháp) | Tên Long, Hạnh là hư cấu, phổ biến. Không có tên ngân hàng hay app |
| 2 | Không vu khống | Có ám chỉ một người, công ty, địa phương cụ thể đang lừa đảo không? | ☑ ĐẠT (nháp) | Bối cảnh "hẻm, chợ, xưởng" chung chung |
| 3 | Không dạy lừa | Chi tiết thủ đoạn có dừng ở mức nhận biết cơ chế, không thành hướng dẫn thực hành? | ☑ ĐẠT (nháp) | Không mô tả cách lập giấy vay, tìm khách hay chia hoa hồng |
| 4 | Không giả mạo | Không logo, giao diện app, sắc phục, con dấu, giấy tờ thật? | ☑ ĐẠT | Đã soát 23 ảnh: giấy tờ và màn hình không đọc được chữ; cán bộ mặc thường phục; đã cắt viền đen; đã sửa c05, c07, c11, c20 cho đúng liên tục cảnh |
| 5 | Tôn trọng nạn nhân | Không chế giễu, không đổ lỗi "ngu nên bị lừa"? | ☑ ĐẠT (nháp) | Má vay vì lo Tết; Anh Hai tự nhận phần lỗi ở C7 |
| 6 | Không kỳ thị | Không gắn lừa đảo với vùng miền, dân tộc, quốc tịch, nghề nghiệp, giới tính? | ☑ ĐẠT (nháp) | Chủ nợ không mang hình tượng giang hồ rập khuôn |
| 7 | Khuyến nghị đúng | Lời khuyên ở thẻ dấu hiệu có đúng, an toàn, không gây hại nếu làm theo? | ☑ ĐẠT | Đã kiểm chứng ngày 16/11, xem mục "Kiểm chứng pháp lý" bên dưới |
| 8 | Thuật toán | Đã quét từ cấm theo policy_wordlists.json (thoại, chữ, tiêu đề)? | ☑ ĐẠT | Quét tự động ở Gate 5: PASS sạch từ cấm |
| 9 | Nguồn cảm hứng (nội bộ) | Đã ghi nguồn cảm hứng vào `source/`? | ☑ ĐẠT | `source/SOURCE.md` |

## Kiểm chứng pháp lý (16/11/2026)
| Câu | Nội dung | Căn cứ | Kết luận |
|---|---|---|---|
| `l41` | Khoản có giấy thì chốt số thực cầm, thu lại giấy gốc | Khoản 1 Điều 468 BLDS 2015; Nghị quyết 01/2019/NQ-HĐTP | ✔ Đúng. Đã lược gọn không giảng điều luật |
| `l42` | Tạm thời đưa Má đi xa ở với người thân, cắt số cũ tránh bị tìm gặp ép ký tiếp | Biện pháp bảo vệ thực tế | ✔ An toàn, hợp lý |
| `l53` | Gốc thực nhận trừ đã góp, cộng lãi hợp pháp, làm tròn lên | Hệ quả pháp lý; đề nghị thương lượng thiện chí | ✔ Hợp lý; làm tròn lên thể hiện không né nợ |
| `l55` | "Ra công an nhờ tính giùm" | Không khẳng định tội danh, không nêu ngưỡng hình sự | ✔ An toàn |
| Disclaimer | "Thông tin pháp lý chỉ mang tính tham khảo – hỏi trợ giúp pháp lý/luật sư" | – | ✔ Có |

**Người thẩm định:** Chủ kênh (đã duyệt Staging v4 lên Production)  **Ngày:** 16/11/2026

**TRẠNG THÁI TỔNG: ĐẠT**
