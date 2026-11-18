# EP05 – TỜ NĂM TRĂM VÀ SÁU GIÂY NHÌN THẲNG *(Bản kịch hóa điện ảnh – v1)*

- **Mã tập:** `EP05` · **Slug:** `ToNamTramVaSauGiayNhinThang`
- **Họ kịch bản:** `MIX` – Dàn cảnh 2 chốt ngoài đời thực: **Chốt 1** thu ảnh căn cước & SĐT qua quà tặng nhỏ (hộp bình nước màu cam làm dấu hiệu nhận diện) → **Chốt 2** đóng vai người trung niên mắt mờ đưa **tờ 500.000đ tiền mặt thật trước** để lấy số tài khoản, rồi nhờ cầm điện thoại bấm thoát màn hình đơ để thu **6 giây khuôn mặt sống + giọng đọc xác nhận** → Bẫy **"giải ngân mồi"** (`+3,5 triệu` đòi `6 triệu`) đánh vào sĩ diện nơi làm việc.
- **Định dạng:** `16:9` (`1920x1080 @ 30fps`) · **Thời lượng ước tính:** `~4:15` (căn theo WAV thật sau Gate 2)
- **Tỷ lệ:** **97% kịch tâm lý đời sống / 3% Người Bóc Trần (đúng 1 câu dưới 10 giây ở thẻ kết)**
- **Nguồn sự thật của timeline:** [`source/build_draft.py`](../source/build_draft.py) → sinh [`episode.json`](../episode.json). Sửa thoại ở file build rồi chạy lại, **không sửa tay `episode.json`**.

## Nhân vật & giọng (`02_CAST/cast.json` – 8 nhân vật / 8 voice tách biệt 100%)
| Nhân vật | Key | Voice | Chỉ đạo giọng |
|---|---|---|---|
| **Anh Hai** (35t) | `anh_hai` | `Orus` | Nam trầm ấm, thẳng tính, đàng hoàng; không gào khóc bi lụy |
| **Chị Hai** (34t) | `chi_hai` | `Sulafat` | Nữ trầm vừa, kiệm lời, thực tế, nói câu nào chắc câu đó |
| **Bé Tom** (8t) | `be_tom` | `Puck` | Bé trai trong sáng, lễ phép, tự nhiên đời thực |
| **Cô Lành** (~50t) | `co_hanh` | `Despina` | Mượt, hiền lành thân tình lúc nhờ giúp; **tuyệt đối không giả giọng bà già run rẩy** |
| **Đầu dây đòi nợ** | `chu_no` | `Fenrir` | Trầm, đều, lịch sự lạnh băng (`af: phone`) |
| **Nhân viên quầy quà** | `ke_ngot_ngao_nu` | `Aoede` | Nữ trẻ tươi tắn, lịch sự (1 câu) |
| **Giao dịch viên ngân hàng** | `chi_tu` | `Zephyr` | Nữ điềm tĩnh, chuẩn mực nghiệp vụ (3 câu ngắn) |
| **Người Bóc Trần** | `nguoi_boc_tran` | `Charon` | Đúng 1 câu (~6,5 giây) ở thẻ kết `NHỚ KỸ` |

## Bản đồ cài – trả
| Cài | Chi tiết | Trả |
|---|---|---|
| `c02` | **Hộp bình nước màu cam** nhận sau khi chụp căn cước | `c03` ánh mắt Cô Lành liếc hộp cam nhận diện con mồi → `c06` tin nhắn *"Khách hộp cam áo xám"* → `c11` bình nước cam bên hông Tom chiều tan học |
| `c02` | Câu tự tin: *"Giờ đụng tới tiền bạc đều phải quét mặt sống hết rồi"* | `c01` & `c04`: Chính Anh Hai tự nộp mặt sống + giọng đọc chỉ 2 phút sau |
| `c03` | **Tờ 500.000đ tiền mặt thật** đưa trước + câu đọc xác nhận | `c01`: Biến thành tệp đính kèm khống chế đòi 6 triệu sau khoản giải ngân mồi 3,5 triệu |
| `c03–c04` | Cặp kính lão & đôi tay run của Cô Lành | `c06` *(cảnh câm)*: Tháo kính lão, tay vững như đá nhận `+300.000` tiền công |
| `c05` | Tay nhặt rau của Chị Hai khựng lại nửa giây | `c07–c08`: Chị Hai không trách một lời, giữ cổ tay chồng kịp lúc trước cú chuyển tiền trả nợ khống |
| `c01` | Đòn đánh vào sĩ diện: *"Sáng thứ Bảy cả xưởng anh xem clip này"* | `c07` suýt tự bù 2,5 triệu tiền túi → `c08` & `c10` báo xưởng trước một bước khiến kẻ đòi nợ cúp máy chặn số |

---

