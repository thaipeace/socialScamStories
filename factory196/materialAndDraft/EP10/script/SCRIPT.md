# KỊCH BẢN PHIM DÀI 16:9 (4–5+ PHÚT) – EP10: Giám đốc 100 Agent – Suất cuối giảm 80%

> Khung ngang `16:9` (`1920x1080 @ 30fps`) · **21 cảnh (`s00`–`s18`, gồm `s13b`, `s16a`/`s16b`) · 44 câu thoại (`v5-level2-abc-staging`) · ~5 phút 50 giây – 6 phút 05 giây (đạt chuẩn `240s+`)** · Tỷ lệ **~97.5% kịch đời thực / ~2.5% Người Bóc Trần (`1 câu, 23 từ`)** theo [LONG_FORMAT_196_SPEC.md](../../../../00_HARNESS_GUIDELINES/LONG_FORMAT_196_SPEC.md) và [STORY_AND_PRODUCTION_HARNESS.md](../../../../00_HARNESS_GUIDELINES/STORY_AND_PRODUCTION_HARNESS.md).
> Nguồn sự thật của timeline: [`source/build_draft.py`](../source/build_draft.py) → sinh [`episode.json`](../episode.json).
> Mọi tên người, doanh nghiệp, ứng dụng, số điện thoại, số tài khoản và số liệu trong kịch bản đều là **hư cấu hoặc chung chung**.

---

## 0. Thẻ tập phim & Khung Thư viện Cảnh giác *(theo [VIGILANCE_LIBRARY_FRAMEWORK.md](../../../../00_HARNESS_GUIDELINES/VIGILANCE_LIBRARY_FRAMEWORK.md))*

| Mục | Nội dung |
| :--- | :--- |
| **Mã tập / Slug** | `EP10` (`factory196`) · `GiamDoc100Agent` |
| **Góc quan sát (Format `A–F`)** | **`A`** – Giải phẫu toàn bộ cơ chế phễu công nghệ AI 2026 *(FOMO tụt hậu AI → Hội nghị neo giá giảm 80% + chim mồi bình dân + tặng "Văn phòng ảo bay trên không gian 100 agent" → Ảo giác làm Sếp + lãi mồi thật `3 triệu` → Bật Chế độ Máy bay quay clip thả nhóm kín VIP làm cháy sạch chiến dịch + Kết mở kết nối Chị Hai & tay IT `EP06`)* |
| **Nhóm chiêu & Biến thể Lớp 1 (`VAR`)** | **`VAR-FUNNEL-01` / `VAR-AI-01`** – Phễu khóa học "Công ty một người thời AI" giảm sốc 80% trong 10 phút + chim mồi hội trường + tặng văn phòng ảo 100 AI agent sáng đèn báo lãi liên tục *(hoạt ảnh vẽ sẵn chạy ngoại tuyến)* để dụ nạp các gói "trạm máy chủ kích hoạt" |
| **Điểm dễ mắc Lớp 2 (`COND`)** | `COND-01` (tiệm gia dụng ế hàng + sợ bị làn sóng AI đào thải) · `COND-02` (tin phông bạt siêu xe, hội nghị khách sạn & giao diện 100 agent) · `COND-03` (rút thật `3 triệu` lãi mồi) · `COND-05` (đồng hồ 10 phút + "còn 3 suất cuối") · `COND-07` (sĩ diện trụ cột, giấu vợ tự xoay) · `COND-08` (say ảo giác làm *"Giám đốc 100 agent"* + thấy chị bán vải chốt trước) |
| **Giá trị ứng phó Lớp 3 (`RESP`)** | `RESP-01` (cắt lỗ ngay, không nạp `40 triệu` mở cổng) · `RESP-03` (câu hỏi gốc *"100 agent bán hàng gì, cho ai?"* + kiểm chứng pháp nhân & thử ngắt mạng kiểm tra ứng dụng lạ) · `RESP-04` (quay bằng chứng cảnh báo nhóm học viên khác dừng nạp tiền, gom sao kê trình báo công an) · `RESP-06` (chặn bẫy lừa lần hai "hội thu hồi vốn") |
| **1 câu neo ký ức (`Recall Anchor`)** | **"Khóa học giảm sốc 80% tặng văn phòng ảo 100 agent tự đẻ lãi chỉ là hoạt ảnh mồi — hỏi xem nó bán hàng gì, cho ai trước khi xuống tiền!"** |
| **Nhân vật trung tâm** | **Tuấn** (`anh_hai` / `Orus`) – 35 tuổi, chủ tiệm đồ gia dụng nhỏ đang ế hàng, ám ảnh nỗi sợ tụt hậu trong cơn bão AI |
| **Đối trọng, Tuyến thao túng & Vũ trụ Chị Hai** | **Hương** (`chi_hai` / `Sulafat`) · **Thầy Quang** (`chu_no` / `Algieba`) · **Trợ lý Khánh** (`ke_ngot_ngao_nam` / `Achird`) · **Chị Lan** (`co_hanh` / `Despina`) · **MC Hội trường** (`ke_ban_hang` / `Zephyr`) · **Chú Bảo Vệ** (`ong_bay` / `Algenib`) · **Chị Hai – Người phụ nữ bí ẩn (`EP04` & `EP08b`)** (`chi_ba` / `Kore`) · *Cameo hồ sơ:* **Ông Bạn Cũ IT giấu mặt (`EP06`)** · **Người Bóc Trần** (`nguoi_boc_tran` / `Charon`) |

