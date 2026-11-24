# KỊCH BẢN PHIM DÀI 16:9 (4–5+ PHÚT) – EP11: Người Biết Quá Nhiều

> Khung ngang `16:9` (`1920x1080 @ 30fps`) · **18 cảnh (`s00`–`s17`) · 36 câu thoại · 760 từ (`100% ≤ 26 từ/câu`) · ~5 phút 15 giây – 5 phút 45 giây (`~315s–345s`, đạt chuẩn `240s+`)** · Tỷ lệ **~97.5% kịch đời thực / ~2.5% Người Bóc Trần (`1 câu, 24 từ, < 8s`)** theo [LONG_FORMAT_196_SPEC.md](../../../../00_HARNESS_GUIDELINES/LONG_FORMAT_196_SPEC.md), [STORY_AND_PRODUCTION_HARNESS.md](../../../../00_HARNESS_GUIDELINES/STORY_AND_PRODUCTION_HARNESS.md) và [VISUAL_MOTION_HARNESS.md](../../../../00_HARNESS_GUIDELINES/VISUAL_MOTION_HARNESS.md) (`HRN-MOTION-L3.0` · `"motion_upgrade": "level3"`).
> Kịch bản nguồn: [`story.txt`](../story.txt) · Nguồn sự thật timeline khi dựng: `source/build_draft.py` → sinh `episode.json`.
> **Độc lập 100%:** Không kết nối vũ trụ các tập trước. Mọi tên người, nhà hàng, đối tác, tài khoản và số tiền đều là **hư cấu hoặc chung chung**.

---

## 0. Thẻ tập phim & Khung Thư viện Cảnh giác *(theo [VIGILANCE_LIBRARY_FRAMEWORK.md](../../../../00_HARNESS_GUIDELINES/VIGILANCE_LIBRARY_FRAMEWORK.md))*

| Mục | Nội dung |
| :--- | :--- |
| **Mã tập / Slug** | `EP11` (`factory196`) · `NguoiBietQuaNhieu` |
| **Góc quan sát (Format `A–F`)** | **`A`** – Giải phẫu chiêu bôi nhọ truyền thông bẩn ép chi tiền gỡ bài + mắt xích nội gián *(nhúng trực tiếp ứng phó thực chiến `RESP` vào Hồi 4–5)* |
| **Nhóm chiêu & Biến thể Lớp 1 (`VAR`)** | **`VAR-EXT-01`** – Đăng bài bôi nhọ ẩn danh cài **ảnh thật từ góc khuất nội bộ** + bình luận mồi ám chỉ quán + chủ động đóng vai *"dịch vụ hỗ trợ xử lý truyền thông"* đòi khoản phí đầu vừa tầm (`20 triệu`) để thử ngưỡng sợ → 4 ngày sau đổi trang ẩn danh mới tung ảnh mới nâng giá gấp ba (`60 triệu`) nhờ tay trong tuồn thông tin |
| **Điểm dễ mắc Lớp 2 (`COND`)** | `COND-01` (vừa chi tiền sửa sảnh, rất cần hợp đồng tiệc đoàn 300 khách bù vốn) · `COND-02` (thấy đối phương có ảnh thật kho bếp & biết đúng hợp đồng ngày mai nên tin họ nắm thóp thật) · `COND-05` (sát giờ ký sáng mai, đối tác vừa gọi hỏi thăm) · `COND-06` (tin nhân viên lễ tân thân cận) |
| **Giá trị ứng phó Lớp 3 (`RESP`)** | `RESP-01` (dừng trả tiền ngay; chuyển lần đầu là xác nhận "con mồi biết sợ" để bị vắt tiếp) · `RESP-02` (không tự nhắn tin nhận vơ trước khi bài chưa nêu tên; không tự đối chất hay trả đũa ngoài luật) · `RESP-03` (rà soát lỗ hổng thông tin nội bộ thay vì chỉ phòng người ngoài) · `RESP-04`, `RESP-05` (lưu nguyên đường dẫn, ID trang, tin nhắn, sao kê và **lập vi bằng qua Thừa phát lại** trước khi đối phương xóa bài phi tang, rồi nộp hồ sơ trình báo công an) · `RESP-06` (không im lặng chi tiền "cho êm chuyện") |
| **1 câu neo ký ức (`Recall Anchor`)** | **"Bị bôi nhọ vòi tiền gỡ bài: càng trả càng bị nâng giá — giữ chứng cứ, lập vi bằng rồi báo công an ngay!"** |
| **Thời lượng mục tiêu** | `~315s – 345s` (~5 phút 15 giây – 5 phút 45 giây, đạt chuẩn `240s+`) |
| **Nhân vật trung tâm** | **Hùng** (`anh_hai` / `Orus`, 40t) – Chủ nhà hàng dày dạn, coi trọng uy tín; lung lay lần đầu trước áp lực sát giờ ký nhưng nhanh chóng tỉnh táo lật lại thế cờ hoàn toàn đúng luật |
| **Đối trọng & Tuyến phụ** | **Minh** (`thang_tun` / `Puck`, 31t, quản lý) · **Lan** (`be_na` / `Leda`, 25t, lễ tân – nội gián) · **Admin** (`chu_no` / `Algieba`, 38t, giấu mặt phòng tối) · **Chị Trang** (`chi_hai` / `Sulafat`, 38t, đại diện công ty đối tác) · **Người Bóc Trần** (`nguoi_boc_tran` / `Charon`) |
| **Nguyên tắc phòng vệ cốt lõi** | Không trả tiền gỡ bài để mua "sự yên ổn" ảo; không tự nhắn tin nhận vơ; giữ nguyên đường dẫn, ID trang, tin nhắn, sao kê — lập vi bằng giữ hiện trạng trước khi đối phương xóa dấu vết rồi trình báo cơ quan công an, đồng thời kiểm tra lỗ hổng nội bộ |

