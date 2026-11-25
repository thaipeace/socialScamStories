# KỊCH BẢN EP14 (V5 — LEVEL 3 FULL · BẪY BẢO HÀNH MÁY LẠNH GIẢ + KẾT MỞ ÔNG TÁM) — MẠO DANH TRUNG TÂM LỚN, GIỮ BO CÂU GIỜ ÉP BỎ ĐỀ PHÒNG! (~76 GIÂY)

- **Mã tập:** `EP14` (`BayBaoHanhMayLanh`) · **Nhà máy:** `factory619` (`9:16` · `1080×1920` · `30fps`) · **Chuẩn Motion:** `HRN-MOTION-L3.0` (`"motion_upgrade": "level3"` — Check 1 → 2 → 3 đầy đủ)
- **Nguồn cảm hứng nội bộ:** Trải nghiệm thực tế đã hư cấu hóa hoàn toàn kết hợp cảnh báo phổ biến về chiêu cố tình mạo danh trung tâm bảo hành lớn mua vị trí đứng đầu tìm kiếm, xem chi tiết tại [`source/SOURCE_NOTES.md`](../source/SOURCE_NOTES.md).
- **Tinh thần dựng (100% nhân vật sống với nhau · Đúng chuỗi nhân quả thực tế):**
  1. **Cố tình mạo danh trung tâm bảo hành lớn ngay từ đầu (`COND-02`):** Đẩy quảng cáo giả lên đầu kết quả tìm kiếm khi gia đình tra tìm trung tâm bảo hành lớn.
  2. **Thấy sai nhận diện nhưng ngại không dám đuổi (`COND-09`):** Hai thợ mặc đồ thường không đồng phục, vợ chồng đã nghi nhưng cả nể để họ tháo bo mạch mang đi kèm biên nhận viết tay.
  3. **Đòn tâm lý câu giờ 2 tầng cực thâm (`COND-04`):**
     - **Tầng 1 (Sau 2 ngày im bặt → báo giá 3 triệu → đồng ý):** Giữ bo mạch im bặt 2 ngày giữa nhà ống nóng ngộp thở để nạn nhân kiệt sức, bỏ hết đề phòng, chỉ muốn có máy xài liền → gọi báo giá **3 triệu** hứa làm liền là gật đầu đồng ý ngay!
     - **Tầng 2 (Thêm 5 ngày nữa mất hút → gọi gào lên → mới xuống ráp lấy 3 triệu):** Đồng ý xong vẫn câu thêm 5 ngày (tổng cả tuần trời), gọi số biên nhận không ai nghe → phải gọi lại số tổng đài đầu tiên gào lên đòi ráp thì họ mới chịu xuống ráp và thu đủ **3 triệu**!
  4. **Cú tát kép (Double Damage):** Ráp vô đúng **2 ngày sau ngắt điện y chang** → gọi đúng bảo hành chính hãng tới mới vỡ lẽ: **bo mạch chẳng hư, họ cũng chưa sửa, chỉ bị tháo rách tem mất luôn bảo hành hãng**!
  5. **Bóc trần siêu gọn 1 câu (`l10`, 17 từ, ~4.8s — cắt gọn nửa thời lượng cũ) + Thẻ `NHỚ KỸ` (`5.0s`) + Kết mở Quyền lực mềm 2.5D (`Khung 9`, ~6s):** Bên tà thắng êm, lộ thoáng **bóng lưng Ông Tám** (`EP07`, tóc muối tiêu, áo polo đen, **lắc bạc cổ tay phải**) bên tách trà & điện thoại ánh xanh ngọc lục bảo (tín hiệu ngầm Chị Hai) buông nhẹ đúng 1 câu: *"Chị thấy không, cũng chỉ là một trò chơi tâm lý."*

---

## 0. THẺ TẬP & KHUNG THƯ VIỆN CẢNH GIÁC *(theo `STRAT-VIGILANCE-LIB-V1`)*

