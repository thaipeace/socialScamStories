# QUY CHUẨN ĐỊNH DẠNG PHIM DÀI 16:9 (4 – 5+ PHÚT) – NHÀ MÁY `factory196`
## Phương châm: XEM ĐỂ KHÔNG BỊ LỪA – Câu chuyện đời thực dẫn dắt cảm xúc, bóc trần tận gốc cơ chế

*Tài liệu này quy định chuẩn kỹ thuật, kịch bản, tâm lý, pháp lý và âm thanh – hình ảnh cho nhà máy **`factory196`** (khung ngang `16:9` – `1920x1080`), đúc kết thực chiến từ quá trình cải tiến `EP01` → `EP01b`.*

---

## I. THÔNG SỐ KỸ THUẬT KHUNG HÌNH & THỜI LƯỢNG (`channel_config.json`)

| Hạng mục | Chuẩn `factory196` (Phim dài 16:9) | So sánh với `factory619` (Short 9:16) |
| :--- | :--- | :--- |
| **Độ phân giải & Tỷ lệ** | **`1920 × 1080` (`16:9` Full HD)** @ `30 fps` (cắt sạch viền đen/trắng letterbox) | `1080 × 1920` (`9:16`) @ `30 fps` |
| **Thời lượng chuẩn** | **Linh hoạt từ `240s` (4 phút) đến `330s` (~5,5 phút)** *(tối đa `1800s`; không cố kéo dài cho đủ 5 phút nếu làm loãng nhịp)* | `45s – 90s` (~56s) |
| **Safe Zone ngang (`X`)** | `120 px → 1800 px` (rộng `1680 px`) | `80 px → 920 px` |
| **Safe Zone dọc (`Y`)** | `96 px → 980 px` (chừa `100 px` đáy cho thanh tua YouTube) | `170 px → 1420 px` |
| **Mật độ lời thoại mục tiêu** | **`≤ 26 từ/câu` · `120 – 140 từ/phút` (`~500 – 650 từ` cho tập 4–5 phút)** *(trần cứng Gate 0: `35 từ/câu`, `185 từ/phút`)* | `≤ 22 từ/câu` · `≤ 115 từ/56s` |
| **Tỷ lệ Kịch / Đồ họa** | **`~80%` hành động & đối thoại nhân vật (`≥ 10–16` ảnh có người) · `~20%` sơ đồ & Người Bóc Trần** | `~90%` tình huống · `~10%` kết |
| **Thẻ Dấu Hiệu (`red_flags`)** | `3 – 6 dấu hiệu` + `1 hành động phòng vệ gốc` | `2 – 4 dấu hiệu` + `1 việc nên làm` |
| **Thư mục xuất bản Master** | `06_RENDERED_VIDEOS/` | `06_RENDERED_SHORTS/` |

---

## II. 7 NGUYÊN TẮC CỐT LÕI CHO PHIM DÀI ĐẠI CHÚNG (ĐÚC KẾT TỪ `EP01b`)

### 1. Không làm "bài giảng nghiệp vụ" – Để nhân vật sống thật trong câu chuyện (`80% Kịch / 20% Đồ họa`)
- Nhân vật **không xuất hiện chỉ để truyền tải thông tin hay giảng giải pháp luật**. Mỗi câu nói, hành động phải xuất phát từ nhu cầu, nỗi sợ, sĩ diện hoặc sự cả tin rất đời của họ.
- **Tập trung vào 1 nhân vật chính rõ rệt** (ví dụ: Tùng ở `EP01b`): đầu tư hoàn cảnh sống, áp lực tài chính/gia đình, tâm lý che giấu người thân, lý do chọn đường tắt trước khi biến cố ập tới. Các nhân vật đi cùng (như vợ chồng Anh Hai – Chị Hai) đóng vai đối trọng tỉnh táo, không chia nhỏ đất diễn dàn trải.
- **Hạn chế sơ đồ cắt ngang vụn vặt:** Giữ tỷ lệ khoảng `80%` cảnh diễn biến con người (phối hợp toàn cảnh, trung cảnh, cận cảnh đạo cụ/biểu cảm) và chỉ `~20%` sơ đồ minh họa cô đọng + phần tổng kết của `Người Bóc Trần` ở cuối phim. Không nhét nhân vật hàng xóm lớn tuổi vào hiện trường chỉ để đứng giảng luật gượng ép.

