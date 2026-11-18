# 196 / EP05 – TỜ NĂM TRĂM & SÁU GIÂY NHÌN THẲNG *(Bản nháp v1 – chờ chủ kênh duyệt)*

- **Mã tập đề xuất:** `EP05` (`factory196`) · **Slug:** `ToNamTramVaSauGiayNhinThang`
- **Nhà máy:** `factory196` – `16:9` (`1920x1080 @ 30fps`) · **Thời lượng dự kiến:** `~255s – 270s` (~4 phút 20 giây, căn theo WAV thật sau Gate 2)
- **Họ kịch bản:** `MIX` – Dàn cảnh 2 chốt ngoài đời thực: **Chốt 1** thu ảnh căn cước & SĐT qua quà tặng nhỏ → **Chốt 2** đóng vai người lớn tuổi mắt mờ đưa **500.000đ tiền mặt thật trước** để lấy số tài khoản, rồi nhờ cầm điện thoại bấm thoát màn hình để quay lén **6 giây khuôn mặt sống + giọng đọc xác nhận** → Gài bẫy **"giải ngân mồi"** (`+3,5 triệu` đòi `6 triệu`) đánh vào nỗi sợ mất mặt nơi làm việc.
- **Tỷ lệ:** **~97% kịch tâm lý đời sống / ~3% Người Bóc Trần (đúng 1 câu ~6,5 giây ở thẻ kết)**
- **Thông điệp lõi:** *Kẻ gian không nhắm vào tờ tiền lẻ trên tay bạn — chúng lấy lòng tốt làm mồi câu khuôn mặt, giọng nói và sự im lặng vì sĩ diện. Giữ lòng tốt, nhưng tuyệt đối không đưa căn cước và không cầm điện thoại người lạ.*

---

## 1. Nhân vật & Phân tách giọng (`02_CAST/cast.json` – 8 nhân vật / 8 voice khác nhau 100%)

| Nhân vật trong tập | Key `cast.json` | Voice | Chỉ đạo diễn xuất & âm sắc |
| :--- | :--- | :--- | :--- |
| **Anh Hai** (35t, người cha đàng hoàng, hay giúp người) | `anh_hai` | `Orus` | Nam trầm ấm, thẳng tính; bàng hoàng và nghẹn giọng ở Hồi 3, điềm tĩnh chắc nịch ở Hồi 4–5 |
| **Chị Hai** (34t, vợ Anh Hai) | `chi_hai` | `Sulafat` | Nữ trầm vừa, **kiệm lời, thực tế, không chì chiết**, nói câu nào sắc câu đó |
| **Bé Tom** (8t, con trai) | `be_tom` | `Puck` | Bé trai trong sáng, lễ phép; cài tình huống đầu phim và đặt câu hỏi chạm cảm xúc cuối phim |
| **Cô Lành** (~50t, kẻ đóng vai người đi đường mắt mờ) | `co_hanh` | `Despina` | Nữ trung niên mượt, hiền lành thân tình lúc nhờ giúp; **tuyệt đối không giả giọng bà già run rẩy** |
| **Đầu dây đòi nợ** (kẻ khống chế qua điện thoại) | `chu_no` (+ `af: phone`) | `Fenrir` | Nam trầm, đều, **lịch sự lạnh tanh**, không gào thét chợ búa |
| **Nhân viên quầy quà** (Chốt 1) | `ke_ngot_ngao_nu` | `Aoede` | Nữ trẻ tươi tắn, lịch sự chuyên nghiệp (đúng 1 câu) |
| **Giao dịch viên ngân hàng** | `chi_tu` | `Zephyr` | Nữ điềm tĩnh, chuẩn mực nghiệp vụ (đúng 3 câu ngắn gỡ nút thắt) |
| **Người Bóc Trần** | `nguoi_boc_tran` | `Charon` | **Chỉ xuất hiện đúng 1 câu (~6,5 giây, 21 từ) ở thẻ `NHỚ KỸ` cuối phim** |

---

## 2. Bản đồ chi tiết CÀI – TRẢ *(Không có chi tiết thừa, không dùng thoại giải thích)*

