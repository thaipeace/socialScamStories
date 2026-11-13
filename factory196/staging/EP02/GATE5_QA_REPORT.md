# BIÊN BẢN KIỂM DUYỆT GATE 5 [factory196 · 16:9] – EP02: Chữ ma – 80 triệu và một cú click

- Video staging: [EP02_ChuMa80TrieuVaMotCuClick_259s_staging.mp4](file:///C:/projects/socialScamStories/factory196/staging/EP02/EP02_ChuMa80TrieuVaMotCuClick_259s_staging.mp4) (102.35 MB)
- Trạng thái: ✅ **ĐẠT 8/8 – được chuyển Gate 6**

| Tiêu chí | Trạng thái | Bằng chứng |
| :--- | :---: | :--- |
| 1. Không định danh người / tổ chức / số thật | ✅ PASS | Cấm cứng: 0; cảnh báo: ['bệnh viện']; SĐT: 0; URL: 0; dãy số TK: 0 |
| 2. Không hướng dẫn thủ đoạn chi tiết (chỉ bóc trần cơ chế tâm lý & dấu hiệu) | ✅ PASS | Người duyệt: Chủ kênh. Chủ kênh duyệt staging lên production |
| 3. Sạch từ khóa thuật toán (ASR/OCR/metadata) | ✅ PASS | Cấm cứng: 0; cảnh báo: 0 |
| 4. Hình ảnh an toàn: không máu me/khỏa thân, không logo – giao diện – sắc phục thật | ✅ PASS | Người duyệt: Chủ kênh. Chủ kênh duyệt staging lên production |
| 5. Tôn trọng nạn nhân, không kỳ thị vùng miền / dân tộc / nghề nghiệp / tuổi tác | ✅ PASS | Người duyệt: Chủ kênh. Chủ kênh duyệt staging lên production |
| 6. Âm thanh: thoại rõ, master đúng chuẩn, đã nghe duyệt | ✅ PASS | Master peak -1.75 dBFS / 259.0s; thoại vừa cửa sổ: True; đã nghe duyệt: True |
| 7. Safe Zone (16:9) + Disclaimer + Thẻ Dấu hiệu nhận biết | ✅ PASS | Overlay trong Safe Zone: True; disclaimer: 1; thẻ dấu hiệu: 3 ý |
| 8. Nhịp & Hook | ✅ PASS | Hook bắt đầu 0.4s; thời lượng 259.0s (file 259.00s) |

> Mục ⏳ cần bạn xem video rồi ký duyệt trong `clearance/human_qa_signoff.json`
> (`python factory196/_engine/run.py signoff EP02`), sau đó chạy lại Gate 5 với `--skip-render`.
