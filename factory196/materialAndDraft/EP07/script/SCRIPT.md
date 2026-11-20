# EP07 – SAU HAI TRĂM TRIỆU *(Bản kịch hóa điện ảnh – v5-draft: Chốt dứt khoát & Kết mở bóng lưng tối giản)*

- **Mã tập:** `EP07` · **Slug:** `SauHaiTramTrieu`
- **Họ kịch bản:** `MIX-RECOVERY` – Bẫy lừa lần hai kết hợp **mắt xích dò thông tin ngoài đời (bàn cà phê sáng)**. **Ông Thành** (65t, vừa về hưu, có 200 triệu dưỡng già) rảnh tay lướt mạng và tin vào kinh nghiệm *"cả một đời đi làm chuyện gì chưa gặp qua"*, mất sạch `200 triệu` sau **3 tuần** bị dẫn dụ nhiều đợt vào một ứng dụng đầu tư lạ (phim làm mờ quá trình nạp lần 1, đẩy thẳng vào hậu quả cao trào). Ngại mất thể diện người cha trước con gái 26 tuổi (**Trang**), ông gạt lời khuyên trình báo, nhờ bạn cũ **Ông Tám** (60t) — nhưng sau khi hỏi kiểm tra *"chưa báo công an, chưa nói kỹ với con Trang phải hông?"*, cầm `5 triệu` và kéo chậm thời gian, Tám **rút êm** lạnh tanh. Không dám thừa nhận với con gái, ông tìm đến **nhóm tự xưng lấy lại tiền** trên mạng (**Khoa**, 31t). Không đòi ngay 10 triệu, Khoa nhử từng đợt nhỏ (`1tr → 2tr → 7tr → 15tr → 30tr`) bằng những "bằng chứng mồi" trông như nắm bên kia trong lòng bàn tay (**ảnh luồng tiền che số, lịch sử chat cũ, phát lại đoạn ghi âm cuộc gọi cũ với Ngọc, biên bản treo 95%, lệnh cộng +200tr không mã tra soát**) — nhưng tất cả đều **không đủ cơ sở xác thực khi trình báo công an**. Khi ông cạn tiền, Khoa chốt rụp một câu lạnh băng rồi chặn ngay. **Kết mở 2 lớp tối giản:** Khoa báo cáo đầu dây trên trong phòng tối, rồi cắt sang cảnh **hoàn toàn câm** tại một quán cà phê ven biển (địa bàn khác) — bóng lưng quen thuộc của **Ông Tám** giơ bàn tay đeo **chiếc lắc bạc** vẫy chào một người bạn già mới, trên bàn là chiếc điện thoại sáng giao diện ứng dụng đã sập quen thuộc.
- **Định dạng:** `16:9` · **Thời lượng:** `463.6s` (`07:43` WAV thật, `26 cảnh`, `49 câu`, `1031 từ`, `133 từ/phút`, câu dài nhất `26 từ`).
- **Tỷ lệ:** ~97% kịch / ~3% Người Bóc Trần (1 câu 19 từ, thẻ kết `7.5s`).
- **Thông điệp lõi:** *Kẻ lừa thứ hai không cần bạn ngây thơ. Nó chỉ cần bạn xấu hổ đến mức không dám nói ra, và chậm đến mức không kịp trình báo.*
- **Nguồn sự thật:** [`source/build_draft.py`](../source/build_draft.py) → [`episode.json`](../episode.json). Không sửa tay `episode.json`.

