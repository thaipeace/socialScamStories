# PROMPT ẢNH PHÂN CẢNH 16:9 (LONG-FORM ≥ 5 PHÚT) – {{EP}}

Quy chuẩn chung cho **nhà máy 196 (khung ngang 16:9 – 1920x1080)**, xem [CAST_AND_VISUAL_STYLE.md](../../../00_HARNESS_GUIDELINES/CAST_AND_VISUAL_STYLE.md):

```text
Horizontal 16:9 widescreen (1920x1080), semi-realistic cinematic 2D anime illustration, contemporary Vietnam setting,
widescreen cinematic composition with clear left-right spatial depth, moody cinematic lighting,
keep bottom 15% relatively clean for subtitles, no text, no letters, no numbers, no license plates,
no logos, no brand names, no real app interface, no real police/bank uniforms or insignia, no blood, no gore.
```

| Scene | Hồi / Nhịp | Thời lượng gợi ý | Motion Level & Chuẩn bị lớp/chi tiết (A/B/C/D) | Prompt riêng (16:9 Widescreen) | Ghi chú nhân vật / bố cục Trái–Phải | Duyệt |
| :-: | :--- | :---: | :--- | :--- | :--- | :-: |
| 01 | Mở màn – Hook | 00:00–00:25 | `A` (`slow_push_in`) | | | ☐ |
| 02 | Hồi 1 – Bối cảnh đời thường | 00:25–00:55 | `A` (`pan_right`) hoặc `B` (tách BG/Subject/FG) | | | ☐ |
| 03 | Hồi 1 – Kẻ lừa tiếp cận | 00:55–01:30 | `C` (`screen_glow` / `detail_reveal` màn hình) | | Chừa vùng màn hình rõ để gắn ánh sáng/thông báo | ☐ |
| 04 | Hồi 2 – Thả mồi tạo lòng tin | 01:30–02:05 | `A` (`slow_push_in`) | | | ☐ |
| 05 | Hồi 2 – Thao túng tâm lý | 02:05–02:45 | `A` (`slow_pull_out`) hoặc `B` (2.5D chiều sâu) | | | ☐ |
| 06 | Hồi 3 – Cô lập nạn nhân | 02:45–03:15 | `C` (`focus_highlight` / `cursor_click` / `light_shift`) | | | ☐ |
| 07 | Hồi 3 – Cao trào ép thời gian | 03:15–03:45 | `A` (`slow_pull_out`) hoặc `D` (clip ngắn tùy chọn) | | | ☐ |
| 08 | Hồi 4 – Cú lật / Giải cứu | 03:45–04:10 | `A` (`pan_left`) hoặc `B` (2.5D đối đầu) | | Bố cục cắt ngang Trái – Phải rõ hướng nhìn | ☐ |
| 09 | Hồi 4 – Bóc trần cơ chế | 04:10–04:40 | `A` (`slow_push_in`) | (kẻ lừa trong bóng tối/ánh màn hình, không lộ mặt rõ) | | ☐ |
| 10 | Hồi 5 – Nền thẻ dấu hiệu | 04:40–05:00+ | `A` (`static_hold`, không rung) | Ảnh bối cảnh bình yên, dịu, ít chi tiết | | ☐ |

Ảnh duyệt xong lưu `assets/scene01.jpg … scene10.jpg` (hoặc thêm `scene11..18.jpg` tùy độ dài phim).
- **Living-Character A/B/C chọn lọc (mặc định cho 3–5 cảnh cận/trung cận thoại đắt giá):** tạo thêm biến thể khóa khung `assets/sceneXX_blink.jpg` (chớp mắt), và với cảnh cận có thoại trực diện tạo thêm `assets/sceneXX_mouth_closed.jpg`, `assets/sceneXX_mouth_open.jpg` (xử lý căn pixel + cân màu da qua `03_ENGINE/face_roi_prep.py` và duyệt bảng QC cận mặt trước khi render).
- **Level B (2.5D + Breathing):** lưu thêm `assets/sXX_bg.jpg`, `assets/sXX_fg.png` (gắn `breathe_y`/`breathe_period` và khóa `eye_blink`/`mouth_sync` theo `layer` nếu phù hợp).
- **Level C (`detail_reveal`):** lưu thêm ảnh đồng khung `assets/sXX_b.jpg`. **Level D:** luôn giữ ảnh gốc `sceneXX.jpg` bên cạnh clip `.mp4` để hạ cấp an toàn nếu cần.

