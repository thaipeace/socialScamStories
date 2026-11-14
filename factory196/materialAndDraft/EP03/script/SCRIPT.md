# EP03 – 120 NGÀN: PHÚT THỨ 89 (Bản Kịch Hóa Thoại Đời Thường – v5)

- **Mã tập:** `EP03`
- **Slug:** `120NganPhutThu89`
- **Họ kịch bản:** `ON-11` (Tuyển dụng giả trên mạng – Phỏng vấn phòng họp đông người → Đổi người sang "Quản lý dự án Bảo an xã hội" → Thả tiền mồi `120.000 VND` dưới danh nghĩa bài test tương tác tài chính thật → Đòi chuyển ngược `200.000 VND` tích điểm bảo an → Thoát ra bị cả phòng họp chia vai nhắn tin níu kéo)
- **Thời lượng mục tiêu:** ~280 giây (~4 phút 40 giây)
- **Định dạng:** `16:9` (`1920x1080 @ 30fps`)
- **Tỷ lệ Kịch / Bóc trần:** **95% Kịch có lời thoại / 5% Nhớ kỹ (đúng 10 giây)**
- **Nhân vật & Giọng (`02_CAST/cast.json`):**
  1. **Hoàng (`anh_hai` – voice `Orus`):** Lập trình viên Frontend 32 tuổi, **mặt mày sáng sủa cạo râu nhẵn nhụi**, mặc áo polo xám đậm, phỏng vấn tại phòng làm việc đầy nắng sáng Giáng Sinh.
  2. **Lan (`em_gai` – voice `Kore`):** Vợ Hoàng, 29 tuổi, dịu dàng, thực tế.
  3. **Bé Tom (`con_trai` – voice `Puck`):** Con trai 6 tuổi của Hoàng, háo hức đi chơi sáng Giáng Sinh.
  4. **Hà – Nhân sự vòng 1 (`ke_ngot_ngao_nu` – voice `Aoede`, `af: phone`):** Điều phối vòng 1, khi Hoàng thoát ra thì đóng vai "người quan tâm hỏi thăm sự cố mạng, báo cả nhóm đang đợi".
  5. **Khải – Quản lý dự án Bảo an xã hội (`ke_gia_danh` – voice `Fenrir`, `af: phone`):** Xuất hiện ở vòng 2, giọng trầm uy quyền, lấy lý do kiểm tra tương tác tài chính và quản trị ứng biến để chuyển `120.000 VND` rồi đòi chuyển ngược `200.000 VND`; khi Hoàng thoát thì dọa hủy hợp đồng `3.000.000 VND`.
  6. **Đức – Ứng viên 04 (`ke_ngot_ngao_nam` – voice `Achird`, `af: phone`):** "Quân xanh" trong phòng họp; khi Hoàng thoát ra thì nhắn tin khoe vừa rút được `380.000 VND` tiền thưởng để dụ Hoàng quay lại.
  7. **Trợ lý AI (`chi_tu` – voice `Zephyr`):** Giọng nữ điềm tĩnh, mạch lạc; tương tác trực tiếp với Hoàng ở 3 bước (vượt vòng 1, soi trang web lỗi ở đầu vòng 2, và cảnh báo về 120K tiền mồi / 200K chuyển ngược ở phút 88).
  8. **Thanh niên bàn bên (`con_trai` – voice `Puck`):** Chàng trai 23 tuổi ngồi bàn kế bên ở quán nước sáng Giáng Sinh – đã chuyển từ 200 ngàn rồi nạp thêm nhiều đợt đến mức đang bị đòi chuyển thêm `7.000.000 VND`.
  9. **Người Bóc Trần (`nguoi_boc_tran` – voice `Charon`):** Chỉ xuất hiện đúng 1 câu ở mở đầu và **10 giây duy nhất** ở thẻ Nhớ Kỹ (không thuyết giáo dài dòng).

---

## CẤU TRÚC NHỊP ĐỘ & CAO TRÀO