## Thay đổi v4 → v5 (tối giản điện ảnh & chuẩn mực nghiệp vụ)
| # | v4 | v5 |
| :-: | :--- | :--- |
| 1 | `s12_mask_off` Khoa nói 2 câu chọc tức/phân tích tâm lý nạn nhân | **Chốt dứt khoát đúng bản chất thực dụng (1 câu lạnh băng):** *"Chú hông đóng đủ bốn chục triệu trong tối nay thì hồ sơ tự hủy. Bên em hết hỗ trợ."* → cúp rụp máy + `ĐÃ CHẶN`. Kẻ lừa không rảnh đôi co; hết giá trị khai thác là cắt ngay |
| 2 | `s21b_tam_coda` có tin nhắn `Hồ sơ #094 đã xong · Rút êm`, `bank_ting` và thoại Ông Tám | **Hoàn toàn câm, không thoại, không bong bóng:** chỉ có **bóng lưng quen thuộc** (áo đen, **lắc bạc**) vẫy tay chào một người bạn già mới ở **một địa bàn hoàn toàn khác (quán cà phê ven biển)**; trên bàn là chiếc điện thoại sáng **giao diện ứng dụng đã sập quen thuộc ở `c04`** |
| 3 | Cán bộ `l39a_cb` nói *"tôi đề nghị ngân hàng phối hợp xác minh ngay"* | Đổi cách nói chuẩn mực và an toàn nghiệp vụ nhất: *"Mấy khoản mới chuyển chú đưa đủ sao kê, chúng tôi tiếp nhận ngay để phối hợp ngân hàng xác minh theo quy trình."* |
| ✓ | **Toàn bộ thành quả v2–v4** | **GIỮ NGUYÊN 100%:** làm mờ lần 1 kéo dài 3 tuần, nhử từng đợt `1tr → 2tr → 7tr → 15tr → 30tr` kèm ghi âm Ngọc (`Aoede`), trục Ông 65t – Trang 26t – Bé Bo 5t, 11 điểm pháp lý v2, 9/9 voice độc lập, Clearance giữ ở `CHỜ DUYỆT` |

## Nhân vật & giọng (8 tuyến / 8 voice độc lập – 100% `gemini-3.8-flash-tts`)
| Nhân vật | Key | Voice | Ghi chú |
|---|---|---|---|
| **Ông Thành** (65t, vừa về hưu) | `ong_bay` | `Algenib` | Trầm hơi khàn từng trải; tự tin → bàng hoàng → sụp đổ; **không giả giọng run rẩy** |
| **Trang** (26t, con gái) | `chi_hai` | `Sulafat` | Ấm, chín chắn, kiệm lời, thương ba không chì chiết |
| **Bé Bo** (5t, cháu ngoại) | `be_tom` | `Puck` | Trong sáng, hồn nhiên; nghe thử 1 câu để giữ đúng nét 5 tuổi |
| **Ông Tám** (60t, bạn cũ – nhân vật bí ẩn) | `anh_hai` | `Orus` | Trầm vang tách hẳn `Algenib`; có bản thường, `phone`, `memory` |
| **Khoa** (31t, tự xưng nhóm lấy lại tiền) | `ke_ngot_ngao_nam` | `Achird` | `phone` (Hồi 1–3); `s21` là giọng phòng thật |
| **Chuyên viên Ngọc** (ghi âm cũ, 1 câu) | `ke_ngot_ngao_nu` | `Aoede` | `af: phone`, phát lại từ loa điện thoại ở `s09b` |
| **Cán bộ tiếp nhận** (nữ 35t) | `chi_tu` | `Zephyr` | 3 câu, bóc rõ bằng chứng mồi vô giá trị xác thực + phối hợp ngân hàng xác minh |
| **Người Bóc Trần** | `nguoi_boc_tran` | `Charon` | 1 câu duy nhất ở Thẻ Nhớ Kỹ |

