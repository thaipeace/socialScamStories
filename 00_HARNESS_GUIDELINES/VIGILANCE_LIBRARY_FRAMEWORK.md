# KHUNG CHIẾN LƯỢC THƯ VIỆN CẢNH GIÁC – TÈO CẢNH GIÁC
*Mã: STRAT-VIGILANCE-LIB-V1 · Trạng thái: **Thử nghiệm cố định cho giai đoạn tiếp theo** · Áp dụng từ các tập mới (`factory196: EP08b, EP10+`, `factory619: EP11+`)*

> [!IMPORTANT]
> **Nguyên tắc áp dụng & Không hồi tố:**
> 1. **Không sửa đổi các tập đã hoàn thành/đã đăng** (`factory196: EP01b–EP08, EP27` và `factory619: EP01–EP10`). Khung này chỉ áp dụng từ các tập mới trở về sau.
> 2. **Tách rõ 2 tầng — không ghi đè kinh nghiệm cầm tay chỉ việc:** Khung này khóa **Tầng Chiến lược dài hơi** (chọn đề tài, phân loại cơ chế, tránh lặp theo giai đoạn). Toàn bộ các nguyên tắc **Tầng Cảm nhận tức thời của người xem** đã được chủ kênh trực tiếp chỉnh qua thực chiến (nhịp phim `~97%` kịch / `~3%` Người Bóc Trần `≤ 10s`, cấm dạy đời, thoại miền Nam tự nhiên, cài–trả, logic hình ảnh/giọng đọc) vẫn **giữ nguyên 100%** tại [STORY_AND_PRODUCTION_HARNESS.md](STORY_AND_PRODUCTION_HARNESS.md) và [LONG_FORMAT_196_SPEC.md](LONG_FORMAT_196_SPEC.md).
> 3. **Có mốc kiểm chứng thực tế:** Vì chưa thể đánh giá hiệu quả của khung trước khi chạy thật, sau **6–8 tập mới** sẽ mở phiếu tổng kết ở Mục VI để quyết định giữ nguyên, tinh chỉnh hay loại bỏ.

---

## I. ĐỊNH VỊ DÀI HƠI: THƯ VIỆN CẢNH GIÁC THỰC DỤNG

- **Bản chất kênh:** Xây dựng một **thư viện cảnh giác có giá trị sử dụng thực tế**, không phải kênh phim tâm lý xã hội hay kênh phân tích tâm lý con người.
- **Kỳ vọng sử dụng:** Người xem đến kênh không phải để nghe phân tích dài dòng vì sao con người tham lam, cô đơn, sợ hãi hay tự ái — mà để khi **gặp một tình huống tương tự ngoài đời**, họ nhớ lại video, nhận ra chuyện gì đang diễn ra và biết bước tiếp theo nên làm gì.
- **Tách rạch ròi Backend (Quản trị kênh) và Frontend (Trải nghiệm xem):**
  - **Backend (Hậu trường):** Quản trị kho kịch bản chặt chẽ theo **Thư viện 3 lớp** và **Bản đồ biến thể** tại [VIGILANCE_LIBRARY_MAP.md](../01_SCAM_MAP/VIGILANCE_LIBRARY_MAP.md) để tránh trùng lặp, biết kênh đang dày chỗ nào, thiếu chỗ nào.
  - **Frontend (Mặt tiền video):** Vẫn kể bằng **tình huống kịch tính đời thực có 1 chi tiết neo ký ức mạnh**, không biến video thành bài thuyết giảng hay từ điển khô khan.

---

## II. VAI TRÒ CỦA TÂM LÝ & ƯU TIÊN BIÊN TẬP

Tâm lý chỉ là **công cụ dẫn chuyện**, không phải chủ đề chính của kênh. Chỉ dùng đủ để giải thích vì sao thủ đoạn đó có hiệu lực với một nhóm người trong một hoàn cảnh cụ thể — không phân tích tâm lý dài dòng, không biến mỗi tập thành bài học nhân sinh, không bắt người xem phải đồng cảm với nạn nhân mới hiểu giá trị cảnh báo.

