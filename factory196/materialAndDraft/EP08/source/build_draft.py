# -*- coding: utf-8 -*-
"""
Trình biên dịch `factory196/materialAndDraft/EP08/episode.json` – Tập EP08:
"Một vòng tiền, hai nửa sự thật" (16:9 Long-form · v2-draft).

Nguồn sự thật duy nhất của timeline: sửa thoại/nhịp ở phần STORY rồi chạy lại
    python3 factory196/materialAndDraft/EP08/source/build_draft.py
Tự đọc độ dài WAV thật trong `audio/tts/` (nếu đã chạy Gate 2) để căn khớp 100%
từng câu, từng cảnh, chapter và mốc YouTube Chapters (không dùng atempo/asetrate).
"""
from __future__ import annotations

import json
import wave
from pathlib import Path

HERE = Path(__file__).resolve().parent
EP = HERE.parent
TTS = EP / "audio" / "tts"
OUT = EP / "episode.json"

SEC_PER_WORD = 0.34
LINE_BASE = 0.90
GAP = 0.34
SCENE_LEAD = 0.35          # hình vào trước tiếng 0.25–0.4s
WINDOW_MARGIN = 1.6


def wav_dur(lid: str) -> float | None:
    p = TTS / f"{lid}.wav"
    if not p.is_file():
        return None
    with wave.open(str(p), "rb") as wf:
        return round(wf.getnframes() / wf.getframerate(), 3)


real = {p.stem: wav_dur(p.stem) for p in TTS.glob("*.wav")} if TTS.is_dir() else {}
real = {k: v for k, v in real.items() if v}

# ---------------------------------------------------------------- GIỌNG
# 8 tuyến nhân vật = 8 voice hoàn toàn tách biệt trong 02_CAST/cast.json
# (DAT_FAKE chủ đích dùng đúng voice Orus + af="phone" cho cú gọi ghép 3s;
#  LONG_P dùng đúng voice Algieba + af="phone" để nối mượt sang nhân vật Long ở EP08b)
NOT_OLD = "tuyệt đối không giả giọng ông già hay bà già run rẩy, không kéo dài chữ, không cải lương"
DAT_BASE = (
    "Giọng nam miền Nam Sài Gòn 38 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
    "giữ cố định một âm sắc trầm chắc, điềm tĩnh, thẳng tính, nói gọn cộc thực dụng, rõ chữ, tự nhiên như đời thực, "
    + NOT_OLD
)
KHANG_BASE = (
    "Giọng nam thanh niên miền Nam Sài Gòn 26 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
    "giữ cố định một âm sắc sáng trẻ, nhịp nhanh gọn, thật thà lễ phép, rõ chữ, tự nhiên như đời thực, " + NOT_OLD
)
KE_BASE = (
    "Giọng nam miền Nam Sài Gòn 40 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
    "giữ cố định một âm sắc trầm đều, lạnh tĩnh, điềm nhiên như kẻ cầm quân cờ, không la hét, " + NOT_OLD
)
SPK = {
    "DAT": dict(
        speaker="anh_hai",
        voice="Orus",
        label_short="ANH ĐẠT",
        speaker_label="Anh Đạt – chủ xưởng nội thất nhỏ 38 tuổi, điềm tĩnh, sòng phẳng, quý nhân viên",
        base=DAT_BASE,
    ),
    "DAT_FAKE": dict(
        speaker="anh_hai",
        voice="Orus",
        af="phone",
        label_short="ANH ĐẠT (HÌNH GHÉP)",
        speaker_label="Giọng cắt ghép giống Anh Đạt trong cuộc gọi video 3 giây chập chờn",
        base=DAT_BASE,
    ),
    "KHANG": dict(
        speaker="thang_tun",
        voice="Puck",
        label_short="KHANG",
        speaker_label="Khang – kỹ thuật viên 26 tuổi, theo Anh Đạt 3 năm, chịu khó, rất nể sếp",
        base=KHANG_BASE,
    ),
    "KHANG_P": dict(
        speaker="thang_tun",
        voice="Puck",
        af="phone",
        label_short="KHANG",
        speaker_label="Khang gọi qua điện thoại cho Anh Đạt",
        base=KHANG_BASE,
    ),
    "QUYEN": dict(
        speaker="chi_hai",
        voice="Sulafat",
        label_short="CHỊ QUYÊN",
        speaker_label="Chị Quyên – vợ Anh Đạt 36 tuổi, thực tế, kiệm lời, quản lý tài khoản chung gia đình",
        base=(
            "Giọng phụ nữ miền Nam Sài Gòn 36 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
            "giữ cố định một âm sắc ấm, trầm vừa, nói gọn chắc, điềm tĩnh, tự nhiên như đời thực, " + NOT_OLD
        ),
    ),
    "HAN": dict(
        speaker="chi_tu",
        voice="Zephyr",
        label_short="HÂN",
        speaker_label="Hân – đồng nghiệp nữ 27 tuổi ngồi bàn kế Khang ở văn phòng xưởng",
        base=(
            "Giọng nữ trẻ miền Nam Sài Gòn 27 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
            "giữ cố định một âm sắc sáng gọn, thân thiện, tự nhiên kiểu đồng nghiệp văn phòng, " + NOT_OLD
        ),
    ),
    "KE_ROOM": dict(
        speaker="chu_no",
        voice="Fenrir",
        af="default",
        label_short="KẺ ĐỨNG GIỮA",
        speaker_label="Kẻ đứng giữa giấu mặt trong phòng tối – bàn kế hoạch với cấp dưới",
        base=KE_BASE,
    ),
    "KE_MSG": dict(
        speaker="chu_no",
        voice="Fenrir",
        af="phone",
        label_short="KẺ ĐỨNG GIỮA",
        speaker_label="Kẻ đứng giữa gõ tin nhắn điều phối từ phòng tối, nhái đúng văn phong Anh Đạt",
        base=KE_BASE,
    ),
    "TECH": dict(
        speaker="ke_ngot_ngao_nam",
        voice="Achird",
        af="default",
        label_short="ĐÀN EM",
        speaker_label="Cấp dưới giấu mặt trong phòng tối – đọc lén tin nhắn và lo phần hình/giọng ghép",
        base=(
            "Giọng nam miền Nam Sài Gòn 28 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
            "giữ cố định một âm sắc gọn, hơi nhanh, tỉnh bơ kiểu dân kỹ thuật làm việc trong phòng tối, " + NOT_OLD
        ),
    ),
    "LONG_P": dict(
        speaker="ke_ngot_ngao_nam",
        voice="Algieba",
        af="phone",
        label_short="ĐẦU DÂY LẠ",
        speaker_label="Đầu dây lạ gọi từ phòng công chứng (chính là giọng Long trong EP08b – cài nối liên hoàn)",
        base=(
            "Giọng nam miền Nam Sài Gòn 32 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
            "giữ cố định một âm sắc sáng vừa, mượt mà, lịch sự nhanh gọn kiểu dân văn phòng, " + NOT_OLD
        ),
    ),
    "N": dict(speaker="nguoi_boc_tran"),
}

