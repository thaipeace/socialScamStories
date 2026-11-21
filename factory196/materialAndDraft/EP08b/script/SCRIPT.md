# KỊCH BẢN PHIM DÀI 16:9 (4–5+ PHÚT) – EP08b: Tiền nổi rồi, tên lại khác

> Khung ngang 16:9 (`1920x1080`) · **Nửa bên kia dòng tiền `45.000.000đ` lúc `12:05` nối trực tiếp từ `EP08`** · Thời lượng mục tiêu **~5 phút (`~315s`, đạt chuẩn `240s–330s`)** · Tỷ lệ **~97% kịch thực tế / ~3% Người Bóc Trần (`< 9s`)** theo [LONG_FORMAT_196_SPEC.md](../../../../00_HARNESS_GUIDELINES/LONG_FORMAT_196_SPEC.md) và [STORY_AND_PRODUCTION_HARNESS.md](../../../../00_HARNESS_GUIDELINES/STORY_AND_PRODUCTION_HARNESS.md).
> Nguồn sự thật của timeline: [`source/build_draft.py`](../source/build_draft.py) → sinh [`episode.json`](../episode.json).
> Mọi tên người, số điện thoại, số tài khoản, biển số xe, tên ngân hàng/ứng dụng trong kịch bản đều là **hư cấu hoặc chung chung**.

## 0. Thẻ tập phim & Khung Thư viện Cảnh giác *(theo [VIGILANCE_LIBRARY_FRAMEWORK.md](../../../../00_HARNESS_GUIDELINES/VIGILANCE_LIBRARY_FRAMEWORK.md))*
| Mục | Nội dung |
| :--- | :--- |
| Góc quan sát (Format `A–F`) | **`D+F`** – Biến thể nối tiếp trực tiếp cơ chế Người đứng giữa từ `EP08` sang giao dịch công chứng mua bán xe máy (`45 triệu`) + Nhúng xử lý sự cố & nguyên tắc "2 Phải – 3 Không" |
| Nhóm chiêu & Biến thể Lớp 1 (`VAR`) | **`VAR-MITM-02` / `VAR-COM-04`** – Bẫy tam giác lệch dòng tiền khi bán xe/tài sản có công chứng thật: dẫn tiền `45 triệu` từ nạn nhân vụ lừa khác (**Khang**, `EP08`) chảy thẳng vào tài khoản người bán xe máy (**Anh Minh**), tay chân (**Long**) ký công chứng lấy xe thật |
| Điểm dễ mắc Lớp 2 (`COND`) | `COND-01` (muốn bán xe nhanh được đúng giá) · `COND-02` (ảo tưởng an toàn tuyệt đối: *"tiền nổi tài khoản + công chứng là chắc ăn"*) · `COND-05` (phòng công chứng đông đúc, tới lượt ký nên yên tâm ký nhanh) |
| Giá trị ứng phó Lớp 3 (`RESP`) | `RESP-01`, `RESP-03` (2 Phải – 3 Không nhúng trực tiếp vào cú chặn bẫy của Nam ở Hồi 5) · `RESP-04`, `RESP-05`, `RESP-06` (không rút/tẩu tán tiền đang xác minh vụ án, dừng ký hoàn trả qua ngân hàng nếu lệch tên, gom chứng cứ trình báo công an ở Hồi 4) |
| 1 câu neo ký ức (`Recall Anchor`) | **"Bán xe, bán đất: ai ký hợp đồng thì đúng người đó chuyển tiền, ghi rõ biển số và ngày hợp đồng — lệch tên là dừng ký ngay!"** |
| Thời lượng mục tiêu | `~315s` (~5p15s) |
| Nhân vật trung tâm (đào sâu hoàn cảnh) | **Anh Minh** (`anh_hai` / `Orus`) – chủ tiệm điện lạnh 39t, bán chiếc xe máy tay ga `45 triệu` |
| Nhân vật đối trọng / Kẻ thao túng | **Chị Thảo** (`chi_hai` / `Sulafat`) · **Nam** (`thang_tun` / `Achird`) · **Kẻ đứng giữa (`EP08`)** (`chu_no` / `Fenrir`) · **Long** (`ke_ngot_ngao_nam` / `Algieba`) · **Người mua hộ nữ** (`ke_ngot_ngao_nu` / `Aoede`) · **Người phụ nữ bí ẩn (liên đới mờ Chị Hai `EP04`)** (`chi_ba` / `Kore`) · **Ngân hàng** (`chi_tu` / `Zephyr`) |
| Nguyên tắc phòng vệ cốt lõi | **2 Phải – 3 Không**: Phải trùng khớp 100% người ký và chủ TK chuyển · Phải ghi rõ mục đích/biển số/ngày HĐ · Không nhận người thứ ba chuyển hộ · Không ký khi nội dung mập mờ · Không vội tin khách chốt quá dễ |

