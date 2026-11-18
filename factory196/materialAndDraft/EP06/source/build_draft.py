# -*- coding: utf-8 -*-
"""
Trình biên dịch `factory196/materialAndDraft/EP06/episode.json` – Tập EP06:
"Ba triệu tám trên màn hình" (16:9 Long-form · v1-draft).

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
# 7 nhân vật = 7 voice hoàn toàn tách biệt trong 02_CAST/cast.json
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
        speaker_label="Giọng Nam phát qua loa điện thoại đặt trên bàn của người bạn IT",
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
        speaker_label="Vy Điều Phối – người hướng dẫn đơn hàng đầu tiên qua tin nhắn thoại",
        base=(
            "Giọng nữ trẻ miền Nam Sài Gòn 28 tuổi, phát âm chuẩn phương ngữ miền Nam, "
            "nhẹ nhàng, ngọt ngào, lịch sự chuyên nghiệp như nhân viên chăm sóc khách hàng thật"
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
        speaker_label="Người bạn IT giấu mặt – không lộ diện mạo, không nêu tên, điềm tĩnh tra hạ tầng",
        base=(
            "Giọng nam miền Nam Sài Gòn 35 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
            "trầm khàn nhẹ, cực kỳ điềm tĩnh, kiệm lời, dứt khoát, nói câu nào sắc câu đó, " + NOT_OLD
        ),
    ),
    "SEC_P": dict(
        speaker="chi_tu",
        voice="Zephyr",
        af="phone",
        label_short="ĐẦU DÂY LẠ",
        speaker_label="Giọng nữ bí ẩn gọi vào máy phụ của người bạn IT ở cảnh kết mở",
        base=(
            "Giọng nữ miền Nam Sài Gòn 35 tuổi, phát âm chuẩn phương ngữ miền Nam, "
            "trầm tĩnh, gọn, chuyên nghiệp, nói khẽ vừa đủ nghe qua điện thoại"
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
bubble("VÍ ĐỐI TÁC ĐƠN HÀNG", "Số dư: 3.850.000đ · Chưa đủ điều kiện đối soát để rút tiền",
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
bubble("HỆ THỐNG ĐỐI SOÁT", "Chỉ còn 01 bước cuối để nhận toàn bộ 6.750.000đ gốc và hoa hồng",
       side="left", y=260, stamp="ĐANG TREO ĐƠN", dur=5.4, offset=0.15)
beat(0.4)
line("l04_ht", "HT_P", "Quy trình tự động không trừ cấn anh nha. Quá hai mươi ba giờ chưa xong đơn là ví đóng băng.",
     "lạnh băng, buông gọn từng chữ",
     sub="Quy trình tự động không trừ cấn anh nha. Quá 23 giờ chưa xong đơn là ví đóng băng.")
sfx("call_end", 0.0, -3)
sfx("heartbeat", 0.2, -5, dur=2.2)
beat(2.4)

# ---- HỒI 1 · BỐN CHỤC NGÀN CẤP SẴN & DÒNG CHỮ "TỪ NĂM 2018" ----
amb("rain", -4.0); bgm("investigative_story", -3.5)
scene("s02_rainy_shift_cut", "assets/c02.jpg", "calm", tr="fade_black", trd=0.45)
chapter("HỒI 1 · BA TỐI TRƯỚC", "BỐN CHỤC NGÀN CẤP SẴN & MỒI NHỬ KHÔNG TỐN VỐN")
sfx("chapter_sting", -0.1, -5)
beat(1.0)
line("l05_nam", "NAM", "Mưa dầm cả tuần nay kho cắt hết ca tối, tháng này chắc hụt tiền phụ em đóng học cho con rồi.",
     "lau áo mưa, thở dài nhẹ với vợ")
line("l06_thao", "THAO", "Tháng nào hụt mình gói ghém tháng đó, mưa gió anh chạy ráng ngoài đường nguy hiểm lắm.",
     "dịu dàng, thực tế, đưa khăn cho chồng", pause=0.4)

amb("night_room", -3.0); bgm("investigative_story", -3.2)
scene("s03_first_free_order", "assets/c03.jpg", "calm", tr="dissolve", trd=0.4)
sfx("notification", 0.2, -5)
# Cài rõ chi tiết "Vận hành từ năm 2018" + "40.000đ cấp sẵn" để trả ở cảnh tra tên miền Hồi 4
bubble("SÀN ĐỐI TÁC ĐƠN HÀNG", "Giới thiệu: Vận hành từ năm 2018 · Cấp sẵn 40.000đ vốn làm thử",
       side="left", y=260, stamp="TUYỂN CTV", dur=5.4, offset=0.2)
beat(1.0)
line("l07_vy", "VY_P", "Chào anh Nam, bên em tặng sẵn bốn chục ngàn trong ví rồi đó. Anh bấm xác nhận đơn ba chục ngàn đầu tiên nha.",
     "ngọt ngào, thân thiện, hướng dẫn nhẹ nhàng",
     sub="Chào anh Nam, bên em tặng sẵn 40 ngàn trong ví rồi đó. Anh bấm xác nhận đơn 30 ngàn đầu tiên nha.")
sfx("typing", 0.1, -6, dur=0.9)
sfx("bank_ting", 1.1, -3)
bubble("VÍ ĐỐI TÁC ĐƠN HÀNG", "Đơn 30.000đ hoàn thành · Cộng gốc & hoa hồng -> Số dư: 45.000đ",
       side="left", y=440, stamp="HOÀN THÀNH", dur=4.2, offset=1.1)
beat(1.6)
line("l08_nam", "NAM", "Ủa… làm thử có một đơn mà nhảy lên bốn lăm ngàn liền nè em.",
     "ngạc nhiên, quay sang khoe vợ",
     sub="Ủa… làm thử có 1 đơn mà nhảy lên 45 ngàn liền nè em.")
line("l09_thao", "THAO", "Làm cái đó có bắt mình bỏ tiền túi ra hông anh?",
     "ngước nhìn chồng, hỏi gọn đúng trọng tâm")
line("l10_nam", "NAM", "Đâu có, trang này ghi chạy từ năm hai ngàn mười tám, lại cho sẵn tiền trong ví làm thử mà.",
     "yên tâm, cười nhẹ trấn an vợ",
     sub="Đâu có, trang này ghi chạy từ năm 2018, lại cho sẵn tiền trong ví làm thử mà.", pause=0.5)

# ---- HỒI 2 · MƯỜI NGÀN "BÙ PHẦN THIẾU" & CON SỐ NHẢY MÚA ----
amb("night_room", -2.5); bgm("investigative_story", -2.8)
scene("s04_ten_thousand_bait", "assets/c04.jpg", "hand", tr="fade_black", trd=0.4)
chapter("HỒI 2 · MỒI NHỬ TỪNG BƯỚC", "MƯỜI NGÀN BÙ THIẾU & CON SỐ NHẢY MÚA")
sfx("chapter_sting", -0.1, -5)
sfx("notification", 0.4, -4)
bubble("ĐƠN HÀNG THỨ 02", "Giá trị đơn: 55.000đ · Ví hiện có: 45.000đ · Thiếu: 10.000đ",
       side="left", y=260, stamp="THIẾU 10.000Đ", dur=5.2, offset=0.4)
beat(1.2)
line("l11_nam", "NAM", "Ủa, sao đơn này báo thiếu mười ngàn vậy ta?",
     "hơi khựng lại nhìn màn hình",
     sub="Ủa, sao đơn này báo thiếu 10 ngàn vậy ta?")
line("l12_vy", "VY_P", "Dạ anh bù đúng mười ngàn phần thiếu thôi. Xong đơn là tiền hàng với hoa hồng cộng dồn hết lại vô ví anh liền.",
     "lịch sự, giải thích trơn tru như chuyện bình thường",
     sub="Dạ anh bù đúng 10 ngàn phần thiếu thôi. Xong đơn là tiền hàng với hoa hồng cộng dồn hết lại vô ví anh liền.")
sfx("typing", 0.1, -6, dur=1.1)
sfx("bank_ting", 1.3, -4)
bubble("LỊCH SỬ GIAO DỊCH VÍ", "Nạp bù +10.000đ -> Hoàn thành đơn -> Số dư mới: 65.000đ",
       side="left", y=440, stamp="+HOA HỒNG", dur=4.0, offset=1.3)
beat(1.8)
line("l13_nam", "NAM", "Ờ… sổ giao dịch ghi cộng trừ rõ ràng thiệt.",
     "gật đầu nhẹ, trút bỏ cảnh giác", pause=0.4)

# Montage hai tối kế tiếp: mỗi lần chỉ "bù phần thiếu" nên không nhận ra mình đã chuyển nhiều
scene("s05_escalating_topups", "assets/c05.jpg", "push", tr="dissolve", trd=0.4)
sfx("bank_ting", 0.3, -5)
sfx("bank_ting", 1.1, -4)
beat(1.4)
line("l14_vy", "VY_P", "Anh lên bậc quen rồi nên được ưu tiên đơn lớn. Ví có sẵn triệu rưỡi, anh bù thêm bốn trăm rưỡi thôi nha.",
     "ngọt ngào khích lệ, bình thường hóa khoản nạp lớn dần",
     sub="Anh lên bậc quen rồi nên được ưu tiên đơn lớn. Ví có sẵn triệu rưỡi, anh bù thêm 450 ngàn thôi nha.")
sfx("typing", 0.1, -6, dur=1.2)
sfx("bank_ting", 1.4, -3)
beat(1.6)

# Khoe vợ số dư gần 4 triệu & câu hỏi chạm bản chất của Thảo
amb("room_tone", -2.5); bgm("investigative_story", -4.0)
scene("s06_wife_sharp_question", "assets/c06.jpg", "calm", tr="dissolve", trd=0.35)
mark("show_balance")
bubble("VÍ ĐỐI TÁC ĐƠN HÀNG", "Số dư khả dụng: 3.850.000đ · Mục Rút Tiền: Đã liên kết TK …6821",
       side="left", y=260, stamp="GẦN 4 TRIỆU", dur=5.4, offset=0.2)
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
chapter("HỒI 3 · ĐỐI CHIẾU NỬA ĐÊM", "TIỀN THẬT ĐI RA & CON SỐ ĐỨNG YÊN")
sfx("chapter_sting", -0.1, -5)
beat(1.2)
sfx("typing", 0.1, -6, dur=1.2)
bubble("NGÂN HÀNG CỦA NAM", "Đã chuyển đi: -10.000đ · -180.000đ · -450.000đ · -1.500.000đ (Tổng: -2.140.000đ)",
       side="left", y=250, stamp="TIỀN THẬT ĐÃ TRỪ", dur=5.8, offset=0.4)
beat(3.8)
sfx("phone_ring", 0.1, -4, dur=1.6)
sfx("call_end", 1.8, -3)
beat(2.2)
line("l18_nam", "NAM", "Lúc biểu bù mười ngàn thì bắt máy lẹ lắm… Tới lúc hỏi rút tiền thì khóa máy luôn.",
     "giọng trầm xuống, chua chát khi gọi điều phối không ai nghe",
     sub="Lúc biểu bù 10 ngàn thì bắt máy lẹ lắm… Tới lúc hỏi rút tiền thì khóa máy luôn.")
sfx("notification", 0.2, -3)
line("l19_ht", "HT_P", "Anh bỏ ngang lúc này là mất trắng ba triệu tám đang nằm sẵn trong ví đó nha.",
     "thúc ép đúng tâm lý tiếc của để dụ nạp thêm",
     sub="Anh bỏ ngang lúc này là mất trắng 3 triệu 8 đang nằm sẵn trong ví đó nha.", pause=0.6)
sfx("heartbeat", 0.0, -4, dur=2.0)
beat(2.2)   # nhịp câm quyết định: Nam nhìn ngón tay mình rồi dứt khoát tắt app ngân hàng, không bấm chuyển

# ---- HỒI 4 · NGƯỜI BẠN IT GIẤU MẶT & TÊN MIỀN SÁU NGÀY TUỔI ----
amb("street", -4.5); bgm("tension_drone", -3.5)
scene("s08_porch_call_friend", "assets/c08.jpg", "calm", tr="fade_black", trd=0.4)
chapter("HỒI 4 · NGƯỜI BẠN GIẤU MẶT", "TÊN MIỀN SÁU NGÀY TUỔI")
sfx("chapter_sting", -0.1, -5)
sfx("phone_ring", 0.4, -4, dur=1.3)
beat(1.8)
line("l20_nam", "NAM", "Ê, giờ này còn thức hông mày? Tao mới gửi cái đường dẫn qua tin nhắn, coi giùm tao trang này cái.",
     "ngồi ngoài hiên vắng, hạ giọng gọi bạn cũ")

# Căn phòng tối của người bạn IT: CỐ Ý KHÔNG LỘ MẶT, KHÔNG NÊU TÊN
amb("night_room", -3.5); bgm("tension_drone", SILENT)
scene("s09_faceless_it_lookup", "assets/c09.jpg", "push", tr="dissolve", trd=0.4)
mark("it_truth")
sfx("typing", 0.2, -4, dur=1.8)
bubble("TRA CỨU ĐĂNG KÝ TÊN MIỀN", "Tự nhận trên trang: Từ năm 2018  |  Ngày đăng ký thật: Thứ Ba tuần trước",
       side="left", y=250, stamp="MỚI MỞ 6 NGÀY", dur=6.0, offset=1.8)
beat(3.0)
line("l21_it", "IT", "Tên miền này mới đăng ký hồi thứ Ba tuần trước. Mà trên trang lại tự nhận hoạt động từ năm hai ngàn mười tám?",
     "nhìn màn hình tra cứu, giọng trầm khàn điềm tĩnh",
     sub="Tên miền này mới đăng ký hồi thứ Ba tuần trước. Mà trên trang lại tự nhận hoạt động từ năm 2018?", pause=0.4)
line("l22_nam", "NAM_P", "Nhưng trong ví tao nó vẫn hiện nguyên ba triệu tám với lịch sử đơn đầy đủ mà mày…",
     "ngỡ ngàng, vẫn còn tiếc con số trên màn hình",
     sub="Nhưng trong ví tao nó vẫn hiện nguyên 3 triệu 8 với lịch sử đơn đầy đủ mà mày…")
line("l23_it", "IT", "Tiền trong ngân hàng mới có nơi giữ cho mày. Còn con số trên trang lạ… tụi nó gõ bao nhiêu chẳng được.",
     "chậm, rõ, bóc trần thẳng bản chất mà không giáo điều", pause=0.4)
line("l24_it", "IT", "Thôi, mày quên con số đó đi. Đừng nạp thêm, cũng đừng tin đứa nào nhận kéo tiền treo về.",
     "dứt khoát, dặn bạn cắt lỗ ngay", pause=0.5)
sfx("call_end", 0.0, -3)
beat(1.4)

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

# ---- KẾT MỞ: BÀN TAY NGƯỜI BẠN IT GIẤU MẶT & CỤM MÁY CHỦ NGẦM ----
amb("night_room", -3.5); bgm("tension_drone", -1.2)
scene("s12_unseen_tracker_coda", "assets/c11.jpg", "push", tr="fade_black", trd=0.45)
sfx("typing", 0.1, -5, dur=1.0)
sfx("phone_vibrate", 1.1, -3, dur=1.1)
beat(2.2)
mark("it_coda")
line("l29_sec", "SEC_P", "Đường dẫn cậu bạn anh vừa gửi… lại trỏ về cụm máy chủ mới mở tuần trước hả anh?",
     "trầm tĩnh hỏi khẽ qua điện thoại", pause=0.4)
sfx("heartbeat", 0.0, -4, dur=2.0)
line("l30_it_coda", "IT", "Ừ. Lại chung một đầu mối đứng sau mấy nhánh đợt trước.",
     "trầm khàn, lạnh sắc, nhìn thẳng vào ánh sáng màn hình", pause=0.25)

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


_desc = [(0.0, "Mở đầu – Ba triệu tám trên màn hình & cú khóa rút tiền")]
_desc += [(c["start"] - 0.2, f"{c['kicker'].split('·')[0].strip().title()} – {c['title'].capitalize()}")
          for c in chapters if c["kicker"]]
_desc += [(marks["rf_start"], "Nhớ kỹ – 5 nguyên tắc nhận diện bẫy cộng tác viên đơn hàng")]
_desc += [(marks["it_coda"] - 2.0, "Kết mở – Căn phòng tối của người bạn giấu mặt")]
desc_chapters = "\n".join(f"{mmss(max(0.0, s))} {label}" for s, label in sorted(_desc))

episode = {
    "episode_id": "EP06",
    "slug": "BaTrieuTamTrenManHinh",
    "title": "Ba triệu tám trên màn hình",
    "version": "v1-draft",
    "scam_family": "JOB-TASK – Cộng tác viên đơn hàng: cấp vốn làm thử, bù phần thiếu & ảo giác số dư trên màn hình",
    "duration_sec": total,
    "visual_style_lock": (
        "Horizontal 16:9 widescreen (1920x1080), semi-realistic cinematic 2D anime illustration, "
        "contemporary Southern Vietnam urban setting, naturalistic dramatic lighting, clean bottom 15% for subtitles, "
        "no text, no letters, no numbers, no license plates, no logos, no real app interface, no real uniforms"
    ),
    "hook": {
        "kicker": "BẪY CỘNG TÁC VIÊN ĐƠN HÀNG · ĐÊM THỨ BA",
        "title": "BA TRIỆU TÁM TRÊN MÀN HÌNH",
        "start": 0.4,
        "end": 5.0,
    },
    "chapters": chapters,
    "scenes": scenes,
    "dialogue": dialogue,
    "chat_bubbles": bubbles,
    "callouts": [],
    "red_flags": {
        "title": "NHỚ KỸ – BẪY CỘNG TÁC VIÊN ĐƠN HÀNG",
        "start": marks["rf_start"],
        "end": marks["rf_end"],
        "stagger_sec": 0.45,
        "items": [
            "VIỆC LÀM THẬT KHÔNG BẮT NẠP TIỀN: Mọi yêu cầu bù phần thiếu hay đóng phí đối soát đều là bẫy",
            "ĐỪNG TIN SỐ DƯ TRÊN TRANG LẠ: Kẻ gian tự tạo đơn, tự cộng hoa hồng ảo và khóa nút rút bất cứ lúc nào",
            "CẢNH GIÁC VỐN CẤP SẴN & MỒI MƯỜI NGÀN: Cho sẵn vài chục ngàn làm thử chỉ để kéo bạn vào chuỗi nạp bù",
            "DỪNG NGAY KHI BỊ ĐÒI BÙ ĐƠN LỚN: Cắt lỗ lập tức, tuyệt đối không nạp thêm tiền thật để cứu con số ảo",
            "KHÔNG THUÊ DỊCH VỤ LẤY LẠI TIỀN TREO: Lưu sao kê và đường dẫn để trình báo cơ quan công an, tránh bị lừa lần hai",
        ],
        "action": "Trước mọi lời mời làm cộng tác viên chốt đơn, hãy tự hỏi: tiền đang nằm trong ngân hàng của mình hay chỉ là con số gõ trên màn hình của người lạ?",
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
            {"start": marks["it_truth"] - 0.2, "end": marks["it_truth"] + 8.0, "bgm_db": -16, "amb_db": -10},
            {"start": marks["wife_warmth"] - 0.2, "end": marks["wife_warmth"] + 4.5, "bgm_db": -12, "amb_db": -6},
            {"start": marks["it_coda"] - 0.2, "end": marks["disc_start"] - 0.2, "bgm_db": -10, "amb_db": -7},
            {"start": marks["disc_start"], "end": total - 0.05},
        ],
    },
    "forbidden_terms": [],
    "publish": {
        "titles": [
            "Ví Hiện 3 Triệu 8 Mà Bắt Nạp Thêm – Cú Tra Tên Miền Nửa Đêm Bóc Trần Tất Cả | Bóc Trần Lừa Đảo",
            "Bù 10 Ngàn Phần Thiếu Khi Nhận Đơn Tại Nhà: Tiền Thật Đi Ra & Con Số Đứng Yên | Bóc Trần Lừa Đảo",
            "Trang Tuyển Cộng Tác Viên Ghi Từ Năm 2018, Tra Ra Mới Mở Tuần Trước | Bóc Trần Lừa Đảo",
        ],
        "description": (
            "Được cấp sẵn 40.000đ làm thử không tốn vốn, mỗi đơn sau chỉ bù thêm phần chênh lệch thiếu vài chục đến vài trăm ngàn — "
            "cho đến khi số dư trên màn hình nhảy lên 3.850.000đ nhưng nút rút tiền bất ngờ khóa chặt.\n\n"
            "⏱️ Các hồi trong phim:\n" + desc_chapters
        ),
        "pinned_comment": (
            "📌 Bạn hay người thân từng gặp chiêu 'cấp sẵn tiền làm thử' rồi dụ bù phần thiếu theo từng đơn chưa? "
            "Chia sẻ ở bình luận để mọi người cùng cảnh giác nhé (lưu ý không đăng SĐT, STK, tên miền thật hay tên người thật)."
        ),
        "hashtags": ["#bóctrầnlừađảo", "#cảnhgiáclừađảo", "#vạnchuyện", "#antoànmạng", "#cộngtácviênảo"],
        "tags": [
            "cảnh giác lừa đảo", "bóc trần lừa đảo", "vạn chuyện", "cộng tác viên đơn hàng",
            "bẫy bù tiền đơn hàng", "số dư ảo trên màn hình", "việc làm thêm tại nhà", "an toàn mạng",
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