### MỞ ĐẦU – HOOK: 120 NGÀN TIỀN THẬT & CÁI BẪY "XEM KỊCH 80 NGÀN" (00:00 – 00:22)
- **Bối cảnh:** Phòng làm việc tại nhà buổi sáng nắng ấm (`c01.jpg`, `c02.jpg`), Hoàng cạo râu nhẵn nhụi, đeo tai nghe trước laptop.
- **00:00 – 00:08 (`s01_hook_ting`):**
  - *Âm thanh:* Tiếng *"Ting!"* ngân hàng dồn dập kèm nhịp tim.
  - *Hình ảnh:* Điện thoại của Hoàng hiện thông báo: `NGÂN HÀNG X: +120.000 VND`. Ngay sát dưới là tin nhắn nhiệm vụ: `Chuyển 200.000 VND để kích hoạt điểm trên hệ thống xã hội bảo an (Còn 01:00)`.
  - **Khải (`l01_khai`):** *"Còn anh Hoàng thôi! Hết một phút hệ thống tự hủy hồ sơ nha!"*
  - **Đức (`l02_duc`):** *"Em chuyển hai trăm ngàn xong rồi anh ơi! Lên điểm liền luôn!"*
- **00:08 – 00:22 (`s02_hook_finger`):**
  - *Hình ảnh:* Ngón cái của Hoàng lơ lửng cách nút `XÁC NHẬN CHUYỂN 200.000 VND` đúng 2mm.
  - **Hoàng (`l03_hoang`):** *"Nhận trăm hai rồi… chuyển lại hai trăm thì cùng lắm lỗ tám chục ngàn."*
  - **Hoàng (`l03b_hoang`):** *"Hay cứ thử coi tụi nó diễn trò gì?"*
  - *Đứng hình (Freeze-frame) + Riser:*
  - **Người Bóc Trần (`l04_narr`):** *"Đi phỏng vấn được chuyển nóng một trăm hai mươi ngàn."*
  - **Người Bóc Trần (`l04b_narr`):** *"Nhưng nếu tặc lưỡi bỏ ra hai trăm ngàn chỉ để xem kịch, cái giá ở phút thứ chín mươi sẽ không dừng ở đó."*

---

### HỒI 1: PHÒNG PHỎNG VẤN BUỔI SÁNG & MÀN "ĐỔI SẾP" (00:22 – 01:50)

#### Nhịp 1 – Áp lực "Ứng viên mồi" & Tương tác AI lần 1: Vượt vòng 1
- **Bối cảnh:** Sáng Giáng Sinh nắng ấm tại phòng khách (`c03.jpg`) và bàn làm việc cạnh cửa sổ ngập nắng sáng (`c04.jpg`, `c06.jpg`, `c05.jpg`).
- **Bé Tom (`l05_tom`):** *"Ba ơi, sáng Giáng Sinh ba hứa chở con đi chơi mà!"*
- **Lan (`l06_lan`):** *"Chín rưỡi mình đi nha anh."*
- **Hoàng (`l07_hoang`):** *"Cho ba đúng một tiếng. Bên Tập đoàn Viễn thông X hẹn phỏng vấn lập trình viên rồi."*
- **Hà – Nhân sự vòng 1 (`l08_ha`):** *"Vòng một: đọc tài liệu trong mười phút và trả lời câu hỏi chung. Ai nhanh nhất được cộng điểm ưu tiên!"*
- **Hoàng (`l09_hoang`):** *"Nhờ Trợ lý AI tóm tắt nhanh bộ tài liệu này coi."*
- **Trợ lý AI (`l09b_ai`):** *"Đã phân tích xong tài liệu. Đây là ba ý cốt lõi và đáp án để bạn trả lời vòng một."*
- **Đức (`l10_duc`):** *"Em xin trả lời câu hỏi vòng một theo đúng ba mục trong tài liệu tập đoàn ạ!"*
- **Hà (`l11_ha`):** *"Xuất sắc! Ứng viên số bốn và anh Hoàng vượt qua vòng một!"*

#### Nhịp 2 – Đổi người sang "Quản lý dự án Bảo an xã hội", lý giải bài test tài chính 120K & Tương tác AI lần 2
- **Hà (`l12_ha`):** *"Vòng hai sẽ do anh Khải, Quản lý dự án Hệ thống Xã hội Bảo an trực tiếp đánh giá."*
- **Khải (`l13_khai`):** *"Chào các bạn. Vòng hai có tương tác tài chính thật nhằm đánh giá khả năng quản trị ứng biến và kiến thức tài chính của ứng viên."*
- **Khải (`l13b_khai`):** *"Mời các bạn vào nền tảng dự án. Hệ thống sẽ chuyển hỗ trợ mỗi bạn một trăm hai mươi ngàn để thực hiện thao tác."*
- **Hoàng (`l14_hoang`):** *"Ủa, tuyển lập trình viên mà qua vòng hai lại kêu vào web dự án Bảo an xã hội? Trang con còn sai chính tả nữa…"*
- **Trợ lý AI (`l14b_ai`):** *"Hãy cẩn thận. Tuyển vị trí kỹ thuật nhưng lại dẫn sang trang web lỗi chính tả và lồng ghép thao tác tiền bạc là dấu hiệu bất thường."*

