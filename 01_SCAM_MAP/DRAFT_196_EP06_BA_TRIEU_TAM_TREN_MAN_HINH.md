# 196 / EP06 – BA TRIỆU TÁM TRÊN MÀN HÌNH *(Bản nháp chuẩn hóa Tầng 1 – chờ duyệt lên Staging)*

- **Mã tập:** `EP06` (`factory196`) · **Slug:** `BaTrieuTamTrenManHinh`
- **Nhà máy:** `factory196` – `16:9` (`1920x1080 @ 30fps`) · **Thời lượng ước tính:** `~260s – 285s` (~4 phút 25 giây sau khi căn WAV TTS thật ở Gate 2)
- **Họ kịch bản:** `JOB-TASK` – Bẫy cộng tác viên xử lý đơn hàng tại nhà: **Cấp sẵn `40.000đ` vốn làm thử** (không tốn tiền túi ở đơn đầu `30.000đ` → nhảy lên `45.000đ`) → Đơn `55.000đ` chỉ bắt **"bù phần thiếu" `10.000đ`** → Trượt dần sang các khoản bù chênh lệch vài trăm ngàn khiến nạn nhân mất **`2.140.000đ` tiền thật**, trong khi màn hình treo con số ảo **`3.850.000đ`** để ép nạp thêm `2.900.000đ` → **Người bạn IT giấu mặt** tra tên miền bóc trần trang tự nhận từ năm 2018 thực chất mới mở 6 ngày → **Kết mở đường dây ngầm:** Cụm máy chủ mới mở lại chung đầu mối với mấy nhánh đợt trước.
- **Tỷ lệ:** **~97% kịch tâm lý – điện ảnh / ~3% Người Bóc Trần (đúng 1 câu 19 từ, thẻ kết `< 9s`)**
- **Thông điệp lõi:** *Tiền nằm trong ngân hàng mới có đơn vị chịu trách nhiệm giữ cho bạn; còn số dư nhảy trên một trang web lạ chỉ là con số người dựng trang muốn gõ bao nhiêu cũng được.*

---

## 1. Đối chiếu nâng cấp từ bản nháp thô [`story.txt`](../factory196/materialAndDraft/EP06/story.txt) sang chuẩn `factory196` (`EP04` / `EP27` / `EP05`)

1. **Sửa lỗi toán học ở mồi nhử đầu tiên:** Bản nháp gốc ghi cấp sẵn `50.000đ`, làm đơn `30.000đ` xong số dư lại tụt còn `45.000đ` (lỗ 5.000đ). Bản chuẩn chỉnh lại: **cấp sẵn `40.000đ`** → hoàn thành đơn `30.000đ` cộng hoa hồng thành **`45.000đ`** → qua đơn `55.000đ` báo **thiếu đúng `10.000đ`** (`55k - 45k = 10k`), khớp logic tuyệt đối.
2. **Đảo cấu trúc Hook `00:00 – 00:30` chuẩn điện ảnh:** Thay vì mở đầu chậm rãi lướt điện thoại, phim mở thẳng vào khoảnh khắc nửa đêm khi Nam bấm rút `3.850.000đ` bị khóa và bị ép nạp thêm `2.900.000đ` trước 23h, sau đó mới lùi về 3 tối mưa trước.
3. **Bối cảnh đời thực tôn trọng nhân vật:** Nam không tham làm giàu ảo — mưa dầm cả tuần làm kho cắt ca tối, anh muốn kiếm thêm chút tiền buổi tối ở nhà phụ vợ đóng học cho con. Vợ Nam (**Thảo**) kiệm lời, tỉnh táo, hỏi đúng 2 câu chạm tim đen (*"Có bắt bỏ tiền túi ra hông?"* và *"Anh rút thử về ngân hàng mình lần nào chưa?"*) và không hề chì chiết khi chồng thú thật mất `2.140.000đ`.
4. **Chuyển hóa đoạn thuyết giảng cuối phim thành thoại đời & Bóc trần `< 10s`:** Đoạn lời dẫn dài gần 100 chữ ở cuối `story.txt` được cô đọng thành câu nói sắc gọn của người bạn IT (*"Tiền trong ngân hàng mới có nơi giữ cho mày. Còn con số trên trang lạ… tụi nó gõ bao nhiêu chẳng được."*) và đúng **1 câu 19 từ (`< 9s`)** của `Người Bóc Trần`.
5. **Giữ trọn chi tiết "Từ năm 2018" + Người bạn IT giấu mặt + Kết mở nhẹ nhàng:**
   - Cài rõ dòng chữ `"Vận hành từ năm 2018"` ngay ở Hồi 1 (`s03`) cả trên bong bóng lẫn câu Nam trấn an vợ để cú tra tên miền ở Hồi 4 (`s09`) có căn cứ chặt chẽ.
   - Giữ đúng ghi chú sản xuất của tác giả: **Người bạn IT hoàn toàn không lộ mặt, không lộ tên**. Sau thẻ `NHỚ KỸ`, thêm đúng 10 giây kết mở khi chiếc điện thoại thứ hai trên bàn anh ta rung lên: *"Ừ. Lại chung một đầu mối đứng sau mấy nhánh đợt trước."* rồi cắt đen đột ngột — nối mạch tự nhiên với `EP04` & `EP05` mà không lộ ý tưởng hay tự trói kịch bản về sau.

---

## 2. Nhân vật & Phân tách giọng (`02_CAST/cast.json` – 7 tuyến / 7 voice khác nhau 100%)