| Mục | Nội dung |
| :--- | :--- |
| **Góc quan sát (Format `A–F`)** | **`A/B` (Giải phẫu chiêu lừa Lai Online → Offline: cố tình mạo danh trung tâm bảo hành lớn đứng đầu tìm kiếm + đòn câu giờ giữ bo mạch ép bỏ đề phòng)** |
| **Lớp 1 — Biến thể bổ sung (`VAR`)** | **`VAR-MIX-01`**: Cố tình mạo danh trung tâm bảo hành lớn mua vị trí đứng đầu tìm kiếm → cử thợ ngoài không đồng phục tới nhà tháo bo mạch → im bặt 2 ngày cho nóng ngộp rồi báo giá 3 triệu → đồng ý xong tiếp tục mất hút thêm 5 ngày mới xuống ráp thu tiền khống và làm rách tem hãng. |
| **Lớp 2 — Điểm dễ mắc (`COND`)** | `COND-02` (tin kết quả đứng đầu là trung tâm bảo hành lớn) · `COND-09` (thấy đồ thường nhưng cả nể ngại đuổi) · `COND-04` (nhà ống nóng ngộp thở khiến nạn nhân bỏ hết đề phòng, chỉ muốn có máy xài liền). |
| **Lớp 3 — Ứng phó (`RESP`)** | `RESP-01` (dừng ngay từ cửa khi thợ không đồng phục, không thẻ hãng, không khớp lịch hẹn) · `RESP-02` (không giao bo mạch/linh kiện đi theo giấy viết tay) · `RESP-03` (chỉ gọi đúng số tổng đài in trên phiếu bảo hành, hóa đơn mua hàng hoặc tem dán trên thân máy). |
| **Dàn nhân vật (`02_CAST/cast.json` — 6 giọng tách biệt 100%)** | • `anh_hai` (`Orus` — Anh Hai 35t, **chồng Chị Hai**)<br>• `chi_hai` (`Sulafat` — Chị Hai 34t, **vợ Anh Hai**)<br>• `ke_gia_danh` (`Fenrir` · `af: "phone"` — Đầu dây tổng đài bảo hành giả)<br>• `thang_tun` (`Puck` · `THỢ HÃNG` — Kỹ thuật viên chính hãng 28t)<br>• `nguoi_boc_tran` (`Charon` — Chốt siêu gọn 1 câu ở `Khung 7`)<br>• `ong_tam` (`Algieba` — **Ông Tám**, Phó tướng tâm lý & đối nội của Chị Hai từ `EP07`, chỉ lộ bóng lưng + lắc bạc ở `Khung 9`) |
| **1 câu neo ký ức (`Recall Anchor`)** | **"Mạo danh trung tâm lớn, giữ bo ép nóng, tự bạn gật đầu nên họ thoát êm!"** |

---

## 1. BẢNG PHÂN CẢNH CHI TIẾT, THOẠI, VISUAL MOTION LEVEL 3 & SOUND DESIGN (10 KHUNG · 11 CÂU · 184 TỪ)

- **Chuỗi Motion Anti-Repetition (0 chuỗi lặp `push_in` ≥ 3):** `slow_push_in` → `parallax_push_in` → `pan_left` → `split_horizontal` → `tense_push` → `pan_right` → `slow_push_in` → `static_hold` → `parallax_pull_out` → `static_hold`.
- **Zero Camera-Gaze:** Toàn bộ nhân vật trong `s1–s6` quay góc 3/4 nói chuyện tự nhiên với nhau hoặc qua điện thoại; tuyệt đối không nhìn ống kính.

