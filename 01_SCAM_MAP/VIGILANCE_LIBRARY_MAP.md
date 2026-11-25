# BẢN ĐỒ PHỦ SÓNG THƯ VIỆN CẢNH GIÁC 3 LỚP (VIGILANCE LIBRARY MAP)
*Sổ theo dõi sống dùng song hành với [VIGILANCE_LIBRARY_FRAMEWORK.md](../00_HARNESS_GUIDELINES/VIGILANCE_LIBRARY_FRAMEWORK.md) · Bổ sung cho danh mục nhóm chiêu cũ tại [SCAM_MAP_ONLINE_TO_OFFLINE.md](SCAM_MAP_ONLINE_TO_OFFLINE.md).*

> [!NOTE]
> **Cách dùng cho các tập mới (`factory196: EP08b, EP10+` — không dùng mã `EP09`, `factory619: EP11+`):**
> - Khi gặp một vụ lừa mới, tra bảng dưới để xác định nó thực sự **bổ sung mã biến thể (`VAR`), điều kiện (`COND`) hay ứng phó (`RESP`) nào chưa có** — tránh làm lại tập cũ chỉ bằng cách đổi vỏ.
> - Bảng Mục I chỉ **lập chỉ mục (read-only)** các tập đã làm để nhìn rõ vùng dày / vùng trống, **không sửa đổi bất kỳ tập cũ nào**.

---

## I. CHỈ MỤC PHỦ SÓNG CÁC TẬP ĐÃ LÀM (BASELINE — KHÔNG HỒI TỐ)

### A. Nhà máy `factory196` (Phim dài 16:9)

| Tập | Tên tập | Góc gần nhất | Lớp 1 — Cơ chế & Biến thể đã phủ | Lớp 2 — Điểm dễ mắc (`COND`) | Lớp 3 — Ứng phó (`RESP`) đã có |
| :-: | :--- | :-: | :--- | :--- | :--- |
| `EP01b` | Đáo hạn thẻ – Một buổi chiều mất xe | `A` | Dịch vụ tài chính phi pháp / bình thường hóa / kẹt thanh khoản đột ngột (`VAR-FIN-01`) | Kẹt tiền, sĩ diện, giấu gia đình (`COND-01`, `COND-07`) | Hỏi trực tiếp ngân hàng trả góp/mức tối thiểu, thỏa thuận gốc dân sự (`RESP-03`, `RESP-04`) |
| `EP02` | Chữ ma – 80 triệu và một cú click | `A` | Giả ngân hàng gửi link cập nhật / đánh cắp quyền truy cập (`VAR-IMP-01`) | Áp lực thời gian sợ khóa tài khoản (`COND-05`) | Ngân hàng không gửi link; tự mở app hoặc gọi số in sau thẻ (`RESP-03`) |
| `EP03` | 120 ngàn – Phút thứ 89 | `A` | Lừa tuyển dụng gắn nhiệm vụ 120k + dàn chim mồi giữ chân chia vai (`VAR-TASK-04`, `VAR-TASK-05`) | Đang cần việc, đồng thuận đám đông giả (`COND-01`, `COND-02`) | Nhà tuyển dụng thật không bắt nạp tiền (`RESP-01`) |
| `EP04` | 300 triệu gom vé hộ & Bí mật của Chị Hai | `A` | Mạo danh kênh bán vé nội bộ / gom tiền tập thể qua trung gian (`VAR-IMP-02`) | Say hào quang đám đông, không nghe khuyên (`COND-08`) | Chỉ mua kênh chính thức, không dùng tài khoản cá nhân gom tiền hộ (`RESP-01`, `RESP-02`) |
| `EP05` | Tờ năm trăm và sáu giây nhìn thẳng | `A+F` | Dàn cảnh offline 2 chốt: đổi quà lấy căn cước + đưa tiền mặt thật trước + quay lén 6s mặt sống + giải ngân mồi ép trả (`VAR-OFF-01`) | Lòng tốt muốn giúp người lớn tuổi + sợ mất mặt ở xưởng (`COND-07`, `COND-09`) | Không đưa căn cước/cầm máy người lạ; khóa thẻ, báo nhóm xưởng, ngân hàng khoanh tiền lạ, lập biên bản (`RESP-02`, `RESP-04`, `RESP-05`) |
| `EP06` | Ba triệu tám trên màn hình | `A` | App mua hàng hộ: cấp sẵn vốn ảo + nhóm chat cảm ơn rối rít + bù phần thiếu + khóa rút tiền đòi nạp tiếp (`VAR-TASK-02`, `VAR-TASK-04`, `VAR-TASK-05`, `VAR-TASK-06`) | Nhìn số dư nhảy tưởng tiền thật, áp lực chốt đơn trước giờ hạn (`COND-03`, `COND-04`, `COND-05`) | Đối chiếu sao kê ngân hàng thật, tra tuổi tên miền, cắt lỗ ngay không nạp gỡ lệnh (`RESP-01`, `RESP-03`, `RESP-06`) |
| `EP07` | Sau hai trăm triệu | `A` | Bẫy lừa lần 2 "hỗ trợ lấy lại tiền" + mắt xích dò thông tin ngoài đời + nhử phí từng đợt bằng bằng chứng mồi (ảnh che số, ghi âm cũ) (`VAR-REC-01`) | Đang mất tiền lớn, xấu hổ giấu con gái, cố cứu khoản đã mất (`COND-04`, `COND-06`, `COND-07`) | Dừng chuyển tiền, không thuê "lấy lại tiền", trình báo công an sớm thay vì chờ (`RESP-01`, `RESP-04`, `RESP-06`) |
| `EP08` | Một vòng tiền, hai nửa sự thật | `A` | Người đứng giữa (MITM): đọc lén lịch sử chat, nhái đúng văn phong sếp + nhá video ghép 3 giây đổ mạng yếu để điều phối 2 người quen tự chuyển tiền vòng (`VAR-MITM-01`) | Tin đã tự xác minh (thấy mặt 3s + gọi đúng số thật) + bị dặn giữ bí mật khỏi vợ (`COND-02`, `COND-06`, `COND-07`) | Gặp yêu cầu tiền kèm lời dặn "giữ bí mật" phải xác nhận trực tiếp đúng nội dung giao dịch (`RESP-03`, `RESP-06`) |
| `EP27` | Sau khoản nợ cuối cùng | `A+F` | Tín dụng đen góp ngày trừ phí trước + chim mồi "cùng cảnh ngộ" ăn hoa hồng 5% dụ ký vay chia đôi (`VAR-LOAN-01`) | Giấu gia đình vì sợ làm phiền, tin người cùng cảnh ngộ (`COND-06`, `COND-07`) | Nói với người thân trước khi ký; phòng trợ giúp pháp lý; ghi âm, tính gốc thực nhận + lãi luật định, lấy lại giấy nợ gốc (`RESP-04`, `RESP-05`) |

