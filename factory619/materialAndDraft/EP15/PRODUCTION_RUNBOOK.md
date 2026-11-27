# PHIẾU THỰC THI – EP15: Bẫy app ngân hàng giả tại quầy – Thấy tận mắt bấm chuyển, tiền vẫn bằng không!

Lệnh chạy từ thư mục gốc dự án (`/Users/thainguyendev/projects/socialScamStories`).

| Gate | Việc | Lệnh | Xong |
| :-: | :--- | :--- | :-: |
| 0 | **TIẾN TRÌNH CHECK 1 → 2 → 3 bắt buộc:** Kịch bản + Clearance ĐẠT (`CHECK 1`) + **Kế thừa Level 2 (`CHECK 2`: `beat_type`/`motion_level`, `2.5D ≥ 1`, `breathing ≥ 1`, `eye_blink ≥ 2`, `mouth_sync ≥ 2` khớp `.wav` thật)** + **Level 3 (`CHECK 3`)** + đồng bộ `source/build_draft.py` | `python3 factory619/_engine/run.py motion-check EP15` rồi `... gate0 EP15` | ☑ |
| 1 | Duyệt ảnh 9:16 (đồng nhất Cô Tư / Bé Na / Khách nam, không logo/chữ lạ) + chuẩn bị đủ **2.5D (`s2_bg/fg`, `s9b_bg/fg`)** + **Living-Character 2.5** (`eye_blink`, `mouth_sync` 3–4 trạng thái qua `03_ENGINE/face_roi_prep.py`, duyệt bảng `face_qc_sheet.jpg`) + xem khung QA | `python3 factory619/_engine/run.py gate EP15 2 --placeholder` rồi `... gate EP15 4 --preview` | ☑ |
| 2 | Sinh giọng thật + **nghe/kiểm duyệt từng câu** + chạy lại `build_draft.py` căn timeline theo WAV thật | `python3 factory619/_engine/run.py gate EP15 2` → `python3 factory619/materialAndDraft/EP15/source/build_draft.py` → `... signoff EP15 --listen PASS --by "<tên>"` | ☑ |
| 3 | SFX/BGM + khớp foley với chuyển động Level 2 & 3 + master | `python3 factory619/_engine/run.py gate EP15 3` | ☑ |
| 4 | Timeline 9:16 + Visual Motion Level 3 (tự chặn nếu chưa qua CHECK 1–2–3; 4 worker `cv2`) + overlay + render video | `python3 factory619/_engine/run.py gate EP15 4 --workers 4 --encoder auto` | ☑ |
| 5 | Render staging + **Bảng CHECK 1–2–3** + QA 8 điểm + **Visual Motion QC 11 điểm** (`GATE5_QA_REPORT.md`) → **CHỦ KÊNH DUYỆT STAGING V4 (8/8 PASS)** | `python3 factory619/_engine/run.py gate EP15 5` | ☑ |
| 6 | Đóng gói phát hành Production (`EP15_BayAppNganHangGia_78s.mp4`, `PUBLISH_PACKAGE_EP15.md`, `youtube_upload/`) | `python3 factory619/_engine/run.py gate EP15 6` | ☑ |
