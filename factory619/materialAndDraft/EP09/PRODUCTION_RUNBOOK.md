# PHIẾU THỰC THI – EP09: Bẫy Cuộc Gọi Nhỡ Lúc Đang Chờ Việc

Lệnh chạy từ thư mục gốc dự án (`c:\projects\socialScamStories`).

| Gate | Việc | Lệnh | Xong |
| :-: | :--- | :--- | :-: |
| 0 | Kịch bản + Clearance ĐẠT + đủ ảnh `assets/scene1..7.jpg` + `episode.json` | `python factory619/_engine/run.py gate0 EP09` | ☑ |
| 1 | Duyệt ảnh (đồng nhất nhân vật, không logo/chữ lạ, không máu me) + xem khung chuyển động | `python factory619/_engine/run.py gate EP09 2 --placeholder` rồi `... gate EP09 4 --preview` | ☑ |
| 2 | Sinh giọng thật + **nghe duyệt từng câu** | `python factory619/_engine/run.py gate EP09 2` → `... signoff EP09 --listen PASS --by "<tên>"` | ☑ |
| 3 | SFX/BGM + master | `python factory619/_engine/run.py gate EP09 3` | ☑ |
| 4 | Timeline + overlay + render video | `python factory619/_engine/run.py gate EP09 4` | ☑ |
| 5 | Render staging + QA 8 điểm → xem video → ký duyệt điểm 2, 4, 5 | `... gate EP09 5` → `... signoff EP09 --point 2 4 5 --by "<tên>"` → `... gate EP09 5 --skip-render` | ☑ |
| 6 | Đóng gói phát hành | `python factory619/_engine/run.py gate EP09 6` | ☑ |

Ghi chú vòng sửa:
- v3 (45.5s): Rút gọn đoạn 0:22–0:42 từ ~20s xuống ~9.4s (bỏ callout giảng bài), chuyển toàn bộ thoại từ s4–s6 sang văn nói đời thường tự nhiên, bỏ lặp ý giữa Anh Hai – Người Bóc Trần – Thẻ NHỚ KỸ, cô đọng Thẻ NHỚ KỸ dễ đọc nhanh.
- v4-level2-abc (45.5s, HRN-MOTION-L2.1): Nâng cấp Living-Character A/B/C (`eye_blink` + `mouth_sync` khớp WAV trên s1–s5 gồm song thoại luân phiên Bé Na ↔ Anh Hai ở s5; tách 2 lớp 2.5D + `breathing` trên s4 & s6 với mặt nhân vật khóa cứng theo layer `fg`), `A=1 · B=2 · C=4 · D=0`, Gate 5 đạt 8/8 PASS và đã xuất bản Gate 6 (thumbnail 11.8s sạch không dính phụ đề).


