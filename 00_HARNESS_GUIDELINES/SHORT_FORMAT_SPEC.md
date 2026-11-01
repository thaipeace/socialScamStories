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

## IV. CHUYỂN CẢNH & CHUYỂN ĐỘNG
| `transition_in.type` | Dùng khi |
| :--- | :--- |
| `dissolve` (0.3s) | Chuyển nhịp thông thường |
| `flash_red` (0.25s) | Vào CÚ CHỐT |
| `glitch` (0.4s) | Vào BÓC TRẦN / lộ deepfake |
| `fade_black` (0.4s) | Vào THẺ DẤU HIỆU |
| `flash_white`, `cut` | Tùy ý |

`motion.wobble`: `none` · `calm` · `handheld` · `tense`; `shakes`: rung tắt dần tại giây khớp foley (impact, đập cửa).

## V. ÂM THANH (preset có sẵn – `python factory/_engine/run.py presets`)
- **Ambience:** room_tone, night_room, office, street, crowd, rain
- **Foley:** phone_ring, phone_vibrate, notification, **bank_ting** (âm nhận diện kênh), message_send, typing, door_knock, footsteps, heartbeat, impact, riser, glitch, call_end
- **BGM:** suspense_pulse (nhịp 1–4), tension_drone (bóc trần), warm_outro (thẻ dấu hiệu)
- Có thể thay preset bằng file thật: `{"file": "assets/sfx/xxx.wav", "at": 12.0}` (chỉ dùng âm thanh có quyền sử dụng).
