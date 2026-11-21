# EP08 – MỘT VÒNG TIỀN, HAI NỬA SỰ THẬT *(Bản kịch hóa điện ảnh – v2-draft)*

- **Mã tập:** `EP08` · **Slug:** `MotVongTienHaiNuaSuThat`
- **Họ kịch bản:** `IMPERSONATION-MITM` – Bẫy "người đứng giữa" trên ứng dụng nhắn tin (không nêu tên nền tảng/thương hiệu). Kẻ gian đọc lén tài khoản của **Anh Đạt** (chủ xưởng nội thất nhỏ), không chỉ nắm thông tin *kỷ niệm 10 năm ngày cưới* mà còn học **đúng cách nói chuyện cộc gọn đặc trưng** (*"cu Khang"*, *"chị nhà"*, *"lộ bài"*, *"làm gọn giùm anh, anh tính"*). Sáng hôm sau, nick giả **nhá cuộc gọi video hình/giọng ghép 3 giây rồi cúp đổ tại mạng yếu** để Khang tin tuyệt đối, rồi đạo diễn để Khang gọi số thật của Đạt xin ứng `45 triệu` (`ND: Ung luong`) và đẩy tiền qua tài khoản lạ. Chiều cùng ngày, kẻ gian tham đòi thêm `30 triệu` thì Đạt sinh nghi và vỡ lẽ. **Kết mở lặng người (không đường dây ngầm):** Chiều hôm sau ở quán cà phê quen, hai người từng tin nhau như anh em lặng lẽ *xin bằng chứng của nhau để phòng thân*.
- **Định dạng:** `16:9` (`1920x1080 @ 30fps`) · **Tỷ lệ:** **~97% kịch tâm lý – điện ảnh / ~3% Người Bóc Trần (< 10 giây)**
- **Nguồn sự thật của timeline:** [`source/build_draft.py`](../source/build_draft.py) → sinh [`episode.json`](../episode.json).

## Thay đổi ở v2-draft (theo góp ý đạo diễn)
1. **Bỏ sạch 2 bong bóng giải thích dài ở `s03`:** Thêm nhân vật **Đàn em kỹ thuật** (`Achird`, giấu mặt trong phòng tối) đối thoại trực tiếp 4 câu ngắn gọn với **Kẻ đứng giữa** (`Fenrir`) để khán giả **nghe là hiểu trọn cơ chế ngay lập tức**, không phải căng mắt đọc chữ.
2. **Bổ sung cú nhá gọi hình/giọng ghép 3 giây (`s04_fake_video_call`):** Trước khi nhắn chuyện tiền bạc, nick mới gọi video chập chờn 3 giây hiện đúng mặt và giọng cắt ghép của Anh Đạt rồi cúp đổ tại mạng yếu — đủ thuyết phục thực tế vì sao Khang không nghi ngờ tài khoản mới.
3. **Khắc sâu khẩu ngữ riêng của Anh Đạt (không chỉ biết thông tin):** Cài rõ bộ khẩu ngữ đặc trưng của Anh Đạt ở `s02` (*"Nè cu Khang"*, *"chị nhà"*, *"lộ bài"*, *"gọn ghẽ / làm gọn giùm anh, anh tính"*) → đàn em phân tích ở `s03` → kẻ đứng giữa nhái y hệt ở `s04`, `s05`, `s08`, `s10` → Khang nhắc lại trong bàng hoàng lúc đối chất `s12`.

