# BIÊN BẢN KIỂM DUYỆT GATE 5 [factory196 · 16:9] – EP08b: Tiền nổi rồi, tên lại khác

- Video staging: [EP08b_TienNoiRoiTenLaiKhac_260s_staging.mp4](file:///C:/projects/socialScamStories/factory196/staging/EP08b/EP08b_TienNoiRoiTenLaiKhac_260s_staging.mp4) (100.9 MB)
- Trạng thái: ❌ **CHƯA ĐẠT** – xem các mục chưa PASS

| Tiêu chí | Trạng thái | Bằng chứng |
| :--- | :---: | :--- |
| 1. Không định danh người / tổ chức / số thật | ✅ PASS | Cấm cứng: 0; cảnh báo: 0; SĐT: 0; URL: 0; dãy số TK: 0 |
| 2. Không hướng dẫn thủ đoạn chi tiết (chỉ bóc trần cơ chế tâm lý & dấu hiệu) | ⏳ CHỜ NGƯỜI DUYỆT | Người duyệt: —. |
| 3. Sạch từ khóa thuật toán (ASR/OCR/metadata) | ✅ PASS | Cấm cứng: 0; cảnh báo: 0 |
| 4. Hình ảnh & chuyển động an toàn: không logo/giao diện/sắc phục thật, không máu me, motion mượt đúng nhịp & giữ continuity (QC 11 điểm) | ⏳ CHỜ NGƯỜI DUYỆT | Người duyệt: —. |
| 5. Tôn trọng nạn nhân, không kỳ thị vùng miền / dân tộc / nghề nghiệp / tuổi tác | ⏳ CHỜ NGƯỜI DUYỆT | Người duyệt: —. |
| 6. Âm thanh: thoại rõ, master đúng chuẩn, đã nghe duyệt | ⏳ CHỜ NGƯỜI DUYỆT | Master peak -2.0 dBFS / 260.13s; thoại vừa cửa sổ: True; đã nghe duyệt: False |
| 7. Safe Zone (16:9) + Disclaimer + Thẻ Dấu hiệu nhận biết | ✅ PASS | Overlay trong Safe Zone: True; disclaimer: 1; thẻ dấu hiệu: 5 ý |
| 8. Nhịp & Hook | ✅ PASS | Hook bắt đầu 0.4s; thời lượng 260.13s (file 260.13s) |

## KIỂM DUYỆT CHUYỂN ĐỘNG HÌNH ẢNH — VISUAL MOTION QC (LEVEL 2)
*Phân bổ thực thi: **Level A = 5 · Level B = 4 · Level C = 14 · Level D = 0** · Chuẩn đối chiếu: [VISUAL_MOTION_HARNESS.md](../../../00_HARNESS_GUIDELINES/VISUAL_MOTION_HARNESS.md)*

- [ ] Motion có phục vụ câu chuyện không?
- [ ] Có cảnh nào bị zoom/pan lặp lại quá máy móc không? *(Tự động: Không có chuỗi ≥ 3 cảnh zoom-in liên tiếp)*
- [ ] Có ít nhất một vài visual highlight đáng nhớ nếu nguồn hình phù hợp không? *(Tự động: Level B=4, Level C=14, Level D=0)*
- [ ] 2.5D có tạo chiều sâu tự nhiên, không méo hình không? *(Level B: 4 cảnh)*
- [ ] Object motion có đúng nội dung và timing không? *(Level C: 14 cảnh · không đổi text/UI/số tiền)*
- [ ] Có chi tiết AI bị biến dạng không? *(Level D: 0 cảnh)*
- [ ] Motion có gây distraction khỏi voice-over không? *(Số cảnh shake: 6)*
- [ ] Có giữ được continuity giữa các cảnh không?
- [ ] Có sound effect nào không cần thiết không? *(Tự động: Khớp foley: 24 · Chưa có foley gần mốc: 0)*
- [ ] Render có smooth, không flicker, không jump frame, không lỗi layer hoặc mask không?
- [ ] Các cảnh không phù hợp motion nâng cao có được giữ xử lý đơn giản không? *(Tự động: Không có cảnh fallback lỗi)*

**Ghi nhận tự động từ Engine:**
- Không có cảnh báo motion tự động.

> **Nguyên tắc hạ cấp:** Nếu bất kỳ hiệu ứng nào không đạt chất lượng, hãy hạ cấp hoặc loại bỏ nó (`video_enabled: false` hoặc chuyển về Level A). Cảnh tĩnh sạch sẽ luôn tốt hơn cảnh chuyển động lỗi.
>
> Mục ⏳ cần bạn xem video rồi ký duyệt trong `clearance/human_qa_signoff.json`
> (`python factory196/_engine/run.py signoff EP08b --point 2 4 5 --by "<tên>"`), sau đó chạy lại Gate 5 với `--skip-render`.