### Tự kiểm Pre-Gate 0 (Bộ lọc `4+2`)
- [x] **Mới:** Lần đầu giải phẫu bẫy tam giác rửa dòng tiền lừa đảo ngay tại phòng công chứng thật (`VAR-MITM-02` / `VAR-COM-04`), nối liền mảnh ghép còn lại của `EP08` mà vẫn độc lập 100% với người xem mới.
- [x] **Thực dụng:** Áp dụng trực tiếp khi mua bán xe máy, ô tô, đất đai có công chứng.
- [x] **Khác biệt:** Ở `EP08`, nạn nhân bị dẫn dụ để **tự chuyển tiền đi**; ở `EP08b`, nạn nhân là **người bán nhận tiền thật + ký công chứng thật** mà vẫn kẹt cứng giữa vụ án lừa đảo.
- [x] **Có ích:** Người xem nắm trọn "2 Phải – 3 Không" và biết cách xử lý cả khi chưa ký lẫn khi đã lỡ giao tài sản.
- [x] **Dễ kể lại:** Đã nén thành đúng 1 câu neo ký ức ngắn gọn.
- [x] **An toàn:** 100% tranh 2D không logo/app/biển số/sắc phục thật; không dạy lừa (`L2`), không tư vấn pháp lý sai lệch (`L8`).

---

## 1. Nhân vật & phân tách giọng (`02_CAST/cast.json` – 10 tuyến / 10 voice độc lập, đồng bộ vũ trụ `EP08` ↔ `EP08b` ↔ `EP04`)
| Nhân vật | Key | Voice | Chỉ đạo giọng & Cầu nối vũ trụ |
| :--- | :--- | :--- | :--- |
| **Khang (`EP08` – Cú twist Hồi 3)** | `thang_tun` | **`Puck`** | Giọng hồi ức (`af="memory"`) trích nguyên câu vỡ lẽ `l29_khang` của `EP08` (*"Nó chặn mất rồi anh Đạt ơi…"*) nổ twist ngay giữa Hồi 3 (`s08a`) |
| **Anh Minh** (39t, chủ tiệm điện lạnh) | `anh_hai` | `Orus` | Nam trầm chắc, thẳng tính, đời thường *(có bản `MINH_P` + `phone` ở Hồi 5)* |
| **Chị Thảo** (36t, vợ Anh Minh) | `chi_hai` | `Sulafat` | Nữ trầm vừa, cẩn thận thực tế, bình tĩnh |
| **Nam** (28t, em họ) | `thang_tun` | **`Achird`** | Nam trẻ gọn sáng *(tách khỏi `Puck` để không trùng giọng Khang)* |
| **Kẻ đứng giữa (`EP08` & `EP04`)** (40t) | `chu_no` | **`Fenrir`** | Nam trầm đều, lịch sự lạnh *(cùng 1 voice với `EP08` và đầu dây mật cuối `EP04`)* |
| **Long (`EP08` s08 → `EP08b`)** (32t) | `ke_ngot_ngao_nam` | **`Algieba`** | Nam sáng vừa, mượt mà, lịch sự *(khớp 100% câu đầu dây lạ `l22b_long_p` lúc `12:05` ở `EP08`)* |
| **Nhân viên ngân hàng** (29t) | `chi_tu` | `Zephyr` | Nữ chuẩn mực, điềm tĩnh (`af="phone"`) |
| **Người mua hộ nữ** (31t, Hồi 5 & Kết mở) | `ke_ngot_ngao_nu` | `Aoede` | Nữ ngọt ngào lịch sự rồi chột dạ lúng túng *(`phone` khi báo động ở kết mở)* |
| **Người phụ nữ bí ẩn *(liên đới mờ Chị Hai `EP04`)*** | `chi_ba` | **`Kore`** | Nữ 35t sắc lạnh, kiệm lời tối đa *(giấu mặt 100%, chỉ lộ thoáng tóc bob đen & tay áo xanh ngọc lục bảo trầm gợi nhớ Chị Hai vụ vé 300 triệu)* |
| **Người Bóc Trần** | `nguoi_boc_tran` | `Charon` | Đúng 1 câu (19 từ, `< 9s`) ở thẻ `NHỚ KỸ` |