## Nhân vật & giọng (`02_CAST/cast.json` – 8 tuyến / 8 voice độc lập)
| Nhân vật | Key | Voice | Chỉ đạo giọng |
|---|---|---|---|
| **Anh Đạt** (38t, chủ xưởng nội thất nhỏ) | `anh_hai` | `Orus` | Nam trầm chắc, điềm tĩnh, nói cộc gọn thực dụng *(bản `DAT_FAKE` dùng đúng `Orus` + `phone` cho cú gọi ghép 3 giây)* |
| **Khang** (26t, kỹ thuật viên theo Đạt 3 năm) | `thang_tun` | `Puck` | Nam trẻ sáng, nhịp nhanh gọn, thật thà lễ phép *(có bản `phone` — đồng bộ sang cú echo đầu `EP08b`)* |
| **Chị Quyên** (36t, vợ Anh Đạt) | `chi_hai` | `Sulafat` | Nữ trầm vừa, thực tế, kiệm lời, quản lý tài khoản chung |
| **Hân** (27t, đồng nghiệp bàn kế Khang) | `chi_tu` | `Zephyr` | Nữ trẻ sáng gọn, thân thiện kiểu công sở |
| **Kẻ đứng giữa** (ẩn mặt phòng tối) | `chu_no` | `Fenrir` | Nam 40t trầm đều, lạnh tĩnh *(đồng bộ 100% sang `EP08b`)* |
| **Đàn em kỹ thuật** (ẩn mặt phòng tối) | `ke_ngot_ngao_nam` | `Achird` | Nam 28t gọn, tỉnh bơ, chỉ xuất hiện ở `s03` bàn kế hoạch |
| **Đầu dây lạ *(Long ở `EP08b`)*** | `ke_ngot_ngao_nam` | `Algieba` | Nam 32t mượt lịch sự (`phone`), chỉ vang 1 câu cài mạch ở `s08` lúc `12:05` |
| **Người Bóc Trần** | `nguoi_boc_tran` | `Charon` | Đúng 1 câu (22 từ, `< 10s`) ở thẻ `NHỚ KỸ` |

## Tự kiểm "Không dạy lừa"
- Tuyệt đối không mô tả cách chiếm tài khoản, không nêu tên phần mềm hay quy trình kỹ thuật làm hình/giọng ghép; chỉ phản ánh đúng bản chất cảnh báo (*tin nhắn cũ bị đọc lén + cuộc gọi hình ghép 3 giây đổ mạng yếu*).

---

## HOOK – CUỘC GỌI LẦN HAI & CÂU HỎI ĐÓNG BĂNG
**`s00_hook_call` · `c00`** – 16:15 chiều. Phòng làm việc xưởng nội thất. *(Bong bóng: "CUỘC GỌI ĐẾN · KHANG: Lần 2 trong ngày · Xin mượn thêm 30.000.000đ" · `LẦN THỨ HAI`)*.
- `l01_dat` **ANH ĐẠT**: Sáng mày mới xin ứng bốn lăm triệu. Giờ mới chiều đã hỏi thêm ba chục… Mày vướng chuyện gì nói thiệt anh coi!
- `l02_khang_p` **KHANG** *(điện thoại)*: Ủa anh… em đang gọi diễn đúng như lời anh nhắn hồi nãy mà!
- `l03_dat` **ANH ĐẠT**: Tao nhắn cho mày hồi nào?!

**`s01_hook_freeze` · `c01`** – Chớp trắng! Cận cảnh Khang sững người ở đầu dây bên kia, tay cầm điện thoại mở khung chat nick giả. *(Bong bóng: "ANH ĐẠT (NICK MỚI): Mượn anh thêm 30.000.000đ · Như sáng nay" · `AI ĐANG NHẮN?`)*. *(Nhịp tim, câm).*

---

## HỒI 1 – HAI HÔM TRƯỚC: CÁCH NÓI CHUYỆN & KẾ HOẠCH PHÒNG TỐI
**`s02_trust_coffee` · `c02`** – Quán cà phê sáng quen gần xưởng, nắng trong, **hai ly cà phê đá** trên bàn gỗ *(cài khẩu ngữ đặc trưng của Anh Đạt + bối cảnh cho cảnh kết)*.
- `l04_dat` **ANH ĐẠT**: Nè cu Khang, mấy công trình đợt này mày chạy gọn ghẽ quá. Cuối tháng anh tính thêm cho.
- `l05_khang` **KHANG**: Anh em làm chung ba năm rồi, tính toán chi anh. Có việc gì cứ kêu em.
- `l06_dat` **ANH ĐẠT**: Ừ, tuần sau kỷ niệm mười năm ngày cưới. Rảnh phụ anh kiếm quà cho chị nhà, đừng để bả biết lộ bài nghen.
- `l07_khang` **KHANG**: Dạ dễ ợt, anh chọn xong cứ nhắn em làm gọn.