### 2. Thoại ngắn, sắc, đời thường – Cắt bỏ câu giải thích dài dòng
- Viết câu ngắn gọn, đúng khẩu ngữ miền Nam đời thực, đủ ý là dừng (`≤ 26 từ/câu`, tổng tập 4–5 phút chỉ khoảng `500 – 650 từ`).
- Thay câu thuyết minh dài bằng hành động hoặc 1 câu thoại đắt giá để khán giả tự hiểu (ví dụ: thay vì nhân vật đứng than vãn giải thích cơ chế cả đoạn dài, chỉ cần 1 câu chua chát trên đường về hoặc 1 chi tiết lặng lẽ đặt chìa khóa xe lên bàn).

### 3. Phân biệt rõ rệt giọng các nhân vật cùng giới tính (`Distinct Voice Separation`)
- Khi trong tập phim (đặc biệt trong cùng một cảnh) có **từ 2–3 nhân vật nam hoặc nữ trở lên**, **bắt buộc tách hẳn `voice` và `style`** về độ trầm/sáng, chất giọng và tốc độ nói để người xem nghe không nhìn hình vẫn phân biệt được ngay:
  - **Tuyến Nam mẫu (`EP01b`):** Thanh niên trẻ tông cao, sáng, nhịp nhanh (`Puck`) ≠ Người anh cả trầm, hơi khàn, chậm chắc (`Algenib` / `Orus`) ≠ Kẻ làm dịch vụ mượt, êm, lịch sự lạnh (`Algieba` / `Achird`) ≠ Người Bóc Trần điềm tĩnh (`Charon`).
  - **Tuyến Nữ mẫu (`EP01b`):** Người mẹ ở quê trầm ấm, chậm rãi (`Gacrux`) ≠ Người vợ trẻ sắc sảo, dứt khoát (`Kore`) ≠ Nhân viên tổng đài chuẩn mực (`Zephyr` + `af: "phone"`).

### 4. Kẻ thao túng đáng sợ vì "bình thường hóa", không phải vì gào thét
- Dân môi giới / dịch vụ ngầm / kẻ thao túng ngoài đời không tỏ ra gian ác ngay từ đầu. Họ tạo cảm giác: *"Khách quen làm mỗi ngày"*, *"Nguy hiểm thì bên em làm được mấy năm nay sao?"*, *"Anh cứ để em lo"*.
- Khi xảy ra sự cố kẹt tiền ở khu dân cư, họ **không khóa cửa bắt nhốt người như phim hành động** (vì phạm tội *Giữ người trái pháp luật* và sợ lộ ổ làm ăn chui), mà đổi sắc mặt lạnh tanh, gây sức ép ngầm bằng sao kê chuyển khoản và việc nắm rõ địa chỉ nhà/công ty của nạn nhân.

### 5. Logic đời thực & Pháp lý chuẩn xác – Không cưỡng ép tình tiết vô lý
- **Không ép kịch bản "lừa đảo giật tiền một lần" vào cơ sở quen biết có địa chỉ cố định:** Chỗ làm ăn phi pháp kiếm phí đều đặn từ khách quen sẽ không tự phá mối vì một vố nhỏ. Hãy khai thác **chính rủi ro nổ chậm thật sự của dịch vụ trái phép đó** làm cao trào chính (ví dụ: ngân hàng khóa thẻ/gọi xác minh ngay giữa lúc đáo hạn khiến nợ ngân hàng biến thành nợ tiền mặt phải trả ngay), còn thủ đoạn lừa đảo online (chụp 2 mặt thẻ CVV, đọc OTP) đưa vào lời cảnh báo mở rộng ở Hồi 5.
- **Không dùng việc tố giác công an làm đòn mặc cả một chiều** khi bản thân người dùng dịch vụ cũng có lỗi vi phạm (như tham gia quẹt khống). Nút thắt phải gỡ bằng tính toán lợi hại thực tế của hai bên (chuyển về hoàn trả tiền gốc dân sự, không lãi ngày).
- **Kiểm chứng kỹ nghiệp vụ tài chính & pháp luật:**
  - Không nói sai cơ chế (ví dụ: nợ thẻ đã được chuyển tiền tất toán thì không ghi nợ xấu CIC; điều kiện chuyển trả góp / mức tối thiểu tùy từng ngân hàng nên chỉ khuyên *"hỏi trực tiếp ngân hàng"*, không hứa chắc duyệt hay nêu cứng %; Luật Căn cước 2023 cấm giữ/cầm cố thẻ căn cước; không nêu số điều luật hình sự khi chưa kiểm chứng; nói rõ người tham gia giao dịch khống cũng vi phạm).
  - **Xưng hô gia đình chuẩn xác:** Vợ của **Anh Hai** phải gọi là **Chị Hai** (`label_short: "CHỊ HAI"`), không gọi nhầm thành "Chị Ba".