| Trục nội dung | Tỷ trọng ưu tiên biên tập | Cách thể hiện khớp với chuẩn thực chiến của kênh |
| :--- | :---: | :--- |
| **1. Thủ đoạn & diễn biến thực tế** | **60 – 70%** | Tập trung vào **bề mặt nạn nhân nhìn thấy, nghe thấy, thao tác** và cấu trúc cái bẫy. Giữ chặt Nguyên tắc #3 *Không dạy lừa* (`L2`) tại [CONTENT_LEGAL_SAFETY_HARNESS.md](CONTENT_LEGAL_SAFETY_HARNESS.md) — không biến cảnh phòng tối thành hướng dẫn thao tác lừa. |
| **2. Tâm lý & điểm dễ mắc** | **15 – 25%** | Thể hiện qua **điều kiện hoàn cảnh cụ thể** (cần việc, đang giữ bí mật, đã nhận tiền thật, tin đã xác minh...) thay vì lời bình tâm lý học đại cương. |
| **3. Cách nhận biết, xử lý, phòng tránh** | **10 – 20%** | **Bắt buộc nhúng vào hành động & quyết định trong kịch** (nhân vật kiểm chứng, khóa thẻ, báo nhóm, lập biên bản, dừng nạp...). **KHÔNG** kéo dài lời giảng của `Người Bóc Trần` cuối phim (vẫn giữ `≤ 10 giây` theo `STORY_AND_PRODUCTION_HARNESS.md`). |

*Lưu ý: Đây là tỷ lệ ưu tiên về giá trị thông tin trong kịch bản, không phải khuôn cứng chia phút thuyết minh.*

---

## III. KIẾN TRÚC THƯ VIỆN 3 LỚP (CỐ ĐỊNH LÂU DÀI)

Thay vì cố định một công thức kể chuyện duy nhất, kênh cố định **3 lớp tri thức** dưới đây. Một tập có thể tập trung sâu vào 1 lớp, hoặc nối cả 3 lớp.

### Lớp 1 — Thư viện Thủ đoạn & Biến thể (`TACTIC / VAR`)
Chuyển trục phân loại từ **tên chiêu phẳng** (*lừa tuyển dụng, lừa nhiệm vụ, lừa đầu tư, lừa OTP...*) sang **cơ chế vận hành & biến thể của cái bẫy**:
- Cách tiếp cận nạn nhân.
- Kịch bản dẫn dụ & lớp vỏ mới.
- Các bước thao túng giao dịch / thông tin.
- Điểm lấy tiền, lấy tài khoản, lấy dữ liệu.
- Những biến thể đã xuất hiện & dấu hiệu đặc trưng.

*Ví dụ minh họa — cùng 1 họ "Lừa nhiệm vụ", nhưng tách thành các biến thể độc lập để không cạn đề tài:*

| Mã mẫu | Biến thể của cái bẫy | Nội dung cảnh giác cần lưu trong thư viện |
| :--- | :--- | :--- |
| `VAR-TASK-01` | Có trả tiền thật ban đầu | Tiền nhận được ban đầu không chứng minh hệ thống hợp pháp |
| `VAR-TASK-02` | Không yêu cầu tiền lúc đầu / cấp sẵn vốn ảo | Mục tiêu thu tiền bị trì hoãn cho đến khi nạn nhân đã tin |
| `VAR-TASK-03` | Có người hướng dẫn riêng (1-1) | Kẻ lừa kiểm soát hoàn toàn luồng thông tin và nhịp độ quyết định |
| `VAR-TASK-04` | Có nhóm người cùng làm (group chat chim mồi) | Tạo áp lực đồng thuận giả để át nghi ngờ cá nhân |
| `VAR-TASK-05` | Nhiệm vụ tăng cấp / bù phần thiếu | Nâng dần mức độ rủi ro sau khi nạn nhân đã bước vào quy trình |
| `VAR-TASK-06` | Phát sinh lỗi rút tiền / sai cú pháp / đối soát | Tiền bị khóa bằng lý do kỹ thuật giả để ép đóng thêm |
| `VAR-TASK-07` | Cho vay hoặc "hỗ trợ góp chung" để hoàn thành nhiệm vụ | Biến nạn nhân thành người chủ động xoay/vay thêm tiền bên ngoài |
| `VAR-TASK-08` | Đổi nền tảng, đổi tên, đổi đối tượng | Thủ đoạn cũ được tái sử dụng dưới lớp vỏ ngành nghề/ứng dụng mới |

