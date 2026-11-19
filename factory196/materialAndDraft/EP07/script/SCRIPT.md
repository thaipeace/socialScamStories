# EP07 – SAU HAI TRĂM TRIỆU *(Bản kịch hóa điện ảnh – v2-draft sau phản biện pháp lý)*

- **Mã tập:** `EP07` · **Slug:** `SauHaiTramTrieu`
- **Họ kịch bản:** `MIX-RECOVERY` – Bẫy lừa lần hai. Hùng mất `200 triệu` vào một ứng dụng đầu tư lạ. Anh gạt lời vợ khuyên trình báo và nhờ **người quen ngoài xã hội** (mất `5 triệu`, nhận lại một câu phủi tay). Vì không dám nói thật với vợ, anh tin **một nhóm tự xưng lấy lại tiền** trên mạng. Nhóm này nói trúng tên người chăm sóc bên sàn cũ, một chi tiết Hùng chưa từng gửi, rồi lấy thêm `55 triệu`. Anh trình báo muộn gần 5 ngày. **Kết mở:** sàn đầu tư và nhóm "lấy lại tiền" là cùng một đầu mối.
- **Định dạng:** `16:9` · **Thời lượng:** công thức ước tính `444.7s`. Đối chiếu tỉ lệ giọng thật ở EP03/04/05/27 (0,77–0,84), bản thu thật dự kiến **khoảng 5:45 – 6:30**.
- **Tỷ lệ:** ~97% kịch / ~3% Người Bóc Trần (1 câu 19 từ, thẻ kết `8.72s`).
- **Thông điệp lõi:** *Kẻ lừa thứ hai không cần bạn ngây thơ. Nó chỉ cần bạn xấu hổ đến mức không dám nói ra, và chậm đến mức không kịp trình báo.*
- **Nguồn sự thật:** [`source/build_draft.py`](../source/build_draft.py) → [`episode.json`](../episode.json). Không sửa tay `episode.json`.

## Thay đổi so với v1 (theo phản biện ngày 19/11)
| # | v1 | v2 |
| :-: | :--- | :--- |
| 1 | Kẻ lừa là "đội anh hùng mạng", kết mở có "nhánh hiệp sĩ mạng" | **Nhóm Hỗ Trợ Lấy Lại Tiền** (tự xưng). Bỏ hoàn toàn "anh hùng mạng" và "hiệp sĩ" khỏi phim, tiêu đề, tag |
| 2 | Thẻ Nhớ Kỹ: "mọi văn phòng pháp lý trên mạng… đều là bẫy"; tên giả có chữ "pháp lý" | Đánh vào **hành vi**: "Ai hứa chắc kéo tiền về rồi đòi phí trước". Bỏ chữ "pháp lý" khỏi tên nhóm giả |
| 3 | Người quen "tìm ra địa chỉ chủ thẻ" | Không tìm ra gì; chỉ nói "toàn đứng tên người bán giấy tờ, lần theo chẳng tới đầu nậu" |
| 4 | "Sàn Đầu Tư Tài Sản Số" | **"Ứng dụng đầu tư lạ"** |
| 5 | Cán bộ 5 câu, chỉ nói "trễ rồi" | 3 câu ngắn, có **hành động thật**: khoản mới thì đề nghị ngân hàng xác minh ngay, khoản cũ thì khó hơn nhiều |
| 6 | Mốc "hai tuần" lệch; chặn liên lạc 2 lần | Mốc "một tuần trước", trình báo trễ "gần năm ngày"; Hook không còn câu chặn, cú lật mặt dồn về `s12` |
| 7 | Chốt bằng "kiêu ngạo" | Chốt bằng **"nỗi xấu hổ không dám nói ra"** (chữ đen cuối, câu lật mặt, câu trùm kết mở) |
| 8 | Không nhắc ngân hàng | Lan nhắc gọi ngân hàng 2 lần (`l12`, `l36`); thẻ Nhớ Kỹ có "gọi tổng đài ngân hàng" |
| 9 | ~8 phút ước tính | ~7:24 ước tính, khoảng 6 phút giọng thật |
| 10 | Tên "Long" (trùng chủ nợ EP27); "NGUYỄN VĂN T…"; "người lao động" | **Anh Tám**; người nhận `•••••`; "người bán giấy tờ" |
| 11 | Tuấn đọc lại dữ liệu Hùng vừa gửi | Tuấn nói trúng tên **"Ngọc"**, người chăm sóc bên sàn cũ mà Hùng không hề gửi. Chi tiết này được trả ở kết mở |
| + | Lan để chồng tự xoay mà không lý do | Hùng: "Tài khoản đứng tên anh… Cho anh ba ngày." Lời hứa đó trở thành áp lực khiến anh nói dối ở `s10` |
| + | Bé My dùng `be_na` (giọng người lớn) | Dùng `be_bong` (thiết kế cho bé gái) |