| Khung | Beat & Motion Level 3 | Diễn biến Hình ảnh (`9:16`) & Sound Design đa lớp | Lời thoại chính (`speaker`) | Từ |
| :--- | :---: | :--- | :--- | :---: |
| **1. HOOK: ÔM BO CẢ TUẦN, NHÀ ỐNG NÓNG NGỘP** | `establishing`<br>**Level C** (`slow_push_in` + `animated_counter: 1→7 NGÀY` + `screen_glow` + Living-Char Anh Hai) | Phòng tối nóng hầm hập, máy lạnh tháo bung trơ dây. Anh Hai xoay 3/4 nói trực tiếp với Chị Hai bên cạnh giữa cái nóng ngột ngạt.<br>• **Hook:** `BẪY BẢO HÀNH MÁY LẠNH` — `Mạo danh trung tâm lớn, giữ bo ép giá!` | **l1 (`anh_hai`):** *"Mình ơi, họ ôm bo cả tuần rồi, nhà ống nóng ngộp chịu không nổi!"* | 15 |
| **2. NGUỒN CƠN: TÌM TRUNG TÂM LỚN TRÊN MẠNG** | `normal`<br>**Level B 2.5D** (`s2_bg` + `s2_fg` + `rack_focus` + `breathing` + `head_micro_tilt` + **4-state `mouth_sync`** + `red_circle_draw`) | Hồi tưởng ban ngày: máy lạnh nháy lỗi phía sau; Anh Hai cúi bấm điện thoại tìm trung tâm bảo hành lớn, `red_circle_draw` khoanh đỏ đúng nhãn quảng cáo giả đứng đầu. | **l2 (`anh_hai`):** *"Máy mới mua tám tháng cứ ngắt! Để anh tìm trung tâm lớn trên mạng gọi liền!"* | 17 |
| **3. THỢ ĐỒ THƯỜNG TỚI: NGHI NHƯNG NGẠI ĐUỔI** | `suspicion`<br>**Level C** (`pan_left` + Living-Char cả 2 vợ chồng) | Phòng khách ban ngày: 2 thợ mặc đồ thường không đồng phục leo thang tháo máy; Chị Hai ghé tai chồng thì thầm nghi ngại, Anh Hai lúng túng cả nể không dám đuổi. | **l3 (`chi_hai`):** *"Ủa anh ơi, sao họ mặc đồ thường chẳng có đồng phục siêu thị? Em thấy nghi nghi..."*<br>**l4 (`anh_hai`):** *"Anh cũng thấy lạ, mà người ta lỡ xuống tận nhà rồi, ngại quá chẳng dám đuổi!"* | 18<br>17 |
| **4. SAU 2 NGÀY IM BẶT: BÁO GIÁ 3 TRIỆU → ĐỒNG Ý ĐẠI** | `climax`<br>**Level C `split_screen` (`horizontal`)** (`whip_pan_left` + `waveform` + `animated_counter: 3.000.000đ · SAU 2 NGÀY IM BẶT` + Living-Char Anh Hai) | **Chia đôi trên–dưới:**<br>• **Trên (`ke_gia_danh` · `phone`):** Bóng tối cầm bo mạch, chờ 2 ngày khách nóng chịu hết nổi mới gọi báo giá 3 triệu hứa làm liền.<br>• **Dưới (`anh_hai`):** Anh Hai kiệt sức quay sang vợ bỏ hết đề phòng, đồng ý đại chỉ mong có máy xài liền! | **l5 (`ke_gia_danh` · `phone`):** *"Alo, bo hư nặng lắm, sửa ba triệu nha anh! Đồng ý thì tụi tôi làm liền!"*<br>**l6 (`anh_hai`):** *"Im bặt hai ngày nhà nóng ngộp quá! Thôi đồng ý đại, có máy xài liền mình ơi!"* | 17<br>18 |
| **5. THÊM 5 NGÀY MẤT HÚT (NGÀY 2→7): GỌI GÀO ĐÒI RÁP** | `climax`<br>**Level C** (`zoom_punch` + `tense_push` + `animated_counter: NGÀY THỨ 2→7 · THÊM 5 NGÀY MẤT HÚT` + `chromatic_pulse` + `shakes` + Living-Char Anh Hai) | Đêm nóng vàng rực hầm hập: Chị Hai phe phẩy quạt kiệt sức; Anh Hai đỏ bừng gào thẳng vào số điện thoại ban đầu vì đồng ý rồi mà thêm 5 ngày mất hút, số biên nhận không ai nghe! | **l7 (`anh_hai`):** *"Alo! Đồng ý rồi mà thêm năm ngày mất hút?! Gọi biên nhận không ai nghe, đem ráp liền!"* | 19 |
| **6. MỚI XUỐNG RÁP LẤY 3TR → 2 NGÀY NGẮT LẠI & RÁCH TEM** | `anomaly`<br>**Level C** (`whip_pan_left` + `pan_right` + `detail_reveal` + `red_circle_draw` + Living-Char Chị Hai, Anh Hai & Thợ hãng) | Ban ngày: Chị Hai đứng dưới lo lắng hỏi thẳng Kỹ thuật viên chính hãng (áo polo xanh, thẻ nhân viên). Thợ hãng trên thang soi đèn chỉ thẳng tem bảo hành bị rách cạnh bo mạch nguyên vẹn (`detail_reveal` + `red_circle_draw`). | **l8 (`chi_hai`):** *"Họ mới xuống ráp lấy ba triệu, hai ngày lại ngắt y chang, anh coi kỹ giùm em!"*<br>**l9 (`thang_tun` · `THỢ HÃNG`):** *"Bo mạch chẳng hư, họ cũng chưa sửa! Chỉ rách tem, mất bảo hành rồi anh chị!"* | 18<br>17 |
| **7. BÓC TRẦN SIÊU GỌN (1 CÂU)** | `anomaly`<br>**Level C** (`glitch` + `slow_push_in` + `detail_reveal` + `red_circle_draw` thanh quảng cáo đầu + `highlighter_sweep` bo mạch) | Kính lúp đỏ soi thẳng vào kết quả quảng cáo mạo danh trung tâm lớn đứng đầu nối tới bo mạch bị giữ — rút gọn đúng 1 câu lạnh, bỏ câu lặp lời khuyên (đã có ở `NHỚ KỸ`). | **l10 (`nguoi_boc_tran`):** *"Mạo danh trung tâm lớn, giữ bo ép nóng, tự bạn gật đầu nên họ thoát êm!"* | 17 |
| **8. THẺ `NHỚ KỸ`** | `ending`<br>**Level A** (`fade_black` + `static_hold`, `5.0s`) | Nền phòng sáng dịu + Thẻ **`NHỚ KỸ`** không thoại (`warm_outro`) chứa trọn 3 dấu hiệu & lời khuyên hành động. | *(Không lời thoại)* | 0 |
| **9. KẾT MỞ QUYỀN LỰC MỀM: BÓNG DÁNG ÔNG TÁM (2.5D)** | `suspicion`<br>**Level B 2.5D** (`fade_black` + `rack_focus` + `breathing` + `screen_glow` xanh ngọc + `ambient_particles` + `noir_evidence`) | Quán trà / phòng làm việc tối yên tĩnh: tiền cảnh **bóng lưng Ông Tám** (`EP07`, tóc muối tiêu chải ngược, áo polo đen, **lắc bạc cổ tay phải**, tuyệt đối không lộ mặt) bên tách trà nóng, sổ tay sơ đồ tâm lý và điện thoại sáng viền **xanh ngọc lục bảo** (tín hiệu ngầm Chị Hai). | **l11 (`ong_tam` · `Algieba`):** *"Chị thấy không, cũng chỉ là một trò chơi tâm lý."* | 11 |
| **10. CẮT ĐEN & `LƯU Ý`** | `ending`<br>**Level A** (`static_hold`, `2.7s`) | Khung đen sâu `#080A0E` + bảng **`LƯU Ý`** không thoại. | *(Không lời thoại)* | 0 |

