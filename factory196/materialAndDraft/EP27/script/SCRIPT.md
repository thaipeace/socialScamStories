# EP27 – SAU KHOẢN NỢ CUỐI CÙNG *(Bản kịch hóa điện ảnh – v3 · Tập đặc biệt Đêm Giao Thừa 05/02/2027)*

- **Mã tập:** `EP27` · **Slug:** `SauKhoanNoCuoiCung`
- **Họ kịch bản:** `MIX` – Tín dụng đen góp ngày (ký 10 triệu, cầm 8 triệu 6) + **chim mồi "chị em cùng cảnh"**: ăn hoa hồng 5% từ chủ nợ, dụ ký vay chia đôi, góp 3 ngày rồi im luôn, vì chính cô ta cũng đang chìm trong vòng xoay.
- **Định dạng:** `16:9` (`1920x1080 @ 30fps`) · **Thời lượng ước tính:** `~7:20` (căn theo WAV thật sau Gate 2)
- **Tỷ lệ:** 97% kịch đời sống / 3% Người Bóc Trần (1 câu ở thẻ kết)
- **Thông điệp lõi:** *Tín dụng đen sống nhờ sự im lặng trong nhà — và lấy đi cả những năm tháng tuổi thơ của con cháu không bao giờ trả lại được.*
- **Nguồn sự thật của timeline:** [`source/build_draft.py`](../source/build_draft.py) → sinh [`episode.json`](../episode.json). Sửa thoại ở file build rồi chạy lại, **không sửa tay `episode.json`**.

## Nhân vật & giọng (`02_CAST/cast.json`)
| Nhân vật | Key | Voice | Chỉ đạo giọng |
|---|---|---|---|
| **Má – Cô Tư** | `co_tu` | `Kore` | Hiền, rõ chữ, tự nhiên. **Không giả giọng người già, không kéo dài chữ, không run rẩy** |
| **Anh Hai** | `anh_hai` | `Orus` | Trầm, thẳng, nói câu nào chắc câu đó |
| **Chị Hai** | `chi_hai` *(mới)* | `Sulafat` | Ấm, ít lời, gọn, không bi lụy |
| **Cô Hạnh** | `co_hanh` *(mới)* | `Despina` | Mượt, ngọt, **nói nhanh và gấp** như người lúc nào cũng đang chạy việc. Không giọng già |
| **Long – chủ nợ** | `chu_no` *(mới)* | `Fenrir` | Lịch sự, đều, lạnh. Không la hét. Có `af: phone` khi gọi điện |
| **Cán bộ trợ giúp pháp lý** | `chi_tu` | `Zephyr` | Điềm tĩnh, đúng 4 câu |
| **Ông Bảy** | – | – | **Chỉ thoáng qua ở C11, không thoại** |
| **Bé Tom** | `be_tom` | `Puck` | 8 tuổi, cháu nội. Đúng 1 câu ngây thơ đứt ruột ở bữa cơm Tết cuối phim (`l62b_tom`) |
| **Người Bóc Trần** | `nguoi_boc_tran` | `Charon` | 1 câu ở thẻ kết |

> [!NOTE]
> Hạnh đổi từ `Gacrux` sang `Despina` theo góp ý "đừng kéo giọng già": Gacrux có âm sắc già, dễ ra giọng bà cụ.

