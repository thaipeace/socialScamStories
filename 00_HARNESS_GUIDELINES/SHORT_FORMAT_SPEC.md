# QUY CHUẨN ĐỊNH DẠNG SHORT 70 GIÂY – “BÓC TRẦN LỪA ĐẢO”
## Phương châm: XEM ĐỂ KHÔNG BỊ LỪA – kịch tính để giữ chân, dấu hiệu để mang về

*Kế thừa nguyên tắc “lát cắt nhỏ, ít thoại, âm thanh gánh 80% kịch tính” của 779 v6. Thời lượng mặc định 70s (cho phép 45–90s, chỉnh `duration_sec`).*

## I. CÔNG THỨC 6 NHỊP (mặc định trong template `episode.json`)

```
[00–05s] 1. HOOK         Khoảnh khắc sốc nhất, đặt câu hỏi “chuyện gì vậy?”
                         – chuông điện thoại lúc nửa đêm / “ting ting” trừ tiền / câu thoại dồn dập
                         – Tít hook ≤ 10 từ xuất hiện trước giây 1.0
[05–20s] 2. MỒI NHỬ      Kẻ lừa tiếp cận: tin nhắn, cuộc gọi, lời mời, món hời
                         – bong bóng tin nhắn giả lập (chat_bubbles)
[20–38s] 3. LEO THANG    Thao túng tâm lý: dọa, dỗ, ép thời gian, cô lập nạn nhân
                         – 1 callout “DẤU HIỆU” giữa video (callouts)
[38–50s] 4. CÚ CHỐT      Nạn nhân làm theo → mất tiền / suýt mất tiền
                         – “ting ting” + impact + cúp máy
[50–60s] 5. BÓC TRẦN     Giọng “Người Bóc Trần”: đây là chiêu gì, vì sao ai cũng có thể tin
                         – transition glitch, kẻ lừa lộ “bóng thật”
[60–70s] 6. DẤU HIỆU     Thẻ DẤU HIỆU NHẬN BIẾT (2–4 ý hiện lần lượt) + VIỆC NÊN LÀM
                         – disclaimer 3 giây cuối
```

**Biến thể kết:** xen kẽ tập “mất tiền” và tập “thoát hiểm” (nạn nhân nhận ra dấu hiệu, gọi người thân) để không gây tâm lý tiêu cực và để làm gương hành vi đúng.

## II. QUY TẮC THOẠI
- 4–6 câu, **≤ 22 từ/câu, tổng ≤ 110 từ** (Gate 0 tự kiểm).
- Lời kẻ lừa: đủ để nhận ra chiêu, **không đủ để chép làm kịch bản** (xem Nguyên tắc 3 – Harness pháp lý).
- Giọng qua điện thoại: dùng speaker `ke_gia_danh` (đã gắn filter `phone`), hoặc thêm `"af": "phone"` vào câu thoại.
- Câu “bóc trần” luôn trả lời 2 ý: **chiêu gì** + **vì sao dễ tin**.

## III. 5 LỚP ĐỒ HỌA (engine Gate 4 tự dựng, cấu hình trong `episode.json`)

| Lớp | Khóa cấu hình | Vị trí | Ghi chú |
| :--- | :--- | :--- | :--- |
| Nhận diện kênh | `channel_config.json` | Trên-trái (VCH + “BÓC TRẦN LỪA ĐẢO”), dưới-phải watermark | Xuyên suốt |
| Hook | `hook` | Y = 170 trở xuống | Kicker đỏ + tít trắng |
| Phụ đề | tự sinh từ Gate 2 | Đáy hộp ≤ Y 1375 | Tự chia dòng, màu theo nhân vật |
| Tin nhắn / Callout | `chat_bubbles`, `callouts` | Giữa khung | Bong bóng trung tính, không UI app thật |
| Thẻ dấu hiệu + Disclaimer | `red_flags`, `disclaimer` | Y 300 → ≤ 1420 | Nền làm tối 60% |

**Safe Zone** (giữ nguyên chuẩn 779): X 80–920, Y ≤ 1420; cấm vùng phải 15% và đáy 25% (UI của Shorts/TikTok/Reels).

## IV. CHUYỂN CẢNH & CHUYỂN ĐỘNG — VISUAL MOTION LEVEL 3 + TIẾN TRÌNH CHECK 1 → 2 → 3
*Áp dụng mặc định theo [VISUAL_MOTION_HARNESS.md](VISUAL_MOTION_HARNESS.md) (`HRN-MOTION-L3.0`): mọi tập làm mới, chỉnh sửa hoặc nâng cấp bắt buộc khai báo `"motion_upgrade": "level3"`, đủ `beat_type` + `motion_level` (`A`/`B`/`C`/`D`) và vượt đủ **CHECK 1 → 2 → 3** (`Level 3 ⊃ Level 2 ⊃ Level 1`) tại `motion-check`, `gate0`, `gate4`, `gate5`.*