### B. Nhà máy `factory619` (Shorts 9:16)

| Tập | Tên tập | Góc gần nhất | Lớp 1 — Biến thể đã phủ | Lớp 2 (`COND`) | Lớp 3 (`RESP`) |
| :-: | :--- | :-: | :--- | :--- | :--- |
| `EP01` | Dàn cảnh chìa tiền ở cổng trường | `A` | Dụ trẻ bằng tiền + người lịch sự + đồng bọn chặn phía sau (`VAR-OFF-02`) | Trẻ nhỏ cả tin (`COND-09`) | Chạy vào cổng tìm bảo vệ ngay (`RESP-04`) |
| `EP02` | Bẫy phỏng vấn 90 đô/giờ chiếm quyền máy | `B` | Giả HR gửi file test giấu lệnh ngầm trong thư mục ẩn, quét virus báo sạch (`VAR-JOB-01`) | Thất nghiệp cần việc, đã tự quét sạch (`COND-01`, `COND-02`, `COND-05`) | Không bấm chạy; kiểm tra mã nguồn trước (`RESP-01`, `RESP-03`) |
| `EP03` | Con đang cấp cứu, chuyển gấp viện phí | `C` | Gọi hàng loạt phụ huynh + nhá video Deepfake lấy từ ảnh giấy khen (`VAR-IMP-03`) | Hoảng loạn + ép thời gian (`COND-05`) | Gọi cô chủ nhiệm xác thực; không đăng công khai ảnh/lớp con (`RESP-02`, `RESP-03`) |
| `EP04` | Dán đè mã QR ban đêm tại quán ăn | `B` | Dán đè decal mã QR cá nhân lên bảng thanh toán hàng loạt (`VAR-OFF-03`) | Vội thanh toán giờ cao điểm (`COND-05`) | Chủ quán kiểm tra bảng mã mỗi sáng; khách đối chiếu tên người nhận (`RESP-03`) |
| `EP05` | Bẫy tình ái kết hợp nhiệm vụ chốt đơn | `A` | Bạn trai ảo hứa hẹn tương lai → dẫn qua chốt đơn rồi khóa tài khoản (`VAR-TASK-01`, `VAR-TASK-06`, `VAR-ROM-01`) | Tình cảm online + sợ mất tiền lẫn người yêu (`COND-03`, `COND-04`) | Gọi video kiểm chứng + tìm kiếm ảnh ngược + ngừng nạp trình báo (`RESP-01`, `RESP-03`) |
| `EP06` | Check-in du lịch thời gian thực mời trộm | `B` | Khai thác bài đăng công khai báo vắng nhà dài ngày (`VAR-PRIV-01`) | Thói quen chia sẻ công khai | Về nhà mới đăng ảnh, nhờ an ninh/hàng xóm để ý (`RESP-02`, `RESP-04`) |
| `EP07` | Mạo danh Ngày hội & Đêm văn hóa | `B` | Lập trang sự kiện giả thu phí vào tài khoản cá nhân (`VAR-IMP-04`) | Tin sự kiện quen thuộc | Soi tên tài khoản nhận (cá nhân vs tổ chức) (`RESP-03`) |
| `EP08` | Biên lai báo nghẽn mạng – bấm nhận lương | `B` | Giả biên lai lỗi để dụ bấm link xác nhận nhận tiền (`VAR-IMP-05`) | Mong nhận tiền nhanh (`COND-05`) | Nhận tiền không bao giờ phải bấm link/nhập mật khẩu (`RESP-01`, `RESP-02`) |
| `EP09` | Bẫy cuộc gọi nhỡ lúc đang chờ việc | `B` | Nhá cuộc gọi nhỡ cước cao/giả danh lúc chờ phỏng vấn (`VAR-TEL-01`) | Đang chờ cuộc gọi quan trọng (`COND-01`) | Kiểm tra kênh chính thức trước khi gọi lại số lạ (`RESP-03`) |
| `EP10` | Hai mạng Wi-Fi trùng tên khách sạn | `B` | Dựng điểm phát Wi-Fi giả (Evil Twin) chiếm quyền/chặn lưu lượng (`VAR-TECH-01`) | Ham nhanh, tiện khi đi du lịch | Không giao dịch ngân hàng trên Wi-Fi công cộng không xác thực (`RESP-02`) |

