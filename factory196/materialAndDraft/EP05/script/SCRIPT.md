# EP05 – TỜ NĂM TRĂM VÀ SÁU GIÂY NHÌN THẲNG *(Bản kịch hóa điện ảnh – v3 Kết Mở)*

- **Mã tập:** `EP05` · **Slug:** `ToNamTramVaSauGiayNhinThang`
- **Họ kịch bản:** `MIX` – Dàn cảnh 2 chốt ngoài đời thực (Chốt 1 lấy căn cước qua hộp quà màu cam → Chốt 2 đưa 500k tiền mặt thật rồi chỉ tay nhờ đọc dòng chữ nhỏ trong lúc né mặt khỏi camera trước) → Nhánh ngoài tung "giải ngân mồi" 3,5 triệu thử phản ứng → **Kết mở đường dây ngầm (cắt đúng `04:15`):** Bà già mắt mờ lộ diện không kính lão ở băng ghế sau xe hơi đen giữa đêm mưa, bình thản nói món tiền đó chỉ là bạc lẻ thả cho nhánh ngoài thử phản ứng.
- **Định dạng:** `16:9` (`1920x1080 @ 30fps`) · **Tỷ lệ:** **97% kịch tâm lý – điện ảnh / 3% Người Bóc Trần (< 10 giây)**
- **Nguồn sự thật của timeline:** [`source/build_draft.py`](../source/build_draft.py) → sinh [`episode.json`](../episode.json).

## Nhân vật & giọng (`02_CAST/cast.json` – 9 tuyến / 9 voice độc lập)
| Nhân vật | Key | Voice | Chỉ đạo giọng |
|---|---|---|---|
| **Anh Hai** (35t) | `anh_hai` | `Orus` | Nam trầm ấm, thẳng tính, đời thực |
| **Chị Hai** (34t) | `chi_hai` | `Sulafat` | Nữ trầm vừa, cực kiệm lời, thực tế |
| **Bé Tom** (8t) | `be_tom` | `Puck` | Bé trai trong sáng, tự nhiên |
| **Cô Lành / Bà Dì** (~50t) | `co_hanh` | `Despina` | Hồi 2: hiền lành luống cuống · Kết mở: trầm lạnh, chậm, đầy quyền lực ngầm |
| **Đàn em báo cáo** | `ke_ngot_ngao_nam` | `Achird` | Cung kính, dè dặt qua điện thoại (`af: phone`) |
| **Đầu dây đòi nợ (nhánh ngoài)** | `chu_no` | `Fenrir` | Trầm, đều, lịch sự lạnh băng (`af: phone`) |
| **Nhân viên quầy quà** | `ke_ngot_ngao_nu` | `Aoede` | Nữ trẻ tươi tắn, lịch sự (1 câu) |
| **Giao dịch viên ngân hàng** | `chi_tu` | `Zephyr` | Nữ điềm tĩnh, chuẩn mực nghiệp vụ (3 câu) |
| **Người Bóc Trần** | `nguoi_boc_tran` | `Charon` | Đúng 1 câu (~6,3 giây) ở thẻ `NHỚ KỸ` |

---

## HOOK – MÓN NỢ TỪ CHÍNH GƯƠNG MẶT MÌNH
**`s00_night_ping` · `c00`** – Đêm. Phòng khách nhà Anh Hai. *(Bong bóng: "NGÂN HÀNG X: +3.500.000 VND · ND: GIAI NGAN HD 6.000.000")*.
- `l01_ah` **ANH HAI**: Alo, ai mới chuyển nhầm tiền vậy?
- `l02_cn` **SỐ LẠ** *(điện thoại)*: Không ai chuyển nhầm hết anh Hai. Hợp đồng sáu triệu của anh tới hạn thứ Sáu.
- `l03_ah` **ANH HAI**: Anh nói bậy gì đó, tôi vay hồi nào?

**`s01_mirror_shock` · `c01`** – Tệp đính kèm bật sáng: Ảnh căn cước 2 mặt ghép sát đoạn video 6 giây quay cận mặt Anh Hai ngoài bãi xe.
- `l04_ah_clip` **ANH HAI (TRONG CLIP)**: Tôi xác nhận đồng ý thực hiện hồ sơ…
- `l05_cn` **SỐ LẠ**: Mặt anh, tiếng anh, căn cước của anh đủ hết. Trễ hẹn thì sáng thứ Bảy cả xưởng anh xem clip này.