---

## 1. Nhân vật & phân tách giọng (`02_CAST/cast.json` – 9 tuyến / 9 voice độc lập 100%)

| Nhân vật | Key | Voice | Chỉ đạo diễn xuất & âm sắc |
| :--- | :--- | :---: | :--- |
| **Tuấn** (35t, chủ tiệm gia dụng) | `anh_hai` | `Orus` | Nam miền Nam trầm chắc, thật thà; lo âu tụt hậu ở Hồi 1, lâng lâng tự hào làm *"Sếp Tuấn"* ở Hồi 3, sững sờ khi thấy hoạt ảnh chạy lúc tắt mạng |
| **Hương** (33t, vợ Tuấn) | `chi_hai` | `Sulafat` | Nữ miền Nam trầm vừa, thực tế, sắc bén, chủ động quay clip Chế độ Máy bay gửi nhóm kín cứu hàng trăm người khác |
| **Thầy Quang** (38t, diễn giả công nghệ) | `chu_no` | `Algieba` | Nam miền Nam trầm mượt, vang đầy sức hút trên sân khấu; đến Kết mở (`af: "phone"`) mất sạch vẻ tự tin, căng thẳng gọi báo cáo Chị Hai |
| **Trợ lý Khánh** (27t, điều phối VIP) | `ke_ngot_ngao_nam` | `Achird` | Nam trẻ sáng, lịch sự mượt mà lúc gọi *"Sếp Tuấn"* (`af: "default"`), lạnh đều vô cảm lúc ép nạp `40 triệu` mở cổng (`af: "phone"`) |
| **Chị Lan** (44t, chim mồi đóng vai chủ sạp vải) | `co_hanh` | `Despina` | Nữ miền Nam ~44t chân chất như tiểu thương đi chợ, bật dậy chốt suất đầu tiên cực thuyết phục (`af: "phone"` khi khoe lãi trong nhóm VIP) |
| **MC Hội trường** (28t) | `ke_ban_hang` | `Zephyr` | Nữ sân khấu tông sáng, hồ hởi, đẩy nhịp FOMO *"chậm tay là đứng ngoài kỷ nguyên AI"* |
| **Chú Bảo Vệ** (55t, sảnh tòa nhà) | `ong_bay` | `Algenib` | Nam lớn tuổi trầm khàn nhẹ, chậm rãi lột mác hội trường thuê theo ngày & xe trắng thuê 4 tiếng |
| **Chị Hai – Người phụ nữ bí ẩn (`EP04` & `EP08b`)** | `chi_ba` | `Kore` | Nữ 35t sắc lạnh, kiệm lời tối đa *(giấu mặt 100%, đồng bộ tuyệt đối với `EP04` & `EP08b`)* |
| **Người Bóc Trần** | `nguoi_boc_tran` | `Charon` | Đúng **1 câu (22 từ, `< 8s`)** ở thẻ `NHỚ KỸ` |

---

## 2. Kế hoạch Visual Motion (Level 2 + Living-Character A/B/C)
*Tổng 20 cảnh: **Level A = 3** (`s15, s17, s18`) · **Level B = 4** (`s00, s04, s06, s08` 2.5D Parallax) · **Level C = 13** (11 cảnh Living-Character A/B/C khóa pixel qua `03_ENGINE/face_roi_prep.py` + 3 `detail_reveal` đồng khung ở `s11, s13, s16b`) · **Level D = 0** · 0 chuỗi lặp zoom-in ≥ 3 cảnh · 100% foley khớp motion.*