---

## 2. LỜI THOẠI CHỐT V5 (11 CÂU · 184 TỪ ≤ 185 · MAX 19 TỪ/CÂU ≤ 22)

1. **`l1` (`anh_hai` · `Orus` · 15 từ):** *"Mình ơi, họ ôm bo cả tuần rồi, nhà ống nóng ngộp chịu không nổi!"*
2. **`l2` (`anh_hai` · `Orus` · 17 từ):** *"Máy mới mua tám tháng cứ ngắt! Để anh tìm trung tâm lớn trên mạng gọi liền!"*
3. **`l3` (`chi_hai` · `Sulafat` · 18 từ):** *"Ủa anh ơi, sao họ mặc đồ thường chẳng có đồng phục siêu thị? Em thấy nghi nghi..."*
4. **`l4` (`anh_hai` · `Orus` · 17 từ):** *"Anh cũng thấy lạ, mà người ta lỡ xuống tận nhà rồi, ngại quá chẳng dám đuổi!"*
5. **`l5` (`ke_gia_danh` · `Fenrir` · `phone` · 17 từ):** *"Alo, bo hư nặng lắm, sửa ba triệu nha anh! Đồng ý thì tụi tôi làm liền!"*
6. **`l6` (`anh_hai` · `Orus` · 18 từ):** *"Im bặt hai ngày nhà nóng ngộp quá! Thôi đồng ý đại, có máy xài liền mình ơi!"*
7. **`l7` (`anh_hai` · `Orus` · 19 từ):** *"Alo! Đồng ý rồi mà thêm năm ngày mất hút?! Gọi biên nhận không ai nghe, đem ráp liền!"*
8. **`l8` (`chi_hai` · `Sulafat` · 18 từ):** *"Họ mới xuống ráp lấy ba triệu, hai ngày lại ngắt y chang, anh coi kỹ giùm em!"*
9. **`l9` (`thang_tun` · `Puck` · `THỢ HÃNG` · 17 từ):** *"Bo mạch chẳng hư, họ cũng chưa sửa! Chỉ rách tem, mất bảo hành rồi anh chị!"*
10. **`l10` (`nguoi_boc_tran` · `Charon` · 17 từ):** *"Mạo danh trung tâm lớn, giữ bo ép nóng, tự bạn gật đầu nên họ thoát êm!"*
11. **`l11` (`ong_tam` · `Algieba` · 11 từ — Kết mở `s9` bóng lưng Ông Tám):** *"Chị thấy không, cũng chỉ là một trò chơi tâm lý."*

