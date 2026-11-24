# HARNESS CHUYỂN ĐỘNG HÌNH ẢNH — VISUAL MOTION UPGRADE (LEVEL 3 + LIVING-CHARACTER 2.5)
*Mã: HRN-MOTION-L3.0 · Nâng cấp nền tảng từ HRN-MOTION-L2.1 (24/11/2026) · Áp dụng cho mọi tập mới của cả `factory196` (16:9) và `factory619` (9:16)*

> [!IMPORTANT]
> **DEFAULT RULE:** Mỗi video Vạn Chuyện / Bóc Trần Lừa Đảo **bắt buộc có Visual Motion Planning trước khi render** (`beat_type` + `motion_level` cho từng cảnh), kết hợp **Living-Character Micro-Motion chọn lọc** (`eye_blink` · `mouth_sync` 3–4 trạng thái khớp `.wav` thật · `breathing` · `eye_gaze` / `expr_swap` · `head_micro_tilt`) cùng các hiệu ứng đạo diễn & không khí **Level 3** (chia đôi cuộc gọi `split_screen`, `phone_waveform`, `rack_focus`, đồ họa vật chứng `red_circle_draw` / `highlighter_sweep` / `animated_counter` / `typing_indicator`, môi trường `rain_layer` / `ambient_particles` / `light_sweep` / `color_mood` / `chromatic_pulse`, chuyển cảnh `whip_pan` / `zoom_punch` / `luma_wipe` / `film_burn`).
>
> **Nguyên tắc không hồi tố & tương thích ngược 100%:** Không bắt buộc sửa hồi tố tập cũ chưa chạm tới. Engine `03_ENGINE` giữ tương thích ngược hoàn toàn với cả tập Legacy, `"motion_upgrade": "level2"`, và `"motion_upgrade": "level3"`, đồng thời mọi tập cũ đều tự hưởng tăng tốc OpenCV + render đa nhân mới.

---

## 0. LUẬT KẾ THỪA CỘNG DỒN & TIẾN TRÌNH CHECK 1 → 2 → 3 BẮT BUỘC
*Áp dụng cứng cho **MỌI TÌNH HUỐNG: LÀM MỚI · CHỈNH SỬA · UPDATE/NÂNG CẤP TẬP CŨ** — được khóa tự động bằng code tại `motion-check`, `gate0`, `gate4` và `gate5` (`03_ENGINE/motion_fx.py`, `gate4_timeline.py`, `gate5_render_audit.py`).*

> [!CAUTION]
> **LUẬT THÉP (`Level 3 ⊃ Level 2 ⊃ Level 1`):**
> - **TUYỆT ĐỐI CẤM NHẢY CÓC:** Muốn gắn `"motion_upgrade": "level3"` thì **BẮT BUỘC phải đạt 100% CHECK 1 (Level 1) VÀ 100% CHECK 2 (Level 2 — gồm 2.5D Parallax + Breathing + Chớp mắt `eye_blink` + Chép miệng `mouth_sync` khớp `.wav` thật)** trước khi áp hiệu ứng Level 3.
> - **CẤM ĐÁNH ĐỔI / LÀM MẤT TÍNH NĂNG CŨ:** Không bao giờ được bỏ chép miệng, chớp mắt, 2.5D, thoại, foley, chat bubble hay safe zone để chỉ dán hiệu ứng mới lên ảnh tĩnh phẳng.
> - **CẤM LỜ ĐI KHI THIẾU TÀI NGUYÊN / LỖI API (VD: 503):** Nếu công cụ sinh ảnh gặp lỗi hoặc hết hạn mức khiến chưa tạo được bộ `eye_blink` / `mouth_sync` / `2.5D`, **PHẢI DỪNG LẠI BÁO CHỦ KÊNH NGAY** — tuyệt đối không được tự ý bỏ trống rồi render tiếp, và **CẤM tự ý ghi `motion_waivers`** khi chưa được chủ kênh đồng ý.

### Tiến trình Check 1 → 2 → 3 bắt buộc trước mọi lần render Staging