MOTION = {
    "calm": {"scale": [1.02, 1.09], "focus": [[0.50, 0.50], [0.50, 0.47]], "wobble": "calm"},
    "tense": {"scale": [1.04, 1.14], "focus": [[0.50, 0.50], [0.48, 0.45]], "wobble": "tense"},
    "push": {"scale": [1.00, 1.16], "focus": [[0.50, 0.50], [0.50, 0.45]], "wobble": "calm"},
    "hand": {"scale": [1.02, 1.10], "focus": [[0.46, 0.48], [0.54, 0.46]], "wobble": "handheld"},
    "still": {"scale": [1.00, 1.05], "focus": [[0.50, 0.50], [0.50, 0.50]], "wobble": "none"},
}

E: list[tuple[str, object]] = []


def scene(sid: str, img: str, m: str = "calm", tr: str | None = None, trd: float = 0.4, shake: float | None = None):
    E.append(("scene", dict(id=sid, image=img, motion=MOTION[m], tr=tr, trd=trd, shake=shake)))


def line(lid: str, spk: str, text: str, emo: str = "", sub: str | None = None, pause: float = 0.0):
    E.append(("line", dict(id=lid, spk=spk, text=text, emo=emo, sub=sub, pause=pause)))


def beat(sec: float):
    E.append(("beat", sec))


def chapter(kicker: str, title: str, offset: float = 0.2, dur: float = 4.4):
    E.append(("chapter", dict(kicker=kicker, title=title, offset=offset, dur=dur)))


def bubble(sender: str, text: str, side: str = "left", y: int = 260, stamp: str | None = None,
           dur: float = 4.6, offset: float = 0.0):
    E.append(("bubble", dict(sender=sender, text=text, side=side, y=y, stamp=stamp, dur=dur, offset=offset)))


def sfx(preset: str, offset: float = 0.0, gain: float = -4.0, dur: float | None = None):
    E.append(("sfx", dict(preset=preset, offset=offset, gain=gain, dur=dur)))


def amb(preset: str, gain: float = -2.0):
    E.append(("amb", dict(preset=preset, gain=gain)))


def bgm(preset: str, gain: float = -3.0):
    E.append(("bgm", dict(preset=preset, gain=gain)))


def mark(name: str):
    E.append(("mark", name))


SILENT = -40.0
EP01B = "factory196/materialAndDraft/EP01b/assets/"

# ================================================================ STORY
# ---- HOOK · CUỘC GỌI LẦN HAI & CÂU HỎI ĐÓNG BĂNG (00:00 – 00:24) ----
amb("office", -2.5); bgm("suspense_pulse", -2.5)
scene("s00_hook_call", "assets/c00.jpg", "push", shake=0.2)
sfx("phone_ring", 0.15, -4, dur=1.2)
bubble("CUỘC GỌI ĐẾN · KHANG", "Lần 2 trong ngày · Xin mượn thêm 30.000.000đ",
       side="left", y=260, stamp="LẦN THỨ HAI", dur=4.6, offset=0.2)
beat(1.4)
line("l01_dat", "DAT", "Sáng mày mới xin ứng bốn lăm triệu. Giờ mới chiều đã hỏi thêm ba chục… Mày vướng chuyện gì nói thiệt anh coi!",
     "giọng đanh lại, nhíu mày lo lắng lẫn nghi ngờ",
     sub="Sáng mày mới xin ứng 45 triệu. Giờ mới chiều đã hỏi thêm 30… Mày vướng chuyện gì nói thiệt anh coi!")
line("l02_khang_p", "KHANG_P", "Ủa anh… em đang gọi diễn đúng như lời anh nhắn hồi nãy mà!",
     "ngơ ngác qua điện thoại, tưởng sếp đang đóng kịch trước mặt vợ")
