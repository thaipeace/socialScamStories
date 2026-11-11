# VẠN CHUYỆN · BÓC TRẦN LỪA ĐẢO – TỪ ONLINE ĐẾN OFFLINE

> **Tầm nhìn**: Kênh phim hoạt hình ngắn 9:16 (~70 giây) dựng lại các chiêu lừa đảo điển hình, mỗi tập kết bằng thẻ **DẤU HIỆU NHẬN BIẾT** và **VIỆC NÊN LÀM**.
> **Phương châm**: *Xem để không bị lừa* – kịch tính để giữ chân, dấu hiệu để mang về.
> **Hạ tầng**: Kế thừa kiến trúc 3 tầng × 6 Gate từ dự án `borderWarSW779`, viết lại thành **engine dùng chung** điều khiển bằng `episode.json`.

---

## ĐỌC THEO THỨ TỰ
0. [Sổ Ràng buộc & Rủi ro](CONSTRAINTS_AND_RISK_REGISTER.md) – đọc đầu tiên
1. [Channel Bible – định hướng kênh](CHANNEL_BIBLE.md)
2. [Harness Pháp lý & An toàn nội dung](00_HARNESS_GUIDELINES/CONTENT_LEGAL_SAFETY_HARNESS.md) – 5 nguyên tắc vàng
3. [Quy chuẩn định dạng Short 70s (`factory619`)](00_HARNESS_GUIDELINES/SHORT_FORMAT_SPEC.md) · [Quy chuẩn định dạng Phim dài 16:9 4–5+ phút (`factory196`)](00_HARNESS_GUIDELINES/LONG_FORMAT_196_SPEC.md)
4. [Hình tượng nhân vật & phong cách hình ảnh](00_HARNESS_GUIDELINES/CAST_AND_VISUAL_STYLE.md) · [cast.json](02_CAST/cast.json)
5. [Harness quy trình sản xuất (Gate 0 → 6)](00_HARNESS_GUIDELINES/EPISODE_PRODUCTION_HARNESS.md)
6. [Bản đồ chiêu trò online → offline](01_SCAM_MAP/SCAM_MAP_ONLINE_TO_OFFLINE.md) · [Kho kịch bản & Lịch phát sóng Tháng 11](01_SCAM_MAP/KHO_KICH_BAN_THANG_11.md)
7. [Bộ từ cấm / cảnh báo tự động](00_HARNESS_GUIDELINES/policy_wordlists.json)

## CẤU TRÚC HAI NHÀ MÁY (`factory196` & `factory619`) + SERVICE DÙNG CHUNG (`03_ENGINE`)
```
00_HARNESS_GUIDELINES/   Harness pháp lý, định dạng Short & Long-form, nhân vật, quy trình, policy_wordlists.json
01_SCAM_MAP/             Bản đồ nhóm chiêu trò (chọn đề tài)
02_CAST/cast.json        Giọng TTS cố định cho các hình tượng nhân vật (dùng chung cả 2 nhà máy)
03_ENGINE/               ENGINE SERVICE DÙNG CHUNG (core, dsp, sfx_library, gate2..gate6, cli.py)
factory196/              NHÀ MÁY PHIM DÀI NGANG 16:9 (1920x1080, thời lượng linh hoạt 4–5+ phút / ≥ 240s)
  _engine/               Chỉ chứa channel_config.json (16:9) + run.py (wrapper 14 dòng gọi 03_ENGINE)
  _templates/EPISODE/    Mẫu một tập phim dài 5 Hồi (240s+): episode.json, script/, clearance/, IMAGE_PROMPTS.md
  materialAndDraft/<EP>/ Tầng 1 – Gate 0–3
  staging/<EP>/          Tầng 2 – Gate 4–5
  production/<EP>/       Tầng 3 – Gate 6
factory619/              NHÀ MÁY VIDEO NGẮN DỌC 9:16 (1080x1920, Shorts/Reels/TikTok ~55–70s)
  _engine/               Chỉ chứa channel_config.json (9:16) + run.py (wrapper 14 dòng gọi 03_ENGINE)
  _templates/EPISODE/    Mẫu một tập Short: episode.json, script/, clearance/, IMAGE_PROMPTS.md
  materialAndDraft/<EP>/ Tầng 1 – Gate 0–3
  staging/<EP>/          Tầng 2 – Gate 4–5
  production/<EP>/       Tầng 3 – Gate 6
06_RENDERED_VIDEOS/      Bản sao các master phim dài 16:9 đã phát hành
06_RENDERED_SHORTS/      Bản sao các master Short 9:16 đã phát hành
```

