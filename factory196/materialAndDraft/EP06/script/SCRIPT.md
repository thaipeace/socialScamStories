# EP06 – BA TRIỆU TÁM TRÊN MÀN HÌNH *(Bản kịch hóa điện ảnh – v2-draft)*

- **Mã tập:** `EP06` · **Slug:** `BaTrieuTamTrenManHinh`
- **Họ kịch bản:** `JOB-TASK` – Ứng dụng mua hàng hộ **"Bạn Thân 4.0"** (mua hàng giùm cho người bận không có thời gian, nhận hoa hồng theo đơn, tự nhận vận hành từ năm 2018): cấp sẵn `40.000đ` làm thử không tốn vốn + **nhóm chat báo thành quả cảm ơn rối rít** → **cả nhóm chia vai chỉ vẽ & khuyến khích** "bù phần thiếu" từ `10.000đ` lên vài trăm ngàn khiến nạn nhân không nhận ra mình đã chuyển `2.140.000đ` tiền thật, trong khi màn hình treo `3.850.000đ` rồi vừa bấm rút liền bị đòi bù `2.900.000đ` trước 23h giữa lúc cả nhóm lẫn hỗ trợ vẫn xúm vô hối nạp tiếp → **Người bạn cũ giấu mặt** cực kiệm lời, nói như đã biết chuyện, chốt dứt khoát giúp Nam dừng tay ngay lập tức → **Kết mở đường dây ngầm:** Màn hình vi tính hiện danh sách khách, câu buông gọn *"Haiz… đúng là trái đất tròn."* và con trỏ chuột rê thẳng vào nút **`"Chốt khách"`**.
- **Định dạng:** `16:9` (`1920x1080 @ 30fps`) · **Thời lượng ước tính:** `~287.4s` (`04:47` · 16 cảnh · 30 câu thoại · 568 từ · câu dài nhất `25 từ`)
- **Tỷ lệ:** **97% kịch tâm lý – điện ảnh / 3% Người Bóc Trần (`< 9 giây`)**
- **Nguồn sự thật của timeline:** [`source/build_draft.py`](../source/build_draft.py) → sinh [`episode.json`](../episode.json).

## Nhân vật & giọng (`02_CAST/cast.json` – 8 tuyến / 8 voice độc lập)
| Nhân vật | Key | Voice | Chỉ đạo giọng |
|---|---|---|---|
| **Nam** (32t, chồng Thảo) | `anh_hai` | `Orus` | Nam trầm ấm, thật thà, chăm làm, rất đời thực |
| **Thảo** (31t, vợ Nam) | `chi_hai` | `Sulafat` | Nữ trầm vừa, cực kiệm lời, thực tế, không chì chiết chồng |
| **Vy Điều Phối** | `ke_ngot_ngao_nu` | `Aoede` | Nữ trẻ ngọt ngào, chỉ 1 câu chào mở đầu ở Hồi 1 (`af: phone`) |
| **Chị Loan** (thành viên nhóm) | `co_hanh` | `Despina` | Nữ ~42t miền Nam thân tình, hồ hởi cảm ơn rối rít & nhiệt tình chỉ vẽ người mới (`af: phone`) |
| **Tuấn** (thành viên nhóm) | `thang_tun` | `Puck` | Nam trẻ 24t sáng, sôi nổi báo thành quả & cổ vũ Nam chốt đơn lớn (`af: phone`) |
| **Bộ phận Hỗ trợ đối soát** | `chu_no` | `Fenrir` | Nam trầm đều, lạnh băng như máy trả lời khi chặn rút tiền (`af: phone`) |
| **Người bạn cũ (giấu mặt)** | `ong_bay` | `Algenib` | Nam 35t trầm khàn nhẹ, **cực kiệm lời, nói như đã biết chuyện, dứt khoát có trọng lượng; cố ý không lộ mặt & không nêu tên** |
| **Người Bóc Trần** | `nguoi_boc_tran` | `Charon` | Đúng 1 câu (19 từ, `< 9s`) ở thẻ `NHỚ KỸ` |

---

