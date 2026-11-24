# SỔ GHI RÀNG BUỘC & RỦI RO (CONSTRAINTS & RISK REGISTER)
## Lập ngày 01/11/2026 khi chuyển hướng từ dự án 779 sang kênh Bóc Trần Lừa Đảo

> **Trạng thái**: `MỞ` · `ĐANG LÀM` · `ĐÃ XONG` · `CHẤP NHẬN RỦI RO` (ghi lý do)
> **Nguyên tắc**: mục mức CAO phải xong trước khi đăng tập đầu tiên.

## L. PHÁP LÝ & NỀN TẢNG
| ID | Rủi ro | Mức | Biện pháp | Trạng thái |
| :--- | :--- | :---: | :--- | :--- |
| L1 | Vu khống / xúc phạm danh dự nếu ám chỉ người, doanh nghiệp, app cụ thể | **CAO** | Nguyên tắc 1–2 harness pháp lý; Gate 5 quét tên thương hiệu, SĐT, STK, URL | ĐANG LÀM (engine đã có bộ quét) |
| L2 | Bị nền tảng coi là nội dung hướng dẫn lừa đảo / gây hại | **CAO** | Nguyên tắc 3 “Không dạy lừa”; mục tự kiểm trong kịch bản; Gate 5 điểm 2 bắt buộc người duyệt | ĐANG LÀM |
| L3 | Vi phạm nhãn hiệu / giả mạo cơ quan (logo, giao diện, sắc phục) | **CAO** | Prompt ảnh bắt buộc “no logos/no uniforms”; bong bóng chat trung tính; Gate 5 điểm 4 | ĐANG LÀM |
| L4 | Nội dung AI hàng loạt bị hạn chế kiếm tiền (inauthentic/repetitious) | TRUNG BÌNH | Mỗi tập có giá trị biên tập riêng (dấu hiệu, việc nên làm); khai báo AI; đa dạng tình huống | MỞ |
| L5 | Từ khóa nhạy cảm (đe dọa, tình dục, cờ bạc, tự hại) bị bóp/giới hạn tuổi | TRUNG BÌNH | `policy_wordlists.json` + câu thay thế | ĐANG LÀM |
| L6 | Bình luận của khán giả lộ thông tin cá nhân / chỉ đích danh | TRUNG BÌNH | Ghim nhắc nhở; ẩn bình luận theo quy trình mục VII harness | MỞ |
| L7 | Căn cứ pháp lý trong harness do AI viết, chưa kiểm chứng | TRUNG BÌNH | Nhờ người có chuyên môn xem lại mục VI harness | MỞ |
| L8 | Khuyến nghị “nên làm” sai hoặc dẫn tới trang giả | **CAO** | Chỉ dùng khuyến nghị phổ quát (mục III harness); không ghi tổng đài/website chưa tự kiểm tra | ĐANG LÀM |

## C. KHẢ THI SẢN XUẤT (1 người)
| ID | Ràng buộc | Mức | Biện pháp | Trạng thái |
| :--- | :--- | :---: | :--- | :--- |
| C1 | Khối lượng 2 tập/tuần cho 1 người | TRUNG BÌNH | Engine dùng chung: mỗi tập chỉ cần `episode.json` + 6 ảnh; thử 8–12 tập trước | ĐANG LÀM |
| C2 | Đồng nhất nhân vật qua nhiều tập | TRUNG BÌNH | Dàn hình tượng cố định + mô tả ngoại hình trong CAST_AND_VISUAL_STYLE.md | MỞ |
| C3 | Tên giọng Gemini TTS trong `cast.json` chưa nghe thử với tiếng Việt | TRUNG BÌNH | Nghe thử từng giọng ở tập đầu, đổi nếu không hợp | MỞ |
| C4 | Engine mới viết lại từ 779, mới chạy thử với dữ liệu giả | TRUNG BÌNH | Chạy trọn 6 gate với tập thật đầu tiên, sửa lỗi phát sinh | ĐANG LÀM |
| C5 | Thư viện SFX tổng hợp có thể chưa đủ “thật” | THẤP | Cho phép thay bằng file âm thanh có bản quyền (`"file": ...`) | MỞ |
| C6 | Giới hạn phần cứng máy dựng (**ThinkPad L480 · Intel i5-8250U · đã nâng cấp 16GB Dual-Channel DDR4-2400 · UHD 620, không GPU rời**) | **TRUNG BÌNH** | Đã nâng Hardware Safety Profile lên **`dual16gb_cpu_l480`** (`motion_fx.py`, `motion_fx_l3.py`, `gate4_timeline.py`): tăng tốc OpenCV (`cv2`), render song song 4 worker (~47s / 450 frames full Level 3 1080p, tổng RAM < 550 MB / 16 GB), mở khóa Level 3 (tối đa 4 lớp 2.5D, Rack Focus `<= 8px`, `split_screen`, `evidence_fx`, `rain_layer`, `ambient_particles`, `light_sweep`, `color_mood`, `chromatic_pulse`, Living-Character 2.5). Vẫn loại trừ AI video/lip-sync cục bộ & Blender 3D; luôn giữ fallback `--safe-motion` về Level A. *(Lưu ý dung lượng ổ C hiện còn ~21GB trống — không cài PyTorch/model nặng).* | ĐÃ XONG |

## D. HIỆU QUẢ
| ID | Vấn đề | Mức | Biện pháp | Trạng thái |
| :--- | :--- | :---: | :--- | :--- |
| D1 | Chủ đề lừa đảo nhiều kênh làm – cần khác biệt | TRUNG BÌNH | Định dạng phim + thẻ dấu hiệu nhận diện riêng; âm hiệu “ting ting” | MỞ |
| D2 | Khán giả 45+ ở Facebook/Zalo nhiều hơn YouTube | TRUNG BÌNH | Đăng song song 3 nền tảng, đo giữ chân | MỞ |
| D3 | Gây lo âu thay vì trao quyền | THẤP | Xen kẽ tập “thoát hiểm”; luôn kết bằng việc nên làm | MỞ |

