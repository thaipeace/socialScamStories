# NGUỒN CẢM HỨNG & HỒ SƠ CHUYỂN HÓA KỊCH BẢN (NỘI BỘ) – 196 EP06

## 1. Chất liệu gốc & phân tích tâm lý
- **Bản nháp ý tưởng gốc:** [`story.txt`](../story.txt) (*Cộng tác viên mua hàng online*) do chủ kênh cung cấp — khai thác góc nhìn tâm lý đời thường cực kỳ tinh tế: sự nhầm lẫn giữa **tiền thật đi ra từ tài khoản ngân hàng** và **con số ảo do người dựng web tự gõ lên màn hình**.
- **Chuẩn hóa nghiệp vụ & cấu trúc theo `LONG_FORMAT_196_SPEC.md` (`v1` → `v2-draft`):**
  1. **Lý do kinh tế thuyết phục & Tên ứng dụng sang hơn (`v2`):** Đặt tên hư cấu **`Bạn Thân 4.0`** kèm lời giới thiệu ngắn gọn ngay Hồi 1: *ứng dụng uy tín kết nối mua hàng giùm cho những người bận không có thời gian, người rảnh nhận mua hộ ăn hoa hồng theo đơn, tự nhận vận hành từ năm 2018*. Nhờ có lý do hợp lý, nhân vật Nam có động cơ thuyết phục để tin và làm tiếp.
  2. **Nhóm chat chim mồi sống động thay cho tương tác 1-1 khô khan (`v2`):** Bổ sung cảnh **`s03b_group_buzz`** trong Hồi 1 với **Nhóm Bạn Thân 4.0** liên tục báo thành quả, cảm ơn rối rít (Chị Loan, Hoa, Tuấn, Minh). Sang Hồi 2 (`s04`, `s05`), giảm bớt tương tác 1-1 với Điều Phối/Hỗ Trợ, đẩy phần giải thích "bù 10.000đ" và cổ vũ lên đơn lớn vào **kênh group chat** để các thành viên chỉ vẽ, khuyến khích tự nhiên. Sang Hồi 3 (`s07`), sau khi bấm rút bị đòi bù `2.900.000đ`, nhóm chat lẫn hỗ trợ **không hề vô lý khóa chặn gì cả** mà tiếp tục xúm vô hối nạp trước 23h — chính sự tương phản giữa sao kê ngân hàng thật `-2.140.000đ` với những tin nhắn hối nạp đó khiến Nam tự khựng tay lại.
  3. **Khớp chuẩn toán học mồi nhử:** Điều chỉnh vốn cấp sẵn thành `40.000đ` → hoàn thành đơn đầu `30.000đ` nhảy lên `45.000đ` (không tốn 1 đồng tiền túi) → đơn thứ hai `55.000đ` thiếu đúng `10.000đ` (`55.000 - 45.000 = 10.000đ`), rồi trượt dần sang `-180.000đ`, `-450.000đ`, `-1.500.000đ` = **`-2.140.000đ` tiền thật** trong khi màn hình treo **`3.850.000đ`** đòi nạp thêm `2.900.000đ`.
  4. **Người bạn cũ giấu mặt cực kiệm lời (`v2`):** Cắt mạnh thoại dài dòng ở Hồi 4 xuống chỉ còn **2 câu (tổng 25 từ)**: *"Tên miền mới mở thứ Ba tuần trước. Biết ngay mà."* và *"Số đó tụi nó tự gõ. Bỏ ngay đi, chuyển nữa là mất nữa."* — sắc gọn như đã biết sẵn chuyện, đủ sức nặng thuyết phục Nam dừng tay ngay lập tức.
  5. **Kết mở đường dây ngầm gọn lạnh, không thừa thông tin (`v2`):** Bỏ cuộc gọi máy phụ giải thích cụm máy chủ/nhánh trước (vốn hơi hiền và dễ trói logic về sau). Chỉ giữ đúng một hình ảnh rợn người trong căn phòng tối: màn hình vi tính hiện **danh sách khách** (`#408 · #409 · #410 · Nam`), đúng 1 câu buông gọn ***"Haiz… đúng là trái đất tròn."***, con trỏ chuột rê thẳng vào nút **`"Chốt khách"`** rồi cắt đen đột ngột.

## 2. Bảng hư cấu hóa 100% (Tuân thủ 5 Nguyên tắc vàng `CONTENT_LEGAL_SAFETY_HARNESS.md`)
| Chi tiết nhạy cảm (KHÔNG ĐƯA VÀO PHIM) | Chi tiết hư cấu hóa trên phim (`196 EP06`) | Lý do an toàn pháp lý |
| :--- | :--- | :--- |
| Tên sàn TMĐT, ứng dụng mua hộ, ngân hàng hoặc ví điện tử thật | **“Bạn Thân 4.0”**, **“Nhóm Bạn Thân 4.0”**, **“Ngân hàng của Nam”**, **“TK …6821”** | Sạch 100% `identity_hard_block` & `ACCOUNT_RE` |
| Tên miền cụ thể có đuôi `.com`, `.vn`, `.online`... | Nhãn mô tả **“Ngày đăng ký thật: Thứ Ba tuần trước (6 ngày)”** | Sạch 100% `URL_RE` (tránh trùng tên miền có thật) |
| Nền tảng mạng xã hội / ứng dụng nhắn tin cụ thể | **“Nhóm”**, **“Tin nhắn”**, **“Đường dẫn”** | Sạch 100% `identity_soft_warn` |
| Cụm từ nhạy cảm thuật toán (`kiếm tiền online`, `lãi khủng`, `chết`...) | **“Mua hàng giùm người bận”**, **“Bù phần thiếu”**, **“Hoa hồng theo đơn”** | Sạch 100% `asr_ocr_soft_warn` |

## 3. Trạng thái hồ sơ
- **Giai đoạn hiện tại:** Hồ sơ Tầng 1 (`factory196/materialAndDraft/EP06` – **`v2-draft`**) đã cập nhật đồng bộ kịch bản `SCRIPT.md`, `source/build_draft.py`, `episode.json`, `IMAGE_PROMPTS.md`, `clearance/CLEARANCE.md`, `PRODUCTION_RUNBOOK.md` — sẵn sàng chờ chủ kênh duyệt để sinh bộ 14 ảnh `16:9` (`assets/c00..c12.jpg` + `c03b.jpg`), thu TTS Gate 2 và dựng bản Staging Gate 5.