---

## 2. Lời thoại chi tiết (42 câu · ≤ 24 từ/câu · ~136 từ/phút)

### HOOK – MÔ-TÍP MÀU SẮC `12:05` (CHƯA LỘ TÊN) & CÚ GỌI XÁC MINH DÒNG TIỀN 45 TRIỆU
**`s00a_pulse_1205` · `c00a`** – *(Nhịp câm + SFX điện ảnh ~2.5s, giữ kín hoàn toàn tên Khang để giấu twist cho Hồi 3!)* **Khung chia đôi liên đới màu sắc hài hòa với `EP08 c09`:** Nửa trái chỉ thấy thoáng **ngón tay trong bóng áo xanh navy đậm** bấm chuyển tiền tỏa dải sáng **`cyan-amber`** quét sang nửa phải — làm bừng sáng màn hình nhận `+45.000.000đ` trên tay Anh Minh ngay cạnh bìa hợp đồng đỏ! Tiếng `typing` → `message_send` → `bank_ting`. *(Bong bóng: "BIẾN ĐỘNG SỐ DƯ · 12:05: +45.000.000đ · Đã vào tài khoản · Công chứng xong" · `TIỀN THẬT ĐÃ NỔI`)*.

**`s00b_hook_call` · `c00`** – Chớp trắng! Chiều hai ngày sau, phòng khách nhà Anh Minh. *(Bong bóng: "XÁC MINH DÒNG TIỀN · NGÂN HÀNG: Đơn trình báo vụ lừa 45.000.000đ · Chảy thẳng vào TK này" · `YÊU CẦU XÁC MINH`)*.
- `l01_bank_p` **NGÂN HÀNG** *(điện thoại)*: Chào anh Minh. Có đơn trình báo vụ lừa bốn lăm triệu, tiền chảy thẳng vô tài khoản anh.
- `l02_minh` **ANH MINH**: Khoan chị! Bốn lăm triệu đó khách mua xe máy chuyển tại phòng công chứng mà! Tôi giao xe rồi!
- `l03_bank_p` **NGÂN HÀNG** *(điện thoại)*: Nhưng người chuyển báo bị lừa, không mua xe của anh. Nội dung cũng không ghi mua xe.

**`s01_hook_freeze` · `c01`** – Chớp trắng! Cận cảnh Anh Minh sững người giữa tờ hợp đồng công chứng bìa đỏ và màn hình sao kê `+45.000.000đ` lúc `12:05`. *(Bong bóng: "SAO KÊ NGÂN HÀNG · 12:05: +45.000.000đ · Từ: TÊN LẠ · ND: Chuyen tien" · `TIỀN TỪ VỤ LỪA?`)*.

### HỒI 1 – BA HÔM TRƯỚC: KHÁCH CHỐT KHÔNG MẶC CẢ
**`s02_sell_bike_cafe` · `c02`** – Quán cà phê nhỏ sáng nắng gần tiệm điện lạnh của Anh Minh, bên lề đậu chiếc **xe máy tay ga màu xám bạc** sạch sẽ (không logo/biển số), trên bàn có **hai ly trà đá**.
- `l04_nam` **NAM**: Chiếc tay ga anh rao bốn lăm triệu cả tuần, thợ trả toàn bốn chục. Chắc bớt chút mới trôi.
- `l05_minh` **ANH MINH**: Đâu có, sáng nay anh Hùng hỏi mua. Coi hình xong chốt thẳng bốn lăm triệu, hông trả giá một đồng!
- `l06_thao` **CHỊ THẢO**: Nghe dễ quá cũng lạ nha anh. Sao ổng hông qua coi máy móc trực tiếp?
- `l07_minh` **ANH MINH**: Ổng công tác xa, thấy xe giữ kỹ hợp màu nên chốt. Tiền nổi vô tài khoản anh mới ký công chứng, sợ gì!
- `l08_nam` **NAM**: Gặp khách sộp vậy sướng ha! Ít bữa em bán chiếc xe máy cũ chắc cũng lên nhóm rao thử.

