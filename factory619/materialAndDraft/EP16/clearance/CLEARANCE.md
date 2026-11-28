# HỒ SƠ THẨM ĐỊNH (CLEARANCE) – EP16: Bẫy Xây Kênh Kiếm Tiền Trên Trang Cá Nhân (V3 · Level 3)

> Gate 0 chỉ mở khi dòng dưới cùng ghi đúng `TRẠNG THÁI TỔNG: ĐẠT`.
> Đối chiếu [CONTENT_LEGAL_SAFETY_HARNESS.md](../../../../00_HARNESS_GUIDELINES/CONTENT_LEGAL_SAFETY_HARNESS.md).

| # | Rào cản | Câu hỏi kiểm tra | Kết quả | Ghi chú |
| :-: | :--- | :--- | :---: | :--- |
| 1 | Không định danh | Có tên/ảnh/giọng/SĐT/STK/biển số/địa chỉ/tên doanh nghiệp/app có thật nào không? | ☑ ĐẠT | Hư cấu hóa 100% bằng dàn hình tượng cố định (`Chị Ba`, `Anh Hai`, `Chị Tư`, `Kẻ lừa ngọt ngào`, `Kẻ giả danh`, `Người Bóc Trần`). Không tên nền tảng mạng xã hội, ngân hàng, nhãn hàng, SĐT, STK hay URL thật. |
| 2 | Không vu khống | Có ám chỉ một người, công ty, địa phương cụ thể đang lừa đảo không? | ☑ ĐẠT | Mô tả cơ chế chiêu thức giả danh đối tác chuyên nghiệp dẫn dụ thêm email và bấm xác nhận đổi quyền trên trang cá nhân; không ám chỉ cá nhân, nhãn hàng hay nền tảng cụ thể nào. |
| 3 | Không dạy lừa | Chi tiết thủ đoạn có dừng ở mức nhận biết, không thành hướng dẫn? | ☑ ĐẠT | Chỉ dừng ở bề mặt cảnh báo nạn nhân thấy trên máy mình (xác nhận mật khẩu chính chủ, hộp thư email chính báo đổi quyền quản trị) và cơ chế làm mềm phòng vệ bằng sự lịch sự; tuyệt đối không hướng dẫn kỹ thuật chiếm quyền hay vượt 2FA. |
| 4 | Không giả mạo | Không logo, giao diện app, sắc phục, con dấu, giấy tờ thật? | ☑ ĐẠT | Khóa prompt sạch 100% (`no text, no letters, no numbers, no logos, no brand names, no real app interface, no real uniforms or insignia`); sẽ kiểm duyệt thị giác đầy đủ tại Gate 1 & Gate 5 trước khi xuất Staging. |
| 5 | Tôn trọng nạn nhân | Không chế giễu, không đổ lỗi “ngu nên bị lừa”? | ☑ ĐẠT | Khắc họa trung thực vì sao cả người cẩn thận vẫn dễ hạ phòng vệ khi đối phương không hề hối thúc và giải thích nghe rất chuyên nghiệp, không chế giễu hay đổ lỗi. |
| 6 | Không kỳ thị | Không gắn lừa đảo với vùng miền, dân tộc, quốc tịch, nghề nghiệp? | ☑ ĐẠT | Kẻ gian chỉ xuất hiện qua giọng điện thoại và bóng tối ẩn danh, không gắn đặc điểm vùng miền hay cộng đồng cụ thể. |
| 7 | Khuyến nghị đúng & Chặn rủi ro `L8` | Lời khuyên ở thẻ dấu hiệu có đúng, an toàn, không xúi giục hành vi nguy hiểm? | ☑ ĐẠT | 100% khuyến nghị phổ quát, an toàn: tách riêng trang công việc và trang cá nhân, dùng email riêng + 2FA bằng ứng dụng, dừng tay ngay khi thấy email chính báo đổi quyền bất kể thái độ đối phương, không chuyển tiền chuộc, báo gấp người thân chặn vạ lây, lưu chứng cứ trình báo cơ quan công an; ghim cảnh báo tránh bẫy "dịch vụ lấy lại trang". |
| 8 | Thuật toán | Đã quét từ cấm theo `policy_wordlists.json` (thoại, chữ, tiêu đề)? | ☑ ĐẠT | Sạch 100%: `0` từ `identity_hard_block`, `0` từ `identity_soft_warn`, `0` từ `asr_ocr_hard_block`, `0` từ `asr_ocr_soft_warn`. |
| 9 | Nguồn cảm hứng (nội bộ) | Đã ghi nguồn cảm hứng vào `source/`? | ☑ ĐẠT | Xem `source/SOURCE_NOTES.md`. |

**Người thẩm định:** Ban Biên Tập VCH / Agent MaterialAndDraft  **Ngày:** 28/11/2026

**TRẠNG THÁI TỔNG: ĐẠT**