## Bản đồ cài – trả
| Cài | Chi tiết | Trả |
|---|---|---|
| `s02` | Đồng hồ cơ cổ điển dây thép viền vàng trên cổ tay trái Ông Thành | `s11` tháo cầm đồ → `s14` Trang nhìn cổ tay trống & lời thú nhận *"cả chiếc đồng hồ"* → `s18` bàn tay trống xoa đầu cháu |
| `s02` | Bản vẽ sửa nhà làm phòng riêng có cửa sổ cho Bé Bo năm sau vô lớp Một | `s10` liếc bản vẽ khi nói dối → `s16` cất vào hộc tủ → `s17` câu hỏi của Bé Bo |
| `s02` | *"Cả một đời ba đi làm, chuyện gì ba chưa gặp qua? Tới giờ con còn sợ ba bị gạt nữa hả?"* | `s05` ngại bị cười *"ông già mới về hưu đã bị gạt"* → `s10` nói dối con gái qua khe cửa → `s14` cúi đầu thú nhận |
| `s03` | **Ông Tám** đeo **lắc bạc**, dò hỏi tiền hưu/sửa nhà & cài câu *"Có chuyện gì cứ gọi một tiếng..."* | `s06` hỏi kiểm tra *"chưa báo công an, chưa nói kỹ với con Trang phải hông?"* → `s07` **rút êm** → `s13` không bắt máy → `s16` `ĐÃ XEM` → `s21b` bóng lưng vẫy chào bạn già mới ở vùng biển, trên bàn là app quen thuộc |
| `s04` | **Chuyên viên chăm sóc: Ngọc** + giao diện app xanh đen/biểu đồ vàng kim bị khóa đỏ | `s09` nói trúng tên Ngọc → `s09b` phát lại **ghi âm cũ của Ngọc** → `s21` *"con Ngọc chuyển qua"* → `s21b` cùng giao diện app đó trên bàn Ông Tám |
| `s09–s11` | Bằng chứng mồi che số / ghi âm cũ / lệnh treo 95% / lệnh cộng +200tr không mã tra soát | `s15` Cán bộ: *"Còn hình che số với ghi âm cũ không đủ cơ sở xác thực bên kia"* |
| `s05` | *"Cho ba ba ngày"* & lời khuyên gọi tổng đài ngân hàng / trình báo ngay | `s10` Trang nhắc *"mai là hết ba ngày rồi"* → `s15` khoản cũ khó xác minh, khoản mới còn kịp |

---

## HOOK – 23:15 ĐÊM CẠN SẠCH TIỀN
**`s00_hook_midnight` · `c00`** – 23:15, phòng khách tối của căn nhà phố cũ, cổ tay trái Ông Thành đã trống. Bong bóng **NHÓM HỖ TRỢ LẤY LẠI TIỀN**: *"Lệnh hoàn trả 200.000.000đ bị lỗi mã xác thực · Cần bổ sung 40.000.000đ"* (`TREO LỆNH`).
- `l01_thanh` **ÔNG THÀNH**: Đủ rồi! Tôi vừa chuyển ba chục triệu cuối cùng xong, sao lại đòi thêm bốn chục triệu nữa?!
- `l02_khoa` **KHOA** *(điện thoại)*: Chú Thành bình tĩnh. Sai mã xác thực thì hệ thống khóa lệnh hoàn trả hai trăm triệu, bên em đâu mở được.
- `l03_thanh` **ÔNG THÀNH**: Tôi biết tụi cậu lừa tôi rồi! Tôi quen biết ngoài đời hông thiếu, tụi cậu trốn đâu tôi cũng tìm ra!

**`s01_hook_freeze` · `c01`** – Chớp trắng, đứng hình gương mặt Ông Thành dưới ánh màn hình điện thoại, nhịp tim. *(câm)*

## HỒI 1 – MỘT THÁNG TRƯỚC
**`s02_retirement_plan` · `c02`** – Phòng khách ấm áp một tháng trước; bản vẽ sửa nhà trên bàn, chiếc đồng hồ thép viền vàng trên cổ tay trái Ông Thành, điện thoại đặt bên cạnh.
- `l05_thanh` **ÔNG THÀNH**: Mới về hưu rảnh tay, gom hai trăm triệu sửa lại nhà, làm phòng riêng cho thằng Bo năm sau vô lớp Một.
- `l06_bo` **BÉ BO**: Phòng mới có cái cửa sổ bự cho con để đồ chơi với học bài hông ông ngoại?
- `l07_thanh` **ÔNG THÀNH**: Có chứ cháu ngoại! Rảnh tay lướt mạng ông tính xoay thêm một cú cho dư dả, sửa xong vẫn còn tiền dưỡng già.
- `l08_trang` **TRANG**: Ba mới nghỉ, rảnh coi tin cho vui thôi nha ba. Tiền hưu cứ để yên ngân hàng, trên mạng giờ đủ thứ bẫy lắm.
- `l08b_thanh` **ÔNG THÀNH**: Trời, cả một đời ba đi làm, chuyện gì ba chưa gặp qua? Tới giờ con còn sợ ba bị gạt nữa hả?