---

## 3. Kịch bản lời thoại chi tiết (`v5` · 44 câu · Phương ngữ miền Nam · Đa dạng đại từ, không lặp "100 agent")

### MỞ MÀN (HOOK) – VĂN PHÒNG BAY TRÊN KHÔNG GIAN & VĂN PHÒNG TRỐNG TRƠN

**`s00_hook_space_stage` · `c00` (Level B 2.5D Parallax + Living-Char `fg` Thầy Quang & MC)** – Ánh đèn sân khấu xanh tím công nghệ rực rỡ, màn LED khổng lồ chiếu **văn phòng kính bay giữa không gian**.
- `l01_quang` **THẦY QUANG**: Ba trăm triệu giảm tám mươi phần trăm còn sáu chục! Tặng ngay văn phòng ảo bay trên không gian với một trăm agent AI!
- `l02_mc` **MC HỘI TRƯỜNG**: Nguyên công ty ảo đủ phòng bán hàng, chăm khách, kế toán vận hành tự động kiếm tiền cho bạn! Chỉ năm suất trong mười phút!

**`s01_hook_cut_empty` · `c01` (Level C Living-Char Tuấn)** – **CHỚP TRẮNG + IMPACT!** Văn phòng thật trống trơn dưới sáng mưa.
- `l03_tuan` **TUẤN**: Văn phòng trên màn hình vẫn bay, mấy phòng ban ảo vẫn sáng đèn báo lãi… mà hai trăm bốn chục triệu tiền thật bay đâu mất rồi?!

---

### HỒI 1 – CƠN BÃO FOMO AI & CHIẾC XE TRẮNG TRƯỚC SẢNH

**`s02_shop_ai_fomo` · `c02` (Level C Living-Char Tuấn & Hương)** – Buổi tối hai tháng trước trong tiệm đồ gia dụng nhỏ; Hương tò mò pha chút lo âu đời thường (không phản biện lộ ý video sớm).
- `l04_huong` **HƯƠNG**: Tháng này bán chậm quá anh ơi. Trừ tiền mặt bằng với hàng tồn là gần như huề vốn.
- `l05_tuan` **TUẤN**: Trên mạng AI sa thải hàng loạt kìa! Người ta dựng nguyên công ty ảo đủ bộ phận bán hàng tự động, mình cứ ghi sổ tay sao theo kịp?!
- `l06_huong` **HƯƠNG**: Thiệt hả anh? Nghe cái gì mà nguyên công ty tự chạy nghe lạ quá… nhưng coi chừng mấy chỗ trên mạng thổi phồng đó anh.
- `l07_tuan` **TUẤN**: Anh coi cho khỏi tụt hậu thôi, có đóng đồng nào đâu mà em lo.

**`s03_space_office_ad` · `c03` (Level C Living-Char Tuấn + `screen_glow`)**
- `l08_quang_p` **THẦY QUANG** *(loa điện thoại)*: Ba năm nữa chỉ còn hai loại người: người làm chủ dàn nhân sự AI tự kiếm tiền, và người bị thời đại bỏ lại phía sau!
- `l09_tuan` **TUẤN**: Vé nghe thử hai trăm chín chín ngàn… không đi cập nhật sớm chắc mình lỗi thời thiệt luôn.

**`s04_hotel_white_car` · `c04` (Level B 2.5D Parallax + Living-Char `fg` Tuấn)**
- `l10_tuan` **TUẤN**: Diễn giả chạy siêu xe, mở hội nghị ngay khách sạn lớn… tầm cỡ này chắc chắn làm ăn thứ thiệt.

---

### HỒI 2 – HỘI TRƯỜNG CÔNG NGHỆ: TẶNG VĂN PHÒNG BAY & NGƯỜI ĐẦU TIÊN GIƠ TAY

**`s05_hall_lan_fomo` · `c05` (Level C Living-Char Tuấn & Chị Lan)**
- `l11_lan` **CHỊ LAN**: Chú cũng sợ bị AI bỏ lại hả? Chị bán sạp vải ngoài chợ, mù công nghệ mà nghe mở công ty tự động hoài nên ráng đi.
- `l12_tuan` **TUẤN**: Dạ y chang em luôn chị. Nghe thầy chiếu mô hình công ty một người nãy giờ mở mang thiệt.

