# HARNESS QUY TRÌNH SẢN XUẤT MỘT TẬP (EPISODE PRODUCTION HARNESS)
*Mã: HRN-PROD-SCAM-V1 · Kế thừa HRN-PROD-V6 của dự án 779, chuyển sang engine dùng chung `factory/_engine/`*

## I. KIẾN TRÚC 3 TẦNG × 7 CỔNG (giữ nguyên từ 779)

```
factory/materialAndDraft/<EP>/   ── Gate 0 (đầu vào) · Gate 1 (duyệt ảnh) · Gate 2 (TTS) · Gate 3 (âm thanh)
        │   episode.json · script/ · clearance/ · assets/ · audio/{tts,sfx,bgm,mix}/ · source/
        ▼
factory/staging/<EP>/            ── Gate 4 (timeline + overlay) · Gate 5 (render + QA 8 điểm)
        │   overlays/ · preview_frames/ · subtitles/ · *_staging.mp4 · GATE5_QA_REPORT.md
        ▼
factory/production/<EP>/         ── Gate 6 (đóng gói phát hành) → bản sao 06_RENDERED_SHORTS/
```

**Khác biệt quan trọng so với 779**
| 779 | Kênh mới |
| :--- | :--- |
| Mỗi tập copy & sửa tay 5 script Python (timestamp, câu thoại viết cứng) | **Một engine dùng chung**; mỗi tập chỉ là `episode.json` + ảnh |
| TTS `gemini-2.5-flash-preview-tts` (đã ngừng) | `gemini-3.8-flash-tts` (Interactions API), giọng cố định theo `02_CAST/cast.json` |
| SFX tổng hợp riêng cho cảnh biển đảo | Thư viện preset chủ đề lừa đảo (chuông, rung, ting ting, glitch…) + nhận file thật |
| Gate 5 tự đánh PASS cả mục cần mắt người | Mục cần người ở trạng thái **⏳ CHỜ NGƯỜI DUYỆT** đến khi ký `signoff` |
| Quét từ cấm bạo lực | Quét thêm: tên ngân hàng/app/nhà mạng, SĐT, STK, URL, từ nhạy cảm chủ đề lừa đảo |

## II. CÁC CỔNG & QUY TẮC BẮT BUỘC (MANDATORY RULES & ANTI-REGRESSION CHECKLIST)