| Nhân vật trong tập | Key `cast.json` | Voice | Chỉ đạo diễn xuất & âm sắc |
| :--- | :--- | :--- | :--- |
| **Nam** (32t, kỹ thuật viên kho, chăm làm) | `anh_hai` | `Orus` | Nam trầm ấm, thật thà; hào hứng lúc đầu, chua chát ở Hồi 3, thẳng thắn nhận lỗi ở Hồi 5 |
| **Thảo** (31t, vợ Nam) | `chi_hai` | `Sulafat` | Nữ trầm vừa, **cực kiệm lời, thực tế, không trách móc**, giữ nhịp tỉnh táo cho gia đình |
| **Vy Điều Phối** (hướng dẫn đơn đầu) | `ke_ngot_ngao_nu` (+ `af: phone`) | `Aoede` | Nữ trẻ ngọt ngào, lịch sự, bình thường hóa việc "bù phần thiếu" rồi khóa máy |
| **Bộ phận Hỗ trợ đối soát** | `chu_no` (+ `af: phone`) | `Fenrir` | Nam trầm đều, **lịch sự lạnh băng**, đánh đúng tâm lý tiếc `3,8 triệu` đang treo |
| **Người bạn IT giấu mặt** | `ong_bay` | `Algenib` | Nam 35t trầm khàn nhẹ, điềm tĩnh, kiệm lời; **khung hình tuyệt đối không lộ mặt** |
| **Đầu dây lạ (Kết mở)** | `chi_tu` (+ `af: phone`) | `Zephyr` | Nữ trầm tĩnh gọi vào máy phụ của người bạn IT ở cảnh kết mở |
| **Người Bóc Trần** | `nguoi_boc_tran` | `Charon` | **Chỉ xuất hiện đúng 1 câu (19 từ, `< 9s`) ở thẻ `NHỚ KỸ`** |

---

## 3. Bản đồ chi tiết CÀI – TRẢ

| Cài ở | Chi tiết điện ảnh | Trả ở |
| :--- | :--- | :--- |
| **C3** (Hồi 1) | Dòng giới thiệu `"Vận hành từ năm 2018"` + câu Nam khoe vợ *"trang này ghi chạy từ năm hai ngàn mười tám"* | **C9** (Hồi 4): Người bạn IT tra ra tên miền thật mới đăng ký hồi **thứ Ba tuần trước (6 ngày tuổi)** |
| **C3–C5** (Hồi 1–2) | Cấp sẵn `40.000đ` → bù `10.000đ` → bù từng khoản chênh lệch lẻ vài trăm ngàn | **C7 & C10** (Hồi 3 & 5): Sao kê ngân hàng thật cộng dồn thành **`-2.140.000đ` tiền thật đã mất** |
| **C6** (Hồi 2) | Câu hỏi tỉnh táo của Thảo: *"Nhưng anh bấm rút thử tiền về ngân hàng mình lần nào chưa?"* | **C0 & C7**: Nút rút tiền có sẵn chỉ là hình vẽ; chính sự tỉnh táo giúp Nam dừng tay không nạp thêm `2.900.000đ` |
| **C8–C9** (Hồi 4) | Căn phòng tối của **Người bạn IT giấu mặt** (chỉ thấy đôi bàn tay cạnh laptop) | **C11 (Kết mở):** Cuộc gọi máy phụ tiết lộ cụm tên miền mới mở lại chung đầu mối với *"mấy nhánh đợt trước"* |

---

## 4. Kịch bản chi tiết theo cảnh (15 cảnh · 30 câu thoại · Mọi câu ≤ 25 từ)

*(Xem toàn văn lời thoại và mã biên dịch timeline tại [`factory196/materialAndDraft/EP06/script/SCRIPT.md`](../factory196/materialAndDraft/EP06/script/SCRIPT.md) và [`factory196/materialAndDraft/EP06/source/build_draft.py`](../factory196/materialAndDraft/EP06/source/build_draft.py)).*

---

## 5. Tự kiểm Pháp lý, Nghiệp vụ & Harness (`Gate 0` & `Gate 5` Pre-check)

- [x] **Sạch 100% `policy_wordlists.json`:** `0 identity_hard_block` (không nêu tên sàn TMĐT, ngân hàng, ví điện tử thật) · `0 identity_soft_warn` (không dùng Zalo/Facebook/Telegram) · `0 asr_ocr_hard_block` · `0 asr_ocr_soft_warn` (tuyệt đối không dùng cụm `"kiếm tiền online"`, `"lãi khủng"`, `"chết"`, `"tống tiền"`).
- [x] **Sạch 100% Regex `PHONE_RE` / `URL_RE` / `ACCOUNT_RE`:** Không viết tên miền có đuôi `.com/.vn/.online` trên bong bóng (dùng nhãn mô tả `"Ngày đăng ký thật: Thứ Ba tuần trước"`), số tài khoản che 4 số cuối (`TK …6821`).
- [x] **Đúng khuyến nghị pháp lý (`CONTENT_LEGAL_SAFETY_HARNESS.md`):** Dặn rõ cắt lỗ ngay, không thuê "dịch vụ lấy lại tiền treo" (tránh bẫy lừa lần hai), lưu sao kê và đường dẫn trình báo cơ quan công an.
- [x] **Chuẩn thoại `factory196`:** 30 câu thoại, **100% câu ≤ 25 từ**, phương ngữ miền Nam tự nhiên xuyên suốt, `Người Bóc Trần` đúng 1 câu 19 từ (`< 9s`).