## Nhân vật & giọng (8 tuyến / 8 voice)
| Nhân vật | Key | Voice | Ghi chú |
|---|---|---|---|
| **Hùng** (38t, chủ xưởng sửa xe) | `anh_hai` | `Orus` | Tự tin → chới với → khàn vỡ |
| **Lan** (36t, vợ) | `chi_hai` | `Sulafat` | Kiệm lời, không chì chiết |
| **Bé My** (6t) | `be_bong` | `Leda` | **Nghe thử 1 câu trước khi thu cả tập** |
| **Anh Tám** (42t, quen ngoài xã hội) | `ong_bay` | `Algenib` | Có bản `phone` và `memory`. Nghe thử để chắc không ra giọng già |
| **Tuấn** (31t, tự xưng nhóm lấy lại tiền) | `ke_ngot_ngao_nam` | `Achird` | `phone`; ở kết mở là giọng phòng thật |
| **Cán bộ tiếp nhận** (nữ 35t) | `chi_tu` | `Zephyr` | 3 câu, không lên lớp |
| **Đầu dây trên** | `chu_no` | `Fenrir` | `phone`, 1 câu |
| **Người Bóc Trần** | `nguoi_boc_tran` | `Charon` | 1 câu |

## Bản đồ cài – trả
| Cài | Chi tiết | Trả |
|---|---|---|
| `s02` | Đồng hồ thép trên cổ tay trái Hùng | `s11` cầm đồ → `s14` Lan nhìn cổ tay trống → `s18` |
| `s02` | Bản vẽ xưởng mới, sân rộng cho bé My | `s10` liếc bản vẽ khi nói dối → `s16` cất vào hộc tủ → `s17` câu hỏi của bé My |
| `s03` | Tám: "Có chuyện gì cứ gọi một tiếng, anh em tao lo liền" | `s07` phủi tay → `s13` gọi không bắt máy + tiếng vọng → `s16` "ĐÃ XEM" |
| `s04` | Bong bóng **"CHUYÊN VIÊN NGỌC"** của ứng dụng đầu tư lạ | `s09` Tuấn nói trúng tên Ngọc → `s21` "Hồ sơ con Ngọc chuyển qua" |
| `s05` | "Cho anh ba ngày" | `s10` Lan hỏi "mai là hết ba ngày" → Hùng nói dối → `s12` "hông dám về nói thật với vợ" |
| `s05` | Lan: "Gọi ngân hàng… ra công an ngay sáng nay" | `s15` khoản cũ khó xác minh, khoản mới còn kịp |

---

## HOOK – ĐÊM THỨ TÁM
**`s00_hook_midnight` · `c00`** – 23:15, xưởng tối, cổ tay trái Hùng đã trống. Bong bóng **NHÓM HỖ TRỢ LẤY LẠI TIỀN**: *"Lệnh hoàn trả 200.000.000đ bị lỗi mã xác thực · Cần bổ sung 40.000.000đ"* (`TREO LỆNH`).
- `l01_hung` **HÙNG**: Đủ rồi! Tao vừa chuyển ba chục triệu cuối cùng xong, sao lại đòi thêm bốn chục triệu nữa?!
- `l02_tuan` **TUẤN** *(điện thoại)*: Anh Hùng bình tĩnh. Sai mã xác thực thì hệ thống khóa lệnh hoàn trả hai trăm triệu, bên em đâu mở được.
- `l03_hung` **HÙNG**: Tao biết tụi bây lừa tao rồi! Tao quen anh em ngoài đời, tụi bây trốn đâu tao cũng tìm ra!

**`s01_hook_freeze` · `c01`** – Chớp trắng, đứng hình gương mặt Hùng, nhịp tim. *(câm)*

## HỒI 1 – MỘT TUẦN TRƯỚC
**`s02_workshop_dream` · `c02`** – Bản vẽ xưởng mới trên bàn, đồng hồ thép trên tay Hùng.
- `l05_hung` **HÙNG**: Sáu năm vợ chồng mình gom góp mới đủ hai trăm triệu. Cuối tháng này ký cọc sang mặt bằng ngoài lộ lớn luôn.
- `l06_my` **BÉ MY**: Xưởng mới có cái sân rộng cho con chạy chơi hông ba?
- `l07_hung` **HÙNG**: Có chứ con gái! Sân rộng gấp ba lần ở đây luôn.
- `l08_lan` **LAN**: Tiền cọc đủ rồi thì anh cứ giữ yên trong ngân hàng, đừng xoay qua chỗ nào nữa nghen anh.

