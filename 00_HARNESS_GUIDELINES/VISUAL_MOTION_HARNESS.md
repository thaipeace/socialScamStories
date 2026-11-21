# HARNESS CHUYỂN ĐỘNG HÌNH ẢNH — VISUAL MOTION UPGRADE (LEVEL 2)
*Mã: HRN-MOTION-L2 · Áp dụng mặc định cho mọi tập mới của cả `factory196` (16:9) và `factory619` (9:16)*

> [!IMPORTANT]
> **DEFAULT RULE:** Mỗi video Tèo Cảnh Giác từ nay **bắt buộc có Visual Motion Planning trước khi render** (`beat_type` + `motion_level` cho từng cảnh). Ken Burns vẫn là nền tảng, nhưng **không còn là giải pháp duy nhất**. Motion nâng cao phải được chọn theo nội dung, có tiết chế, có chủ đích và được QC đủ 11 điểm ở Gate 5 trước khi xuất bản.
>
> **Nguyên tắc không hồi tố & tương thích ngược:** Không sửa các tập đã hoàn thành/đã phát hành (`factory196: EP01b–EP08, EP27`; `factory619: EP01–EP10`). Engine `03_ENGINE` giữ tương thích ngược 100% với tập cũ chưa khai báo `"motion_upgrade": "level2"`.

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

### LEVEL B — DEPTH MOTION / 2.5D PARALLAX (`"motion_level": "B"`)
Áp dụng cho **~2–4 cảnh nổi bật có chiều sâu không gian** mỗi video khi nguồn hình phù hợp *(không bắt buộc đủ số lượng nếu ảnh không phù hợp)*.
- Tách cảnh thành 2–3 lớp: **Background (`bg`)** · **Main subject (`subject`/`mid` RGBA)** · **Foreground (`fg` RGBA tùy chọn)**.
- Tạo chuyển động camera chậm (`push_in`, `pull_out`, `pan_left`, `pan_right`, `drift_push`) để các lớp dịch chuyển theo tốc độ `depth` khác nhau (tùy chọn `blur` nhẹ trên `bg`/`fg` để tạo chiều sâu trường ảnh).
- **Cấm exaggerate depth**, cấm làm méo cơ thể, gương mặt hoặc vật thể.
- Nếu nguồn ảnh không đủ sạch để tách lớp không lỗi biên → **giữ Level A**, không cố ép 2.5D.

### LEVEL C — OBJECT / DETAIL MOTION (`"motion_level": "C"`)
Ưu tiên **animate một chi tiết cụ thể** thay vì animate toàn bộ khung hình.
- Các dạng được `03_ENGINE` hỗ trợ trực tiếp:
  - **Màn hình / ánh sáng phản chiếu (`screen_glow`, `light_shift`):** điện thoại sáng màn hình, ánh sáng màn hình hắt lên mặt/bàn tay, đèn bật/tắt.
  - **Chi tiết thay đổi theo nhịp (`detail_reveal`):** chuyển mượt giữa 2 ảnh đồng khung (toàn khung hoặc vùng `region` có làm mềm biên `feather`), ví dụ: màn hình tối → sáng, đèn tắt → bật, chi tiết vật chứng lộ diện.
  - **Notification & Tin nhắn theo nhịp kể (`notifications`, `chat_bubbles`):** thanh thông báo trung tính trượt nhẹ từ mép trên Safe Zone, bong bóng tin nhắn trượt lên theo đúng mốc thoại & SFX (tuyệt đối không logo/UI app thật).
  - **Thao tác chuột / chạm (`cursor_click`):** con trỏ tối giản di chuyển mượt tới tọa độ mục tiêu và tạo vòng sóng click nhẹ đúng mốc `click_at`.
  - **Bàn tay / vật thể chuyển động nhẹ (`detail_layer`):** lớp RGBA PNG tách riêng dịch chuyển vị trí/scale/opacity gọn nhẹ theo trục có kiểm soát.
  - **Dẫn mắt / Không khí nhẹ (`focus_highlight`, `light_shift`):** gom sáng tập trung vào chi tiết quan trọng hoặc đổi tông ánh sáng/độ sáng bằng 1D LUT siêu nhẹ (thay thế hoàn toàn các hiệu ứng hạt/volumetric nặng).
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