**`s03_dark_room_plan` · `c03`** – Đêm hôm trước. Phòng tối ánh xanh lạnh: **hai bóng lưng/bàn tay giấu mặt** bên cạnh hai chiếc điện thoại đặt song song. *(KHÔNG dùng bong bóng chữ — bàn thẳng bằng đối thoại cực rõ)*.
- `l08_tech` **ĐÀN EM**: Tin nhắn cũ của ông Đạt em đọc kỹ rồi. Ổng nói cộc lắm, cứ mở miệng kêu cu Khang, gọi vợ là chị nhà.
- `l09_ke` **KẺ ĐỨNG GIỮA**: Tốt, nhắn y chang kiểu đó. Tới lúc cần thì nhá cuộc gọi hình ghép ba giây, cắt giọng từ tin cũ rồi cúp liền.
- `l10_tech` **ĐÀN EM**: Đổ tại mạng yếu là nó tin liền. Mà mượn thẳng thằng Khang thì sao nó có tiền nhiều?
- `l11_ke` **KẺ ĐỨNG GIỮA**: Không mượn nó. Bày nó gọi số thật ông Đạt xin ứng bốn lăm triệu. Sếp tự chuyển cho lính, rồi lính đẩy qua mình.

---

## HỒI 2 – SÁNG HÔM SAU: CUỘC GỌI HÌNH GHÉP & NHÁI GIỌNG SẾP
**`s04_fake_video_call` · `c04`** – Văn phòng xưởng sáng nắng. Điện thoại Khang đổ chuông video từ nick mới của Anh Đạt: hiện thoáng gương mặt giống Anh Đạt bị giật hình mờ nhẹ rồi ngắt phụt. *(Bong bóng: "CUỘC GỌI VIDEO · ANH ĐẠT (NICK MỚI): Tín hiệu yếu · Đã kết thúc (00:03)" · `HÌNH GHÉP 3 GIÂY`)*.
- `l12_dat_fake` **ANH ĐẠT (HÌNH GHÉP)** *(điện thoại + glitch)*: Nè cu Khang! Mạng chỗ xưởng gỗ yếu quá hình giật hết trơn… Thôi cúp nha, anh nhắn tin cho gọn!
- *(Glitch + Tút! Cuộc gọi ngắt gọn trong 3 giây).*

**`s05_fake_step1_dark` · `c05`** – Cắt ngay sang phòng tối ánh xanh lạnh: bàn tay kẻ đứng giữa gõ trên chiếc điện thoại bên phải, nhái y hệt cách nói chuyện của Anh Đạt. *(Bong bóng: "ANH ĐẠT (NICK MỚI): Gọi số cũ xin ứng 45tr · Giữ bí mật cho chị nhà" · `NHỊP 1 · NHÁI GIỌNG`)*.
- `l13_ke` **KẺ ĐỨNG GIỮA** *(phòng tối)*: Nè cu Khang, anh đặt đồng hồ kỷ niệm cho chị nhà rồi. Tài khoản chung anh tự chuyển là lộ bài liền.
- `l14_ke` **KẺ ĐỨNG GIỮA** *(phòng tối)*: Trưa nay gọi số cũ xin ứng bốn lăm triệu, nói dưới quê có việc gấp. Làm gọn giùm anh, xong việc anh tính.

**`s06_office_relay` · `c06`** – Văn phòng xưởng sáng nắng. Khang đọc xong gật đầu đứng dậy *(không tự nói một mình)*. Hân ngồi bàn bên hỏi tự nhiên.
- `l15_han` **HÂN**: Ủa Khang, gần trưa rồi còn đi đâu mà cười tủm tỉm vậy?
- `l16_khang` **KHANG**: Anh Đạt nhờ đặt quà kỷ niệm cho chị nhà. Ảnh mới gọi hình qua nick mới mà mạng yếu quá nên nhắn tiếp.
- `l17_han` **HÂN**: Chà, sếp cưng vợ ghê ha. Mà sao ảnh hông tự chuyển tiền luôn?
- `l18_khang` **KHANG**: Tài khoản nhà chị Quyên giữ chung, ảnh tự chuyển lộ bài liền. Tiền của ảnh mà, mình phụ một tay thôi.