### Tự kiểm Pre-Gate 0 (Bộ lọc `4+2`)
- [x] **Mới:** Phủ đúng khoảng trống mới trên [VIGILANCE_LIBRARY_MAP.md](../../../../01_SCAM_MAP/VIGILANCE_LIBRARY_MAP.md) — chiêu bôi nhọ thương hiệu/quán ăn núp bóng *"dịch vụ xử lý truyền thông"* kết hợp mắt xích nội gián.
- [x] **Thực dụng:** Áp dụng trực tiếp cho chủ quán, hộ kinh doanh và người làm dịch vụ khi gặp bài bôi nhọ vòi tiền.
- [x] **Khác biệt:** Không lặp lại mô-típ lừa tiêu dùng/đầu tư; tập trung vào tâm lý "bỏ tiền lần đầu cho êm" và phép thử hợp pháp bóc lộ rò rỉ nội bộ.
- [x] **Có ích:** Người xem nắm rõ thao tác **lập vi bằng giữ hiện trạng** trước khi đối phương xóa bài/khóa trang phi tang, kèm cách trình báo công an đúng quy trình.
- [x] **Dễ kể lại:** Đã nén gọn thành 1 câu neo ký ức sắc bén.
- [x] **An toàn:** 100% hư cấu, không logo/giao diện app/số tài khoản/sắc phục thật; không dạy lừa (`L2`), không viện dẫn số điều luật chưa kiểm chứng (`L7`), không khuyến nghị sai nghiệp vụ (`L8`), sạch 100% [policy_wordlists.json](../../../../00_HARNESS_GUIDELINES/policy_wordlists.json).

---

## 1. Nhân vật, Phân tách giọng (`02_CAST/cast.json`) & Bản đồ Cài – Trả

### Phân tách giọng (6 tuyến / 6 voice độc lập 100%)
| Nhân vật | Key (`cast.json`) | Voice | Chỉ đạo diễn xuất & âm sắc (Phương ngữ miền Nam) |
| :--- | :--- | :---: | :--- |
| **Hùng** (40t, chủ nhà hàng) | `anh_hai` | **`Orus`** | Nam miền Nam trầm chắc, điềm tĩnh; căng thẳng dồn nén ở Hồi 2, sắc lạnh và tỉnh táo ở Hồi 4–5 |
| **Minh** (31t, quản lý) | `thang_tun` | **`Puck`** | Nam miền Nam tông sáng, nhịp nhanh, thẳng tính; thực tế khi can ngăn, bức xúc ở Hồi 3, bất ngờ trước nước cờ của Hùng ở Hồi 4 |
| **Lan** (25t, lễ tân) | `be_na` | **`Leda`** | Nữ miền Nam trẻ, trong trẻo, lễ phép tự nhiên; tuyệt đối không diễn lộ vẻ gian ác để giữ độ bất ngờ tới Coda |
| **Admin** (38t, kẻ đứng sau) | `chu_no` | **`Algieba`** | Nam miền Nam trầm mượt, lịch sự mà lạnh (`af: "phone"`), nói kiểu "dịch vụ chuyên nghiệp", không gào thét |
| **Chị Trang** (38t, đối tác) | `chi_hai` | **`Sulafat`** | Nữ miền Nam trầm vừa, chững chạc (`af: "phone"`), dè dặt lịch sự khi hỏi về đường link lạ |
| **Người Bóc Trần** | `nguoi_boc_tran` | **`Charon`** | Nam trung niên điềm tĩnh, rõ chữ — đúng **1 câu (24 từ, `< 8s`)** ở thẻ `NHỚ KỸ` |

### Dòng tiền hư cấu & Bản đồ Cài – Trả
- **Bậc thang dòng tiền (100% hư cấu):** Lần 1 **`20.000.000đ`** *(phí gỡ bài đêm trước ngày ký hợp đồng 300 khách)* → 4 ngày sau đổi trang mới tung ảnh mới nâng gấp ba lên **`60.000.000đ`** *(Hùng dừng hẳn, không chuyển thêm)*.
- **Hình ảnh biểu tượng đối lập:** Sảnh nhà hàng đèn vàng ấm, bàn tiệc trắng, cuốn sổ lịch phòng VIP 300 khách ↔ Ánh xanh lạnh của bài bôi nhọ có ảnh chụp lén góc kho bếp chưa dọn & con dấu đỏ **`VI BẰNG & TIẾP NHẬN TIN BÁO · 16:30 HÔM QUA`**.

| Cài ở | Chi tiết điện ảnh | Trả ở |
| :--- | :--- | :--- |
| **`s02` (Hồi 1)** | Lan mang **cuốn sổ lịch phòng VIP** vào xác nhận hợp đồng **tiệc 300 khách bên công ty chị Trang** lúc 10h sáng mai *(chỉ 3 người biết: Hùng, Minh, Lan)* | **`s05` (Hồi 2):** Admin gọi điện nhắc trúng phóc *"mai quán ký tiệc ba trăm khách bên chị Trang"* → **`s09` (Hồi 4):** Hùng xếp 3 chứng cứ và khựng ngay dòng này |
| **`s03` (Hồi 1)** | Bài đăng mới lên **`18 phút`**, chưa ghi tên, mới vài lượt xem — nhưng chính **Lan** đem lên văn phòng đầu tiên và nhắc *"phiền hợp đồng chị Trang"* | **`s09` (Hồi 4):** Hùng nối mốc `21:30` (ảnh góc kho bếp) → `21:48` (Lan đưa lên) để nhận ra lỗ hổng nội bộ |
| **`s04` (Hồi 1)** | Hùng nhận ra **góc kho bếp** khách ngoài sảnh không thể vào chụp | **`s08` (Hồi 3):** Trang ẩn danh mới tung tiếp **ảnh khu nhập hàng sáng sớm** → khẳng định 100% ảnh chụp từ người bên trong |
| **`s10` (Hồi 4)** | `16:30` chiều, Hùng và Minh lập xong **`VI BẰNG`** và nộp đơn trình báo công an | **`s11` (Hồi 4):** `21:50` tối Hùng cố ý nói trước mặt Lan là *"sáng mai mới đi"* → **`s12` & `s15` (Hồi 5 & Coda):** `22:14` Lan báo xóa sạch hai trang tưởng thoát nạn, không ngờ vi bằng đã chốt từ `16:30` chiều hôm trước |