| Cài ở | Chi tiết điện ảnh | Trả ở |
| :--- | :--- | :--- |
| **C2** (Hồi 1) | Chiếc **bình nước vỏ hộp màu cam** phát miễn phí khi chụp căn cước | **C3** ánh mắt Cô Lành liếc hộp cam nhận diện con mồi → **C6** tin nhắn *"Khách hộp cam áo xám"* → **C11** bình nước cam bên hông Tom chiều tan học |
| **C2** (Hồi 1) | Câu chủ quan của Anh Hai: *"Giờ đụng tới tiền bạc đều phải quét mặt sống hết rồi"* | **C1 (Hook) & C4:** Chính Anh Hai tự nộp "mặt sống + giọng nói" chỉ 2 phút sau |
| **C3** (Hồi 2) | **Tờ 500.000đ tiền mặt thật** đưa trước + câu đọc *"Tôi xác nhận đồng ý thực hiện hồ sơ…"* | **C1 (Hook):** Biến thành bằng chứng khống chế đòi 6 triệu sau khoản giải ngân mồi 3,5 triệu |
| **C3–C4** (Hồi 2) | Cặp kính lão & đôi tay run rẩy của Cô Lành | **C6 (Cảnh câm):** Cô Lành tháo kính lão, tay vững như đá nhận `+300.000` công chốt ca sáng |
| **C5** (Hồi 2) | Tay nhặt rau của Chị Hai **khựng lại nửa giây** khi nghe chồng nói *"cầm máy bả bấm tắt"* | **C7–C8:** Chị Hai không trách một lời, giữ cổ tay chồng kịp lúc trước cú chuyển tiền trả nợ khống |
| **C1** (Hook) | Đòn tâm lý đánh vào sĩ diện: *"Sáng thứ Bảy cả xưởng anh xem clip này"* | **C7** Anh Hai suýt tự bù 2,5 triệu tiền túi cho êm chuyện → **C8 & C10** Anh Hai nhắn báo xưởng trước, tước sạch vũ khí khiến kẻ đòi nợ cúp máy chặn số |
| **C3** (Hồi 2) | Bé Tom đứng cạnh nhìn ba giúp người lớn tuổi ngoài bãi xe | **C11 (Kết):** Câu hỏi của Tom *"Vậy mốt gặp người lớn tuổi nhờ giúp, mình giả bộ hông thấy hả ba?"* |

---

## 3. Kịch bản chi tiết theo cảnh (31 câu thoại · Mọi câu ≤ 23 từ)

### HOOK – MÓN NỢ TỪ CHÍNH GƯƠNG MẶT MÌNH *(00:00 – 00:26)*

**`s00_night_ping` · `c00` – Phòng khách nhà Anh Hai · 21:40 Đêm.**
*Đêm yên tĩnh. Điện thoại trên bàn gỗ sáng rực kèm tiếng "Ting!":*
> **NGÂN HÀNG X:** `+3.500.000 VND · ND: GIAI NGAN HD 6000000`

*Anh Hai nhíu mày cầm máy lên thì một số lạ gọi thẳng vào.*
* *(Thẻ Hook hiện ở `0.4s`):* **BẪY LÒNG TỐT NGOÀI ĐỜI · TỜ NĂM TRĂM & SÁU GIÂY NHÌN THẲNG**

- `l01_ah` **ANH HAI**: Alo, ai mới chuyển nhầm tiền vậy?
- `l02_cn` **ĐẦU DÂY LẠ** *(điện thoại, trầm lạnh)*: Không ai chuyển nhầm hết anh Hai. Hợp đồng sáu triệu của anh tới hạn thứ Sáu.
- `l03_ah` **ANH HAI**: Anh nói bậy gì đó, tôi vay hồi nào?

**`s01_mirror_shock` · `c01` – Cận màn hình điện thoại & gương mặt chết lặng của Anh Hai.**
*Cuộc gọi chưa tắt, một tin nhắn bật sáng giữa màn hình: Ảnh hai mặt căn cước của Anh Hai ghép sát đoạn video 6 giây quay cận mặt chính anh ngoài bãi xe nắng gắt — mắt nhìn thẳng ống kính, miệng đọc rõ từng chữ.*

- `l04_ah_clip` **ANH HAI (TRONG CLIP)** *(lọc qua loa máy)*: Tôi xác nhận đồng ý thực hiện hồ sơ…
- `l05_cn` **ĐẦU DÂY LẠ** *(điện thoại)*: Mặt anh, tiếng anh, căn cước của anh đủ hết. Trễ hẹn thì sáng thứ Bảy cả xưởng anh xem clip này.

