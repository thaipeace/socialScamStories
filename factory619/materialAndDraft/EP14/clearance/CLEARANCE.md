# HỒ SƠ THẨM ĐỊNH (CLEARANCE) – EP14: Bẫy Bảo Hành Máy Lạnh Giả (V1 · Level 3)

> Gate 0 chỉ mở khi dòng dưới cùng ghi đúng `TRẠNG THÁI TỔNG: ĐẠT`.
> Đối chiếu [CONTENT_LEGAL_SAFETY_HARNESS.md](../../../../00_HARNESS_GUIDELINES/CONTENT_LEGAL_SAFETY_HARNESS.md).

| # | Rào cản | Câu hỏi kiểm tra | Kết quả | Ghi chú |
| :-: | :--- | :--- | :---: | :--- |
| 1 | Không định danh | Có tên/ảnh/giọng/SĐT/STK/biển số/địa chỉ/tên doanh nghiệp/app có thật nào không? | ☑ ĐẠT | Hư cấu hóa 100% bằng dàn hình tượng cố định (`Anh Hai`, `Chị Hai`, `Kẻ giả danh`, `Người Bóc Trần`). Loại bỏ hoàn toàn tên hãng máy lạnh, tên siêu thị điện máy, tên công cụ tìm kiếm, SĐT và địa chỉ thật. |
| 2 | Không vu khống | Có ám chỉ một người, công ty, địa phương cụ thể đang lừa đảo không? | ☑ ĐẠT | Mô tả thủ đoạn giả mạo trung tâm bảo hành điện máy mua vị trí đứng đầu kết quả tìm kiếm phổ biến ngoài thực tế; không ám chỉ cá nhân, cửa hàng hay doanh nghiệp cụ thể nào. |
| 3 | Không dạy lừa | Chi tiết thủ đoạn có dừng ở mức nhận biết, không thành hướng dẫn? | ☑ ĐẠT | Chỉ mô tả bề mặt nạn nhân gặp phải (kết quả đầu gắn nhãn quảng cáo, thợ không đồng phục/thẻ, biên nhận viết tay không tên công ty, cầm bo mạch ép giá); không hướng dẫn cách chạy quảng cáo giả hay kỹ thuật phá hỏng thiết bị. |
| 4 | Không giả mạo | Không logo, giao diện app, sắc phục, con dấu, giấy tờ thật? | ☑ ĐẠT | Khóa prompt sạch 100% (`no text, no letters, no numbers, no logos, no brand names, no real app interface, no real uniforms or insignia`); mọi ảnh nền, 2.5D, `detail_reveal` và Living-Character sẽ được kiểm duyệt thị giác qua `face_qc_sheet.jpg` và `preview_frames` trước Gate 5. |
| 5 | Tôn trọng nạn nhân | Không chế giễu, không đổ lỗi “ngu nên bị lừa”? | ☑ ĐẠT | Khắc họa chân thực sự tin tưởng và tâm lý cả nể bình thường của vợ chồng trẻ lần đầu gọi bảo hành, không chế giễu hay đổ lỗi. |
| 6 | Không kỳ thị | Không gắn lừa đảo với vùng miền, dân tộc, quốc tịch, nghề nghiệp? | ☑ ĐẠT | Đặt song song kẻ giả mạo bảo hành với kỹ thuật viên chính hãng tận tâm xử lý đúng lỗi; không vơ đũa nghề sửa chữa hay gắn đặc điểm vùng miền. |
| 7 | Khuyến nghị đúng & Chặn rủi ro `L8` | Lời khuyên ở thẻ dấu hiệu có đúng, an toàn, không xúi giục hành vi nguy hiểm? | ☑ ĐẠT | 100% khuyến nghị phổ quát an toàn: chỉ gọi số tổng đài in trên phiếu bảo hành/hóa đơn/tem máy; kiểm tra đồng phục/thẻ/tin nhắn lịch hẹn từ hãng; không giao linh kiện theo biên nhận viết tay không tên công ty. |
| 8 | Thuật toán | Đã quét từ cấm theo `policy_wordlists.json` (thoại, chữ, tiêu đề)? | ☑ ĐẠT | Sạch 100%: `0` từ `identity_hard_block`, `0` từ `identity_soft_warn`, `0` từ `asr_ocr_hard_block`, `0` từ `asr_ocr_soft_warn`. |
| 9 | Nguồn cảm hứng (nội bộ) | Đã ghi nguồn cảm hứng vào `source/`? | ☑ ĐẠT | Xem `source/SOURCE_NOTES.md`. |

**Người thẩm định:** Ban Biên Tập VCH / Agent MaterialAndDraft  **Ngày:** 25/11/2026

**TRẠNG THÁI TỔNG: ĐẠT**
