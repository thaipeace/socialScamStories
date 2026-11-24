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

Ảnh duyệt xong lưu `assets/scene1.jpg … scene6.jpg`. **BẮT BUỘC đủ tài nguyên CHECK 2 + CHECK 3 (Luật kế thừa cộng dồn `Level 3 ⊃ Level 2 ⊃ Level 1`):**
- **Living-Character 2.5 (Bắt buộc tối thiểu `eye_blink ≥ 2` và `mouth_sync ≥ 2`, khuyến nghị 2–4 cảnh cận rõ mặt):** tạo biến thể khóa khung `assets/sceneX_blink.jpg`, `assets/sceneX_mouth_closed.jpg`, `assets/sceneX_mouth_open.jpg` (tùy chọn `*_mouth_round.jpg`, `*_gaze.jpg`) → xử lý căn pixel + cân màu da qua `03_ENGINE/face_roi_prep.py` và duyệt bảng Face QC cận mặt trước khi render.
- **Level B (2.5D + Breathing + Rack Focus + Head Micro-Tilt — Bắt buộc tối thiểu `≥ 1` cảnh, khuyến nghị 1–2 cảnh):** lưu thêm `assets/sX_bg.jpg`, `assets/sX_fg.png` (gắn `breathe_y`/`breathe_period`, `blur_from/blur_to <= 8.0px`, `head_tilt_deg <= 2.2°` và khóa `eye_blink`/`mouth_sync` theo `layer: "fg"`).
- **Level C (`detail_reveal` + Level 3 FX):** lưu thêm ảnh đồng khung `assets/sX_b.jpg`; nếu dùng `split_screen` 9:16 trên–dưới (`layout: "horizontal"`) ưu tiên gắn thêm `eye_blink`/`mouth_sync` trên panel (`region_space: "source"`). **Level D:** luôn giữ ảnh gốc `sceneX.jpg` bên cạnh clip `.mp4` dựng ngoài.