line("l03_dat", "DAT", "Tao nhắn cho mày hồi nào?!",
     "sững lại, cắt ngang dứt khoát")

scene("s01_hook_freeze", "assets/c01.jpg", "tense", tr="flash_white", trd=0.22, shake=0.15)
mark("hook_freeze")
sfx("impact", 0.0, -2.5)
bubble("ANH ĐẠT (NICK MỚI)", "Mượn anh thêm 30.000.000đ · Như sáng nay",
       side="left", y=260, stamp="AI ĐANG NHẮN?", dur=2.5, offset=0.15)
sfx("heartbeat", 0.2, -5, dur=2.2)
beat(2.8)

# ---- HỒI 1 · HAI HÔM TRƯỚC: CÁCH NÓI CHUYỆN ĐẶC TRƯNG & KẾ HOẠCH PHÒNG TỐI ----
amb("street", -5.0); bgm("investigative_story", -3.8)
scene("s02_trust_coffee", "assets/c02.jpg", "calm", tr="fade_black", trd=0.45)
chapter("HỒI 1 · HAI HÔM TRƯỚC", "CÁCH NÓI CHUYỆN & KẾ HOẠCH PHÒNG TỐI")
sfx("chapter_sting", -0.1, -5)
beat(0.8)
# Cài rõ khẩu ngữ đặc trưng của Anh Đạt: "Nè cu Khang", "gọn ghẽ", "anh tính", "chị nhà", "lộ bài"
line("l04_dat", "DAT", "Nè cu Khang, mấy công trình đợt này mày chạy gọn ghẽ quá. Cuối tháng anh tính thêm cho.",
     "cười thoải mái bên ly cà phê sáng, nói cộc gọn đầy tin cậy")
line("l05_khang", "KHANG", "Anh em làm chung ba năm rồi, tính toán chi anh. Có việc gì cứ kêu em.",
     "cười tươi, lễ phép và rất quý sếp")
line("l06_dat", "DAT", "Ừ, tuần sau kỷ niệm mười năm ngày cưới. Rảnh phụ anh kiếm quà cho chị nhà, đừng để bả biết lộ bài nghen.",
     "hạ giọng vui vẻ, dặn dò thân mật đúng kiểu người đàn ông thực dụng",
     sub="Ừ, tuần sau kỷ niệm 10 năm ngày cưới. Rảnh phụ anh kiếm quà cho chị nhà, đừng để bả biết lộ bài nghen.")
line("l07_khang", "KHANG", "Dạ dễ ợt, anh chọn xong cứ nhắn em làm gọn.",
     "gật đầu nhanh nhẹn, tự tin", pause=0.3)

# Phòng tối ánh xanh lạnh: KHÔNG dùng bong bóng dài — hai gã bàn nhau rõ ràng để người xem NGHE LÀ HIỂU 100%!
amb("night_room", -2.5); bgm("tension_drone", -2.8)
scene("s03_dark_room_plan", "assets/c03.jpg", "push", tr="fade_black", trd=0.4)
mark("two_phones")
sfx("typing", 0.2, -5, dur=1.2)
beat(0.8)
line("l08_tech", "TECH", "Tin nhắn cũ của ông Đạt em đọc kỹ rồi. Ổng nói cộc lắm, cứ mở miệng kêu cu Khang, gọi vợ là chị nhà.",
     "vừa lướt màn hình bên trái vừa báo cáo gọn gàng")
line("l09_ke", "KE_ROOM", "Tốt, nhắn y chang kiểu đó. Tới lúc cần thì nhá cuộc gọi hình ghép ba giây, cắt giọng từ tin cũ rồi cúp liền.",
     "lạnh tĩnh chỉ đạo, giọng trầm đều không vội vã",
     sub="Tốt, nhắn y chang kiểu đó. Tới lúc cần thì nhá cuộc gọi hình ghép 3 giây, cắt giọng từ tin cũ rồi cúp liền.")
line("l10_tech", "TECH", "Đổ tại mạng yếu là nó tin liền. Mà mượn thẳng thằng Khang thì sao nó có tiền nhiều?",
     "hỏi gọn đúng trọng tâm cơ chế")
line("l11_ke", "KE_ROOM", "Không mượn nó. Bày nó gọi số thật ông Đạt xin ứng bốn lăm triệu. Sếp tự chuyển cho lính, rồi lính đẩy qua mình.",
     "điềm nhiên chốt toàn bộ nước cờ hai đầu dây",
     sub="Không mượn nó. Bày nó gọi số thật ông Đạt xin ứng 45 triệu. Sếp tự chuyển cho lính, rồi lính đẩy qua mình.",
     pause=0.35)

# ---- HỒI 2 · SÁNG HÔM SAU: CUỘC GỌI HÌNH GHÉP 3 GIÂY & VĂN PHONG Y HỆT ----
amb("office", -3.0); bgm("suspense_pulse", -3.0)
scene("s04_fake_video_call", "assets/c04.jpg", "tense", tr="fade_black", trd=0.4)
chapter("HỒI 2 · SÁNG HÔM SAU", "CUỘC GỌI HÌNH GHÉP & NHÁI GIỌNG SẾP")
sfx("chapter_sting", -0.1, -5)
sfx("phone_ring", 0.3, -4, dur=1.1)
beat(1.3)
sfx("glitch", 0.0, -3)
bubble("CUỘC GỌI VIDEO · ANH ĐẠT (NICK MỚI)", "Tín hiệu yếu · Đã kết thúc (00:03)",
       side="left", y=260, stamp="HÌNH GHÉP 3 GIÂY", dur=4.8, offset=0.1)
