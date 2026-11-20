# HỒ SƠ THẨM ĐỊNH (CLEARANCE 16:9 LONG-FORM) – EP06: Ba triệu tám trên màn hình *(v2-draft)*

> Gate 0 chỉ mở khi dòng dưới cùng ghi đúng `TRẠNG THÁI TỔNG: ĐẠT` và đã bổ sung đủ 14 ảnh `assets/c00.jpg … c12.jpg` (kèm `c03b.jpg`).
> Đối chiếu [CONTENT_LEGAL_SAFETY_HARNESS.md](../../../../00_HARNESS_GUIDELINES/CONTENT_LEGAL_SAFETY_HARNESS.md).

| # | Rào cản | Câu hỏi kiểm tra | Kết quả | Ghi chú |
| :-: | :--- | :--- | :---: | :--- |
| 1 | Không định danh | Có tên/ảnh/giọng/SĐT/STK/biển số/địa chỉ/tên doanh nghiệp/tên miền thật nào không? | ☑ ĐẠT | Hư cấu 100%: vợ chồng *Nam – Thảo*, thành viên nhóm hư cấu (*Chị Loan, Tuấn, Hoa, Minh*), *Người bạn cũ giấu mặt*, `TK …6821` (4 số cuối), không hiển thị bất kỳ chuỗi URL/tên miền thật nào. |
| 2 | Không vu khống | Có ám chỉ một người, sàn thương mại điện tử hay công ty cụ thể đang lừa đảo không? | ☑ ĐẠT | Dùng tên ứng dụng hư cấu *Bạn Thân 4.0* / *Nhóm Bạn Thân 4.0*, không nhắc hay mô phỏng màu sắc/giao diện bất kỳ sàn TMĐT, app mua hộ hay ngân hàng thật nào. |
| 3 | Không dạy lừa | Chi tiết thủ đoạn trong phim dài có dừng ở mức nhận biết cơ chế tâm lý, không thành hướng dẫn thực hành? | ☑ ĐẠT | Không mô tả cách dựng trang web giả, không nêu công cụ tạo cổng thanh toán hay mã nguồn; chỉ bóc trần cơ chế tâm lý nhóm chat chim mồi, "bù phần thiếu" và kiểm chứng tuổi tên miền cơ bản. |
| 4 | Không giả mạo | Không logo, giao diện app, sắc phục, con dấu, giấy tờ thật? | ☑ ĐẠT | Toàn bộ 14 prompt ảnh khóa cứng không chữ, không số, không URL, không logo; màn hình điện thoại & vi tính chỉ hiển thị bố cục trừu tượng, mọi nhãn chữ (kể cả danh sách và nút `[ CHỐT KHÁCH ]`) đều do engine ghép sạch. |
| 5 | Tôn trọng nạn nhân | Không chế giễu, không đổ lỗi “ngu nên bị lừa”? | ☑ ĐẠT | Nam tin làm tiếp vì lý do mua hàng giùm người bận có vẻ hợp lý, được cả nhóm chat cổ vũ và muốn bù ca mưa lo học phí cho con; anh kịp dừng ở mức 2,14 triệu và được vợ đồng hành ấm áp, không trách móc. |
| 6 | Không kỳ thị | Không gắn lừa đảo với vùng miền, dân tộc, quốc tịch, nghề nghiệp, giới tính? | ☑ ĐẠT | Hoàn toàn trung tính, không gắn đặc điểm vùng miền hay nghề nghiệp nhạy cảm. |
| 7 | Khuyến nghị đúng | Lời khuyên ở thẻ dấu hiệu có đúng, an toàn, không gây hại nếu làm theo? | ☑ ĐẠT | Hướng dẫn chuẩn xác: việc làm thật không thu tiền trước; cảnh giác nhóm chat cảm ơn rối rít (chim mồi); cắt lỗ ngay khi bị đòi nạp bù; tuyệt đối không thuê "dịch vụ lấy lại tiền treo"; lưu sao kê và đường dẫn trình báo cơ quan công an. |
| 8 | Thuật toán | Đã quét từ cấm theo `policy_wordlists.json` (thoại, chữ, tiêu đề)? | ☑ ĐẠT | Đã chạy quét tự động trên `episode.json` (`v2-draft`): 0 `identity_hard_block` · 0 `identity_soft_warn` · 0 `asr_ocr_hard_block` · 0 `asr_ocr_soft_warn` · 0 `PHONE_RE` / `URL_RE` / `ACCOUNT_RE`. |
| 9 | Nguồn cảm hứng (nội bộ) | Đã ghi nguồn cảm hứng vào `source/` (không bắt buộc công bố)? | ☑ ĐẠT | Đã lập và cập nhật đầy đủ tại `source/SOURCE.md` đối chiếu trực tiếp từ `story.txt` và ghi chú nâng cấp `v2-draft`. |

**Người thẩm định (Bản nháp Tầng 1 – v2):** Ban Biên Tập VCH  **Ngày:** 19/11/2026

**TRẠNG THÁI TỔNG: ĐẠT**