**`s03_drinking_table` · `c03`** – Quán vỉa hè, Hùng trả trọn chầu.
- `l09_tam` **ANH TÁM**: Chơi với thằng Hùng tao khoái cái tính sòng phẳng. Khu này có chuyện gì cứ gọi một tiếng, anh em tao lo liền.
- `l10_hung` **HÙNG**: Sống ngoài đời hơn nhau chỗ có anh em! Chứ đụng chuyện mà chạy đi làm đơn chờ giấy tờ tới chừng nào.

**`s04_first_trap_200m` · `c04`** – Hai tối sau. Bong bóng **CHUYÊN VIÊN NGỌC**: *"Lệnh thử đã rút +6.500.000đ · Gói chốt tuần: nạp 200.000.000đ trước 21h nha anh"* → **ỨNG DỤNG ĐẦU TƯ LẠ**: *"Tài khoản đã bị đóng băng"* (`MẤT 200 TRIỆU`).
- `l11_hung` **HÙNG**: Mấy triệu đầu rút thử trơn tru vậy mà… Ủa, sao vừa đẩy hai trăm triệu vô là sập trang luôn?!

## HỒI 2 – NGƯỜI QUEN NGOÀI ĐỜI & CÁI TÀI KHOẢN MƯỢN TÊN
**`s05_reject_police` · `c05`** – Sáng hôm sau.
- `l12_lan` **LAN**: Ngưng lại liền đi anh! Gọi ngân hàng khóa giao dịch, rồi cầm sao kê ra công an trình báo ngay sáng nay.
- `l13_hung` **HÙNG**: Báo công an?! Làm đơn chờ tới mùa quýt nào mới thấy lại tiền? Tiệm mình cuối tháng ký cọc rồi!
- `l14_lan` **LAN**: Hai trăm triệu là tiền sáu năm mình dành dụm. Ngoài ngân hàng với công an, ai truy được tiền trên mạng hả anh?
- `l15_hung` **HÙNG**: Tài khoản đứng tên anh, để anh lo! Cho anh ba ngày, anh nhờ anh Tám ngoài xã hội tìm tới tận cửa.
- *(Lan nhìn chồng rất lâu, im lặng.)*

**`s06_meet_tam` · `c06`** – Quán cà phê. Bong bóng **BIÊN LAI**: *"Người nhận: ••••• (TK ••••) · Tổng 3 đợt: 200.000.000đ"* (`ĐƯA 5 TRIỆU ĐI HỎI`).
- `l16_hung` **HÙNG**: Chút tiền xăng xe anh em đi việc. Anh Tám coi quen ai rành, lần giùm em cái tài khoản này nha.
- `l17_tam` **ANH TÁM**: Ừ, để anh hỏi thử mấy đứa coi sao.

**`s07_tam_brushoff` · `c07`** – Tối hôm sau, Hùng một mình trong xưởng nghe điện thoại.
- `l18_tam` **ANH TÁM** *(điện thoại)*: Tao hỏi mấy đứa rành chuyện này rồi. Tài khoản kiểu đó toàn đứng tên người bán giấy tờ, lần theo chẳng tới đầu nậu.
- `l19_hung` **HÙNG**: Vậy anh nhờ anh em lần tiếp đi anh! Hai trăm triệu của em đó!
- `l20_tam` **ANH TÁM** *(điện thoại)*: Dính lừa trên mạng là dính pháp luật, anh em tao hông đụng. Mày tự ra công an đi.
- *(Cúp máy. Không ai nhắc tới 5 triệu.)*

## HỒI 3 – CÁI BẪY LẦN HAI
**`s08_search_alone` · `c08`** – Đêm đó. Bong bóng **NHÓM HỖ TRỢ LẤY LẠI TIỀN**: *"Cam kết lấy lại tiền bị treo trên sàn · Không cần chờ thủ tục"* (`QUẢNG CÁO`) + **BÌNH LUẬN**: *"Cảm ơn nhóm đã lấy lại 180 triệu cho em sau 3 ngày!"* (`TÀI KHOẢN ẢO`).
- `l22_tuan` **TUẤN**: Nói thật với anh Hùng, chờ thủ tục lâu lắm. Bên em có đội kỹ thuật chuyên kéo tiền bị treo trên sàn về.
- `l23_hung` **HÙNG**: Tao mới mất hai trăm triệu xong, đừng hòng dụ tao lần nữa. Tụi bây có gì chứng minh làm được thật?
- `l24_tuan` **TUẤN**: Anh cảnh giác là đúng. Bên em hông thu đồng nào trước. Anh cứ gửi sao kê qua kiểm tra.

