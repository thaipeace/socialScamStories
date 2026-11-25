# HỒ SƠ THẨM ĐỊNH (CLEARANCE) – EP13: Tài Liệu Ôn Thi Miễn Phí (V1 · Level 3)

> Gate 0 chỉ mở khi dòng dưới cùng ghi đúng `TRẠNG THÁI TỔNG: ĐẠT`.
> Đối chiếu [CONTENT_LEGAL_SAFETY_HARNESS.md](../../../../00_HARNESS_GUIDELINES/CONTENT_LEGAL_SAFETY_HARNESS.md).

| # | Rào cản | Câu hỏi kiểm tra | Kết quả | Ghi chú |
| :-: | :--- | :--- | :---: | :--- |
| 1 | Không định danh | Có tên/ảnh/giọng/SĐT/STK/biển số/địa chỉ/tên doanh nghiệp/app có thật nào không? | ☑ ĐẠT | Hư cấu hóa 100% bằng dàn hình tượng cố định (`Bé Na`, `Chị Ba`, `Kẻ giấu mặt`, `Người Bóc Trần`). Loại bỏ hoàn toàn tên nạn nhân thật, địa danh, tên mạng xã hội, ngân hàng và đường link có thật. |
| 2 | Không vu khống | Có ám chỉ một người, công ty, địa phương cụ thể đang lừa đảo không? | ☑ ĐẠT | Mô tả thủ đoạn giả mạo tài liệu học tập phổ biến trên mạng, không chỉ đích danh bất kỳ cá nhân, trường học hay trang tài liệu hợp pháp nào. |
| 3 | Không dạy lừa | Chi tiết thủ đoạn có dừng ở mức nhận biết, không thành hướng dẫn? | ☑ ĐẠT | Chỉ mô tả dấu hiệu bề mặt (link miền lạ đòi đăng nhập mật khẩu mạng xã hội, tệp lạ ẩn mã độc) và cơ chế cảnh giác; không hướng dẫn tạo web phishing hay phát tán mã độc. |
| 4 | Không giả mạo | Không logo, giao diện app, sắc phục, con dấu, giấy tờ thật? | ☑ ĐẠT | Đã kiểm duyệt thị giác 100% toàn bộ bộ tài nguyên Gate 1 (12 ảnh nền/panel `s1..s10` + 3 ảnh `detail_reveal` + 4 lớp 2.5D `s2_bg/fg`, `s9_bg/fg` + 16 biến thể Living-Character kiểm qua `source/face_qc_sheet.jpg` + 26 khung Safe Zone `gate 4 --preview`): sạch chữ rác, không logo/UI app thật, không sắc phục/phù hiệu, không viền lỗi màu da. |
| 5 | Tôn trọng nạn nhân | Không chế giễu, không đổ lỗi “ngu nên bị lừa”? | ☑ ĐẠT | Thể hiện sự đồng cảm với áp lực sát giờ thi của sinh viên; không cười cợt hay đổ lỗi nạn nhân. |
| 6 | Không kỳ thị | Không gắn lừa đảo với vùng miền, dân tộc, quốc tịch, nghề nghiệp? | ☑ ĐẠT | Kẻ gian chỉ hiện bóng ngược sáng trong phòng tối, không mang đặc điểm nhận dạng cộng đồng hay vùng miền. |
| 7 | Khuyến nghị đúng & Chặn rủi ro `L8` | Lời khuyên ở thẻ dấu hiệu có đúng, an toàn, không xúi giục hành vi nguy hiểm? | ☑ ĐẠT | Khuyến nghị 100% phổ quát và bám sát cảnh báo chính thức: không nhập mật khẩu vào link lạ, bật 2FA, báo ngay người thân, không chuyển tiền khi bị uy hiếp, lưu bằng chứng trình báo cơ quan công an. |
| 8 | Thuật toán | Đã quét từ cấm theo `policy_wordlists.json` (thoại, chữ, tiêu đề)? | ☑ ĐẠT | Sạch 100%: `0` từ `identity_hard_block`, `0` từ `identity_soft_warn`, `0` từ `asr_ocr_hard_block`, `0` từ `asr_ocr_soft_warn`. |
| 9 | Nguồn cảm hứng (nội bộ) | Đã ghi nguồn cảm hứng vào `source/`? | ☑ ĐẠT | Xem `source/SOURCE_NOTES.md` (VTV24 `2zs3HPL_k6w`). |

**Người thẩm định:** Ban Biên Tập VCH / Agent MaterialAndDraft  **Ngày:** 25/11/2026

**TRẠNG THÁI TỔNG: ĐẠT**