## HOOK – CON SỐ ĐỨNG YÊN & CÚ CHẶN RÚT TIỀN
**`s00_hook_blocked` · `c00`** – 22:30 Đêm. Phòng khách nhà Nam. *(Bong bóng: "VÍ BẠN THÂN 4.0: Số dư: 3.850.000đ · Chưa đủ điều kiện đối soát để rút tiền")*.
- `l01_nam` **NAM**: Alo, trong ví tôi đang có ba triệu tám, sao bấm rút về ngân hàng lại khóa?
- `l02_ht` **HỖ TRỢ** *(điện thoại)*: Tài khoản anh còn treo một đơn đối soát cuối. Anh bù thêm hai triệu chín là hệ thống giải ngân toàn bộ.
- `l03_nam` **NAM**: Tiền tôi nằm sẵn trỏng gần bốn triệu rồi, sao không trừ thẳng mà bắt nạp thêm?!

**`s01_hook_two_screens` · `c01`** – Chớp trắng sang cận gương mặt sững sờ của Nam trước dòng hối thúc trên màn hình. *(Bong bóng: "HỆ THỐNG BẠN THÂN 4.0: Chỉ còn 01 bước cuối để nhận toàn bộ 6.750.000đ gốc và hoa hồng")*.
- `l04_ht` **HỖ TRỢ** *(điện thoại)*: Quy trình tự động không trừ cấn anh nha. Quá hai mươi ba giờ chưa xong đơn là ví đóng băng.
- *(Cuộc gọi kết thúc. Ngón tay Nam khựng trên màn hình).*

## HỒI 1 – ỨNG DỤNG "BẠN THÂN 4.0" & NHÓM CHAT CẢM ƠN RỐI RÍT
**`s02_rainy_shift_cut` · `c02`** – Ba tối trước. Mưa dầm ngoài hiên, Nam lau áo mưa bước vào nhà.
- `l05_nam` **NAM**: Mưa dầm cả tuần nay kho cắt hết ca tối, tháng này chắc hụt tiền phụ em đóng học cho con rồi.
- `l06_thao` **THẢO**: Tháng nào hụt mình gói ghém tháng đó, mưa gió anh chạy ráng ngoài đường nguy hiểm lắm.

**`s03_first_free_order` · `c03`** – Nam ngồi ghế gỗ mở ứng dụng **"Bạn Thân 4.0"** giới thiệu ngắn gọn, thuyết phục về mô hình mua hàng giùm cho người không có thời gian *(Bong bóng cài chi tiết gốc: "BẠN THÂN 4.0 · TỪ NĂM 2018: Ứng dụng uy tín mua hàng giùm cho người không có thời gian · Cấp sẵn 40.000đ làm thử")*.
- `l07_vy` **ĐIỀU PHỐI** *(tin nhắn thoại chào mừng)*: Chào anh vô Bạn Thân bốn chấm không, app mua hàng giùm người bận. Ví cấp sẵn bốn chục ngàn, anh thử đơn đầu nha.
- *(Ting! Bong bóng: "VÍ BẠN THÂN 4.0: Đơn mua hộ 30.000đ hoàn thành · Cộng gốc & hoa hồng -> Số dư: 45.000đ")*.
- `l08_nam` **NAM**: Ủa… làm thử có một đơn mà nhảy lên bốn lăm ngàn liền nè em.
- `l09_thao` **THẢO**: Làm cái đó có bắt mình bỏ tiền túi ra hông anh?
- `l10_nam` **NAM**: Đâu có, app mua hàng giùm cho người không có thời gian, chạy từ năm hai ngàn mười tám, cho sẵn tiền thử mà.

**`s03b_group_buzz` · `c03b`** – Nam mở **Nhóm Bạn Thân 4.0**: tin nhắn và tiếng báo thưởng nổ liên tục, mọi người báo thành quả cảm ơn rối rít *(4 bong bóng nối tiếp từ Chị Loan, Hoa, Tuấn, Minh)*:
- `l10b_loan` **CHỊ LOAN (NHÓM)** *(tin nhắn thoại)*: Em mới xong ba đơn chiều nay, hoa hồng cộng vô ví liền. Cảm ơn nhóm mình nhiều lắm luôn ạ!
- `l10c_tuan` **TUẤN (NHÓM)** *(tin nhắn thoại)*: Trời mưa ở nhà mua hộ khách bận mà đỡ cực ghê. Em vừa nhận hoa hồng xong, cảm ơn cả nhà nha!

