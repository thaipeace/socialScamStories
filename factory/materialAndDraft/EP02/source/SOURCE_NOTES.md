# GHI CHÚ NGUỒN (SOURCE NOTES) — EP02 (`BayPhongVanHackMay`)

- **Họ kịch bản:** `ON-16` — Giả mạo HR tuyển dụng gửi bài kiểm tra (Take-home test / Repo) cài cắm lệnh ngầm chiếm quyền máy tính (Chiến dịch *Contagious Interview* / *Lazarus Group*).
- **Nguồn thực tế trực tiếp:** Bài chia sẻ trải nghiệm thực tế của tác giả **Thai Nguyen** trên LinkedIn:
  - URL: `https://www.linkedin.com/posts/thai-nguyen-a59583135_cybersecurity-jobsearch-developer-share-7508385459602120705-uEml/`
  - Nội dung cốt lõi từ nhân chứng:
    1. Kẻ gian giả danh HR gửi thư mục dự án / bài test, quét virus online lẫn offline đều báo sạch.
    2. Trong cuộc gọi, HR liên tục hối thúc ứng viên **chia sẻ màn hình** và chạy ngay theo hướng dẫn trong README để "xem tiến độ".
    3. Ứng viên cảnh giác không chạy ngay mà hẹn sang ngày hôm sau thì HR tỏ thái độ không vui / khó chịu.
    4. Hôm sau ứng viên mở kiểm tra thủ công thư mục ẩn `.git/hooks/post-checkout` và phát hiện dòng lệnh ngầm `curl ... | sh` tự động tải và thực thi mã độc ngay khi chạy lệnh đầu tiên, nhắm vào mật khẩu, khóa bảo mật và tài sản số.
- **Cách chuyển thể đại chúng:** Giữ nguyên chuỗi tâm lý đắt giá (*Quét ngoài báo sạch → HR hối chia sẻ màn hình mở ngay → Hẹn lại mai thì HR cáu gắt → Kiểm tra thư mục ẩn phát hiện lệnh ngầm cướp mật khẩu*), diễn đạt bằng từ ngữ đời thường để bất kỳ người xem nào cũng hiểu và cảnh giác.