line("l12_dat_fake", "DAT_FAKE", "Nè cu Khang! Mạng chỗ xưởng gỗ yếu quá hình giật hết trơn… Thôi cúp nha, anh nhắn tin cho gọn!",
     "gấp gáp, hơi đứt quãng như sóng yếu qua cuộc gọi video ngắn")
sfx("glitch", 0.0, -3)
sfx("call_end", 0.2, -3)
beat(0.5)

# Cắt chéo phòng tối: gã điều phối gõ Nhịp 1 nhái Y HỆT cách nói chuyện của Anh Đạt
amb("night_room", -2.8); bgm("suspense_pulse", -3.2)
scene("s05_fake_step1_dark", "assets/c05.jpg", "tense", tr="dissolve", trd=0.3)
sfx("message_send", 0.2, -4)
bubble("ANH ĐẠT (NICK MỚI)", "Gọi số cũ xin ứng 45tr · Giữ bí mật cho chị nhà",
       side="left", y=260, stamp="NHỊP 1 · NHÁI GIỌNG", dur=5.6, offset=0.2)
beat(0.6)
line("l13_ke", "KE_MSG", "Nè cu Khang, anh đặt đồng hồ kỷ niệm cho chị nhà rồi. Tài khoản chung anh tự chuyển là lộ bài liền.",
     "cộc gọn đúng nhịp nói của Anh Đạt")
line("l14_ke", "KE_MSG", "Trưa nay gọi số cũ xin ứng bốn lăm triệu, nói dưới quê có việc gấp. Làm gọn giùm anh, xong việc anh tính.",
     "nhái y hệt câu cửa miệng của Anh Đạt",
     sub="Trưa nay gọi số cũ xin ứng 45 triệu, nói dưới quê có việc gấp. Làm gọn giùm anh, xong việc anh tính.",
     pause=0.3)

# Cắt về văn phòng sáng nắng: Khang không tự nói một mình — thoại tự nhiên với đồng nghiệp Hân
amb("office", -3.0); bgm("investigative_story", -4.0)
scene("s06_office_relay", "assets/c06.jpg", "calm", tr="dissolve", trd=0.35)
beat(0.4)
line("l15_han", "HAN", "Ủa Khang, gần trưa rồi còn đi đâu mà cười tủm tỉm vậy?",
     "ngước từ bàn bên nhìn qua, hỏi đùa nhẹ nhàng")
line("l16_khang", "KHANG", "Anh Đạt nhờ đặt quà kỷ niệm cho chị nhà. Ảnh mới gọi hình qua nick mới mà mạng yếu quá nên nhắn tiếp.",
     "ghé nhỏ giọng vui vẻ, hoàn toàn tin vì đã thấy mặt nghe giọng")
line("l17_han", "HAN", "Chà, sếp cưng vợ ghê ha. Mà sao ảnh hông tự chuyển tiền luôn?",
     "cười hỏi tự nhiên")
line("l18_khang", "KHANG", "Tài khoản nhà chị Quyên giữ chung, ảnh tự chuyển lộ bài liền. Tiền của ảnh mà, mình phụ một tay thôi.",
     "xua tay nhẹ, thấy chuyện hợp lý tuyệt đối", pause=0.3)

# ---- HỒI 3 · BUỔI TRƯA: DÒNG TIỀN ĐI MỘT VÒNG ----
amb("room_tone", -3.0); bgm("investigative_story", -3.5)
scene("s07_real_call_home", "assets/c07.jpg", "calm", tr="fade_black", trd=0.45)
chapter("HỒI 3 · BUỔI TRƯA", "DÒNG TIỀN ĐI MỘT VÒNG")
sfx("chapter_sting", -0.1, -5)
sfx("phone_ring", 0.3, -4, dur=1.1)
beat(1.3)
line("l19_khang_p", "KHANG_P", "Alo anh Đạt… Dưới quê nhà em đột xuất có việc gấp, anh cho em ứng trước bốn lăm triệu được hông?",
     "hơi vội vã nhập vai qua điện thoại",
     sub="Alo anh Đạt… Dưới quê nhà em đột xuất có việc gấp, anh cho em ứng trước 45 triệu được hông?")
line("l20_dat", "DAT", "Chuyện gấp hả cu Khang? Rồi, để anh chuyển qua tài khoản mày liền, lo xong rồi tính.",
     "không chút nghi ngờ vì nghe đúng giọng người em quen")
line("l21_quyen", "QUYEN", "Thằng Khang làm với mình ba năm nay đàng hoàng. Anh cứ ghi rõ nội dung ứng lương rồi chuyển cho nó đi.",
     "ngồi bên mâm cơm, điềm tĩnh gật đầu thực tế")
sfx("bank_ting", 0.1, -3)
bubble("NGÂN HÀNG CỦA ĐẠT", "Chuyển sang Khang: -45.000.000đ · ND: Ung luong",
       side="left", y=260, stamp="1 · ĐẠT → KHANG", dur=4.8, offset=0.1)