---

## 2. Cấu trúc 5 Hồi & Kế hoạch Visual Motion (`HRN-MOTION-L3.0` · Level 3 + Living-Character 2.5)

*Kiểm soát chặt **CHECK 1 → 2 → 3**: `"motion_upgrade": "level3"` · Tổng **18 cảnh**: **Level A = 3** (`s13, s16, s17`) · **Level B = 4** (`s00, s02, s08, s14` — 2.5D Parallax + `breathing` + `rack_focus` / `head_micro_tilt`) · **Level C = 11** (Living-Character 2.5 khóa pixel qua `03_ENGINE/face_roi_prep.py`: `eye_blink = 11`, `mouth_sync = 10` gồm khẩu hình 4 trạng thái `round_image` ở các cảnh cận đắt giá, `eye_gaze = 2`; kết hợp Level 3 FX: `split_screen` 2 cảnh, `phone_waveform`, `red_circle_draw`, `highlighter_sweep`, `animated_counter`, `typing_indicator`, `rain_layer`, `ambient_particles`, `light_sweep`, `color_mood`, `chromatic_pulse`) · **Level D = 0** · **0 chuỗi lặp `push_in` ≥ 3 cảnh liên tiếp** (tối đa 2 ở `s08–s09`) · **`shakes` = 2/18 cảnh (`11%`)** khớp `impact`.*