---

### HỒI 2: 120 NGÀN TIỀN THẬT, CÚ CHỐT PHÚT 89 & MÀN CHIA VAI NÍU KÉO (01:50 – 03:25)

#### Nhịp 3 – 120.000đ tiền thật đánh sập nghi ngờ & Cái bẫy "Lỗ 80 ngàn coi kịch"
- **Hoàng (`l15_hoang`):** *"Ủa… họ chuyển một trăm hai mươi ngàn hỗ trợ vòng hai thật luôn?"*
- **Đức (`l16_duc`):** *"Em nhận được trăm hai rồi anh Khải ơi! Dự án lớn có khác, uy tín quá!"*
- **Khải (`l17_khai`):** *"Giờ để chứng minh khả năng quản lý và giao tiếp, mỗi bạn chuyển ngược hai trăm ngàn vào tài khoản chỉ định."*
- **Khải (`l18_khai`):** *"Tiền này được ghi nhận thành điểm trên hệ thống xã hội bảo an, rút ra bất cứ lúc nào."*
- **Đức (`l19_duc`):** *"Em chuyển hai trăm ngàn xong rồi nha anh! Hệ thống cộng điểm liền luôn!"*
- **Hoàng (`l20_hoang`):** *"Trừ đi trăm hai mới nhận thì lỗ có tám chục ngàn. Coi như mua vé xem kịch cũng được mà…"*

#### Nhịp 4 – CAO TRÀO: Tương tác AI lần 3 & Phút 89 bấm THOÁT
- **Hoàng (`l20b_hoang`):** *"Nhưng người ta chuyển cho mình một trăm hai mươi ngàn thật rồi, giờ chuyển lại hai trăm ngàn tích điểm bảo an thì sao?"*
- **Trợ lý AI (`l20c_ai`):** *"Việc họ chuyển trước một trăm hai mươi ngàn không làm nó hợp pháp, mà càng khẳng định là kịch bản dẫn dụ."*
- **Trợ lý AI (`l20d_ai`):** *"Tuyệt đối không chuyển hai trăm ngàn, không làm nhiệm vụ tiếp theo và không cung cấp mã xác thực."*
- **Hoàng (`l21_hoang`):** *"Khoan… Mình đi ứng tuyển lập trình viên. Tại sao phải chuyển tiền để chứng minh khả năng giao tiếp?"*
- **Khải (`l23_khai`):** *"Anh Hoàng! Còn mười giây cuối, anh chuyển chưa?!"*
- *Hình ảnh (`s13_leave_meeting` – `c11.jpg`):* Đúng phút thứ 89, Hoàng bấm thẳng vào nút đỏ **`RỜI CUỘC HỌP`**.

#### Nhịp 5 – CẢ PHÒNG HỌP CHIA VAI NHẮN TIN NÍU KÉO HOÀNG QUAY LẠI (`s14a`, `s14b`, `s14c`)
- *Hình ảnh (`c12b.jpg`, `c12.jpg`):* Vừa thoát phòng họp được 3 giây, chiếc điện thoại trên bàn làm việc đầy nắng sáng của Hoàng rung bần bật. Hàng loạt tin nhắn từ các thành viên trong phòng họp dội về theo đúng kịch bản chia vai hoàn hảo:
  1. **Vai hỏi thăm sự cố & báo cả team đang đợi – Nhân sự Hà (`l24a_ha`):**
     *"Anh Hoàng ơi sao thoát vậy, mạng bên anh bị lỗi hả? Hồ sơ anh điểm cao nhất, cả nhóm đang đợi mình anh đó!"*
  2. **Vai ứng viên hỏi thăm thông tin & khoe vừa rút được tiền thưởng – Ứng viên 07 & Ứng viên 04 Đức (`l24b_duc`):**
     - *Bubble Ứng viên 07:* `"Ông ơi sao thoát ngang vậy? Bên ông bị vướng chỗ điền thông tin bảo an hả, cần tui chỉ cách làm không?"`
     - *Thoại Đức (`l24b_duc`):* *"Anh Hoàng ơi sao thoát uổng vậy?! Em vừa chuyển hai trăm ngàn xong, rút về được luôn ba trăm tám mươi ngàn tiền thưởng nè! Vô lại lẹ đi anh!"*
  3. **Vai Quản lý dự án thúc ép & thả mồi hợp đồng 3 triệu – Quản lý Khải (`l24c_khai`):**
     *"Anh Hoàng quay lại phòng họp gấp! Anh vừa được duyệt suất hợp đồng ba triệu đồng, bỏ ngang là hủy toàn bộ quyền lợi nhé!"*
