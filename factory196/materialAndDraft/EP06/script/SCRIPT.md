# EP06 – BA TRIỆU TÁM TRÊN MÀN HÌNH *(Bản kịch hóa điện ảnh – v1-draft)*

- **Mã tập:** `EP06` · **Slug:** `BaTrieuTamTrenManHinh`
- **Họ kịch bản:** `JOB-TASK` – Tuyển cộng tác viên xử lý đơn hàng tại nhà: cấp sẵn `40.000đ` làm thử không tốn vốn → dụ "bù phần thiếu" từ `10.000đ` lên vài trăm ngàn khiến nạn nhân không nhận ra mình đã chuyển hơn hai triệu tiền thật, trong khi số dư trên màn hình nhảy lên `3.850.000đ` rồi khóa rút → **Người bạn IT giấu mặt** tra tên miền bóc trần trang tự nhận từ năm 2018 thực chất mới mở 6 ngày → **Kết mở đường dây ngầm:** Cụm máy chủ mới mở lại trùng đầu mối với mấy nhánh đợt trước.
- **Định dạng:** `16:9` (`1920x1080 @ 30fps`) · **Tỷ lệ:** **97% kịch tâm lý – điện ảnh / 3% Người Bóc Trần (< 10 giây)**
- **Nguồn sự thật của timeline:** [`source/build_draft.py`](../source/build_draft.py) → sinh [`episode.json`](../episode.json).

## Nhân vật & giọng (`02_CAST/cast.json` – 7 tuyến / 7 voice độc lập)
| Nhân vật | Key | Voice | Chỉ đạo giọng |
|---|---|---|---|
| **Nam** (32t, chồng Thảo) | `anh_hai` | `Orus` | Nam trầm ấm, thật thà, chăm làm, rất đời thực |
| **Thảo** (31t, vợ Nam) | `chi_hai` | `Sulafat` | Nữ trầm vừa, cực kiệm lời, thực tế, không chì chiết chồng |
| **Vy Điều Phối** | `ke_ngot_ngao_nu` | `Aoede` | Nữ trẻ ngọt ngào, lịch sự hướng dẫn lúc đầu rồi khóa máy (`af: phone`) |
| **Bộ phận Hỗ trợ đối soát** | `chu_no` | `Fenrir` | Nam trầm đều, lạnh băng như máy trả lời khi chặn rút tiền (`af: phone`) |
| **Người bạn IT giấu mặt** | `ong_bay` | `Algenib` | Nam 35t trầm khàn nhẹ, điềm tĩnh, **cố ý không lộ mặt & không nêu tên** |
| **Đầu dây lạ (Kết mở)** | `chi_tu` | `Zephyr` | Nữ trầm tĩnh gọi vào máy phụ của người bạn IT (`af: phone`) |
| **Người Bóc Trần** | `nguoi_boc_tran` | `Charon` | Đúng 1 câu (19 từ, `< 9s`) ở thẻ `NHỚ KỸ` |

---

## HOOK – CON SỐ ĐỨNG YÊN & CÚ CHẶN RÚT TIỀN
**`s00_hook_blocked` · `c00`** – 22:30 Đêm. Phòng khách nhà Nam. *(Bong bóng: "VÍ ĐỐI TÁC ĐƠN HÀNG: Số dư: 3.850.000đ · Chưa đủ điều kiện đối soát để rút tiền")*.
- `l01_nam` **NAM**: Alo, trong ví tôi đang có ba triệu tám, sao bấm rút về ngân hàng lại khóa?
- `l02_ht` **HỖ TRỢ** *(điện thoại)*: Tài khoản anh còn treo một đơn đối soát cuối. Anh bù thêm hai triệu chín là hệ thống giải ngân toàn bộ.
- `l03_nam` **NAM**: Tiền tôi nằm sẵn trỏng gần bốn triệu rồi, sao không trừ thẳng mà bắt nạp thêm?!

**`s01_hook_two_screens` · `c01`** – Chớp trắng sang cận gương mặt sững sờ của Nam trước dòng hối thúc trên màn hình. *(Bong bóng: "HỆ THỐNG ĐỐI SOÁT: Chỉ còn 01 bước cuối để nhận toàn bộ 6.750.000đ gốc và hoa hồng")*.
- `l04_ht` **HỖ TRỢ** *(điện thoại)*: Quy trình tự động không trừ cấn anh nha. Quá hai mươi ba giờ chưa xong đơn là ví đóng băng.
- *(Tút! Đầu dây cúp phụt. Ngón tay Nam khựng trên màn hình).*