**`s03_old_friends_cafe` · `c03`** – Quán cà phê sáng quen thuộc của hội bạn cũ; Ông Tám (60t, đeo lắc bạc cổ tay, điện thoại úp nhẹ trên bàn) hỏi thăm tự nhiên mà ánh mắt dò xét kỹ.
- `l09a_tam` **ÔNG TÁM**: Mới lãnh cục tiền hưu về, tính sửa nhà cho cháu ngoại rồi để tiền nằm không vậy hả Thành?
- `l09_tam` **ÔNG TÁM**: Chơi với mày tao khoái cái tính sòng phẳng. Có chuyện gì cứ gọi một tiếng, mấy thằng em ngoài đời của tao lo liền.
- `l10_thanh` **ÔNG THÀNH**: Sống tới tuổi này hơn nhau chỗ biết rộng, quen nhiều! Chứ đụng chuyện mà đi làm đơn chờ thủ tục tới chừng nào.

**`s04_first_trap_aftermath` · `c04`** – Ba tuần sau (làm mờ quá trình dẫn dụ từng bước, đẩy thẳng vào hậu quả cao trào). Bong bóng **LỊCH SỬ NẠP · 3 TUẦN**: *"Nhiều đợt cộng dồn: 200.000.000đ · Chuyên viên chăm sóc: Ngọc"* (`SAU BA TUẦN`) → **ỨNG DỤNG ĐẦU TƯ LẠ**: *"Tài khoản đã bị đóng băng · Không thể kết nối máy chủ"* (`MẤT 200 TRIỆU`).
- `l11_thanh` **ÔNG THÀNH**: Ba tuần nay làm từng bước đều rút được lời… Sao vừa gom đủ hai trăm triệu chốt gói cuối là sập trang luôn?!

## HỒI 2 – NGƯỜI QUEN NGOÀI ĐỜI & CÁI TÀI KHOẢN MƯỢN TÊN
**`s05_reject_police` · `c05`** – Sáng hôm sau, Trang thấy ba thức trắng cả đêm với đống sao kê trên bàn.
- `l12_trang` **TRANG**: Ba dừng lại liền đi! Gọi tổng đài ngân hàng khóa giao dịch, rồi con chở ba ra công an trình báo ngay sáng nay.
- `l13_thanh` **ÔNG THÀNH**: Báo công an?! Chờ thủ tục tới chừng nào? Rồi người ta cười vô mặt, nói ông già mới về hưu đã bị gạt!
- `l14_trang` **TRANG**: Hai trăm triệu là tiền cả đời ba làm cực khổ. Ngoài ngân hàng với công an, ai truy được tiền trên mạng hả ba?
- `l15_thanh` **ÔNG THÀNH**: Tiền ba làm ra, tài khoản đứng tên ba, để ba tự lo! Cho ba ba ngày, ba nhờ chú Tám lần tới tận cửa.
- *(Trang nhìn ba rất lâu, im lặng — làm con không thể giật điện thoại hay nặng lời.)*

**`s06_meet_tam` · `c06`** – Quán cà phê trưa vắng. Bong bóng **BIÊN LAI CHUYỂN KHOẢN**: *"Người nhận: ••••• (TK ••••) · Tổng cộng 3 tuần: 200.000.000đ"* (`ĐƯA 5 TRIỆU ĐI HỎI`).
- `l16_thanh` **ÔNG THÀNH**: Chút tiền xăng xe cho mấy đứa nhỏ đi việc. Mày coi quen ai rành, lần giùm tao cái tài khoản này nha Tám.
- `l17a_tam` **ÔNG TÁM**: Mày chưa báo công an, cũng chưa nói kỹ với con Trang phải hông?
- `l17b_thanh` **ÔNG THÀNH**: Chưa, tao hẹn nó ba ngày tự lo.
- `l17c_tam` **ÔNG TÁM**: Ừ, để tao hỏi mấy đứa coi sao.