## Bản đồ cài – trả
| Cài | Chi tiết | Trả |
|---|---|---|
| C1 | Vệt da trắng ở ngón áp út | C7 biên nhận cầm nhẫn → C12 tiệm đã thanh lý → C15 bàn tay ở mâm cơm Tết → dòng chữ cuối |
| C2 | Mốc **7 năm** ("7 năm nay con gom trả mấy đợt") + ảnh thôi nôi Tom 1 tuổi trên tủ lạnh | C7 lời thú nhận "7 năm trước, 7 cái Tết người ta canh đầu hẻm không dám qua thăm cháu" → C8 "7 năm xoay ra 7 khoản" → C15 câu hỏi của bé Tom: *"Sao hồi con còn nhỏ, con hông thấy bà?"* |
| C2 | "Lần này là lần cuối con trả" | C7 tiếng vọng → "Tại con nói câu đó, phải hông má?" |
| C3 | 10 triệu, cầm 8 triệu 6 | C6 phát hiện → C8 tính ra hơn 300%/năm → C11 phản đòn bằng con số |
| C3 | +500.000 "hh", chuyển đi ngay trong 10 giây | C10 "Năm phần trăm" + "ngưng xoay một bữa là sập" |
| C2/C4 | Cuốn sổ góp, mỗi ngày một vạch | C6 ba vạch bên tên Hạnh → C14 Má trao sổ cho con |
| C1/C5 | Long biết chỗ làm, gọi lên xưởng | C5 bật ghi âm → C11 điện thoại ghi âm đặt giữa bàn |

---

## HOOK – CUỘC GỌI LÚC ĐÊM
**`s00_night_call` · `c00`** – Đêm. Phòng nhỏ, đèn vàng. Điện thoại rung bần bật. *(Bong bóng: "14 cuộc gọi nhỡ")*. Thẻ hook: **TẬP ĐẶC BIỆT CUỐI NĂM · MÙA VAY NÓNG – SAU KHOẢN NỢ CUỐI CÙNG**.
- `l01_long` **LONG** *(điện thoại)*: Chị Tư, hôm nay tới ngày rồi đó.
- `l02_ma` **MÁ**: Cho chị thêm ít bữa nữa nghen em.
- `l03_long` **LONG**: Bữa nào chị cũng nói vậy. Không có thì kêu thằng Hai lo. Nó làm ở xưởng gần chợ mà, em biết chỗ.
- `l04_ma` **MÁ**: Đừng gọi cho con chị. Để chị tự lo.

**`s01_finger_hover` · `c01`** – Cận tay Má: vệt da trắng ở ngón áp út, ngón cái lơ lửng trên dòng *"Con Hai"*… rồi rút về. Úp điện thoại.

## HỒI 1 – LẦN CUỐI *(bảy năm trước tới nay)*
**`s02_son_visit` · `c02`** – Anh Hai đặt túi gạo, sữa, thuốc huyết áp. Cuốn sổ góp mở trên bàn.
- `l05_ah` **ANH HAI**: Bảy năm nay con gom trả cho má mấy đợt rồi. Má đừng mượn ai nữa nghen.
- `l06_ma` **MÁ**: Ừ, má biết rồi.
- `l07_ah` **ANH HAI**: Lần này là lần cuối con trả. Lần sau má tự chịu đó.
- `l08_ma` **MÁ**: Má biết mà. Con lo đi làm đi.

**`s03_tet_photo` · `c03`** – Má nhìn tấm ảnh cũ phai màu trên tủ lạnh: ảnh 7 năm trước lúc bé Tom mới đầy năm nằm trong vòng tay bà nội. Tin nhắn sáng lên: *"Chị Tư cần xoay thì nói em nha. Em có cách."* – **HẠNH**.

## HỒI 2 – NGƯỜI CÙNG CẢNH NGỘ
**`s04_tea_stall` · `c04`** – Quán nước đầu hẻm. Hạnh đeo vòng vàng, cầm điện thoại đời mới, bấm tắt tiếng một cuộc gọi.
- `l09_ha` **HẠNH**: Chị còn thiếu nhiều hông?
- `l10_ma` **MÁ**: Chỗ này một ít, chỗ kia một ít. Trả chỗ này lại hụt chỗ kia.
- `l11_ha` **HẠNH**: Em cũng từng y chang chị. Có bữa đứng giữa chợ mà muốn khóc.
- `l12_ha` **HẠNH**: Chị ký giấy mười triệu, cầm về tám triệu sáu. Chia đôi, em góp mỗi ngày phụ chị.
- `l13_ma` **MÁ**: Sao mười triệu mà cầm có tám triệu sáu?
- `l14_ha` **HẠNH**: Phí hồ sơ đó chị. Bên nào cũng trừ, em làm hoài à.
- `l15_ma` **MÁ**: Mà giấy đứng tên ai?
- `l16_ha` **HẠNH**: Tên chị. Chị em mình mà, em bỏ chị sao được.

