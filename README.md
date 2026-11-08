# VẠN CHUYỆN · BÓC TRẦN LỪA ĐẢO – TỪ ONLINE ĐẾN OFFLINE

> **Tầm nhìn**: Kênh phim hoạt hình ngắn 9:16 (~70 giây) dựng lại các chiêu lừa đảo điển hình, mỗi tập kết bằng thẻ **DẤU HIỆU NHẬN BIẾT** và **VIỆC NÊN LÀM**.
> **Phương châm**: *Xem để không bị lừa* – kịch tính để giữ chân, dấu hiệu để mang về.
> **Hạ tầng**: Kế thừa kiến trúc 3 tầng × 6 Gate từ dự án `borderWarSW779`, viết lại thành **engine dùng chung** điều khiển bằng `episode.json`.

---

## ĐỌC THEO THỨ TỰ
0. [Sổ Ràng buộc & Rủi ro](CONSTRAINTS_AND_RISK_REGISTER.md) – đọc đầu tiên
1. [Channel Bible – định hướng kênh](CHANNEL_BIBLE.md)
2. [Harness Pháp lý & An toàn nội dung](00_HARNESS_GUIDELINES/CONTENT_LEGAL_SAFETY_HARNESS.md) – 5 nguyên tắc vàng
3. [Quy chuẩn định dạng Short 70s](00_HARNESS_GUIDELINES/SHORT_FORMAT_SPEC.md)
4. [Hình tượng nhân vật & phong cách hình ảnh](00_HARNESS_GUIDELINES/CAST_AND_VISUAL_STYLE.md) · [cast.json](02_CAST/cast.json)
5. [Harness quy trình sản xuất (Gate 0 → 6)](00_HARNESS_GUIDELINES/EPISODE_PRODUCTION_HARNESS.md)
6. [Bản đồ chiêu trò online → offline](01_SCAM_MAP/SCAM_MAP_ONLINE_TO_OFFLINE.md) · [Kho kịch bản & Lịch phát sóng Tháng 11](01_SCAM_MAP/KHO_KICH_BAN_THANG_11.md)
7. [Bộ từ cấm / cảnh báo tự động](00_HARNESS_GUIDELINES/policy_wordlists.json)

## CẤU TRÚC
```
00_HARNESS_GUIDELINES/   Harness pháp lý, định dạng, nhân vật, quy trình, policy_wordlists.json
01_SCAM_MAP/             Bản đồ nhóm chiêu trò (chọn đề tài)
02_CAST/cast.json        Giọng TTS cố định cho các hình tượng nhân vật
factory/
  _engine/               Engine dùng chung (core, dsp, sfx_library, gate2..gate6, run.py, channel_config.json)
  _templates/EPISODE/    Mẫu một tập: episode.json, script/, clearance/, IMAGE_PROMPTS.md, PRODUCTION_RUNBOOK.md
  materialAndDraft/<EP>/ Tầng 1 – Gate 0–3
  staging/<EP>/          Tầng 2 – Gate 4–5
  production/<EP>/       Tầng 3 – Gate 6
06_RENDERED_SHORTS/      Bản sao các master đã phát hành
```

## QUY TẮC VẬN HÀNH BẮT BUỘC & CHỐNG LẶP LỖI (USER MANDATES)
1. **Luôn làm Staging trước – chờ duyệt mới lên Production:** Mọi tập chỉ chạy đến **Gate 5 (`factory/staging/<EP>/*_staging.mp4`)** để chủ kênh xem và nghe duyệt. **Tuyệt đối không chạy Gate 6 (`production/`)** trước khi chủ kênh xác nhận duyệt bản Staging.
2. **Giọng nhân vật đồng nhất 100% & tự nhiên tuyệt đối:**
   - Mỗi nhân vật khóa cố định `model` + `voice` + `style` + `af` trong [`02_CAST/cast.json`](02_CAST/cast.json) (không để fallback đổi model giữa chừng cho cùng 1 nhân vật).
   - **CẤM dùng `asetrate` / `atempo`** làm méo tốc độ và cao độ (do WAV gốc từ Gemini TTS là `24000 Hz`).
   - **CẤM nối gộp câu bằng `" ... ... "`** rồi cắt tự động; phải thu độc lập từng câu và nghe kiểm tra trực tiếp từng file `.mp3` sau Gate 2.
3. **Mạch chuyện tự nhiên như phim, không làm kiểu "bài giáo án":** Không dùng hộp đen `callouts` giữa phim; phụ đề là chữ viền điện ảnh trong suốt (boxless outline); thời lượng gọn (~55–58s), kết nhanh dứt khoát.
4. **Logic không gian & hướng nhìn nhân vật chuẩn xác:** Cảnh đối đầu/giải cứu phải bố cục cắt ngang Trái – Phải rõ ràng (người bảo vệ đứng ngay cổng đón nạn nhân và quay mặt nhìn nghi ngờ thẳng về phía kẻ gian); kẻ dụ dỗ có vẻ ngoài hiền lành, lịch sự.

## BẮT ĐẦU NHANH
```powershell
cd c:\projects\socialScamStorys
python factory/_engine/run.py new EP01 --slug TenTap --title "Tên tập"   # tạo tập từ template
# viết script/SCRIPT.md, clearance/CLEARANCE.md, đặt ảnh assets/scene1..6.jpg, điền episode.json
python factory/_engine/run.py gate0 EP01                                  # kiểm tra đầu vào
python factory/_engine/run.py gate EP01 2 --placeholder                   # giọng giả, không tốn API
python factory/_engine/run.py gate EP01 4 --preview                       # xem nhanh khung QA
python factory/_engine/run.py all EP01                                    # Gate 2 → 5 với giọng thật
python factory/_engine/run.py signoff EP01 --listen PASS --by "Tên"
python factory/_engine/run.py signoff EP01 --point 2 4 5 --by "Tên"
python factory/_engine/run.py gate EP01 5 --skip-render
python factory/_engine/run.py gate EP01 6                                 # đóng gói phát hành
python factory/_engine/run.py presets                                     # danh sách âm thanh có sẵn
```

**Yêu cầu**: Python 3.10+, `numpy`, `Pillow`, FFmpeg (tự dùng `C:\projects\HaizFlow-main\runtime\bin` nếu có), Gemini API key (biến `GEMINI_API_KEY` hoặc file keys của HaizFlow).

