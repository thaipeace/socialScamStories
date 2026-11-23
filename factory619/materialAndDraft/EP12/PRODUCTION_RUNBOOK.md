# PHIẾU THỰC THI – EP12: Mở trai tìm ngọc trên livestream (V3)

Lệnh chạy từ thư mục gốc dự án (`/Users/thainguyendev/projects/socialScamStories`).

| Gate | Việc | Lệnh | Xong |
| :-: | :--- | :--- | :-: |
| 0 | Kịch bản V3 + **Visual Motion Plan (Level 2: `beat_type`, `motion_level` A/B/C)** + Clearance ĐẠT + đủ ảnh `assets/` + `episode.json` | `python3 factory619/_engine/run.py motion-check EP12` rồi `... gate0 EP12` | ☑ |
| 1 | Duyệt ảnh (đồng nhất Cô Tư & phòng live, không logo/chữ rác/sắc phục thật) + biến thể **Living-Character A/B/C** (`eye_blink`/`mouth_sync` qua `03_ENGINE/face_roi_prep.py` + Face QC sheet), `detail_reveal`, lớp 2.5D `s9b_bg`/`s9b_fg` | `python3 factory619/_engine/run.py gate EP12 4 --preview` | ☑ |
| 2 | Sinh giọng thật (`gemini-3.8-flash-tts`) + **nghe duyệt từng câu** + dàn lại timeline theo thời lượng WAV thật | `python3 factory619/_engine/run.py gate EP12 2` → `... signoff EP12 --listen PASS --by "Chủ kênh"` | ☑ |
| 3 | Custom SFX/chatter livestream + BGM + khớp foley với motion Level C/B + trộn master audio | `python3 factory619/_engine/run.py gate EP12 3` | ☑ |
| 4 | Timeline + Visual Motion Level 2 + overlay + render video staging | `python3 factory619/_engine/run.py gate EP12 4` | ☐ |
| 5 | Render staging + QA 8 điểm + **Visual Motion QC 11 điểm** → **DỪNG CHỜ DUYỆT STAGING** | `... gate EP12 5` → `... signoff EP12 --point 2 4 5 --by "Chủ kênh"` → `... gate EP12 5 --skip-render` | ☐ |
| 6 | Đóng gói phát hành (chỉ chạy sau khi chủ kênh duyệt Staging) | `python3 factory619/_engine/run.py gate EP12 6` | ☐ |

Ghi chú bản V3:
- Bậc thang phí tâm lý chuẩn: `399K → 4 triệu (ký quỹ mở hạn mức thu mua) → 14 triệu (phí đổi ngoại tệ)`.
- Dựng 100% như lừa thật "cá cắn câu" từ `Khung 1` đến hết `Khung 5` (tuyệt đối không cài đạo cụ trinh thám sớm).
- Kết mở 2 shot câm thoại (`Khung 9A–9B`): Cô Tư phóng to ảnh kịp chụp màn hình 1 giây trước khi bị thu hồi → phòng đèn vòng bị ánh đèn chớp xanh–đỏ ập vào đêm sau.