beat(0.7)
line("l22_dat", "DAT", "Rồi, anh mới chuyển bốn lăm triệu xong đó. Lo gọn việc dưới quê đi nghen.",
     "bấm xong điện thoại, dặn gọn rồi tắt máy",
     sub="Rồi, anh mới chuyển 45 triệu xong đó. Lo gọn việc dưới quê đi nghen.")
sfx("call_end", 0.0, -4)
beat(0.35)

# Cắt chéo sang phòng tối (12:05): cài thoáng giọng Long (Algieba) từ đầu dây phòng công chứng → bắc cầu sang EP08b
amb("night_room", -2.5); bgm("suspense_pulse", -2.5)
scene("s08_dark_step2_account", "assets/c08.jpg", "push", tr="dissolve", trd=0.35)
sfx("notification", 0.1, -4)
beat(0.4)
line("l22b_long_p", "LONG_P", "Em tới quầy công chứng rồi, bên bán chờ tiền vô là ký.",
     "nói gọn qua loa điện thoại từ nơi ồn ào, khớp đúng giọng Long ở EP08b", pause=0.2)
sfx("message_send", 0.1, -3)
bubble("ANH ĐẠT (NICK MỚI)", "Chuyển 45.000.000đ vô TK cửa hàng này",
       side="left", y=260, stamp="2 · GỬI STK LẠ", dur=5.2, offset=0.15)
beat(0.5)
line("l23_ke", "KE_MSG", "Tiền vô rồi hả cu Khang? Đẩy bốn lăm triệu vô số tài khoản cửa hàng này gọn giùm anh, họ giao thẳng về xưởng.",
     "bình thản, giữ đúng kiểu nói cộc gọn của Anh Đạt",
     sub="Tiền vô rồi hả cu Khang? Đẩy 45 triệu vô số tài khoản cửa hàng này gọn giùm anh, họ giao thẳng về xưởng.",
     pause=0.25)

# Khang bấm chuyển tiền ngay — dòng tiền 3 bước hoàn tất
amb("office", -3.5); bgm("tension_drone", -2.8)
scene("s09_khang_transfers", "assets/c09.jpg", "hand", tr="dissolve", trd=0.3)
mark("money_loop")
sfx("typing", 0.15, -5, dur=0.9)
sfx("bank_ting", 1.1, -2.5)
bubble("NGÂN HÀNG CỦA KHANG", "Đã chuyển: -45.000.000đ → TK ••••",
       side="left", y=260, stamp="3 · KHANG → KẺ GIAN", dur=3.0, offset=1.1)
beat(4.3)

# ---- HỒI 4 · BỐN GIỜ CHIỀU: NHỊP THỨ HAI & PHÚT VỠ LẼ ----
amb("night_room", -2.5); bgm("tension_drone", -2.0)
scene("s10_second_attempt_dark", "assets/c10.jpg", "tense", tr="fade_black", trd=0.4)
chapter("HỒI 4 · BỐN GIỜ CHIỀU", "NHỊP THỨ HAI & PHÚT VỠ LẼ")
sfx("chapter_sting", -0.1, -5)
sfx("message_send", 0.3, -4)
bubble("ANH ĐẠT (NICK MỚI)", "Gọi số cũ mượn anh thêm 30.000.000đ",
       side="left", y=260, stamp="NHỊP 2 · ĐÒI THÊM", dur=5.0, offset=0.3)
beat(0.7)
line("l24_ke", "KE_MSG", "Cu Khang, cửa hàng còn thêm món quà kèm đẹp quá. Gọi số cũ mượn anh thêm ba chục triệu, làm gọn giùm anh nha.",
     "thản nhiên lặp lại đúng văn phong cũ",
     sub="Cu Khang, cửa hàng còn thêm món quà kèm đẹp quá. Gọi số cũ mượn anh thêm 30 triệu, làm gọn giùm anh nha.")

# Nối tiếp ngay sau câu hỏi ở Hook
amb("office", -2.5); bgm("action_climax", -2.5)
scene("s11_real_call_suspect", "assets/c11.jpg", "tense", tr="dissolve", trd=0.3, shake=0.15)
sfx("riser", 0.0, -4, dur=1.0)
beat(0.45)
line("l25_dat", "DAT", "Mày đứng yên đó, chạy thẳng qua phòng anh ngay! Đem cái điện thoại qua đây cho anh coi!",
     "gấp gáp, nghiêm giọng dứt khoát")
sfx("call_end", 0.0, -3)
beat(0.55)

# Đối chất trực diện: hai điện thoại đặt cạnh nhau trên bàn
amb("office", -3.0); bgm("action_climax", -2.2)
scene("s12_confrontation_desk", "assets/c12.jpg", "tense", tr="flash_white", trd=0.22, shake=0.18)
mark("confrontation")
sfx("impact", 0.0, -2.5)
beat(0.45)
line("l26_khang", "KHANG", "Anh coi nè! Hồi sáng nó còn gọi hình đúng mặt đúng giọng anh, nhắn y chang kiểu cu Khang, chị nhà luôn mà!",
     "hốt hoảng đặt điện thoại xuống bàn, giọng run lên")
line("l27_dat", "DAT", "Tài khoản này đâu phải của anh! Mà sao nó có clip mặt anh với biết tuần sau kỷ niệm ngày cưới?!",
     "sững sờ nhìn màn hình, giọng trầm nặng")