## HỒI 1 – CHIẾC HỘP CAM & TẤM HÌNH CĂN CƯỚC
**`s02_promo_desk` · `c02`** – Sáng Chủ Nhật, 4 ngày trước. Bé Tom đã ôm chiếc hộp màu cam vào lòng ngước nhìn ba; Anh Hai khựng tay ngập ngừng trên ví rồi đành chìa thẻ căn cước ra.
- `l06_tom` **TOM**: Ba ơi, mình đăng ký lấy cái bình màu cam nghen ba!
- `l07_vy` **QUẦY QUÀ**: Dạ quà tặng cho bé, anh cho em chụp căn cước với số điện thoại để tránh nhận trùng nha.
- `l08_ah` **ANH HAI** *(ngập ngừng rồi tặc lưỡi)*: Ờ… vậy em chụp lẹ giùm anh nha.

## HỒI 2 – TỜ NĂM TRĂM TIỀN THẬT & GÓC NÉ CAMERA
**`s03_parking_approach` · `c03`** – Bãi giữ xe ngoài trời. Cô Lành liếc nhanh hộp cam trên tay Tom, đưa tờ 500.000đ tiền mặt thật ra trước.
- `l09_la` **CÔ LÀNH**: Chú ơi, làm ơn giúp chị với. Chị đóng tiền thuốc mà thẻ lỗi hoài, chú đổi giùm chị năm trăm tiền mặt nghen.
- `l10_ah` **ANH HAI**: Dạ được chị. Chị đọc số tài khoản đi em chuyển cho.

**`s04_six_seconds_face` · `c04`** – Cô Lành đứng sát cạnh, đưa điện thoại ra trước mặt Anh Hai, **ngón tay chỉ vào dòng chữ nhỏ trên màn hình nhưng đầu và người bà ta khéo léo nghiêng lùi ra sau vai Anh Hai để không lọt vào camera trước**.
- `l11_la` **CÔ LÀNH**: Khổ thiệt, mắt chị mờ quá… Chú đọc giùm chị dòng chữ nhỏ ngay ngón tay chị chỉ nè.
- `l12_ah` **ANH HAI**: Tôi xác nhận đồng ý thực hiện hồ sơ… Rồi, em bấm thoát giùm chị luôn rồi đó.
- `l13_la` **CÔ LÀNH**: Cảm ơn hai cha con nhiều lắm, đúng là gặp quý nhân!

**`s05_home_noon` · `c05`** – Bếp nhà Anh Hai buổi trưa.
- `l14_tom` **TOM**: Mẹ ơi, sáng nay ba mới giúp một bà cô mắt mờ ngoài bãi xe đó!
- `l15_ch` **CHỊ HAI**: Giúp sao vậy anh?
- `l16_ah` **ANH HAI**: Bả đưa tờ năm trăm trước, nhờ anh chuyển khoản rồi bấm tắt giùm cái màn hình đơ.

**`s06_glasses_off` · `c06`** – Góc khuất sau bãi xe. Cô Lành tháo kính lão, tay vững như đá. Bong bóng: *"GỬI NHÁNH NGOÀI: Mẫu hộp cam áo xám: Đã khớp căn cước quầy trong. Sáu giây mặt với tiếng nét căng."* → *"Chuyển bộ nháp cho tụi bây thử nước trước đi."* *(câm)*

## HỒI 3 – CÁI BẪY "TRẢ CHO ÊM CHUYỆN"
**`s07_midnight_temptation` · `c07`** – 22:00 Đêm. Anh Hai định bù 2,5 triệu tiền túi trả cho xong; Chị Hai giữ cổ tay chồng.
- `l17_ch` **CHỊ HAI**: Anh chuyển vô tài khoản cá nhân đó, lấy gì chắc tụi nó xóa clip?
- `l18_ah` **ANH HAI**: Bù có hai triệu rưỡi tiền mình thôi em… Chứ mai nó rải clip khắp xưởng, anh nhìn mặt ai?
- `l19_ch` **CHỊ HAI**: Nó thấy anh sợ mất mặt mà chịu trả lần đầu, tuần sau chính cái clip đó sẽ đẻ ra khoản thứ hai.