**`s03_buyer_chat_dark` · `c03`** – Đúng căn phòng tối ánh xanh lạnh với **hai chiếc điện thoại song song** từ `EP08`: bàn tay kẻ đứng giữa gõ tin chốt mua chiếc xe máy `45 triệu`. *(Bong bóng: "KHÁCH MUA · ANH HÙNG: Chốt 45tr · Nhờ em họ Long đứng tên mua hộ" · `MỒI CHỐT NHANH`)*.
- `l09_buyer_msg` **KHÁCH MUA** *(tin nhắn)*: Anh bận công tác xa chưa về kịp, nên nhờ em họ tên Long ra công chứng đứng tên mua hộ.
- `l10_buyer_msg` **KHÁCH MUA** *(tin nhắn)*: Chú yên tâm. Bao giờ tiền nổi đủ bốn lăm triệu trong tài khoản rồi hẵng ký giao xe!

### HỒI 2 – TRƯA HÔM SAU (`12:05`): TIỀN ĐÃ NỔI TRONG TÀI KHOẢN
**`s04_notary_meeting` · `c04`** – Phòng công chứng sáng trưa **đông đúc người chờ** (`amb: crowd`). Minh & Thảo ngồi bên trái; Long (áo sơ mi trắng gọn gàng) ngồi bên phải cùng bìa hợp đồng đỏ.
- `l11_long` **LONG**: Em là Long, em họ anh Hùng. Hồ sơ em nộp quầy rồi, chờ gọi tên thôi anh chị.
- `l12_thao` **CHỊ THẢO**: Rồi chút nữa bên anh Hùng chuyển thẳng qua luôn hả cậu?
- `l13_long` **LONG**: Dạ ảnh đang bấm chuyển đó chị, tiền vô là mình vô ký gọn.

**`s05_money_arrives_mismatch` · `c05`** – Đúng **`12:05 trưa`** giữa sảnh công chứng ồn ào, tiếng *ting ting* vang lên! Anh Minh thấy đủ `45 triệu` là yên tâm kiệm lời ngay; Chị Thảo chỉ liếc thoáng nửa giây găm **1 cú hook nghi ngờ cực nhẹ** (đúng cái tên **Khang**!). *(Bong bóng trung tính: "NGÂN HÀNG CỦA MINH · 12:05: +45.000.000đ · Đã vào tài khoản" · `ĐÃ NHẬN TIỀN`)*.
- `l14_minh` **ANH MINH**: Đủ bốn lăm triệu rồi. Ra ký đi em.
- `l15_thao` **CHỊ THẢO**: Ủa… người gửi sao tên Khang lạ vậy anh?
- `l16_long` **LONG**: Kế toán bên công ty ảnh chuyển đó chị. Tới số mình vô ký rồi.

**`s06_sign_handover` · `c06`** – Trước sân phòng công chứng nắng trưa. Anh Minh trao chìa khóa, Long vui vẻ nổ máy lái chiếc xe máy tay ga màu xám bạc đi. *(Bong bóng: "HỢP ĐỒNG CÔNG CHỨNG: Bên mua: Long · Đã nhận đủ 45.000.000đ · Đã giao xe" · `XONG TRÊN GIẤY`)*.
- `l17_long` **LONG**: Cảm ơn anh chị nha. Em chạy xe về nhà anh Hùng đây!

