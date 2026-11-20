# PHIẾU THỰC THI (16:9 LONG-FORM 4–5 PHÚT) – EP08: Một vòng tiền, hai nửa sự thật

Lệnh chạy từ thư mục gốc dự án (`socialScamStories`).

| Gate | Việc | Lệnh | Xong |
| :-: | :--- | :--- | :-: |
| 0 | Kịch bản 4–5 phút (`~265s–285s` giọng thật ≥ 240s, nhịp ngắn gọn) + Clearance ĐẠT + `source/build_draft.py` → `episode.json` *(chờ sinh đủ ảnh `c00..c15.jpg` khi lên Staging)* | `python3 factory196/materialAndDraft/EP08/source/build_draft.py` rồi `python3 factory196/_engine/run.py gate0 EP08` | ⏳ Đã xong kịch bản v2 & `episode.json` Tầng 1 |
| 1 | Sinh & duyệt ảnh 16:9 (16 ảnh `c00..c15.jpg` `1920x1080`, Đạt & Khang cạo râu nhẵn xuyên suốt, khóa 2 ly cà phê đá ở `c02/c13/c14`, phòng tối 2 người ẩn mặt 100% ở `c03`, cú gọi hình giật ở `c04`, không viền letterbox, không chữ/logo/URL/thương hiệu) | Kiểm tra trực quan từng ảnh & khung `preview_frames/*_safezone.jpg` | ☐ |
| 2 | Sinh giọng thật (`35/35` câu `gemini-3.8-flash-tts`, 7 tuyến nhân vật = 7 voice tách biệt, riêng `l12_dat_fake` dùng đúng voice Anh Đạt + `phone` cho cú gọi ghép 3 giây) + chạy lại `build_draft.py` căn timeline theo WAV thật + nghe rà soát cả 35 file `.mp3` | `python3 factory196/_engine/run.py gate EP08 2` | ☐ |
| 3 | SFX/BGM + master | `python3 factory196/_engine/run.py gate EP08 3` | ☐ |
| 4 | Timeline `1920x1080 @ 30fps` + Chapter cards + Boxless Subtitle + Safe Zone QA | `python3 factory196/_engine/run.py gate EP08 4` | ☐ |
| 5 | Render staging + QA 8 điểm → **DỪNG CHỜ CHỦ KÊNH DUYỆT STAGING** | `python3 factory196/_engine/run.py gate EP08 5` | ☐ |
| 6 | Đóng gói phát hành (chỉ chạy sau khi chủ kênh duyệt Staging) | `python3 factory196/_engine/run.py signoff EP08 --listen PASS --point 2 4 5 --by "Chủ kênh"` → `... gate EP08 5 --skip-render` → `... gate EP08 6` | ☐ |

Ghi chú vòng sửa:
- **20/11/2026 – v1-draft:** Khởi tạo trọn bộ hồ sơ Tầng 1 `factory196/EP08` (*Một vòng tiền, hai nửa sự thật*).
- **20/11/2026 – v2-draft:** (1) Bỏ sạch 2 bong bóng giải thích dài ở `s03`, thay bằng 4 câu đối thoại trực tiếp giữa Kẻ đứng giữa và Đàn em kỹ thuật để người xem nghe là hiểu ngay; (2) Bổ sung cảnh `s04_fake_video_call` nhá cuộc gọi hình/giọng ghép 3 giây đổ mạng yếu để tăng độ thuyết phục cho nick mới; (3) Cài – nhái – trả trọn vẹn phong cách nói chuyện đặc trưng của Anh Đạt (*"cu Khang"*, *"chị nhà"*, *"lộ bài"*, *"làm gọn giùm anh, anh tính"*).
