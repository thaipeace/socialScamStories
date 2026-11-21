# -*- coding: utf-8 -*-
"""
Trình biên dịch `factory196/materialAndDraft/EP08b/episode.json` – Tập EP08b:
"Tiền nổi rồi, tên lại khác" (16:9 Long-form · Nối tiếp trực tiếp dòng tiền 45 triệu từ EP08 · v1-draft).

Nguồn sự thật duy nhất của timeline: sửa thoại/nhịp ở phần STORY rồi chạy lại
    python3 factory196/materialAndDraft/EP08b/source/build_draft.py
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
# 10 tuyến nhân vật = 10 voice hoàn toàn tách biệt trong 02_CAST/cast.json
# Lưu ý đồng bộ vũ trụ EP08 ↔ EP08b ↔ EP04:
# - KHANG_ECHO dùng đúng voice `Puck` + `af="memory"` (khớp Khang của EP08)
# - Kẻ đứng giữa dùng đúng voice `Fenrir` (`chu_no` của EP08 & đầu dây bí ẩn cuối EP04)
# - Long dùng đúng voice `Algieba` (khớp câu đầu dây lạ `l22b_long_p` lúc 12:05 ở EP08)
# - Nam tách sang voice `Achird` để không trùng `Puck` của Khang
# - Người phụ nữ bí mật ở kết mở dùng đúng voice `Kore` (`chi_ba` – hơi liên đới Chị Hai vụ vé 300tr ở EP04, giấu mặt 100%)
NOT_OLD = "tuyệt đối không giả giọng ông già hay bà già run rẩy, không kéo dài chữ, không cải lương"
KHANG_BASE = (
    "Giọng nam thanh niên miền Nam Sài Gòn 26 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
    "giữ cố định một âm sắc sáng trẻ, nhịp nhanh gọn, thật thà lễ phép, rõ chữ, tự nhiên như đời thực, "
    + NOT_OLD
)
MINH_BASE = (
    "Giọng nam miền Nam Sài Gòn 39 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
    "giữ cố định một âm sắc trầm chắc, thẳng tính, đời thường, nói gọn rõ chữ, tự nhiên như đời thực, "
    + NOT_OLD
)
THAO_BASE = (
    "Giọng phụ nữ miền Nam Sài Gòn 36 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
    "giữ cố định một âm sắc ấm, trầm vừa, cẩn thận thực tế, nói gọn chắc, tự nhiên như đời thực, "
    + NOT_OLD
)
NAM_BASE = (
    "Giọng nam thanh niên miền Nam Sài Gòn 28 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
    "giữ cố định một âm sắc gọn, sáng vừa, nhanh nhẹn, thật thà gần gũi, rõ chữ, tự nhiên như đời thực, "
    + NOT_OLD
)
BUYER_BASE = (
    "Giọng nam miền Nam Sài Gòn 40 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
    "giữ cố định một âm sắc trầm đều, lịch sự mà lạnh tĩnh như kẻ cầm quân cờ, không la hét, "
    + NOT_OLD
)
PROXY_NU_BASE = (
    "Giọng nữ miền Nam Sài Gòn 31 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
    "giữ cố định một âm sắc ngọt ngào lịch sự nhưng nhanh chóng chột dạ lúng túng khi bị chặn, "
    + NOT_OLD
)

SPK = {
    "KHANG_ECHO": dict(
        speaker="thang_tun",
        voice="Puck",
        af="memory",
        label_short="KHANG (EP08)",
        speaker_label="Khang (EP08) – tiếng vọng hồi ức từ khoảnh khắc chuyển 45 triệu sang tài khoản lạ",
        base=KHANG_BASE,
    ),
    "MINH": dict(
        speaker="anh_hai",
        voice="Orus",
        label_short="ANH MINH",
        speaker_label="Anh Minh – chủ tiệm điện lạnh 39 tuổi, thẳng tính, bán chiếc xe máy tay ga 45 triệu",
        base=MINH_BASE,
    ),
    "MINH_P": dict(
        speaker="anh_hai",
        voice="Orus",
        af="phone",
        label_short="ANH MINH",
        speaker_label="Anh Minh gọi qua điện thoại cản gấp Nam ở phòng công chứng",
        base=MINH_BASE,
    ),
    "THAO": dict(
        speaker="chi_hai",
        voice="Sulafat",
        label_short="CHỊ THẢO",
        speaker_label="Chị Thảo – vợ Anh Minh 36 tuổi, tinh ý, thực tế, bình tĩnh xử lý đúng luật",
        base=THAO_BASE,
    ),
    "NAM": dict(
        speaker="thang_tun",
        voice="Achird",
        label_short="NAM",
        speaker_label="Nam – em họ 28 tuổi, thật thà, phản ứng nhanh khi được nhắc kịp thời",
        base=NAM_BASE,
    ),
    "BUYER_MSG": dict(
        speaker="chu_no",
        voice="Fenrir",
        af="phone",
        label_short="KHÁCH MUA",
        speaker_label="Kẻ đứng giữa (từ EP08) đóng vai nick 'Anh Hùng' nhắn chốt mua xe máy 45 triệu",
        base=BUYER_BASE,
    ),
    "BUYER_ROOM": dict(
        speaker="chu_no",
        voice="Fenrir",
        af="default",
        label_short="KẺ ĐỨNG GIỮA",
        speaker_label="Kẻ đứng giữa giấu mặt trong phòng tối – khớp giọng và bối cảnh 2 điện thoại của EP08",
        base=BUYER_BASE,
    ),
    "LONG": dict(
        speaker="ke_ngot_ngao_nam",
        voice="Algieba",
        af="default",
        label_short="LONG",
        speaker_label="Long – người 32 tuổi lịch sự đứng tên mua hộ (khớp giọng Algieba ở EP08 s08)",
        base=(
            "Giọng nam miền Nam Sài Gòn 32 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
            "giữ cố định một âm sắc sáng vừa, mượt mà, lịch sự khéo léo kiểu dân văn phòng, nói nhanh gọn, "
            + NOT_OLD
        ),
    ),
    "LONG_P": dict(
        speaker="ke_ngot_ngao_nam",
        voice="Algieba",
        af="phone",
        label_short="LONG",
        speaker_label="Long báo cáo qua cuộc gọi nhóm đường dây ngầm ở kết mở",
        base=(
            "Giọng nam miền Nam Sài Gòn 32 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
            "giữ cố định một âm sắc sáng vừa, mượt mà, gọn gàng kiểu tay chân báo cáo sếp, "
            + NOT_OLD
        ),
    ),
    "BANK_P": dict(
        speaker="chi_tu",
        voice="Zephyr",
        af="phone",
        label_short="NGÂN HÀNG",
        speaker_label="Nhân viên ngân hàng 29 tuổi gọi xác minh dòng tiền 45 triệu từ đơn trình báo của Khang",
        base=(
            "Giọng nữ miền Nam Sài Gòn 29 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
            "giữ cố định một âm sắc rõ ràng, chuẩn mực, điềm tĩnh kiểu tổng đài viên ngân hàng, "
            + NOT_OLD
        ),
    ),
    "PROXY_NU": dict(
        speaker="ke_ngot_ngao_nu",
        voice="Aoede",
        af="default",
        label_short="NGƯỜI MUA HỘ",
        speaker_label="Người phụ nữ 31 tuổi lịch sự đóng vai đứng tên mua hộ ở Hồi 5",
        base=PROXY_NU_BASE,
    ),
    "PROXY_NU_P": dict(
        speaker="ke_ngot_ngao_nu",
        voice="Aoede",
        af="phone",
        label_short="NGƯỜI MUA HỘ",
        speaker_label="Người mua hộ nữ gọi điện báo động cho bà trùm ở kết mở",
        base=PROXY_NU_BASE,
    ),
    "BOSS_NU": dict(
        speaker="chi_ba",
        voice="Kore",
        af="default",
        label_short="NGƯỜI PHỤ NỮ BÍ ẨN",
        speaker_label="Nhân vật nữ bí mật giấu mặt – hơi liên đới âm sắc & thần thái sắc lạnh kiệm lời của Chị Hai (EP04)",
        base=(
            "Giọng phụ nữ miền Nam Sài Gòn 35 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
            "giữ cố định một âm sắc sắc lạnh, trầm tĩnh, kiệm lời đầy uy quyền, nói ngắn cắt gọn không chút cảm xúc, "
            + NOT_OLD
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
# ---- HOOK · MÔ-TÍP MÀU SẮC 12:05 (CHƯA LỘ TÊN) & CÚ GỌI XÁC MINH 45 TRIỆU (00:00 – 00:26) ----
amb("office", -3.0); bgm("suspense_pulse", -2.5)
scene("s00a_pulse_1205", "assets/c00a.jpg", "push")
sfx("typing", 0.1, -5, dur=0.6)
sfx("message_send", 0.75, -3)
sfx("bank_ting", 1.2, -2.5)
bubble("BIẾN ĐỘNG SỐ DƯ · 12:05", "+45.000.000đ · Đã vào tài khoản · Công chứng xong",
       side="left", y=260, stamp="TIỀN THẬT ĐÃ NỔI", dur=2.2, offset=0.2)
beat(2.3)

amb("room_tone", -2.5); bgm("suspense_pulse", -2.5)
scene("s00b_hook_call", "assets/c00.jpg", "push", tr="flash_white", trd=0.2, shake=0.18)
sfx("phone_ring", 0.1, -4, dur=0.8)
bubble("XÁC MINH DÒNG TIỀN · NGÂN HÀNG", "Đơn trình báo vụ lừa 45.000.000đ · Chảy thẳng vào TK này",
       side="left", y=260, stamp="YÊU CẦU XÁC MINH", dur=4.5, offset=0.15)
beat(0.85)
line("l01_bank_p", "BANK_P",
     "Chào anh Minh. Có đơn trình báo vụ lừa bốn lăm triệu, tiền chảy thẳng vô tài khoản anh.",
     "chuẩn mực, bình tĩnh qua điện thoại",
     sub="Chào anh Minh. Có đơn trình báo vụ lừa 45 triệu, tiền chảy thẳng vô tài khoản anh.")
line("l02_minh", "MINH",
     "Khoan chị! Bốn lăm triệu đó khách mua xe máy chuyển tại phòng công chứng mà! Tôi giao xe rồi!",
     "sững người, giọng gấp gáp khó tin",
     sub="Khoan chị! 45 triệu đó khách mua xe máy chuyển tại phòng công chứng mà! Tôi giao xe rồi!")
line("l03_bank_p", "BANK_P",
     "Nhưng người chuyển báo bị lừa, không mua xe của anh. Nội dung cũng không ghi mua xe.",
     "rõ ràng, dứt khoát đúng nghiệp vụ")

scene("s01_hook_freeze", "assets/c01.jpg", "tense", tr="flash_white", trd=0.22, shake=0.15)
mark("hook_freeze")
sfx("impact", 0.0, -2.5)
bubble("SAO KÊ NGÂN HÀNG · 12:05", "+45.000.000đ · Từ: TÊN LẠ · ND: Chuyen tien",
       side="left", y=260, stamp="TIỀN TỪ VỤ LỪA?", dur=2.0, offset=0.15)
sfx("heartbeat", 0.2, -5, dur=1.6)
beat(1.9)

# ---- HỒI 1 · BA HÔM TRƯỚC: KHÁCH CHỐT KHÔNG MẶC CẢ ----
amb("street", -5.0); bgm("investigative_story", -3.8)
scene("s02_sell_bike_cafe", "assets/c02.jpg", "calm", tr="fade_black", trd=0.45)
chapter("HỒI 1 · BA HÔM TRƯỚC", "KHÁCH CHỐT KHÔNG MẶC CẢ")
sfx("chapter_sting", -0.1, -5)
beat(0.55)
line("l04_nam", "NAM",
     "Chiếc tay ga rao bốn lăm triệu cả tuần, thợ trả bốn chục. Chắc bớt chút mới trôi.",
     "uống trà đá nói chuyện thoải mái",
     sub="Chiếc tay ga rao 45 triệu cả tuần, thợ trả 40. Chắc bớt chút mới trôi.")
line("l05_minh", "MINH",
     "Sáng nay có anh Hùng hỏi mua. Coi hình xong chốt thẳng bốn lăm triệu, hông trả giá một đồng!",
     "mừng rỡ khoe với em họ và vợ",
     sub="Sáng nay có anh Hùng hỏi mua. Coi hình xong chốt thẳng 45 triệu, hông trả giá một đồng!")
line("l06_thao", "THAO",
     "Nghe dễ quá cũng lạ nha anh. Sao ổng hông qua coi xe trực tiếp?",
     "nhíu mày nhẹ, đặt câu hỏi thực tế")
line("l07_minh", "MINH",
     "Ổng công tác xa, thấy xe hợp màu nên chốt. Tiền nổi vô tài khoản anh mới ký công chứng, sợ gì!",
     "xua tay tự tin tuyệt đối vào quy tắc cũ")
line("l08_nam", "NAM",
     "Gặp khách sộp vậy sướng ha! Ít bữa em bán xe máy chắc cũng lên nhóm rao thử.",
     "cười trầm trồ thật thà", pause=0.15)

amb("night_room", -2.8); bgm("tension_drone", -3.0)
scene("s03_buyer_chat_dark", "assets/c03.jpg", "push", tr="fade_black", trd=0.4)
sfx("typing", 0.15, -5, dur=0.8)
sfx("message_send", 0.9, -4)
bubble("KHÁCH MUA · ANH HÙNG", "Chốt 45tr · Nhờ em họ Long đứng tên mua hộ",
       side="left", y=260, stamp="MỒI CHỐT NHANH", dur=4.8, offset=0.15)
beat(0.5)
line("l09_buyer_msg", "BUYER_MSG",
     "Anh bận công tác xa chưa về kịp, nên nhờ em họ tên Long ra công chứng đứng tên mua hộ.",
     "lịch sự, bình thản đầy tin cậy")
line("l10_buyer_msg", "BUYER_MSG",
     "Chú yên tâm. Bao giờ tiền nổi đủ bốn lăm triệu trong tài khoản rồi hẵng ký giao xe!",
     "chủ động trấn an để hạ cảnh giác",
     sub="Chú yên tâm. Bao giờ tiền nổi đủ 45 triệu trong tài khoản rồi hẵng ký giao xe!",
     pause=0.15)

# ---- HỒI 2 · 12 GIỜ TRƯA HÔM SAU: PHÒNG CÔNG CHỨNG ĐÔNG ĐÚC & MỘT THOÁNG GỢN LẠ ----
amb("crowd", -5.5); bgm("investigative_story", -4.0)
scene("s04_notary_meeting", "assets/c04.jpg", "calm", tr="fade_black", trd=0.4)
chapter("HỒI 2 · TRƯA HÔM SAU", "TIỀN ĐÃ NỔI TRONG TÀI KHOẢN")
sfx("chapter_sting", -0.1, -5)
beat(0.55)
line("l11_long", "LONG",
     "Em là Long, em họ anh Hùng. Hồ sơ nộp quầy rồi, chờ gọi tên thôi anh chị.",
     "cười lịch sự, gọn gàng giữa sảnh công chứng đông người")
line("l12_thao", "THAO",
     "Rồi chút nữa bên anh Hùng chuyển thẳng qua luôn hả cậu?",
     "hỏi xã giao bình thường, không chút căng thẳng")
line("l13_long", "LONG",
     "Dạ ảnh đang bấm chuyển đó chị, tiền vô là mình vô ký gọn.",
     "trấn an nhẹ nhàng, hoàn toàn tự nhiên", pause=0.15)

amb("crowd", -5.5); bgm("suspense_pulse", -4.2)
scene("s05_money_arrives_mismatch", "assets/c05.jpg", "tense", tr="dissolve", trd=0.3)
mark("money_mismatch")
sfx("bank_ting", 0.15, -2.5)
bubble("NGÂN HÀNG CỦA MINH · 12:05", "+45.000.000đ · Đã vào tài khoản",
       side="left", y=260, stamp="ĐÃ NHẬN TIỀN", dur=4.2, offset=0.15)
beat(0.6)
line("l14_minh", "MINH",
     "Đủ bốn lăm triệu rồi. Ra ký đi em.",
     "nhìn thoáng số dư, giọng nhẹ hẳn xuống đầy yên tâm và kiệm lời",
     sub="Đủ 45 triệu rồi. Ra ký đi em.")
line("l15_thao", "THAO",
     "Ủa… người gửi sao tên Khang lạ vậy anh?",
     "liếc màn hình đúng nửa giây, khựng nhẹ hỏi nhỏ")
line("l16_long", "LONG",
     "Kế toán bên công ty ảnh chuyển đó chị. Tới số mình vô ký rồi.",
     "cười nhẹ lịch sự, gật gọn tự nhiên hướng về quầy công chứng", pause=0.15)

amb("street", -4.5); bgm("investigative_story", -3.8)
scene("s06_sign_handover", "assets/c06.jpg", "hand", tr="dissolve", trd=0.35)
sfx("footsteps", 0.15, -5, dur=1.0)
bubble("HỢP ĐỒNG CÔNG CHỨNG", "Bên mua: Long · Đã nhận đủ 45.000.000đ · Đã giao xe",
       side="left", y=260, stamp="XONG TRÊN GIẤY", dur=4.0, offset=0.15)
beat(0.5)
line("l17_long", "LONG",
     "Cảm ơn anh chị nha. Em chạy xe về nhà anh Hùng đây!",
     "tươi cười nhận chìa khóa, nổ máy chạy chiếc tay ga đi", pause=0.2)

# ---- HỒI 3 · HAI NGÀY SAU: NICK ĐÃ XÓA, DÒNG TIỀN TỪ VỤ LỪA KHÁC ----
amb("room_tone", -2.5); bgm("tension_drone", -2.5)
scene("s07_call_blocked", "assets/c07.jpg", "tense", tr="fade_black", trd=0.4, shake=0.15)
chapter("HỒI 3 · HAI NGÀY SAU", "NICK ĐÃ XÓA, XE ĐÃ SANG TAY")
sfx("chapter_sting", -0.1, -5)
sfx("phone_ring", 0.2, -5, dur=0.7)
sfx("call_end", 0.95, -3)
bubble("LIÊN HỆ NGƯỜI MUA", "Nick khách mua đã xóa · Số của Long tắt máy",
       side="left", y=260, stamp="MẤT DẤU CẢ HAI", dur=4.2, offset=0.25)
beat(1.0)
line("l18_minh", "MINH",
     "Trời đất ơi! Nick ông Hùng xóa rồi! Gọi số thằng Long cũng tắt máy luôn!",
     "tái mặt hoảng hốt, giọng run lên")
line("l19_thao", "THAO",
     "Lúc ký em thoáng thấy tên Khang lạ mà tưởng tiền vô là xong… Người đó là ai?",
     "sững người lo lắng, chợt nhớ lại khoảnh khắc hôm công chứng")
line("l20_minh", "MINH",
     "Công an nói anh Khang bị giả sếp nhờ mua quà kỷ niệm cho vợ, lừa chuyển bốn lăm triệu vô máy mình!",
     "giọng trầm nặng, bàng hoàng không tin nổi",
     sub="Công an nói anh Khang bị giả sếp nhờ mua quà kỷ niệm cho vợ, lừa chuyển 45 triệu vô máy mình!")

# CÚ NỔ TWIST HỒI 3: Hồi ức trực tiếp mặt Khang & Anh Đạt (EP08) + giọng thật Puck gọi "anh Đạt ơi"!
amb("office", -4.5); bgm("tension_drone", -2.0)
scene("s08a_ep08_twist", "assets/c08a.jpg", "push", tr="flash_white", trd=0.22, shake=0.18)
mark("ep08_twist")
sfx("impact", 0.0, -2.0)
bubble("12:05 · MẢNH GHÉP CÒN LẠI", "Khang (-45.000.000đ)  →  Chảy thẳng vào tài khoản Anh Minh",
       side="left", y=260, stamp="CÙNG MỘT VỤ LỪA", dur=5.0, offset=0.15)
beat(0.35)
line("l20b_khang_echo", "KHANG_ECHO",
     "Nó chặn mất rồi anh Đạt ơi… Bốn mươi lăm triệu em vừa chuyển qua tài khoản lạ rồi!",
     "tái mặt nghẹn giọng — trích nguyên khoảnh khắc vỡ lẽ từ EP08 (voice Puck)",
     sub="Nó chặn mất rồi anh Đạt ơi… 45 triệu em vừa chuyển qua tài khoản lạ rồi!", pause=0.2)

amb("room_tone", -2.5); bgm("tension_drone", -2.5)
scene("s08b_paper_trap", "assets/c08.jpg", "push", tr="dissolve", trd=0.35)
mark("paper_trap")
sfx("heartbeat", 0.2, -5, dur=1.6)
beat(0.35)
line("l21_thao", "THAO",
     "Hợp đồng bán xe cho Long ghi nhận đủ, còn tiền lại từ anh Khang bị lừa!",
     "đặt hai tờ giấy cạnh nhau trên bàn, giọng trầm căng")
line("l22_minh", "MINH",
     "Nội dung chỉ ghi chuyển tiền, không biển số, không ngày hợp đồng… Cả hai đều là nạn nhân!",
     "ôm trán bàng hoàng nhận ra cái bẫy kế trùng kế", pause=0.15)

# ---- HỒI 4 · LỘ DIỆN CƠ CHẾ: MỘT DÒNG TIỀN, HAI NẠN NHÂN & XỬ LÝ ĐÚNG LUẬT ----
amb("night_room", -2.5); bgm("suspense_pulse", -2.5)
scene("s09_triangle_reveal", "assets/c09.jpg", "push", tr="flash_white", trd=0.22, shake=0.14)
chapter("HỒI 4 · LỘ DIỆN CƠ CHẾ", "TAM GIÁC LỆCH DÒNG TIỀN")
mark("triangle_reveal")
sfx("impact", 0.0, -2.5)
bubble("BẪY TAM GIÁC · 12:05 TRƯA", "Khang chuyển 45tr → TK Minh · Long công chứng lấy xe máy",
       side="left", y=260, stamp="RỬA TIỀN SẠCH", dur=5.2, offset=0.2)
beat(0.5)
line("l23_buyer_room", "BUYER_ROOM",
     "Đầu kia lừa thằng Khang đẩy bốn lăm triệu. Đầu này cho Long công chứng hốt chiếc xe máy.",
     "trầm lạnh điềm nhiên từ phòng tối hai điện thoại",
     sub="Đầu kia lừa thằng Khang đẩy 45 triệu. Đầu này cho Long công chứng hốt chiếc xe máy.")
line("l24_buyer_room", "BUYER_ROOM",
     "Tiền bẩn đổi ra xe thật trong một buổi trưa. Hai nạn nhân tự giải trình với nhau!",
     "lạnh tĩnh chốt gọn ván cờ hai đầu dây", pause=0.15)

amb("room_tone", -3.0); bgm("investigative_story", -3.6)
scene("s10_response_action", "assets/c10.jpg", "calm", tr="fade_black", trd=0.4)
mark("response_action")
beat(0.3)
line("l25_minh", "MINH",
     "Hay anh rút bốn lăm triệu cất trước, chừng nào kiếm lại được xe rồi mới tính?",
     "sốt ruột định làm theo phản xạ",
     sub="Hay anh rút 45 triệu cất trước, chừng nào kiếm lại được xe rồi mới tính?")
line("l26_thao", "THAO",
     "Khoan! Đừng rút hay chuyển đi đâu! Tiền đang xác minh vụ án mà tự tẩu tán còn rắc rối nặng hơn!",
     "cản ngay lập tức, giọng điềm tĩnh kiên quyết")
line("l27_minh", "MINH",
     "Vậy giữ nguyên tiền trong tài khoản, gom hợp đồng, sao kê với tin nhắn trình báo công an liền!",
     "hít sâu lấy lại bình tĩnh, gật đầu dứt khoát", pause=0.2)

# ---- HỒI 5 · HAI TUẦN SAU: CÚ GỌI CHẶN BẪY & NGUYÊN TẮC 2 PHẢI – 3 KHÔNG ----
amb("crowd", -5.5); bgm("suspense_pulse", -3.0)
scene("s11_nam_calls_notary", "assets/c11.jpg", "hand", tr="fade_black", trd=0.45)
chapter("HỒI 5 · HAI TUẦN SAU", "NGUYÊN TẮC HAI PHẢI, BA KHÔNG")
sfx("chapter_sting", -0.1, -5)
sfx("phone_ring", 0.25, -4, dur=0.8)
beat(0.95)
line("l28_nam", "NAM",
     "Alo anh Minh! Em đang công chứng bán xe máy. Khách chốt nhanh, nhờ người thân đứng tên hộ!",
     "vui vẻ gọi khoe anh họ ngay trước khi ký")
line("l29_minh_p", "MINH_P",
     "Khoan ký! Dừng lại liền! Anh mới dính bẫy tam giác kẹt cứng bốn lăm triệu đây nè!",
     "quát gấp qua điện thoại để chặn ngay lập tức",
     sub="Khoan ký! Dừng lại liền! Anh mới dính bẫy tam giác kẹt cứng 45 triệu đây nè!")

amb("street", -4.5); bgm("action_climax", -3.2)
scene("s12_minh_warns_rule", "assets/c12.jpg", "tense", tr="dissolve", trd=0.3)
mark("two_musts")
bubble("NGUYÊN TẮC 2 PHẢI", "1. Ai ký HĐ, người đó chuyển · 2. Ghi tên, mua xe, BSX, ngày HĐ",
       side="left", y=260, stamp="CHẶN BẪY NGAY", dur=5.2, offset=0.15)
beat(0.3)
line("l30_minh", "MINH",
     "Ai ký hợp đồng chính người đó chuyển tiền. Tuyệt đối không nhận tài khoản thứ ba chuyển giùm!",
     "dặn nhanh, rõ từng chữ đầy khẩn thiết")
line("l31_minh", "MINH",
     "Nội dung ghi rõ họ tên, mua xe, biển số và ngày hợp đồng. Lệch tên là dừng ký!",
     "nhấn mạnh nguyên tắc sống còn", pause=0.15)

amb("crowd", -5.5); bgm("action_climax", -2.5)
scene("s13_nam_tests_proxy", "assets/c13.jpg", "tense", tr="dissolve", trd=0.3)
mark("confrontation")
sfx("riser", 0.0, -4.5, dur=0.8)
beat(0.3)
line("l32_nam", "NAM",
     "Hợp đồng tên chị nên chị dùng đúng tài khoản tên chị chuyển, ghi rõ biển số với ngày hợp đồng nha!",
     "bình tĩnh dứt khoát, nhìn thẳng đối phương")
line("l33_proxy_nu", "PROXY_NU",
     "Ủa… chồng chị ở xa chuyển giùm cho nhanh, tiền vô rồi cần gì rắc rối?",
     "hơi khựng lại nhưng cố cười trấn an")
line("l34_nam", "NAM",
     "Không được chị. Lệch tên hay mập mờ em không ký, tiền lỡ vô em cũng ra ngân hàng hoàn lại.",
     "kiên quyết đóng chặt mọi kẽ hở", pause=0.15)

scene("s14_scammer_flees", "assets/c14.jpg", "push", tr="flash_white", trd=0.2, shake=0.14)
sfx("impact", 0.0, -2.5)
sfx("footsteps", 0.35, -4, dur=1.1)
beat(0.35)
line("l35_proxy_nu", "PROXY_NU",
     "À… thôi để chị ra ngoài gọi hỏi lại chồng chút nha!",
     "lúng túng chột dạ, vội gom giấy đứng dậy đi thẳng")
line("l36_nam", "NAM",
     "Đi mất tiêu rồi! May gọi kịp anh Minh… suýt chút nữa mất trắng chiếc xe!",
     "thở phào nhẹ nhõm nhìn theo bóng người kia rời khỏi cửa", pause=0.2)

amb("room_tone", -5.0); bgm("investigative_story", SILENT)
scene("s15_outro_still", "assets/c15.jpg", "still", tr="fade_black", trd=0.4)
beat(0.8)

# ---- THẺ NHỚ KỸ (< 10 GIÂY) ----
amb("room_tone", -5.0); bgm("warm_outro", -4.2)
scene("s16_red_flags", EP01B + "scene18.jpg", "still", tr="fade_black", trd=0.4)
mark("rf_start")
sfx("bank_ting", 0.0, -5)
line("l37_narr", "N",
     "Tiền nổi rồi vẫn mất nếu lệch tên. Ai ký hợp đồng người đó chuyển, ghi rõ mục đích.")
beat(0.5)
mark("rf_end")

# ---- KẾT MỞ ĐƯỜNG DÂY NGẦM (CỘC GỌN SẮC LẠNH · HỘI TỤ MẮT XÍCH EP08 & EP08b · LIÊN ĐỚI MỜ CHỊ HAI EP04) ----
amb("rain", -3.2); bgm("tension_drone", -2.4)
scene("s17a_syndicate_grid", "assets/c16a.jpg", "push", tr="fade_black", trd=0.4)
mark("boss_coda")
sfx("phone_vibrate", 0.1, -5, dur=0.5)
beat(0.3)
line("l38a_ke_p", "BUYER_MSG",
     "Bên ông Đạt với Khang… công an vào cuộc.",
     "báo cáo cộc gọn, lạnh tĩnh qua điện thoại từ phòng tối EP08", pause=0.12)
line("l38b_long_p", "LONG_P",
     "Chiếc tay ga đẩy xong. Số hủy sạch.",
     "ngắn gọn, dứt khoát qua điện thoại", pause=0.12)
line("l38c_proxy_p", "PROXY_NU_P",
     "Khu này động. Chủ xe đòi chính chủ chuyển.",
     "gấp gáp, cộc gọn báo động qua điện thoại", pause=0.2)

scene("s17b_boss_order", "assets/c16b.jpg", "push", tr="dissolve", trd=0.25)
sfx("heartbeat", 0.0, -5, dur=0.9)
beat(0.35)
line("l39_boss_nu", "BOSS_NU",
     "Bỏ xe. Dời vùng. Sang kèo đất.",
     "lạnh băng, cắt gọn ba nhịp dứt khoát, không chút cảm xúc — gợi âm hưởng 'Cứ để đó!' ở EP04", pause=0.15)

sfx("impact", 0.0, -1.5)
scene("s18_black_cut", "assets/c17.jpg", "still", tr="fade_black", trd=0.08)
beat(1.3)

# ---- DISCLAIMER ----
amb("room_tone", -6.0); bgm("warm_outro", -7.5)
scene("s19_disclaimer", EP01B + "scene18.jpg", "still", tr="fade_black", trd=0.35)
mark("disc_start")
beat(4.0)

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


_desc = [(0.0, "Mở đầu – Tiền 45 triệu đã nổi, công chứng rồi sao vẫn mất?")]
_desc += [(c["start"] - 0.2, f"{c['kicker'].split('·')[0].strip().title()} – {c['title'].capitalize()}")
          for c in chapters if c["kicker"]]
_desc += [(marks["rf_start"], "Nhớ kỹ – Nguyên tắc 2 Phải, 3 Không khi bán xe, bán đất")]
desc_chapters = "\n".join(f"{mmss(max(0.0, s))} {label}" for s, label in sorted(_desc))

episode = {
    "episode_id": "EP08b",
    "slug": "TienNoiRoiTenLaiKhac",
    "title": "Tiền nổi rồi, tên lại khác",
    "version": "v1-draft",
    "scam_family": "VAR-MITM-02 / VAR-COM-04 · TRIANGULATION-PAYMENT-MISMATCH – Nửa bên kia dòng tiền 45 triệu từ EP08: bẫy tam giác đẩy tiền của nạn nhân vụ lừa khác vào tài khoản người bán xe máy công chứng",
    "duration_sec": total,
    "visual_style_lock": (
        "Horizontal 16:9 widescreen (1920x1080), semi-realistic cinematic 2D anime illustration, "
        "contemporary Southern Vietnam urban setting, naturalistic dramatic lighting, clean bottom 15% for subtitles, "
        "no text, no letters, no numbers, no license plates, no logos, no real app interface, no real uniforms"
    ),
    "hook": {
        "kicker": "12:05 TRƯA · CÔNG CHỨNG THẬT",
        "title": "TIỀN NỔI RỒI, TÊN LẠI KHÁC",
        "start": 0.4,
        "end": 5.0,
    },
    "chapters": chapters,
    "scenes": scenes,
    "dialogue": dialogue,
    "chat_bubbles": bubbles,
    "callouts": [],
    "red_flags": {
        "title": "NHỚ KỸ – NGUYÊN TẮC 2 PHẢI, 3 KHÔNG",
        "start": marks["rf_start"],
        "end": marks["rf_end"],
        "stagger_sec": 0.42,
        "items": [
            "PHẢI TRÙNG KHỚP 100%: Ai đứng tên ký hợp đồng mua bán thì chính chủ tài khoản đó chuyển tiền",
            "PHẢI GHI RÕ NỘI DUNG: Họ tên người mua + thanh toán mua xe + biển số + theo hợp đồng ngày ký",
            "KHÔNG NHẬN NGƯỜI THỨ BA CHUYỂN HỘ: Từ chối mọi lý do tài khoản người thân hay công ty chuyển giùm",
            "LỆCH TÊN HAY MẬP MỜ LÀ DỪNG KÝ NGAY: Tiền đã lỡ vào thì không giao xe và phối hợp ngân hàng hoàn trả",
            "CẢNH GIÁC KHÁCH CHỐT QUÁ DỄ: Không mặc cả, né gặp mặt, nhờ người khác đứng tên mua hộ",
        ],
        "action": "Nếu đã lỡ giao tài sản và nhận báo tiền từ vụ lừa khác, giữ nguyên tiền trong tài khoản, gom hợp đồng, sao kê và tin nhắn trình báo công an ngay.",
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
            {"start": marks["hook_freeze"] - 0.2, "end": marks["hook_freeze"] + 2.4, "bgm_db": -12, "amb_db": -8},
            {"start": marks["money_mismatch"] - 0.2, "end": marks["money_mismatch"] + 5.0, "bgm_db": -10, "amb_db": -7},
            {"start": marks["ep08_twist"] - 0.2, "end": marks["ep08_twist"] + 6.0, "bgm_db": -12, "amb_db": -8},
            {"start": marks["paper_trap"] - 0.2, "end": marks["paper_trap"] + 8.0, "bgm_db": -11, "amb_db": -7},
            {"start": marks["triangle_reveal"] - 0.2, "end": marks["triangle_reveal"] + 12.0, "bgm_db": -11, "amb_db": -8},
            {"start": marks["confrontation"] - 0.2, "end": marks["confrontation"] + 14.0, "bgm_db": -11, "amb_db": -7},
            {"start": marks["boss_coda"] - 0.2, "end": marks["disc_start"] - 0.2, "bgm_db": -10, "amb_db": -7},
            {"start": marks["disc_start"], "end": total - 0.05},
        ],
    },
    "forbidden_terms": [],
    "publish": {
        "titles": [
            "Tiền Nổi Đủ 45 Triệu Mới Ký Công Chứng Bán Xe Máy – Sao Hai Ngày Sau Vẫn Kẹt Cứng? | Bóc Trần Lừa Đảo",
            "Tiền Nổi Rồi, Tên Lại Khác: Cái Bẫy Ngay Tại Phòng Công Chứng Đông Người | Bóc Trần Lừa Đảo",
            "Bán Xe Máy Thấy Tiền Nổi Đủ 45 Triệu Mới Giao Xe – Sự Thật Đằng Sau Dòng Tiền Lạ | Bóc Trần Lừa Đảo",
        ],
        "description": (
            "Đúng 12 giờ 05 trưa tại phòng công chứng đông người, chủ xe máy thấy tiền thật nổi đủ 45 triệu trong tài khoản mới đặt bút ký giao xe — "
            "vậy mà hai ngày sau lại nhận thông báo khoản tiền đó chảy thẳng từ một vụ lừa đảo khác.\n\n"
            "Ghi nhớ nguyên tắc 2 Phải – 3 Không khi mua bán xe máy, ô tô, đất đai: ai ký hợp đồng thì chính người đó chuyển tiền, "
            "và nội dung chuyển khoản phải ghi rõ họ tên, tài sản/biển số cùng ngày hợp đồng.\n\n"
            "⏱️ Các hồi trong phim:\n" + desc_chapters
        ),
        "pinned_comment": (
            "📌 Tới Hồi 3 bạn có giật mình nhận ra cái tên 'Khang' và câu gọi 'anh Đạt ơi' nối thẳng từ tập trước không? "
            "Chia sẻ cảm nhận và kinh nghiệm đi công chứng mua bán xe bên dưới nhé!\n"
            "⚠️ Lưu ý: Không đăng SĐT, STK hay tên người thật; tuyệt đối cảnh giác mọi bình luận mời chào dịch vụ 'hỗ trợ lấy lại tiền'."
        ),
        "hashtags": ["#bóctrầnlừađảo", "#cảnhgiáclừađảo", "#vạnchuyện", "#bẫytamgiác", "#muabánxe"],
        "tags": [
            "cảnh giác lừa đảo", "bóc trần lừa đảo", "vạn chuyện", "lừa đảo tam giác",
            "lệch dòng tiền giao dịch", "lừa đảo mua bán xe công chứng", "nguyên tắc 2 phải 3 không",
            "rửa tiền mua xe máy", "an toàn giao dịch",
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
