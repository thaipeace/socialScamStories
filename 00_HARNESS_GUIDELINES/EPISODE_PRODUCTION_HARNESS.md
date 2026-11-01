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

## II. CÁC CỔNG

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