### HỒI 3 – HAI NGÀY SAU: NICK ĐÃ XÓA, XE ĐÃ SANG TAY
**`s07_call_blocked` · `c07`** – Phòng khách nhà Anh Minh (nối sau Hook). Minh gọi lại Long chỉ nghe tút tút thuê bao, mở tin nhắn thì nick Hùng đã biến mất. *(Bong bóng: "LIÊN HỆ NGƯỜI MUA: Nick khách mua đã xóa · Số của Long tắt máy" · `MẤT DẤU CẢ HAI`)*.
- `l18_minh` **ANH MINH**: Trời đất ơi! Nick ông Hùng xóa rồi! Gọi số thằng Long cũng tắt máy luôn!
- `l19_thao` **CHỊ THẢO**: Lúc ký em thoáng thấy tên Khang lạ mà tưởng tiền vô là xong… Người đó là ai vậy anh?
- `l20_minh` **ANH MINH**: Bên công an nói anh Khang bị giả sếp nhờ mua quà kỷ niệm cho vợ, lừa chuyển bốn lăm triệu vô đúng máy mình!

**`s08a_ep08_twist` · `c08a`** – **CÚ NỔ TWIST HỒI 3 (`flash_white` + `impact`):** Hồi ức đập thẳng vào thị giác & thính giác của người xem `EP08` — hiện rõ **gương mặt Khang (áo xanh navy đậm tái mặt) & Anh Đạt ở bàn xưởng gỗ (`EP08 c12`)** phủ viền hồi ức cùng câu thoại đinh của Khang (`Puck`, `af="memory"`). *(Bong bóng: "12:05 · MẢNH GHÉP CÒN LẠI: Khang (-45.000.000đ)  →  Chảy thẳng vào tài khoản Anh Minh" · `CÙNG MỘT VỤ LỪA`)*.
- `l20b_khang_echo` **KHANG (`EP08`)** *(hồi ức)*: Nó chặn mất rồi anh Đạt ơi… Bốn mươi lăm triệu em vừa chuyển qua tài khoản lạ rồi!

**`s08b_paper_trap` · `c08`** – Cận cảnh bàn phòng khách: hợp đồng công chứng bìa đỏ (bên mua: Long) đặt cạnh tờ sao kê ngân hàng (`12:05` – người chuyển: Khang, nội dung trống) — **toàn bộ thế "kế trùng kế" vỡ òa trọn vẹn**.
- `l21_thao` **CHỊ THẢO**: Hợp đồng bán xe cho Long ghi nhận đủ, còn tiền lại từ anh Khang bị lừa!
- `l22_minh` **ANH MINH**: Nội dung chỉ ghi chuyển tiền, không biển số, không ngày hợp đồng… Cả hai đều là nạn nhân!

### HỒI 4 – LỘ DIỆN CƠ CHẾ: TAM GIÁC LỆCH DÒNG TIỀN & XỬ LÝ ĐÚNG LUẬT
**`s09_triangle_reveal` · `c09`** – Cắt chớp trắng sang căn phòng tối ánh xanh lạnh với **hai chiếc điện thoại song song** (cùng bối cảnh & giọng **Kẻ đứng giữa** ở `EP08`). *(Bong bóng: "BẪY TAM GIÁC · 12:05 TRƯA: Khang chuyển 45tr → TK Minh · Long công chứng lấy xe máy" · `RỬA TIỀN SẠCH`)*.
- `l23_buyer_room` **KẺ ĐỨNG GIỮA**: Đầu kia lừa thằng Khang đẩy bốn lăm triệu. Đầu này cho Long công chứng hốt chiếc xe máy.
- `l24_buyer_room` **KẺ ĐỨNG GIỮA**: Tiền bẩn đổi thẳng ra xe thật trong một buổi trưa. Hai nạn nhân tự giải trình với nhau!

**`s10_response_action` · `c10`** – Sáng hôm sau tại nhà Anh Minh: Anh Minh sốt ruột định rút `45 triệu` cất thì Chị Thảo kịp cản lại, cả hai gom đủ tập chứng từ gốc đi trình báo.
- `l25_minh` **ANH MINH**: Hay anh rút bốn lăm triệu ra cất trước, chừng nào kiếm lại được xe rồi mới tính?
- `l26_thao` **CHỊ THẢO**: Khoan! Đừng rút hay chuyển đi đâu! Tiền đang xác minh vụ án mà tự ý tẩu tán còn vướng rắc rối nặng hơn đó!
- `l27_minh` **ANH MINH**: Vậy giữ nguyên tiền trong tài khoản, gom hợp đồng, sao kê với tin nhắn trình báo công an liền!