## HỒI 1 – BỐN CHỤC NGÀN CẤP SẴN & DÒNG CHỮ "TỪ NĂM 2018"
**`s02_rainy_shift_cut` · `c02`** – Ba tối trước. Mưa dầm ngoài hiên, Nam lau áo mưa bước vào nhà.
- `l05_nam` **NAM**: Mưa dầm cả tuần nay kho cắt hết ca tối, tháng này chắc hụt tiền phụ em đóng học cho con rồi.
- `l06_thao` **THẢO**: Tháng nào hụt mình gói ghém tháng đó, mưa gió anh chạy ráng ngoài đường nguy hiểm lắm.

**`s03_first_free_order` · `c03`** – Nam ngồi ghế gỗ lướt thấy tin tuyển CTV đơn hàng *(Bong bóng cài chi tiết gốc: "SÀN ĐỐI TÁC ĐƠN HÀNG: Giới thiệu: Vận hành từ năm 2018 · Cấp sẵn 40.000đ vốn làm thử")*.
- `l07_vy` **ĐIỀU PHỐI** *(điện thoại)*: Chào anh Nam, bên em tặng sẵn bốn chục ngàn trong ví rồi đó. Anh bấm xác nhận đơn ba chục ngàn đầu tiên nha.
- *(Ting! Bong bóng: "Đơn 30.000đ hoàn thành · Cộng gốc & hoa hồng -> Số dư: 45.000đ")*.
- `l08_nam` **NAM**: Ủa… làm thử có một đơn mà nhảy lên bốn lăm ngàn liền nè em.
- `l09_thao` **THẢO**: Làm cái đó có bắt mình bỏ tiền túi ra hông anh?
- `l10_nam` **NAM**: Đâu có, trang này ghi chạy từ năm hai ngàn mười tám, lại cho sẵn tiền trong ví làm thử mà.

## HỒI 2 – MƯỜI NGÀN "BÙ PHẦN THIẾU" & CON SỐ NHẢY MÚA
**`s04_ten_thousand_bait` · `c04`** – Nửa tiếng sau. Đơn thứ hai trị giá `55.000đ`, báo thiếu đúng `10.000đ`.
- `l11_nam` **NAM**: Ủa, sao đơn này báo thiếu mười ngàn vậy ta?
- `l12_vy` **ĐIỀU PHỐI** *(điện thoại)*: Dạ anh bù đúng mười ngàn phần thiếu thôi. Xong đơn là tiền hàng với hoa hồng cộng dồn hết lại vô ví anh liền.
- *(Nam chặc lưỡi chuyển 10.000đ. Số dư nhảy lên `65.000đ` kèm sổ lịch sử cộng trừ rõ từng dòng).*
- `l13_nam` **NAM**: Ờ… sổ giao dịch ghi cộng trừ rõ ràng thiệt.

**`s05_escalating_topups` · `c05`** – Hai tối kế tiếp: mỗi đơn chỉ "bù phần thiếu" vài trăm ngàn nên cảm giác tiền bỏ ra rất ít.
- `l14_vy` **ĐIỀU PHỐI** *(điện thoại)*: Anh lên bậc quen rồi nên được ưu tiên đơn lớn. Ví có sẵn triệu rưỡi, anh bù thêm bốn trăm rưỡi thôi nha.

**`s06_wife_sharp_question` · `c06`** – Bàn ăn buổi tối. Nam hào hứng xoay màn hình hiện `3.850.000đ` khoe vợ.
- `l15_nam` **NAM**: Em nhìn nè, ba tối nay anh gom hoa hồng lên được gần bốn triệu rồi đó!
- `l16_thao` **THẢO**: Nhưng anh bấm rút thử tiền về ngân hàng mình lần nào chưa?
- `l17_nam` **NAM**: Mục rút tiền với số tài khoản anh nằm sẵn đây nè. Làm nốt đợt tối nay cho chẵn rồi anh rút một lượt luôn.

## HỒI 3 – TIỀN THẬT ĐI RA & CON SỐ ĐỨNG YÊN
**`s07_real_vs_screen` · `c07`** – 22:35 Đêm (nối tiếp sau Hook). Nam mở ứng dụng ngân hàng thật đối chiếu từng khoản tiền thật đã chuyển đi (`-10.000đ · -180.000đ · -450.000đ · -1.500.000đ = Tổng -2.140.000đ`), rồi nhìn sang con số `3.850.000đ` đứng yên trên trang web. Nam gọi lại cho Vy Điều Phối nhưng máy khóa.
- `l18_nam` **NAM**: Lúc biểu bù mười ngàn thì bắt máy lẹ lắm… Tới lúc hỏi rút tiền thì khóa máy luôn.
- `l19_ht` **HỖ TRỢ** *(điện thoại)*: Anh bỏ ngang lúc này là mất trắng ba triệu tám đang nằm sẵn trong ví đó nha.
- *(Nhịp câm: Nam nhìn ngón cái của mình rồi dứt khoát tắt ứng dụng ngân hàng, không chuyển thêm một đồng nào).*