| Giai đoạn | Phạm vi kiểm tra bắt buộc | Ngưỡng khóa cứng trong Engine | Điểm chặn tự động |
| :--- | :--- | :--- | :--- |
| **CHECK 1**<br>*(Nền Level 1)* | • Thời lượng hợp lệ, cảnh phủ kín `0 → duration` không hở/chồng<br>• Đủ `hook`, `chapters` (16:9), `dialogue` đúng `cast.json` & trần từ, `red_flags`, `disclaimer`, `clearance: ĐẠT`<br>• Giữ nguyên 100% dữ liệu Level 1 khi **sửa/update** (`dialogue`, `chat_bubbles`, `ambience`, `bgm`, `foley`, `shakes`)<br>• **Nguồn sự thật duy nhất:** nếu tập có `source/build_draft.py`, mọi thay đổi phải được cập nhật vào `build_draft.py` (không chỉ sửa chắp vá `episode.json`)<br>• Safe Zone, Boxless Subtitles, không `asetrate`/`atempo`, sạch từ cấm ASR/OCR | 0 lỗi `gate0` phần đầu vào + 0 lỗi Gate 5 điểm `1, 3, 6, 7, 8`; cảnh báo `[SYNC]` nếu `episode.json` mới hơn `source/build_draft.py` | `gate0`, `gate5` |
| **CHECK 2**<br>*(Kế thừa Level 2 — Bắt buộc cho cả `level2` & `level3`)* | • **2A. Visual Beat & Nhịp:** 100% cảnh có `beat_type` + `motion_level` (`A/B/C/D`), không chuỗi lặp `≥ 3` `push_in`, không lạm dụng `shakes`<br>• **2B. Chiều sâu 2.5D (`Level B`) + Nhịp thở (`breathing`):** lớp `bg/fg` tách sạch + `breathe_y`/`breathe_scale`<br>• **2C. Living-Character khóa pixel (`face_roi_prep.py`):** chớp mắt (`eye_blink`) + **chép miệng khớp `.wav` thật (`mouth_sync`)** (đếm cả trên cảnh thường, layer `fg` 2.5D và trong `split_screen.panels`)<br>• **2D. Detail Motion nền & Motion↔SFX Sync:** `screen_glow`/`light_shift`/`detail_reveal`/`focus_highlight` khớp foley | • **Phim dài 16:9 (`factory196`):** `2.5D ≥ 1` *(khuyến nghị 2–4)* · `Breathing ≥ 1` · **`eye_blink ≥ 3`** · **`mouth_sync ≥ 3`**<br>• **Short 9:16 (`factory619`):** `2.5D ≥ 1` *(khuyến nghị 1–2)* · `Breathing ≥ 1` · **`eye_blink ≥ 2`** · **`mouth_sync ≥ 2`** | **CHẶN CỨNG** tại `motion-check`, `gate0`, `gate4`, `gate5` (điểm 4 = `FAIL`) |
| **CHECK 3**<br>*(Nâng cấp Level 3 — Chỉ mở khi CHECK 1 & 2 đều PASS)* | • **3A. Thực chất Level 3:** có ít nhất 1 hiệu ứng/kỹ thuật Level 3 (`split_screen`, `phone_waveform`, `red_circle_draw`, `highlighter_sweep`, `animated_counter`, `typing_indicator`, `rain_layer`, `ambient_particles`, `light_sweep`, `color_mood`, `chromatic_pulse`, `rack_focus`, `head_micro_tilt`, `eye_gaze`/`expr_swap`, 4-state `round_image`, chuyển cảnh L3)<br>• **3B. An toàn phần cứng (`dual16gb_cpu_l480`) & căn ROI:** ≤ 4 lớp 2.5D, blur ≤ 8.0px, `head_tilt_deg ≤ 2.2°`, 0 hiệu ứng cấm cục bộ; panel `split_screen` dùng `crop_x`/`crop_y` tự đồng bộ ROI (`region_space: "source"` nếu dùng tọa độ ảnh gốc)<br>• **3C. Chống Stale Signoff (khi Sửa/Update):** chữ ký duyệt `clearance/human_qa_signoff.json` cũ tự động mất hiệu lực ngay khi `episode.json` đổi `version`/`sha256` hoặc Gate 4 render lại → bắt buộc chủ kênh xem duyệt bản Staging mới trước Gate 6 | • Nếu CHECK 2 = `FAIL` → CHECK 3 tự động **`BLOCKED`**<br>• `L3_total ≥ 1`<br>• Chữ ký duyệt cũ bị tự động chuyển về `⏳ CHỜ NGƯỜI DUYỆT` | **CHẶN CỨNG** tại `motion-check`, `gate0`, `gate4`, `gate5` |

### Quy trình bắt buộc theo từng loại công việc (Làm mới · Sửa · Update)
1. **Khi LÀM MỚI tập (`run.py new <EP>`):** Thiết kế `episode.json` theo `"motion_upgrade": "level3"` ngay từ đầu → Gate 1 chuẩn bị đủ ảnh nền + 2.5D (`bg/fg`) + bộ Living-Character (`blink` + `mouth_closed/mid/open[/round]` qua `face_roi_prep.py` + duyệt bảng Face QC) → chạy `motion-check` & `gate0` (**phải PASS đủ CHECK 1 → 2 → 3**) → Gate 2 → 3 → 4 → 5 (dừng Staging).
2. **Khi CHỈNH SỬA tập đã có:** Sửa trực tiếp trong `source/build_draft.py` (nếu có) rồi biên dịch lại `episode.json` → đối chiếu số lượng `2.5D`, `eye_blink`, `mouth_sync`, `L3_FX` trước & sau sửa không bị sụt giảm → chạy lại `motion-check` & `gate0` → render lại Gate 4 → Gate 5 (**chữ ký cũ tự hết hạn, phải duyệt lại Staging**).
3. **Khi UPDATE / NÂNG CẤP tập cũ (Legacy v1–v3 → Level 3):** Tuyệt đối KHÔNG nhảy thẳng lên Level 3. Phải sao lưu `episode.json` gốc → thực hiện đủ **tầng Level 2 trước** (tách 2.5D + tạo bộ `eye_blink` & `mouth_sync` qua `face_roi_prep.py` + duyệt Face QC) → giữ nguyên toàn bộ dữ liệu Level 1 (đặc biệt KHÔNG re-synth Gate 2 TTS nếu thoại không đổi) → mới áp thêm lớp Level 3 → đồng bộ vào `source/build_draft.py` → vượt đủ **CHECK 1 → 2 → 3** ở `gate0`/`gate4`/`gate5` → dừng Staging chờ duyệt lại.
4. **Cơ chế ngoại lệ duy nhất (`motion_waivers`):** Chỉ dùng khi **kịch bản thực sự không có cảnh lộ mặt hoặc ảnh đặc thù không thể tách 2.5D** VÀ **đã được chủ kênh đồng ý**. Khai báo tường minh `"motion_waivers": {"mouth_sync": "Lý do cụ thể >= 12 ký tự"}` trong `episode.json`; mọi waiver đều bị in nổi bật `⚠️ WAIVER` ở `motion-check`, `gate0` và `GATE5_QA_REPORT.md` để không bao giờ che giấu được.