**`s05_signing` · `c05`** – Cận cảnh: ngón áp út trống chạm thân bút, nét chữ run. *(câm)*

**`s06_hanh_alone` · `c06`** – Má đi khuất. Bong bóng: **"+500.000 · hh khách chị Tư"** *(LONG – HOA HỒNG 5%)*. Mười giây sau: **"–500.000 · –4.300.000"**. Hạnh thở hắt ra như vừa ngoi lên mặt nước. Điện thoại lại rung. *(câm)*

**`s07_ledger_days` · `c07`** – Montage: Ngày 1–3 *"Hạnh chuyển +150.000"*, Má gạch từng vạch → Ngày 4 gọi không ai bắt máy → Ngày 5 *"Hạnh ơi?"*, tin báo **KHÔNG GỬI ĐƯỢC**. *(câm)*

## HỒI 3 – CÚ SẬP
**`s08_workshop_call` · `c08`** – Xưởng ồn tiếng máy.
- `l17_long` **LONG** *(điện thoại)*: Anh Hai phải hông? Má anh nợ bên tôi chín triệu mốt. Trễ ba bữa rồi.
- `l18_ah` **ANH HAI**: Anh là ai?
- `l19_long` **LONG**: Anh khỏi cần biết. Chiều nay không có, mai tôi ghé xưởng nói chuyện với quản lý anh.
- *(Bong bóng "Tự động ghi âm cuộc gọi: BẬT")*

**`s09_paper_found` · `c09`** – Nhà Má. Anh Hai cầm tờ giấy vay. Má đứng ở cửa bếp, tay cầm giẻ.
- `l20_ah` **ANH HAI**: Giấy ghi mười triệu. Má cầm về có tám triệu sáu?
- `l21_ma` **MÁ**: Hạnh nói phí hồ sơ…
- `l22_ah` **ANH HAI**: Rồi tiền đâu?
- `l23_ma` **MÁ**: Má đưa nó một nửa. Nó nói góp mỗi ngày phụ má.
- `l24_ah` **ANH HAI**: Nó góp được mấy bữa?
- *(Anh lật cuốn sổ: ba vạch. Đặt xuống, rất chậm.)*

**`s10_papers_ring` · `c10`** – Tối. Giấy tờ kín bàn. *(trọng tâm cảm xúc 1)*
- `l25_ah` **ANH HAI**: Khoản này của ai? Còn khoản này?
- `l26_ma` **MÁ**: Má hông nhớ rõ nữa. Cứ mượn chỗ này đắp chỗ kia, riết rồi hông biết khoản nào còn bao nhiêu.
- *(Anh rút ra tờ biên nhận cầm đồ, nhìn vệt da trắng trên tay Má.)*
- `l27_ah` **ANH HAI**: Nhẫn của ba?
- `l28_ah` **ANH HAI**: Sao má hông nói với con?
- `l29_ma` **MÁ**: Đợt trước con vét hết tiền để dành trả cho má rồi, vợ chồng con còn nuôi thằng Tom nhỏ xíu.
- `l30_ma` **MÁ**: Má tưởng ráng xoay thêm một bận là êm, ai dè lãi đẻ ra lãi. Má sợ con biết.
- `l31_ma` **MÁ**: Rồi con nói lần đó là lần cuối. Má đâu dám nói nữa.
- `l32_ah_echo` **ANH HAI** *(tiếng vọng, `af: memory`)*: Lần này là lần cuối con trả.