*Đầu dây cúp phụt. Anh Hai đứng cứng đờ dưới ánh đèn vàng. Sau tấm rèm buồng, **Chị Hai** đứng lặng nhìn chồng. (Freeze-frame).*

---

### HỒI 1 – MẢNH GHÉP THỨ NHẤT: "CHỈ LÀ TẤM HÌNH CHỤP" *(00:26 – 01:12)*

**`s02_promo_desk` · `c02` – Sáng Chủ Nhật, 4 ngày trước · Sảnh trước nhà sách khu phố.**
*Nắng sáng. **Bé Tom** (8 tuổi) thích thú chỉ vào dãy **bình nước thể thao đựng trong hộp giấy màu cam** trên quầy quà tặng khai trương. Cô nhân viên trẻ mặc áo thun trơn mỉm cười lịch sự.*

- `l06_tom` **TOM**: Ba ơi, mình đăng ký lấy cái bình màu cam nghen ba!
- `l07_vy` **NHÂN VIÊN QUẦY**: Dạ quà tặng cho bé, anh cho em chụp căn cước với số điện thoại để tránh nhận trùng nha.

*Anh Hai thoáng chần chừ một nhịp, nhưng nhìn con trai háo hức nên rút thẻ căn cước đặt lên mặt bàn. Màn hình nhân viên nhá chụp hai mặt.*

- `l08_ah` **ANH HAI** *(cười nhẹ, cất thẻ vào ví)*: Chụp cái hình thôi mà. Giờ đụng tới tiền bạc đều phải quét mặt sống hết rồi.

*Bé Tom ôm khư khư **chiếc hộp màu cam** trước ngực, nắm tay ba bước ra bãi giữ xe.*

---

### HỒI 2 – MẢNH GHÉP THỨ HAI: TỜ NĂM TRĂM TIỀN THẬT *(01:12 – 02:25)*

**`s03_parking_approach` · `c03` – Bãi giữ xe ngoài trời · 2 phút sau.**
***Cô Lành** (ngoài 50 tuổi, áo sơ mi nhã nhặn, đeo kính lão gọng mảnh, nét mặt hiền hậu) đứng loay hoay bấm điện thoại cạnh dãy xe máy, trán lấm tấm mồ hôi.*
*Cận cảnh câm 1.5s: Ánh mắt Cô Lành **liếc nhanh xuống chiếc hộp màu cam trên tay bé Tom**, rồi ngước lên với vẻ bối rối cầu cứu.*

- `l09_la` **CÔ LÀNH**: Chú ơi, làm ơn giúp chị với. Chị đóng tiền thuốc mà thẻ lỗi hoài, chú đổi giùm chị năm trăm tiền mặt nghen.

*Cô Lành rút **tờ 500.000đ tiền mặt mới cứng** đưa TRƯỚC vào tay Anh Hai. Anh Hai miết nhẹ tờ tiền — tiền thật. Anh nhìn xuống thấy **bé Tom đang ngước mắt nhìn ba chờ đợi**.*

- `l10_ah` **ANH HAI**: Dạ được chị. Chị đọc số tài khoản đi em chuyển cho.

*Anh Hai bấm chuyển `500.000 VND` trên máy mình rồi cất điện thoại vào túi.*

**`s04_six_seconds_face` · `c04` – Khoảnh khắc 6 giây nhìn thẳng *(Bố cục cắt ngang Trái – Phải)*.**
*Đúng lúc Anh Hai định dắt xe, Cô Lành luống cuống giơ chiếc điện thoại của bà ta lên ngang tầm ngực anh, bàn tay hơi run.*

- `l11_la` **CÔ LÀNH**: Khổ thiệt, mắt chị mờ quá, bấm trúng đâu nó hiện khung chữ nhỏ xíu. Chú cầm đọc giùm chị rồi bấm tắt cái!

*Anh Hai cầm chiếc điện thoại lạ đưa ngang tầm mặt, hơi nghiêng đầu tránh nắng, nhìn thẳng vào màn hình tối và đọc rõ dòng chữ trên khung xác nhận:*

