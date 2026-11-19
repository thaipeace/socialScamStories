# PHIẾU THỰC THI (16:9 LONG-FORM ~6 PHÚT) – EP07: Sau hai trăm triệu

Lệnh chạy từ thư mục gốc dự án (`socialScamStories`).

| Gate | Việc | Lệnh | Xong |
| :-: | :--- | :--- | :-: |
| 0 | Kịch bản v2 (ước tính `444.7s`, giọng thật dự kiến ~5:45–6:30) + **Clearance đang CHỜ DUYỆT (cần người duyệt)** + `source/build_draft.py` → `episode.json` *(chờ sinh đủ ảnh `c00..c20.jpg` khi lên Staging)* | `python factory196/materialAndDraft/EP07/source/build_draft.py` rồi `python factory196/_engine/run.py gate0 EP07` | ⏳ Chờ người duyệt Clearance |
| 1 | Sinh & duyệt ảnh 16:9 (21 ảnh `c00..c20.jpg` `1920x1080`: Hùng cạo râu nhẵn, **đồng hồ thép trên cổ tay trái ở `c02–c10`, tháo ở `c11`, cổ tay trống trơn ở `c00, c01, c12–c18`**; `c07` chỉ có Hùng (Anh Tám nói qua điện thoại); cán bộ `c15` áo sơ mi trắng trơn không sắc phục; kẻ lừa `c19` giấu mặt 100%; không viền letterbox, không chữ/logo/vũ khí) | Kiểm tra trực quan từng ảnh & khung `preview_frames/*_safezone.jpg` | ☐ |
| 2 | Sinh giọng thật (`46/46` câu `gemini-3.8-flash-tts`, 8 tuyến nhân vật = 8 voice độc lập) + căn timeline theo WAV thật + nghe rà soát cả 46 file `.mp3` | `python factory196/_engine/run.py gate EP07 2` | ☐ |
| 3 | SFX/BGM + master (kiểm tra rõ hiệu ứng `af: phone` và `af: memory` ở `l33_tam_mem`; **nghe thử trước giọng Bé My (`be_bong`) và Anh Tám (`ong_bay`)**) | `python factory196/_engine/run.py gate EP07 3` | ☐ |
| 4 | Timeline `1920x1080 @ 30fps` + Chapter cards + Màn hình đen chữ trắng + Boxless Subtitle + Safe Zone QA | `python factory196/_engine/run.py gate EP07 4` | ☐ |
| 5 | Render staging + QA 8 điểm → **DỪNG CHỜ CHỦ KÊNH DUYỆT STAGING** | `python factory196/_engine/run.py gate EP07 5` | ☐ |
| 6 | Đóng gói phát hành (chỉ chạy sau khi chủ kênh duyệt Staging) | `python factory196/_engine/run.py signoff EP07 --listen PASS --point 2 4 5 --by "Chủ kênh"` → `... gate EP07 5 --skip-render` → `... gate EP07 6` | ☐ |

Ghi chú vòng sửa:
- **19/11/2026 – v1-draft:** Hoàn chỉnh trọn bộ hồ sơ Tầng 1 `factory196/EP07` (24 cảnh, 48 câu thoại ngắn gọn `≤ 25 từ`, Người Bóc Trần đúng 1 câu 20 từ `< 9.1s`, đánh đổ hoàn toàn ảo tưởng quan hệ giang hồ, anh hùng mạng thu hồi tiền và thái độ xem thường cơ quan pháp luật; sạch 100% `policy_wordlists.json` và Regex Gate 5).
- **19/11/2026 – v2-draft:** Sửa theo phản biện pháp lý (11 điểm): bỏ "anh hùng mạng/hiệp sĩ/pháp lý/tài sản số", Anh Tám không truy tìm được ai, cán bộ có hành động với khoản mới, sửa mốc ngày và lần chặn trùng, chốt bằng "xấu hổ", thêm bước gọi ngân hàng. Clearance chuyển về CHỜ DUYỆT.