## HỒI 2 – CẢ NHÓM CHỈ VẼ & CON SỐ NHẢY MÚA
**`s04_ten_thousand_bait` · `c04`** – Nửa tiếng sau. Đơn mua hộ thứ hai trị giá `55.000đ`, báo thiếu đúng `10.000đ`. Nam nhắn hỏi thẳng lên nhóm chat, lập tức các bạn trong nhóm xúm vô chỉ vẽ thân tình thay cho điều phối.
- `l11_nam` **NAM**: Ủa cả nhà ơi, sao đơn mua hộ thứ hai này báo ví em thiếu mười ngàn vậy ta?
- *(Bong bóng `MINH · NHÓM BẠN THÂN 4.0`: "Đúng rồi anh, mới vô em cũng hỏi y chang. Bù 10 ngàn xong ví nhảy lên 65 ngàn liền đó!")*
- `l12_loan` **CHỊ LOAN (NHÓM)** *(tin nhắn thoại)*: Bình thường đó anh mới ơi! Bù đúng mười ngàn phần thiếu thôi, xong đơn tiền hàng với hoa hồng cộng vô ví liền.
- *(Nam chặc lưỡi chuyển 10.000đ. Số dư nhảy lên `65.000đ` kèm sổ lịch sử cộng trừ rõ từng dòng).*
- `l13_nam` **NAM**: Ờ… sổ giao dịch ghi cộng trừ rõ ràng thiệt.

**`s05_escalating_topups` · `c05`** – Hai tối kế tiếp: không khí nhóm chat liên tục chúc mừng, khuyến khích chốt đơn lớn để mỗi lần chỉ "bù phần thiếu" nên cảm giác bỏ ra rất ít *(Bong bóng `NHÓM BẠN THÂN 4.0` chúc mừng lên bậc khách quen & `CHỊ LOAN` cổ vũ gần chạm mốc 4 triệu)*.
- `l14_tuan` **TUẤN (NHÓM)** *(tin nhắn thoại)*: Ví anh có sẵn triệu rưỡi rồi, bù thêm bốn trăm rưỡi thôi. Em mới chốt xong, hoa hồng ngon lắm anh!

**`s06_wife_sharp_question` · `c06`** – Bàn ăn buổi tối. Nam hào hứng xoay màn hình hiện `3.850.000đ` khoe vợ.
- `l15_nam` **NAM**: Em nhìn nè, ba tối nay anh gom hoa hồng lên được gần bốn triệu rồi đó!
- `l16_thao` **THẢO**: Nhưng anh bấm rút thử tiền về ngân hàng mình lần nào chưa?
- `l17_nam` **NAM**: Mục rút tiền với số tài khoản anh nằm sẵn đây nè. Làm nốt đợt tối nay cho chẵn rồi anh rút một lượt luôn.

## HỒI 3 – TIỀN THẬT ĐI RA & CON SỐ ĐỨNG YÊN
**`s07_real_vs_screen` · `c07`** – Hai tiếng sau bữa cơm (22:35 Đêm, nối liền cú bấm rút bị đòi bù `2.900.000đ` ở Mở đầu). Nam mở ứng dụng ngân hàng thật để kiểm tra thì khựng người thấy toàn bộ các khoản tiền thật đã trừ đi (`-10.000đ · -180.000đ · -450.000đ · -1.500.000đ = Tổng -2.140.000đ`) mà chưa hề có một đồng nào chảy về. Trong khi đó, nhóm chat lẫn hỗ trợ **không hề khóa gì cả** — trái lại, Chị Loan trong nhóm vẫn xúm vô hối nạp nốt trước 23h *(Bong bóng `CHỊ LOAN · NHÓM BẠN THÂN 4.0`: "Ráng bù nốt 2 triệu 9 trước 23h đi anh Nam ơi! Bữa em cũng kẹt bước này, xong rút cả cục về liền!")*:
- `l18_nam` **NAM**: Vừa bấm rút đã đòi bù thêm hai triệu chín… Mình chuyển đi hơn hai triệu rồi, mà cả nhóm vẫn chỉ hối nạp tiếp.
- `l19_ht` **HỖ TRỢ** *(điện thoại)*: Còn hai mươi phút nữa tới hai mươi ba giờ anh Nam nha. Xong đơn này hệ thống giải ngân liền sáu triệu bảy.
- *(Nhịp câm: Nam nhìn ngón cái của mình rồi dứt khoát tắt ứng dụng ngân hàng, không chuyển thêm một đồng nào).*

