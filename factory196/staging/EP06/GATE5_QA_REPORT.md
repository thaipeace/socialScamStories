# BIÊN BẢN KIỂM DUYỆT GATE 5 [factory196 · 16:9] – EP06: Ba triệu tám trên màn hình

- Video staging: [EP06_BaTrieuTamTrenManHinh_242s_staging.mp4](file:///C:/projects/socialScamStories/factory196/staging/EP06/EP06_BaTrieuTamTrenManHinh_242s_staging.mp4) (189.16 MB)
- Phiên bản dựng: `v3-level3-full-abc-staging` · `motion_upgrade: level3` · `sha256: 7ed856f04e01e818`
- Trạng thái: ✅ **ĐẠT 8/8 – được chuyển Gate 6**

## TIẾN TRÌNH CHECK 1 → 2 → 3 (LUẬT KẾ THỪA CỘNG DỒN: `Level 3 ⊃ Level 2 ⊃ Level 1`)

| Tầng Check | Trạng thái | Thông số thực đo |
| :--- | :---: | :--- |
| **CHECK 1 — Nền Level 1** *(Cốt truyện · TTS · Safe Zone · Pháp lý)* | ✅ PASS | Điểm tự động 1, 3, 7, 8 + master âm thanh Gate 3 |
| **CHECK 2 — Kế thừa Level 2** *(2.5D + Breathing + Chớp mắt + Chép miệng)* | ✅ PASS | `2.5D`: **4** *(≥1)* · `Breathing`: **7** *(≥1)* · `eye_blink`: **16** *(≥3)* · `mouth_sync`: **13** *(≥3; 4-state: 9)* |
| **CHECK 3 — Nâng cấp Level 3** *(Đạo diễn · Không khí · Living-Char 2.5)* | ✅ PASS | `split_screen`: **1** · `RackFocus`: **4** · `HeadTilt`: **2** · `Gaze/Expr`: **0** · `L3_FX`: **38** · `L3_Trans`: **10** |

## BẢNG KIỂM DUYỆT 8 ĐIỂM GATE 5

| Tiêu chí | Trạng thái | Bằng chứng |
| :--- | :---: | :--- |
| 1. Không định danh người / tổ chức / số thật | ✅ PASS | Cấm cứng: 0; cảnh báo: 0; SĐT: 0; URL: 0; dãy số TK: 0 |
| 2. Không hướng dẫn thủ đoạn chi tiết (chỉ bóc trần cơ chế tâm lý & dấu hiệu) | ✅ PASS | Người duyệt: ChuKenh. |
| 3. Sạch từ khóa thuật toán (ASR/OCR/metadata) | ✅ PASS | Cấm cứng: 0; cảnh báo: 0 |
| 4. Hình ảnh & chuyển động an toàn: không logo/giao diện/sắc phục thật, không máu me, motion mượt đúng nhịp & giữ continuity (QC 11 điểm) | ✅ PASS | Người duyệt: ChuKenh. |
| 5. Tôn trọng nạn nhân, không kỳ thị vùng miền / dân tộc / nghề nghiệp / tuổi tác | ✅ PASS | Người duyệt: ChuKenh. |
| 6. Âm thanh: thoại rõ, master đúng chuẩn, đã nghe duyệt | ✅ PASS | Master peak -2.74 dBFS / 242.29s; thoại vừa cửa sổ: True; đã nghe duyệt: True |
| 7. Safe Zone (16:9) + Disclaimer + Thẻ Dấu hiệu nhận biết | ✅ PASS | Overlay trong Safe Zone: True; disclaimer: 1; thẻ dấu hiệu: 5 ý |
| 8. Nhịp & Hook | ✅ PASS | Hook bắt đầu 0.4s; thời lượng 242.29s (file 242.29s) |

## KIỂM DUYỆT CHUYỂN ĐỘNG HÌNH ẢNH — VISUAL MOTION QC (LEVEL3)
*Phân bổ thực thi: **Level A = 3 · Level B = 4 · Level C = 9 · Level D = 0** · Profile: `dual16gb_cpu_l480` · Chuẩn đối chiếu: [VISUAL_MOTION_HARNESS.md](../../../00_HARNESS_GUIDELINES/VISUAL_MOTION_HARNESS.md)*

- [x] Motion có phục vụ câu chuyện không?
- [x] Có cảnh nào bị zoom/pan lặp lại quá máy móc không? *(Tự động: Không có chuỗi ≥ 3 cảnh zoom-in liên tiếp)*
- [x] Có ít nhất một vài visual highlight đáng nhớ nếu nguồn hình phù hợp không? *(Tự động: Level B=4, Level C=9, Level D=0)*
- [x] 2.5D có tạo chiều sâu tự nhiên, không méo hình không? *(Level B: 4 cảnh · Breathing: 7 lớp)*
- [x] Object motion & Living-Character (`eye_blink`=16, `mouth_sync`=13) có đúng nội dung, đúng giọng nhân vật nói và không lộ viền màu da không? *(Level C: 9 cảnh · không đổi text/UI/số tiền)*
- [x] Có chi tiết AI bị biến dạng không? *(Level D: 0 cảnh)*
- [x] Motion có gây distraction khỏi voice-over không? *(Số cảnh shake: 2)*
- [x] Có giữ được continuity giữa các cảnh không?
- [x] Có sound effect nào không cần thiết không? *(Tự động: Khớp foley: 23 · Chưa có foley gần mốc: 3)*
- [x] Render có smooth, không flicker, không jump frame, không lỗi layer hoặc mask không?
- [x] Các cảnh không phù hợp motion nâng cao có được giữ xử lý đơn giản không? *(Tự động: Không có cảnh fallback lỗi)*

**Ghi nhận tự động từ Engine:**
- Không có cảnh báo motion tự động.

> **Nguyên tắc kế thừa & hạ cấp:** Level 3 bắt buộc kế thừa đủ Level 1 + Level 2 (không nhảy cóc bỏ chép miệng / chớp mắt / 2.5D). Nếu bất kỳ hiệu ứng nào không đạt chất lượng, hãy sửa tài nguyên hoặc hạ cấp có lý do rõ ràng — tuyệt đối không lờ đi.
>
> Mục ⏳ cần bạn xem video rồi ký duyệt trong `clearance/human_qa_signoff.json`
> (`python factory196/_engine/run.py signoff EP06 --point 2 4 5 --by "<tên>"`), sau đó chạy lại Gate 5 với `--skip-render`.
