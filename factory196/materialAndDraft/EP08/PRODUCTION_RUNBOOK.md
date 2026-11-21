# PHIẾU THỰC THI (16:9 LONG-FORM 4–5 PHÚT) – EP08: Một vòng tiền, hai nửa sự thật

Lệnh chạy từ thư mục gốc dự án (`socialScamStories`).

| Gate | Việc | Lệnh | Xong |
| :-: | :--- | :--- | :-: |
| 0 | Kịch bản v3 đã căn theo WAV thật (`242.2s = 04:02`, `19 cảnh`, `32 câu`, `626 từ`, `155 từ/phút`) + Clearance `ĐẠT` + đủ 17 ảnh `c00..c13, c14a, c14b, c15.jpg` `1920x1080` | `python factory196/materialAndDraft/EP08/source/build_draft.py` rồi `python factory196/_engine/run.py gate0 EP08` | ☑ |
| 1 | Sinh & duyệt ảnh 16:9 (17 ảnh `c00..c13, c14a, c14b, c15.jpg` `1920x1080`, Đạt & Khang cạo râu nhẵn xuyên suốt, `c06` ngồi tại bàn cười tủm tỉm không nón bảo hiểm, khóa 2 ly cà phê đá ở `c02/c13/c14b`, cặp góc cận đối đầu OTS lạnh ở `c14a/c14b`, phòng tối 2 người ẩn mặt 100% ở `c03`, cú gọi hình giật ở `c04`, không viền letterbox, không chữ/logo/URL/thương hiệu) | Đã kiểm tra trực quan 17/17 ảnh & 22 khung `preview_frames/*_safezone.jpg` | ☑ |
| 2 | Sinh giọng thật (`32/32` câu `PASS`, 100% `gemini-3.8-flash-tts`, 7 tuyến nhân vật = 7 voice tách biệt, riêng `l12_dat_fake` dùng đúng voice Anh Đạt + `phone` cho cú gọi ghép 3 giây) + căn timeline theo WAV thật + đã nghe rà soát trực tiếp 32/32 file `.mp3` | `python factory196/_engine/run.py gate EP08 2` | ☑ |
| 3 | SFX/BGM + master (`242.15s · peak -1.42 dBFS · rms -20.32 dBFS`) | `python factory196/_engine/run.py gate EP08 3` | ☑ |
| 4 | Timeline `1920x1080 @ 30fps` (`7.264 frames`) + Chapter cards + Boxless Subtitle + `22` khung Safe Zone QA | `python factory196/_engine/run.py gate EP08 4` | ☑ |
| 5 | Render staging (`EP08_MotVongTienHaiNuaSuThat_242s_staging.mp4`, `92.97 MB`) + QA 8 điểm (**tất cả mục tự động PASS, đang chờ Chủ kênh duyệt Staging**) | `python factory196/_engine/run.py gate EP08 5` | ⏳ Chờ duyệt Staging |
| 6 | Đóng gói phát hành (chỉ chạy sau khi chủ kênh duyệt Staging) | `python factory196/_engine/run.py signoff EP08 --listen PASS --point 2 4 5 --by "Chủ kênh"` → `... gate EP08 5 --skip-render` → `... gate EP08 6` | ☐ |

Ghi chú vòng sửa:
- **20/11/2026 – v1-draft:** Khởi tạo trọn bộ hồ sơ Tầng 1 `factory196/EP08` (*Một vòng tiền, hai nửa sự thật*).
- **20/11/2026 – v2-draft:** (1) Bỏ sạch 2 bong bóng giải thích dài ở `s03`, thay bằng 4 câu đối thoại trực tiếp giữa Kẻ đứng giữa và Đàn em kỹ thuật để người xem nghe là hiểu ngay; (2) Bổ sung cảnh `s04_fake_video_call` nhá cuộc gọi hình/giọng ghép 3 giây đổ mạng yếu để tăng độ thuyết phục cho nick mới; (3) Cài – nhái – trả trọn vẹn phong cách nói chuyện đặc trưng của Anh Đạt (*"cu Khang"*, *"chị nhà"*, *"lộ bài"*, *"làm gọn giùm anh, anh tính"*).
- **21/11/2026 – Staging Gate 5 (v2 → v3):** (1) Thu gọn `s03` phòng tối xuống 2 câu ám hiệu gọn sắc (*"nhớ gọi nhá nó một cái rồi mới nhắn. Đánh vòng qua thằng Khang cho gọn."*), bỏ diễn giải 3s/mạng yếu; (2) Sinh lại `c06.jpg` Khang ngồi ngay tại bàn ôm điện thoại cười tủm tỉm (bỏ nón bảo hiểm/"đi đâu"), rút gọn thoại với Hân tự nhiên không lặp thông tin; (3) Ngắt cú lật rạn nứt lòng tin ra **SAU thẻ `NHỚ KỸ`** (chuẩn EP05–EP07) với cặp cận over-the-shoulder bóng lạnh `c14a.jpg`/`c14b.jpg` và cặp thoại sắc lạnh *"À Khang… gửi anh giữ làm bằng"* ↔ *"Được anh… gửi em giữ làm bằng luôn đi"* → `impact` + cắt đen đột ngột. Bản Staging `v3` (`242.13s`, `92.97 MB`) đang chờ Chủ kênh duyệt trước khi chạy Gate 6.