> [!IMPORTANT]
> **7 QUY TẮC CHỐNG LẶP LỖI BẮT BUỘC CHO MỌI TẬP TIẾP THEO (ĐÚC KẾT TỪ EP01):**
>
> 1. **Làm Staging trước – Chờ duyệt mới lên Production:**
>    - Luôn dừng lại ở tầng **Staging (`Gate 5` – xuất file `factory/staging/<EP>/<EP>_*_staging.mp4`)** để chủ kênh xem và nghe duyệt trước.
>    - **Tuyệt đối KHÔNG tự ý chạy `Gate 6 (Production)`** khi chủ kênh chưa xác nhận duyệt bản Staging.
>
> 2. **Giọng nhân vật đồng nhất 100% – CẤM bẻ giọng bằng `asetrate`/`atempo` & CẤM nối gộp câu bằng `" ... ... "`:**
>    - **Lỗi đã gặp ở EP01:**
>      - File WAV thô từ Gemini TTS có sample rate **`24000 Hz`**. Dùng `asetrate=48000*1.06` làm FFmpeg đọc luồng `24000 Hz` ở `50880 Hz` (tua nhanh `2.12x` và méo tiếng chuột chipmunk).
>      - Nối gộp nhiều câu bằng `" ... ... "` rồi cắt tự động (`split_wav_by_pauses`) khiến TTS đọc thành tiếng `"ưm... ừm..."` ở đầu câu và cắt nhầm vào dấu `"..."` giữa câu thoại.
>      - Để TTS tự động fallback giữa `gemini-3.8-flash-tts` và `gemini-3.8-flash-lite-tts` trong cùng một nhân vật làm đổi âm sắc giữa các cảnh (cảnh nghe như thanh niên, cảnh nghe như trẻ con).
>    - **Quy tắc bắt buộc từ EP02:**
>      - **Tuyệt đối KHÔNG dùng `asetrate` hay `atempo`** trong `02_CAST/cast.json`. Chỉ dùng filter EQ/compressor sạch (`highpass`, `acompressor`).
>      - **Khóa cố định 1 model TTS duy nhất (`"model"` trong `cast.json`) + 1 `voice` + 1 `style` + 1 `af`** cho mỗi nhân vật xuyên suốt cả tập.
>      - **Tổng hợp từng câu độc lập** (1 request/câu), và **bắt buộc dùng công cụ nghe trực tiếp từng file `.mp3`** sau khi chạy Gate 2 để kiểm tra tốc độ, dấu thanh và độ trọn vẹn câu trước khi qua Gate 3.
>
> 3. **Mạch chuyện tự nhiên như phim hoạt hình – Không làm kiểu "bài giáo án":**
>    - Để tình huống diễn tiến bằng **hành động và lời thoại đối đáp tự nhiên** của nhân vật (kẻ dụ dỗ – nạn nhân – người giải cứu), chỉ dùng 1 câu đúc kết ngắn gọn của `nguoi_boc_tran` ở cảnh mở rộng/kết.
>    - **Không chèn các hộp chữ giải thích (`callouts`) giữa phim** làm đứt mạch cảm xúc và che tranh.
>    - Thời lượng gọn gàng (`50–58s`), kết nhanh và dứt khoát (`5s` cuối cho bảng `NHỚ KỸ` + `Disclaimer`).
>
> 4. **Phụ đề điện ảnh không nền đen (Boxless Cinematic Subtitles):**
>    - Phụ đề (`plate_subtitle` trong `gate4_timeline.py`) chỉ vẽ **chữ viền đen dày + bóng đổ nhẹ (boxless outline)**, không vẽ hộp nền đen đặc và không gắn nhãn tên nhân vật phía trên phụ đề.
>    - Thẻ `NHỚ KỸ` ở cuối tập dùng thẻ gọn bán trong suốt (`alpha <= 195`), **không phủ đen toàn màn hình** để vẫn thấy bối cảnh phía sau.
>
> 5. **Bố cục hình ảnh & Hướng nhìn nhân vật hợp logic không gian (Spatial Logic):**
>    - **Lỗi đã gặp ở EP01:** Vẽ chú bảo vệ ngồi trong phòng kín (vô lý khi cứu bé ngoài cổng), hoặc vẽ góc nhìn trực diện từ trước ra sau khiến chú bảo vệ quay lưng lại phía kẻ gian và nhìn/thổi còi vào lưng bé.
>    - **Quy tắc bắt buộc từ EP02:**
>      - Khi có cảnh đối đầu / giải cứu / nghi ngờ giữa 2 phe (ví dụ: bảo vệ đón bé và nhìn nghi ngờ kẻ gian), bắt buộc dùng **bố cục cắt ngang Trái – Phải (3/4 side view)**: Phe bảo vệ đứng bên trái quay mặt/ánh mắt nhìn thẳng sang bên phải về phía kẻ gian, tay mở rộng đón nạn nhân chạy từ phải sang trái.
>      - Bối cảnh phải có chiều sâu xã hội thực tế (cổng trường giờ tan tầm đông phụ huynh, học sinh, cây phượng, xe cộ xa xa).
>      - Kẻ lừa đảo nhóm "ngọt ngào" (`ke_ngot_ngao_nu`/`nam`) phải có **ngoại hình lịch sự, hiền lành, cười thân thiện** (không vẽ mặt dữ tợn hay bịt khẩu trang/nón đen lộ liễu), chỉ để đồng bọn rình ở góc khuất phía sau.
>
> 6. **Kiểm tra OCR chữ rác / biển số xe ở mép ảnh trước khi chạy Gate 4:**
>    - Luôn kiểm tra mép ảnh (đặc biệt đuôi xe máy ở rìa khung hình) để xóa/làm mờ mọi ký tự số ngẫu nhiên tránh bị trình quét OCR ở Gate 5 bắt nhầm.
>
> 7. **Cao trào âm nhạc & SFX đúng điểm bùng nổ (Climax Punch):**
>    - Điểm lật tình huống (twist/climax) phải có combo `riser` dẫn nhịp -> `impact` + `flash_white` + `shakes` -> nhạc nền `action_climax` đẩy gain rõ rệt và tiếng động hiện trường (`whistle`, `footsteps`).
>
> 8. **Chuẩn riêng bắt buộc cho Phim dài 16:9 `factory196` (Đúc kết từ `EP01` → `EP01b`, chi tiết tại [LONG_FORMAT_196_SPEC.md](LONG_FORMAT_196_SPEC.md)):**
>    - **Thời lượng linh hoạt `4 – 5+ phút` (`min_duration_sec = 240s`)**: Không gò ép kéo dài cho đủ 5 phút bằng lời thoại giải thích lê thê; câu thoại phải ngắn gọn, đủ ý (`≤ 26 từ/câu`, mật độ `~120–140 từ/phút`).
>    - **Kể chuyện đời sống (`~80%` kịch nhân vật / `~20%` sơ đồ & Người Bóc Trần)**: Chọn 1 nhân vật chính để khắc họa sâu đời tư, tính cách, hoàn cảnh gia đình; không biến nhân vật thành cái máy giảng nghiệp vụ/pháp luật.
>    - **Phản biện đa chiều Pháp lý & Logic trước khi dựng**: Không ép tình tiết "lừa giật một lần" vào điểm giao dịch quen cố định; không nói sai cơ chế tài chính/pháp luật (như CIC, giữ căn cước, hứa duyệt trả góp); xưng hô đúng vai vế gia đình (vợ của Anh Hai là **Chị Hai**).
>    - **Tách biệt rõ rệt giọng các nhân vật cùng giới**: Có từ 2–3 nhân vật nam/nữ trở lên thì phải gán `voice` + `style` khác hẳn nhau về âm sắc (cao sáng vs. trầm khàn vs. mượt chậm) để người nghe phân biệt được ngay.
>    - **Cảnh vào trước tiếng & Dàn timeline theo TTS thật**: Cảnh mới phải lên hình trước ít nhất `0.25–0.4s` rồi nhân vật mới cất tiếng; sau Gate 2 bắt buộc căn lại toàn bộ timeline và mốc YouTube chapters theo thời lượng WAV thật.