| Hồi | Thời gian dự kiến | Cảnh (`Asset`) | Diễn biến tâm lý & Hành động | Beat · Motion Level · Hiệu ứng L2/L3 | Âm thanh & SFX khớp Motion |
| :--- | :---: | :--- | :--- | :--- | :--- |
| **HOOK** | `00:00–00:11` | `s00` (`c00`) | Đêm trước ngày ký: ảnh góc kho bếp + cuộc gọi *"hai chục triệu là êm re"* | `climax` · **Lv B** (`push_in` 2.5D + `rack_focus` nền → điện thoại + `screen_glow` + `phone_waveform` + `color_mood: high_tension`) | `suspense_pulse` + `phone_ring` + `notification` |
| **HOOK** | `00:11–00:22` | `s01` (`c01`) | Chớp trắng 4 ngày sau tối mưa: biên lai `20tr` + trang mới tung ảnh sáng nay đòi `60tr` | `aftermath` · **Lv C** (`static_hold`, `flash_white`, `rain_layer`, `animated_counter` `20tr→60tr`, `chromatic_pulse`, Living-Char `Hùng`, `shakes` 1 mốc) | `impact` + `rain` + `counter_tick` + cắt về `room_tone` |
| **HỒI 1** | `00:22–00:46` | `s02` (`c02`) | Bốn tối trước (`19:30`), sảnh đèn vàng ấm; Lan mang sổ phòng VIP chốt tiệc 300 khách bên chị Trang | `establishing` · **Lv B** (`pan_right` 2.5D + `breathing` + `head_micro_tilt` + Living-Char `Lan/Minh/Hùng` + `ambient_particles` + `color_mood: warm_daily`) | `chapter_sting` + `crowd` dịu + `warm_daily` |
| **HỒI 1** | `00:46–01:08` | `s03` (`c03`) | `21:48`: Lan đem bài đăng mới lên 18 phút (ảnh góc kho bếp) tới văn phòng, nhắc *"phiền hợp đồng chị Trang"* | `information` · **Lv C** (`pan_left`, Living-Char `Lan` & `Hùng`, `screen_glow`, `focus_highlight`) | `room_tone` + `notification` + `low_accent` nhẹ |
| **HỒI 1** | `01:08–01:22` | `s04` (`c04`) | Minh thấy ít tương tác tưởng nhẹ; Hùng nghi ngại góc kho bếp khách ngoài không vào chụp được | `suspicion` · **Lv C** (`slow_pull_out`, Living-Char `Minh` & `Hùng`, `detail_layer` zoom góc bếp, `color_mood: cold_suspicion`) | `investigative_story` + `low_accent` |
| **HỒI 2** | `01:22–01:55` | `s05` (`c05_l`, `c05_r`) | `21:55`: Admin phòng tối chủ động gọi chào *"gỡ bài 20 triệu"*, nhắc trúng tiệc 300 khách bên chị Trang | `suspicion` · **Lv C** (**`split_screen`** dọc Trái `Admin` – Phải `Hùng`, `whip_pan_left`, `phone_waveform`, Living-Char `Hùng`, `color_mood: cold_suspicion`) | `phone_vibrate` + `click` + `tension_drone` |
| **HỒI 2** | `01:55–02:18` | `s06` (`c06_l`, `c06_r`) | Chị Trang gọi điện dè dặt vì nhận link lạ gửi tới công ty, nói mai cân nhắc lại | `anomaly` · **Lv C** (**`split_screen`** dọc Trái `Chị Trang` – Phải `Hùng`, `luma_wipe`, `phone_waveform`, Living-Char `Hùng` & `Chị Trang`) | `phone_ring` + `heartbeat` nhẹ |
| **HỒI 2** | `02:18–02:50` | `s07` (`c07 → c07_gone`) | Nửa đêm: Minh can ngăn nhưng Hùng chuyển `20tr` giữ hợp đồng; 15 phút sau bài biến mất | `aftermath` · **Lv C** (`static_hold`, Living-Char `Hùng` & `Minh`, `cursor_click`, `detail_reveal` bài biến mất, `light_shift`) | `night_room` + `click` + `bank_ting` + `notification` |
| **HỒI 3** | `02:50–03:22` | `s08` (`c08`) | Bốn ngày sau: trang ẩn danh mới đăng ảnh khu nhập hàng sáng nay + Admin gọi vòi `60tr` → Hùng bừng tỉnh | `climax` · **Lv B** (`drift_push` 2.5D + `breathing` + `head_micro_tilt`, Living-Char `Hùng` & `Minh`, `animated_counter` `20tr→60tr`, `phone_waveform`, `chromatic_pulse`) | `phone_vibrate` + `counter_tick` + `suspense_pulse` + `call_end` |
| **HỒI 4** | `03:22–03:52` | `s09` (`c09`) | `14:15`: Hùng xếp 3 chứng cứ trên máy tính, khoanh đỏ *"tiệc 300 khách"* & mốc `18 phút` → nhận ra rò rỉ nội bộ | `anomaly` · **Lv C** (`zoom_punch`, `slow_push_in`, **`red_circle_draw`**, **`highlighter_sweep`**, Living-Char `Hùng` & `Minh`, `color_mood: noir_evidence`) | `keyboard` + `marker_draw` + `low_accent` |
| **HỒI 4** | `03:52–04:08` | `s10` (`c10 → c10_police`) | `16:30`: Hùng & Minh ra khỏi Văn phòng Thừa phát lại (cầm `VI BẰNG`) rồi nộp đơn tại cổng cơ quan công an | `information` · **Lv C** (`pan_right`, `detail_reveal` dấu đỏ `VI BẰNG`, `ambient_particles`, `light_sweep`) | `street` dịu + `click` dấu + `chapter_sting` |
| **HỒI 4** | `04:08–04:38` | `s11` (`c11`) | `21:50`: Hùng cố ý nói *"sáng mai đi lập vi bằng báo công an"* đúng lúc Lan mang sổ vào → ánh mắt Lan khựng nửa nhịp | `suspicion` · **Lv C** (`static_hold`, Living-Char 2.5 **`Lan` `eye_gaze`** + `eye_blink`/`mouth_sync` `Hùng/Minh/Lan`, `light_shift`) | `room_tone` căng + `low_accent` đúng nhịp Lan khựng mắt |
| **HỒI 5** | `04:38–04:56` | `s12` (`c12 → c12_file`) | Sáng hôm sau: cả hai trang đã tự xóa từ hơn `22h` đêm qua; Hùng đặt tay lên tập `VI BẰNG` đã chốt hồi chiều | `aftermath` · **Lv C** (`slow_pull_out`, `detail_reveal` màn hình xóa bài ↔ tập `VI BẰNG`, Living-Char `Minh` & `Hùng`, `color_mood: warm_daily`) | `warm_outro` nhẹ + `click` |
| **HỒI 5** | `04:56–05:05` | `s13` (`c12`) | Thẻ **`NHỚ KỸ`** (`4 dấu hiệu + 1 việc nên làm ngay`) + đúng 1 câu `Người Bóc Trần` (`< 8s`) | `ending` · **Lv A** (`static_hold`, không rung, làm tối nền 60%) | `bank_ting` + `warm_outro` |
| **CODA** | `05:05–05:18` | `s14` (`c14`) | Sảnh sáng: Hùng cảm ơn Lan bình thản; Lan cười nhẹ nhõm; ánh mắt Hùng lạnh đi qua mặt kính phản chiếu | `suspicion` · **Lv B** (`pan_left` 2.5D + `rack_focus` Lan ↔ phản chiếu kính Hùng + `head_micro_tilt` + **`Hùng` `eye_gaze`** + Living-Char `Hùng/Lan`) | `crowd` nhẹ → tắt dần sang `tension_drone` |
| **CODA** | `05:18–05:33` | `s15` (`c15 → c15_stamp`) | Cắt nhanh phòng tối (`22:14 ĐÊM QUA`): tin nhắn `LAN – LỄ TÂN` + lời Admin *"yên tâm không lộ đâu"* → tắt phụt, đập cận dấu đỏ **`VI BẰNG · 16:30 HÔM QUA`** | `climax` · **Lv C** (`film_burn`, `slow_push_in`, **`typing_indicator`**, `chat_bubbles`, `phone_waveform` `Admin`, `detail_reveal` dấu đỏ `16:30`, `chromatic_pulse`, `shakes` 1 mốc) | `typing` + `message_send` + `click` + **`impact` trầm** |
| **CODA** | `05:33–05:35` | `s16` (`c16`) | Cắt đen đột ngột `1.2s` | `ending` · **Lv A** (`static_hold`, đen tuyệt đối) | Im lặng hoàn toàn |
| **KẾT** | `05:35–05:39` | `s17` (`c12`) | Bảng **LƯU Ý** (`3.5s`) | `ending` · **Lv A** (`static_hold`, không rung) | `room_tone` siêu nhẹ |

---

## 3. Kịch bản lời thoại chi tiết (`36 câu · 760 từ · 100% ≤ 26 từ · Phương ngữ miền Nam`)

### MỞ MÀN (HOOK) – HAI CHỤC TRIỆU CHO ÊM & TẤM ẢNH HỒI SÁNG