---

## I. MỤC TIÊU & NGUYÊN TẮC BẮT BUỘC

### Mục tiêu
Nâng cấp video từ cảm giác "slideshow có zoom/pan" lên **cảm giác không gian, chiều sâu và diễn biến trực quan**:
- Hình ảnh có cảm giác đang diễn ra, không còn quá tĩnh.
- Chuyển động phục vụ câu chuyện, không phải hiệu ứng trang trí.
- Tạo chiều sâu không gian, cinematic camera movement và motion có chủ đích.
- Tạo điểm nhấn trực quan ở các chi tiết quan trọng: điện thoại, tin nhắn, ánh mắt, bàn tay, vật chứng.
- Giữ ổn định thời gian render, chi phí AI và độ tin cậy của workflow 6 Gate.

### Nguyên tắc bắt buộc (CẤM VI PHẠM)
1. **Không loại bỏ** workflow ảnh tĩnh hiện tại (ảnh tĩnh + Ken Burns vẫn là xương sống).
2. **Không biến toàn bộ video thành AI video.**
3. **Không animate tất cả ảnh giống nhau.**
4. **Không sử dụng rung (`shake`/`wobble`), zoom, pan một cách máy móc trên mọi cảnh.**
5. **Không dùng chuyển động quá mạnh, nhanh, chóng mặt hoặc không liên quan nội dung.**
6. **Không tạo chuyển động làm thay đổi ý nghĩa hình ảnh**, biểu cảm nhân vật, đạo cụ, nội dung điện thoại, văn bản, số tiền, tên, trang phục hoặc continuity.
7. **Mọi chuyển động phải có lý do:** kể chuyện, nhấn cảm xúc, tiết lộ thông tin, tạo suspense hoặc dẫn mắt người xem.

---

## II. PHÂN CẤP 4 LEVEL XỬ LÝ HÌNH ẢNH (`motion_level`)

Mỗi cảnh trong `episode.json` bắt buộc được phân loại trước khi dựng:

### LEVEL A — STATIC CINEMATIC MOTION (`"motion_level": "A"`)
Áp dụng cho **phần lớn cảnh kể chuyện thông thường**.
- Sử dụng: Ken Burns có kiểm soát (`slow_push_in`, `slow_pull_out`, `pan_left`, `pan_right`, `drift_up`, `drift_down`, `subtle_push_left`, `subtle_push_right`) và **`static_hold`** (giữ khung tĩnh có chủ đích ở khoảnh khắc im lặng/căng thẳng/kết).
- **Không dùng rung hình tùy tiện** (`wobble: "none"` mặc định cho Level A; chỉ bật `handheld`/`tense` ở cảnh nghi vấn/cao trào có lý do rõ ràng).

### LEVEL B — DEPTH MOTION / 2.5D PARALLAX + RACK FOCUS (`"motion_level": "B"`)
Áp dụng cho **~2–5 cảnh nổi bật có chiều sâu không gian** mỗi video khi nguồn hình phù hợp *(không bắt buộc đủ số lượng nếu ảnh không phù hợp)*.
- Tách cảnh thành **2–4 lớp**: **Background (`bg`)** · **Mid (`mid` tùy chọn)** · **Main subject (`subject` RGBA)** · **Foreground (`fg` RGBA tùy chọn)**.
- Tạo chuyển động camera chậm (`push_in`, `pull_out`, `pan_left`, `pan_right`, `drift_push`) để các lớp dịch chuyển theo tốc độ `depth` khác nhau.
- **Rack Focus (Dynamic DoF — mới ở Level 3):** Thay vì blur tĩnh, có thể khai báo `blur_from` / `blur_to` (`<= 8.0px`), `blur_at`, `blur_dur` ngay trên từng layer để chuyển nét mượt từ tiền cảnh ↔ hậu cảnh (chỉ tính blur 1 lần lúc nạp cảnh rồi blend siêu nhẹ).
- **Head Micro-Tilt (Living-Character 2.5 — mới ở Level 3):** Trên lớp nhân vật (`fg`/`subject`), có thể bật `head_tilt_deg` (`<= ±2.2°`), `head_pivot` (`[0.5, 0.78]`), và tùy chọn `tilt_speaker` / `tilt_line_ids` để nhân vật nghiêng/gật cực nhẹ theo nhịp nhấn giọng `.wav` thật.
- **Cấm exaggerate depth**, cấm làm méo cơ thể, gương mặt hoặc vật thể.
- Nếu nguồn ảnh không đủ sạch để tách lớp không lỗi biên → **giữ Level A**, không cố ép 2.5D.