**`s11_son_beside` · `c11`** – Anh Hai vòng qua bàn, ngồi cạnh Má, tay đặt lên vai.
- `l33_ah` **ANH HAI**: Tại con nói câu đó, phải hông má?
- *(Má khóc thành tiếng. Anh gom giấy cho thẳng mép, không nói gì thêm.)*

## HỒI 4 – LỐI THOÁT DUY NHẤT · NGÀY MÁ RỜI ĐI *(Thời điểm D & E)*
**`s12_couple_night` · `c12`** – Khuya, nhà Anh Hai.
- `l34_ch` **CHỊ HAI**: Bao nhiêu anh?
- `l35_ah` **ANH HAI**: Bảy khoản lớn nhỏ. Tiền để dành đợt trước mình vét sạch rồi.
- `l36_ah` **ANH HAI**: Riêng khoản của Hạnh: cầm tám triệu sáu, phải góp mười hai triệu trong bốn chục ngày.
- `l37_ah` **ANH HAI**: Tính ra hơn ba trăm phần trăm một năm.
- `l38_ch` **CHỊ HAI**: Vậy mình rà lại từng khoản, rồi vay ngân hàng trả góp dài hạn đi anh.
- `l39_ch` **CHỊ HAI**: Tính kéo dài chừng bảy năm, mỗi tháng gói ghém lại vẫn còn đủ nuôi thằng Tom.

**`s13_legal_aid` · `c13`** – Tư vấn *(Thời điểm D – rút gọn tối đa, không giáo điều)*.
- `l41_cb` **CÁN BỘ**: Khoản có giấy thì chốt số thực cầm, thu lại giấy gốc. Nhưng mấy mối bên ngoài chưa êm ngay đâu.
- `l42_cb` **CÁN BỘ**: Tạm thời nên đưa cô đi xa ở với người thân, cắt hết số cũ để họ khỏi tìm gặp ép ký tiếp.

**`s14_hand_over` · `c19`** – **CAO TRÀO RA ĐI *(Thời điểm E)***: Hiên nhà tờ mờ sáng. Túi đồ cạnh cửa.
- `l58_ah` **ANH HAI**: Số mới. Con lưu số con, vợ con với dì Ba rồi.
- *(Má định tháo SIM điện thoại cũ.)*
- `l59_ah` **ANH HAI**: Má đưa con giữ. Trong đó là bằng chứng.
- `l60_ma` **MÁ**: Má đi vậy, có phải trốn nợ hông con?
- `l61_ah` **ANH HAI**: Khoản nào đúng thì mình trả đủ. Nhưng má ở lại đây, tụi nó hông để má yên đâu.

**`s14b_farewell_baby` · `c19b`** – Đầu hẻm mờ sương lúc 5h30 sáng. Chị Hai bế **bé Tom 1 tuổi đang ngủ say** trên vai. Má khẽ chạm bàn tay trống nhẫn vào chân cháu:
- `l61b_ma` **MÁ**: Má về dưới ít tháng, êm chuyện rồi má lên thăm thằng Tom liền nghen con.
- `l61c_ch` **CHỊ HAI**: Dạ, má đi giữ gìn sức khỏe. Ở trên này tụi con lo được.

**`s14c_walk_away` · `c19c`** – Bóng lưng nhỏ thó của Má xách túi vải lủi thủi bước đi xa dần cuối con hẻm sương sớm; vợ chồng Anh Hai bồng con thơ đứng nhìn theo. *(câm)*

## CHẶNG 7 NĂM RÒNG RÃ · 84 KỲ TRẢ GÓP *(Anh Hai ở lại đương đầu)*
**`s15_hanh_door` · `c14`** – Dãy trọ cũ. Hạnh hốc hác, **cổ tay trống**, điện thoại vẫn rung.
- `l45_ah` **ANH HAI**: Tôi là con trai chị Tư.
- `l46_ah` **ANH HAI**: Tôi hông tới đòi tiền. Tôi chỉ hỏi: mỗi người cô dắt vô, Long trả cô bao nhiêu?
- `l47_ha` **HẠNH**: Năm phần trăm.
- `l48_ha` **HẠNH**: Em mà ngưng xoay một bữa là sập hết. Em cũng nợ ổng. Nợ cả chục chỗ.
- `l49_ah` **ANH HAI**: Cô ghi giùm tôi một tờ: cô đã nhận bốn triệu ba của má tôi.
- `l50_ah` **ANH HAI**: Cô đừng dắt thêm ai nữa.