**`s00_hook_night_post` · `c00` (Lv B · 2.5D `push_in` + `rack_focus` + `screen_glow` + `phone_waveform`)** – Văn phòng nhà hàng tối bớt đèn, bản hợp đồng đặt tiệc còn mở trên bàn. Điện thoại Hùng sáng ánh xanh lạnh: bài đăng ẩn danh kèm **tấm ảnh chụp lén góc khuất kho bếp** chưa dọn và vài bình luận úp mở. Cắt thoáng bàn tay trong phòng tối đang gọi điện. *(Bong bóng trung tính: "GỠ SẠCH BÀI TỐI NAY · PHÍ HỖ TRỢ: 20.000.000đ" · `ĐÊM TRƯỚC NGÀY KÝ`)*
- `l01_admin_p` **ADMIN** *(cuộc gọi, mượt mà lạnh)*: Ngày mai quán anh ký tiệc ba trăm khách, để lùm xùm tối nay thì tiếc lắm. Hai chục triệu là êm re.

**`s01_hook_cut_round2` · `c01` (Lv C · `static_hold` + `flash_white` + `rain_layer` + `animated_counter` + `chromatic_pulse` + Living-Char `Hùng`)** – **CHỚP TRẮNG + IMPACT!** Bốn ngày sau, tối mưa ngoài cửa kính văn phòng. Biên lai `20.000.000đ` còn mở trên màn hình máy tính, nhưng điện thoại trên tay Hùng vừa nhảy **trang ẩn danh hoàn toàn mới** đăng ảnh **khu nhập hàng sáng nay** kèm tin đòi `60.000.000đ` *(counter nhảy `20.000.000đ → 60.000.000đ`)*. *(Bong bóng trung tính: "ĐÃ CHUYỂN: 20.000.000đ · YÊU CẦU MỚI: 60.000.000đ" · `BỐN NGÀY SAU`)*
- `l02_hung` **HÙNG**: Mới chuyển hai chục triệu bốn bữa trước cho êm… sao tụi nó lại có hình mới chụp ngay trong quán hồi sáng?!

---

### HỒI 1 – HỢP ĐỒNG BA TRĂM KHÁCH & BÀI ĐĂNG MỚI LÊN MƯỜI TÁM PHÚT

**`s02_restaurant_vip_booking` · `c02` (Lv B · 2.5D `pan_right` + `breathing` + `head_micro_tilt` + Living-Char `Lan/Minh/Hùng` + `ambient_particles`)** – Bốn tối trước (`19:30`), sảnh nhà hàng đèn vàng ấm, khăn bàn trắng, khách đông nhộn nhịp. Trong văn phòng có vách kính nhìn ra sảnh, Hùng và Minh xem hợp đồng; **Lan** gõ cửa bước vào đặt **cuốn sổ lịch phòng VIP** lên bàn.
- `l03_lan` **LAN**: Anh Hùng ơi, bên công ty chị Trang mới xác nhận mười giờ sáng mai tới ký hợp đồng tiệc ba trăm khách đó anh.
- `l04_minh` **MINH**: Trúng đơn này là dư sức bù tiền sửa sảnh luôn anh. Hồi nãy em dặn bếp kiểm tra kỹ hết rồi.
- `l05_hung` **HÙNG**: Ừ, giữ lịch phòng kín giúp anh nha Lan. Xong đơn mai là nguyên quý này quán mình nhẹ hẳn.

**`s03_lan_brings_post` · `c03` (Lv C · `pan_left` + Living-Char `Lan/Hùng` + `screen_glow` + `focus_highlight`)** – Hai tiếng sau (`21:48`), quán đã vãn khách. Lan gõ cửa quay lại văn phòng với vẻ lo lắng tự nhiên, đưa điện thoại cho Hùng xem bài đăng ẩn danh **mới lên đúng 18 phút**, chưa ghi tên, mới vài lượt xem, kèm **ảnh góc khuất kho bếp lúc đang dọn cuối ca** và 2 bình luận mồi úp mở tên đường. *(Bong bóng trung tính: "BÀI ĐĂNG ẨN DANH · 18 PHÚT TRƯỚC · Chưa ghi tên quán" · `MỒI NHỬ ĐẦU TIÊN`)*
- `l06_lan` **LAN**: Anh Hùng coi cái này giùm em. Bài mới đăng chưa ghi tên, nhưng nhìn góc bếp là nhận ra quán mình liền.
- `l07_lan` **LAN**: Em sợ sáng mai bên chị Trang họ lướt trúng mấy bài kiểu này thì phiền hợp đồng lắm anh.
- `l08_hung` **HÙNG**: Cảm ơn em báo sớm. Để anh với Minh coi lại.

**`s04_office_debate` · `c04` (Lv C · `slow_pull_out` + Living-Char `Minh/Hùng` + `detail_layer` zoom góc kho bếp)** – Lan khép cửa ra quầy lễ tân. Minh cầm điện thoại phóng to tấm ảnh tỏ ra nhẹ nhõm; Hùng nhìn kỹ góc khuất trong khung hình.
- `l09_minh` **MINH**: Bài này mới đăng chưa tới hai chục phút, có mấy lượt coi à anh. Có ghi tên mình đâu mà lo?
- `l10_hung` **HÙNG**: Không đơn giản đâu Minh. Góc kho bếp này khách ngồi ngoài sảnh đâu có đi vô chụp được.

---

### HỒI 2 – "DỊCH VỤ XỬ LÝ TRUYỀN THÔNG" & ÁP LỰC SÁT GIỜ KÝ

