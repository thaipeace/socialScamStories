# PHIẾU THỰC THI – {{EP}}: {{TITLE}}

Lệnh chạy từ thư mục gốc dự án (`c:\projects\socialScamStories`).

| Gate | Việc | Lệnh | Xong |
| :-: | :--- | :--- | :-: |
| 0 | **TIẾN TRÌNH CHECK 1 → 2 → 3 bắt buộc (Làm mới · Sửa · Update):** Kịch bản + Clearance ĐẠT (`CHECK 1`) + **Kế thừa Level 2 (`CHECK 2`: `beat_type`/`motion_level`, `2.5D ≥ 1`, `breathing ≥ 1`, `eye_blink ≥ 2`, `mouth_sync ≥ 2` khớp `.wav` thật)** + **Level 3 (`CHECK 3`)** + đồng bộ `source/build_draft.py` | `python factory619/_engine/run.py motion-check {{EP}}` rồi `... gate0 {{EP}}` | ☐ |
| 1 | Duyệt ảnh 9:16 (đồng nhất nhân vật, không logo/chữ lạ, không máu me) + chuẩn bị đủ **2.5D (`sX_bg.jpg`, `sX_fg.png`)** + **Living-Character 2.5** (`eye_blink`, `mouth_sync` 3–4 trạng thái qua `03_ENGINE/face_roi_prep.py`, duyệt bảng Face QC cận mặt) + xem khung QA | `python factory619/_engine/run.py gate {{EP}} 2 --placeholder` rồi `... gate {{EP}} 4 --preview` | ☐ |
| 2 | Sinh giọng thật + **nghe duyệt từng câu** *(không re-synth khi chỉ sửa hình)* | `python factory619/_engine/run.py gate {{EP}} 2` → `... signoff {{EP}} --listen PASS --by "<tên>"` | ☐ |
| 3 | SFX/BGM + khớp foley với chuyển động Level 2 & 3 (`click`/`notification`/`light_switch`/`low_accent`/`marker_draw`/`counter_tick`) + master | `python factory619/_engine/run.py gate {{EP}} 3` | ☐ |
| 4 | Timeline 9:16 + Visual Motion Level 3 (tự chặn nếu chưa qua CHECK 1–2–3; 4 worker `cv2`) + overlay + render video | `python factory619/_engine/run.py gate {{EP}} 4 --workers 4 --encoder auto` | ☐ |
| 5 | Render staging + **Bảng CHECK 1–2–3** + QA 8 điểm + **Visual Motion QC 11 điểm** (`GATE5_QA_REPORT.md`; chữ ký cũ tự hết hiệu lực khi sửa/render mới) → **DỪNG CHỜ DUYỆT STAGING** → ký duyệt điểm 2, 4, 5 | `... gate {{EP}} 5` → `... signoff {{EP}} --point 2 4 5 --by "<tên>"` → `... gate {{EP}} 5 --skip-render` | ☐ |
| 6 | Đóng gói phát hành (chỉ chạy sau khi chủ kênh duyệt Staging bản mới nhất) | `python factory619/_engine/run.py gate {{EP}} 6` | ☐ |

Ghi chú vòng sửa:
- 