### HỒI 5 – HAI TUẦN SAU: NGUYÊN TẮC HAI PHẢI, BA KHÔNG
**`s11_nam_calls_notary` · `c11`** – Hai tuần sau, sảnh phòng công chứng sáng nắng đông người. Nam đứng gọi điện khoe Anh Minh; phía xa sau lưng là một người phụ nữ lịch sự cầm bìa hợp đồng đỏ chờ sẵn.
- `l28_nam` **NAM**: Alo anh Minh! Em đang công chứng bán xe máy. Khách chốt nhanh, nhờ người thân đứng tên mua hộ!
- `l29_minh_p` **ANH MINH** *(điện thoại)*: Khoan ký! Dừng lại liền! Anh mới dính bẫy tam giác kẹt cứng bốn lăm triệu đây nè!

**`s12_minh_warns_rule` · `c12`** – Tiệm điện lạnh của Anh Minh: Minh nắm chặt điện thoại dặn nhanh gọn nguyên tắc 2 Phải. *(Bong bóng: "NGUYÊN TẮC 2 PHẢI: 1. Ai ký HĐ, người đó chuyển · 2. Ghi tên, mua xe, BSX, ngày HĐ" · `CHẶN BẪY NGAY`)*.
- `l30_minh` **ANH MINH**: Ai ký hợp đồng thì chính người đó chuyển tiền. Tuyệt đối không nhận tài khoản người thứ ba chuyển giùm!
- `l31_minh` **ANH MINH**: Nội dung ghi rõ họ tên, mua xe, biển số và ngày hợp đồng. Lệch tên hay thiếu là dừng ký!

**`s13_nam_tests_proxy` · `c13`** – Bố cục cắt ngang Trái (Nam bình tĩnh) – Phải (Người mua hộ nữ) tại bàn phòng công chứng.
- `l32_nam` **NAM**: Chị ơi, hợp đồng tên chị nên chị dùng đúng tài khoản tên chị chuyển, ghi rõ biển số với ngày hợp đồng nha!
- `l33_proxy_nu` **NGƯỜI MUA HỘ**: Ủa… chồng chị ở xa chuyển giùm cho nhanh, tiền vô rồi cần gì rắc rối?
- `l34_nam` **NAM**: Không được chị. Lệch tên hay mập mờ em không ký, tiền lỡ vô em cũng ra ngân hàng hoàn lại.

**`s14_scammer_flees` · `c14`** – Chớp trắng! Người mua hộ nữ khựng nụ cười, vơ vội hồ sơ đi thẳng ra cửa; Nam đứng thở phào nhẹ nhõm.
- `l35_proxy_nu` **NGƯỜI MUA HỘ**: À… thôi để chị ra ngoài gọi hỏi lại chồng chút nha!
- `l36_nam` **NAM**: Đi mất tiêu rồi! May gọi kịp cho anh Minh… suýt chút nữa mất trắng chiếc xe!

**`s15_outro_still` · `c15`** – Nhịp lặng ngắn tại tiệm Anh Minh dẫn vào thẻ kết.

### THẺ NHỚ KỸ *(DƯỚI 10 GIÂY)*
**`s16_red_flags`** *(nền `EP01b/scene18.jpg`)*
- `l37_narr` **NGƯỜI BÓC TRẦN**: Tiền nổi rồi vẫn mất nếu lệch tên. Ai ký hợp đồng người đó chuyển, ghi rõ mục đích.