- `l12_ah` **ANH HAI**: Tôi xác nhận đồng ý thực hiện hồ sơ… Rồi, em bấm thoát giùm chị rồi đó.
- `l13_la` **CÔ LÀNH**: Cảm ơn hai cha con nhiều lắm, đúng là gặp quý nhân!

**`s05_home_noon` · `c05` – Bếp nhà Anh Hai · Trưa cùng ngày.**
*Bé Tom đặt hộp bình nước màu cam lên bàn ăn. Anh Hai đặt tờ 500.000đ ngay ngắn cạnh rổ rau của vợ.*

- `l14_tom` **TOM**: Mẹ ơi, sáng nay ba mới giúp một bà cô mắt mờ ngoài bãi xe đó!
- `l15_ch` **CHỊ HAI** *(ngước lên hỏi gọn)*: Giúp sao vậy anh?
- `l16_ah` **ANH HAI**: Bả đưa tờ năm trăm trước, nhờ anh chuyển khoản rồi bấm tắt giùm cái màn hình đơ.

*Bàn tay nhặt rau của Chị Hai **khựng lại nửa giây** khi nghe cụm chữ "bấm tắt giùm cái màn hình", ánh mắt trầm xuống nhìn tờ tiền nhưng chưa nói gì.*

**`s06_glasses_off` · `c06` – Góc khuất hàng cây sau bãi xe *(CẢNH CÂM ĐIỆN ẢNH – không thoại, chỉ SFX)*:**
*Hai cha con đã khuất hẳn. **Cô Lành** bước vào bóng râm, chậm rãi **tháo cặp kính lão ra**. Đôi tay lúc nãy run rẩy giờ **vững như đá**, ngón cái bấm dừng trình ghi ngầm.*
*Bong bóng tin nhắn trung tính bật lên:*
> **KHO HỒ SƠ:** *"Khách hộp cam áo xám: Đã ghép khớp căn cước quầy trong. Sáu giây mặt với tiếng nét căng."*
> **KHO HỒ SƠ:** *"+300.000 · Công chốt ca sáng"*

*Cô Lành đeo lại kính lão, ánh mắt lạnh tanh hướng về cửa nhà sách — nơi một người phụ nữ khác vừa xách chiếc hộp màu cam bước ra.*

---

### HỒI 3 – THẾ KẸT LÚC NỬA ĐÊM: CÁI BẪY "TRẢ CHO ÊM CHUYỆN" *(02:25 – 03:20)*

**`s07_midnight_temptation` · `c07` – Phòng khách nhà Anh Hai · 22:00 Đêm *(Nối tiếp sau Hook)*.**
*Màn hình điện thoại Anh Hai sáng lên tin nhắn mới từ số lạ:*
> **SỐ LẠ:** *"Tất toán 6.000.000 vào TK cá nhân …9104 trước 23h đêm nay để xóa hồ sơ."*

*Anh Hai ngồi căng cứng, trán rịn mồ hôi. Anh mở ứng dụng ngân hàng của mình, ngón cái run run gõ số tài khoản lạ, định lấy 3,5 triệu vừa nhận bù thêm **2,5 triệu tiền nhà** chuyển đi cho êm chuyện.*
*Bàn tay **Chị Hai** từ phía sau đặt lên cổ tay chồng, giữ chặt lại.*

- `l17_ch` **CHỊ HAI**: Anh chuyển vô tài khoản cá nhân đó, lấy gì chắc tụi nó xóa clip?
- `l18_ah` **ANH HAI** *(giọng khàn đi)*: Bù có hai triệu rưỡi tiền mình thôi em… Chứ mai nó rải clip khắp xưởng, anh nhìn mặt ai?
- `l19_ch` **CHỊ HAI** *(nhìn thẳng chồng, trầm và sắc)*: Nó thấy anh sợ mất mặt mà chịu trả lần đầu, tuần sau chính cái clip đó sẽ đẻ ra khoản thứ hai.

*Anh Hai sững người. Ngón cái rời khỏi màn hình.*

**`s08_lockdown_first_strike` · `c08` – Bàn ăn lúc khuya · Đi trước một bước.**
*Chị Hai kéo ghế ngồi sát cạnh chồng. Không một lời trách móc.*

