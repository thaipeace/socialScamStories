# BIÊN BẢN KIỂM DUYỆT GATE 5 [factory196 · 16:9] – EP07: Sau hai trăm triệu

- Video staging: [EP07_SauHaiTramTrieu_464s_staging.mp4](file:///C:/projects/socialScamStories/factory196/staging/EP07/EP07_SauHaiTramTrieu_464s_staging.mp4) (266.89 MB)
- Phiên bản dựng: `v6-level3-full-abc-staging` · `motion_upgrade: level3` · `sha256: f0aeb1904b6cb913`
- Trạng thái: ✅ **ĐẠT 8/8 – được chuyển Gate 6**

## TIẾN TRÌNH CHECK 1 → 2 → 3 (LUẬT KẾ THỪA CỘNG DỒN: `Level 3 ⊃ Level 2 ⊃ Level 1`)

| Tầng Check | Trạng thái | Thông số thực đo |
| :--- | :---: | :--- |
| **CHECK 1 — Nền Level 1** *(Cốt truyện · TTS · Safe Zone · Pháp lý)* | ✅ PASS | Điểm tự động 1, 3, 7, 8 + master âm thanh Gate 3 |
| **CHECK 2 — Kế thừa Level 2** *(2.5D + Breathing + Chớp mắt + Chép miệng)* | ✅ PASS | `2.5D`: **4** *(≥1)* · `Breathing`: **7** *(≥1)* · `eye_blink`: **24** *(≥3)* · `mouth_sync`: **22** *(≥3; 4-state: 8)* |
| **CHECK 3 — Nâng cấp Level 3** *(Đạo diễn · Không khí · Living-Char 2.5)* | ✅ PASS | `split_screen`: **0** · `RackFocus`: **4** · `HeadTilt`: **2** · `Gaze/Expr`: **0** · `L3_FX`: **53** · `L3_Trans`: **15** |

## BẢNG KIỂM DUYỆT 8 ĐIỂM GATE 5

| Tiêu chí | Trạng thái | Bằng chứng |
| :--- | :---: | :--- |
| 1. Không định danh người / tổ chức / số thật | ✅ PASS | Cấm cứng: 0; cảnh báo: 0; SĐT: 0; URL: 0; dãy số TK: 0 |
| 2. Không hướng dẫn thủ đoạn chi tiết (chỉ bóc trần cơ chế tâm lý & dấu hiệu) | ✅ PASS | Người duyệt: Chu kenh. Duyet Staging v6-level3-full-abc (24 blink, 22 mouth_sync 100% canh noi, 4x 2.5D, 82 L3 FX) |
| 3. Sạch từ khóa thuật toán (ASR/OCR/metadata) | ✅ PASS | Cấm cứng: 0; cảnh báo: 0 |
| 4. Hình ảnh & chuyển động an toàn: không logo/giao diện/sắc phục thật, không máu me, motion mượt đúng nhịp & giữ continuity (QC 11 điểm) | ✅ PASS | Người duyệt: Chu kenh. Duyet Staging v6-level3-full-abc (24 blink, 22 mouth_sync 100% canh noi, 4x 2.5D, 82 L3 FX) |
| 5. Tôn trọng nạn nhân, không kỳ thị vùng miền / dân tộc / nghề nghiệp / tuổi tác | ✅ PASS | Người duyệt: Chu kenh. Duyet Staging v6-level3-full-abc (24 blink, 22 mouth_sync 100% canh noi, 4x 2.5D, 82 L3 FX) |
| 6. Âm thanh: thoại rõ, master đúng chuẩn, đã nghe duyệt | ✅ PASS | Master peak -2.57 dBFS / 463.61s; thoại vừa cửa sổ: True; đã nghe duyệt: True |
| 7. Safe Zone (16:9) + Disclaimer + Thẻ Dấu hiệu nhận biết | ✅ PASS | Overlay trong Safe Zone: True; disclaimer: 1; thẻ dấu hiệu: 5 ý |
| 8. Nhịp & Hook | ✅ PASS | Hook bắt đầu 0.4s; thời lượng 463.61s (file 463.60s) |

## KIỂM DUYỆT CHUYỂN ĐỘNG HÌNH ẢNH — VISUAL MOTION QC (LEVEL3)
*Phân bổ thực thi: **Level A = 4 · Level B = 4 · Level C = 18 · Level D = 0** · Profile: `dual16gb_cpu_l480` · Chuẩn đối chiếu: [VISUAL_MOTION_HARNESS.md](../../../00_HARNESS_GUIDELINES/VISUAL_MOTION_HARNESS.md)*

- [x] Motion có phục vụ câu chuyện không?
- [x] Có cảnh nào bị zoom/pan lặp lại quá máy móc không? *(Tự động: Không có chuỗi ≥ 3 cảnh zoom-in liên tiếp)*
- [x] Có ít nhất một vài visual highlight đáng nhớ nếu nguồn hình phù hợp không? *(Tự động: Level B=4, Level C=18, Level D=0)*
- [x] 2.5D có tạo chiều sâu tự nhiên, không méo hình không? *(Level B: 4 cảnh · Breathing: 7 lớp)*
- [x] Object motion & Living-Character (`eye_blink`=24, `mouth_sync`=22) có đúng nội dung, đúng giọng nhân vật nói và không lộ viền màu da không? *(Level C: 18 cảnh · không đổi text/UI/số tiền)*
- [x] Có chi tiết AI bị biến dạng không? *(Level D: 0 cảnh)*
- [x] Motion có gây distraction khỏi voice-over không? *(Số cảnh shake: 2)*
- [x] Có giữ được continuity giữa các cảnh không?
- [x] Có sound effect nào không cần thiết không? *(Tự động: Khớp foley: 27 · Chưa có foley gần mốc: 0)*
- [x] Render có smooth, không flicker, không jump frame, không lỗi layer hoặc mask không?
- [x] Các cảnh không phù hợp motion nâng cao có được giữ xử lý đơn giản không? *(Tự động: Không có cảnh fallback lỗi)*

**Ghi nhận tự động từ Engine:**
- Không có cảnh báo motion tự động.

> **Nguyên tắc kế thừa & hạ cấp:** Level 3 bắt buộc kế thừa đủ Level 1 + Level 2 (không nhảy cóc bỏ chép miệng / chớp mắt / 2.5D). Nếu bất kỳ hiệu ứng nào không đạt chất lượng, hãy sửa tài nguyên hoặc hạ cấp có lý do rõ ràng — tuyệt đối không lờ đi.
>
> Mục ⏳ cần bạn xem video rồi ký duyệt trong `clearance/human_qa_signoff.json`
> (`python factory196/_engine/run.py signoff EP07 --point 2 4 5 --by "<tên>"`), sau đó chạy lại Gate 5 với `--skip-render`.