| `transition_in.type` | Dùng khi |
| :--- | :--- |
| `dissolve` (0.3s) | Chuyển nhịp thông thường |
| `whip_pan_left/right` (0.25s), `zoom_punch` (0.28s) | Chuyển cú sốc, cắt vào đối đầu / bóc trần nhanh (Level 3) |
| `luma_wipe` (0.35s), `film_burn` (0.4s) | Chuyển hồi, chuyển thời điểm hoặc lật mặt (Level 3) |
| `flash_red` (0.25s), `flash_white` | Vào CÚ CHỐT |
| `glitch` (0.4s) | Vào BÓC TRẦN / lộ deepfake |
| `fade_black` (0.4s), `cut` | Vào THẺ DẤU HIỆU / tiết lộ gọn |

- **Tiến trình Check 1 → 2 → 3 bắt buộc cho Short 9:16 (~50–70s):**
  - **CHECK 1 (Level 1):** Đủ timeline, thoại ≤ 22 từ/câu & ≤ 110 từ, Safe Zone 9:16, `hook`, `red_flags`, `disclaimer`, `clearance: ĐẠT`; khi sửa/update giữ nguyên dữ liệu cũ và đồng bộ `source/build_draft.py`.
  - **CHECK 2 (Kế thừa Level 2 — Khóa cứng không được bỏ qua):**
    - **Level A:** Đa dạng preset (`slow_push_in`, `slow_pull_out`, `pan_left/right`, `drift_up`, `static_hold`) — **cấm lặp zoom-in ≥ 3 cảnh liên tiếp**.
    - **Level B (2.5D + Breathing — Bắt buộc `≥ 1` cảnh, khuyến nghị `1–2` cảnh):** Tách 2–4 lớp sạch (`sX_bg.jpg` + `sX_fg.png`), gắn `breathe_y`/`breathe_period` (`≥ 1` lớp), hỗ trợ thêm `rack_focus` và `head_micro_tilt <= 2.2°`.
    - **Living-Character khóa pixel qua `face_roi_prep.py` — Bắt buộc `eye_blink ≥ 2` và `mouth_sync ≥ 2` (khuyến nghị `2–4` cảnh cận rõ mặt):** Chớp mắt + **chép miệng 3–4 trạng thái khớp `.wav` thật** (duyệt bảng Face QC cận mặt), kết hợp `screen_glow`, `detail_reveal`, `light_shift`, `notifications`/`chat_bubbles`, `focus_highlight` khớp foley.
  - **CHECK 3 (Nâng cấp Level 3 — Chỉ PASS sau khi CHECK 1 & 2 đều PASS):** Áp dụng chọn lọc `split_screen` (`layout: "horizontal"` trên–dưới cho 9:16), `phone_waveform`, `red_circle_draw`, `highlighter_sweep`, `animated_counter`, `typing_indicator`, `rain_layer`, `ambient_particles`, `light_sweep`, `color_mood`, `chromatic_pulse`, `eye_gaze`/`expr_swap`, 4-state `round_image`. Mọi lần sửa/render lại đều tự hủy chữ ký `human_qa_signoff.json` cũ để buộc duyệt lại bản Staging mới.
  - **Level D (AI I2V ngắn dựng ngoài tùy chọn):** Tối đa 1 khoảnh khắc phản ứng đặc biệt nếu không biến dạng; có lỗi → hạ cấp ngay bằng `"video_enabled": false`.

## V. ÂM THANH (preset có sẵn – `python factory619/_engine/run.py presets`)
- **Ambience:** `room_tone`, `night_room`, `office`, `street`, `crowd`, `rain`
- **Foley:** `phone_ring`, `phone_vibrate`, `notification`, **`bank_ting`** (âm nhận diện kênh), `message_send`, `typing`, `keyboard`, `click`, `light_switch`, `low_accent`, `door_knock`, `footsteps`, `heartbeat`, `impact`, `riser`, `glitch`, `call_end`, `whistle`, `school_bell`, `chapter_sting`
- **BGM:** `investigative_story`, `suspense_pulse` (nhịp 1–4), `tension_drone` (bóc trần), `action_climax`, `warm_outro` (thẻ dấu hiệu)
- Có thể thay preset bằng file thật: `{"file": "assets/sfx/xxx.wav", "at": 12.0}` (chỉ dùng âm thanh có quyền sử dụng). Không chèn SFX thừa chỉ để lấp khoảng trống; mọi SFX đi kèm motion phải giữ mức không lấn thoại.