---

## 3. THẺ `NHỚ KỸ` (`red_flags` · 5.0 GIÂY · KHÔNG THOẠI)

- **Tiêu đề:** `NHỚ KỸ`
- **3 dấu hiệu nhận biết:**
  1. Cố tình mạo danh trung tâm bảo hành lớn đứng đầu tìm kiếm; thợ tới mặc đồ thường, không thẻ hãng
  2. Tháo bo mạch giữ lại rồi im bặt 2 ngày giữa trời nóng ngộp, chờ bạn bỏ đề phòng mới báo giá 3 triệu
  3. Đồng ý xong vẫn câu giờ thêm 5 ngày không nghe số biên nhận, phải gào đòi mới xuống ráp và rách luôn tem hãng
- **Nên làm (`action`):** *Chỉ gọi đúng số in trên phiếu bảo hành hoặc tem dán trên thân máy · Sai nhận diện dừng ngay từ cửa — không giao bo mạch cho thợ lạ!*

---

## 4. TỰ KIỂM "KHÔNG DẠY LỪA" & AN TOÀN (`L1` / `L2` / `L8`)

- [x] **Không định danh / Không vu khống (`L1`/`L2`):** Hư cấu hóa 100%, không tên hãng, không tên siêu thị, không tên công cụ tìm kiếm, không địa danh/SĐT thật.
- [x] **Sạch từ khóa `policy_wordlists.json`:** **0** `identity_hard_block`, **0** `identity_soft_warn`, **0** `asr_ocr_hard_block`, **0** `asr_ocr_soft_warn`.
