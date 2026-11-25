# PHIẾU THỰC THI – EP13: Tài Liệu Ôn Thi Miễn Phí (V1 · Level 3 Full)

Lệnh chạy từ thư mục gốc dự án (`/Users/thainguyendev/projects/socialScamStories`).

| Gate | Việc | Lệnh | Xong |
| :-: | :--- | :--- | :-: |
| 0 | Kịch bản V1 + **Visual Motion Level 3 Plan (`CHECK 1 → 2 → 3`)** + `source/build_draft.py` + `CLEARANCE.md` ĐẠT + đủ ảnh `assets/` + `episode.json` | `python3 factory619/_engine/run.py motion-check EP13` rồi `... gate0 EP13` | ☑ |
| 1 | Duyệt ảnh (đồng nhất Bé Na & Chị Ba, không logo/chữ rác/UI thật) + 2 bộ 2.5D (`s2`, `s9`) + 5 bộ **Living-Character 2.5** (`eye_blink` + `mouth_sync` gồm 4-state `round_image` qua `03_ENGINE/face_roi_prep.py` + `source/face_qc_sheet.jpg`) + 3 cặp `detail_reveal` + kiểm duyệt khung Safe Zone `--preview` | `python3 factory619/_engine/run.py gate EP13 4 --preview` | ☑ |
| 2 | Sinh giọng thật (`gemini-3.8-flash-tts`, 10/10 PASS `-3.0 dBFS`, đã thêm kỹ thuật SSO) + nghe duyệt từng file `.mp3` + dàn lại timeline theo thời lượng WAV thật (`77.32s`) qua `source/build_draft.py` | `python3 factory619/_engine/run.py gate EP13 2` → `... signoff EP13 --listen PASS --by "Chủ kênh"` | ☑ |
| 3 | Ambience + Foley khớp 9/9 motion Level 2/3 (`marker_draw`, `counter_tick`, `glitch`, `impact`...) + BGM + trộn master audio (`77.32s · peak -1.1 dBFS · rms -18.02 dBFS`) | `python3 factory619/_engine/run.py gate EP13 3` | ☑ |
| 4 | Timeline + Visual Motion Level 3 + overlay + render video Staging (`2320 frames · 48.76s @ 47.6 fps · libx264 · 4 workers`) | `python3 factory619/_engine/run.py gate EP13 4 --workers 4 --encoder auto` | ☑ |
| 5 | Render Staging (`EP13_TaiLieuOnThiMienPhi_77s_staging.mp4`, `48 MB`) + QA **8/8 PASS** + **Check 1–2–3 PASS** (Chủ kênh đã ký duyệt `human_qa_signoff.json`) | `... signoff EP13 --listen PASS --point 2 4 5 --by "Chủ kênh"` → `... gate EP13 5 --skip-render` | ☑ |
| 6 | Đóng gói phát hành Production (`factory619/production/EP13/` + bản sao `06_RENDERED_SHORTS/EP13_TaiLieuOnThiMienPhi_77s.mp4` + YouTube Upload Kit) | `python3 factory619/_engine/run.py gate EP13 6` | ☑ |

Ghi chú bản V1 (Level 3 Full):
- Nguồn cảm hứng: VTV24 *Thật - Giả, Kiểm chứng: Thủ đoạn lừa đảo bằng tài liệu miễn phí* (`2zs3HPL_k6w`).
- Đủ 2 mũi bẫy cốt lõi: (1) Link miền lạ bắt nhập mật khẩu mạng xã hội → mất nick & mạo danh vay tiền người thân; (2) Tệp giả dạng tài liệu giấu mã độc lấy ảnh riêng tư uy hiếp ép chuyển tiền.
- Đủ chuẩn Kế thừa Cộng dồn `HRN-MOTION-L3.0` (`Level 3 ⊃ Level 2 ⊃ Level 1`): 2 cảnh 2.5D (`s2`, `s9`) kèm Rack Focus + Breathing + Head Micro-Tilt, `split_screen` cuộc gọi 2 chiều (`s4`), 5 rig `eye_blink` + 5 rig `mouth_sync` (gồm 4-state `round_image` trên `s2`), cùng trọn bộ Level 3 FX (`red_circle_draw`, `highlighter_sweep`, `animated_counter`, `phone_waveform`, `typing_indicator`, `chromatic_pulse`, `ambient_particles`, `light_sweep`, `color_mood`, transitions `zoom_punch`/`whip_pan_left`/`film_burn`).