**`s08_lockdown_first_strike` · `c08`** – Phản ứng thực tế, gọn dứt khoát.
- `l20_ch` **CHỊ HAI**: Anh khóa thẻ trước đi.
- `l21_ah` **ANH HAI**: Ừ… Để anh nhắn lên nhóm xưởng báo trước một tiếng luôn.

## HỒI 4 – KHOANH GIỮ TIỀN LẠ & LẬP BIÊN BẢN
**`s09_bank_counter` · `c09`** – Sáng hôm sau tại quầy ngân hàng.
- `l22_gdv` **NGÂN HÀNG**: Ngân hàng chính thống bắt buộc quét chip căn cước thật, nên kẻ gian không mở trộm khoản vay ngân hàng dưới tên anh được.
- `l23a_gdv` **NGÂN HÀNG**: Em đã cập nhật lại khuôn mặt và tra tín dụng cá nhân của anh, hoàn toàn không có nợ vay.
- `l23b_gdv` **NGÂN HÀNG**: Còn khoản ba triệu rưỡi chuyển vào không rõ nguồn, ngân hàng sẽ khoanh giữ chờ công an xử lý.

**`s10_police_gate_call` · `c10`** – Trưa cùng ngày, trước hiên trụ sở cơ quan công an.
- `l24_cn` **SỐ LẠ**: Quá giờ rồi đó anh Hai. Chuyển sáu triệu hay để tôi gửi clip vô xưởng?
- `l25_ah` **ANH HAI**: Xưởng tôi báo hết từ tối qua rồi. Khoản ba triệu rưỡi bên anh chuyển vô, tôi cũng vừa lập biên bản ngoài công an.
- `l26_ah` **ANH HAI**: Anh muốn nhận lại tiền thì mang giấy tờ ra cơ quan công an làm việc.
- *(Tút! Số lạ cúp máy và chặn liên lạc.)*

## HỒI 5 – GIỮ LÒNG TỐT, NHƯNG ĐỪNG ĐƯA ĐIỆN THOẠI
**`s11_school_pickup` · `c11`** – Chiều tan học trước cổng trường Tiểu học.
- `l27_tom` **TOM**: Ba ơi… Vậy mốt gặp người lớn tuổi ngoài đường nhờ giúp, mình giả bộ hông thấy hả ba?
- `l28_ah` **ANH HAI**: Đâu có con. Người ta lạc đường hay mệt thì mình vẫn gọi bảo vệ, gọi người nhà phụ họ.
- `l29_ah` **ANH HAI**: Chỉ có căn cước của mình với cái điện thoại người lạ… là ba con mình không đưa, không cầm thôi.

## THẺ NHỚ KỸ *(DƯỚI 10 GIÂY)*
**`s12_red_flags`** *(nền `EP01b/scene18.jpg`)*
- `l30_narr` **NGƯỜI BÓC TRẦN**: Thứ chúng lấy không phải tiền lẻ trên tay, mà là khuôn mặt và lòng tốt của bạn.

## KẾT MỞ ĐƯỜNG DÂY NGẦM – CUỘC GỌI ĐÊM MƯA TRÊN CHIẾC XE ĐEN
**`s13_backseat_boss` · `c12`** – Đêm mưa lất phất. Ở băng ghế da phía sau chiếc xe hơi đen sang trọng đỗ trong bóng tối, **"Cô Lành"** mặc áo khoác tối màu sang trọng, không kính lão, gương mặt sắc lạnh quyền lực nhìn xuống màn hình máy tính bảng hắt sáng.
- `l31_sub` **ĐẦU DÂY DƯỚI** *(điện thoại)*: Dì ơi, thằng hộp cam đem khoản ba triệu rưỡi ra công an rồi. Nhánh ngoài cắt số rút êm rồi dì.
- `l32_lanh_boss` **NGƯỜI ĐÀN BÀ**: Mấy đồng bạc lẻ đó… thả cho nhánh ngoài thử phản ứng thôi.
- **`s14_black_cut` · `c13` (`04:15`)** – **IMPACT + CẮT ĐEN ĐỘT NGỘT!**

**`s15_disclaimer`** – LƯU Ý.