### 6. Đồng bộ chuyển cảnh & Điểm vào giọng thoại (`Scene Cut Before Voice`)
- **Hình vào trước tiếng (`0.25s – 0.4s`):** Khi chuyển sang bối cảnh/nhân vật mới, cảnh hình ảnh mới bắt buộc phải cắt vào trước ít nhất `0.25 – 0.4 giây` rồi giọng nhân vật của cảnh đó mới vang lên. Tuyệt đối không để tiếng của nhân vật cảnh sau phát chồng lên cuối hình của cảnh trước (trừ kỹ thuật J-cut có chủ đích ở giây mở màn Hook).

### 7. Dàn lại Timeline theo thời lượng giọng TTS thật (`Real-TTS Retiming`)
- Cấm cắt chữ, cấm dùng `atempo`/`asetrate` ép tốc độ giọng.
- Sau khi Gate 2 sinh xong toàn bộ WAV thật, phải căn lại `start`, `window`, điểm cắt `scenes`, `chapters`, `thumbnail_sec` và **mốc thời gian YouTube Chapters trong `publish.description`** khớp 100% với độ dài audio thực tế (nằm gọn trong khoảng `240s+`).

---

## III. KHUNG CẤU TRÚC 5 HỒI MẪU (`4 – 5+ PHÚT`)

| Hồi | Thời lượng gợi ý | Vai trò kịch tính |
| :--- | :---: | :--- |
| **Mở màn – Hook** | `0:00 – 0:20` | Khoảnh khắc biến cố trực diện ngay tại hiện trường (không báo cáo dài dòng), đặt câu hỏi kéo khán giả ở lại. Thẻ `hook` hiện trước `2.0s`. |
| **Hồi 1 – Đời tư & Nguyên nhân gốc** | `0:20 – 1:20` | Hoàn cảnh sống, tính cách, áp lực thật khiến nhân vật chính bước vào con đường tắt / dịch vụ rủi ro. |
| **Hồi 2 – Lời rủ rê & Điểm mù tâm lý** | `1:20 – 2:10` | Sự tự tin mù quáng của người trong cuộc đối lập với câu hỏi tỉnh táo của người thân (phát hiện phí chồng phí, dấu hiệu bất thường). |
| **Hồi 3 – Hiện trường & Cú sập bẫy / Sự cố** | `2:10 – 3:10` | Không khí "bình thường hóa" tại hiện trường → sự cố nổ ra theo nhiều nhịp leo thang (từ chối giao dịch, cuộc gọi xác minh, lật mặt). |
| **Hồi 4 – Thế kẹt & Cái giá thật** | `3:10 – 4:10` | Xung đột tâm lý căng thẳng, người thân kịp chặn vạ lây, thỏa thuận trả giá đắt nhưng đúng thực tế & đúng luật. |
| **Hồi 5 – Bóc trần & Phòng vệ** | `4:10 – 5:00` | Cách xử lý chính thống sáng hôm sau + `Người Bóc Trần` đúc kết ngắn gọn cơ chế, trách nhiệm pháp lý, cảnh báo mở rộng + Bảng `NHỚ KỸ (3–6 ý)` + `Disclaimer`. |

---

## IV. LỆNH VẬN HÀNH NHÀ MÁY `factory196`

```powershell
# 1. Tạo tập phim dài mới (mặc định 270s = 4p30s, hợp lệ từ 240s = 4p trở lên)
python factory196/_engine/run.py new EP02 --slug TenTapPhim --title "Tên tập phim dài" --duration 270

# 2. Kiểm tra đầu vào Gate 0
python factory196/_engine/run.py gate0 EP02

# 3. Chạy thật Gate 2 → Gate 5 (dàn lại timeline sau Gate 2 theo độ dài TTS thật, luôn dừng ở Staging)
python factory196/_engine/run.py gate EP02 2
python factory196/_engine/run.py gate EP02 3
python factory196/_engine/run.py gate EP02 4
python factory196/_engine/run.py gate EP02 5

# 4. Sau khi chủ kênh xem & nghe duyệt bản Staging MP4:
python factory196/_engine/run.py signoff EP02 --listen PASS --point 2 4 5 --by "Chủ kênh"
python factory196/_engine/run.py gate EP02 5 --skip-render
python factory196/_engine/run.py gate EP02 6
```