**`s06_countdown_space_office` · `c06` (Level B 2.5D Parallax + Living-Char `fg` Chị Lan + `light_shift`)**
- `l13_quang` **THẦY QUANG**: Cọc mười triệu trong mười phút giữ suất sáu chục! Tặng văn phòng không gian đủ phòng kinh doanh, tiếp thị, kế toán — gắn tên bạn làm giám đốc!
- `l14_lan` **CHỊ LAN**: Thầy ơi cho em chốt suất đầu tiên! Không rành máy tính mà có nguyên dàn nhân sự ảo làm giùm hết thế này em không bỏ lỡ đâu!
- `l15_mc` **MC HỘI TRƯỜNG**: Suất giám đốc số một đã có chủ! Chỉ còn bốn suất giảm tám mươi phần trăm! Chậm tay là đứng ngoài kỷ nguyên AI!

**`s07_tuan_swipes_deposit` · `c07` (Level C Living-Char Tuấn + `screen_glow`)**
- `l16_tuan` **TUẤN**: Ba trăm triệu còn sáu chục lại có sẵn công ty đủ bộ phận tự chạy… chị bán vải còn dám chốt, mình chậm là tụt hậu!

---

### HỒI 3 – CƠN SAY "GIÁM ĐỐC TUẤN" GIỮA KHÔNG GIAN & SỰ LÚNG TÚNG KHI BỊ HỎI THẲNG

**`s08_floating_office_debut` · `c08` (Level B 2.5D Parallax `drift_push` + Living-Char `bg` Quang, Khánh, Tuấn + `screen_glow`)**
- `l17_tuan` **TUẤN**: Trời ơi… văn phòng bay giữa không gian, từ phòng kinh doanh tới kế toán sáng đèn hết, gọi đúng tên mình là giám đốc luôn nè!
- `l18_quang` **THẦY QUANG**: Đây mới là bản chạy thử. Muốn hệ thống nối khách thật đổ lãi về ngân hàng, em phải nạp gói máy chủ kích hoạt.
- `l19_khanh` **TRỢ LÝ KHÁNH**: Anh kích hoạt gói thử hai chục triệu trước. Tụi nó chốt đơn tới đâu, sếp Tuấn thu tiền tới đó mỗi ngày!

**`s09_boss_in_small_shop` · `c09` (Level C Living-Char Tuấn & Hương + `screen_glow`)** – Sau câu hỏi chí mạng của Hương, Tuấn ngập ngừng lúng túng rõ rệt vì chính mình cũng không biết công ty bán hàng gì.
- `l20_lan_p` **CHỊ LAN** *(tin nhắn nhóm VIP)*: Cảm ơn thầy Quang nhiều lắm! Em nâng máy chủ lớn hôm qua, dàn nhân sự chạy suốt đêm, lãi về gấp đôi tiền học rồi!
- `l21_tuan` **TUẤN**: Em coi nè! Nguyên văn phòng ảo gọi anh bằng sếp, mấy phòng ban chốt đơn báo lãi liên tục — rút được ba triệu thật luôn!
- `l22_huong` **HƯƠNG**: Nguyên công ty ảo sáng đèn bay ngoài không gian… nhưng tụi nó bán món hàng gì, bán cho ai mà tiền tự chảy về túi anh?
- `l22b_tuan` **TUẤN** *(ngập ngừng lúng túng đánh trống lảng)*: Thì… thầy nói tụi nó chạy thuật toán kết nối sàn quốc tế gì đó… công nghệ cao lắm anh cũng không rành, miễn tiền về thật là được!

**`s10_fomo_server_all_in` · `c10` (Level C `screen_glow`)**
- `l23_quang_p` **THẦY QUANG** *(tin nhắn riêng)*: Sếp Tuấn có tố chất dẫn đầu. Chỉ còn đúng ba suất trạm máy chủ một trăm sáu mươi triệu trước khi khóa cổng.
- `l24_tuan` **TUẤN**: Rút ba triệu thật rồi, mấy phòng ban trên kia vẫn chốt lãi ầm ầm… xoay gói lớn một đợt là đổi đời luôn!

---

### HỒI 4 – NÔ LỆ HÓA, PHẢN PHÁO NGOẠI TUYẾN & ĐÒN BÓC `0 KB` KHÔNG THỂ CHỐI CÃI