---

## HỒI 3 – BUỔI TRƯA: DÒNG TIỀN ĐI MỘT VÒNG
**`s07_real_call_home` · `c07`** – 11:45 trưa. Nhà Anh Đạt ấm cúng; Đạt nghe cuộc gọi thật từ số Khang, Chị Quyên ngồi cạnh bên bàn cơm.
- `l19_khang_p` **KHANG** *(điện thoại)*: Alo anh Đạt… Dưới quê nhà em đột xuất có việc gấp, anh cho em ứng trước bốn lăm triệu được hông?
- `l20_dat` **ANH ĐẠT**: Chuyện gấp hả cu Khang? Rồi, để anh chuyển qua tài khoản mày liền, lo xong rồi tính.
- `l21_quyen` **CHỊ QUYÊN**: Thằng Khang làm với mình ba năm nay đàng hoàng. Anh cứ ghi rõ nội dung ứng lương rồi chuyển cho nó đi.
- *(Ting! Bong bóng: "NGÂN HÀNG CỦA ĐẠT: Chuyển sang Khang: -45.000.000đ · ND: Ung luong" · `1 · ĐẠT → KHANG`)*.
- `l22_dat` **ANH ĐẠT**: Rồi, anh mới chuyển bốn lăm triệu xong đó. Lo gọn việc dưới quê đi nghen.

**`s08_dark_step2_account` · `c08`** – 12:05 trưa. Phòng tối ánh xanh lạnh: bàn tay kẻ đứng giữa bên 2 chiếc điện thoại (màn hình phụ phía sau hắt thoáng **bóng mờ chiếc xe máy tay ga xám bạc + chấm sáng bìa hồ sơ đỏ** — cài thị giác nối sang `EP08b`). Từ loa ngoài điện thoại trái vang gọn 1 câu giọng `Algieba` (chính là Long ở `EP08b`), rồi kẻ đứng giữa gửi số tài khoản lạ cho Khang. *(Bong bóng: "ANH ĐẠT (NICK MỚI): Chuyển 45.000.000đ vô TK cửa hàng này" · `2 · GỬI STK LẠ`)*.
- `l22b_long_p` **ĐẦU DÂY LẠ** *(loa điện thoại – giọng Long `EP08b`)*: Em tới quầy công chứng rồi, bên bán chờ tiền vô là ký.
- `l23_ke` **KẺ ĐỨNG GIỮA** *(phòng tối)*: Tiền vô rồi hả cu Khang? Đẩy bốn lăm triệu vô số tài khoản cửa hàng này gọn giùm anh, họ giao thẳng về xưởng.

**`s09_khang_transfers` · `c09`** – Góc văn phòng giờ trưa. Khang mở ngân hàng thấy tiền từ Anh Đạt đã vào, bình thản bấm chuyển tiếp trọn 45 triệu đi. *(Bong bóng: "NGÂN HÀNG CỦA KHANG: Đã chuyển: -45.000.000đ → TK ••••" · `3 · KHANG → KẺ GIAN`)*. *(Nhịp câm nhìn rõ dòng tiền rời tay).*

---

## HỒI 4 – BỐN GIỜ CHIỀU: NHỊP THỨ HAI & PHÚT VỠ LẼ
**`s10_second_attempt_dark` · `c10`** – 16:05 chiều. Phòng tối ánh xanh lạnh: kẻ đứng giữa tiếp tục gõ đòi thêm lần hai. *(Bong bóng: "ANH ĐẠT (NICK MỚI): Gọi số cũ mượn anh thêm 30.000.000đ" · `NHỊP 2 · ĐÒI THÊM`)*.
- `l24_ke` **KẺ ĐỨNG GIỮA** *(phòng tối)*: Cu Khang, cửa hàng còn thêm món quà kèm đẹp quá. Gọi số cũ mượn anh thêm ba chục triệu, làm gọn giùm anh nha.

