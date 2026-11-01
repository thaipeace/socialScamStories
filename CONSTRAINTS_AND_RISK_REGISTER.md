# SỔ GHI RÀNG BUỘC & RỦI RO (CONSTRAINTS & RISK REGISTER)
## Lập ngày 01/11/2026 khi chuyển hướng từ dự án 779 sang kênh Bóc Trần Lừa Đảo

> **Trạng thái**: `MỞ` · `ĐANG LÀM` · `ĐÃ XONG` · `CHẤP NHẬN RỦI RO` (ghi lý do)
> **Nguyên tắc**: mục mức CAO phải xong trước khi đăng tập đầu tiên.

## L. PHÁP LÝ & NỀN TẢNG
| ID | Rủi ro | Mức | Biện pháp | Trạng thái |
| :--- | :--- | :---: | :--- | :--- |
| L1 | Vu khống / xúc phạm danh dự nếu ám chỉ người, doanh nghiệp, app cụ thể | **CAO** | Nguyên tắc 1–2 harness pháp lý; Gate 5 quét tên thương hiệu, SĐT, STK, URL | ĐANG LÀM (engine đã có bộ quét) |
| L2 | Bị nền tảng coi là nội dung hướng dẫn lừa đảo / gây hại | **CAO** | Nguyên tắc 3 “Không dạy lừa”; mục tự kiểm trong kịch bản; Gate 5 điểm 2 bắt buộc người duyệt | ĐANG LÀM |
| L3 | Vi phạm nhãn hiệu / giả mạo cơ quan (logo, giao diện, sắc phục) | **CAO** | Prompt ảnh bắt buộc “no logos/no uniforms”; bong bóng chat trung tính; Gate 5 điểm 4 | ĐANG LÀM |
| L4 | Nội dung AI hàng loạt bị hạn chế kiếm tiền (inauthentic/repetitious) | TRUNG BÌNH | Mỗi tập có giá trị biên tập riêng (dấu hiệu, việc nên làm); khai báo AI; đa dạng tình huống | MỞ |
| L5 | Từ khóa nhạy cảm (đe dọa, tình dục, cờ bạc, tự hại) bị bóp/giới hạn tuổi | TRUNG BÌNH | `policy_wordlists.json` + câu thay thế | ĐANG LÀM |
| L6 | Bình luận của khán giả lộ thông tin cá nhân / chỉ đích danh | TRUNG BÌNH | Ghim nhắc nhở; ẩn bình luận theo quy trình mục VII harness | MỞ |
| L7 | Căn cứ pháp lý trong harness do AI viết, chưa kiểm chứng | TRUNG BÌNH | Nhờ người có chuyên môn xem lại mục VI harness | MỞ |
| L8 | Khuyến nghị “nên làm” sai hoặc dẫn tới trang giả | **CAO** | Chỉ dùng khuyến nghị phổ quát (mục III harness); không ghi tổng đài/website chưa tự kiểm tra | ĐANG LÀM |

## C. KHẢ THI SẢN XUẤT (1 người)
| ID | Ràng buộc | Mức | Biện pháp | Trạng thái |
| :--- | :--- | :---: | :--- | :--- |
| C1 | Khối lượng 2 tập/tuần cho 1 người | TRUNG BÌNH | Engine dùng chung: mỗi tập chỉ cần `episode.json` + 6 ảnh; thử 8–12 tập trước | ĐANG LÀM |
| C2 | Đồng nhất nhân vật qua nhiều tập | TRUNG BÌNH | Dàn hình tượng cố định + mô tả ngoại hình trong CAST_AND_VISUAL_STYLE.md | MỞ |
| C3 | Tên giọng Gemini TTS trong `cast.json` chưa nghe thử với tiếng Việt | TRUNG BÌNH | Nghe thử từng giọng ở tập đầu, đổi nếu không hợp | MỞ |
| C4 | Engine mới viết lại từ 779, mới chạy thử với dữ liệu giả | TRUNG BÌNH | Chạy trọn 6 gate với tập thật đầu tiên, sửa lỗi phát sinh | ĐANG LÀM |
| C5 | Thư viện SFX tổng hợp có thể chưa đủ “thật” | THẤP | Cho phép thay bằng file âm thanh có bản quyền (`"file": ...`) | MỞ |

## D. HIỆU QUẢ
| ID | Vấn đề | Mức | Biện pháp | Trạng thái |
| :--- | :--- | :---: | :--- | :--- |
| D1 | Chủ đề lừa đảo nhiều kênh làm – cần khác biệt | TRUNG BÌNH | Định dạng phim + thẻ dấu hiệu nhận diện riêng; âm hiệu “ting ting” | MỞ |
| D2 | Khán giả 45+ ở Facebook/Zalo nhiều hơn YouTube | TRUNG BÌNH | Đăng song song 3 nền tảng, đo giữ chân | MỞ |
| D3 | Gây lo âu thay vì trao quyền | THẤP | Xen kẽ tập “thoát hiểm”; luôn kết bằng việc nên làm | MỞ |

## E. KẾ THỪA TỪ 779
| Hạng mục | Trạng thái |
| :--- | :--- |
| Kiến trúc 3 tầng `materialAndDraft → staging → production` | ✅ Giữ nguyên |
| 6 Gate + phiếu runbook | ✅ Giữ, thêm Gate 0 tự động |
| TTS Gemini + mastering (trim không phá, −3 dBFS) | ✅ Port, nâng model `gemini-3.8-flash-tts` |
| DSP tổng hợp SFX/BGM + auto-ducking + limiter | ✅ Port thành `dsp.py`, thư viện preset mới |
| Ken Burns, rung, chuyển cảnh, Safe Zone, branding VCH | ✅ Port thành `gate4_timeline.py` cấu hình hóa |
| Bộ lọc từ khóa ASR/OCR | ✅ Port + mở rộng |
| Nội dung lịch sử, nhân vật, bản đồ, harness chính trị 779 | ❌ Loại bỏ hoàn toàn |

## F. NHẬT KÝ
| Ngày | ID | Việc đã làm |
| :--- | :--- | :--- |
| 01/11/2026 | — | Khởi tạo dự án, port engine 6 Gate từ 779, viết harness pháp lý & định dạng mới, chạy thử engine với tập giả `EP00_SMOKE` |