**`s11_frozen_agents_still_looping` · `c11 → c11_reveal` (Level C `detail_reveal` + `eye_blink` + `light_shift`)** – Điểm chạm tâm lý **nô lệ hóa**: nhà đã vét sạch `240tr` không còn một đồng, "Sếp Tuấn" phải hạ mình van xin thương lượng trừ cấn 40tr vô tiền lãi nhưng bị Khánh lạnh lùng cúp máy.
- `l25_tuan` **TUẤN**: Alo Khánh ơi! Trên màn hình vẫn báo chốt đơn ầm ầm mà sao anh bấm rút bị khóa, gọi thầy Quang cũng tắt máy rồi?!
- `l26_khanh_p` **TRỢ LÝ KHÁNH** *(điện thoại)*: Trạm máy chủ anh đang kẹt đối soát. Nạp thêm bốn chục triệu mở cổng trước trưa nay, không là hệ thống đóng băng hết.
- `l26b_tuan` **TUẤN** *(giọng run hẳn xuống nước năn nỉ van vỉ)*: Khánh ơi, nhà anh vét sạch hai trăm bốn chục triệu rồi, không còn đồng nào! Cho anh gặp thầy xin trừ đỡ bốn chục vô tiền lãi đi!
- `l26c_khanh_p` **TRỢ LÝ KHÁNH** *(lạnh ngắt trịch thượng)*: Quy định hệ thống không trừ cấn. Kiếm đủ bốn chục trước trưa thì mở, không thì mất trắng!

**`s12_empty_office_guard` · `c12` (Level C Living-Char Tuấn & Chú Bảo Vệ)** – Tuấn chạy dưới mưa tới tận tòa nhà hy vọng gặp thầy thương lượng, rồi bàng hoàng nhận ra sự bẽ bàng của ảo giác làm sếp.
- `l27_tuan` **TUẤN**: Chú ơi, học viện thầy Quang tầng năm đâu rồi chú? Cháu hết tiền rồi, chạy tới xin thầy trừ đỡ… chiếc xe trắng cũng không thấy nữa?
- `l28_guard` **CHÚ BẢO VỆ**: Đoàn đó chỉ thuê hội trường với phòng họp theo ngày thôi chú ơi. Chiếc xe trắng cũng là xe thuê đậu chụp hình bốn tiếng!
- `l28b_tuan` **TUẤN** *(sững sờ chua chát nghẹn đắng)*: Bỏ hai trăm bốn chục triệu mơ làm giám đốc… hóa ra biến thành kẻ quỵ lụy đi năn nỉ xin lại chính tiền của mình!

**`s13_offline_clip_and_group_expose` · `c13 → c13_reveal` (Level C `detail_reveal` + Living-Char Tuấn & Hương)** – **Hiệp 1:** Hương bật Chế độ Máy bay quay clip quăng vô nhóm kín — lập tức quản trị viên phản pháo bằng chiêu *"tính năng chạy ngoại tuyến không gián đoạn"*!
- `l29_tuan` **TUẤN**: Tắt mạng rồi mà văn phòng bay với mấy bảng lãi vẫn nhảy y chang… Hóa ra chỉ là đoạn hoạt ảnh vẽ sẵn!
- `l30_huong` **HƯƠNG**: Em quay lại rồi! Quăng thẳng vô nhóm kín cho mấy trăm người kia coi mà dừng nạp tiền liền!
- `l30b_khanh_p` **TRỢ LÝ KHÁNH** *(phản pháo trong nhóm VIP)*: Mọi người bình tĩnh! Đó là tính năng chạy ngoại tuyến không gián đoạn, lát có mạng tự đồng bộ đơn thật — đừng nghe kẻ phá đám!

**`s13b_undeniable_killshot` · `c13b` (Level C `push_in_breathe` + `screen_glow`)** – **Hiệp 2 không thể chối cãi:** Hương soi cài đặt lưu lượng mạng cả tháng của app (**`0 KB`**) + chỉnh đồng hồ về **năm 2000** vẫn nhảy đơn mới tinh → đập tan lời ngụy biện, cả nhóm VIP 300 người vỡ trận hủy cọc!
- `l30c_huong` **HƯƠNG**: Ngoại tuyến hả? Coi cài đặt mạng cả tháng của app: bằng không! Chỉnh ngày về năm hai ngàn vẫn nhảy đơn mới tinh kìa!
- `l31_tuan` **TUẤN**: Anh sai rồi Hương ơi… sáu chục tiền học, trăm tám gói máy chủ. Chuyển đi sạch hai trăm bốn chục triệu rồi.
- `l32_huong` **HƯƠNG**: Ngưng liền! Đừng nạp mở cổng, đừng tin tin nhắn lấy lại tiền giùm! Gom sao kê, biên nhận lên công an trình báo ngay!

---

### HỒI 5 – LÀM LẠI TỪ VIỆC THẬT & THẺ NHỚ KỸ

