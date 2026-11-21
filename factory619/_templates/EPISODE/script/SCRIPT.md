# KỊCH BẢN – {{EP}}: {{TITLE}}

> Khung 70 giây / 6 nhịp theo [SHORT_FORMAT_SPEC.md](../../../../00_HARNESS_GUIDELINES/SHORT_FORMAT_SPEC.md).
> Mọi tên người, số điện thoại, số tài khoản, tên ngân hàng/app trong kịch bản đều phải là **hư cấu hoặc chung chung**.

## 0. Thẻ tập & Khung Thư viện Cảnh giác *(theo [VIGILANCE_LIBRARY_FRAMEWORK.md](../../../../00_HARNESS_GUIDELINES/VIGILANCE_LIBRARY_FRAMEWORK.md))*
| Mục | Nội dung |
| :--- | :--- |
| Góc quan sát (Format `A–F`) | `B` 1 chi tiết tưởng bình thường / `C` Hai nạn nhân / `D` Biến thể mới / `E` Kiểm tra thực chiến |
| Nhóm chiêu & Biến thể Lớp 1 (`VAR`) | (tra [VIGILANCE_LIBRARY_MAP.md](../../../../01_SCAM_MAP/VIGILANCE_LIBRARY_MAP.md) — ghi rõ điểm mới bổ sung) |
| Điểm dễ mắc Lớp 2 (`COND`) | (điều kiện hoàn cảnh cụ thể, không phân tích tâm lý đại cương) |
| Ứng phó Lớp 3 (`RESP`) | (1 hành động rõ ràng, phổ quát/đã kiểm chứng) |
| Nạn nhân & Kẻ lừa hình tượng | (từ `02_CAST/cast.json`) |
| 1 câu neo ký ức (`Recall Anchor`) | *(đúng 1 câu dễ kể lại cho bố mẹ/bạn bè)* |

### Tự kiểm Pre-Gate 0 (Bộ lọc `4+2`)
- [ ] **Mới** · [ ] **Thực dụng** · [ ] **Khác biệt** (không trùng tập cũ) · [ ] **Có ích** · [ ] **1 câu dễ kể lại** · [ ] **An toàn (`L2`/`L8`)**

## 1. Sáu nhịp & Kế hoạch Visual Motion (Level 2)
*Phân loại `beat_type` và `motion_level` (`A`/`B`/`C`/`D`) trước khi dựng theo [VISUAL_MOTION_HARNESS.md](../../../../00_HARNESS_GUIDELINES/VISUAL_MOTION_HARNESS.md); tránh lặp zoom-in máy móc.*

| Nhịp | Thời gian | Hình (scene) | Beat & Motion Level (A/B/C/D + Lý do) | Thoại / VO | Chữ trên hình | Âm thanh khớp Motion |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1. HOOK | 00–05s | scene1 | `climax` · Lv `A` (`slow_push_in` nhẹ) | | Hook | chuông/rung máy |
| 2. MỒI NHỬ | 05–20s | scene2 | `information` · Lv `C` (`screen_glow` + `chat_bubbles`/`notifications`) | | bong bóng tin nhắn | `notification` / `click` |
| 3. LEO THANG | 20–38s | scene3 | `suspicion` · Lv `A` hoặc `B` (2.5D nếu có chiều sâu) | | | `heartbeat`, nhạc dồn |
| 4. CÚ CHỐT | 38–50s | scene4 | `climax` · Lv `A` (`slow_pull_out`) hoặc `D` (clip ngắn tùy chọn) | | | `bank_ting` + `impact` |
| 5. BÓC TRẦN | 50–60s | scene5 | `anomaly` · Lv `C` (`focus_highlight` / `detail_reveal`) | VO Người Bóc Trần | | `glitch`, `low_accent`, drone |
| 6. DẤU HIỆU | 60–70s | scene6 | `ending` · Lv `A` (`static_hold`, không rung) | (không thoại) | Thẻ dấu hiệu + Disclaimer | `warm_outro` |

## 2. Lời thoại chốt (≤ 110 từ tổng, ≤ 22 từ/câu)
1. 
2. 

## 3. Thẻ DẤU HIỆU NHẬN BIẾT
1. 
2. 
3. 
- **Nên làm:** 

## 4. Tự kiểm “Không dạy lừa”
- [ ] Không có câu thoại kẻ lừa đủ chi tiết để người xem chép lại làm kịch bản lừa thật.
- [ ] Không chỉ cách lập tài khoản giả, vượt xác thực, lấy OTP, rửa tiền.
- [ ] Phần “bóc trần” giải thích **vì sao nạn nhân tin** và **dấu hiệu**, không giải thích **cách vận hành đường dây**.