### LEVEL C — OBJECT / DETAIL MOTION + LIVING-CHARACTER 2.5 + LEVEL 3 FX (`"motion_level": "C"`)
Ưu tiên **animate chi tiết kể chuyện & tạo không khí có chủ đích** thay vì animate máy móc toàn khung:
- **Nhóm Đạo diễn & Bóc trần Vật chứng (Level 3 — Nhóm 1):**
  - **Chia đôi màn hình cuộc gọi (`split_screen`):** Cảnh 2 khung (`layout: "vertical"` mặc định cho 16:9, `"horizontal"` mặc định cho 9:16), mỗi bên chạy camera + `eye_blink` + `mouth_sync` độc lập, tự làm sáng viền & tối nhẹ bên im lặng theo người đang nói (`speaker`), kèm thanh sóng âm điện thoại sống động (`waveform: true`).
  - **Sóng âm thoại (`phone_waveform`):** Thanh equalizer tối giản chạy theo biên độ `.wav` thật (dùng cho cảnh thoại qua điện thoại `"af": "phone"` hoặc phần phân tích).
  - **Khoanh đỏ & Bút dạ quang vẽ động (`red_circle_draw`, `highlighter_sweep`):** Khoanh tròn / đóng khung / gạch chân đỏ vẽ nét theo thời gian hoặc quẹt dạ quang vàng trong suốt (giữ rõ chữ nền) trực tiếp lên chi tiết gian dối (số tiền, link lạ, đồng hồ đếm ngược); ghép kèm foley `marker_draw`.
  - **Số nhảy động (`animated_counter`):** Đếm ngược áp lực thời gian (`fmt: "mmss"`, VD `00:59 → 00:00`) hoặc biến động số dư (`fmt: "vnd"`, VD `0 → -18.000.000đ`); ghép kèm foley `counter_tick`.
  - **Đang nhập tin nhắn (`typing_indicator`):** Bong bóng `...` trung tính nhấp nhô 1–1.5s ngay trước khi `chat_bubbles` bật lên.
  - **Chuyển cảnh điện ảnh mới (`transition_in`):** `whip_pan_left`, `whip_pan_right`, `zoom_punch`, `luma_wipe`, `film_burn` (bên cạnh `cut`, `dissolve`, `flash_white`, `flash_red`, `fade_black`, `glitch`).
- **Nhóm Không khí, Ánh sáng & Màu phim (Level 3 — Nhóm 2):**
  - **Mưa 2 lớp siêu nhẹ (`rain_layer`, alias `rain`):** Cuộn 2 lớp hạt mưa nghiêng tiền–hậu cảnh mượt mà, rất hợp cảnh đêm/hậu quả (`aftermath`) khớp ambience `rain`.
  - **Hạt bụi ánh sáng / bokeh (`ambient_particles`):** 15–45 hạt mềm trôi chậm trong không gian (hội trường LED, phòng tối, nắng cửa sổ).
  - **Vệt sáng / bóng quét (`light_sweep`, alias `shadow_drift`):** Tia sáng đèn xe / ánh đèn quét ngang mềm (tính ở 1/4 res) cho cảnh đêm/nghi vấn.
  - **Tông màu điện ảnh (`color_mood`):** LUT nhanh + vignette + film grain mịn theo 5 mood sẵn: `warm_daily`, `cold_suspicion`, `high_tension`, `flashback`, `noir_evidence`.
  - **Cú sốc tách sắc (`chromatic_pulse`):** Tách nhẹ kênh R/B (`4–8px`) + zoom blur nhẹ trong `0.25–0.35s` khớp `impact` / `bank_ting` ở cảnh `climax`.
- **Nhóm chi tiết nền Level 2 (vẫn dùng đều):** `screen_glow`, `light_shift`, `detail_reveal`, `notifications`, `chat_bubbles`, `cursor_click`, `detail_layer`, `focus_highlight`.
- **Nhân vật sống động chọn lọc — Living-Character Level 2.5 (Tổ hợp A + B + C + 3.7):**
  - **A · Chớp mắt (`eye_blink`):** Swap vùng elip nhỏ quanh mắt (~40 KB), hỗ trợ `"layer": "fg"` khóa cứng trên cảnh 2.5D Level B.
  - **B · Miệng nói theo `.wav` thật (`mouth_sync`, 3 hoặc 4 trạng thái):** Đọc RMS + (tùy chọn) phổ tần số trực tiếp từ `audio/tts/<line_id>.wav`. Hỗ trợ **3 trạng thái** (`closed_image` · `mid_image` · `open_image`) hoặc **4 trạng thái nâng cấp** khi thêm **`round_image`** (tự tách âm tròn môi `O/Ô/U` theo spectral centroid `< 980 Hz`).
  - **C · Nhịp thở & Nghiêng đầu vi mô (`breathing` + `head_micro_tilt`):** Nhịp thở (`breathe_y`, `breathe_scale`) + nghiêng/gật đầu nhẹ (`head_tilt_deg <= 2.2°`, `tilt_speaker`) trên lớp `fg` 2.5D.
  - **D · Đảo ánh mắt & Đổi biểu cảm cục bộ (`eye_gaze`, `expr_swap`):** Swap ROI elip khóa pixel có mốc `at` / `dur` / `hold_dur` (hoặc mảng `events`) để nhân vật liếc xuống điện thoại, nhíu mày hoặc sững sờ ngay trong cùng 1 cảnh.