---

## II. BẢN ĐỒ KHOẢNG TRỐNG GỢI Ý CHO CÁC TẬP MỚI (CẬP NHẬT DẦN)

Nhìn từ chỉ mục trên, những nhóm biến thể & lớp tri thức **chưa phủ hoặc còn mỏng** để ưu tiên khai thác ở giai đoạn tới (`EP10+` / `EP11+`):

### 1. Khoảng trống ở Lớp 1 (Biến thể chưa có tập riêng)
- **Họ Nhiệm vụ / Đầu tư:**
  - `VAR-TASK-01` (trả tiền thật về tài khoản ngân hàng 2–3 lần đầu để xóa sạch nghi ngờ — *mới nhắc lướt ở Short EP05, chưa giải phẫu sâu ở 196*).
  - `VAR-TASK-03` (có "mentor/cố vấn" kèm 1-1 kiểm soát nhịp độ, tách biệt với dạng group chat đông người ở `EP06`).
  - `VAR-TASK-07` (kẻ lừa tự đề nghị "cho vay tạm / góp chung 50%" để nạn nhân có động lực đi vay ngoài đập vào).
  - `VAR-TASK-08` (đổi lớp vỏ mới: đánh giá khách sạn, tương tác thương hiệu, tiếp thị liên kết, dịch thuật/đánh máy tại nhà).
- **Họ Giả danh / Chiếm quyền thiết bị:**
  - `VAR-DEV-01` (cài ứng dụng ngoài kho chính thức — giả dịch vụ công, thuế, điện lực, định danh — cấp quyền trợ năng/đọc màn hình).
  - `VAR-DEV-02` (kết hợp chia sẻ màn hình khi gọi hỗ trợ "khắc phục lỗi ngân hàng / sàn TMĐT").
- **Họ Giao dịch đời thường & Mua bán:**
  - `VAR-COM-01` (giao đơn hàng COD giá nhỏ không đặt nhưng đúng tên/địa chỉ nhà — tận dụng thói quen nhận giùm người thân).
  - `VAR-COM-02` (mua bán đồ cũ / thuê trọ / đặt cọc du lịch — bill chuyển khoản giả + giục giao hàng/giữ chỗ ngay).
  - `VAR-COM-03` (chuyển nhầm tiền vào tài khoản rồi dùng số khác đòi trả lại kèm bẫy xác minh/vay nợ).