## HOOK – MÓN NỢ TỪ CHÍNH GƯƠNG MẶT MÌNH
**`s00_night_ping` · `c00`** – Đêm. Phòng khách nhà Anh Hai. *(Bong bóng: "NGÂN HÀNG X: +3.500.000 VND · ND: GIAI NGAN HD 6.000.000")*. Số lạ gọi thẳng vào máy. Thẻ hook: **BẪY LÒNG TỐT NGOÀI ĐỜI · ĐÊM THỨ NĂM – TỜ NĂM TRĂM & SÁU GIÂY NHÌN THẲNG**.
- `l01_ah` **ANH HAI**: Alo, ai mới chuyển nhầm tiền vậy?
- `l02_cn` **SỐ LẠ** *(điện thoại)*: Không ai chuyển nhầm hết anh Hai. Hợp đồng sáu triệu của anh tới hạn thứ Sáu.
- `l03_ah` **ANH HAI**: Anh nói bậy gì đó, tôi vay hồi nào?

**`s01_mirror_shock` · `c01`** – Tin nhắn đính kèm bật lên giữa cuộc gọi: Ảnh căn cước 2 mặt ghép sát đoạn video 6 giây quay cận mặt Anh Hai ngoài bãi xe nắng gắt.
- `l04_ah_clip` **ANH HAI (TRONG CLIP)** *(loa điện thoại)*: Tôi xác nhận đồng ý thực hiện hồ sơ…
- `l05_cn` **SỐ LẠ** *(điện thoại)*: Mặt anh, tiếng anh, căn cước của anh đủ hết. Trễ hẹn thì sáng thứ Bảy cả xưởng anh xem clip này.
- *(Cúp máy. Anh Hai chết lặng; sau rèm buồng Chị Hai đứng nhìn chồng.)*

## HỒI 1 – CHIẾC HỘP CAM & TẤM HÌNH CĂN CƯỚC
**`s02_promo_desk` · `c02`** – Sáng Chủ Nhật, 4 ngày trước. Quầy quà tặng trước sảnh nhà sách. Bé Tom chỉ vào chiếc bình nước đựng trong hộp giấy màu cam.
- `l06_tom` **TOM**: Ba ơi, mình đăng ký lấy cái bình màu cam nghen ba!
- `l07_vy` **QUẦY QUÀ**: Dạ quà tặng cho bé, anh cho em chụp căn cước với số điện thoại để tránh nhận trùng nha.
- `l08_ah` **ANH HAI**: Chụp cái hình thôi mà. Giờ đụng tới tiền bạc đều phải quét mặt sống hết rồi.

## HỒI 2 – TỜ NĂM TRĂM TIỀN THẬT & SÁU GIÂY NHÌN THẲNG
**`s03_parking_approach` · `c03`** – Bãi giữ xe ngoài trời, 2 phút sau. Cô Lành đeo kính lão đứng cạnh dãy xe máy; **ánh mắt liếc nhanh xuống chiếc hộp màu cam trên tay Tom**, rồi bước tới chìa tờ 500.000đ tiền mặt thật ra trước.
- `l09_la` **CÔ LÀNH**: Chú ơi, làm ơn giúp chị với. Chị đóng tiền thuốc mà thẻ lỗi hoài, chú đổi giùm chị năm trăm tiền mặt nghen.
- `l10_ah` **ANH HAI**: Dạ được chị. Chị đọc số tài khoản đi em chuyển cho.

**`s04_six_seconds_face` · `c04`** – Cắt ngang Trái – Phải. Cô Lành luống cuống đưa chiếc điện thoại của bà ta lên ngang tầm mặt Anh Hai.
- `l11_la` **CÔ LÀNH**: Khổ thiệt, mắt chị mờ quá, bấm trúng đâu nó hiện khung chữ nhỏ xíu. Chú cầm đọc giùm chị rồi bấm tắt cái!
- `l12_ah` **ANH HAI**: Tôi xác nhận đồng ý thực hiện hồ sơ… Rồi, em bấm thoát giùm chị rồi đó.
- `l13_la` **CÔ LÀNH**: Cảm ơn hai cha con nhiều lắm, đúng là gặp quý nhân!

**`s05_home_noon` · `c05`** – Bếp nhà Anh Hai buổi trưa. Hộp màu cam và tờ 500.000đ trên bàn.
- `l14_tom` **TOM**: Mẹ ơi, sáng nay ba mới giúp một bà cô mắt mờ ngoài bãi xe đó!
- `l15_ch` **CHỊ HAI**: Giúp sao vậy anh?
- `l16_ah` **ANH HAI**: Bả đưa tờ năm trăm trước, nhờ anh chuyển khoản rồi bấm tắt giùm cái màn hình đơ.
- *(Tay nhặt rau của Chị Hai khựng lại nửa giây.)*

**`s06_glasses_off` · `c06`** – Góc khuất hàng cây sau bãi xe. Cô Lành tháo kính lão, tay vững như đá. Bong bóng: *"Khách hộp cam áo xám: Đã khớp căn cước quầy trong. Sáu giây mặt với tiếng nét căng."* → *"+300.000 VND · Công chốt ca sáng"*. *(câm)*