### Lớp 2 — Thư viện Điểm dễ mắc (`COND`)
Không phải lý thuyết tâm lý đại cương, mà là **các điều kiện hoàn cảnh khiến thủ đoạn có tác dụng**:
- `COND-01`: Đang cần việc / kẹt tiền gấp.
- `COND-02`: Tin rằng mình đã tự xác minh được đối phương (quét virus sạch, thấy video 3 giây, nghe giọng thật, thấy tên miền/giấy tờ giả).
- `COND-03`: Đã nhận tiền thật hoặc lợi ích thật ở bước đầu.
- `COND-04`: Đang có tiền mắc kẹt / tâm lý cố cứu khoản đã mất.
- `COND-05`: Bị thúc ép về thời gian (cấp cứu, khóa tài khoản, sát giờ chốt đơn).
- `COND-06`: Có người quen giới thiệu / nhân danh người cùng cảnh ngộ / sếp / đồng nghiệp.
- `COND-07`: Đang giữ bí mật với gia đình (vì sĩ diện, sợ bị trách, hoặc bị dặn "đừng nói ai").
- `COND-08`: Say ảo tưởng quyền lực / lợi ích đám đông tung hô.
- `COND-09`: Muốn giúp người (lòng tốt, sự lịch sự) trong tình huống vội vã ngoài đời.

### Lớp 3 — Thư viện Ứng phó (`RESP`)
Người xem cần làm gì khi tình huống xảy ra thật:
- `RESP-01`: Dừng ở bước nào? (điểm cắt lỗ / điểm ngắt tương tác).
- `RESP-02`: Tuyệt đối không cung cấp thêm gì? (OTP, căn cước, khuôn mặt nhìn thẳng cam, tiền "gỡ lệnh").
- `RESP-03`: Kiểm tra ở đâu, bằng cách nào? (kênh độc lập, gọi lại số gốc, đối chiếu sao kê thật, tra thông tin ngoài kịch bản kẻ gian).
- `RESP-04`: Liên hệ ai & báo ngay cho nhóm xung quanh? (người thân, nhóm công ty/xưởng, ngân hàng, cơ quan công an).
- `RESP-05`: Đã lỡ chuyển tiền / lộ thông tin / cài ứng dụng lạ thì xử lý ngay những bước nào?
- `RESP-06`: Những hành động nào khiến tình hình tệ hơn? (tự im lặng giấu gia đình, chuyển thêm để "êm chuyện", tìm dịch vụ "lấy lại tiền" trên mạng).

> [!WARNING]
> **Rào chắn pháp lý cho Lớp 3 (`L6` & `L8`):** Mọi hướng dẫn ứng phó chi tiết (đặc biệt liên quan ngân hàng, gỡ mã độc, thủ tục pháp lý) phải tuân thủ Mục III [CONTENT_LEGAL_SAFETY_HARNESS.md](CONTENT_LEGAL_SAFETY_HARNESS.md) — chỉ nêu khuyến nghị phổ quát hoặc đã kiểm chứng; tuyệt đối không chèn hotline/web chưa xác thực, và luôn ghim cảnh báo chống lừa đảo "hỗ trợ lấy lại tiền" dưới phần bình luận.

