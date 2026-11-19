# HỒ SƠ THẨM ĐỊNH (CLEARANCE) – EP10: Hai Mạng Wi-Fi Trùng Tên & Kết Mở Tiệm Đối Diện

> Gate 0 chỉ mở khi dòng dưới cùng ghi đúng `TRẠNG THÁI TỔNG: ĐẠT`.
> Đối chiếu [CONTENT_LEGAL_SAFETY_HARNESS.md](../../../../00_HARNESS_GUIDELINES/CONTENT_LEGAL_SAFETY_HARNESS.md).

| # | Rào cản | Câu hỏi kiểm tra | Kết quả | Ghi chú |
| :-: | :--- | :--- | :---: | :--- |
| 1 | Không định danh | Có tên/ảnh/giọng/SĐT/STK/biển số/địa chỉ/tên doanh nghiệp/app có thật nào không? | ☑ ĐẠT | Không nêu tên khách sạn, tiệm sửa điện thoại, sân bay, ngân hàng, nhà mạng hay ứng dụng cụ thể nào; không có URL, SĐT hay STK thật. |
| 2 | Không vu khống | Có ám chỉ một người, công ty, địa phương, cơ quan cụ thể đang lừa đảo không? | ☑ ĐẠT | Tình huống hư cấu điển hình với dàn nhân vật hình tượng cố định; cảnh kết mở (Tùng trả 200K, xa xa có người ôm điện thoại chạy từ khách sạn đối diện tới) **tuyệt đối không quy kết** tiệm sửa máy, để mở hoàn toàn cho người xem suy ngẫm. |
| 3 | Không dạy lừa | Chi tiết thủ đoạn có dừng ở mức nhận biết, không thành hướng dẫn? | ☑ ĐẠT | Chỉ cảnh báo dấu hiệu 2 mạng trùng tên không mật khẩu và trang web dụ bấm đồng ý cài gói kết nối (app chạy ngầm); không nêu tên phần cứng, tên file hay cách chế tạo mã độc. |
| 4 | Không giả mạo | Không logo, giao diện app, sắc phục, con dấu, giấy tờ, biểu trưng thật? | ☑ ĐẠT | Toàn bộ 9 khung hình dùng biểu tượng đồ họa trừu tượng (cột sóng, ổ khóa, cờ-lê, thẻ ngân hàng, tờ tiền màu đỏ nâu không chữ số), không logo, không giao diện thật. |
| 5 | Tôn trọng nạn nhân | Không chế giễu, không đổ lỗi “ngu nên bị lừa”? | ☑ ĐẠT | Khắc họa đúng tâm lý người bình thường: thấy 2 mạng trùng tên chọn miễn phí cho lẹ, thấy máy đơ thì bấm thử lại rồi hoảng hốt tắt nguồn chạy qua tiệm đối diện. |
| 6 | Không kỳ thị | Không gắn lừa đảo với vùng miền, dân tộc, quốc tịch, nghề nghiệp, giới tính? | ☑ ĐẠT | Không kỳ thị ngành sửa chữa điện thoại hay bất kỳ cộng đồng nào; không quy kết nghề nghiệp. |
| 7 | Khuyến nghị đúng | Lời khuyên ở thẻ dấu hiệu có đúng, an toàn, không gây hại nếu làm theo? | ☑ ĐẠT | Chuẩn thực tế cho người dùng phổ thông: thấy máy tự mở ngân hàng thì đè tắt nguồn ngay, không bật lại và đem ra tiệm kỹ thuật uy tín gỡ sạch; hỏi quầy đúng Wi-Fi thật; chuyển tiền dùng 4G/5G riêng. |
| 8 | Thuật toán | Đã quét từ cấm theo policy_wordlists.json (thoại, chữ, tiêu đề)? | ☑ ĐẠT | Sạch 100%: `0` từ `hard_block` và `0` từ `soft_warn`. |
| 9 | Nguồn cảm hứng (nội bộ) | Đã ghi nguồn cảm hứng vào `source/`? | ☑ ĐẠT | Xem `story.txt` và `source/SOURCE_NOTES.md`. |

**Người thẩm định:** Chủ kênh / Ban Biên Tập VCH  **Ngày:** 19/11/2026

**TRẠNG THÁI TỔNG: ĐẠT**