**`s07_tam_brushoff` · `c07`** – Tối hôm sau, Ông Thành đứng một mình bên hiên nhà nghe điện thoại giữa ánh hoàng hôn tắt dần.
- `l18_tam` **ÔNG TÁM** *(điện thoại)*: Tao hỏi mấy đứa rành chuyện này rồi. Tài khoản kiểu đó toàn đứng tên người bán giấy tờ, lần theo chẳng tới đầu nậu.
- `l19_thanh` **ÔNG THÀNH**: Vậy mày nhờ tụi nó lần tiếp giùm tao đi Tám! Tiền dưỡng già cả đời tao đó!
- `l20_tam` **ÔNG TÁM** *(điện thoại)*: Dính lừa trên mạng là dính pháp luật, mấy đứa nó hông đụng đâu. Mày tự ra công an đi.
- *(Cúp máy. Không ai nhắc tới 5 triệu.)*

## HỒI 3 – CÁI BẪY LẦN HAI: NHỬ TỪNG ĐỢT NHỎ & MỒI BẰNG CHỨNG
**`s08_search_alone` · `c08`** – Đêm đó, phòng khách tối. Bong bóng **NHÓM HỖ TRỢ LẤY LẠI TIỀN**: *"Cam kết lấy lại tiền bị treo trên sàn · Không thu tiền công trước"* (`QUẢNG CÁO`) + **BÌNH LUẬN**: *"Cảm ơn nhóm đã lấy lại 180 triệu cho chú tôi sau 3 ngày!"* (`TÀI KHOẢN ẢO`).
- `l22_khoa` **KHOA** *(điện thoại)*: Nói thật với chú Thành, chờ thủ tục lâu lắm. Bên em có đội kỹ thuật chuyên kéo tiền bị treo trên sàn về.
- `l23_thanh` **ÔNG THÀNH**: Tôi mới mất hai trăm triệu xong, cậu đừng hòng dụ ông già này lần nữa. Tụi cậu có gì chứng minh làm được thật?
- `l24_khoa` **KHOA** *(điện thoại)*: Chú cảnh giác là quá đúng. Bên em hông thu tiền công trước. Chú cứ gửi sao kê qua kiểm tra miễn phí.

**`s09_insider_detail` · `c09`** – Hai tiếng sau. Bong bóng **HỒ SƠ #094 · KIỂM TRA MIỄN PHÍ**: *"Khoanh nguồn tiền treo: 200.000.000đ · Chuyên viên bên sàn: Ngọc"* (`KHỚP DỮ LIỆU`).
- `l25_khoa` **KHOA** *(điện thoại)*: Bên em kiểm tra xong rồi. Bên sàn đó, chuyên viên chăm sóc chú ba tuần nay tên Ngọc, đúng hông chú?
- `l26_thanh` **ÔNG THÀNH**: Sao… sao cậu biết tên con nhỏ đó? Tôi đâu có gửi tin nhắn nào…
- `l26b_khoa` **KHOA** *(điện thoại)*: Bên em vẫn chưa lấy công. Chú thử nạp một triệu phí trích cổng, coi ảnh luồng tiền rồi hãy tính tiếp.