> [!WARNING]
> **HARDWARE SAFETY PROFILE (`low_ram_cpu_l480`) — ThinkPad L480 · Intel i5-8250U · 8GB RAM · iGPU (không GPU rời):**
> 1. **CẤM dùng trên máy hiện tại (Excluded):** AI image-to-video / diffusion chạy cục bộ, Blender / 3D rendering, model AI cần GPU (`torch`/`rembg`/depth AI), heavy blur (`> 2.0px` hoặc blur theo từng frame), complex masking, optical flow, **particle systems (`rain`)**, **volumetric / full-frame shader sweeps (`shadow_drift`)**, bộ đệm frame lớn, render song song nhiều cảnh cùng lúc và nạp toàn bộ ảnh full-res vào RAM cùng một lúc.
> 2. **An toàn & Khuyến nghị (Safe & Active):** Giữ nguyên đầu ra 1080p của pipeline hiện hữu, không cài thêm thư viện ngoài `Pillow + NumPy + FFmpeg`; chạy tuần tự từng cảnh với **cơ chế nạp trượt (sliding-window lazy load: tối đa 1–2 cảnh trong RAM tại mọi thời điểm)** và FFmpeg `-threads 4`.
> 3. **Fallback bắt buộc:** Mọi hiệu ứng nâng cao đều tùy chọn; nếu chậm, lỗi hoặc thiếu tài nguyên, hạ cấp tức thì về Level A Ken Burns (theo từng cảnh bằng `"video_enabled": false` / bỏ `parallax` hoặc toàn tập bằng cờ `--safe-motion`).
> 4. **Thử ngắn trước khi render dài:** Mọi mẫu motion mới phải thử trên 1 đoạn ngắn `5–10 giây` để kiểm thời gian render, mức RAM và độ mượt trước khi chạy cả tập.

| Hạng mục | Trạng thái trong `03_ENGINE` | Ghi chú vận hành & Giới hạn kỹ thuật |
| :--- | :---: | :--- |
| **Pre-production Visual Beat & Motion Audit** | ✅ Tự động hóa | `gate0` (chặn nếu thiếu `motion_level`/`beat_type` ở tập Level 2 hoặc vượt quá 3 lớp 2.5D) + lệnh `motion-check <EP>` |
| **Level A (Static Cinematic + Presets + Easing)** | ✅ Tự động hóa (Nhẹ) | `gate4_timeline.py` + `motion_fx.py`: 11 preset (`static_hold`, `slow_push_in`, `slow_pull_out`, `pan_left/right`, `drift_up/down`...), `smoothstep`/`ease_out`/`ease_in` |
| **Level B (Simple 2.5D Parallax · max 2–3 lớp)** | ✅ Tự động ghép lớp (Nhẹ)<br>⚠️ Tách lớp ngoài | `gate4_timeline.py` ghép tối đa **2–3 lớp** (`bg` + `subject` RGBA + `fg` RGBA tùy chọn), giới hạn `blur <= 2.0px` tính 1 lần lúc nạp cảnh, tự giải phóng RAM ngay khi qua cảnh. **Giới hạn:** Không chạy AI tách nền/depth cục bộ; file PNG trong suốt chuẩn bị ngoài ở Gate 1, tự fallback Level A nếu thiếu lớp |
| **Level C (Lightweight Object / Detail Motion)** | ✅ Tự động hóa (Nhẹ) | Hỗ trợ 6 hiệu ứng nhẹ: `detail_reveal` (vùng chữ nhật đơn giản feather `<= 10px`), `screen_glow` (ROI cục bộ), `light_shift` (1D LUT siêu nhẹ), `cursor_click` (crop cục bộ), `focus_highlight` (mặt nạ tĩnh), `detail_layer` (vị trí/scale/opacity) + `notifications` & `chat_bubbles` trượt nhẹ. **Đã loại trừ:** `rain` (particle) và `shadow_drift` (volumetric) |
| **Level D (Optional External Clip)** | ✅ Phát & hạ cấp an toàn<br>❌ Không sinh AI cục bộ | Hỗ trợ phát clip `.mp4` dựng ngoài (`natural_hold` + `video_start_offset`) và hạ cấp tức thì bằng `"video_enabled": false` hoặc `--safe-motion`. Tuyệt đối không cài/chạy AI I2V cục bộ |
| **Sound-Motion Foley Presets** | ✅ Tự động hóa | Đã bổ sung `click`, `keyboard`, `light_switch`, `low_accent` vào `03_ENGINE/sfx_library.py` |
| **Gate 5 Visual Motion QC (11 điểm)** | ✅ Tự động hóa báo cáo + Human signoff | Tự ghi `motion_qc` vào `qa_audit_report_gate5.json` và xuất đủ bảng 11 điểm vào `GATE5_QA_REPORT.md` gắn với điểm duyệt số 4 |

