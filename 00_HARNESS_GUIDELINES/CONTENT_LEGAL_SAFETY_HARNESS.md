# HARNESS PHÁP LÝ & AN TOÀN NỘI DUNG – KÊNH BÓC TRẦN LỪA ĐẢO
*Mã: HRN-LEGAL-SCAM-V1 · Áp dụng cho mọi tập, tiêu đề, description, bình luận ghim, thumbnail*

> [!CAUTION]
> Tài liệu này do AI soạn để làm khung làm việc, **không phải tư vấn pháp lý**. Các điều luật dẫn ở mục VI cần người có chuyên môn kiểm tra lại số điều và hiệu lực (xem rủi ro `L7` trong [CONSTRAINTS_AND_RISK_REGISTER.md](../CONSTRAINTS_AND_RISK_REGISTER.md)).

## I. VÌ SAO CHỦ ĐỀ NÀY AN TOÀN HƠN 779 – VÀ RỦI RO CÒN LẠI Ở ĐÂU

| | Dự án 779 (chiến tranh biên giới) | Kênh Bóc Trần Lừa Đảo |
| :--- | :--- | :--- |
| Rủi ro chính trị, đối ngoại, chủ quyền | Cao | Gần như không có |
| Phụ thuộc nguồn sử liệu / nhân chứng | Bắt buộc | Không bắt buộc (hư cấu hóa tình huống điển hình) |
| Rủi ro **vu khống / xúc phạm danh dự** | Thấp | **Cao nhất** – nếu chỉ đích danh người, doanh nghiệp, app |
| Rủi ro **“dạy lừa”** (nền tảng xếp vào nội dung lừa đảo/gây hại) | Không có | **Cao** – nếu đi quá sâu vào thao tác |
| Rủi ro **giả mạo thương hiệu / cơ quan** | Bản đồ | Logo ngân hàng, giao diện app, sắc phục công an |

→ Toàn bộ harness xoay quanh **5 NGUYÊN TẮC VÀNG** dưới đây.

## II. 5 NGUYÊN TẮC VÀNG

### 1. KHÔNG ĐỊNH DANH (Zero Real Identity)
- Mọi nhân vật là **hình tượng** trong [02_CAST/cast.json](../02_CAST/cast.json). Không dùng tên, ảnh, giọng của người thật – kể cả nạn nhân đã lên báo.
- **Không** hiển thị/đọc số điện thoại, số tài khoản, biển số, địa chỉ, link, mã QR thật. Nếu cần trên hình: `0xx.xxx.xxxx`, `STK: ••••••`, `Ngân hàng A`, `Ứng dụng X`.
- **Không** nêu tên ngân hàng, ví điện tử, nhà mạng, sàn TMĐT, hãng vận chuyển, doanh nghiệp. Gate 5 tự quét theo `identity_hard_block` trong [policy_wordlists.json](policy_wordlists.json).
- Tên mạng xã hội chung (Zalo, Facebook, Telegram…) và tên cơ quan (công an, tòa án, BHXH…) chỉ dùng khi **cần để nhận biết chiêu**, theo dạng “**giả danh** …”, và phải được ký xác nhận ở Gate 5 (soft warn).

### 2. KHÔNG VU KHỐNG (No Accusation)
- Không ám chỉ một cá nhân, doanh nghiệp, địa phương, cộng đồng cụ thể đang lừa đảo – kể cả bằng chi tiết gợi nhận dạng (logo đổi màu, tên gần giống, địa chỉ thật).
- Câu chữ dùng thể **mô tả chiêu thức**: “Có kẻ giả danh…”, “Một kiểu chiêu trò…”, không dùng “Công ty X lừa đảo”.
- Không đưa con số thiệt hại cụ thể như thể sự thật nếu không có nguồn; có thể nói chung “nhiều người đã mất tiền”.

### 3. KHÔNG DẠY LỪA (Expose, Don’t Instruct)
Ranh giới: **bóc trần cơ chế tâm lý + dấu hiệu nhận biết**, không mô tả **cách vận hành**.

| ✅ ĐƯỢC | ❌ KHÔNG |
| :--- | :--- |
| “Chúng tạo áp lực thời gian để bạn không kịp hỏi ai” | Kịch bản thoại đầy đủ, từng bước để gọi lừa |
| “Đường link lạ có thể chiếm quyền điều khiển máy” | Cách tạo link/app giả, cách vượt xác thực, cách lấy OTP |
| “Chúng chia nhỏ số tiền để bạn không nghi” | Cách thuê/mua tài khoản ngân hàng, cách rút tiền, rửa tiền |
| “Video gọi có thể là hình ghép” | Công cụ/ quy trình làm deepfake |

Mỗi kịch bản có mục tự kiểm “Không dạy lừa” (template `script/SCRIPT.md`); Gate 5 điểm 2 bắt buộc người duyệt.

