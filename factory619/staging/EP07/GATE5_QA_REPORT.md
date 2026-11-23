# BIÊN BẢN KIỂM DUYỆT GATE 5 [factory619 · 9:16] – EP07: Mạo danh Ngày hội & Đêm văn hóa – Lộ tẩy ở tên tài khoản nhận

- Video staging: [EP07_BayMuaLeHoi_52s_staging.mp4](file:///C:/projects/socialScamStories/factory619/staging/EP07/EP07_BayMuaLeHoi_52s_staging.mp4) (24.56 MB)
- Trạng thái: ✅ **ĐẠT 8/8 – được chuyển Gate 6**

| Tiêu chí | Trạng thái | Bằng chứng |
| :--- | :---: | :--- |
| 1. Không định danh người / tổ chức / số thật | ✅ PASS | Cấm cứng: 0; cảnh báo: 0; SĐT: 0; URL: 0; dãy số TK: 0 |
| 2. Không hướng dẫn thủ đoạn chi tiết (chỉ bóc trần cơ chế tâm lý & dấu hiệu) | ✅ PASS | Người duyệt: Chủ kênh. Chủ kênh duyệt staging lên production |
| 3. Sạch từ khóa thuật toán (ASR/OCR/metadata) | ✅ PASS | Cấm cứng: 0; cảnh báo: 0 |
| 4. Hình ảnh & chuyển động an toàn: không logo/giao diện/sắc phục thật, không máu me, motion mượt đúng nhịp & giữ continuity (QC 11 điểm) | ✅ PASS | Người duyệt: Chủ kênh. Đã duyệt bản Staging nâng cấp v3-level2-abc (A/B/C + 2.5D 3 lớp) |
| 5. Tôn trọng nạn nhân, không kỳ thị vùng miền / dân tộc / nghề nghiệp / tuổi tác | ✅ PASS | Người duyệt: Chủ kênh. Chủ kênh duyệt staging lên production |
| 6. Âm thanh: thoại rõ, master đúng chuẩn, đã nghe duyệt | ✅ PASS | Master peak -1.36 dBFS / 52.31s; thoại vừa cửa sổ: True; đã nghe duyệt: True |
| 7. Safe Zone (9:16) + Disclaimer + Thẻ Dấu hiệu nhận biết | ✅ PASS | Overlay trong Safe Zone: True; disclaimer: 1; thẻ dấu hiệu: 2 ý |
| 8. Nhịp & Hook | ✅ PASS | Hook bắt đầu 0.3s; thời lượng 52.31s (file 52.30s) |

## KIỂM DUYỆT CHUYỂN ĐỘNG HÌNH ẢNH — VISUAL MOTION QC (LEVEL 2)
*Phân bổ thực thi: **Level A = 1 · Level B = 2 · Level C = 3 · Level D = 0** · Chuẩn đối chiếu: [VISUAL_MOTION_HARNESS.md](../../../00_HARNESS_GUIDELINES/VISUAL_MOTION_HARNESS.md)*

- [x] Motion có phục vụ câu chuyện không?
- [x] Có cảnh nào bị zoom/pan lặp lại quá máy móc không? *(Tự động: Không có chuỗi ≥ 3 cảnh zoom-in liên tiếp)*
- [x] Có ít nhất một vài visual highlight đáng nhớ nếu nguồn hình phù hợp không? *(Tự động: Level B=2, Level C=3, Level D=0)*
- [x] 2.5D có tạo chiều sâu tự nhiên, không méo hình không? *(Level B: 2 cảnh)*
- [x] Object motion có đúng nội dung và timing không? *(Level C: 3 cảnh · không đổi text/UI/số tiền)*
- [x] Có chi tiết AI bị biến dạng không? *(Level D: 0 cảnh)*
- [x] Motion có gây distraction khỏi voice-over không? *(Số cảnh shake: 1)*
- [x] Có giữ được continuity giữa các cảnh không?
- [x] Có sound effect nào không cần thiết không? *(Tự động: Khớp foley: 4 · Chưa có foley gần mốc: 0)*
- [x] Render có smooth, không flicker, không jump frame, không lỗi layer hoặc mask không?
- [x] Các cảnh không phù hợp motion nâng cao có được giữ xử lý đơn giản không? *(Tự động: Không có cảnh fallback lỗi)*

**Ghi nhận tự động từ Engine:**
- Không có cảnh báo motion tự động.

> **Nguyên tắc hạ cấp:** Nếu bất kỳ hiệu ứng nào không đạt chất lượng, hãy hạ cấp hoặc loại bỏ nó (`video_enabled: false` hoặc chuyển về Level A). Cảnh tĩnh sạch sẽ luôn tốt hơn cảnh chuyển động lỗi.
>
> Mục ⏳ cần bạn xem video rồi ký duyệt trong `clearance/human_qa_signoff.json`
> (`python factory619/_engine/run.py signoff EP07 --point 2 4 5 --by "<tên>"`), sau đó chạy lại Gate 5 với `--skip-render`.