**`s05_admin_proactive_call` · `c05_l` + `c05_r` (Lv C · `split_screen` dọc Trái `Admin` – Phải `Hùng` + `whip_pan_left` + `phone_waveform` + Living-Char `Hùng`)** – `21:55`: Hộp thư nhà hàng bật tin nhắn tự xưng *"Hỗ trợ xử lý truyền thông"*, nối ngay bằng cuộc gọi ẩn số. Bên trái là bóng lưng giấu mặt của **Admin** trong căn phòng tối ánh xanh lạnh; bên phải là **Hùng** ngồi căng thẳng trong văn phòng.
- `l11_admin_p` **ADMIN** *(điện thoại)*: Chào anh Hùng, bên em chuyên hỗ trợ gỡ bài xấu cho nhà hàng. Bài bếp quán anh sắp bị đẩy lên các nhóm lớn đó.
- `l12_hung` **HÙNG**: Hình đó chỉ là lúc bếp đang dọn cuối ca. Quán tôi làm ăn đàng hoàng, mấy anh dựa vô đâu mà đòi gỡ?
- `l13_admin_p` **ADMIN** *(điện thoại)*: Khách trên mạng đâu chờ anh giải thích. Mai quán ký tiệc ba trăm khách bên chị Trang, bỏ hai chục triệu tối nay cho êm.

**`s06_partner_call_pressure` · `c06_l` + `c06_r` (Lv C · `split_screen` dọc Trái `Chị Trang` – Phải `Hùng` + `luma_wipe` + `phone_waveform` + Living-Char `Chị Trang` & `Hùng`)** – Vừa ngắt máy, điện thoại Hùng lại reo ngay — cuộc gọi từ **Chị Trang (Đối tác)** vì có tài khoản lạ vừa gửi đường link bài đăng tới hộp thư công ty chị. *(Bong bóng trung tính: "CUỘC GỌI ĐẾN · CHỊ TRANG (ĐỐI TÁC)" · `ÁP LỰC THẬT`)*
- `l14_trang_p` **CHỊ TRANG** *(điện thoại)*: Anh Hùng ơi, có nick lạ gửi link nói chuyện bếp quán mình. Chuyện sao vậy anh, mai chắc bên em cân nhắc lại.
- `l15_hung` **HÙNG**: Dạ hiểu lầm hình dọn bếp cuối ca thôi chị Trang. Sáng mai chị cứ qua coi trực tiếp trước khi ký nha.

**`s07_first_payment` · `c07 → c07_gone` (Lv C · `static_hold` + Living-Char `Hùng/Minh` + `cursor_click` + `detail_reveal` + `light_shift`)** – Nửa đêm trong văn phòng ánh đèn vàng hắt lên bản hợp đồng 300 khách và màn hình tin nhắn thúc giục. Minh lắc đầu can; Hùng bấm chuyển **`20.000.000đ`** *(thông báo trừ tiền trung tính, không hiện số tài khoản thật)*. Mười lăm phút sau, màn hình đổi sang `"Nội dung không còn tồn tại"`. *(Bong bóng trung tính: "CHUYỂN KHOẢN: -20.000.000đ · 15 PHÚT SAU: Bài viết đã biến mất" · `NHƯỢNG BỘ LẦN ĐẦU`)*
- `l16_minh` **MINH**: Họ cố tình gửi link cho chị Trang để ép mình đó anh! Trả hai chục triệu rồi tụi nó có dừng thiệt không?
- `l17_hung` **HÙNG**: Mất hợp đồng mai là đi luôn mấy trăm triệu với uy tín cả quán. Thôi, bỏ hai chục triệu cho qua chuyện tối nay đã.
- `l18_minh` **MINH**: Bài biến mất thiệt rồi anh… coi như xong rồi ha?
- `l19_hung` **HÙNG**: Anh cũng mong vậy.

---

### HỒI 3 – TRANG MỚI, ẢNH MỚI & CÁI GIÁ GẤP BA

**`s08_second_wave_new_page` · `c08` (Lv B · 2.5D `drift_push` + `breathing` + `head_micro_tilt` + Living-Char `Hùng/Minh` + `animated_counter` + `phone_waveform` + `chromatic_pulse`)** – Bốn ngày sau, buổi trưa nhà hàng đông khách, hợp đồng 300 khách đã ký xong. Điện thoại rung dồn: **trang ẩn danh mới** đăng **ảnh khu nhập hàng phía sau quán sáng sớm nay** kèm bình luận mồi *"Nghe nói bữa trước quán này chi tiền bịt miệng rồi!"*; cuộc gọi quen thuộc từ **Admin** lại vang lên *(counter nhảy `20.000.000đ → 60.000.000đ`)*. *(Bong bóng trung tính: "TRANG ẨN DANH MỚI · ẢNH KHU NHẬP HÀNG SÁNG NAY · ĐÒI: 60.000.000đ" · `VÒNG XOÁY NÂNG GIÁ`)*
- `l20_admin_p` **ADMIN** *(điện thoại)*: Anh Hùng, bên khác lại có hình mới rồi. Đợt này căng hơn, gói dọn sạch tháng này là sáu chục triệu nha anh.
- `l21_minh` **MINH**: Trời đất ơi! Bốn bữa trước mới đưa hai chục, giờ tụi nó mọc trang mới đòi vọt lên sáu chục triệu luôn?!
- `l22_hung` **HÙNG**: Lần trước anh tưởng bỏ tiền là mua sự yên ổn. Hóa ra mình tự gắn bảng biết sợ lên trán cho tụi nó vắt tiếp.

---

### HỒI 4 – BA MẢNH GHÉP, LẬP VI BẰNG & NƯỚC CỜ CHÍN GIỜ NĂM MƯƠI