- **Quy tắc chọn lọc Living-Character & Chống lỗi cắt dán:**
  - **Chỉ áp dụng chọn lọc:** `2–4 cảnh` cận/trung cận rõ mặt cho Short 9:16 (`factory619`) và `3–6 cảnh` cận thoại đắt giá cho Phim dài 16:9 (`factory196`). **KHÔNG dùng `mouth_sync`** trên cảnh toàn, cảnh quay lưng, mặt nhỏ hoặc cảnh câm lặng.
  - **Quy trình tạo ảnh biến thể khóa pixel (`03_ENGINE/face_roi_prep.py`):** CẤM vẽ mắt/miệng bằng hình khối code và CẤM dùng AI lip-sync cục bộ (`Wav2Lip`/`LivePortrait`/`SadTalker`). Bắt buộc tạo ảnh biến thể từ chính ảnh cảnh đã duyệt → chạy `03_ENGINE/face_roi_prep.py` → **kiểm bảng QC cận mặt trước khi render**.
- Chuyển động phải **đúng timing** với voice-over, câu chuyện và sound effect.
- **Tuyệt đối không tự ý thay đổi nội dung văn bản, UI, số tiền, tên, thông tin hoặc bằng chứng đang hiển thị.**

### LEVEL D — AI IMAGE-TO-VIDEO MOTION (`"motion_level": "D"`, TÙY CHỌN – KHÔNG CHẠY CỤC BỘ)
Chỉ dùng cho **một số rất ít khoảnh khắc đặc biệt** khi chuyển động tự nhiên của người/vật thể thực sự làm tăng giá trị cảm xúc/kể chuyện *(không bắt buộc dùng ở mọi video; tuyệt đối **KHÔNG** chạy AI video / diffusion cục bộ trên máy ThinkPad L480)*.
- Ví dụ phù hợp: nhân vật quay đầu, ánh mắt chuyển hướng, nhân vật khựng lại, bàn tay ngập ngừng, phản ứng nhỏ khi nhận ra điều bất thường.
- Chỉ nạp clip `.mp4` ngắn (2–5 giây) đã sinh sẵn từ bên ngoài và kiểm duyệt sạch (`video_fit: "natural_hold"`).
- **CẤM dùng** nếu gây biến dạng mặt, tay, trang phục, bối cảnh, vật thể, lệch continuity hoặc tự bịa chi tiết không có trong kịch bản.
- **Cơ chế hạ cấp tức thì:** Luôn khai báo kèm `"image"` gốc; nếu clip lỗi hoặc máy cần tối ưu tài nguyên, đặt `"video_enabled": false` hoặc chạy `--safe-motion` để hạ cấp sạch về Level A.

---

## III. QUY TẮC PHÂN BỔ MOTION & VISUAL BEAT PLANNING (PRE-PRODUCTION)

Trước khi render (tại bước viết `SCRIPT.md` + `IMAGE_PROMPTS.md` và lập `episode.json`, trước `Gate 0`), **bắt buộc phân tích Visual Beat** dựa trên kịch bản và voice-over.

| Mã `beat_type` | Loại cảnh | Motion gợi ý |
| :--- | :--- | :--- |
| `establishing` | Thiết lập bối cảnh | Level A (`pan_right`, `pan_left`, `slow_pull_out`) hoặc Level B (2.5D mở không gian) |
| `normal` | Kể chuyện thông thường | Level A (`slow_push_in`, `pan_left`, `drift_up`, `static_hold`), `wobble: "none"` |
| `information` | Cung cấp thông tin / tin nhắn / vật chứng | Level C (`notifications`, `chat_bubbles`, `detail_reveal`, `cursor_click`, `focus_highlight`) |
| `suspicion` | Nghi vấn / bất an | Level A (`slow_push_in` chậm hoặc `static_hold`), Level B push-in (tối đa 2–3 lớp), hoặc Level C (`screen_glow`, `light_shift`) |
| `anomaly` | Phát hiện dấu hiệu bất thường | Level C (`focus_highlight`, `detail_reveal`, `screen_glow`) hoặc Level D (clip ngắn dựng ngoài, tùy chọn) |
| `climax` | Cao trào / cú chốt | Level A/B/C có kiểm soát, chỉ dùng `shakes` đúng 1–2 mốc khớp foley `impact` |
| `aftermath` | Hậu quả / lắng đọng | Level A (`slow_pull_out`, `static_hold`) hoặc Level C (`light_shift` dịu + `ambience: rain`) |
| `ending` | Cảnh kết / Thẻ dấu hiệu | Level A (`static_hold`, `wobble: "none"`), tuyệt đối không rung |

### Quy tắc nhịp thị giác (Anti-Repetition)
- **Tránh lặp cùng một pattern `push_in` (zoom-in) từ 3 cảnh liên tiếp trở lên.** Thay đổi nhịp bằng `slow_pull_out`, `pan_left`/`pan_right`, `static_hold`, Level B parallax và Level C detail motion có chủ đích.
- Không ép cảnh nào cũng phải có hiệu ứng mới. Chạy `python factory196/_engine/run.py motion-check <EP>` (hoặc `factory619`) để tự động kiểm tra chuỗi lặp trước khi render.

---

## IV. TIMING, CƯỜNG ĐỘ & SOUND DESIGN ĐI KÈM MOTION

### Timing & Cường độ
- Chuyển động camera chậm, mượt, không giật (`scale` biên độ nhỏ `1.02–1.12`, ưu tiên `smoothstep` / `ease_out`).
- Không zoom quá mức, không lạm dụng camera shake (cảnh báo nếu > 35% số cảnh có `shakes`).
- Giữ **`static_hold`** ở những giây cần im lặng hoặc căng thẳng để tạo tương phản thị giác.
- Chuyển động phải khớp nhịp voice-over; khi tiết lộ thông tin quan trọng, dùng chuyển động/cut có chủ đích thay vì hiệu ứng ngẫu nhiên.

