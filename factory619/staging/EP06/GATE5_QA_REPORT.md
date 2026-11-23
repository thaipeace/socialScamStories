# BIÊN BẢN KIỂM DUYỆT GATE 5 [factory619 · 9:16] – EP06: Thói quen check-in du lịch thời gian thực mời trộm vào nhà

- Video staging: [EP06_CheckInDuLich_48s_staging.mp4](file:///C:/projects/socialScamStories/factory619/staging/EP06/EP06_CheckInDuLich_48s_staging.mp4) (29.68 MB)
- Trạng thái: ✅ **ĐẠT 8/8 – được chuyển Gate 6**

| Tiêu chí | Trạng thái | Bằng chứng |
| :--- | :---: | :--- |
| 1. Không định danh người / tổ chức / số thật | ✅ PASS | Cấm cứng: 0; cảnh báo: 0; SĐT: 0; URL: 0; dãy số TK: 0 |
| 2. Không hướng dẫn thủ đoạn chi tiết (chỉ bóc trần cơ chế tâm lý & dấu hiệu) | ✅ PASS | Người duyệt: Antigravity Staging Visual QA. Da kiem tra 12 anh keyframe + 6 clip 30fps va preview frames EP06 v5: mo dau tren xe xem lai anh check-in, nhip nhanh 47.62s khong cau gio, hinh anh an toan khong logo/sac phuc/bien so that |
| 3. Sạch từ khóa thuật toán (ASR/OCR/metadata) | ✅ PASS | Cấm cứng: 0; cảnh báo: 0 |
| 4. Hình ảnh & chuyển động an toàn: không logo/giao diện/sắc phục thật, không máu me, motion mượt đúng nhịp & giữ continuity (QC 11 điểm) | ✅ PASS | Người duyệt: Antigravity Visual QC (theo uỷ quyền chủ kênh). Đã soi đủ 27 mảnh mặt, 2 cảnh 2.5D (s4a/s5a), 10 khung render thực tế MP4 và thumbnail 31.93s sạch phụ đề (v6-level2-abc) |
| 5. Tôn trọng nạn nhân, không kỳ thị vùng miền / dân tộc / nghề nghiệp / tuổi tác | ✅ PASS | Người duyệt: Antigravity Staging Visual QA. Da kiem tra 12 anh keyframe + 6 clip 30fps va preview frames EP06 v5: mo dau tren xe xem lai anh check-in, nhip nhanh 47.62s khong cau gio, hinh anh an toan khong logo/sac phuc/bien so that |
| 6. Âm thanh: thoại rõ, master đúng chuẩn, đã nghe duyệt | ✅ PASS | Master peak -1.08 dBFS / 47.62s; thoại vừa cửa sổ: True; đã nghe duyệt: True |
| 7. Safe Zone (9:16) + Disclaimer + Thẻ Dấu hiệu nhận biết | ✅ PASS | Overlay trong Safe Zone: True; disclaimer: 1; thẻ dấu hiệu: 2 ý |
| 8. Nhịp & Hook | ✅ PASS | Hook bắt đầu 0.25s; thời lượng 47.62s (file 47.62s) |

## KIỂM DUYỆT CHUYỂN ĐỘNG HÌNH ẢNH — VISUAL MOTION QC (LEVEL 2)
*Phân bổ thực thi: **Level A = 2 · Level B = 2 · Level C = 8 · Level D = 0** · Chuẩn đối chiếu: [VISUAL_MOTION_HARNESS.md](../../../00_HARNESS_GUIDELINES/VISUAL_MOTION_HARNESS.md)*

- [x] Motion có phục vụ câu chuyện không?
- [x] Có cảnh nào bị zoom/pan lặp lại quá máy móc không? *(Tự động: Không có chuỗi ≥ 3 cảnh zoom-in liên tiếp)*
- [x] Có ít nhất một vài visual highlight đáng nhớ nếu nguồn hình phù hợp không? *(Tự động: Level B=2, Level C=8, Level D=0)*
- [x] 2.5D có tạo chiều sâu tự nhiên, không méo hình không? *(Level B: 2 cảnh)*
- [x] Object motion có đúng nội dung và timing không? *(Level C: 8 cảnh · không đổi text/UI/số tiền)*
- [x] Có chi tiết AI bị biến dạng không? *(Level D: 0 cảnh)*
- [x] Motion có gây distraction khỏi voice-over không? *(Số cảnh shake: 1)*
- [x] Có giữ được continuity giữa các cảnh không?
- [x] Có sound effect nào không cần thiết không? *(Tự động: Khớp foley: 3 · Chưa có foley gần mốc: 0)*
- [x] Render có smooth, không flicker, không jump frame, không lỗi layer hoặc mask không?
- [x] Các cảnh không phù hợp motion nâng cao có được giữ xử lý đơn giản không? *(Tự động: Không có cảnh fallback lỗi)*

**Ghi nhận tự động từ Engine:**
- Không có cảnh báo motion tự động.

> **Nguyên tắc hạ cấp:** Nếu bất kỳ hiệu ứng nào không đạt chất lượng, hãy hạ cấp hoặc loại bỏ nó (`video_enabled: false` hoặc chuyển về Level A). Cảnh tĩnh sạch sẽ luôn tốt hơn cảnh chuyển động lỗi.
>
> Mục ⏳ cần bạn xem video rồi ký duyệt trong `clearance/human_qa_signoff.json`
> (`python factory619/_engine/run.py signoff EP06 --point 2 4 5 --by "<tên>"`), sau đó chạy lại Gate 5 với `--skip-render`.