## E. KẾ THỪA TỪ 779
| Hạng mục | Trạng thái |
| :--- | :--- |
| Kiến trúc 3 tầng `materialAndDraft → staging → production` | ✅ Giữ nguyên |
| 6 Gate + phiếu runbook | ✅ Giữ, thêm Gate 0 tự động |
| TTS Gemini + mastering (trim không phá, −3 dBFS) | ✅ Port, nâng model `gemini-3.8-flash-tts` |
| DSP tổng hợp SFX/BGM + auto-ducking + limiter | ✅ Port thành `dsp.py`, thư viện preset mới |
| Ken Burns, rung, chuyển cảnh, Safe Zone, branding VCH | ✅ Đã nâng cấp lên **Visual Motion Level 3 + Living-Character 2.5** (`motion_fx.py` + `motion_fx_l3.py` + `gate4_timeline.py`: tăng tốc OpenCV `cv2`, render đa nhân 4 worker, `split_screen`, `rack_focus`, `evidence_fx`, môi trường `rain_layer`/`ambient_particles`/`light_sweep`/`color_mood`/`chromatic_pulse`, Living-Character 2.5 `head_micro_tilt`/`eye_gaze`/`expr_swap`/4-state `mouth_sync`, 11 chuyển cảnh điện ảnh) |
| Bộ lọc từ khóa ASR/OCR | ✅ Port + mở rộng |
| Nội dung lịch sử, nhân vật, bản đồ, harness chính trị 779 | ❌ Loại bỏ hoàn toàn |

## F. NHẬT KÝ
| Ngày | ID | Việc đã làm |
| :--- | :--- | :--- |
| 01/11/2026 | — | Khởi tạo dự án, port engine 6 Gate từ 779, viết harness pháp lý & định dạng mới, chạy thử engine với tập giả `EP00_SMOKE` (Gate 0→5 chạy trọn, Gate 6 từ chối đúng khi chưa ký duyệt) |
| 01/11/2026 | C3, C4 | Gọi thử thật `gemini-3.8-flash-tts` (giọng Charon) qua key HaizFlow: trả về WAV 24 kHz hợp lệ. Các giọng khác trong cast.json chưa nghe thử |
| 21/11/2026 | — | Tích hợp chuẩn **Visual Motion Upgrade (Level 2)** (`VISUAL_MOTION_HARNESS.md`, `03_ENGINE/motion_fx.py`, `gate4_timeline.py`, `gate5_render_audit.py`, `cli.py`, `sfx_library.py` + templates 2 nhà máy). Lưu ý giới hạn kỹ thuật: tách lớp PNG cho Level B và sinh clip ngắn AI I2V cho Level D thực hiện ngoài engine (do chưa cài ML segmentation/video API), engine đảm nhiệm ghép lớp, animate chi tiết, đồng bộ SFX, tự kiểm lặp zoom-in và hạ cấp an toàn về Level A |
| 24/11/2026 | C6 | Máy nâng cấp lên **16GB Dual-Channel DDR4-2400**. Nâng cấp toàn diện `03_ENGINE` lên nền tảng **Visual Motion Level 3 + Living-Character 2.5 (`HRN-MOTION-L3.0` · profile `dual16gb_cpu_l480`)**: cài `opencv-python-headless`, thêm module `03_ENGINE/motion_fx_l3.py`, render đa nhân mặc định 4 worker + tự chặn QSV đa phiên (khắc phục nghẽn UHD 620 thực đo), bổ sung trọn bộ Nhóm 1 (`split_screen`, `phone_waveform`, `rack_focus`, `red_circle_draw`, `highlighter_sweep`, `animated_counter`, `typing_indicator`, chuyển cảnh `whip_pan`/`zoom_punch`/`luma_wipe`/`film_burn`), Nhóm 2 (`rain_layer`, `ambient_particles`, `light_sweep`, `color_mood`, `chromatic_pulse`), Nhóm 3.7 (`head_micro_tilt`, `eye_gaze`, `expr_swap`, khẩu hình 4 trạng thái `round_image`), và 2 foley mới (`marker_draw`, `counter_tick`). Thực đo 450 frames 1080p full Level 3 FX: **47.0s (~9.6 fps, tổng RAM < 550 MB)**, giữ tương thích ngược 100% |
| 24/11/2026 | C4 | **Khóa cứng Luật Kế Thừa Cộng Dồn & Tiến trình Check 1 → 2 → 3** sau sự cố `EP05` nhảy cóc bỏ qua nền Level 2 (`mouth_sync`/`eye_blink`/`2.5D`): (1) `motion_fx.py`, `cli.py`, `gate4_timeline.py`, `gate5_render_audit.py` chặn cứng mọi tập `level2`/`level3` thiếu 2.5D/Breathing/EyeBlink/MouthSync (bất chấp làm mới, sửa hay update), đồng thời cảnh báo `[SYNC]` nếu `episode.json` lệch `source/build_draft.py`; (2) Gate 5 tự động hủy hiệu lực `human_qa_signoff.json` cũ (chống stale signoff khi sửa/render mới) và xuất bảng Check 1–2–3 trong `GATE5_QA_REPORT.md`; (3) vá căn ROI `crop_x`/`crop_y` + `region_space: "source"` trong `split_screen` (`motion_fx_l3.py`); (4) đồng bộ đủ toàn bộ Harness & Template 2 nhà máy lên `HRN-MOTION-L3.0` + Tiến trình Check 1–2–3 |