**`s11_real_call_suspect` · `c11`** – 16:15 chiều. Xưởng nội thất (nối ngay sau câu hỏi ở Hook).
- `l25_dat` **ANH ĐẠT**: Mày đứng yên đó, chạy thẳng qua phòng anh ngay! Đem cái điện thoại qua đây cho anh coi!

**`s12_confrontation_desk` · `c12`** – 16:25 chiều. Phòng làm việc của Anh Đạt — bố cục cắt ngang Trái (Đạt) – Phải (Khang), hai chiếc điện thoại đặt cạnh nhau trên mặt bàn.
- `l26_khang` **KHANG**: Anh coi nè! Hồi sáng nó còn gọi hình đúng mặt đúng giọng anh, nhắn y chang kiểu cu Khang, chị nhà luôn mà!
- `l27_dat` **ANH ĐẠT**: Tài khoản này đâu phải của anh! Mà sao nó có clip mặt anh với biết tuần sau kỷ niệm ngày cưới?!
- `l28_dat` **ANH ĐẠT**: Khoan… hồi khuya máy anh có báo đăng nhập từ thiết bị khác. Anh tưởng lỗi mạng nên bấm bỏ qua mất tiêu rồi!
- *(Gọi lại nick giả — tút tút thuê bao).*
- `l29_khang` **KHANG**: Nó chặn mất rồi anh Đạt ơi… Bốn mươi lăm triệu em vừa chuyển qua tài khoản lạ rồi!
- `l30_dat` **ANH ĐẠT**: Bình tĩnh lại. Gọi tổng đài ngân hàng liền đi, rồi gom hết sao kê với tin nhắn đi trình báo công an!

---

## HỒI 5 – CHIỀU HÔM SAU: THỨ MẤT ĐI KHÔNG CHỈ LÀ TIỀN *(KẾT MỞ LẶNG NGƯỜI)*
**`s13_coffee_aftermath` · `c13`** – Đúng quán cà phê quen đầu phim (`c02`), vẫn **hai ly cà phê đá** trên bàn gỗ, nhưng trời chiều xám lạnh. Đạt (trái) và Khang (phải) ngồi đối diện, trầm lặng.
- `l31_khang` **KHANG**: Bên ngân hàng nói tiền đi qua nhiều lớp rồi, khó giữ kịp… Bốn lăm triệu đó để em góp lương trả dần.
- `l32_dat` **ANH ĐẠT**: Thôi, coi như hai anh em xui. Chuyện tiền nong cứ để từ từ tính.
- `l33_dat` **ANH ĐẠT**: À… mấy đoạn tin nhắn với nick giả hôm qua, em chụp lại đủ hết rồi gửi cho anh giữ một bản nha.

**`s14_silent_crack` · `c14`** – Cận cảnh Khang ở bên phải: tay cầm ly cà phê đá khựng lại nửa nhịp, mắt liếc xuống màn hình điện thoại đang sáng dòng sao kê ngân hàng. *(Bong bóng: "SAO KÊ NGÂN HÀNG: Anh Đạt → Khang: +45.000.000đ · ND: Ung luong" · `CHỨNG TỪ DUY NHẤT`)*.
- `l34_khang` **KHANG**: Dạ. Vậy anh cũng chụp gửi em cái thông báo tài khoản anh bị đăng nhập lạ hôm kia… để em giữ.

**`s15_black_cut` · `c15`** – **IMPACT TRẦM + CẮT ĐEN ĐỘT NGỘT!** *(Không đường dây ngầm — để dư âm rạn nứt lắng trọn vẹn).*

---

## THẺ NHỚ KỸ *(DƯỚI 10 GIÂY)*
**`s16_red_flags`** *(nền `EP01b/scene18.jpg`)*
- `l35_narr` **NGƯỜI BÓC TRẦN**: Mặt, giọng hay cách nói đều giả được. Cứ dính tiền mà dặn giữ bí mật, hãy gọi số thật hỏi thẳng.

**`s17_disclaimer`** – LƯU Ý.