**`s16_standoff` · `c15`** – Quán cà phê. **Không nhạc.** Long ngồi đối diện. Ông Bảy ngồi bàn bên, **thoáng qua, không thoại**. Điện thoại đang ghi âm ngửa lên bàn.
- `l51_long` **LONG**: Chín triệu mốt. Anh mang đủ chưa?
- `l52_ah` **ANH HAI**: Má tôi cầm về tám triệu sáu, đã góp ba triệu chín. Còn bốn triệu bảy.
- `l53_ah` **ANH HAI**: Tôi tính thêm lãi đúng luật, làm tròn năm triệu.
- `l54_long` **LONG**: Anh giỡn hả?
- `l55_ah` **ANH HAI**: Anh thấy hông đúng thì mình mang giấy này, với mấy cuộc gọi lên xưởng tôi, ra công an nhờ tính giùm.
- `l56_ah` **ANH HAI**: Anh ký nhận đủ. Rồi trả tôi tờ giấy nợ.

**`s17_settled_paper` · `c16`** – Cận cảnh tờ giấy nợ gốc được thu hồi, Ông Bảy ký làm chứng. *(câm)*

**`s18_pawnshop` · `c17`** – Thẻ chương: **BẢY NĂM RÒNG RÃ · 84 KỲ TRẢ GÓP – CÁI GIÁ PHẢI TRẢ**. Tiệm cầm đồ: chủ tiệm lắc đầu, chiếc nhẫn của ba đã quá hạn thanh lý. *(câm)*

**`s19_five_am` · `c18`** – 5 giờ sáng. Anh Hai vịn cạnh bàn vì choáng. Chị Hai khoác áo lên vai chồng:
- `l57_ch` **CHỊ HAI**: Nợ thì trả dần. Anh mà ngã xuống, mình lấy gì trả.

**`s20_ledger_84m` · `c22`** – Sổ chi tiêu khép lại chặng đường 7 năm. Bong bóng: *"Ngân hàng gom nợ – Kỳ 84 / 84 (7 NĂM)"* · *"Khoản nợ cuối cùng – ĐÃ TẤT TOÁN"*.

## HỒI 5 – BẢY NĂM SAU · NGÀY MÁ QUAY VỀ *(Thời điểm F)*
**`s21_tet_return` · `c20`** – 7 năm sau, khi mọi sự bên ngoài đã êm xuôi, Má quay về trong ngày Tết bình dị ở nhà Anh Hai. Trên kệ tủ là mấy khung hình suốt 7 năm chỉ có vợ chồng Anh Hai và bé Tom lúc nhỏ. Đứa bé ngủ trên vai mẹ sáng hôm bà đi nay đã là **bé Tom 8 tuổi**, kéo ghế mời bà nội.
- `l62_ch` **CHỊ HAI**: Ăn cơm thôi cả nhà.

**`s22_bare_finger` · `c21`** – Cận bàn tay sương gió không nhẫn của Má nâng bát cơm trắng, đôi đũa của Anh Hai gắp miếng thịt kho tàu đặt vào bát. *(câm)*

**`s23_tom_asks` · `c21b`** – Cận trung bên mâm cơm Tết bình dị (bánh tét, củ kiệu, thịt kho trứng). Bé Tom (8 tuổi) hai tay bưng chén cơm, ngước mắt trong veo nhìn bà nội:
- `l62b_tom` **TOM**: Bà nội ơi, sao hồi con còn nhỏ, con hông thấy bà vậy?