**`s09b_bait_proof` · `c09b`** – Ngay sau đó (`1tr` xem ảnh luồng tiền bị che `•••••` → `2tr` mở lịch sử chat cũ và phát lại ghi âm cuộc gọi cũ với Ngọc → `7tr` mở cổng giải tỏa). Bong bóng **GÓI TRÍCH DỮ LIỆU · 1TR -> 2TR**: *"Ảnh luồng tiền (TK •••••) · Lịch sử chat cũ · Ghi âm cuộc gọi với Ngọc"* (`BẰNG CHỨNG MỒI`).
- `l26d_ngoc_rec` **GHI ÂM · NGỌC** *(loa điện thoại)*: Chú Thành yên tâm, chốt đủ hai trăm triệu là tối nay rút gốc luôn nha chú.
- `l26e_thanh` **ÔNG THÀNH**: Trời… cả đoạn ghi âm bữa trước tôi nói chuyện với nó mà tụi cậu cũng kéo ra được! Coi như trong lòng bàn tay rồi!
- `l27_khoa` **KHOA** *(điện thoại)*: Mọi thứ nằm gọn trong tay rồi chú. Lệnh khóa giữ hai mươi bốn tiếng, chú đóng nốt bảy triệu mở cổng giải tỏa nha chú.
- *(Bong bóng **TỔNG CÁC ĐỢT NHỬ BAN ĐẦU**: `Trích luồng tiền: -1tr · Chat & ghi âm: -2tr · Mở cổng: -7tr (= -10.000.000đ)` · `ĐÃ ĐÓNG 10 TRIỆU`.)*

**`s10_doubt_and_lie` · `c10`** – Tối hôm sau, cạnh khe cửa phòng ngủ của mẹ con Trang hở đèn vàng ấm. Bong bóng **LỆNH CHỜ GIẢI NGÂN #094 · 95%**: *"Biên bản treo 200.000.000đ (mã cổng che mờ) · Bổ sung 15.000.000đ phí xác minh"* (`PHÁT SINH PHÍ`).
- `l28_thanh` **ÔNG THÀNH**: Khoan đã! Từ một triệu, hai triệu, bảy triệu… sao nay lại đẻ thêm mười lăm triệu?! Tụi cậu giở trò phải hông?
- `l29_khoa` **KHOA** *(điện thoại)*: Hồ sơ chạy tới chín mươi lăm phần trăm rồi chú. Chú nghi thì cứ hủy, tiếc hai trăm triệu với mười triệu vừa đóng thôi.
- `l30_trang` **TRANG** *(vọng qua khe cửa)*: Ba ơi, khuya rồi vô ngủ đi ba. Mai là hết ba ngày rồi, bên chú Tám lo tới đâu rồi ba?
- `l31_thanh` **ÔNG THÀNH**: Ờ… sắp xong rồi con. Con với thằng Bo ngủ trước đi.

**`s11_pawn_watch` · `c11`** – Khoa gửi màn hình **LỆNH HOÀN TIỀN #094 · CHỜ DUYỆT**: *"Hiển thị +200.000.000đ chờ vào TK (không mã tra soát) · Nộp 30.000.000đ giải ngân"* (`CHỈ CÒN 1 BƯỚC`) → Ông Thành tháo chiếc đồng hồ cơ kỷ niệm đặt lên quầy cầm đồ → Bong bóng **LỊCH SỬ CHUYỂN KHOẢN · 5 ĐỢT**: *"1tr + 2tr + 7tr + 15tr + 30tr · Tổng lần hai: -55.000.000đ"* (`CẠN SẠCH TIỀN`). *(câm)*

**`s12_mask_off` · `c12`** – Đêm cao trào 23:15, nối tiếp `l03`. Không nhạc. Cắt kết nối dứt khoát đúng bản chất thực dụng (hết tiền là dừng, không đôi co).
- `l32_khoa` **KHOA** *(điện thoại)*: Chú hông đóng đủ bốn chục triệu trong tối nay thì hồ sơ tự hủy. Bên em hết hỗ trợ.
- *(Cúp máy ngay lập tức. Bong bóng **ĐÃ CHẶN**.)*

## HỒI 4 – TRÌNH BÁO MUỘN MÀNG
**`s13_unanswered_call` · `c13`** – Nửa đêm, gọi Ông Tám không ai bắt máy.
- `l33_tam_mem` **ÔNG TÁM** *(tiếng vọng)*: Có chuyện gì cứ gọi một tiếng, mấy thằng em ngoài đời của tao lo liền.