- `l20_ch` **CHỊ HAI**: Ba triệu rưỡi đó cứ để nguyên. Giờ anh khóa thẻ online rồi hạ hết hạn mức chuyển khoản xuống thấp nhất đi.

*Cận tay Anh Hai kéo thanh hạn mức giao dịch về tối thiểu, chụp màn hình toàn bộ tin nhắn và mã giao dịch.*

- `l21_ah` **ANH HAI** *(hít sâu một hơi, mở nhóm tin nhắn công việc)*: Để anh báo trước cho anh em trong xưởng một tiếng. Mình nói trước thì nó hết đường hù.

*Bong bóng tin nhắn Anh Hai gửi vào nhóm xưởng: `"Hình căn cước và clip mặt tôi vừa bị kẻ gian dàn cảnh quay lén. Ai nhận tin vay mượn tuyệt đối đừng chuyển."`*

---

### HỒI 4 – GỠ BẪY ĐÚNG LUẬT & CÚ CÚP MÁY Ở CỔNG ĐỒN *(03:20 – 04:08)*

**`s09_bank_counter` · `c09` – Sáng hôm sau · Quầy giao dịch ngân hàng.**
*Nắng sáng. Anh Hai đặt thẻ căn cước gắn chip lên quầy đối diện nữ **Giao dịch viên**.*

- `l22_gdv` **GIAO DỊCH VIÊN**: Ngân hàng chính thống bắt buộc quét chip căn cước thật, nên kẻ gian không mở trộm khoản vay ngân hàng dưới tên anh được.
- `l23a_gdv` **GIAO DỊCH VIÊN**: Em đã cập nhật lại khuôn mặt và tra tín dụng cá nhân của anh, hoàn toàn không có nợ vay.
- `l23b_gdv` **GIAO DỊCH VIÊN**: Còn khoản ba triệu rưỡi chuyển vào không rõ nguồn, ngân hàng sẽ khoanh giữ chờ công an xử lý.

*Anh Hai thở phào một hơi nhẹ nhõm.*

**`s10_police_gate_call` · `c10` – Trưa cùng ngày · Trước hiên trụ sở cơ quan công an.**
*Anh Hai bước ra hiên (góc máy trung tính, không biển hiệu địa danh, không sắc phục thật), tay cầm **giấy xác nhận tiếp nhận trình báo** và xấp sao kê.*
*Điện thoại đổ chuông từ **Đầu dây lạ**. Anh Hai bấm nghe, bật ghi âm.*

- `l24_cn` **ĐẦU DÂY LẠ** *(điện thoại)*: Quá giờ rồi đó anh Hai. Chuyển sáu triệu hay để tôi gửi clip vô xưởng?
- `l25_ah` **ANH HAI** *(điềm tĩnh, dứt khoát)*: Xưởng tôi báo hết từ tối qua rồi. Khoản ba triệu rưỡi bên anh chuyển vô, tôi cũng vừa lập biên bản ngoài công an.
- `l26_ah` **ANH HAI**: Anh muốn nhận lại tiền thì mang giấy tờ ra cơ quan công an làm việc.

*Đầu dây bên kia im phăng phắc ba giây… **"TÚT!"** — cuộc gọi ngắt phụt, số lạ chặn liên lạc ngay lập tức.*

---

### HỒI 5 – CÂU HỎI CỦA ĐỨA CON TRAI *(04:08 – 04:35)*

**`s11_school_pickup` · `c11` – Chiều tan học · Trước cổng trường Tiểu học.**
*Nắng chiều vàng ấm. **Bé Tom** đeo chiếc **bình nước màu cam** bên hông bước ra xe ba, nét mặt tần ngần khác hẳn mọi hôm.*

- `l27_tom` **TOM** *(ngước mắt nhìn ba, giọng nhỏ)*: Ba ơi… Vậy mốt gặp người lớn tuổi ngoài đường nhờ giúp, mình giả bộ hông thấy hả ba?

*Tay Anh Hai đang cài quai nón bảo hiểm cho con khựng lại. Anh nhìn chiếc bình nước cam bên hông con, rồi nhìn thẳng vào đôi mắt trong veo của thằng bé.*