### KẾT MỞ ĐƯỜNG DÂY NGẦM *(CỘC GỌN SẮC LẠNH · HỘI TỤ MẮT XÍCH `EP08` & `EP08b` · LIÊN ĐỚI MỜ CHỊ HAI `EP04`)*
**`s17a_syndicate_grid` · `c16a`** – Đêm mưa. **Khung hình chia lưới 4 ô tối ánh xanh lạnh** hội tụ tất cả nhân vật mờ ám của cả hai tập đang liên lạc cùng lúc: (1) Phòng tối 2 điện thoại của **Kẻ đứng giữa** (`Fenrir`) & **Đàn em kỹ thuật** (`EP08`, hoodie xám đậm, ẩn mặt 100%); (2) Bóng tối cạnh xe tay ga xám bạc & bìa đỏ của **Long** (`Algieba`); (3) **Người mua hộ nữ** (`Aoede`) dưới hiên mưa; (4) Bàn tay lộ thoáng cổ tay **áo lụa xanh ngọc lục bảo trầm** cầm chiếc điện thoại đen mảnh (gợi mơ hồ tới Chị Hai ở `EP04`, không lộ mặt).
- `l38a_ke_p` **KẺ ĐỨNG GIỮA (`EP08`)** *(điện thoại)*: Bên ông Đạt với Khang… công an vào cuộc.
- `l38b_long_p` **LONG (`EP08b`)** *(điện thoại)*: Chiếc tay ga đẩy xong. Số hủy sạch.
- `l38c_proxy_p` **NGƯỜI MUA HỘ (`EP08b`)** *(điện thoại)*: Khu này động. Chủ xe đòi chính chủ chuyển.

**`s17b_boss_order` · `c16b`** – **TUYỆT ĐỐI KHÔNG THẤY RÕ MẶT:** Quay từ phía sau vai / bóng tối sâu trong khoang sau chiếc xe đen đêm mưa — chỉ lộ đường viền **tóc đen ngắn ngang vai uốn cụp** cùng cổ áo/tay áo **lụa xanh ngọc lục bảo trầm** (hơi liên đới Chị Hai vụ mua vé 300 triệu ở `EP04` mà không khẳng định rõ mặt) cầm chiếc điện thoại phụ màu đen mảnh, buông đúng 3 nhịp lạnh băng:
- `l39_boss_nu` **NGƯỜI PHỤ NỮ BÍ ẨN** *(voice `Kore`)*: Bỏ xe. Dời vùng. Sang kèo đất.

**`s18_black_cut` · `c17`** – **IMPACT TRẦM + CẮT ĐEN ĐỘT NGỘT!**

**`s19_disclaimer`** – LƯU Ý.

---

## 3. Thẻ DẤU HIỆU NHẬN BIẾT & NGUYÊN TẮC 2 PHẢI – 3 KHÔNG
1. **PHẢI TRÙNG KHỚP 100%:** Ai đứng tên ký hợp đồng mua bán thì chính chủ tài khoản đó chuyển tiền.
2. **PHẢI GHI RÕ NỘI DUNG:** Họ tên người mua + thanh toán mua xe + biển số + theo hợp đồng ngày ký.
3. **KHÔNG NHẬN NGƯỜI THỨ BA CHUYỂN HỘ:** Từ chối mọi lý do tài khoản người thân hay công ty chuyển giùm.
4. **LỆCH TÊN HAY MẬP MỜ LÀ DỪNG KÝ NGAY:** Tiền đã lỡ vào thì không giao xe và phối hợp ngân hàng hoàn trả.
5. **CẢNH GIÁC KHÁCH CHỐT QUÁ DỄ:** Không mặc cả, né gặp mặt, nhờ người khác đứng tên mua hộ.
- **Việc nên làm ngay:** Nếu đã lỡ giao tài sản và nhận báo tiền từ vụ lừa khác, giữ nguyên tiền trong tài khoản, gom hợp đồng, sao kê và tin nhắn trình báo công an ngay.

## 4. Tự kiểm “Không dạy lừa”
- [x] Không có câu thoại kẻ lừa đủ chi tiết kỹ thuật để người xem chép lại làm kịch bản lừa thật.
- [x] Không hướng dẫn cách kết nối hai đầu vụ lừa, cách tìm tài khoản mồi hay cách tiêu thụ xe.
- [x] Phần bóc trần (`s09`) chỉ nêu gọn cấu trúc lệch dòng tiền giữa hai nạn nhân thật để khán giả nhận diện và chặn bẫy ngay tại bàn công chứng.