**`s09_insider_detail` · `c09`** – Hai tiếng sau. Bong bóng **HỒ SƠ #094**: *"Đã khóa nguồn tiền treo: 200.000.000đ · Chuyên viên phụ trách bên sàn: Ngọc"*.
- `l25_tuan` **TUẤN**: Đội kỹ thuật khóa được hai trăm triệu của anh rồi. Bên sàn đó, chuyên viên chăm sóc anh tên Ngọc, đúng hông?
- `l26_hung` **HÙNG**: Sao… sao mày biết tên con nhỏ đó? Tao đâu có gửi tin nhắn nào…
- `l26b_tuan` **TUẤN**: Bên em truy tới tận người chăm sóc bên sàn mà anh.
- `l26c_hung` **HÙNG**: Giỏi thiệt… hơn hẳn mấy ông anh ngoài đời.
- `l27_tuan` **TUẤN**: Lệnh khóa chỉ giữ hai mươi bốn tiếng. Anh đóng mười triệu mở hồ sơ, tiền về là hoàn lại đủ.

**`s10_doubt_and_lie` · `c10`** – Tối hôm sau, cạnh khe cửa phòng ngủ. Bong bóng: *"…bổ sung 15.000.000đ phí xác minh giải tỏa"*.
- `l28_hung` **HÙNG**: Khoan đã! Hôm qua mày nói đóng mười triệu là xong, sao nay đẻ thêm mười lăm triệu?! Tụi bây giở trò phải hông?
- `l29_tuan` **TUẤN**: Anh nghi thì cứ hủy hồ sơ, bên em đâu ép. Chỉ tiếc hai trăm triệu với mười triệu vừa đóng mất trắng thôi.
- `l30_lan` **LAN** *(vọng qua khe cửa)*: Anh Hùng ơi, mai là hết ba ngày rồi. Bên anh Tám lo tới đâu rồi anh?
- `l31_hung` **HÙNG**: Ờ… sắp xong rồi em. Em ngủ trước đi.

**`s11_pawn_watch` · `c11`** – Tháo đồng hồ cầm đồ. Bong bóng: *"Đợt 1: -10tr · Đợt 2: -15tr · Đợt 3: -30tr (Tổng lần hai: -55.000.000đ)"*. *(câm)*

**`s12_mask_off` · `c12`** – Đêm Hook, nối tiếp `l03`. Không nhạc.
- `l32a_tuan` **TUẤN**: Anh biết có mùi từ bữa đóng mười lăm triệu rồi, đúng hông?
- `l32b_tuan` **TUẤN**: Anh vẫn tự nộp thêm ba chục triệu… chỉ vì hông dám về nói thật với vợ thôi.
- *(Cúp máy. Bong bóng **ĐÃ CHẶN**.)*

## HỒI 4 – TRÌNH BÁO MUỘN MÀNG
**`s13_unanswered_call` · `c13`** – Gọi Anh Tám, không ai bắt máy.
- `l33_tam_mem` **ANH TÁM** *(tiếng vọng)*: Khu này có chuyện gì cứ gọi một tiếng, anh em tao lo liền.

**`s14_bare_wrist_confession` · `c14`**
- `l34_lan` **LAN**: Hết sạch rồi hả anh?
- `l35_hung` **HÙNG**: Hai trăm triệu ban đầu… cộng thêm sáu chục triệu anh tự đi lo bên ngoài… mất hết rồi Lan ơi.
- `l36_lan` **LAN**: Giờ gọi tổng đài ngân hàng liền đi anh. Sáng mai vợ chồng mình ra công an.

**`s15_police_truth` · `c15`** – Cán bộ mặc áo sơ mi trắng trơn, không sắc phục.
- `l37_cb` **CÁN BỘ**: Anh để gần năm ngày mới trình báo. Hai trăm triệu đầu chuyển đi lâu quá, xác minh khó hơn nhiều rồi.
- `l38_hung` **HÙNG**: Còn mấy khoản em nộp cho nhóm lấy lại tiền…
- `l39a_cb` **CÁN BỘ**: Mấy khoản đó còn mới. Tôi đề nghị ngân hàng phối hợp xác minh ngay.
- `l39b_cb` **CÁN BỘ**: Người lạ hứa kéo tiền về rồi đòi phí trước, đó là lừa lần hai.

