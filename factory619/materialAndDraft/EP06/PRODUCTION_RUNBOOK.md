# PHIẾU THỰC THI – EP06: Thói quen check-in du lịch mời trộm vào nhà (v6-level2-abc)

Lệnh chạy từ thư mục gốc dự án (`c:\projects\socialScamStories`).

| Gate | Việc | Lệnh | Xong |
| :-: | :--- | :--- | :-: |
| 0 | Kịch bản + Clearance ĐẠT + đủ 12 ảnh gốc + 27 mảnh mặt sống + 2 cặp 2.5D + `episode.json` | `python factory619/_engine/run.py gate0 EP06` | ☑ |
| 1 | Duyệt ảnh + soi phóng đại 4 bảng Face QC & mô phỏng 2.5D (`s4a`, `s5a`) | Kiểm tra trực quan `assets/` + `motion-check EP06` | ☑ |
| 2 | Sinh giọng thật `gemini-3.8-flash-tts` + **nghe duyệt trực tiếp cả 9 câu** | `python factory619/_engine/run.py gate EP06 2` → `... signoff EP06 --listen PASS --by "agent"` | ☑ |
| 3 | SFX/BGM + master (`47.62s`, `-1.08 dBFS`) | `python factory619/_engine/run.py gate EP06 3` | ☑ |
| 4 | Timeline 12 cảnh thuần Engine `HRN-MOTION-L2.1` + overlay + render `30fps` | `python factory619/_engine/run.py gate EP06 4` | ☑ |
| 5 | Render staging + QA 8 điểm + soi trực tiếp 10 khung MP4 & thumbnail | `python factory619/_engine/run.py gate EP06 5` | ☑ |
| 6 | Đóng gói phát hành (giữ nguyên `EP06_Uplodaed` cũ) | `python factory619/_engine/run.py gate EP06 6` | ☑ |

Ghi chú vòng sửa:
- `v5` (`47.62s`): Đổi mở đầu (`s1_hook`) sang cảnh ngồi trên xe trở về nhà xem lại ảnh check-in bãi biển 4 ngày với lời thoại vợ chồng tự nhiên; chỉnh giọng Chú tổ trưởng an ninh (`ong_bay`) và Chú tuần tra (`chu_bao_ve`) nhanh gọn, dứt khoát.
- `v6-level2-abc` (`47.62s`, `HRN-MOTION-L2.1`): Thay thế hoàn toàn 6 clip `.mp4` cũ bằng **12 cảnh thuần Engine** (`A=2 · B=2 · C=8 · D=0`, không lặp zoom-in liên tiếp). Bổ sung **27 mảnh mặt sống** (`mouth_sync` 3 trạng thái khớp WAV cho `s1a` Chị Ba, `s2b` Anh Hai, `s3a` Chị Ba, `s3b` Ông Bảy, `s4b` Chị Ba + `eye_blink` toàn tập) và **2 cảnh 2.5D** (`s4a` tách tiền cảnh 2 chú tuần tra khóa trục chóa đèn pin + `s5a` kính lúp đỏ/điện thoại check-in trên nền hẻm tối & cổng khóa). Gate 5 đạt `8/8 PASS`, xuất bản Gate 6 (thumbnail `31.93s` sạch không phụ đề).