## HỒI 3 – CÁI BẪY "TRẢ CHO ÊM CHUYỆN"
**`s07_midnight_temptation` · `c07`** – 22:00 Đêm tại nhà. Tin nhắn hối chuyển `6.000.000` vào `TK cá nhân …9104`. Anh Hai định lấy 3,5 triệu lạ bù thêm 2,5 triệu tiền nhà chuyển đi; Chị Hai giữ chặt cổ tay chồng.
- `l17_ch` **CHỊ HAI**: Anh chuyển vô tài khoản cá nhân đó, lấy gì chắc tụi nó xóa clip?
- `l18_ah` **ANH HAI**: Bù có hai triệu rưỡi tiền mình thôi em… Chứ mai nó rải clip khắp xưởng, anh nhìn mặt ai?
- `l19_ch` **CHỊ HAI**: Nó thấy anh sợ mất mặt mà chịu trả lần đầu, tuần sau chính cái clip đó sẽ đẻ ra khoản thứ hai.

**`s08_lockdown_first_strike` · `c08`** – Hai vợ chồng ngồi cạnh nhau xử lý ngay trong đêm.
- `l20_ch` **CHỊ HAI**: Ba triệu rưỡi đó cứ để nguyên. Giờ anh khóa thẻ online rồi hạ hết hạn mức chuyển khoản xuống thấp nhất đi.
- `l21_ah` **ANH HAI**: Để anh báo trước cho anh em trong xưởng một tiếng. Mình nói trước thì nó hết đường hù.
- *(Bong bóng tin nhắn báo trước gửi vào nhóm xưởng cơ khí.)*

## HỒI 4 – KHOANH GIỮ TIỀN LẠ & LẬP BIÊN BẢN
**`s09_bank_counter` · `c09`** – Sáng hôm sau tại quầy ngân hàng.
- `l22_gdv` **NGÂN HÀNG**: Ngân hàng chính thống bắt buộc quét chip căn cước thật, nên kẻ gian không mở trộm khoản vay ngân hàng dưới tên anh được.
- `l23a_gdv` **NGÂN HÀNG**: Em đã cập nhật lại khuôn mặt và tra tín dụng cá nhân của anh, hoàn toàn không có nợ vay.
- `l23b_gdv` **NGÂN HÀNG**: Còn khoản ba triệu rưỡi chuyển vào không rõ nguồn, ngân hàng sẽ khoanh giữ chờ công an xử lý.

**`s10_police_gate_call` · `c10`** – Trưa cùng ngày, trước hiên trụ sở cơ quan công an. **Không nhạc nền.**
- `l24_cn` **SỐ LẠ** *(điện thoại)*: Quá giờ rồi đó anh Hai. Chuyển sáu triệu hay để tôi gửi clip vô xưởng?
- `l25_ah` **ANH HAI**: Xưởng tôi báo hết từ tối qua rồi. Khoản ba triệu rưỡi bên anh chuyển vô, tôi cũng vừa lập biên bản ngoài công an.
- `l26_ah` **ANH HAI**: Anh muốn nhận lại tiền thì mang giấy tờ ra cơ quan công an làm việc.
- *(Im lặng 2,6 giây… Tút! Số lạ cúp máy và chặn liên lạc.)*

## HỒI 5 – GIỮ LÒNG TỐT, NHƯNG ĐỪNG ĐƯA ĐIỆN THOẠI
**`s11_school_pickup` · `c11`** – Chiều tan học trước cổng trường Tiểu học. Bé Tom đeo bình nước màu cam bên hông.
- `l27_tom` **TOM**: Ba ơi… Vậy mốt gặp người lớn tuổi ngoài đường nhờ giúp, mình giả bộ hông thấy hả ba?
- `l28_ah` **ANH HAI**: Đâu có con. Người ta lạc đường hay mệt thì mình vẫn gọi bảo vệ, gọi người nhà phụ họ.
- `l29_ah` **ANH HAI**: Chỉ có căn cước của mình với cái điện thoại người lạ… là ba con mình không đưa, không cầm thôi.

## THẺ KẾT *(DƯỚI 10 GIÂY)*
**`s12_red_flags`** *(nền `EP01b/scene18.jpg`)*
- `l30_narr` **NGƯỜI BÓC TRẦN**: Thứ chúng lấy không phải tiền lẻ trên tay, mà là khuôn mặt và lòng tốt của bạn.

### NHỚ KỸ – BẢO VỆ CĂN CƯỚC & KHUÔN MẶT
1. **Không cho chụp căn cước** ở các quầy tặng quà, khảo sát dọc đường.
2. **Không cầm điện thoại người lạ** đưa ngang mặt hay đọc theo chữ trên màn hình.
3. **Nhận tiền "giải ngân" lạ:** giữ nguyên, tuyệt đối không tự chuyển trả vào tài khoản cá nhân.
4. **Khóa thẻ online & hạ hạn mức**, báo trước nơi làm việc và kiểm tra tín dụng tại quầy ngân hàng.
5. **Lập biên bản tại cơ quan công an** để bảo vệ mình trước mọi tranh chấp vay mạo danh.
- **Việc nên làm:** Giúp người lớn tuổi ngoài đường bằng cách gọi bảo vệ hoặc người thân hỗ trợ — tuyệt đối không đưa căn cước và không nhìn vào màn hình điện thoại người lạ.

**`s13_disclaimer`** – LƯU Ý (hư cấu + thông tin tham khảo).