## HỒI 5 – LÀM LẠI TỪ ĐẦU
**`s16_drawer_seen` · `c16`** – Cất bản vẽ vào hộc tủ. Bong bóng **ANH TÁM**: *"Anh Tám ơi, em kẹt tiền nhập đồ…"* (`ĐÃ XEM · 3 NGÀY TRƯỚC`). *(câm)*

**`s17_daughter_question` · `c17`**
- `l40_my` **BÉ MY**: Ba ơi, chừng nào mình dọn qua xưởng lớn có sân rộng cho con chạy chơi hả ba?

**`s18_start_over` · `c18`**
- `l41_hung` **HÙNG**: Chắc còn lâu lắm con… Ba làm sai rồi. Giờ ba phải làm lại từ đầu.

**`s19_black_epilogue` · `c20`**
> **Kẻ lừa đầu tiên lấy tiền bằng lời hứa bạn sẽ có thêm.**
> **Kẻ thứ hai lấy nốt phần còn lại, bằng nỗi xấu hổ không dám nói ra.**

## THẺ NHỚ KỸ
- `l42_narr` **NGƯỜI BÓC TRẦN**: Giấu người nhà, nhờ người quen thay vì báo công an, là mở cửa cho lần lừa thứ hai.
1. **Ai hứa chắc kéo tiền về rồi đòi phí trước:** đó là bẫy lừa lần hai, dù họ xưng là nhóm hỗ trợ, chuyên gia hay người từng bị lừa.
2. **Người quen ngoài đời không truy được tiền:** truy vết dòng tiền là việc của ngân hàng và cơ quan điều tra.
3. **Biết đúng chuyện của bạn chưa chắc đáng tin:** kẻ gian có thể chung một đầu mối với nhóm đã lừa bạn lần đầu.
4. **Dừng từ khoản phí đầu tiên.**
5. **Báo càng sớm càng có cơ hội:** gọi tổng đài ngân hàng, lưu sao kê, trình báo công an, đừng giấu người nhà.

## KẾT MỞ – CÙNG MỘT ĐẦU MỐI
**`s21_scam_ring_coda` · `c19`** – Phòng tối, không lộ mặt. Bong bóng **HỒ SƠ TUẦN NÀY**: *"Ứng dụng đầu tư: -200.000.000đ -> Nhóm lấy lại tiền: +55.000.000đ"* (`CHUYỂN VÒNG 2`).
- `l43_tuan_coda` **TUẤN**: Hồ sơ hai trăm triệu con Ngọc chuyển qua, bên em chốt thêm được năm mươi lăm triệu rồi anh.
- `l44_boss_coda` **ĐẦU DÂY TRÊN** *(điện thoại)*: Lọc tiếp danh sách tuần này. Ưu tiên mấy người giấu vợ con, chưa chịu đi trình báo.

**`s22_black_cut`** – Cắt đen. **`s23_disclaimer`** – LƯU Ý.

---

## Tự kiểm "Không dạy lừa" & "Không bôi nhọ"
- [x] Không có "anh hùng mạng", "hiệp sĩ", "pháp lý", "luật sư", "tài sản số" trong phim và metadata. Nhóm giả luôn được mô tả là **tự xưng**.
- [x] Thẻ Nhớ Kỹ đánh vào **hành vi** (hứa chắc + đòi phí trước), không đánh vào nghề nghiệp hay cộng đồng nào.
- [x] Không ai tìm ra danh tính hay địa chỉ chủ tài khoản, nên không ám chỉ ngân hàng làm lộ dữ liệu, không cổ súy tự truy tìm người.
- [x] Không mô tả cách lập sàn giả, cách mua bán tài khoản, cách dựng hồ sơ giả.
- [x] Cán bộ không hứa lấy lại tiền; chỉ nói khoản mới "đề nghị ngân hàng phối hợp xác minh".
- [x] Sạch `policy_wordlists.json` và regex Gate 5 (quét tự động lại sau khi sửa).

## ⚠️ Cần người có chuyên môn kiểm chứng trước khi chuyển Clearance sang ĐẠT
- [ ] `l39a_cb`: cách nói "đề nghị ngân hàng phối hợp xác minh" có đúng nghiệp vụ tiếp nhận tin báo không.
- [ ] `l18_tam`: mô tả "tài khoản đứng tên người bán giấy tờ" là thông tin phổ biến trên báo chí, không mang tính hướng dẫn.
- [ ] Tên **"Ứng dụng đầu tư lạ"** và **"Nhóm Hỗ Trợ Lấy Lại Tiền"** không trùng với tổ chức hay sản phẩm nào có thật.
- [ ] Người duyệt xem lại toàn bộ hàm ý, không chỉ kết quả quét từ khóa.