## QUY TẮC VẬN HÀNH BẮT BUỘC & CHỐNG LẶP LỖI (USER MANDATES)
1. **Luôn làm Staging trước – chờ duyệt mới lên Production:** Mọi tập chỉ chạy đến **Gate 5 (`factory/staging/<EP>/*_staging.mp4`)** để chủ kênh xem và nghe duyệt. **Tuyệt đối không chạy Gate 6 (`production/`)** trước khi chủ kênh xác nhận duyệt bản Staging.
2. **Giọng nhân vật đồng nhất 100% & tự nhiên tuyệt đối:**
   - Mỗi nhân vật khóa cố định `model` + `voice` + `style` + `af` trong [`02_CAST/cast.json`](02_CAST/cast.json) (không để fallback đổi model giữa chừng cho cùng 1 nhân vật).
   - **CẤM dùng `asetrate` / `atempo`** làm méo tốc độ và cao độ (do WAV gốc từ Gemini TTS là `24000 Hz`).
   - **CẤM nối gộp câu bằng `" ... ... "`** rồi cắt tự động; phải thu độc lập từng câu và nghe kiểm tra trực tiếp từng file `.mp3` sau Gate 2.
3. **Mạch chuyện tự nhiên như phim, không làm kiểu "bài giáo án":** Không dùng hộp đen `callouts` giữa phim; phụ đề là chữ viền điện ảnh trong suốt (boxless outline); thời lượng gọn (~55–58s), kết nhanh dứt khoát.
4. **Logic không gian & hướng nhìn nhân vật chuẩn xác:** Cảnh đối đầu/giải cứu phải bố cục cắt ngang Trái – Phải rõ ràng (người bảo vệ đứng ngay cổng đón nạn nhân và quay mặt nhìn nghi ngờ thẳng về phía kẻ gian); kẻ dụ dỗ có vẻ ngoài hiền lành, lịch sự.
5. **Chuẩn riêng cho Phim dài 16:9 (`factory196`, 4–5+ phút / `≥ 240s`):** Giữ tỷ lệ `~80%` kịch đời sống xoay quanh 1 nhân vật chính có chiều sâu đời tư / `~20%` sơ đồ & Người Bóc Trần; phản biện đa chiều pháp lý & logic trước khi dựng; lời thoại ngắn gọn (`≤ 26 từ/câu`, `~120–140 từ/phút`); phân tách rõ âm sắc các giọng cùng giới tính; cắt cảnh lên hình trước giọng nói (`0.25–0.4s`) và căn lại timeline theo độ dài WAV thật sau Gate 2.

## BẮT ĐẦU NHANH
```powershell
cd c:\projects\socialScamStories

# --- NHÀ MÁY 196: PHIM DÀI 16:9 (4–5+ PHÚT / ≥ 240s) ---
python factory196/_engine/run.py new EP01 --slug HoSoLuaDao --title "Tên tập phim dài" --duration 270
python factory196/_engine/run.py gate0 EP01
python factory196/_engine/run.py gate EP01 2 --placeholder
python factory196/_engine/run.py gate EP01 4 --preview
python factory196/_engine/run.py all EP01
python factory196/_engine/run.py presets

# --- NHÀ MÁY 619: VIDEO SHORT 9:16 (~55-70s) ---
python factory619/_engine/run.py new EP01 --slug TenTapShort --title "Tên tập Short"
python factory619/_engine/run.py gate0 EP01
python factory619/_engine/run.py all EP01
```

**Yêu cầu**: Python 3.10+, `numpy`, `Pillow`, FFmpeg (tự dùng `C:\projects\HaizFlow-main\runtime\bin` nếu có), Gemini API key (biến `GEMINI_API_KEY` hoặc file keys của HaizFlow).