### 4. KHÔNG GIẢ MẠO (No Brand / Authority Replica)
- Ảnh AI: prompt luôn kèm `no text, no logos, no real app interface, no real uniforms or insignia`.
- Bong bóng tin nhắn của engine là **thiết kế trung tính** (không màu nhận diện, không icon của app thật).
- Kẻ giả danh cơ quan: trang phục **mơ hồ, không phù hiệu, không quân hàm, không quốc huy/công an hiệu**; ưu tiên chỉ thấy bóng/ánh màn hình.
- Không dựng giấy tờ, con dấu, lệnh bắt, văn bản cơ quan nhà nước giống thật (chỉ khung mờ, không chữ đọc được).

### 5. TÔN TRỌNG NẠN NHÂN & KHÔNG KỲ THỊ
- Nạn nhân là người **bình thường bị thao túng**, không phải “ngu”, “tham”. Không cười cợt nỗi mất mát.
- Không gắn lừa đảo với vùng miền, dân tộc, quốc tịch, giới tính, nghề nghiệp, tuổi tác. Kẻ lừa là “kẻ giấu mặt”, không mang đặc điểm nhận dạng cộng đồng.
- Không nhắc chi tiết nạn nhân tự làm hại bản thân (chủ đề tự tử thuộc `asr_ocr_hard_block`). Nếu tập có hậu quả nặng nề về tinh thần: kết bằng thông điệp chia sẻ với người thân, tìm hỗ trợ.

## III. KHUYẾN NGHỊ “NÊN LÀM” TRÊN THẺ DẤU HIỆU
Chỉ dùng các khuyến nghị **phổ quát, không gây hại nếu làm theo**:
- Cúp máy; tự gọi lại **số chính thức** (in trên thẻ, hợp đồng, website chính thức) – không gọi lại số vừa gọi đến.
- Không chuyển tiền, không đọc mã OTP, không bấm link, không cài ứng dụng theo yêu cầu người lạ.
- Hỏi ngay một người thân tin cậy trước khi làm theo bất cứ yêu cầu tiền bạc nào.
- Đã lỡ chuyển tiền: gọi ngay tổng đài ngân hàng để yêu cầu phong tỏa và trình báo cơ quan công an nơi gần nhất.
- Số khẩn cấp công an: **113**.

> [!WARNING]
> Không ghi tổng đài, website “tra cứu/khiếu nại” nào khác lên video khi chưa tự kiểm tra là kênh chính thức còn hoạt động – kẻ lừa thường giả mạo chính các trang “lấy lại tiền”.

## IV. AN TOÀN THUẬT TOÁN (kế thừa 779 – mục IV POLITICAL_LEGAL_HARNESS)
- Nền tảng quét song song **giọng (ASR) + chữ trên hình (OCR) + metadata**.
- Danh sách cấm/ cảnh báo và câu thay thế: [policy_wordlists.json](policy_wordlists.json) (Gate 5 tự quét).
- Chủ đề lừa đảo hay chạm: bạo lực đe dọa, tình dục (sextortion), cờ bạc, ma túy, tự hại → luôn dùng từ thay thế, không minh họa.

## V. MINH BẠCH AI & HƯ CẤU
- Disclaimer cuối video (engine tự chèn): *“Tình huống được dựng lại để cảnh báo. Nhân vật, tên, số liệu đều là hư cấu.”*
- Description tự gắn nhãn `🎬 PHIM HOẠT HÌNH DỰNG LẠI TÌNH HUỐNG` + `🤖 hỗ trợ bởi AI`.
- Bật khai báo nội dung tổng hợp/AI trên YouTube, TikTok, Facebook khi đăng.

## VI. CĂN CỨ PHÁP LÝ THAM KHẢO (CẦN KIỂM CHỨNG)
| Vấn đề | Văn bản thường được dẫn | Áp dụng cho kênh |
| :--- | :--- | :--- |
| Danh dự, nhân phẩm, uy tín; quyền đối với hình ảnh | Bộ luật Dân sự 2015 (các điều về quyền nhân thân) | Nguyên tắc 1, 2 |
| Vu khống | Bộ luật Hình sự 2015 (tội vu khống) | Nguyên tắc 2 |
| Hành vi bị cấm trên không gian mạng; thông tin sai sự thật | Luật An ninh mạng 2018 và các nghị định xử phạt vi phạm hành chính lĩnh vực thông tin – truyền thông | Nguyên tắc 2, 4 |
| Sở hữu trí tuệ (nhãn hiệu, logo) | Luật Sở hữu trí tuệ | Nguyên tắc 4 |

## VII. QUY TRÌNH KHI CÓ KHIẾU NẠI / BÌNH LUẬN CHỈ ĐÍCH DANH
1. Ẩn ngay bình luận chứa tên người, số điện thoại, số tài khoản, ảnh chụp tin nhắn có thông tin cá nhân.
2. Nếu có người/doanh nghiệp cho rằng video ám chỉ họ: chuyển video sang *Riêng tư*, ghi nhận nội dung, đối chiếu hồ sơ clearance, chỉnh sửa trước khi đăng lại.
3. Không tranh cãi công khai; không đăng lại thông tin cá nhân của người khiếu nại.