line("l28_dat", "DAT", "Khoan… hồi khuya máy anh có báo đăng nhập từ thiết bị khác. Anh tưởng lỗi mạng nên bấm bỏ qua mất tiêu rồi!",
     "mở máy mình lên, chợt giật mình nhận ra lỗ hổng", pause=0.2)
sfx("phone_ring", 0.0, -5, dur=0.9)
sfx("call_end", 0.95, -3)
beat(1.05)
line("l29_khang", "KHANG", "Nó chặn mất rồi anh Đạt ơi… Bốn mươi lăm triệu em vừa chuyển qua tài khoản lạ rồi!",
     "tái mặt, giọng nghẹn lại khi gọi nick giả không còn liên lạc được",
     sub="Nó chặn mất rồi anh Đạt ơi… 45 triệu em vừa chuyển qua tài khoản lạ rồi!")
line("l30_dat", "DAT", "Bình tĩnh lại. Gọi tổng đài ngân hàng liền đi, rồi gom hết sao kê với tin nhắn đi trình báo công an!",
     "kìm giọng dứt khoát, xử lý ngay lập tức", pause=0.4)

# ---- HỒI 5 · CHIỀU HÔM SAU: KẾT MỞ LẶNG NGƯỜI (XIN BẰNG CHỨNG CỦA NHAU) ----
amb("street", -5.5); bgm("tension_drone", -4.5)
scene("s13_coffee_aftermath", "assets/c13.jpg", "calm", tr="fade_black", trd=0.55)
chapter("HỒI 5 · CHIỀU HÔM SAU", "THỨ MẤT ĐI KHÔNG CHỈ LÀ TIỀN")
sfx("chapter_sting", -0.1, -6)
beat(0.9)
mark("quiet_aftermath")
line("l31_khang", "KHANG", "Bên ngân hàng nói tiền đi qua nhiều lớp rồi, khó giữ kịp… Bốn lăm triệu đó để em góp lương trả dần.",
     "ngồi cúi mắt bên ly cà phê đá, giọng trầm buồn áy náy",
     sub="Bên ngân hàng nói tiền đi qua nhiều lớp rồi, khó giữ kịp… 45 triệu đó để em góp lương trả dần.")
line("l32_dat", "DAT", "Thôi, coi như hai anh em xui. Chuyện tiền nong cứ để từ từ tính.",
     "lắc đầu nhẹ, giọng điềm tĩnh không một lời trách móc", pause=0.6)
line("l33_dat", "DAT", "À… mấy đoạn tin nhắn với nick giả hôm qua, em chụp lại đủ hết rồi gửi cho anh giữ một bản nha.",
     "hạ giọng nhẹ tênh như tiện miệng nhắc, mắt nhìn thẳng Khang", pause=0.35)

# Cú lặng quyết định: Khang liếc sao kê "Ung luong" rồi đáp nhẹ ngang nhau
amb("room_tone", -5.0); bgm("tension_drone", SILENT)
scene("s14_silent_crack", "assets/c14.jpg", "push", tr="dissolve", trd=0.35)
mark("silent_crack")
bubble("SAO KÊ NGÂN HÀNG", "Anh Đạt → Khang: +45.000.000đ · ND: Ung luong",
       side="left", y=260, stamp="CHỨNG TỪ DUY NHẤT", dur=5.4, offset=0.2)
sfx("heartbeat", 0.3, -5, dur=1.8)
beat(1.1)
line("l34_khang", "KHANG", "Dạ. Vậy anh cũng chụp gửi em cái thông báo tài khoản anh bị đăng nhập lạ hôm kia… để em giữ.",
     "ngừng tay trên ly cà phê, ngước lên nhìn thẳng sếp, giọng nhẹ nhưng lạnh hẳn đi", pause=0.6)

# Cắt đen đột ngột! (Không đường dây ngầm)
sfx("impact", 0.0, -1.5)
scene("s15_black_cut", "assets/c15.jpg", "still", tr="fade_black", trd=0.08)
beat(2.0)

# ---- THẺ NHỚ KỸ (< 10 GIÂY) ----
amb("room_tone", -5.0); bgm("warm_outro", -4.2)
scene("s16_red_flags", EP01B + "scene18.jpg", "still", tr="fade_black", trd=0.4)
mark("rf_start")
sfx("bank_ting", 0.0, -5)
line("l35_narr", "N", "Mặt, giọng hay cách nói đều giả được. Cứ dính tiền mà dặn giữ bí mật, hãy gọi số thật hỏi thẳng.")
beat(0.8)
mark("rf_end")

# ---- DISCLAIMER ----
amb("room_tone", -6.0); bgm("warm_outro", -7.5)
scene("s17_disclaimer", EP01B + "scene18.jpg", "still", tr="fade_black", trd=0.35)
mark("disc_start")
beat(4.2)

# ================================================================ COMPILE
t = 0.0
scenes, dialogue, bubbles, foley, chapters = [], [], [], [], []
amb_runs, bgm_runs, marks = [], [], {}


def est(text: str) -> float:
    return len(text.split()) * SEC_PER_WORD + LINE_BASE


