# HỒ SƠ THẨM ĐỊNH (CLEARANCE) – EP15: Bẫy App Ngân Hàng Giả Tại Quầy (V2 · Level 3)

> Gate 0 chỉ mở khi dòng dưới cùng ghi đúng `TRẠNG THÁI TỔNG: ĐẠT`.
> Đối chiếu [CONTENT_LEGAL_SAFETY_HARNESS.md](../../../../00_HARNESS_GUIDELINES/CONTENT_LEGAL_SAFETY_HARNESS.md).

| # | Rào cản | Câu hỏi kiểm tra | Kết quả | Ghi chú |
| :-: | :--- | :--- | :---: | :--- |
| 1 | Không định danh | Có tên/ảnh/giọng/SĐT/STK/biển số/địa chỉ/tên doanh nghiệp/app có thật nào không? | ☑ ĐẠT | Hư cấu hóa 100% bằng dàn hình tượng cố định (`Cô Tư`, `Bé Na`, `Khách nam / Kẻ lừa ngọt ngào`, `Người Bóc Trần`). Loại bỏ hoàn toàn tên ngân hàng, ví điện tử, chợ, SĐT và STK thật. |
| 2 | Không vu khống | Có ám chỉ một người, công ty, địa phương cụ thể đang lừa đảo không? | ☑ ĐẠT | Mô tả biến thể lừa đảo bằng ứng dụng ngân hàng giả mạo tại quầy bán hàng được VTV24 cảnh báo rộng rãi; không ám chỉ cá nhân, tổ chức hay địa phương cụ thể nào. |
| 3 | Không dạy lừa | Chi tiết thủ đoạn có dừng ở mức nhận biết, không thành hướng dẫn? | ☑ ĐẠT | Chỉ dừng ở bề mặt nạn nhân thấy tại quầy (màn hình dấu tích xanh trên tay khách + đòn kì kèo “sợ trả hai lần”); tuyệt đối không mô tả nơi tìm/mua app giả, không hướng dẫn nhập trường giả lập hay kỹ thuật tạo app. |
| 4 | Không giả mạo | Không logo, giao diện app, sắc phục, con dấu, giấy tờ thật? | ☑ ĐẠT | Khóa prompt sạch 100% (`no text, no letters, no numbers, no logos, no brand names, no real bank app interface, no real uniforms or insignia`); mọi ảnh nền, 2.5D, `detail_reveal` và Living-Character được kiểm duyệt thị giác qua `face_qc_sheet.jpg` và `preview_frames` trước Gate 5. |
| 5 | Tôn trọng nạn nhân | Không chế giễu, không đổ lỗi “ngu nên bị lừa”? | ☑ ĐẠT | Đặt người trẻ rành điện thoại (`Bé Na`) vào tình huống suýt tin và nao núng thật trước lý lẽ “trả hai lần” để phản ánh đúng áp lực thực tế của người bán hàng, không chế giễu hay đổ lỗi. |
| 6 | Không kỳ thị | Không gắn lừa đảo với vùng miền, dân tộc, quốc tịch, nghề nghiệp? | ☑ ĐẠT | Kẻ gian ăn mặc lịch sự như người bình thường, không gắn đặc điểm vùng miền hay cộng đồng cụ thể. |
| 7 | Khuyến nghị đúng & Chặn rủi ro `L8` | Lời khuyên ở thẻ dấu hiệu có đúng, an toàn, không xúi giục hành vi nguy hiểm? | ☑ ĐẠT | 100% khuyến nghị phổ quát theo cảnh báo chính thức của VTV24: nguyên tắc “Kiểm trước, tin sau” — chỉ giao hàng khi tiền đã nổi trên chính app ngân hàng hoặc loa báo số dư của mình; khách vội có thể trả tiền mặt kèm giấy ký nhận hoàn lại khi tiền về. |
| 8 | Thuật toán | Đã quét từ cấm theo `policy_wordlists.json` (thoại, chữ, tiêu đề)? | ☑ ĐẠT | Sạch 100%: `0` từ `identity_hard_block`, `0` từ `identity_soft_warn`, `0` từ `asr_ocr_hard_block`, `0` từ `asr_ocr_soft_warn`. |
| 9 | Nguồn cảm hứng (nội bộ) | Đã ghi nguồn cảm hứng vào `source/`? | ☑ ĐẠT | Xem `source/SOURCE_NOTES.md`. |

**Người thẩm định:** Ban Biên Tập VCH / Agent MaterialAndDraft  **Ngày:** 27/11/2026

**TRẠNG THÁI TỔNG: ĐẠT**
