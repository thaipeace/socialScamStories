# HỒ SƠ THẨM ĐỊNH (CLEARANCE 16:9 LONG-FORM) – EP10: Giám đốc 100 Agent – Suất cuối giảm 80%

> Gate 0 chỉ mở khi dòng dưới cùng ghi đúng `TRẠNG THÁI TỔNG: ĐẠT` và đã bổ sung đủ ảnh `assets/c00.jpg … c17.jpg` cùng các file lớp 2.5D, `detail_reveal` và Living-Character A/B/C.
> Đối chiếu [CONTENT_LEGAL_SAFETY_HARNESS.md](../../../../00_HARNESS_GUIDELINES/CONTENT_LEGAL_SAFETY_HARNESS.md) và [VIGILANCE_LIBRARY_FRAMEWORK.md](../../../../00_HARNESS_GUIDELINES/VIGILANCE_LIBRARY_FRAMEWORK.md).

| # | Rào cản | Câu hỏi kiểm tra | Kết quả | Ghi chú |
| :-: | :--- | :--- | :---: | :--- |
| 1 | Không định danh | Có tên/ảnh/giọng/SĐT/STK/biển số/địa chỉ/tên doanh nghiệp/tên miền thật nào không? | ☑ ĐẠT | Hư cấu 100%: **Tuấn – Hương – Thầy Quang – Trợ lý Khánh – Chị Lan – MC Hội trường – Chú Bảo Vệ – Chị Hai**; thang giá hư cấu hoàn toàn (`300tr → 60tr`, không dùng `1,5 tỷ → 300tr`); không hiển thị hay đọc bất kỳ SĐT, STK, biển số xe, URL, tên doanh nghiệp hay công cụ AI thật nào. |
| 2 | Không vu khống | Có ám chỉ một cá nhân, diễn giả, khóa học, nền tảng AI hay ngân hàng cụ thể nào không? | ☑ ĐẠT | Không nêu bất kỳ tên cá nhân, tổ chức, học viện hay công cụ AI có thương hiệu; chỉ mô tả chung *hội nghị công nghệ*, *nhóm kín VIP*, *ứng dụng văn phòng ảo*, *ngân hàng*. Khẳng định rõ AI chân chính là công cụ hỗ trợ làm việc thật (`s02`, `s14`). |
| 3 | Không dạy lừa | Chi tiết thủ đoạn trong phim dài có dừng ở mức nhận biết cơ chế, không thành hướng dẫn thực hành (`L2`)? | ☑ ĐẠT | Tuyệt đối không hướng dẫn cách lập trình ứng dụng hoạt ảnh giả, dựng kịch bản hội thảo hay tuyển chim mồi; chỉ bóc rõ cơ chế FOMO, neo giá giảm 80%, lãi mồi 3 triệu và cách kiểm chứng thực chiến (câu hỏi *"bán hàng gì, cho ai?"* + thử ngắt mạng). |
| 4 | Không giả mạo | Không logo, giao diện app, sắc phục, con dấu, giấy tờ thật? | ☑ ĐẠT | Toàn bộ prompt ảnh khóa cứng không chữ, không số, không biển số xe, không logo siêu xe/ngân hàng/ứng dụng thật; Chú Bảo Vệ mặc áo xanh nhạt trơn không phù hiệu không mũ; Chị Hai giấu mặt 100%; màn hình chỉ hiện khối đồ họa trừu tượng không chữ/số đọc được. |
| 5 | Tôn trọng nạn nhân | Không chế giễu, không đổ lỗi “ngu nên bị lừa”? | ☑ ĐẠT | Tuấn là tiểu thương chăm chỉ đang lo lắng bị bỏ lại trước biến động công nghệ nên rơi vào bẫy tâm lý được dàn dựng công phu; Hương đồng hành thực tế cùng chồng cắt lỗ, cảnh báo nhóm học viên khác và làm lại từ công việc thật. |
| 6 | Không kỳ thị | Không gắn lừa đảo với vùng miền, dân tộc, quốc tịch, nghề nghiệp, giới tính? | ☑ ĐẠT | Không gán định kiến cho bất kỳ nhóm nghề nghiệp, vùng miền hay cộng đồng nào; các nhân vật thao túng đều lịch sự đời thường để phản ánh đúng tính khó nhận diện của chiêu trò. |
| 7 | Khuyến nghị đúng | Lời khuyên ở thẻ dấu hiệu và lời thoại ứng phó có đúng, an toàn, chuẩn xác pháp lý (`L8`)? | ☑ ĐẠT | Chuẩn xác, an toàn: hỏi rõ nguồn tạo giá trị (*"bán hàng gì, cho ai?"*) và kiểm chứng pháp nhân trước khi xuống tiền; dừng cắt lỗ ngay không nạp phí mở cổng; cảnh giác bẫy lừa lần hai *"hỗ trợ lấy lại tiền"*; gom sao kê, biên nhận trình báo cơ quan công an. |
| 8 | Thuật toán | Đã quét từ cấm theo `policy_wordlists.json` (thoại, chữ, tiêu đề, mô tả, bình luận ghim)? | ☑ ĐẠT | 0 `identity_hard_block` · 0 `identity_soft_warn` · 0 `asr_ocr_hard_block` · 0 `asr_ocr_soft_warn` · 0 `PHONE_RE` / `URL_RE` / `ACCOUNT_RE`. Kết mở Chị Hai chỉ dùng cụm an toàn *"loại thẳng"*, tuyệt đối không chứa từ khóa bạo lực. |
| 9 | Nguồn cảm hứng (nội bộ) | Đã ghi nguồn cảm hứng và bảng hư cấu hóa vào `source/`? | ☑ ĐẠT | Đã lập đầy đủ tại `source/SOURCE.md` cùng đăng ký `EP10` (`VAR-FUNNEL-01` / `VAR-AI-01`) tại `01_SCAM_MAP/VIGILANCE_LIBRARY_MAP.md`. |

**Người thẩm định (Tầng 1 `materialAndDraft`):** Ban Biên Tập VCH  **Ngày:** 23/11/2026

**TRẠNG THÁI TỔNG: ĐẠT**