## HỒI 4 – NGƯỜI BẠN IT GIẤU MẶT & TÊN MIỀN SÁU NGÀY TUỔI
**`s08_porch_call_friend` · `c08`** – Ngoài hiên nhà sau cơn mưa đêm, Nam ngồi một mình bấm gọi người bạn cũ.
- `l20_nam` **NAM**: Ê, giờ này còn thức hông mày? Tao mới gửi cái đường dẫn qua tin nhắn, coi giùm tao trang này cái.

**`s09_faceless_it_lookup` · `c09`** – Căn phòng tối ở một nơi khác (**cố ý không lộ mặt, không giới thiệu danh tính**: góc máy chỉ lấy đôi bàn tay người đàn ông đặt điện thoại cạnh laptop sáng xanh). *(Bong bóng: "TRA CỨU ĐĂNG KÝ TÊN MIỀN: Tự nhận trên trang: Từ năm 2018 | Ngày đăng ký thật: Thứ Ba tuần trước")*.
- `l21_it` **BẠN CŨ**: Tên miền này mới đăng ký hồi thứ Ba tuần trước. Mà trên trang lại tự nhận hoạt động từ năm hai ngàn mười tám?
- `l22_nam` **NAM** *(loa điện thoại)*: Nhưng trong ví tao nó vẫn hiện nguyên ba triệu tám với lịch sử đơn đầy đủ mà mày…
- `l23_it` **BẠN CŨ**: Tiền trong ngân hàng mới có nơi giữ cho mày. Còn con số trên trang lạ… tụi nó gõ bao nhiêu chẳng được.
- `l24_it` **BẠN CŨ**: Thôi, mày quên con số đó đi. Đừng nạp thêm, cũng đừng tin đứa nào nhận kéo tiền treo về.

## HỒI 5 – TẮT MÀN HÌNH & GIỮ LẠI TIỀN THẬT
**`s10_turn_off_screen` · `c10`** – Phòng khách nhà Nam. Thảo mang ly nước ấm đặt xuống bàn cạnh chồng.
- `l25_nam` **NAM**: Anh mất hai triệu mốt tiền thiệt rồi Thảo ơi… Tưởng bù mỗi lần vài trăm lẻ, cộng lại đứt mấy ngày công.
- `l26_thao` **THẢO**: Dừng ngay khúc này là may lắm rồi anh. Chứ nãy tiếc của mà nạp thêm ba triệu nữa là lún sâu luôn đó.
- `l27_nam` **NAM**: Ừ… Mai anh đem sao kê trình báo công an, rồi dặn anh em dưới kho né cái trò bù tiền này ra.
- *(Nam bấm tắt màn hình, đặt úp chiếc điện thoại xuống mặt bàn gỗ).*

## THẺ NHỚ KỸ *(DƯỚI 10 GIÂY)*
**`s11_red_flags`** *(nền `EP01b/scene18.jpg`)*
- `l28_narr` **NGƯỜI BÓC TRẦN**: Số dư trên trang lạ là chữ họ tự gõ, còn tiền rời ngân hàng bạn mới mất thật.

## KẾT MỞ ĐƯỜNG DÂY NGẦM – CĂN PHÒNG TỐI CỦA NGƯỜI BẠN GIẤU MẶT
**`s12_unseen_tracker_coda` · `c11`** – Căn phòng tối của người bạn IT giấu mặt (vẫn chỉ thấy bóng vai và bàn tay cạnh laptop cùng cuốn sổ bìa đen). Chiếc điện thoại thứ hai trên bàn khẽ rung lên.
- `l29_sec` **ĐẦU DÂY LẠ** *(điện thoại)*: Đường dẫn cậu bạn anh vừa gửi… lại trỏ về cụm máy chủ mới mở tuần trước hả anh?
- `l30_it_coda` **BẠN CŨ**: Ừ. Lại chung một đầu mối đứng sau mấy nhánh đợt trước.
- **`s13_black_cut` · `c12`** – **IMPACT + CẮT ĐEN ĐỘT NGỘT!**

**`s14_disclaimer`** – LƯU Ý.