- **Họ Offline / Lai (`OFF` / `MIX`):**
  - `VAR-OFF-04` (hội thảo tặng quà / khám sức khỏe miễn phí cho người cao tuổi — cơ chế "có đi có lại" + cô lập không gian).

### 2. Khoảng trống ở Góc quan sát (Format A–F)
- Hiện `factory196` chủ yếu mới dùng **A** và **A+F**; **chưa có tập nào thử C** (*Cùng một chiêu, hai nạn nhân* ở bản dài) hoặc **D** (*Cập nhật biến thể mới của chiêu cũ*).
- Hiện `factory619` mới tập trung **A** và **B**; **chưa thử E** (*Kiểm tra thực chiến* — đưa tin nhắn/tình huống cho người xem tự bắt lỗi trong 5 giây trước khi giải thích) và **D** (*Cập nhật biến thể mới*).

### 3. Khoảng trống ở Lớp 3 (Ứng phó thực chiến `RESP`)
- Xử lý ngay trong **15 phút vàng** khi lỡ cài app lạ / cấp quyền màn hình (`RESP-05` — cần kiểm chứng kỹ thuật trước khi dựng theo `L8`).
- Xử lý khi bị **mất quyền tài khoản mạng xã hội** (cách chặn vạ lây bạn bè bị nhắn vay tiền).
- Xử lý khi **lỡ lộ ảnh căn cước / ảnh chân dung** (phân biệt rủi ro thật vs hù dọa để không bị tống tiền).

---

## III. BẢNG ĐĂNG KÝ TẬP MỚI (ĐIỀN TRƯỚC GATE 0)

