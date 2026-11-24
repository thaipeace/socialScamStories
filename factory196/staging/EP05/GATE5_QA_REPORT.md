# BIÊN BẢN KIỂM DUYỆT GATE 5 [factory196 · 16:9] – EP05: Tờ năm trăm và sáu giây nhìn thẳng

- Video staging: [EP05_ToNamTramVaSauGiayNhinThang_262s_staging.mp4](file:///C:/projects/socialScamStories/factory196/staging/EP05/EP05_ToNamTramVaSauGiayNhinThang_262s_staging.mp4) (204.51 MB)
- Phiên bản dựng: `v4-level3-cinematic-staging` · `motion_upgrade: level3` · `sha256: 3d4511e9db50e1ca`
- Trạng thái: ❌ **CHƯA ĐẠT** – xem các mục chưa PASS

## TIẾN TRÌNH CHECK 1 → 2 → 3 (LUẬT KẾ THỪA CỘNG DỒN: `Level 3 ⊃ Level 2 ⊃ Level 1`)

| Tầng Check | Trạng thái | Thông số thực đo |
| :--- | :---: | :--- |
| **CHECK 1 — Nền Level 1** *(Cốt truyện · TTS · Safe Zone · Pháp lý)* | ✅ PASS | Điểm tự động 1, 3, 7, 8 + master âm thanh Gate 3 |
| **CHECK 2 — Kế thừa Level 2** *(2.5D + Breathing + Chớp mắt + Chép miệng)* | ❌ FAIL | `2.5D`: **0** *(≥1)* · `Breathing`: **4** *(≥1)* · `eye_blink`: **0** *(≥3)* · `mouth_sync`: **0** *(≥3; 4-state: 0)* |
| **CHECK 3 — Nâng cấp Level 3** *(Đạo diễn · Không khí · Living-Char 2.5)* | 🚫 BỊ CHẶN | `split_screen`: **1** · `RackFocus`: **0** · `HeadTilt`: **0** · `Gaze/Expr`: **0** · `L3_FX`: **38** · `L3_Trans`: **13** |

## BẢNG KIỂM DUYỆT 8 ĐIỂM GATE 5

| Tiêu chí | Trạng thái | Bằng chứng |
| :--- | :---: | :--- |
| 1. Không định danh người / tổ chức / số thật | ✅ PASS | Cấm cứng: 0; cảnh báo: 0; SĐT: 0; URL: 0; dãy số TK: 0 |
| 2. Không hướng dẫn thủ đoạn chi tiết (chỉ bóc trần cơ chế tâm lý & dấu hiệu) | ⏳ CHỜ NGƯỜI DUYỆT | Chữ ký cũ bị hủy hiệu lực (ký từ bản dựng cũ (2026-11-19T00:16) trước lần render Gate 4 mới) -> cần xem bản dựng mới & ký lại. |
| 3. Sạch từ khóa thuật toán (ASR/OCR/metadata) | ✅ PASS | Cấm cứng: 0; cảnh báo: 0 |
| 4. Hình ảnh & chuyển động an toàn: không logo/giao diện/sắc phục thật, không máu me, motion mượt đúng nhịp & giữ continuity (QC 11 điểm) | ❌ FAIL | KHÔNG ĐẠT TIẾN TRÌNH CHECK 1–2–3: [CHECK 2 · Kế thừa Level 2] Thiếu Cảnh 2.5D Parallax (Level B): hiện có 0, tối thiểu bắt buộc >= 1 (landscape). Không được nhảy cóc bỏ qua nền Level 2!; [CHECK 2 · Kế thừa Level 2] Thiếu Rig chớp mắt khóa pixel (eye_blink): hiện có 0, tối thiểu bắt buộc >= 3 (landscape). Không được nhảy cóc bỏ qua nền Level 2!; [CHECK 2 · Kế thừa Level 2] Thiếu Rig chép miệng khớp .wav thật (mouth_sync): hiện có 0, tối thiểu bắt buộc >= 3 (landscape). Không được nhảy cóc bỏ qua nền Level 2! |
| 5. Tôn trọng nạn nhân, không kỳ thị vùng miền / dân tộc / nghề nghiệp / tuổi tác | ⏳ CHỜ NGƯỜI DUYỆT | Chữ ký cũ bị hủy hiệu lực (ký từ bản dựng cũ (2026-11-19T00:16) trước lần render Gate 4 mới) -> cần xem bản dựng mới & ký lại. |
| 6. Âm thanh: thoại rõ, master đúng chuẩn, đã nghe duyệt | ✅ PASS | Master peak -2.58 dBFS / 262.08s; thoại vừa cửa sổ: True; đã nghe duyệt: True |
| 7. Safe Zone (16:9) + Disclaimer + Thẻ Dấu hiệu nhận biết | ✅ PASS | Overlay trong Safe Zone: True; disclaimer: 1; thẻ dấu hiệu: 5 ý |
| 8. Nhịp & Hook | ✅ PASS | Hook bắt đầu 0.4s; thời lượng 262.08s (file 262.07s) |

## KIỂM DUYỆT CHUYỂN ĐỘNG HÌNH ẢNH — VISUAL MOTION QC (LEVEL3)
*Phân bổ thực thi: **Level A = 3 · Level B = 0 · Level C = 14 · Level D = 0** · Profile: `dual16gb_cpu_l480` · Chuẩn đối chiếu: [VISUAL_MOTION_HARNESS.md](../../../00_HARNESS_GUIDELINES/VISUAL_MOTION_HARNESS.md)*

- [ ] Motion có phục vụ câu chuyện không?
- [ ] Có cảnh nào bị zoom/pan lặp lại quá máy móc không? *(Tự động: Không có chuỗi ≥ 3 cảnh zoom-in liên tiếp)*
- [ ] Có ít nhất một vài visual highlight đáng nhớ nếu nguồn hình phù hợp không? *(Tự động: Level B=0, Level C=14, Level D=0)*
- [ ] 2.5D có tạo chiều sâu tự nhiên, không méo hình không? *(Level B: 0 cảnh · Breathing: 4 lớp)*
- [ ] Object motion & Living-Character (`eye_blink`=0, `mouth_sync`=0) có đúng nội dung, đúng giọng nhân vật nói và không lộ viền màu da không? *(Level C: 14 cảnh · không đổi text/UI/số tiền)*
- [ ] Có chi tiết AI bị biến dạng không? *(Level D: 0 cảnh)*
- [ ] Motion có gây distraction khỏi voice-over không? *(Số cảnh shake: 2)*
- [ ] Có giữ được continuity giữa các cảnh không?
- [ ] Có sound effect nào không cần thiết không? *(Tự động: Khớp foley: 18 · Chưa có foley gần mốc: 0)*
- [ ] Render có smooth, không flicker, không jump frame, không lỗi layer hoặc mask không?
- [ ] Các cảnh không phù hợp motion nâng cao có được giữ xử lý đơn giản không? *(Tự động: Không có cảnh fallback lỗi)*

**Ghi nhận tự động từ Engine:**
- ❌ [CHECK 2 · Kế thừa Level 2] Thiếu Cảnh 2.5D Parallax (Level B): hiện có 0, tối thiểu bắt buộc >= 1 (landscape). Không được nhảy cóc bỏ qua nền Level 2!
- ❌ [CHECK 2 · Kế thừa Level 2] Thiếu Rig chớp mắt khóa pixel (eye_blink): hiện có 0, tối thiểu bắt buộc >= 3 (landscape). Không được nhảy cóc bỏ qua nền Level 2!
- ❌ [CHECK 2 · Kế thừa Level 2] Thiếu Rig chép miệng khớp .wav thật (mouth_sync): hiện có 0, tối thiểu bắt buộc >= 3 (landscape). Không được nhảy cóc bỏ qua nền Level 2!
- 🔒 **Điểm 2 (chữ ký cũ bị hủy):** ký từ bản dựng cũ (2026-11-19T00:16) trước lần render Gate 4 mới
- 🔒 **Điểm 4 (chữ ký cũ bị hủy):** ký từ bản dựng cũ (2026-11-19T00:16) trước lần render Gate 4 mới
- 🔒 **Điểm 5 (chữ ký cũ bị hủy):** ký từ bản dựng cũ (2026-11-19T00:16) trước lần render Gate 4 mới
- ⚠️ [SYNC] episode.json mới hơn source/build_draft.py (>60s) -> nhớ đồng bộ lại source/build_draft.py (Nguồn sự thật duy nhất) để tránh bị ghi đè mất nâng cấp khi sửa tập

> **Nguyên tắc kế thừa & hạ cấp:** Level 3 bắt buộc kế thừa đủ Level 1 + Level 2 (không nhảy cóc bỏ chép miệng / chớp mắt / 2.5D). Nếu bất kỳ hiệu ứng nào không đạt chất lượng, hãy sửa tài nguyên hoặc hạ cấp có lý do rõ ràng — tuyệt đối không lờ đi.
>
> Mục ⏳ cần bạn xem video rồi ký duyệt trong `clearance/human_qa_signoff.json`
> (`python factory196/_engine/run.py signoff EP05 --point 2 4 5 --by "<tên>"`), sau đó chạy lại Gate 5 với `--skip-render`.