---

## VII. THAM CHIẾU CẤU HÌNH `episode.json` (LEVEL 2)

```json
{
  "motion_upgrade": "level2",
  "scenes": [
    {
      "id": "s02_boi_canh",
      "image": "assets/scene02.jpg",
      "start": 25.0,
      "end": 42.0,
      "beat_type": "establishing",
      "motion_level": "A",
      "motion_intent": "Quét ngang nhẹ giới thiệu bối cảnh đời thường",
      "motion": {"preset": "pan_right"}
    },
    {
      "id": "s04_chieu_sau",
      "image": "assets/scene04.jpg",
      "start": 55.0,
      "end": 72.0,
      "beat_type": "suspicion",
      "motion_level": "B",
      "motion_intent": "Đẩy nhẹ 2.5D tạo chiều sâu không gian khi bắt đầu nghi vấn",
      "parallax": {
        "camera": "push_in",
        "strength": 1.0,
        "layers": [
          {"role": "bg",      "image": "assets/s04_bg.jpg",  "depth": 0.35, "blur": 1.2},
          {"role": "subject", "image": "assets/s04_mid.png", "depth": 1.00},
          {"role": "fg",      "image": "assets/s04_fg.png",  "depth": 1.45, "blur": 1.6}
        ]
      }
    },
    {
      "id": "s05_tin_nhan",
      "image": "assets/scene05.jpg",
      "start": 72.0,
      "end": 88.0,
      "beat_type": "information",
      "motion_level": "C",
      "motion_intent": "Màn hình điện thoại sáng lên kèm thao tác click đúng nhịp thoại",
      "motion": {"preset": "static_hold"},
      "detail_fx": [
        {"type": "screen_glow", "start": 73.5, "end": 86.0, "pos": [0.52, 0.62], "radius": [0.22, 0.24], "color": [130, 195, 255], "intensity": 0.34, "mode": "turn_on"},
        {"type": "cursor_click", "start": 76.0, "click_at": 77.2, "end": 78.4, "from": [0.64, 0.72], "to": [0.52, 0.60]}
      ]
    },
    {
      "id": "s07_phan_ung",
      "image": "assets/scene07.jpg",
      "video": "assets/s07_turn.mp4",
      "video_enabled": true,
      "video_fit": "natural_hold",
      "video_start_offset": 0.6,
      "start": 105.0,
      "end": 112.0,
      "beat_type": "anomaly",
      "motion_level": "D",
      "motion_intent": "Nhân vật khựng lại khi phát hiện chi tiết lạ (tắt video_enabled nếu lỗi)"
    }
  ],
  "notifications": [
    {"start": 73.5, "end": 77.5, "title": "Tin nhắn mới", "text": "Số lạ: Vui lòng xác nhận trong 5 phút", "stamp": "vừa xong", "style": "danger"}
  ]
}
```
*Xem nhanh toàn bộ danh sách preset khả dụng bằng:* `python factory196/_engine/run.py presets`

---

## VIII. QUALITY CONTROL — BẮT BUỘC KIỂM TRA TRƯỚC KHI XUẤT VIDEO (GATE 5)

Mỗi video phải qua đủ **11 điểm kiểm tra** (được xuất tự động vào `staging/<EP>/GATE5_QA_REPORT.md` trước khi ký duyệt Gate 5 điểm 4):

- [ ] Motion có phục vụ câu chuyện không?
- [ ] Có cảnh nào bị zoom/pan lặp lại quá máy móc không?
- [ ] Có ít nhất một vài visual highlight đáng nhớ nếu nguồn hình phù hợp không?
- [ ] 2.5D có tạo chiều sâu tự nhiên, không méo hình không?
- [ ] Object motion có đúng nội dung và timing không?
- [ ] Có chi tiết AI bị biến dạng không?
- [ ] Motion có gây distraction khỏi voice-over không?
- [ ] Có giữ được continuity giữa các cảnh không?
- [ ] Có sound effect nào không cần thiết không?
- [ ] Render có smooth, không flicker, không jump frame, không lỗi layer hoặc mask không?
- [ ] Các cảnh không phù hợp motion nâng cao có được giữ xử lý đơn giản không?

> **Quy tắc chốt:** Nếu một hiệu ứng không đạt chất lượng, hãy **hạ cấp hoặc loại bỏ nó**. Chất lượng cảnh tĩnh sạch sẽ luôn tốt hơn một cảnh chuyển động lỗi.