| Tập | Nhà máy | Góc (`A–F`) | Mã mới bổ sung (Lớp 1 / 2 / 3) | 1 câu neo ký ức (`Recall Anchor`) | Đạt bộ lọc `4+2`? | Trạng thái |
| :-: | :-: | :-: | :--- | :--- | :-: | :---: |
| `EP08b` | `factory196` | `D+F` | `VAR-MITM-02` / `VAR-COM-04` (nối trực tiếp `45tr` lúc `12:05` từ Khang ở `EP08` → chảy thẳng vào TK người bán xe máy công chứng; bẫy tam giác 2 nạn nhân thật) / `COND-01,02,05` / `RESP-01,03,04,05,06` ("2 Phải – 3 Không" + giữ nguyên tiền xác minh) | Bán xe, bán đất: ai ký hợp đồng thì đúng người đó chuyển tiền, ghi rõ biển số và ngày hợp đồng — lệch tên là dừng ký ngay! | ☑ | Đã lập draft Tầng 1 (`v1-draft`) |
| `EP10` | `factory196` | `A` | `VAR-FUNNEL-01` / `VAR-AI-01` (cơn bão FOMO AI 2026 + phễu khóa học giảm sốc 80% trong 10 phút + chim mồi bình dân + tặng công ty ảo đủ bộ phận vận hành tự động dụ nạp máy chủ `240tr` + điểm chạm nô lệ hóa xin trừ cấn → Hương bật Chế độ Máy bay, đập tan phản pháo ngoại tuyến bằng `0 KB` dữ liệu mạng & chỉnh năm `2000` làm vỡ trận nhóm VIP 300 người + kết mở Chị Hai `EP04`/`EP08b` với tay IT `EP06`) / `COND-01,02,03,05,07,08` / `RESP-01,03,04,06` | Khóa học giảm sốc 80% tặng công ty ảo 100 agent tự kiếm tiền chỉ là hoạt ảnh mồi — hỏi xem nó bán hàng gì, cho ai trước khi xuống tiền! | ☑ | Đã hoàn tất **Staging `v5`** (Gate 0–5 · `v5-level2-abc-staging`, `368.8s`, `186.73 MB`, `A=3 · B=4 · C=14`, 22 bộ Living-Char, chờ chủ kênh duyệt trước Gate 6) |
| `EP12` | `factory196` | `C+F` | `VAR-COM-03` (đặt song song 2 nhánh: chuyển nhầm thật không trả vs. bẫy giả chuyển nhầm) / `COND-05,09` / `RESP-01,02,03,05` | Tiền lạ vô tài khoản: không rút tiêu, không tự chuyển trả theo số lạ — giữ nguyên đó, chỉ hoàn qua ngân hàng hoặc công an! | ☑ | Ghi nháp ý tưởng (`DRAFT_196_EP12`) |
| `EP11` | `factory619` | `B` | `VAR-OFF-05` (dàn cảnh đám đông ngày hội đa thế hệ/tầng lớp: va chạm – vây chặn nhiều người – hỏi chuyện – giật chuyền tay – tản vào dòng người + kết mở người điều phối trung niên áo polo từ ban công) / `COND-09` / `RESP-01,04` | Chỗ đông người: vừa bị va chạm lại có người lạ áp sát hỏi chuyện — giữ chặt cổ/túi và lùi khỏi dòng chen liền! | ☑ | Đã phát hành Production (Gate 6 · `v4-multigen-festival-level2`, 62.6s) |
| `EP12` | `factory619` | `A/D` | `VAR-LIVE-01` (livestream mở trai tìm ngọc mồi nhỏ `399k` → bậc thang tâm lý `4 triệu` ký quỹ mở hạn mức thu mua → đòi tiếp `14 triệu` phí đổi ngoại tệ; dựng 100% như cá cắn câu đến phút chụp hình khay ngọc lọt góc hóa đơn bàn bị ông sếp đập bàn thu hồi chặn máy + kết mở Cô Tư đổi sắc lạnh phóng to ảnh kịp chụp màn hình gửi hồ sơ → phòng đèn vòng bị ập vào) / `COND-02,03,05,08` / `RESP-01,05` | Cho tự chọn, thấy tận mắt khiến bạn sợ bỏ lỡ mà cố tin — hễ đòi đóng phí trước là lừa! | ☑ | Hoàn tất Tầng 1 `materialAndDraft` (Gate 0/1/2/3 PASS · `v3-final-level2-abc`, 77.05s WAV thật) |
| `EP13` | `factory619` | `A/D` | `VAR-DOC-01` (mồi link tải đề thi/đề cương ôn tập miễn phí lúc khuya sát giờ thi → lợi dụng người dùng chưa hiểu cơ chế **SSO / đăng nhập một lần** để mở trang ngoài bắt đăng nhập lại chiếm nick mạo danh vay tiền người thân + tệp giả tài liệu giấu mã độc chạy ngầm lấy ảnh riêng tư uy hiếp ép chuyển tiền; kết mở 2.5D Bé Na kịp bấm cảnh báo cả nhóm lớp sáng hôm sau) / `COND-02,05` / `RESP-01,02,04,05` | Mạng xã hội đang dùng không bao giờ bắt đăng nhập lại (chỉ đăng nhập trong chính app mạng xã hội đó) — tài liệu sạch không đòi mật khẩu hay tệp lạ! | ☑ | Đã phát hành Production (Gate 6 · `v2-level3-sso-real-tts`, `77.32s`, `48 MB`, Check 1-2-3 PASS) |
| `EP14` | `factory619` | `A/B` | `VAR-MIX-01` (**cố tình mạo danh trung tâm bảo hành lớn** mua vị trí đứng đầu tìm kiếm → cử 2 thợ mặc đồ công nhân thường tới nhà tận dụng tâm lý ngại đuổi → tháo bo mạch đem đi kèm biên nhận viết tay rồi **im bặt 2 ngày giữa nhà ống nóng ngộp thở để nạn nhân bỏ hết đề phòng, chỉ muốn có máy xài liền** mới gọi báo giá 3 triệu → **đồng ý xong tiếp tục mất hút thêm 5 ngày (tổng cả tuần), gọi số biên nhận không nghe, phải gọi số đầu gào lên mới xuống ráp lấy 3 triệu** → 2 ngày hư y chang, thợ chính hãng bóc trần bo mạch chẳng hư, họ cũng chưa sửa, chỉ rách tem mất luôn bảo hành; kết mở 2.5D Chị Hai chụp lưu tem tổng đài chính hãng) / `COND-02,04,05,09` / `RESP-01,02,03` | Mạo danh trung tâm lớn, giữ bo câu giờ ép nóng là bạn bỏ hết đề phòng — gọi bảo hành chỉ lấy số trên phiếu hoặc tem máy! | ☑ | Đã hoàn tất **Staging `v4-level3-2day-5day-real-tts`** (Gate 0–5 · `79.95s`, `44.13 MB`, 5 giọng tách biệt, 100% đối thoại sống không nhìn camera, đúng mạch mạo danh từ đầu + im 2 ngày đồng ý + câu thêm 5 ngày gọi đòi mới xuống ráp lấy 3tr, `A=2 · B=2 · C=6`, 2×2.5D, 9×Blink, 8×Mouth, 23×L3_FX, Check 1-2-3 PASS, chờ chủ kênh duyệt trước Gate 6) |