### Sound Design đi kèm Motion (`03_ENGINE/sfx_library.py`)
Khi motion có tương tác vật lý hoặc sự kiện rõ ràng, ghép foley đúng mốc `at` (±0.15s) ở Gate 3:
- Điện thoại rung → `phone_vibrate` · Thông báo / tin nhắn → `notification`, `message_send`, `bank_ting`
- Click / chạm màn hình (`cursor_click`) → `click`
- Gõ phím điện thoại / máy tính → `typing`, `keyboard`
- Bật/tắt đèn (`light_shift`, `detail_reveal`) → `light_switch`
- Nhấn trầm tinh tế khi lộ chi tiết/nghi vấn → `low_accent` *(mức nhẹ −11.5 dBFS, không lấn voice-over)*
- Không gian / mưa (`rain`) → ambience `room_tone`, `night_room`, `office`, `street`, `rain`
- **Không thêm SFX chỉ để lấp khoảng trống.** Giữ gain hợp lý, tuyệt đối không lấn thoại.

---

## V. GIỮ CONTINUITY (NHẤT QUÁN XUYÊN SUỐT)

- Giữ nhất quán ngoại hình nhân vật, trang phục, đạo cụ, hướng nhìn và bố cục không gian giữa các cảnh (khớp [CAST_AND_VISUAL_STYLE.md](CAST_AND_VISUAL_STYLE.md) & [STORY_AND_PRODUCTION_HARNESS.md](STORY_AND_PRODUCTION_HARNESS.md)).
- Không đổi thiết kế điện thoại, không đổi nội dung chữ/số liệu đang hiển thị, không tạo hành động trái kịch bản.
- Không dùng motion khiến người xem hiểu nhầm diễn biến.
- Nếu ảnh nguồn không phù hợp để tách lớp (Level B) hoặc animate (Level C/D) → **hạ về Level A**.

---

## VI. RÀNG BUỘC AN TOÀN PHẦN CỨNG & NĂNG LỰC KỸ THUẬT (`03_ENGINE`)

> [!TIP]
> **HARDWARE SAFETY PROFILE (`dual16gb_cpu_l480`) — ThinkPad L480 · Intel i5-8250U (4C/8T) · 16GB Dual-Channel DDR4-2400 · Intel UHD 620 (đã nâng cấp 24/11/2026):**
> 1. **Đã mở khóa & kiểm chứng thực đo:** Tăng tốc xử lý khung bằng **`opencv-python-headless` (`cv2`)**, **render song song đa nhân (`--workers 4`, mặc định tự động `4` worker cho clip `>= 12s`)** kết hợp cơ chế nạp trượt (sliding-window lazy load: tổng RAM 4 worker + FFmpeg chỉ ~`370–550 MB / 16 GB`), tối đa **4 lớp 2.5D**, **Rack Focus blur `<= 8.0px`** (tính 1 lần lúc nạp cảnh), **`head_micro_tilt <= ±2.2°`**, **`split_screen`**, toàn bộ **Level 3 Nhóm 1 + Nhóm 2 + Living-Character 2.5**.
> 2. **Quy tắc Bộ mã hóa H.264 (`--encoder auto|x264|qsv`):**
>    - Chế độ đa nhân (`--workers 2..4`, mặc định `--encoder auto`): dùng **`libx264`** (`4 worker`: thực đo **47.0s / 450 frames full Level 3 1080p ~ 9.6 fps** — nhanh hơn gần **2×** bản đơn luồng cũ!).
>    - Chế độ đơn nhân (`--workers 1 --encoder qsv`): dùng **`h264_qsv`** (Intel Quick Sync, nhanh hơn `1w x264` ~18%, file gọn hơn ~23%). **KHÔNG chạy nhiều worker `h264_qsv` cùng lúc** (UHD 620 bị nghẽn phiên phần cứng khi >1 phiên song song — engine đã tự chặn).
> 3. **Vẫn CẤM dùng cục bộ (do không có GPU rời):** AI image-to-video / diffusion / AI lip-sync cục bộ (`Wav2Lip`, `LivePortrait`, `SadTalker`, `MuseTalk`), PyTorch nặng, Blender / 3D rendering thời gian thực.
> 4. **Fallback bắt buộc:** Mọi hiệu ứng nâng cao đều tùy chọn; hạ cấp tức thì về Level A bằng `"video_enabled": false` hoặc cờ `--safe-motion`.
> 5. **Lộ trình mở rộng sau này (Phase 2 — sẵn sàng khi cần):** Khi cần tách lớp 2.5D tự động hàng loạt, có thể bổ sung tool chuẩn bị asset ngoại tuyến bằng `onnxruntime` CPU + `isnet-anime` (~170MB) hoặc `Depth Anything V2 Small` (~100MB) — hoàn toàn tách khỏi vòng lặp render Gate 4.