**`s24_tet_silence` · `c21c`** – Cả bàn ăn khựng lại. Anh Hai dừng đũa, cúi mặt xuống chén cơm giấu đôi mắt cay xè. Má rưng rưng nhưng cố mỉm cười hiền, bàn tay trống nhẫn khẽ đặt lên đầu cháu:
- `l62c_ma` **MÁ**: Tại hồi đó bà ở xa. Giờ bà về ở luôn với Tom rồi.

**`s23_black_text` · `c23`** – Màn hình đen:
> **Có những khoản nợ phải mất nhiều năm mới trả hết.**
> **Và có những thứ, một khi đã mất, không thể lấy lại.**

## THẺ KẾT
**`s24_red_flags`** *(nền EP01b/scene18)*
- `l63_narr` **NGƯỜI BÓC TRẦN**: Người dắt bạn vào nợ có khi cũng đang chìm. Và tín dụng đen sống được là nhờ sự im lặng trong mỗi nhà.

### NHỚ KỸ – 5 DẤU HIỆU TÍN DỤNG ĐEN
1. **Ký mười, cầm tám:** tiền bị trừ trước khi đưa là lãi trá hình.
2. **Góp ngày, phạt trễ:** quy ra lãi năm có thể lên tới hàng trăm phần trăm.
3. **"Chị em cùng cảnh" rủ ký vay chia đôi:** giấy đứng tên bạn thì nợ là của bạn.
4. **Gọi lên chỗ làm, nhắn người thân:** giữ ghi âm, tin nhắn và trình báo công an.
5. **Khi trả nợ:** có biên nhận, có người làm chứng, lấy lại giấy nợ gốc.
- **Việc nên làm:** Trước khi ký bất kỳ giấy vay nào, hãy nói với một người thân. Và nếu bạn là người thân ấy, hãy nghe trước khi trách.

**`s25_disclaimer`** – LƯU Ý (hư cấu + thông tin pháp lý chỉ mang tính tham khảo).

---

## Tự kiểm "Không dạy lừa"
- [x] Không mô tả cách lập giấy vay, cách tính phí, cách tìm khách hay cách chia hoa hồng. Cơ chế chỉ lộ ra qua hậu quả.
- [x] Không tên ngân hàng, ứng dụng hay thương hiệu nào. Tin nhắn dùng bong bóng trung tính của engine.
- [x] Không dùng từ trong `policy_wordlists.json` (đã dùng "gây sức ép" thay cho từ nhạy cảm).
- [x] Không đổ lỗi cho nạn nhân. Má có lý do rất đời (lo Tết), Hạnh cũng là người đang chìm chứ không phải "ác nhân".

## ⚠️ Kiểm chứng pháp lý (bắt buộc trước khi Clearance ĐẠT)
- [ ] `l41`: trần lãi thỏa thuận 20%/năm và nguyên tắc phần vượt không có hiệu lực (Bộ luật Dân sự 2015). Không đọc số điều luật trong phim.
- [ ] `l42`: lãi đã trả vượt mức được trừ vào nợ gốc, và cách xử lý khoản "phí" trừ trước. Đã viết mềm thành *"đem ra tính cho rõ"*.
- [ ] `l53`: cách Anh Hai tính số còn phải trả (gốc thực nhận trừ đã góp, cộng lãi hợp pháp) có hợp lý về pháp lý không.
- [ ] `l55`: chỉ "ra công an nhờ tính giùm", không nói chắc là tội hình sự.
- [ ] Số liệu đã tự kiểm: (12 − 8,6) / 8,6 × 365/40 ≈ **360%/năm** ✔ · 8,6 − 3,9 = **4,7** ✔ · 5% × 10 triệu = **500 nghìn** ✔ · lãi 20%/năm trên 8,6 triệu trong khoảng 16 ngày ≈ 75 nghìn, nên làm tròn 5 triệu là trả dư ✔.