- *Hình ảnh (`c12.jpg`):* Hoàng nhìn những dòng tin nhắn nhảy liên hồi trên màn hình, mỉm cười tỉnh táo:
- **Hoàng (`l24d_hoang`):** *"Người hỏi thăm rớt mạng, người chỉ cách làm, người khoe rút được tiền, người hứa hợp đồng lớn… Cả một phòng họp chia vai diễn kịch chỉ để kéo mình quay lại."*
- **Hoàng (`l24_hoang`):** *"Nghỉ khỏe."* (bấm chặn và khép màn hình laptop).

---

### NHỚ KỸ TRONG 10 GIÂY (03:25 – 03:35)
- *Hình ảnh (`s18_red_flags`):* Thẻ 3 dấu hiệu nhận biết hiện gọn trong 10 giây, không thuyết giáo dài dòng.
- **Người Bóc Trần (`l29_narr` – 7.5s):** *"Nhà tuyển dụng thật trả lương cho bạn, không bắt bạn nạp tiền. Thấy yêu cầu chuyển khoản: thoát phòng họp ngay."*

---

### HỒI 3: BA LY TRÀ TRÁI CÂY SÁNG GIÁNG SINH & LỆNH CHUYỂN 7 TRIỆU BÀN BÊN (03:35 – KẾT)
- **Bối cảnh (`c15.jpg`, `c16.jpg`, `c17.jpg`):** 10 giờ sáng Giáng Sinh 25/12 tại quán nước ngập nắng. Trên bàn gỗ của gia đình Hoàng là **3 ly trà trái cây nhiệt đới / trà sữa cỡ lớn** mát lạnh đồng nhất giữa mọi cảnh.
- **Bé Tom (`l30_tom`):** *"Woa, nay ba khao con ly bự luôn! Giáng Sinh vui quá ba ơi!"*
- **Lan (`l31_lan`):** *"Phỏng vấn sao rồi mà nay hào phóng dữ vậy anh?"*
- **Hoàng (`l32_hoang`):** *"Ba tự đánh rớt ở phút thứ tám mươi chín rồi."*
- **Hoàng (`l32b_hoang`):** *"Mà bên đó… tài trợ nhà mình một trăm hai mươi ngàn uống nước Giáng Sinh nè."*
- **Lan (`l33_lan`):** *"Hả? Đi xin việc mà rớt vẫn được khao nước?"*
- **Hoàng (`l34_hoang`):** *"Tiền mồi đó em. Hên là anh không bỏ thêm hai trăm ngàn để coi tiếp vở kịch của tụi nó."*
- *Hình ảnh (`c16.jpg` – trên bàn Hoàng vẫn là ly trà trái cây đá cỡ lớn):* Ngay bàn bên cạnh sau lưng Hoàng, một cậu thanh niên 23 tuổi đeo tai nghe trước laptop, giọng run rẩy:
- **Thanh niên bàn bên (`l35_tn`):** *"Anh ơi… từ nãy hai trăm ngàn em chuyển thêm mấy đợt rồi mà sao vẫn chưa rút về được vậy anh?"*
- **Giọng Khải vang ra từ tai nghe (`l36_khai_cafe`):** *"Chuyển thêm bảy triệu để hoàn tất hồ sơ đổi điểm bảo an thành tiền rút về em nhé!"*
- *Hình ảnh (`c17.jpg`):* Hoàng quay sang, sững người nhìn ngón tay run rẩy của cậu thanh niên đặt trên nút xác nhận chuyển **`7.000.000 VND`** — **CẮT ĐEN (`c18.jpg`)**.
- **Người Bóc Trần (`l37_narr`):** *"Bắt đầu từ hai trăm ngàn tưởng như chẳng đáng bao nhiêu."*
- **Người Bóc Trần (`l37b_narr`):** *"Nhưng khi đã bước vào vòng xoáy tiếc tiền, không ai biết mình sẽ dừng lại ở con số mấy triệu."*