---

## IV. SÁU GÓC QUAN SÁT (FORMAT A–F) & PHÂN VAI 2 NHÀ MÁY

Để cùng một chủ đề cũ nhưng cách tiếp cận không nhàm, mỗi tập mới chọn rõ **1 góc quan sát chủ đạo** trong 6 dạng sau và gắn đúng nhà máy phù hợp:

| Mã | Góc quan sát | Trọng tâm nội dung | Nhà máy ưu tiên | Ghi chú thực chiến |
| :-: | :--- | :--- | :---: | :--- |
| **A** | **Giải phẫu một chiêu lừa** | Theo dõi toàn bộ cơ chế vận hành từ lúc tiếp cận đến điểm lấy tiền/dữ liệu. | `factory196` *(16:9)* | Xương sống phim dài 4–6 phút (nối cả 3 lớp). |
| **B** | **Một chi tiết tưởng bình thường** | Soi sâu đúng 1 dấu hiệu nhỏ, 1 câu nói, 1 thao tác hoặc 1 bước quy trình hay bị bỏ qua. | `factory619` *(9:16)* | Hợp Short 50–60s; đánh thẳng vào 1 nút `VAR` hoặc `COND`. |
| **C** | **Cùng một chiêu, hai nạn nhân** | Đặt 2 tình huống thực tế song song: vì sao người này phát hiện, người kia mắc bẫy (không phán xét trí thông minh). | `factory196` hoặc `factory619` | Đã chứng minh hiệu quả ở Short `EP03`; trên phim dài nên đặt trong cùng 1 trục truyện để không loãng nhân vật. |
| **D** | **Cập nhật biến thể mới** | Chiêu cũ quay lại với 1 thay đổi mới — chỉ rõ **cái mới nằm ở đâu, cái cũ nào vẫn còn**. | `factory619` *(9:16)* hoặc `factory196` | Cực mạnh khi có biến thể mới nóng ngoài xã hội mà không cần kể lại chiêu cũ từ đầu. |
| **E** | **Kiểm tra thực chiến** | Đưa ra 1 tình huống/tin nhắn/lời mời cụ thể để người xem tự tìm điểm đáng ngờ trước khi video lật đáp án. | `factory619` *(9:16)* | Kéo comment & xem lại cao trên Shorts/Reels; giữ nhịp gọn trong 55s. |
| **F** | **Khi đã mắc bẫy, phải làm gì?** | Xử lý thực tế sau khi đã chuyển tiền, lộ giấy tờ, cài app lạ, mất tài khoản, bị gây sức ép. | **Nhúng vào Hồi 4–5 của `factory196`**, hoặc tách **Playlist riêng** | Giá trị tìm kiếm cao nhưng chạm rủi ro `L8` & `L6` — nếu làm tập độc lập phải kiểm chứng nghiệp vụ kỹ và kiểm duyệt comment chặt. |

**Quy tắc về mạch cài "đường dây ngầm / kết mở" (nếu dùng ở `factory196`):**
- Phần thân tập (`0% – 95%`) phải **độc lập 100%** như một mục hoàn chỉnh của thư viện (khán giả xem riêng lẻ vẫn hiểu trọn vẹn và áp dụng được ngay).
- Chi tiết cài đường dây ngầm (nếu có) chỉ giữ như *easter egg 10–15 giây cuối*, không làm lu mờ giá trị cảnh giác thực dụng.

---

## V. CỔNG DUYỆT Ý TƯỞNG TRƯỚC GATE 0 (PRE-GATE 0 FILTER)

**Nguyên tắc cốt lõi:** *Không làm video chỉ vì thấy một vụ lừa mới trên báo/mạng. Chỉ làm khi tìm được ít nhất 1 giá trị cảnh giác mới rõ ràng cho thư viện.* (Ngược lại, chiêu cũ 5 năm trước vẫn làm nếu bổ sung biến thể, góc nhìn hoặc cách xử lý mà thư viện chưa có).

