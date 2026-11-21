# DRAFT Ý TƯỞNG – 196 EP12: CHUYỂN NHẦM THẬT & GIẢ CHUYỂN NHẦM *(Ghi chú ý tưởng · Chờ phát triển sau)*

*Trạng thái: **Ghi nháp ý tưởng (Idea Seed)** · Nhà máy: **`factory196` (16:9 Long-form)** · Áp dụng khung **`STRAT-VIGILANCE-LIB-V1`***

---

## 1. Ý tưởng gốc từ chủ kênh
Dựng một tập phim dài đặt **song song 2 sự kiện xảy ra quanh cùng một hiện tượng "tiền lạ bất ngờ chuyển vào tài khoản"**:
1. **Nhánh A — Chuyển nhầm THẬT nhưng người nhận cố tình không trả:** Khai thác hệ lụy thực tế (bị tra soát, xác minh, nguy cơ vướng trách nhiệm dân sự / hình sự nếu cố tình rút tiêu hoặc từ chối hoàn trả khoản tiền không thuộc về mình).
2. **Nhánh B — GIẢ chuyển nhầm (Bẫy chuyển nhầm):** Kẻ gian cố tình chuyển tiền vào tài khoản nạn nhân, sau đó dùng số lạ gọi khóc lóc/hối thúc nhờ chuyển trả sang **một tài khoản thứ ba khác**, hoặc gửi đường link xác nhận hoàn tiền, hoặc biến khoản tiền đó thành vỏ bọc ép trả nợ/lãi suất cao.

→ **Góc nhìn sắc bén tạo sự khác biệt cho tập:** Ngoài đời, đứng trước một khoản tiền lạ nổ vào tài khoản, **chính người dân — thậm chí ở bước đầu cả người ngoài lẫn cơ quan tiếp nhận — cũng chưa thể nhìn mắt thường mà biết ngay đó là "chuyển nhầm thật" hay "bẫy giả chuyển nhầm"** (*kế trùng kế*). Vì vậy, không cần tự đoán đúng/sai — chỉ cần làm đúng **một quy trình chuẩn duy nhất an toàn cho cả hai trường hợp**.

---

## 2. Định vị trên Khung Thư viện Cảnh giác 3 lớp (`STRAT-VIGILANCE-LIB-V1`)
| Hạng mục | Định hướng dự kiến |
| :--- | :--- |
| **Góc quan sát (Format)** | **`C+F`** – *Hai tình huống song song (Chuyển nhầm thật vs. Giả chuyển nhầm) + Quy trình ứng phó chuẩn* *(lấp khoảng trống Format `C` đầu tiên cho `factory196`)* |
| **Lớp 1 – Biến thể (`VAR`)** | **`VAR-COM-03`** – Bẫy giả chuyển nhầm vào tài khoản (đối ứng với tình huống chuyển nhầm thật) |
| **Lớp 2 – Điểm dễ mắc (`COND`)** | - Nhánh A: Tâm lý *"tiền tự rớt vô túi mình, cứ im rút xài"* hoặc ngại rắc rối không hợp tác.<br>- Nhánh B: Lòng tốt muốn trả nhanh cho xong chuyện (`COND-09`), bị thúc gấp về thời gian (`COND-05`), không biết rủi ro khi chuyển sang tài khoản thứ ba hoặc bấm link. |
| **Lớp 3 – Ứng phó chuẩn (`RESP`)** | **1 quy trình bất biến cho cả 2 nhánh (`RESP-01`, `RESP-02`, `RESP-03`, `RESP-05`):**<br>1. **Không rút tiêu, không đụng vào khoản tiền lạ** (tránh vi phạm pháp luật nếu là chuyển nhầm thật).<br>2. **Không tự chuyển ngược trực tiếp** theo lời người gọi lạ, tuyệt đối không chuyển sang tài khoản khác tên/khác nguồn, không bấm link "xác nhận hoàn trả".<br>3. **Chủ động liên hệ ngân hàng (kênh chính thức / ra quầy)** để làm thủ tục tra soát và chỉ hoàn trả qua ngân hàng hoặc có xác nhận của cơ quan công an. |
| **1 câu neo ký ức (`Recall Anchor`)** | *"Tiền lạ vô tài khoản: **không rút tiêu, không tự chuyển trả theo số lạ** — giữ nguyên đó, chỉ hoàn qua ngân hàng hoặc công an!"* |

---

## 3. Lưu ý kiểm chứng & phát triển kịch bản sau này (`L7` / `L8`)
- Giữ mạch truyện 2 nhánh đan xen trên **cùng một trục bối cảnh/mối quan hệ gọn** (ví dụ 2 đồng nghiệp hoặc 2 người trong cùng khu trọ/gia đình nhận tiền lạ trong cùng giai đoạn) để không bị loãng nhân vật trên phim dài 16:9.
- Kiểm chứng kỹ quy trình hoàn trả tiền chuyển nhầm của ngân hàng và ranh giới pháp lý tội *"Chiếm giữ trái phép tài sản"* (mức giá trị tối thiểu, điều kiện cấu thành sau khi đã có yêu cầu hoàn trả hợp pháp) trước khi viết lời thoại chính thức — không viện dẫn điều luật chưa kiểm chứng.
- Nhấn mạnh giá trị sử dụng thực tế: xem xong tập này, dù gặp **người chuyển nhầm thật** hay **kẻ giăng bẫy giả chuyển nhầm**, người xem đều biết chính xác 3 bước xử lý không bao giờ sai.