**`s14_bare_wrist_confession` · `c14`** – Ánh đèn hành lang ấm nhạt; Trang ngồi đối diện, ánh mắt dừng lại ở cổ tay trái trống trơn không còn đồng hồ của ba.
- `l34_trang` **TRANG**: Hết sạch rồi hả ba?
- `l35_thanh` **ÔNG THÀNH**: Hai trăm triệu tiền dưỡng già… cộng thêm sáu chục triệu tiền phòng thân với cả chiếc đồng hồ… mất hết rồi con ơi.
- `l36_trang` **TRANG**: Giờ ba gọi tổng đài ngân hàng liền đi. Sáng mai con chở ba ra công an.

**`s15_police_truth` · `c15`** – Sáng hôm sau; cán bộ tiếp nhận mặc áo sơ mi trắng trơn, không sắc phục.
- `l37_cb` **CÁN BỘ**: Chú để gần năm ngày mới trình báo. Hai trăm triệu đầu chuyển đi lâu quá, xác minh khó hơn nhiều rồi.
- `l38_thanh` **ÔNG THÀNH**: Tôi có mấy hình luồng tiền với ghi âm cũ nhóm kia gửi… còn mấy khoản mới nộp thì sao cô?
- `l39a_cb` **CÁN BỘ**: Mấy khoản mới chuyển chú đưa đủ sao kê, chúng tôi tiếp nhận ngay để phối hợp ngân hàng xác minh theo quy trình.
- `l39b_cb` **CÁN BỘ**: Còn hình che số với ghi âm cũ không đủ cơ sở xác thực bên kia. Nhử phí từng đợt nhỏ, đó là lừa lần hai.

## HỒI 5 – ĐỐI DIỆN SỰ THẬT
**`s16_drawer_seen` · `c16`** – Chiều muộn một tuần sau; cất cuộn bản vẽ sửa nhà vào hộc tủ gỗ cũ. Bong bóng **ÔNG TÁM**: *"Tám ơi, tao đang kẹt xoay tiền, mày cho tao mượn tạm ít bữa…"* (`ĐÃ XEM · 3 NGÀY TRƯỚC`). *(câm)*

**`s17_grandson_question` · `c17`** – Hiên nhà lúc chạng vạng; Bé Bo kéo gấu áo ông ngoại, Trang phía cửa quay mặt đi giấu nước mắt.
- `l40_bo` **BÉ BO**: Ông ngoại ơi, chừng nào chú thợ qua làm phòng mới có cửa sổ cho con học lớp Một hả ông?

**`s18_face_the_truth` · `c18`** – Ông Thành ngồi ngang tầm cháu, bàn tay trái trống trơn xoa đầu cháu.
- `l41_thanh` **ÔNG THÀNH**: Chắc còn lâu lắm con… Ông ngoại tính sai rồi. Nhưng năm sau con vô lớp Một, ông vẫn tập viết với con mỗi tối.

**`s19_black_epilogue` · `c20`**
> **Kẻ lừa đầu tiên lấy tiền bằng lời hứa bạn sẽ có thêm.**
> **Kẻ thứ hai lấy nốt phần còn lại, bằng nỗi xấu hổ không dám nói ra.**

## THẺ NHỚ KỸ
- `l42_narr` **NGƯỜI BÓC TRẦN**: Giấu người nhà, nhờ người quen thay vì báo công an, là mở cửa cho lần lừa thứ hai.
1. **Ai hứa chắc kéo tiền về rồi nhử phí từng đợt:** dù bắt đầu chỉ 1–2 triệu hay xưng nhóm hỗ trợ, chuyên gia, đó vẫn là bẫy lừa lần hai.
2. **Người quen ngoài đời không truy được tiền:** truy vết dòng tiền là việc của ngân hàng và cơ quan điều tra; cẩn trọng cả với người dò hỏi hoàn cảnh gia đình.
3. **Ảnh che số, tin nhắn cũ, ghi âm cũ không xác thực được bên kia:** kẻ gian có thể chung một đầu mối với nhóm đã lừa bạn lần đầu.
4. **Dừng từ khoản phí đầu tiên:** không bỏ thêm tiền thật để cứu khoản tiền đã mất.
5. **Báo càng sớm càng có cơ hội:** gọi tổng đài ngân hàng, lưu sao kê, trình báo công an và đừng giấu người nhà.