## HỒI 4 – NGƯỜI BẠN CŨ GIẤU MẶT & TÊN MIỀN SÁU NGÀY TUỔI
**`s08_porch_call_friend` · `c08`** – Ngoài hiên nhà sau cơn mưa đêm, Nam ngồi một mình bấm gọi người bạn cũ.
- `l20_nam` **NAM**: Ê, còn thức hông mày? Tao mới gửi đường dẫn trang Bạn Thân bốn chấm không, coi giùm tao cái.

**`s09_faceless_it_lookup` · `c09`** – Căn phòng tối ở một nơi khác (**cố ý không lộ mặt, không giới thiệu danh tính**: góc máy chỉ lấy đôi bàn tay người đàn ông đặt điện thoại cạnh laptop sáng xanh). *(Bong bóng: "TRA CỨU ĐĂNG KÝ TÊN MIỀN: Tự nhận trên trang: Từ năm 2018 | Ngày đăng ký thật: Thứ Ba tuần trước")*. **Người bạn cũ cực kiệm lời, phản ứng như đã biết rõ chuyện từ trước, chốt một câu dứt khoát đầy trọng lượng:**
- `l21_it` **BẠN CŨ**: Tên miền mới mở thứ Ba tuần trước. Biết ngay mà.
- `l22_nam` **NAM** *(loa điện thoại)*: Nhưng ví tao vẫn hiện nguyên ba triệu tám mà mày…
- `l23_it` **BẠN CŨ**: Số đó tụi nó tự gõ. Bỏ ngay đi, chuyển nữa là mất nữa.
- *(Tút! Cuộc gọi dứt gọn, không thêm một lời giải thích dài dòng).*

## HỒI 5 – TẮT MÀN HÌNH & GIỮ LẠI TIỀN THẬT
**`s10_turn_off_screen` · `c10`** – Phòng khách nhà Nam. Thảo mang ly nước ấm đặt xuống bàn cạnh chồng.
- `l25_nam` **NAM**: Anh mất hai triệu mốt tiền thiệt rồi Thảo ơi… Tưởng bù mỗi lần vài trăm lẻ, cộng lại đứt mấy ngày công.
- `l26_thao` **THẢO**: Dừng ngay khúc này là may lắm rồi anh. Chứ nãy tiếc của mà nạp thêm ba triệu nữa là lún sâu luôn đó.
- `l27_nam` **NAM**: Ừ… Mai anh đem sao kê trình báo công an, rồi dặn anh em dưới kho né cái trò bù tiền này ra.
- *(Nam bấm tắt màn hình, đặt úp chiếc điện thoại xuống mặt bàn gỗ).*

## THẺ NHỚ KỸ *(DƯỚI 10 GIÂY)*
**`s11_red_flags`** *(nền `EP01b/scene18.jpg`)*
- `l28_narr` **NGƯỜI BÓC TRẦN**: Số dư trên trang lạ là chữ họ tự gõ, còn tiền rời ngân hàng bạn mới mất thật.

## KẾT MỞ ĐƯỜNG DÂY NGẦM – MÀN HÌNH DANH SÁCH & NÚT "CHỐT KHÁCH"
**`s12_unseen_tracker_coda` · `c11`** – Căn phòng tối của người bạn cũ (vẫn chỉ thấy bóng vai khuất tối và bàn tay đặt trên chuột máy tính trước màn hình vi tính phát sáng). Màn hình vi tính hiện một **danh sách khách** (`#408 · Đang theo đơn | #409 · Chờ đối soát | #410 · Nam`). Không gọi điện, không giải thích thêm bất kỳ thông tin nào:
- `l29_it_coda` **BẠN CŨ**: Haiz… đúng là trái đất tròn.
- *(Tiếng nhịp tim trầm dội lên — con trỏ chuột rê thẳng vào nút đỏ **`[  CHỐT KHÁCH  ]`**).*
- **`s13_black_cut` · `c12`** – **IMPACT + CẮT ĐEN ĐỘT NGỘT!**

**`s14_disclaimer`** – LƯU Ý.