for kind, d in E:
    if kind == "scene":
        if scenes:
            scenes[-1]["end"] = round(t, 2)
        sc = {"id": d["id"], "image": d["image"], "start": round(t, 2), "end": None, "motion": d["motion"]}
        if d["tr"]:
            sc["transition_in"] = {"type": d["tr"], "dur": d["trd"]}
        if d["shake"] is not None:
            sc["shakes"] = [{"at": round(t + d["shake"], 2), "dur": 0.4, "amp": 16}]
        scenes.append(sc)
        t += SCENE_LEAD
    elif kind == "line":
        p = SPK[d["spk"]]
        dur = real.get(d["id"], est(d["text"]))
        ln = {"id": d["id"], "speaker": p["speaker"]}
        for k in ("voice", "label_short", "speaker_label", "af"):
            if k in p:
                ln[k] = p[k]
        if "base" in p:
            ln["style"] = p["base"] + (". Sắc thái câu này: " + d["emo"] if d["emo"] else "") + "."
        ln["start"] = round(t, 2)
        ln["window"] = round(max(dur, est(d["text"])) + WINDOW_MARGIN, 2)
        ln["text"] = d["text"]
        if d["sub"]:
            ln["subtitle"] = [d["sub"]]
        dialogue.append(ln)
        t += dur + GAP + d["pause"]
    elif kind == "beat":
        t += d
    elif kind == "chapter":
        s = scenes[-1]["start"] + d["offset"]
        chapters.append({"kicker": d["kicker"], "title": d["title"], "start": round(s, 2), "end": round(s + d["dur"], 2)})
    elif kind == "bubble":
        s = t + d["offset"]
        bubbles.append({
            "sender": d["sender"],
            "text": d["text"],
            "side": d["side"],
            "y": d["y"],
            "stamp": d["stamp"],
            "start": round(s, 2),
            "end": round(s + d["dur"], 2),
        })
    elif kind == "sfx":
        f = {"preset": d["preset"], "at": round(max(0.0, t + d["offset"]), 2), "gain_db": d["gain"]}
        if d["dur"]:
            f["dur"] = d["dur"]
        foley.append(f)
    elif kind == "amb":
        if amb_runs:
            amb_runs[-1]["end"] = round(t, 2)
        amb_runs.append({"preset": d["preset"], "start": round(t, 2), "end": None, "gain_db": d["gain"]})
    elif kind == "bgm":
        if bgm_runs:
            bgm_runs[-1]["end"] = round(t, 2)
        bgm_runs.append({"preset": d["preset"], "start": round(t, 2), "end": None, "gain_db": d["gain"]})
    elif kind == "mark":
        marks[d] = round(t, 2)

total = round(t, 2)
scenes[-1]["end"] = total
amb_runs[-1]["end"] = total
bgm_runs[-1]["end"] = total


def mmss(x: float) -> str:
    return f"{int(x // 60):02d}:{int(x % 60):02d}"


_desc = [(0.0, "Mở đầu – Cuộc gọi lần hai & câu hỏi đóng băng")]
_desc += [(c["start"] - 0.2, f"{c['kicker'].split('·')[0].strip().title()} – {c['title'].capitalize()}")
          for c in chapters if c["kicker"]]
_desc += [(marks["rf_start"], "Nhớ kỹ – 5 nguyên tắc chặn bẫy người đứng giữa")]
desc_chapters = "\n".join(f"{mmss(max(0.0, s))} {label}" for s, label in sorted(_desc))

