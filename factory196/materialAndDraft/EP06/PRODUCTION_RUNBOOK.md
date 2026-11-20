# PHIẾU THỰC THI (16:9 LONG-FORM 4–5+ PHÚT) – EP06: Ba triệu tám trên màn hình *(v2-draft)*

Lệnh chạy từ thư mục gốc dự án (`c:\projects\socialScamStories`).

| Gate | Việc | Lệnh | Xong |
| :-: | :--- | :--- | :-: |
| 0 | Kịch bản 4–5 phút (`242.29s` / `04:02` theo WAV thật ≥ 240s, 16 cảnh, 30 câu thoại `v2-draft`) + Clearance ĐẠT + đủ 14 ảnh `c00..c12.jpg` + `c03b.jpg` | `python factory196/materialAndDraft/EP06/source/build_draft.py` rồi `python factory196/_engine/run.py gate0 EP06` | ☑ |
| 1 | Sinh & duyệt ảnh 16:9 (14/14 ảnh `c00..c12.jpg` + `c03b.jpg` `1920x1080`, Nam cạo râu nhẵn xuyên suốt, `c09` & `c11` người bạn cũ cố ý giấu mặt 100%, `c11` màn hình danh sách trừu tượng & con trỏ rê vào nút đỏ, không viền letterbox, không chữ/logo/URL) | Kiểm tra trực quan từng ảnh & khung `preview_frames/*_safezone.jpg` | ☑ |
| 2 | Sinh giọng thật (`30/30` câu `gemini-3.8-flash-tts`, 8 tuyến nhân vật = 8 voice tách biệt) + căn timeline theo WAV thật (`242.29s`) + đã nghe rà soát cả 30 file `.mp3` (`l29_it_coda` tiếng thở dài `"Haiz…"` tự nhiên) | `python factory196/_engine/run.py gate EP06 2` | ☑ |
| 3 | SFX/BGM + master (`peak -2.74 dBFS` / `rms -20.16 dBFS` / `242.29s`) | `python factory196/_engine/run.py gate EP06 3` | ☑ |
| 4 | Timeline `1920x1080 @ 30fps` (7269 frames) + Chapter cards + Boxless Subtitle + Callout `[ CHỐT KHÁCH ]` + Safe Zone QA (`100% compliant`) | `python factory196/_engine/run.py gate EP06 4` | ☑ |
| 5 | Render staging (`EP06_BaTrieuTamTrenManHinh_242s_staging.mp4`, `97.84 MB`) + QA 8/8 PASS (Chủ kênh đã ký duyệt `human_qa_signoff.json`) | `python factory196/_engine/run.py gate EP06 5 --skip-render` | ☑ |
| 6 | Đóng gói phát hành (`EP06_BaTrieuTamTrenManHinh_242s.mp4` + `PUBLISH_PACKAGE_EP06.md` + `youtube_upload/` + bản sao `06_RENDERED_VIDEOS/`) | `python factory196/_engine/run.py gate EP06 6` | ☑ |

Ghi chú vòng sửa:
- **19/11/2026 – v1-draft:** Chuẩn hóa bản nháp `story.txt` sang trọn bộ hồ sơ Tầng 1 `factory196/EP06` (15 cảnh, 30 câu thoại ngắn gọn `≤ 25 từ`, Người Bóc Trần 1 câu `< 9s`).
- **19/11/2026 – v2-draft:** Cập nhật theo góp ý chủ kênh:
  1. Đặt tên ứng dụng hư cấu **`Bạn Thân 4.0`** kèm lời giới thiệu ngắn thuyết phục ở Hồi 1 (*mua hàng giùm cho người không có thời gian, tự nhận từ năm 2018*) + thêm cảnh **`s03b_group_buzz`** với nhóm chat mọi người báo thành quả cảm ơn rối rít.
  2. Giảm tương tác 1-1 với Điều Phối/Hỗ Trợ (Điều Phối chỉ còn 1 câu chào ở Hồi 1), đẩy tương tác hướng dẫn bù `10.000đ` và cổ vũ chốt đơn lớn ở Hồi 2 sang **nhóm chat** để các thành viên (*Chị Loan, Tuấn, Minh*) chỉ vẽ, khuyến khích; sang Hồi 3 (`s07`), giữ đúng logic đời thực: nhóm chat và hỗ trợ không tự dưng khóa chặn hay đoán Nam bỏ ngang, mà vẫn tiếp tục hối nạp nốt `2.900.000đ` trước 23h — tạo tương phản sắc nét với sao kê ngân hàng thật `-2.140.000đ`.
  3. Rút gọn mạnh thoại **Người bạn cũ** ở Hồi 4 xuống chỉ còn **2 câu / 25 từ** (*"Tên miền mới mở thứ Ba tuần trước. Biết ngay mà."* / *"Số đó tụi nó tự gõ. Bỏ ngay đi, chuyển nữa là mất nữa."*), cực kiệm lời nhưng đủ sức nặng thuyết phục ngay.
  4. Sửa **Kết mở đường dây ngầm** gọn và lạnh hơn, không lộ thêm thông tin rườm rà: bỏ cuộc gọi máy phụ, chỉ còn màn hình vi tính hiện danh sách khách, 1 câu *"Haiz… đúng là trái đất tròn."* và con trỏ chuột rê vào nút **`[ CHỐT KHÁCH ]`** → cắt đen đột ngột.