### GATE 0 – ĐẦU VÀO (`run.py gate0 <EP>`)
Tự kiểm: thời lượng hợp lệ · cảnh phủ kín timeline & đủ ảnh · speaker có trong cast · độ dài thoại · thẻ dấu hiệu 2–4 ý + việc nên làm · có hook · có kịch bản · `clearance/CLEARANCE.md` ghi `TRẠNG THÁI TỔNG: ĐẠT`.

### GATE 1 – DUYỆT ẢNH & CHUYỂN ĐỘNG (thủ công + preview)
1. Kiểm 5 tiêu chí trên từng ảnh: **đồng nhất nhân vật** · **không chữ/logo/giao diện app/sắc phục thật** · **bối cảnh Việt Nam đương đại** · **không máu me, khỏa thân** · **kẻ lừa không lộ mặt rõ**.
2. Chạy thử nhanh không tốn API: `run.py gate <EP> 2 --placeholder` rồi `run.py gate <EP> 4 --preview` → xem `staging/<EP>/preview_frames/*_safezone.jpg`.
3. Chỉnh `motion` / `shakes` / `transition_in` trong `episode.json` đến khi ưng.

### GATE 2 – GIỌNG THOẠI (`run.py gate <EP> 2`)
- Engine chỉ tổng hợp lại câu **có thay đổi** (text/voice/style) – tiết kiệm API.
- Bắt buộc **nghe từng câu** (dấu thanh, cảm xúc, giọng điện thoại). Đạt → `run.py signoff <EP> --listen PASS --by "<tên>"`.
- Câu vượt `window` → rút gọn thoại hoặc nới `window`.

### GATE 3 – ÂM THANH (`run.py gate <EP> 3`)
- 3 lớp: Ambience · Foley (đặt theo giây `at`) · BGM; tự ducking dưới mọi câu thoại + vùng `duck_extra`.
- Chuẩn mức: thoại −3 dBFS; master đỉnh trong −6 → −0.8 dBFS (limiter mềm kế thừa 779).

### GATE 4 – TIMELINE (`run.py gate <EP> 4`)
- Ken Burns sub-pixel, wobble, rung tắt dần, chuyển cảnh, branding, hook, phụ đề tự động, tin nhắn, callout, thẻ dấu hiệu, disclaimer.
- Kiểm Safe Zone tự động; ảnh QA tại `preview_frames/`.

### GATE 5 – RENDER & QA 8 ĐIỂM (`run.py gate <EP> 5`)
| # | Tiêu chí | Kiểm |
| :-: | :--- | :--- |
| 1 | Không định danh người/tổ chức/số thật | Tự động (WARN cần ký) |
| 2 | Không hướng dẫn thủ đoạn chi tiết | **Người duyệt** |
| 3 | Sạch từ khóa thuật toán | Tự động (WARN cần ký) |
| 4 | Hình ảnh an toàn, không logo/giao diện/sắc phục thật | **Người duyệt** |
| 5 | Tôn trọng nạn nhân, không kỳ thị | **Người duyệt** |
| 6 | Âm thanh đạt chuẩn + đã nghe duyệt (không còn giọng placeholder) | Tự động + người |
| 7 | Safe Zone + Disclaimer + Thẻ dấu hiệu | Tự động |
| 8 | Hook trước 1s, thời lượng đúng | Tự động |

Xem video staging trên **điện thoại** → `run.py signoff <EP> --point 2 4 5 --by "<tên>"` (thêm `1 3` nếu có WARN đã xem xét) → `run.py gate <EP> 5 --skip-render`.

### GATE 6 – ĐÓNG GÓI (`run.py gate <EP> 6`)
Chỉ chạy khi 8/8 PASS. Tạo master MP4, SRT, thumbnail, `release_manifest_gate6.json` (SHA-256), `PUBLISH_PACKAGE_<EP>.md` (tiêu đề, description có nhãn hư cấu + AI, bình luận ghim, checklist khai báo AI).

## III. LỊCH LÀM VIỆC GỢI Ý CHO 1 NGƯỜI (2 tập/tuần)
| Ngày | Việc |
| :--- | :--- |
| T2 | Chọn 2 chiêu từ `01_SCAM_MAP`, viết kịch bản + clearance |
| T3 | Sinh ảnh 12 cảnh, Gate 0–1 |
| T4 | Gate 2–4 cả 2 tập |
| T5 | Gate 5, xem trên điện thoại, sửa |
| T6 | Gate 6, lên lịch đăng; trả lời bình luận tập trước |

