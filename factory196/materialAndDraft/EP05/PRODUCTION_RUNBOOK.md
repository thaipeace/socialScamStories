# PHIẾU THỰC THI (16:9 LONG-FORM 4–5+ PHÚT) – EP05: Tờ năm trăm và sáu giây nhìn thẳng

Lệnh chạy từ thư mục gốc dự án (`c:\projects\socialScamStories`).

| Gate | Việc | Lệnh | Xong |
| :-: | :--- | :--- | :-: |
| 0 | Kịch bản 4–5+ phút (≥ 240s, phản biện nghiệp vụ ngân hàng & pháp lý 2026) + Clearance ĐẠT + `source/build_draft.py` → `episode.json` + đủ ảnh 16:9 | `python factory196/materialAndDraft/EP05/source/build_draft.py` rồi `python factory196/_engine/run.py gate0 EP05` | ☐ (chờ sinh `c00..c11.jpg`) |
| 1 | Duyệt ảnh 16:9 (Anh Hai cạo râu nhẵn xuyên suốt, đồng nhất hộp cam → bình nước cam, không viền letterbox, không chữ/logo/biển số, bubble không đè mặt) + xem khung QA | `python factory196/_engine/run.py gate EP05 2 --placeholder` rồi `python factory196/_engine/run.py gate EP05 4 --preview` | ☐ |
| 2 | Sinh giọng thật (8 nhân vật = 8 voice tách biệt) + chạy lại `build_draft.py` căn timeline theo WAV thật + **nghe duyệt `.mp3`** | `python factory196/_engine/run.py gate EP05 2` → `python factory196/materialAndDraft/EP05/source/build_draft.py` → `python factory196/_engine/run.py signoff EP05 --listen PASS --by "<tên>"` | ☐ |
| 3 | SFX/BGM + master (≥ 240s) | `python factory196/_engine/run.py gate EP05 3` | ☐ |
| 4 | Timeline 1920x1080 + Chapter cards + Boxless Subtitle + Render video | `python factory196/_engine/run.py gate EP05 4` | ☐ |
| 5 | Render staging + QA 8 điểm → **DỪNG CHỜ CHỦ KÊNH DUYỆT STAGING** → ký duyệt điểm 2, 4, 5 | `python factory196/_engine/run.py gate EP05 5` → `... signoff EP05 --point 2 4 5 --by "<tên>"` → `... gate EP05 5 --skip-render` | ☐ |
| 6 | Đóng gói phát hành (chỉ chạy sau khi chủ kênh duyệt Staging) | `python factory196/_engine/run.py gate EP05 6` | ☐ |

Ghi chú vòng sửa:
- **18/11/2026 – v1-draft:** Hoàn thành trọn bộ hồ sơ Tầng 1 (`source/SOURCE.md`, `source/build_draft.py`, `episode.json`, `script/SCRIPT.md`, `clearance/CLEARANCE.md`, `IMAGE_PROMPTS.md`); 8 nhân vật tách biệt 8 giọng trong `02_CAST/cast.json`; 31 câu thoại ngắn gọn (`≤ 23 từ/câu`), Người Bóc Trần đúng 1 câu ở thẻ kết (`< 10s`), sạch 100% `policy_wordlists.json`.