**`s09_timeline_deduction` · `c09` (Lv C · `zoom_punch` + `slow_push_in` + `red_circle_draw` + `highlighter_sweep` + Living-Char `Hùng/Minh` + `color_mood: noir_evidence`)** – `14:15` cùng chiều trong văn phòng yên tĩnh. Hùng mở máy tính đặt cạnh nhau 3 mảnh chứng cứ: ảnh kho bếp `21:30` & ảnh khu nhập hàng sáng nay; mốc bài đầu mới lên `18 phút` (`highlighter_sweep`); dòng tin nhắc trúng *"tiệc ba trăm khách bên chị Trang"* (`red_circle_draw` + foley `marker_draw`).
- `l23_hung` **HÙNG**: Minh coi kỹ ba dòng này đi. Tiệc ba trăm khách bên chị Trang… trong quán này chỉ có đúng ba người biết lịch ký.
- `l24_minh` **MINH**: Ý anh là… hình góc bếp, giờ ký hợp đồng, tới bài mới đăng mười tám phút… có người trong quán tuồn ra ngoài?!
- `l25_hung` **HÙNG**: Đừng làm lớn chuyện, cũng đừng tự đối chất. Gom hết đường link gốc, tin nhắn với sao kê hai chục triệu đi theo anh liền.

**`s10_notary_and_police` · `c10 → c10_police` (Lv C · `pan_right` + `detail_reveal` dấu đỏ `VI BẰNG` + `ambient_particles` + `light_sweep`)** – Nắng chiều (`16:30`): Hùng và Minh bước ra khỏi văn phòng **Thừa phát lại** cầm tập hồ sơ đóng dấu đỏ **`VI BẰNG`** *(ghi nhận nguyên hiện trạng hai bài đăng, ID trang và tin nhắn)*, rồi nối tiếp bước ra khỏi cổng **cơ quan công an** với biên nhận tiếp nhận tin báo. *(Bong bóng trung tính: "16:30 · ĐÃ LẬP VI BẰNG HIỆN TRẠNG & NỘP ĐƠN TRÌNH BÁO" · `CHỐT CHỨNG CỨ HỢP PHÁP`)*
- `l26_hung` **HÙNG**: Lập vi bằng xong rồi, nộp hồ sơ trình báo cũng xong rồi. Tụi nó có xóa bài cũng hết đường chối.

**`s11_intentional_bait_lan` · `c11` (Lv C · `static_hold` + Living-Char 2.5 `Lan` `eye_gaze` + `eye_blink`/`mouth_sync` `Hùng/Minh/Lan` + `light_shift`)** – `21:50` tối cùng ngày trong văn phòng, cửa kính khép hờ. Thấy bóng **Lan** đi từ hành lang tới ôm sổ chốt bàn, Hùng khẽ ra hiệu Minh, hạ nhẹ màn hình rồi nói đủ rõ ngay lúc Lan gõ cửa bước vào đặt sổ. Ánh mắt Lan khựng đúng nửa giây (`eye_gaze` + `low_accent`) rồi cười lễ phép lui ra.
- `l27_hung` **HÙNG**: Minh ơi, anh không chuyển nữa. Giữ nguyên đường link đi, sáng mai mình ra lập vi bằng rồi báo công an.
- `l28_lan` **LAN**: Dạ… em gửi sổ chốt bàn tối nay nha anh. Em xin phép ra quầy trước ạ.
- `l29_minh` **MINH**: Ủa anh… hồi chiều mình lập vi bằng với trình báo công an xong hết rồi mà, sao anh nói sáng mai mới đi?
- `l30_hung` **HÙNG**: Để coi tối nay… hai cái bài đăng kia có tự biến mất không.

---

### HỒI 5 – BÀI XÓA LÚC NỬA ĐÊM & THẺ NHỚ KỸ *(DƯỚI 8 GIÂY)*

**`s12_next_morning_vanished` · `c12 → c12_file` (Lv C · `slow_pull_out` + `detail_reveal` + Living-Char `Minh/Hùng` + `color_mood: warm_daily`)** – Sáng hôm sau, nắng ấm chiếu vào văn phòng. Minh đưa màn hình điện thoại cho Hùng xem: cả hai bài đăng lẫn hai trang ẩn danh đều đã biến mất từ tối qua. Hùng đặt bàn tay lên tập hồ sơ **`VI BẰNG & BIÊN NHẬN TRÌNH BÁO`** đã lập từ chiều hôm trước.
- `l31_minh` **MINH**: Y như anh đoán luôn anh Hùng! Hơn mười giờ đêm qua tụi nó xóa sạch hai bài, khóa luôn cả hai trang rồi!
- `l32_hung` **HÙNG**: Bài đăng thì xóa được, chứ vi bằng lập hồi chiều sao xóa. Còn ai báo tin nửa đêm… để công an làm rõ.

**`s13_red_flags` · `c12` (Lv A · `static_hold`, không rung, làm tối nền 60%)** – Hiện thẻ **`NHỚ KỸ`** (`4 dấu hiệu + 1 việc nên làm ngay`) + đúng 1 câu của `Người Bóc Trần` (`24 từ`, `< 8 giây`):
- `l33_narr` **NGƯỜI BÓC TRẦN**: Bị bôi nhọ vòi tiền gỡ bài: càng trả càng bị nâng giá. Giữ chứng cứ, lập vi bằng rồi báo công an ngay!

---

### KẾT MỞ SAU THẺ NHỚ KỸ (CODA – ĐỘC LẬP 100%)