episode = {
    "episode_id": "EP08",
    "slug": "MotVongTienHaiNuaSuThat",
    "title": "Một vòng tiền, hai nửa sự thật",
    "version": "v2-draft",
    "scam_family": "IMPERSONATION-MITM – Người đứng giữa đọc lén trò chuyện, nhái đúng văn phong + nhá video hình/giọng ghép 3 giây để điều phối hai người quen tự chuyển tiền đường vòng",
    "duration_sec": total,
    "visual_style_lock": (
        "Horizontal 16:9 widescreen (1920x1080), semi-realistic cinematic 2D anime illustration, "
        "contemporary Southern Vietnam urban setting, naturalistic dramatic lighting, clean bottom 15% for subtitles, "
        "no text, no letters, no numbers, no license plates, no logos, no real app interface, no real uniforms"
    ),
    "hook": {
        "kicker": "BẪY NGƯỜI ĐỨNG GIỮA · BỐN GIỜ CHIỀU",
        "title": "MỘT VÒNG TIỀN, HAI NỬA SỰ THẬT",
        "start": 0.4,
        "end": 5.0,
    },
    "chapters": chapters,
    "scenes": scenes,
    "dialogue": dialogue,
    "chat_bubbles": bubbles,
    "callouts": [],
    "red_flags": {
        "title": "NHỚ KỸ – BẪY NGƯỜI ĐỨNG GIỮA",
        "start": marks["rf_start"],
        "end": marks["rf_end"],
        "stagger_sec": 0.45,
        "items": [
            "HỎI THẲNG ĐÚNG VIỆC ĐƯỢC NHỜ: Gọi số thật vẫn dính bẫy nếu bạn diễn theo kịch bản giữ bí mật của kẻ gian",
            "CUỘC GỌI HÌNH MỜ 3 GIÂY RỒI CÚP ĐỔ MẠNG YẾU: Có thể là hình ghép và giọng cắt ghép từ tin nhắn cũ",
            "ĐÚNG GIỌNG ĐIỆU VẪN CHƯA CHẮC CHÍNH CHỦ: Kẻ đọc lén tài khoản có thể bắt chước cả cách xưng hô lẫn chuyện riêng",
            "KHÔNG CHUYỂN TIỀN ĐƯỜNG VÒNG QUA TÀI KHOẢN LẠ: Nhận tiền người quen rồi chuyển tiếp cho bên thứ ba là kẽ hở cực lớn",
            "ĐỪNG BỎ QUA CẢNH BÁO ĐĂNG NHẬP LẠ: Kiểm tra thiết bị ngay; nếu đã lỡ chuyển tiền, gọi tổng đài ngân hàng và trình báo công an",
        ],
        "action": "Trước mọi yêu cầu tiền bạc kèm lời dặn 'giữ bí mật, đừng nói với ai', hãy gọi trực tiếp số thật hoặc gặp mặt và hỏi thẳng đúng yêu cầu đó.",
    },
    "disclaimer": {
        "header": "LƯU Ý",
        "start": marks["disc_start"],
        "end": total,
        "lines": [
            "Tình huống trong phim được dựng lại nhằm mục đích cảnh báo cộng đồng; nhân vật, tên gọi và số liệu đều là hư cấu.",
            "Thông tin nghiệp vụ và pháp lý chỉ mang tính tham khảo — khi gặp sự cố, hãy liên hệ trực tiếp ngân hàng và cơ quan công an nơi gần nhất.",
        ],
    },
    "audio": {
        "ambience": amb_runs,
        "foley": foley,
        "bgm": bgm_runs,
        "duck_extra": [
            {"start": marks["hook_freeze"] - 0.2, "end": marks["hook_freeze"] + 3.0, "bgm_db": -12, "amb_db": -8},
            {"start": marks["two_phones"] - 0.2, "end": marks["two_phones"] + 10.0, "bgm_db": -11, "amb_db": -8},
            {"start": marks["money_loop"] - 0.2, "end": marks["money_loop"] + 4.0, "bgm_db": -10, "amb_db": -7},
            {"start": marks["confrontation"] - 0.2, "end": marks["confrontation"] + 14.0, "bgm_db": -11, "amb_db": -7},
            {"start": marks["quiet_aftermath"] - 0.2, "end": marks["silent_crack"] - 0.2, "bgm_db": -12, "amb_db": -7},
            {"start": marks["silent_crack"] - 0.2, "end": marks["rf_start"] - 0.2, "bgm_db": -18, "amb_db": -10},
            {"start": marks["disc_start"], "end": total - 0.05},
        ],
    },
    "forbidden_terms": [],
    "publish": {
        "titles": [
            "Thấy Đúng Mặt, Gọi Đúng Số Thật Vẫn Mất 45 Triệu – Bẫy Người Đứng Giữa | Bóc Trần Lừa Đảo",
            "Một Vòng Tiền, Hai Nửa Sự Thật: Khi Sếp Và Nhân Viên Cùng Tự Tay Chuyển Tiền Cho Kẻ Gian | Bóc Trần Lừa Đảo",
            "Nick Mới Nhái Y Chang Cách Nói Chuyện Của Sếp – Gọi Số Thật Sao Vẫn Sập Bẫy? | Bóc Trần Lừa Đảo",
        ],
        "description": (
            "Thấy đúng mặt sếp qua cuộc gọi hình 3 giây chập chờn, tin nhắn nhái y hệt cách xưng hô thường ngày, "
            "rồi chính nhân viên gọi thẳng vào số điện thoại thật của sếp — nhưng 45 triệu đồng vẫn đi trọn một vòng rồi biến mất vào tài khoản lạ.\n\n"
            "⏱️ Các hồi trong phim:\n" + desc_chapters
        ),
        "pinned_comment": (
            "📌 Theo bạn, sau câu nói ở cuối phim trên bàn cà phê, hai anh em có còn làm việc chung với nhau được nữa không? "
            "Chia sẻ góc nhìn ở bình luận để mọi người cùng cảnh giác nhé (lưu ý không đăng SĐT, STK hay tên người thật)."
        ),
        "hashtags": ["#bóctrầnlừađảo", "#cảnhgiáclừađảo", "#vạnchuyện", "#antoànmạng", "#ngườiđứnggiữa"],
        "tags": [
            "cảnh giác lừa đảo", "bóc trần lừa đảo", "vạn chuyện", "lừa đảo người đứng giữa",
            "cuộc gọi hình ghép", "giả mạo tài khoản người quen", "chuyển tiền đường vòng", "an toàn mạng",
        ],
        "category": "Education (Giáo dục)",
        "playlist": "Hồ Sơ Bóc Trần Lừa Đảo – Phim Dài Chuyên Sâu",
        "thumbnail_sec": round(marks["confrontation"] + 1.5, 2),
    },
}

OUT.write_text(json.dumps(episode, ensure_ascii=False, indent=2), encoding="utf-8")
words = sum(len(l["text"].split()) for l in dialogue)
narr_lines = [l for l in dialogue if l["speaker"] == "nguoi_boc_tran"]
narr = sum(len(l["text"].split()) for l in narr_lines)
rf_dur = round(marks["rf_end"] - marks["rf_start"], 2)
maxw = max(len(l["text"].split()) for l in dialogue)
print(
    f"episode.json: {total:.1f}s ({mmss(total)}) · {len(scenes)} cảnh · {len(dialogue)} câu · {words} từ "
    f"({words / (total / 60):.0f} từ/phút) · câu dài nhất {maxw} từ · "
    f"Bóc trần {len(narr_lines)} câu ({narr} từ, thẻ kết {rf_dur}s) · "
    f"{'TTS thật' if real else 'ước tính'} ({len(real)} câu thật)"
)
print(desc_chapters)