### Kết quả Benchmark thực đo trên ThinkPad L480 (16GB Dual-Channel · 15s @ 1920×1080 30fps · 100% cảnh nhồi đầy Level 3 FX)
| Chế độ | Encoder | Workers | Thời gian | Tốc độ thực | Khung hình | Ghi chú |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| Đơn nhân CPU | `libx264` | 1 | 77.85s | 5.8 fps | 450/450 (`yuv420p`) | Baseline sau tối ưu `cv2` |
| Đơn nhân QSV | `h264_qsv` | 1 | 65.77s | 6.8 fps | 450/450 (`yuv420p`) | File nhẹ hơn (~22.7 MB), chỉ chạy 1 worker |
| Đa nhân 3w | `libx264` | 3 | 54.28s | 8.3 fps | 450/450 (`yuv420p`) | Ổn định, tổng RAM ~370 MB |
| **Đa nhân 4w (Mặc định)** | **`libx264`** | **4** | **46.99s** | **9.6 fps** | **450/450 (`yuv420p`)** | **Nhanh nhất (~1.9×), tổng RAM < 550 MB / 16 GB** |

*(Trên tập thật có xen kẽ Level A/B/C, tốc độ thực tế đạt ~14–22 fps; Short 60s render ~1.5–2 phút, Phim dài 5 phút ~7–9 phút).*

| Hạng mục | Trạng thái trong `03_ENGINE` | Ghi chú vận hành & Giới hạn kỹ thuật |
| :--- | :---: | :--- |
| **Pre-production Visual Beat & Motion Audit** | ✅ Tự động hóa | `gate0` + `motion-check <EP>` hỗ trợ cả `level2` và `level3`, kiểm `split_screen`, `rack_focus`, `transitions`, `detail_fx` |
| **Level A (Static Cinematic + Presets + Easing)** | ✅ Tự động hóa (`cv2`) | `gate4_timeline.py` + `motion_fx.py`: 11 preset + 11 kiểu `transition_in` (thêm `whip_pan_left/right`, `zoom_punch`, `luma_wipe`, `film_burn`) |
| **Level B (2.5D Parallax · max 4 lớp + Rack Focus + Head Micro-Tilt)** | ✅ Tự động ghép lớp (`cv2`) | `motion_fx.py` + `motion_fx_l3.py`: ghép 2–4 lớp, `blur_from/blur_to <= 8.0px` (pre-baked 1 lần), `breathing`, `head_tilt_deg <= 2.2°` khớp `.wav` |
| **Level C (Level 2 + Level 3 Nhóm 1 & 2 + Living-Character 2.5)** | ✅ Tự động hóa (`cv2`) | **20 loại `detail_fx` + `split_screen`:** `detail_reveal`, `eye_blink`, `mouth_sync` (3–4 trạng thái gồm `round_image`), `eye_gaze`, `expr_swap`, `screen_glow`, `light_shift`, `cursor_click`, `focus_highlight`, `detail_layer`, `phone_waveform`, `red_circle_draw`, `highlighter_sweep`, `animated_counter`, `typing_indicator`, `rain_layer`, `ambient_particles`, `light_sweep`, `color_mood`, `chromatic_pulse` |
| **Level D (Optional External Clip)** | ✅ Phát & hạ cấp an toàn<br>❌ Không sinh AI cục bộ | Hỗ trợ phát clip `.mp4` dựng ngoài (`natural_hold` + `video_start_offset`), hạ cấp tức thì bằng `"video_enabled": false` hoặc `--safe-motion` |
| **Render Engine Đa Nhân + QSV** | ✅ Tự động hóa | `gate4_timeline.py`: mặc định `--workers 4 --encoder auto` (tự nối chunk lossless `-c copy`), hỗ trợ `--workers 1 --encoder qsv` |
| **Sound-Motion Foley Presets** | ✅ Tự động hóa | Đã bổ sung thêm `marker_draw` và `counter_tick` vào `03_ENGINE/sfx_library.py` |
| **Gate 5 Visual Motion QC (11 điểm)** | ✅ Tự động hóa báo cáo + Human signoff | Tự ghi `motion_qc` + `render_stats` vào `qa_audit_report_gate5.json` và `GATE5_QA_REPORT.md` |

---

## VII. THAM CHIẾU CẤU HÌNH `episode.json` (LEVEL 3 — SẴN DÙNG CHO CẢ 16:9 & 9:16)

