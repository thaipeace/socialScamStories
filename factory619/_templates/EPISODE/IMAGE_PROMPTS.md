# PROMPT ẢNH PHÂN CẢNH – {{EP}}

Quy chuẩn chung (dán vào đầu mọi prompt), xem [CAST_AND_VISUAL_STYLE.md](../../../00_HARNESS_GUIDELINES/CAST_AND_VISUAL_STYLE.md):

```text
Vertical 9:16 (1080x1920), semi-realistic cinematic 2D anime illustration, contemporary Vietnam setting,
moody cinematic lighting, no text, no letters, no logos, no brand names, no real app interface,
no real police/bank uniforms or insignia, no blood, no gore.
```

| Scene | Nhịp | Motion Level & Chuẩn bị lớp/chi tiết (A/B/C/D) | Prompt riêng | Ghi chú nhân vật / đạo cụ | Duyệt |
| :-: | :--- | :--- | :--- | :--- | :-: |
| 1 | Hook | `A` (`slow_push_in`) | | | ☐ |
| 2 | Mồi nhử | `C` (`screen_glow` / `detail_reveal` màn hình) | | Chừa vùng màn hình rõ để gắn ánh sáng/tin nhắn | ☐ |
| 3 | Leo thang | `A` hoặc `B` (tách BG/Subject/FG nếu có chiều sâu) | | | ☐ |
| 4 | Cú chốt | `A` (`slow_pull_out`) hoặc `D` (clip ngắn tùy chọn) | | | ☐ |
| 5 | Bóc trần | `C` (`focus_highlight`) | (kẻ lừa: bóng tối/ánh màn hình, KHÔNG lộ mặt rõ) | | ☐ |
| 6 | Nền thẻ dấu hiệu | `A` (`static_hold`, không rung) | ảnh dịu, ít chi tiết | | ☐ |

Ảnh duyệt xong lưu `assets/scene1.jpg … scene6.jpg`.
- **Living-Character A/B/C chọn lọc (mặc định cho 2–4 cảnh cận rõ mặt):** tạo thêm biến thể khóa khung `assets/sceneX_blink.jpg` (chớp mắt), và với cảnh cận có thoại trực diện tạo thêm `assets/sceneX_mouth_closed.jpg`, `assets/sceneX_mouth_open.jpg` (xử lý căn pixel + cân màu da qua `03_ENGINE/face_roi_prep.py` và duyệt bảng QC cận mặt trước khi render).
- **Level B (2.5D + Breathing):** lưu thêm `assets/sX_bg.jpg`, `assets/sX_fg.png` (có thể gắn `breathe_y`/`breathe_period` và khóa `eye_blink` theo `layer: "fg"`).
- **Level C (`detail_reveal`):** lưu thêm ảnh đồng khung `assets/sX_b.jpg`. **Level D:** luôn giữ ảnh gốc `sceneX.jpg` bên cạnh clip `.mp4` để hạ cấp an toàn nếu cần.