Trước khi viết kịch bản (`Gate 0`), chấm ý tưởng theo **4 câu cốt lõi + 2 câu thực chiến**:

1. **Mới:** Người xem chưa được biết chi tiết/biến thể này, hoặc chưa từng thấy nó dưới góc quan sát này?
2. **Thực dụng:** Kiến thức trong tập có áp dụng được trực tiếp khi gặp chuyện ngoài đời không?
3. **Khác biệt:** Đối chiếu [VIGILANCE_LIBRARY_MAP.md](../01_SCAM_MAP/VIGILANCE_LIBRARY_MAP.md) — tập này có chỉ đang lặp lại tập cũ bằng cách đổi tên thủ đoạn không?
4. **Có ích:** Xem xong, người xem biết thêm cụ thể điều gì để bảo vệ mình hoặc người thân?
5. **Dễ kể lại (1 câu neo ký ức):** Có nén được bài học lõi của tập thành **đúng 1 câu dễ nhớ** để khán giả nhắc lại với bố mẹ/bạn bè không?
6. **An toàn & Hình ảnh hóa được:** Thể hiện rõ bằng tranh 2D không logo/app thật, không chạm `L2` (*Không dạy lừa*) và không chạm `L8` (*Khuyến nghị chưa kiểm chứng*)?

> **Quyết định duyệt:** Phải vượt qua câu 6 (an toàn pháp lý) **và** tạo ra ít nhất **1 nút kiến thức mới rõ ràng** ở Lớp 1, Lớp 2 hoặc Lớp 3. Nếu không đạt → bỏ qua hoặc chuyển xuống làm Short biến thể (`B`/`D`), không làm phim dài.

---

## VI. PHIẾU TỔNG KẾT ĐÁNH GIÁ KHUNG SAU 1 GIAI ĐOẠN (6–8 TẬP MỚI)

Vì khung chiến lược này được chốt để **thử nghiệm thực tế dài hơi**, sau khi phát hành đủ **6–8 tập mới** theo khung (ví dụ `factory196: EP08b, EP10–EP14` và/hoặc `factory619: EP11–EP18`), chủ kênh rà soát lại 5 tiêu chí dưới đây để quyết định giữ nguyên hay điều chỉnh:

| Tiêu chí đánh giá | Cách quan sát thực tế | Câu hỏi chốt sau giai đoạn |
| :--- | :--- | :--- |
| **1. Giữ chân người xem** | Retention 30 giây đầu & tỷ lệ xem đến thẻ `NHỚ KỸ` so với nhóm `EP03–EP08` | Chuyển trọng tâm sang cơ chế/thủ đoạn có giữ người xem tốt hơn hay kém hơn nhóm tập nặng tâm lý? |
| **2. Tỷ lệ chia sẻ & lưu** | Share / View và bình luận dạng *"gửi cho bố mẹ"*, *"mới gặp y chang"* | Khung Thư viện 3 lớp có làm tăng giá trị sử dụng & hành vi chia sẻ không? |
| **3. Hiệu quả phân format (A–F)** | So sánh CTR & View giữa các góc `A`, `B`, `C`, `D`, `E`, `F` | Format nào ăn khách nhất ở `factory196` và `factory619`? Format nào nên bỏ? |
| **4. Tốc độ & độ dễ ra đề tài** | Cảm nhận của chủ kênh khi chọn đề tài 6–8 tập liên tiếp | Bản đồ 3 lớp + bộ lọc có giúp tránh bí ý tưởng & cắt thời gian do dự không? |
| **5. An toàn pháp lý & comment** | Cảnh báo nền tảng, mức độ xuất hiện comment "dịch vụ lấy lại tiền" | Rủi ro `L2`, `L6`, `L8` có nằm trong tầm kiểm soát khi làm sâu về cơ chế & ứng phó? |