## KẾT MỞ – CÙNG MỘT ĐẦU MỐI & BÓNG LƯNG QUEN THUỘC
**`s21_scam_ring_coda` · `c19`** – Phòng tối, không lộ mặt. Bong bóng **HỒ SƠ TUẦN NÀY**: *"Vòng 1 (3 tuần): -200.000.000đ  ->  Vòng 2 (5 đợt): +55.000.000đ"* (`CHUYỂN VÒNG 2`).
- `l43_khoa_coda` **KHOA**: Hồ sơ hai trăm triệu con Ngọc chuyển qua, nhử năm đợt bên em chốt thêm năm mươi lăm triệu rồi anh.

**`s21b_tam_coda` · `c19b`** – *(Cắt chuyển liền ngay sau câu báo cáo của Khoa — hoàn toàn câm, không thoại, không bong bóng.)* Quán cà phê ngoài trời tại một **địa bàn khác ven biển** ngập nắng gió. Thấy từ phía sau **bóng lưng quen thuộc** (tóc muối tiêu chải ngược, áo polo đen) của **Ông Tám** giơ bàn tay đeo **chiếc lắc bạc** vẫy chào thân thiện một **lão ngư dân da sạm nắng** (đội nón lá, quàng khăn cổ, áo lao động xanh bạc màu) đang bước tới từ xa; trên bàn gỗ bên ly cà phê đá là chiếc điện thoại sáng **giao diện ứng dụng đã sập quen thuộc ở `c04`**.

**`s22_black_cut`** – Cắt đen đột ngột (`impact`). **`s23_disclaimer`** – LƯU Ý.

---

## Tự kiểm "Không dạy lừa" & "Không bôi nhọ" & "Không kỳ thị"
- [x] Không có "anh hùng mạng", "hiệp sĩ", "văn phòng pháp lý", "hỗ trợ pháp lý", "luật sư", "tài sản số" trong phim và metadata. Nhóm giả luôn là **tự xưng**.
- [x] Không mô tả cách lập sàn giả, cách dựng biên bản giả hay cách móc nối ngoài đời; cảnh câm `s21b` chỉ dùng tín hiệu thị giác tối giản (bóng lưng, địa bàn khác, giao diện app quen thuộc) để khán giả tự suy ngẫm.
- [x] Thẻ Nhớ Kỹ đánh vào **hành vi** (hứa chắc + nhử phí từng đợt nhỏ + bằng chứng mồi không xác thực), không đánh vào nghề nghiệp, tuổi tác hay cộng đồng nào.
- [x] Kết mở nhấn mạnh nạn nhân bị lọc theo **hành vi giấu con cháu / chưa trình báo**, không kỳ thị người cao tuổi.
- [x] Cán bộ không hứa lấy lại tiền; nói chuẩn mực "tiếp nhận ngay để phối hợp ngân hàng xác minh theo quy trình" và chỉ rõ hình che số/ghi âm cũ không đủ cơ sở xác thực bên kia.
- [x] Sạch `policy_wordlists.json` và regex Gate 5 (0 hard block, 0 soft warn, 0 SĐT/URL/STK).

## ⚠️ Cần người có chuyên môn kiểm chứng trước khi chuyển Clearance sang ĐẠT
- [ ] `l39a_cb` & `l39b_cb`: cách nói của cán bộ về "tiếp nhận ngay để phối hợp ngân hàng xác minh theo quy trình" và giá trị xác thực của ảnh chụp/ghi âm do bên thứ ba gửi.
- [ ] `l18_tam`: mô tả "tài khoản đứng tên người bán giấy tờ" là thông tin phổ biến trên báo chí, không mang tính hướng dẫn.
- [ ] Người duyệt xem kỹ toàn bộ hàm ý của tuyến nhân vật bí ẩn **Ông Tám** (`s03`, `s06`, `s21b`) và sắc thái tuổi 65 trước khi ký Clearance.
