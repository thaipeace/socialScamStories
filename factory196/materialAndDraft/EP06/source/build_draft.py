# -*- coding: utf-8 -*-
"""
Trình biên dịch `factory196/materialAndDraft/EP06/episode.json` – Tập EP06:
"Ba triệu tám trên màn hình" (16:9 Long-form · v2-draft).

Nguồn sự thật duy nhất của timeline: sửa thoại/nhịp ở phần STORY rồi chạy lại
    python factory196/materialAndDraft/EP06/source/build_draft.py
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
NOT_OLD = "tuyệt đối không giả giọng ông già hay bà già run rẩy, không kéo dài chữ, không cải lương"
SPK = {
    "NAM": dict(
        speaker="anh_hai",
        voice="Orus",
        label_short="NAM",
        speaker_label="Nam – kỹ thuật viên 32 tuổi, chăm làm, hiền lành, muốn kiếm việc phụ buổi tối",
        base=(
            "Giọng nam miền Nam Sài Gòn 32 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
            "giữ cố định một âm sắc trầm ấm, thật thà, rõ chữ, tự nhiên như đời thực"
        ),
    ),
    "NAM_P": dict(
        speaker="anh_hai",
        voice="Orus",
        af="phone",
        label_short="NAM",
        speaker_label="Giọng Nam phát qua loa điện thoại đặt trên bàn của người bạn cũ",
        base=(
            "Giọng nam miền Nam Sài Gòn 32 tuổi, phát âm chuẩn phương ngữ miền Nam, "
            "giữ cố định cùng âm sắc với Nam, rõ chữ"
        ),
    ),
    "THAO": dict(
        speaker="chi_hai",
        voice="Sulafat",
        label_short="THẢO",
        speaker_label="Thảo – vợ Nam 31 tuổi, thực tế, kiệm lời, tinh tế, không chì chiết chồng",
        base=(
            "Giọng phụ nữ miền Nam Sài Gòn 31 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
            "giữ cố định một âm sắc ấm, trầm vừa, nói cực gọn, điềm tĩnh, tự nhiên như đời thực, " + NOT_OLD
        ),
    ),
    "VY_P": dict(
        speaker="ke_ngot_ngao_nu",
        voice="Aoede",
        af="phone",
        label_short="ĐIỀU PHỐI",
        speaker_label="Vy Điều Phối – lời chào mở đầu khi Nam vừa vào ứng dụng Bạn Thân 4.0",
        base=(
            "Giọng nữ trẻ miền Nam Sài Gòn 28 tuổi, phát âm chuẩn phương ngữ miền Nam, "
            "nhẹ nhàng, ngọt ngào, lịch sự chuyên nghiệp như nhân viên chăm sóc khách hàng thật"
        ),
    ),
    "LOAN_P": dict(
        speaker="co_hanh",
        voice="Despina",
        af="phone",
        label_short="CHỊ LOAN",
        speaker_label="Chị Loan – thành viên kỳ cựu trong nhóm chat Bạn Thân 4.0, cảm ơn rối rít và nhiệt tình chỉ vẽ người mới",
        base=(
            "Giọng phụ nữ miền Nam Sài Gòn 42 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
            "thân tình, hồ hởi, nhanh nhẹn, nói tự nhiên như chị em cùng nhóm ngoài đời, " + NOT_OLD
        ),
    ),
    "TUAN_P": dict(
        speaker="thang_tun",
        voice="Puck",
        af="phone",
        label_short="TUẤN",
        speaker_label="Tuấn – thành viên trẻ trong nhóm chat Bạn Thân 4.0, báo thành quả và khuyến khích chốt đơn lớn",
        base=(
            "Giọng nam thanh niên miền Nam Sài Gòn 24 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
            "sáng, sôi nổi, nhiệt tình, nói gọn gàng phấn khởi như người vừa nhận thưởng thật"
        ),
    ),
    "HT_P": dict(
        speaker="chu_no",
        voice="Fenrir",
        af="phone",
        label_short="HỖ TRỢ",
        speaker_label="Bộ phận Hỗ trợ đối soát – trả lời lạnh lùng rập khuôn khi chặn rút tiền",
        base=(
            "Giọng nam miền Nam Sài Gòn 40 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
            "trầm, đều, lịch sự lạnh băng như máy trả lời, không gào thét nhưng gây áp lực tâm lý nặng"
        ),
    ),
    "IT": dict(
        speaker="ong_bay",
        voice="Algenib",
        label_short="BẠN CŨ",
        speaker_label="Người bạn cũ giấu mặt – không lộ diện mạo, không nêu tên, cực kiệm lời và dứt khoát",
        base=(
            "Giọng nam miền Nam Sài Gòn 35 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
            "trầm khàn nhẹ, cực kỳ điềm tĩnh, kiệm lời, dứt khoát có trọng lượng, " + NOT_OLD
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


def chapter(kicker: str, title: str, offset: float = 0.2, dur: float = 4.6):
    E.append(("chapter", dict(kicker=kicker, title=title, offset=offset, dur=dur)))


def bubble(sender: str, text: str, side: str = "left", y: int = 280, stamp: str | None = None,
           dur: float = 4.6, offset: float = 0.0):
    E.append(("bubble", dict(sender=sender, text=text, side=side, y=y, stamp=stamp, dur=dur, offset=offset)))


def callout(text: str, style: str = "danger", y: int = 520, dur: float = 2.4, offset: float = 0.0,
            size: str = "normal", kicker: str = ""):
    E.append(("callout", dict(text=text, style=style, y=y, dur=dur, offset=offset, size=size, kicker=kicker)))


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
# ---- HOOK · CON SỐ ĐỨNG YÊN & CÚ CHẶN RÚT TIỀN (00:00 – 00:30) ----
amb("night_room", -1.5); bgm("suspense_pulse", -2.5)
scene("s00_hook_blocked", "assets/c00.jpg", "push", shake=0.2)
sfx("notification", 0.15, -2)
bubble("VÍ BẠN THÂN 4.0", "Số dư: 3.850.000đ · Chưa đủ điều kiện đối soát để rút tiền",
       side="left", y=270, stamp="KHÓA RÚT TIỀN", dur=5.2, offset=0.2)
sfx("phone_ring", 1.1, -4, dur=1.4)
beat(2.2)
line("l01_nam", "NAM", "Alo, trong ví tôi đang có ba triệu tám, sao bấm rút về ngân hàng lại khóa?",
     "sốt ruột, hỏi thẳng",
     sub="Alo, trong ví tôi đang có 3 triệu 8, sao bấm rút về ngân hàng lại khóa?")
line("l02_ht", "HT_P", "Tài khoản anh còn treo một đơn đối soát cuối. Anh bù thêm hai triệu chín là hệ thống giải ngân toàn bộ.",
     "trầm đều, lạnh tanh như máy trả lời",
     sub="Tài khoản anh còn treo 1 đơn đối soát cuối. Anh bù thêm 2 triệu 9 là hệ thống giải ngân toàn bộ.")
line("l03_nam", "NAM", "Tiền tôi nằm sẵn trỏng gần bốn triệu rồi, sao không trừ thẳng mà bắt nạp thêm?!",
     "nhíu mày, bức xúc",
     sub="Tiền tôi nằm sẵn trỏng gần 4 triệu rồi, sao không trừ thẳng mà bắt nạp thêm?!")

scene("s01_hook_two_screens", "assets/c01.jpg", "tense", tr="flash_white", trd=0.25, shake=0.15)
mark("hook_freeze")
sfx("impact", 0.0, -3)
bubble("HỆ THỐNG BẠN THÂN 4.0", "Chỉ còn 01 bước cuối để nhận toàn bộ 6.750.000đ gốc và hoa hồng",
       side="left", y=260, stamp="ĐANG TREO ĐƠN", dur=5.4, offset=0.15)
beat(0.4)
line("l04_ht", "HT_P", "Quy trình tự động không trừ cấn anh nha. Quá hai mươi ba giờ chưa xong đơn là ví đóng băng.",
     "lạnh băng, buông gọn từng chữ",
     sub="Quy trình tự động không trừ cấn anh nha. Quá 23 giờ chưa xong đơn là ví đóng băng.")
sfx("call_end", 0.0, -3)
sfx("heartbeat", 0.2, -5, dur=2.2)
beat(2.4)

# ---- HỒI 1 · ỨNG DỤNG "BẠN THÂN 4.0" & NHÓM CHAT CẢM ƠN RỐI RÍT ----
amb("rain", -4.0); bgm("investigative_story", -3.5)
scene("s02_rainy_shift_cut", "assets/c02.jpg", "calm", tr="fade_black", trd=0.45)
chapter("HỒI 1 · BA TỐI TRƯỚC", "ỨNG DỤNG BẠN THÂN 4.0 & NHÓM CHAT RỐI RÍT CẢM ƠN")
sfx("chapter_sting", -0.1, -5)
beat(1.0)
line("l05_nam", "NAM", "Mưa dầm cả tuần nay kho cắt hết ca tối, tháng này chắc hụt tiền phụ em đóng học cho con rồi.",
     "lau áo mưa, thở dài nhẹ với vợ")
line("l06_thao", "THAO", "Tháng nào hụt mình gói ghém tháng đó, mưa gió anh chạy ráng ngoài đường nguy hiểm lắm.",
     "dịu dàng, thực tế, đưa khăn cho chồng", pause=0.4)

amb("night_room", -3.0); bgm("investigative_story", -3.2)
scene("s03_first_free_order", "assets/c03.jpg", "calm", tr="dissolve", trd=0.4)
sfx("notification", 0.2, -5)
# Giới thiệu ngắn lý do thuyết phục (mua hàng giùm người không có thời gian) + cài chi tiết "Từ năm 2018"
bubble("BẠN THÂN 4.0 · TỪ NĂM 2018", "Ứng dụng uy tín mua hàng giùm cho người không có thời gian · Cấp sẵn 40.000đ làm thử",
       side="left", y=190, stamp="MUA HỘ ĐÁNG TIN", dur=5.6, offset=0.2)
beat(1.0)
line("l07_vy", "VY_P", "Chào anh vô Bạn Thân bốn chấm không, app mua hàng giùm người bận. Ví cấp sẵn bốn chục ngàn, anh thử đơn đầu nha.",
     "ngọt ngào, lịch sự, chuyên nghiệp",
     sub="Chào anh vô Bạn Thân 4.0, app mua hàng giùm người bận. Ví cấp sẵn 40 ngàn, anh thử đơn đầu nha.")
sfx("typing", 0.1, -6, dur=0.9)
sfx("bank_ting", 1.1, -3)
bubble("VÍ BẠN THÂN 4.0", "Đơn mua hộ 30.000đ hoàn thành · Cộng gốc & hoa hồng -> Số dư: 45.000đ",
       side="left", y=410, stamp="HOÀN THÀNH", dur=4.4, offset=1.1)
beat(1.6)
line("l08_nam", "NAM", "Ủa… làm thử có một đơn mà nhảy lên bốn lăm ngàn liền nè em.",
     "ngạc nhiên, quay sang khoe vợ",
     sub="Ủa… làm thử có 1 đơn mà nhảy lên 45 ngàn liền nè em.")
line("l09_thao", "THAO", "Làm cái đó có bắt mình bỏ tiền túi ra hông anh?",
     "ngước nhìn chồng, hỏi gọn đúng trọng tâm")
line("l10_nam", "NAM", "Đâu có, app mua hàng giùm cho người không có thời gian, chạy từ năm hai ngàn mười tám, cho sẵn tiền thử mà.",
     "yên tâm, cười nhẹ giải thích cho vợ",
     sub="Đâu có, app mua hàng giùm cho người không có thời gian, chạy từ năm 2018, cho sẵn tiền thử mà.", pause=0.45)

# Group chat sôi động: mọi người báo thành quả liên tục, cảm ơn rối rít
scene("s03b_group_buzz", "assets/c03b.jpg", "calm", tr="dissolve", trd=0.35)
sfx("notification", 0.15, -4)
sfx("bank_ting", 1.25, -4.5)
bubble("CHỊ LOAN · NHÓM BẠN THÂN 4.0", "Em mới mua hộ xong 3 đơn chiều nay, hoa hồng cộng liền tay. Cảm ơn nhóm nhiều lắm luôn ạ!",
       side="left", y=170, stamp="CẢM ƠN RỐI RÍT", dur=7.2, offset=0.15)
bubble("HOA · NHÓM BẠN THÂN 4.0", "Cảm ơn admin với cả nhà! Em vừa chốt xong đơn thứ 5, mua hộ cho khách bận mà nhẹ nhàng quá!",
       side="left", y=430, stamp="BÁO THÀNH QUẢ", dur=6.0, offset=1.35)
beat(1.4)
line("l10b_loan", "LOAN_P", "Em mới xong ba đơn chiều nay, hoa hồng cộng vô ví liền. Cảm ơn nhóm mình nhiều lắm luôn ạ!",
     "hồ hởi, rối rít cảm ơn trong tin nhắn thoại nhóm",
     sub="Em mới xong 3 đơn chiều nay, hoa hồng cộng vô ví liền. Cảm ơn nhóm mình nhiều lắm luôn ạ!")
sfx("notification", 0.1, -4)
sfx("bank_ting", 1.3, -4.5)
bubble("TUẤN · NHÓM BẠN THÂN 4.0", "Trời mưa ở nhà mua hộ khách bận đỡ cực ghê. Cảm ơn cả nhà hướng dẫn em nha!",
       side="left", y=180, stamp="VỪA NHẬN THƯỞNG", dur=6.8, offset=0.15)
bubble("MINH · NHÓM BẠN THÂN 4.0", "Cảm ơn cả nhà nhiều lắm! Em vừa lên thêm 2 đơn nữa, tối nay ấm luôn rồi!",
       side="left", y=420, stamp="BÁO THÀNH QUẢ", dur=5.0, offset=1.5)
line("l10c_tuan", "TUAN_P", "Trời mưa ở nhà mua hộ khách bận mà đỡ cực ghê. Em vừa nhận hoa hồng xong, cảm ơn cả nhà nha!",
     "sôi nổi, phấn khởi báo thành quả trong nhóm", pause=0.5)
beat(0.4)

# ---- HỒI 2 · CẢ NHÓM CHỈ VẼ & CON SỐ NHẢY MÚA ----
amb("night_room", -2.5); bgm("investigative_story", -2.8)
scene("s04_ten_thousand_bait", "assets/c04.jpg", "hand", tr="fade_black", trd=0.4)
chapter("HỒI 2 · CẢ NHÓM CHỈ VẼ", "MƯỜI NGÀN BÙ THIẾU & CON SỐ NHẢY MÚA")
sfx("chapter_sting", -0.1, -5)
sfx("notification", 0.4, -4)
bubble("ĐƠN MUA HỘ #02", "Giá trị đơn: 55.000đ · Ví hiện có: 45.000đ · Thiếu: 10.000đ",
       side="left", y=250, stamp="THIẾU 10.000Đ", dur=5.4, offset=0.4)
beat(1.2)
line("l11_nam", "NAM", "Ủa cả nhà ơi, sao đơn mua hộ thứ hai này báo ví em thiếu mười ngàn vậy ta?",
     "hơi khựng lại, nhắn hỏi lên nhóm",
     sub="Ủa cả nhà ơi, sao đơn mua hộ thứ 2 này báo ví em thiếu 10 ngàn vậy ta?")
sfx("notification", 0.2, -4.5)
bubble("MINH · NHÓM BẠN THÂN 4.0", "Đúng rồi anh, mới vô em cũng hỏi y chang. Bù 10 ngàn xong ví nhảy lên 65 ngàn liền đó!",
       side="left", y=470, stamp="CÙNG NHÓM CHỈ VẼ", dur=5.6, offset=0.4)
line("l12_loan", "LOAN_P", "Bình thường đó anh mới ơi! Bù đúng mười ngàn phần thiếu thôi, xong đơn tiền hàng với hoa hồng cộng vô ví liền.",
     "nhiệt tình, thân tình chỉ vẽ người mới như chuyện quá quen",
     sub="Bình thường đó anh mới ơi! Bù đúng 10 ngàn phần thiếu thôi, xong đơn tiền hàng với hoa hồng cộng vô ví liền.")
sfx("typing", 0.1, -6, dur=1.1)
sfx("bank_ting", 1.3, -4)
bubble("VÍ BẠN THÂN 4.0", "Nạp bù +10.000đ -> Hoàn thành đơn -> Số dư mới: 65.000đ",
       side="left", y=470, stamp="+HOA HỒNG", dur=4.0, offset=1.3)
beat(1.8)
line("l13_nam", "NAM", "Ờ… sổ giao dịch ghi cộng trừ rõ ràng thiệt.",
     "gật đầu nhẹ, trút bỏ cảnh giác", pause=0.4)

# Montage hai tối kế tiếp: qua kênh group chat, các bạn cổ vũ khuyến khích chốt đơn lớn
scene("s05_escalating_topups", "assets/c05.jpg", "push", tr="dissolve", trd=0.4)
sfx("notification", 0.2, -4.5)
sfx("bank_ting", 1.0, -4)
bubble("NHÓM BẠN THÂN 4.0", "Chúc mừng anh Nam lên bậc khách quen! Được nhận đơn mua hộ lớn hoa hồng cao hơn nhiều!",
       side="left", y=210, stamp="NHÓM CỔ VŨ", dur=6.0, offset=0.2)
beat(1.4)
bubble("CHỊ LOAN · NHÓM BẠN THÂN 4.0", "Cố lên anh Nam ơi, làm nốt mấy đơn tối nay là gần 4 triệu rồi. Cảm ơn nhóm mình quá trời!",
       side="left", y=460, stamp="KHUYẾN KHÍCH", dur=5.6, offset=2.0)
line("l14_tuan", "TUAN_P", "Ví anh có sẵn triệu rưỡi rồi, bù thêm bốn trăm rưỡi thôi. Em mới chốt xong, hoa hồng ngon lắm anh!",
     "hào hứng cổ vũ, đẩy cảm giác bỏ ra rất ít mà lời ngon",
     sub="Ví anh có sẵn triệu rưỡi rồi, bù thêm 450 ngàn thôi. Em mới chốt xong, hoa hồng ngon lắm anh!")
sfx("typing", 0.1, -6, dur=1.2)
sfx("bank_ting", 1.4, -3)
beat(1.6)

# Khoe vợ số dư gần 4 triệu & câu hỏi chạm bản chất của Thảo
amb("room_tone", -2.5); bgm("investigative_story", -4.0)
scene("s06_wife_sharp_question", "assets/c06.jpg", "calm", tr="dissolve", trd=0.35)
mark("show_balance")
bubble("VÍ BẠN THÂN 4.0", "Số dư: 3.850.000đ · Mục Rút Tiền: TK …6821",
       side="left", y=240, stamp="GẦN 4 TRIỆU", dur=5.4, offset=0.2)
beat(0.8)
line("l15_nam", "NAM", "Em nhìn nè, ba tối nay anh gom hoa hồng lên được gần bốn triệu rồi đó!",
     "hào hứng đưa điện thoại cho vợ coi",
     sub="Em nhìn nè, 3 tối nay anh gom hoa hồng lên được gần 4 triệu rồi đó!")
line("l16_thao", "THAO", "Nhưng anh bấm rút thử tiền về ngân hàng mình lần nào chưa?",
     "nhìn kỹ màn hình rồi ngước hỏi chồng, điềm tĩnh mà sắc")
line("l17_nam", "NAM", "Mục rút tiền với số tài khoản anh nằm sẵn đây nè. Làm nốt đợt tối nay cho chẵn rồi anh rút một lượt luôn.",
     "chỉ tay vô màn hình, tự tin vì thấy giao diện đầy đủ", pause=0.6)
beat(1.0)

# ---- HỒI 3 · TIỀN THẬT ĐI RA & CON SỐ ĐỨNG YÊN ----
amb("night_room", -2.0); bgm("tension_drone", -2.0)
scene("s07_real_vs_screen", "assets/c07.jpg", "tense", tr="fade_black", trd=0.45)
chapter("HỒI 3 · HAI TIẾNG SAU", "TIỀN THẬT ĐI RA & CON SỐ ĐỨNG YÊN")
sfx("chapter_sting", -0.1, -5)
beat(1.2)
sfx("typing", 0.1, -6, dur=1.2)
bubble("NGÂN HÀNG CỦA NAM", "Đã chuyển đi: -10.000đ · -180.000đ · -450.000đ · -1.500.000đ (Tổng: -2.140.000đ)",
       side="left", y=250, stamp="TIỀN THẬT ĐÃ TRỪ", dur=6.2, offset=0.4)
beat(3.8)
sfx("notification", 0.2, -3.5)
bubble("CHỊ LOAN · NHÓM BẠN THÂN 4.0", "Ráng bù nốt 2 triệu 9 trước 23h đi anh Nam ơi! Bữa em cũng kẹt bước này, xong rút cả cục về liền!",
       side="left", y=470, stamp="XÚM VÔ HỐI NẠP", dur=5.8, offset=0.4)
beat(2.0)
line("l18_nam", "NAM", "Vừa bấm rút đã đòi bù thêm hai triệu chín… Mình chuyển đi hơn hai triệu rồi, mà cả nhóm vẫn chỉ hối nạp tiếp.",
     "giọng trầm xuống, tỉnh táo dần khi đối chiếu sao kê thật với tin nhắn hối nạp",
     sub="Vừa bấm rút đã đòi bù thêm 2 triệu 9… Mình chuyển đi hơn 2 triệu rồi, mà cả nhóm vẫn chỉ hối nạp tiếp.")
sfx("notification", 0.2, -3)
line("l19_ht", "HT_P", "Còn hai mươi phút nữa tới hai mươi ba giờ anh Nam nha. Xong đơn này hệ thống giải ngân liền sáu triệu bảy.",
     "trầm đều, lạnh tanh, lấy mốc giờ để thúc ép nạp tiền",
     sub="Còn 20 phút nữa tới 23 giờ anh Nam nha. Xong đơn này hệ thống giải ngân liền 6 triệu 7.", pause=0.6)
sfx("heartbeat", 0.0, -4, dur=2.0)
beat(2.2)   # nhịp câm quyết định: Nam nhìn ngón tay mình rồi dứt khoát tắt app ngân hàng, không bấm chuyển

# ---- HỒI 4 · NGƯỜI BẠN CŨ GIẤU MẶT & TÊN MIỀN SÁU NGÀY TUỔI ----
amb("street", -4.5); bgm("tension_drone", -3.5)
scene("s08_porch_call_friend", "assets/c08.jpg", "calm", tr="fade_black", trd=0.4)
chapter("HỒI 4 · NGƯỜI BẠN GIẤU MẶT", "TÊN MIỀN SÁU NGÀY TUỔI")
sfx("chapter_sting", -0.1, -5)
sfx("phone_ring", 0.4, -4, dur=1.3)
beat(1.8)
line("l20_nam", "NAM", "Ê, còn thức hông mày? Tao mới gửi đường dẫn trang Bạn Thân bốn chấm không, coi giùm tao cái.",
     "ngồi ngoài hiên vắng, hạ giọng gọi bạn cũ",
     sub="Ê, còn thức hông mày? Tao mới gửi đường dẫn trang Bạn Thân 4.0, coi giùm tao cái.")

# Căn phòng tối của người bạn cũ: CỐ Ý KHÔNG LỘ MẶT, CỰC KIỆM LỜI, NÓI NHƯ ĐÃ BIẾT CHUYỆN
amb("night_room", -3.5); bgm("tension_drone", SILENT)
scene("s09_faceless_it_lookup", "assets/c09.jpg", "push", tr="dissolve", trd=0.4)
mark("it_truth")
sfx("typing", 0.2, -4, dur=1.2)
bubble("TRA CỨU ĐĂNG KÝ TÊN MIỀN", "Tự nhận trên trang: Từ năm 2018  |  Ngày đăng ký thật: Thứ Ba tuần trước",
       side="left", y=250, stamp="MỚI MỞ 6 NGÀY", dur=6.0, offset=1.3)
beat(2.4)
line("l21_it", "IT", "Tên miền mới mở thứ Ba tuần trước. Biết ngay mà.",
     "nhìn màn hình tra cứu, điềm tĩnh như đã biết chuyện từ trước, nói cực gọn", pause=0.35)
line("l22_nam", "NAM_P", "Nhưng ví tao vẫn hiện nguyên ba triệu tám mà mày…",
     "ngỡ ngàng, vẫn còn tiếc con số trên màn hình",
     sub="Nhưng ví tao vẫn hiện nguyên 3 triệu 8 mà mày…")
line("l23_it", "IT", "Số đó tụi nó tự gõ. Bỏ ngay đi, chuyển nữa là mất nữa.",
     "trầm khàn, dứt khoát có trọng lượng thuyết phục ngay lập tức, không giải thích dài dòng", pause=0.45)
sfx("call_end", 0.0, -3)
beat(1.5)

# ---- HỒI 5 · TẮT MÀN HÌNH & GIỮ LẠI TIỀN THẬT ----
amb("room_tone", -3.5); bgm("warm_outro", -3.5)
scene("s10_turn_off_screen", "assets/c10.jpg", "calm", tr="fade_black", trd=0.5)
chapter("HỒI 5 · DỪNG ĐÚNG LÚC", "TẮT MÀN HÌNH ĐỂ GIỮ LẠI TIỀN THẬT")
sfx("chapter_sting", -0.1, -5)
beat(1.0)
mark("wife_warmth")
line("l25_nam", "NAM", "Anh mất hai triệu mốt tiền thiệt rồi Thảo ơi… Tưởng bù mỗi lần vài trăm lẻ, cộng lại đứt mấy ngày công.",
     "thật thà nhận lỗi với vợ, giọng trầm buồn",
     sub="Anh mất 2 triệu mốt tiền thiệt rồi Thảo ơi… Tưởng bù mỗi lần vài trăm lẻ, cộng lại đứt mấy ngày công.")
line("l26_thao", "THAO", "Dừng ngay khúc này là may lắm rồi anh. Chứ nãy tiếc của mà nạp thêm ba triệu nữa là lún sâu luôn đó.",
     "đặt ly nước ấm xuống bàn, giọng ấm áp tỉnh táo, không một lời trách móc",
     sub="Dừng ngay khúc này là may lắm rồi anh. Chứ nãy tiếc của mà nạp thêm 3 triệu nữa là lún sâu luôn đó.")
line("l27_nam", "NAM", "Ừ… Mai anh đem sao kê trình báo công an, rồi dặn anh em dưới kho né cái trò bù tiền này ra.",
     "bình tĩnh lại, bấm tắt màn hình đặt úp điện thoại xuống bàn", pause=0.8)
beat(2.2)

# ---- THẺ NHỚ KỸ (DƯỚI 10 GIÂY) ----
amb("room_tone", -5.0); bgm("warm_outro", -4.0)
scene("s11_red_flags", EP01B + "scene18.jpg", "still", tr="fade_black", trd=0.4)
mark("rf_start")
sfx("bank_ting", 0.0, -5)
line("l28_narr", "N", "Số dư trên trang lạ là chữ họ tự gõ, còn tiền rời ngân hàng bạn mới mất thật.")
beat(1.0)
mark("rf_end")

# ---- KẾT MỞ ĐƯỜNG DÂY NGẦM · MÀN HÌNH DANH SÁCH & NÚT "CHỐT KHÁCH" ----
amb("night_room", -3.5); bgm("tension_drone", -1.2)
scene("s12_unseen_tracker_coda", "assets/c11.jpg", "push", tr="fade_black", trd=0.45)
sfx("typing", 0.25, -5.5, dur=0.55)
bubble("DANH SÁCH KHÁCH", "#408 · Đang theo đơn  |  #409 · Chờ đối soát  |  #410 · Nam",
       side="left", y=210, stamp="MÀN HÌNH VI TÍNH", dur=7.1, offset=0.2)
beat(1.4)
mark("it_coda")
line("l29_it_coda", "IT", "Haiz… đúng là trái đất tròn.",
     "bắt đầu bằng tiếng thở dài khẽ tự nhiên như tiếng thở hắt ra, tuyệt đối không đánh vần chữ z, rồi buông gọn trầm khàn lạnh sắc",
     sub="Haiz… đúng là trái đất tròn.", pause=0.35)
sfx("heartbeat", 0.0, -4, dur=1.8)
callout("[  CHỐT KHÁCH  ]", style="danger", y=520, dur=2.1, offset=0.0, size="large", kicker="CON TRỎ CHUỘT RÊ VÀO")
beat(2.15)

sfx("impact", 0.0, -1)
scene("s13_black_cut", "assets/c12.jpg", "still", tr="fade_black", trd=0.08)
beat(2.0)

# ---- DISCLAIMER ----
amb("room_tone", -6.0); bgm("tension_drone", -8.0)
scene("s14_disclaimer", EP01B + "scene18.jpg", "still", tr="fade_black", trd=0.35)
mark("disc_start")
beat(4.2)

# ================================================================ COMPILE
t = 0.0
scenes, dialogue, bubbles, callouts, foley, chapters = [], [], [], [], [], []
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
    elif kind == "callout":
        s = t + d["offset"]
        co = {
            "text": d["text"],
            "style": d["style"],
            "y": d["y"],
            "size": d["size"],
            "start": round(s, 2),
            "end": round(s + d["dur"], 2),
        }
        if d["kicker"]:
            co["kicker"] = d["kicker"]
        callouts.append(co)
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


_desc = [(0.0, "Mở đầu – Ba triệu tám trên màn hình & cú khóa rút tiền")]
_desc += [(c["start"] - 0.2,
           f"{c['kicker'].split('·')[0].strip().title()} – {c['title'].capitalize().replace('bạn thân 4.0', 'Bạn Thân 4.0')}")
          for c in chapters if c["kicker"]]
_desc += [(marks["rf_start"], "Nhớ kỹ – 5 nguyên tắc nhận diện bẫy mua hàng hộ")]
_desc += [(marks["it_coda"] - 1.5, "Kết mở – Màn hình danh sách & nút Chốt khách")]
desc_chapters = "\n".join(f"{mmss(max(0.0, s))} {label}" for s, label in sorted(_desc))

episode = {
    "episode_id": "EP06",
    "slug": "BaTrieuTamTrenManHinh",
    "title": "Ba triệu tám trên màn hình",
    "version": "v2-draft",
    "scam_family": "JOB-TASK – Ứng dụng mua hàng hộ Bạn Thân 4.0: nhóm chat chim mồi cảm ơn rối rít, bù phần thiếu & ảo giác số dư",
    "duration_sec": total,
    "visual_style_lock": (
        "Horizontal 16:9 widescreen (1920x1080), semi-realistic cinematic 2D anime illustration, "
        "contemporary Southern Vietnam urban setting, naturalistic dramatic lighting, clean bottom 15% for subtitles, "
        "no text, no letters, no numbers, no license plates, no logos, no real app interface, no real uniforms"
    ),
    "hook": {
        "kicker": "BẪY CỘNG TÁC VIÊN MUA HÀNG HỘ · ĐÊM THỨ BA",
        "title": "BA TRIỆU TÁM TRÊN MÀN HÌNH",
        "start": 0.4,
        "end": 5.0,
    },
    "chapters": chapters,
    "scenes": scenes,
    "dialogue": dialogue,
    "chat_bubbles": bubbles,
    "callouts": callouts,
    "red_flags": {
        "title": "NHỚ KỸ – BẪY CỘNG TÁC VIÊN MUA HÀNG HỘ",
        "start": marks["rf_start"],
        "end": marks["rf_end"],
        "stagger_sec": 0.45,
        "items": [
            "VIỆC LÀM THẬT KHÔNG BẮT NẠP TIỀN: Mọi lý do mua hàng hộ đòi bù phần thiếu hay phí đối soát đều là bẫy",
            "NHÓM CHAT CẢM ƠN RỐI RÍT ĐA PHẦN LÀ CHIM MỒI: Tài khoản ảo chia vai báo thành quả và chỉ vẽ để tạo niềm tin giả",
            "ĐỪNG TIN SỐ DƯ TRÊN TRANG LẠ: Kẻ gian tự tạo đơn, tự cộng hoa hồng ảo và khóa nút rút bất cứ lúc nào",
            "DỪNG NGAY KHI BỊ ĐÒI BÙ ĐƠN LỚN: Cắt lỗ lập tức, tuyệt đối không nạp thêm tiền thật để cứu con số ảo",
            "KHÔNG THUÊ DỊCH VỤ LẤY LẠI TIỀN TREO: Lưu sao kê và đường dẫn để trình báo cơ quan công an, tránh bị lừa lần hai",
        ],
        "action": "Trước mọi lời mời mua hàng hộ chốt đơn, hãy tự hỏi: tiền đang nằm trong ngân hàng của mình hay chỉ là con số gõ trên màn hình của người lạ?",
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
            {"start": marks["hook_freeze"] - 0.2, "end": marks["hook_freeze"] + 3.5, "bgm_db": -12, "amb_db": -8},
            {"start": marks["it_truth"] - 0.2, "end": marks["it_truth"] + 7.5, "bgm_db": -16, "amb_db": -10},
            {"start": marks["wife_warmth"] - 0.2, "end": marks["wife_warmth"] + 4.5, "bgm_db": -12, "amb_db": -6},
            {"start": marks["it_coda"] - 0.2, "end": marks["disc_start"] - 0.2, "bgm_db": -10, "amb_db": -7},
            {"start": marks["disc_start"], "end": total - 0.05},
        ],
    },
    "forbidden_terms": [],
    "publish": {
        "titles": [
            "App Mua Hàng Hộ 'Bạn Thân 4.0' & Nhóm Chat Cảm Ơn Rối Rít: Cú Khóa Rút 3 Triệu 8 | Bóc Trần Lừa Đảo",
            "Bù 10 Ngàn Phần Thiếu Khi Mua Hàng Hộ Tại Nhà: Tiền Thật Đi Ra & Con Số Đứng Yên | Bóc Trần Lừa Đảo",
            "Trang Mua Hàng Hộ Ghi Từ Năm 2018, Tra Ra Mới Mở Tuần Trước | Bóc Trần Lừa Đảo",
        ],
        "description": (
            "Ứng dụng 'Bạn Thân 4.0' giới thiệu mua hàng giùm cho người bận không có thời gian, cấp sẵn 40.000đ làm thử cùng nhóm chat báo thành quả cảm ơn rối rít — "
            "cho đến khi số dư trên màn hình nhảy lên 3.850.000đ nhưng nút rút tiền bất ngờ khóa chặt.\n\n"
            "⏱️ Các hồi trong phim:\n" + desc_chapters
        ),
        "pinned_comment": (
            "📌 Bạn hay người thân từng được mời vào nhóm chat mua hàng hộ 'cấp sẵn tiền làm thử' rồi mọi người báo thành quả cảm ơn rối rít chưa? "
            "Chia sẻ ở bình luận để mọi người cùng cảnh giác nhé (lưu ý không đăng SĐT, STK, tên miền thật hay tên người thật)."
        ),
        "hashtags": ["#bóctrầnlừađảo", "#cảnhgiáclừađảo", "#vạnchuyện", "#antoànmạng", "#cộngtácviênảo"],
        "tags": [
            "cảnh giác lừa đảo", "bóc trần lừa đảo", "vạn chuyện", "cộng tác viên mua hàng hộ",
            "bẫy bù tiền đơn hàng", "nhóm chat chim mồi", "số dư ảo trên màn hình", "an toàn mạng",
        ],
        "category": "Education (Giáo dục)",
        "playlist": "Hồ Sơ Bóc Trần Lừa Đảo – Phim Dài Chuyên Sâu",
        "thumbnail_sec": round(marks["it_truth"] + 1.5, 2),
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