**`s14_coda_front_desk` · `c14` (Lv B · 2.5D `pan_left` + `rack_focus` Lan ↔ mặt kính phản chiếu Hùng + `head_micro_tilt` + `Hùng` `eye_gaze` + Living-Char `Hùng/Lan`)** – Sảnh nhà hàng buổi sáng. Lan đứng sau quầy lễ tân cười tươi đón khách, đinh ninh mọi dấu vết đã xóa kịp đêm qua. Hùng đi ngang qua quầy, dừng lại một nhịp bình thản; đến lúc anh bước đi, hình phản chiếu qua mặt kính quầy lễ tân cho thấy ánh mắt anh lạnh đi đúng một nhịp (`eye_gaze`).
- `l34_hung` **HÙNG**: Lan này. Cảm ơn em hôm trước báo anh sớm vụ bài đăng nha.
- `l35_lan` **LAN**: Dạ có gì đâu anh, em chỉ lo ảnh hưởng tới nhà hàng mình thôi ạ.

**`s15_coda_dark_room_reveal` · `c15 → c15_stamp` (Lv C · `film_burn` + `slow_push_in` + `typing_indicator` + `chat_bubbles` + `phone_waveform` `Admin` + `detail_reveal` dấu đỏ `16:30` + `chromatic_pulse` + `shakes` 1 mốc)** – Cắt nhanh về chiếc điện thoại trên bàn trong căn phòng tối *(nhãn mốc giờ: `22:14 ĐÊM QUA`)*, cuộc trò chuyện trung tính với **`LAN – LỄ TÂN`**:
- *(Bong bóng cũ, kèm ảnh góc kho bếp):* `"Mai 10h ký tiệc 300 khách bên chị Trang. Chủ quán đang rất lo."`
- *(Bong bóng gửi lúc `22:14` sau nhịp `typing_indicator`):* `"Ổng không chuyển sáu chục đâu. Sáng mai đi lập vi bằng báo công an. Xóa sạch bài với khóa trang liền đi."`
- *(Bong bóng trả lời lúc `22:15` khớp giọng trầm lạnh của `Admin` + `phone_waveform`):*
- `l36_admin_p` **ADMIN** *(giọng lạnh gọn)*: Rõ. Đã xóa sạch hai trang. Tạm ngưng chỗ này, yên tâm không lộ đâu.
- **CHUYỂN CẮT DỨT KHOÁT (`detail_reveal` + `chromatic_pulse` + `shakes`):** Màn hình điện thoại tắt phụt → Cắt thẳng sang cận cảnh dấu đỏ trên tập hồ sơ trong văn phòng Hùng: **`VI BẰNG & TIẾP NHẬN TIN BÁO · 16:30 HÔM QUA`** *(tiếng khép tập hồ sơ + **`impact` TRẦM → CẮT ĐEN ĐỘT NGỘT!**)*.

**`s16_black_cut` · `c16` (Lv A · `static_hold`)** – Cắt đen `1.2 giây`.

**`s17_disclaimer` · `c12` (Lv A · `static_hold`)** – Bảng **LƯU Ý** (`3.5 giây`): *"Tình huống được dựng lại để cảnh báo. Nhân vật, tên, số liệu đều là hư cấu."*

---

## 4. Thẻ DẤU HIỆU NHẬN BIẾT (`red_flags` — 4 ý + 1 hành động gốc)

1. **Bài bôi nhọ ẩn danh cài chi tiết nội bộ:** Dùng ảnh góc khuất hoặc lịch làm việc thật để tạo cảm giác *"họ nắm thóp mình"* và gây áp lực sát giờ quan trọng.
2. **Đội lốt "dịch vụ xử lý truyền thông" chào gỡ bài:** Nói chuyện lịch sự như làm dịch vụ, đưa mức phí đầu vừa tầm để dụ chủ quán tặc lưỡi xuống tiền.
3. **Trả lần đầu sẽ mở cửa cho lần hai nâng giá:** Chuyển tiền một lần là xác nhận bạn dễ sợ — chúng sẽ lập trang mới, dùng ảnh mới để đòi mức tiền gấp nhiều lần.
4. **Rò rỉ thông tin từ chính bên trong:** Khi người ngoài biết rõ lịch ký hợp đồng hay có ảnh khu vực hạn chế, cần rà soát lỗ hổng nội bộ thay vì chỉ đề phòng bên ngoài.
- **Việc nên làm ngay:** Không tự nhắn tin nhận vơ và tuyệt đối không chuyển tiền gỡ bài; lưu nguyên đường dẫn, ID trang, tin nhắn, sao kê — lập vi bằng giữ hiện trạng rồi trình báo cơ quan công an!

---

## 5. Tự kiểm “Không dạy lừa” & Pháp lý (`HRN-LEGAL-SCAM-V1`)

- [x] Không định danh cá nhân, nhà hàng, đối tác, nền tảng hay ngân hàng thật (`L1`).
- [x] Không có câu thoại hay chi tiết đủ để người xem sao chép vận hành trang bôi nhọ, chạy bình luận mồi hay mua chuộc nội bộ (`L2`).
- [x] Không mô phỏng giao diện ứng dụng thật, logo thật, số tài khoản thật hay phù hiệu cơ quan thật (`L3`).
- [x] Nghiệp vụ **lập vi bằng** trình bày đúng bản chất pháp lý: Thừa phát lại ghi nhận hiện trạng bài đăng/tin nhắn trên thiết bị làm nguồn chứng cứ trước khi đối phương xóa dấu vết, nộp kèm hồ sơ trình báo cơ quan công an; không nêu số điều luật chưa kiểm chứng (`L7`, `L8`).
- [x] Nhân vật chính xử lý hoàn toàn đúng luật: không tự đối chất, không tự ý công khai thông tin cá nhân hay giữ người trái pháp luật.
- [x] Đã rà soát sạch 100% `identity_hard_block`, `identity_soft_warn`, `asr_ocr_hard_block` và `asr_ocr_soft_warn` theo [policy_wordlists.json](../../../../00_HARNESS_GUIDELINES/policy_wordlists.json).