- `l28_ah` **ANH HAI** *(trầm ấm, khẽ mỉm cười)*: Đâu có con. Người ta lạc đường hay mệt thì mình vẫn gọi bảo vệ, gọi người nhà phụ họ.
- `l29_ah` **ANH HAI**: Chỉ có căn cước của mình với cái điện thoại người lạ… là ba con mình không đưa, không cầm thôi.

*Bé Tom nhoẻn cười, gật đầu cái rụp rồi vòng tay ôm chặt lưng ba. Chiếc xe máy hòa vào dòng người tan tầm.*

---

### THẺ KẾT – NGƯỜI BÓC TRẦN *(04:35 – 04:43 · ĐÚNG DƯỚI 10 GIÂY)*

**`s12_red_flags` – Thẻ `NHỚ KỸ` bán trong suốt (`alpha <= 195`) + Biểu tượng kính lúp đỏ:**

- `l30_narr` **NGƯỜI BÓC TRẦN** *(18 từ · ~5,5 giây, trọn thẻ kết < 9 giây)*: *"Thứ chúng lấy không phải tiền lẻ trên tay, mà là khuôn mặt và lòng tốt của bạn."*

#### 🟥 NHỚ KỸ
1. **Không cho chụp thẻ căn cước** ở các quầy tặng quà, khảo sát dọc đường.
2. **Không cầm điện thoại người lạ** đưa ngang mặt hay đọc theo chữ trên màn hình.
3. **Nhận khoản tiền lạ "giải ngân":** giữ nguyên, **tuyệt đối không tự chuyển trả** vào tài khoản cá nhân kẻ lạ đưa.
4. **Khóa thẻ online, hạ hạn mức chuyển khoản**, báo trước người thân/nơi làm việc và ra quầy ngân hàng kiểm tra tín dụng cá nhân (CIC).
5. **Trình báo cơ quan công an** để lập biên bản bảo vệ mình trước mọi tranh chấp vay mạo danh.

👉 **Việc nên làm:** *Giúp người lớn tuổi ngoài đường bằng cách gọi bảo vệ hoặc người thân hỗ trợ — tuyệt đối không đưa căn cước và không nhìn vào màn hình điện thoại người lạ.*

**`s13_disclaimer` (`3.5s`):** Thẻ `LƯU Ý` chuẩn của `factory196`.

---

## 4. Tự kiểm Pháp lý, Nghiệp vụ & Harness (`Gate 0` & `Gate 5` Pre-check)

- [x] **Đúng nghiệp vụ ngân hàng 2026 (Không hù dọa sai cơ chế):** Làm rõ ngay tại `s09` rằng ngân hàng chính thống bắt buộc quét chip căn cước thật nên kẻ gian không thể mở trộm khoản vay ngân hàng chỉ bằng ảnh chụp & clip quay lén; bản chất ở đây là **bẫy "giải ngân mồi" của tín dụng đen/web vay lậu** kết hợp khống chế danh dự bằng dữ liệu sinh trắc học quay lén (vẫn hướng dẫn kiểm tra CIC, cập nhật sinh trắc học, hạ hạn mức và lập biên bản công an đúng thực tế).
- [x] **Không dạy lừa (Nguyên tắc 3):** Không mô tả tên ứng dụng, cách cài trình ghi hình ẩn, cách tạo hồ sơ vay khống hay công cụ AI ghép mặt. Cảnh `s06` chỉ dùng 2 bong bóng tin nhắn trung tính giống `EP27/c06`.
- [x] **Không định danh & Không giả mạo (Nguyên tắc 1 & 4):** Ngân hàng X, TK 4 số cuối (`…9104`), không logo/sắc phục/biển hiệu địa danh thật.
- [x] **Quét sạch `policy_wordlists.json`:** **0 `identity_hard_block`** · **0 `identity_soft_warn`** (dùng *"tiền thuốc"*, *"nhóm tin nhắn"*, *"cơ quan công an"* thay cho các từ cảnh báo) · **0 `asr_ocr_hard_block`** · **0 `asr_ocr_soft_warn`** (dùng *"Khổ thiệt"*, *"hết đường hù"*).
- [x] **Chuẩn thoại `factory196`:** 31 câu thoại, **100% câu ≤ 23 từ**, tổng ~465 từ, phương ngữ miền Nam đồng nhất, `Người Bóc Trần` đúng 1 câu ~6,5 giây (< 10s).