**`s14_next_morning_shop` · `c14` (Level C `pan_right_breathe` + `light_shift`)**
- `l33_tuan` **TUẤN**: Bữa nay anh mới tỉnh… ngồi làm giám đốc cái công ty ảo đó, cuối cùng người giàu nhất vẫn là người đứng trên sân khấu.

**`s15_red_flags` · `c15` (Level A `static_hold`)**
- `l34_narr` **NGƯỜI BÓC TRẦN**: Giảm sốc tặng công ty ảo một trăm agent tự kiếm tiền chỉ là hoạt ảnh mồi. Kiểm chứng trước khi xuống tiền!

---

### KẾT MỞ SAU THẺ NHỚ KỸ – VŨ TRỤ CHỊ HAI (`EP04 ↔ EP06 ↔ EP08b ↔ EP10`)

**`s16a_coda_quang_report` · `c16a` (Level C Living-Char Thầy Quang + `screen_glow`)**
- `l35_quang_p` **THẦY QUANG** *(điện thoại)*: Chị Hai… hỏng hết rồi! Khách quay clip tắt mạng, soi dữ liệu mạng bằng không quăng vô nhóm, học viên làm loạn đòi rút tiền sạch!
- `l36_quang_p` **THẦY QUANG** *(điện thoại)*: Tay viết app đợt Bạn Thân bốn chấm không làm ẩu rồi! Nhận tiền dựng máy chủ mà nhét mỗi đoạn hoạt ảnh chạy chay!

**`s16b_coda_chihai_order` · `c16b → c16b_off` (Level C `static_hold` + `detail_reveal` tắt phụt màn hình)**
- `l37_chihai` **CHỊ HAI** *(voice `Kore`)*: Đợt trước mềm lòng tha bạn cũ đã suýt lộ. Giờ còn dám qua mặt tôi.
- `l38_chihai` **CHỊ HAI** *(voice `Kore`)*: Đóng app. Rút hết đoàn. Còn tay đó… làm đi.
- *(Tay áo lụa xanh ngọc lục bảo bấm tắt phụt màn hình máy tính bảng → `click` + `impact` trầm + cắt đen đột ngột!)*

**`s17_black_cut` · `c17`** – Cắt đen 1.2 giây.
**`s18_disclaimer` · `c15`** – Bảng **LƯU Ý** *(3.8 giây)*.

---

## 4. Thẻ DẤU HIỆU NHẬN BIẾT (`red_flags` — 4 ý + 1 hành động gốc)
1. **Đánh vào nỗi sợ tụt hậu AI & giảm sốc 80%:** Hù bị thời đại đào thải rồi ép cọc ngay trong 10 phút đếm ngược để bạn không kịp kiểm chứng.
2. **Văn phòng ảo 100 agent sáng đèn báo lãi liên tục:** Hình ảnh bay bổng, gọi tên bạn làm "giám đốc" rất dễ chỉ là hoạt ảnh lập trình sẵn — không có hàng hóa hay khách mua thật.
3. **Phông bạt sang trọng & chim mồi hội trường:** Xe sang, hội trường có thể thuê theo giờ; người bật dậy chốt suất đầu tiên dễ là nhân sự đóng vai.
4. **Trả lãi mồi thật đợt đầu rồi khóa cổng đòi phí:** Cho rút khoản nhỏ ban đầu để xóa nghi ngờ, khi bạn nạp gói máy chủ lớn liền báo kẹt đối soát đòi đóng thêm.
- **Việc nên làm ngay:** Luôn hỏi thẳng "hàng gì, bán cho ai" và kiểm chứng pháp nhân trước khi xuống tiền; lỡ sập bẫy phải dừng cắt lỗ ngay, cảnh giác dịch vụ "thu hồi vốn" và gom sao kê, biên nhận trình báo công an!

## 5. Tự kiểm “Không dạy lừa”
- [x] Không mô tả cách lập trình app hoạt ảnh giả, thuê hội trường/siêu xe hay tổ chức đội chim mồi chi tiết (`L2`).
- [x] Không phủ nhận công nghệ AI chân chính (Hương khẳng định rõ AI là công cụ phụ bán hàng thật ở `s02` và hai vợ chồng ứng dụng quay clip hàng thật ở `s14`).
- [x] Kết mở Chị Hai tuyệt đối không dùng từ bạo lực (`giết`, `khử`, `sát hại`, `thủ tiêu`...), sạch 100% `policy_wordlists.json`.