```json
{
  "motion_upgrade": "level3",
  "scenes": [
    {
      "id": "s01_parallax_rack_living25",
      "image": "assets/scene01.jpg",
      "start": 0.0,
      "end": 12.0,
      "beat_type": "establishing",
      "motion_level": "B",
      "motion_intent": "2.5D parallax + chuyển nét Rack Focus mờ nền + thở + nghiêng đầu nhẹ theo giọng + liếc mắt + khẩu hình 4 trạng thái",
      "parallax": {
        "camera": "push_in",
        "layers": [
          {"role": "bg", "image": "assets/s01_bg.jpg", "depth": 0.4, "blur_from": 0.5, "blur_to": 5.5, "blur_at": 2.0, "blur_dur": 2.5},
          {"role": "fg", "image": "assets/s01_fg.png", "depth": 1.25, "breathe_y": 2.0, "breathe_period": 3.6,
           "head_tilt_deg": 1.2, "head_pivot": [0.5, 0.78], "tilt_speaker": "thang_tun"}
        ]
      },
      "detail_fx": [
        {"type": "eye_blink", "image": "assets/s01_blink.jpg", "region": [0.45, 0.35, 0.58, 0.42], "times": [1.8, 5.4, 9.2], "layer": "fg"},
        {"type": "eye_gaze", "image": "assets/s01_gaze_down.jpg", "region": [0.45, 0.35, 0.58, 0.42], "at": 3.5, "dur": 0.16, "hold_dur": 1.4, "layer": "fg"},
        {"type": "mouth_sync", "speaker": "thang_tun", "region": [0.47, 0.43, 0.56, 0.49],
         "closed_image": "assets/s01_m_closed.jpg", "mid_image": "assets/scene01.jpg",
         "open_image": "assets/s01_m_open.jpg", "round_image": "assets/s01_m_round.jpg", "layer": "fg"},
        {"type": "ambient_particles", "count": 26, "opacity": 0.38},
        {"type": "color_mood", "mood": "warm_daily", "strength": 0.75}
      ]
    },
    {
      "id": "s02_split_cuoc_goi",
      "image": "assets/s02_scammer.jpg",
      "start": 12.0,
      "end": 24.0,
      "beat_type": "suspicion",
      "motion_level": "C",
      "motion_intent": "Chia đôi màn hình cuộc gọi (16:9 trái-phải / 9:16 trên-dưới) sáng viền & sóng âm theo người đang nói",
      "transition_in": {"type": "whip_pan_left", "dur": 0.28},
      "split_screen": {
        "layout": "vertical",
        "ratio": 0.5,
        "panels": [
          {"image": "assets/s02_scammer.jpg", "speaker": "ke_gia_danh", "label": "SỐ LẠ", "waveform": true},
          {"image": "assets/s02_victim.jpg", "speaker": "co_tu", "label": "NẠN NHÂN", "waveform": true}
        ]
      }
    },
    {
      "id": "s03_boc_tran_vat_chung",
      "image": "assets/scene03.jpg",
      "start": 24.0,
      "end": 36.0,
      "beat_type": "information",
      "motion_level": "C",
      "motion": {"preset": "slow_push_in"},
      "transition_in": {"type": "zoom_punch", "dur": 0.28},
      "detail_fx": [
        {"type": "red_circle_draw", "region": [0.64, 0.30, 0.88, 0.44], "at": 25.0, "dur": 0.55, "style": "circle"},
        {"type": "highlighter_sweep", "region": [0.64, 0.48, 0.88, 0.55], "at": 26.2, "dur": 0.45},
        {"type": "animated_counter", "start": 24.5, "end": 34.5, "count_dur": 2.4, "from_val": 0, "to_val": -18000000,
         "fmt": "vnd", "label": "SỐ DƯ TÀI KHOẢN", "pos": [0.22, 0.30], "style": "danger"},
        {"type": "phone_waveform", "speaker": "nguoi_boc_tran", "start": 24.5, "end": 35.5, "pos": [0.22, 0.72], "label": "PHÂN TÍCH"},
        {"type": "color_mood", "mood": "noir_evidence"}
      ]
    },
    {
      "id": "s04_cao_trao_mua_dem",
      "image": "assets/scene04.jpg",
      "start": 36.0,
      "end": 46.0,
      "beat_type": "climax",
      "motion_level": "C",
      "motion": {"preset": "tense_push"},
      "transition_in": {"type": "film_burn", "dur": 0.4},
      "detail_fx": [
        {"type": "rain_layer", "opacity": 0.34, "density": 1.0},
        {"type": "light_sweep", "mode": "light", "intensity": 0.28, "repeat": 2},
        {"type": "chromatic_pulse", "at": 38.5, "dur": 0.30, "shift_px": 6, "zoom_blur": 0.025},
        {"type": "color_mood", "mood": "high_tension"}
      ],
      "shakes": [{"at": 38.5, "amp": 26}]
    }
  ]
}
```
*Xem nhanh toàn bộ preset & cấu hình phần cứng khả dụng bằng:* `python factory196/_engine/run.py presets`  
*Lệnh render linh hoạt:* `python factory196/_engine/run.py gate <EP> 4 [--workers 4] [--encoder auto|x264|qsv] [--safe-motion]`

---

## VIII. QUALITY CONTROL — BẮT BUỘC KIỂM TRA TRƯỚC KHI XUẤT VIDEO (GATE 5)

Mỗi video phải qua đủ **11 điểm kiểm tra** (được xuất tự động vào `staging/<EP>/GATE5_QA_REPORT.md` trước khi ký duyệt Gate 5 điểm 4):

- [ ] Motion có phục vụ câu chuyện không?
- [ ] Có cảnh nào bị zoom/pan lặp lại quá máy móc không?
- [ ] Có ít nhất một vài visual highlight đáng nhớ nếu nguồn hình phù hợp không?
- [ ] 2.5D có tạo chiều sâu tự nhiên, không méo hình không?
- [ ] Object motion & Living-Character (`eye_blink`, `mouth_sync`, `breathing`) có đúng nội dung, đúng giọng nhân vật nói và không lộ viền màu da không?
- [ ] Có chi tiết AI bị biến dạng không?
- [ ] Motion có gây distraction khỏi voice-over không?
- [ ] Có giữ được continuity giữa các cảnh không?
- [ ] Có sound effect nào không cần thiết không?
- [ ] Render có smooth, không flicker, không jump frame, không lỗi layer hoặc mask không?
- [ ] Các cảnh không phù hợp motion nâng cao có được giữ xử lý đơn giản không?

> **Quy tắc chốt:** Nếu một hiệu ứng không đạt chất lượng, hãy **hạ cấp hoặc loại bỏ nó**. Chất lượng cảnh tĩnh sạch sẽ luôn tốt hơn một cảnh chuyển động lỗi.
