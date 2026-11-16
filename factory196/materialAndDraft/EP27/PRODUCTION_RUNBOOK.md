# PHIẾU THỰC THI (16:9 LONG-FORM 4–5+ PHÚT) – EP27: Sau khoản nợ cuối cùng

Lệnh chạy từ thư mục gốc dự án (`c:\projects\socialScamStories`).

| Gate | Việc | Lệnh | Xong |
| :-: | :--- | :--- | :-: |
| 0 | Kịch bản 4–5+ phút (≥ 240s, phản biện pháp lý & logic) + Clearance ĐẠT + đủ ảnh 16:9 + `episode.json` | `python factory196/_engine/run.py gate0 EP27` | ☑ |
| 1 | Duyệt ảnh 16:9 (không viền letterbox, không chữ/logo/biển số, cảnh lên hình trước thoại 0.3s) + xem khung QA | `python factory196/_engine/run.py gate EP27 2 --placeholder` rồi `... gate EP27 4 --preview` | ☑ |
| 2 | Sinh giọng thật (tách rõ âm sắc các nhân vật cùng giới) + căn lại timeline theo WAV thật + **nghe duyệt `.mp3`** | `python factory196/_engine/run.py gate EP27 2` → `... signoff EP27 --listen PASS --by "<tên>"` | ☑ |
| 3 | SFX/BGM + master (≥ 240s) | `python factory196/_engine/run.py gate EP27 3` | ☑ |
| 4 | Timeline 1920x1080 + Chapter cards + Subtitle + Render video | `python factory196/_engine/run.py gate EP27 4` | ☑ |
| 5 | Render staging + QA 8 điểm → **DỪNG CHỜ CHỦ KÊNH DUYỆT STAGING** → ký duyệt điểm 2, 4, 5 | `... gate EP27 5` → `... signoff EP27 --point 2 4 5 --by "<tên>"` → `... gate EP27 5 --skip-render` | ☑ |
| 6 | Đóng gói phát hành (chỉ chạy sau khi chủ kênh duyệt Staging) | `python factory196/_engine/run.py gate EP27 6` | ☑ |

Ghi chú vòng sửa:
- **16/11/2026 – v2-draft:** Đã có script, `episode.json` (sinh từ `source/build_draft.py`), prompt ảnh, clearance, cast mới (`chi_hai`, `co_hanh`, `chu_no`).
- **16/11/2026 – v4-tet2027 (EP27 · trục A → B → C → D → E → 7 năm → F):** Căn chuẩn lại toàn bộ mốc thời gian: đợt tiết kiệm đã cạn (A) → tái vay & chim mồi (B, C) → cắt gọn tư vấn còn 2 câu không giáo điều (D) → đẩy **Cao trào Ra đi** lên đỉnh cảm xúc với `c19`, `c19b`, `c19c` khi bé Tom mới 1 tuổi ngủ trên vai mẹ (E) → chặng **7 năm / 84 kỳ trả góp** & đối chất thu giấy gốc → **7 năm sau quay về** ngày Tết bình dị (`c20`, `c21`, `c21b`, `c21c`) khi sóng gió đã êm và bé Tom nay 8 tuổi hỏi câu đứt ruột. 64/64 câu đồng nhất `gemini-3.8-flash-tts`.

