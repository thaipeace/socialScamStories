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

## IV. CHUYỂN CẢNH & CHUYỂN ĐỘNG — VISUAL MOTION UPGRADE (LEVEL 2)
*Áp dụng mặc định theo [VISUAL_MOTION_HARNESS.md](VISUAL_MOTION_HARNESS.md): mỗi cảnh bắt buộc khai báo `beat_type` và `motion_level` (`A`/`B`/`C`/`D`) trong `episode.json` (`"motion_upgrade": "level2"`).*

| `transition_in.type` | Dùng khi |
| :--- | :--- |
| `dissolve` (0.3s) | Chuyển nhịp thông thường |
| `flash_red` (0.25s) | Vào CÚ CHỐT |
| `glitch` (0.4s) | Vào BÓC TRẦN / lộ deepfake |
| `fade_black` (0.4s) | Vào THẺ DẤU HIỆU |
| `flash_white`, `cut` | Tùy ý (ưu tiên `cut` gọn khi tiết lộ thông tin quan trọng) |

- **Phân cấp Motion cho Short 9:16 (~55–70s):**
  - **Level A (nền tảng):** Đa dạng hóa `motion.preset` (`slow_push_in`, `slow_pull_out`, `pan_left`, `pan_right`, `drift_up`, `static_hold`) — **cấm lặp zoom-in máy móc ≥ 3 cảnh liên tiếp**; giữ `wobble: "none"` mặc định cho cảnh thường/kết, chỉ dùng `handheld`/`tense` và `shakes` đúng điểm cao trào khớp foley.
  - **Level B (2.5D parallax):** Chọn 1–2 cảnh đắt giá có chiều sâu phù hợp (tách lớp `bg` + `subject` + `fg` tùy chọn), không bắt buộc nếu nguồn hình chưa phù hợp.
  - **Level C (Object/Detail motion):** Rất hiệu quả trên khung dọc 9:16 cho điện thoại sáng màn hình (`screen_glow`), thông báo trượt xuống (`notifications`), tin nhắn trượt lên (`chat_bubbles`), thao tác bấm (`cursor_click`), đổi chi tiết đồng khung (`detail_reveal`) hoặc gom sáng (`focus_highlight`), khớp sát nhịp VO & foley.
  - **Level D (AI I2V ngắn tùy chọn):** Tối đa 1 khoảnh khắc phản ứng đặc biệt nếu không biến dạng; có lỗi → hạ cấp ngay bằng `"video_enabled": false`.

## V. ÂM THANH (preset có sẵn – `python factory619/_engine/run.py presets`)
- **Ambience:** `room_tone`, `night_room`, `office`, `street`, `crowd`, `rain`
- **Foley:** `phone_ring`, `phone_vibrate`, `notification`, **`bank_ting`** (âm nhận diện kênh), `message_send`, `typing`, `keyboard`, `click`, `light_switch`, `low_accent`, `door_knock`, `footsteps`, `heartbeat`, `impact`, `riser`, `glitch`, `call_end`, `whistle`, `school_bell`, `chapter_sting`
- **BGM:** `investigative_story`, `suspense_pulse` (nhịp 1–4), `tension_drone` (bóc trần), `action_climax`, `warm_outro` (thẻ dấu hiệu)
- Có thể thay preset bằng file thật: `{"file": "assets/sfx/xxx.wav", "at": 12.0}` (chỉ dùng âm thanh có quyền sử dụng). Không chèn SFX thừa chỉ để lấp khoảng trống; mọi SFX đi kèm motion phải giữ mức không lấn thoại.

