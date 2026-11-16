# -*- coding: utf-8 -*-
"""
Trình biên dịch `factory196/materialAndDraft/EP27/episode.json` – Tập EP27:
"Sau khoản nợ cuối cùng" (16:9 Long-form · Tập đặc biệt Đêm Giao Thừa 05/02/2027).

Nguồn sự thật duy nhất của timeline: sửa thoại/nhịp ở phần STORY rồi chạy lại
    python factory196/materialAndDraft/EP27/source/build_draft.py
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
# Khóa voice theo 02_CAST/cast.json; base style cố định cho từng nhân vật, chỉ nối thêm sắc thái cảm xúc.
NOT_OLD = "tuyệt đối không giả giọng người già, không kéo dài chữ, không run rẩy, không cải lương"
SPK = {
    "MA": dict(
        speaker="co_tu", voice="Kore", label_short="MÁ", speaker_label="Má – Cô Tư, góa chồng, ở một mình",
        base=("Giọng phụ nữ miền Nam Sài Gòn, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
              "giữ cố định một âm sắc rõ chữ, hiền, tự nhiên như đời thực, tốc độ vừa phải, " + NOT_OLD),
    ),
    "AH": dict(
        speaker="anh_hai", voice="Orus", label_short="ANH HAI", speaker_label="Anh Hai – con trai, 36 tuổi",
        base=("Giọng nam miền Nam Sài Gòn 36 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
              "giữ cố định một âm sắc trầm, thẳng, nói câu nào chắc câu đó, tự nhiên đời thực"),
    ),
    "AH_MEM": dict(
        speaker="anh_hai", voice="Orus", af="memory", label_short="ANH HAI", speaker_label="Anh Hai – tiếng vọng ký ức",
        base=("Giọng nam miền Nam Sài Gòn 36 tuổi, phát âm chuẩn phương ngữ miền Nam, "
              "giữ cố định một âm sắc trầm, thẳng, chắc nịch, không lớn tiếng"),
    ),
    "CH": dict(
        speaker="chi_hai", voice="Sulafat", label_short="CHỊ HAI", speaker_label="Chị Hai – vợ Anh Hai, 34 tuổi",
        base=("Giọng phụ nữ miền Nam Sài Gòn 34 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
              "giữ cố định một âm sắc ấm, trầm vừa, ít lời; nói gọn, chắc, không ngân dài, không bi lụy"),
    ),
    "HA": dict(
        speaker="co_hanh", voice="Despina", label_short="HẠNH", speaker_label="Cô Hạnh – 'chị em cùng cảnh'",
        base=("Giọng phụ nữ miền Nam Sài Gòn khoảng 45 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
              "giữ cố định một âm sắc mượt, ngọt, thân tình; nói nhanh, gọn, hơi gấp như người lúc nào cũng đang chạy việc; "
              + NOT_OLD),
    ),
    "LONG_P": dict(
        speaker="chu_no", voice="Fenrir", af="phone", label_short="LONG", speaker_label="Long – chủ nợ (qua điện thoại)",
        base=("Giọng nam miền Nam Sài Gòn 40 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
              "giữ cố định một âm sắc trầm, đều, lịch sự mà lạnh; không la hét, không dồn dập"),
    ),
    "LONG": dict(
        speaker="chu_no", voice="Fenrir", label_short="LONG", speaker_label="Long – chủ nợ",
        base=("Giọng nam miền Nam Sài Gòn 40 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
              "giữ cố định một âm sắc trầm, đều, lịch sự mà lạnh; không la hét, không dồn dập"),
    ),
    "CB": dict(
        speaker="chi_tu", voice="Zephyr", label_short="CÁN BỘ", speaker_label="Cán bộ trợ giúp pháp lý",
        base=("Giọng phụ nữ miền Nam Sài Gòn 38 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
              "giữ cố định một âm sắc điềm tĩnh, rõ ràng, chậm vừa, thân thiện mà chắc chắn"),
    ),
    "TOM": dict(
        speaker="be_tom", voice="Puck", label_short="TOM", speaker_label="Bé Tom – cháu nội, 8 tuổi",
        base=("Giọng cậu bé trai 8 tuổi người miền Nam Sài Gòn, phát âm chuẩn phương ngữ miền Nam, "
              "trong sáng, lễ phép, nói tốc độ vừa phải, rõ chữ, tự nhiên như đời thực, giữ đúng một tông giọng duy nhất"),
    ),
    "N": dict(speaker="nguoi_boc_tran"),
}


def mo(kind: str) -> dict:
    return {
        "tense": {"scale": [1.04, 1.14], "focus": [[0.5, 0.5], [0.48, 0.45]], "wobble": "tense"},
        "calm": {"scale": [1.02, 1.09], "focus": [[0.5, 0.5], [0.5, 0.47]], "wobble": "calm"},
        "hand": {"scale": [1.02, 1.10], "focus": [[0.46, 0.48], [0.54, 0.46]], "wobble": "handheld"},
        "push": {"scale": [1.0, 1.16], "focus": [[0.5, 0.5], [0.5, 0.45]], "wobble": "calm"},
        "pull": {"scale": [1.12, 1.02], "focus": [[0.5, 0.46], [0.5, 0.5]], "wobble": "calm"},
        "still": {"scale": [1.0, 1.05], "focus": [[0.5, 0.5], [0.5, 0.5]], "wobble": "none"},
    }[kind]


E: list = []


def scene(sid, image, motion="calm", tr=None, trd=0.35, shake=None):
    E.append(("scene", dict(id=sid, image=image, motion=mo(motion), tr=tr, trd=trd, shake=shake)))


def line(lid, spk, text, emo="", sub=None, pause=0.0):
    E.append(("line", dict(id=lid, spk=spk, text=text, emo=emo, sub=sub, pause=pause)))


def beat(sec):
    E.append(("beat", sec))


def chapter(kicker, title, offset=0.2, dur=4.6):
    E.append(("chapter", dict(kicker=kicker, title=title, offset=offset, dur=dur)))


def bubble(sender, text, side="left", y=300, stamp="", dur=5.0, offset=0.0):
    E.append(("bubble", dict(sender=sender, text=text, side=side, y=y, stamp=stamp, dur=dur, offset=offset)))


def sfx(preset, offset=0.0, gain=-4, dur=None):
    E.append(("sfx", dict(preset=preset, offset=offset, gain=gain, dur=dur)))


def amb(preset, gain=-2.0):
    E.append(("amb", dict(preset=preset, gain=gain)))


def bgm(preset, gain=-1.5):
    E.append(("bgm", dict(preset=preset, gain=gain)))


def mark(name):
    E.append(("mark", name))


SILENT = -40.0   # "không có nhạc" – giữ run liên tục cho Gate 3 nhưng gần như tắt hẳn
EP01B = "factory196/materialAndDraft/EP01b/assets/"

# ================================================================ STORY
# ---- HOOK · C1 – CUỘC GỌI LÚC ĐÊM ----
amb("night_room", -1.5); bgm("suspense_pulse", -3.0)
scene("s00_night_call", "assets/c00.jpg", "push")
sfx("phone_vibrate", 0.0, -2, dur=2.4)
bubble("ĐIỆN THOẠI", "14 cuộc gọi nhỡ", side="right", y=260, stamp="SỐ LẠ", dur=4.0, offset=0.3)
beat(2.4)
line("l01_long", "LONG_P", "Chị Tư, hôm nay tới ngày rồi đó.", "đều đều, như nhắc chuyện thường ngày")
line("l02_ma", "MA", "Cho chị thêm ít bữa nữa nghen em.", "nhỏ giọng, ngại ngùng")
line("l03_long", "LONG_P", "Bữa nào chị cũng nói vậy. Không có thì kêu thằng Hai lo. Nó làm ở xưởng gần chợ mà, em biết chỗ.",
     "lạnh, chậm rãi nhấn ba chữ cuối")
line("l04_ma", "MA", "Đừng gọi cho con chị. Để chị tự lo.", "vội vàng, hoảng")
sfx("call_end", 0.0, -4)
scene("s01_finger_hover", "assets/c01.jpg", "push", tr="dissolve", trd=0.3)
bubble("DANH BẠ", "Con Hai", side="right", y=300, stamp="GỌI?", dur=4.2, offset=0.2)
beat(4.6)
sfx("impact", 0.0, -8)
beat(0.8)

# ---- HỒI 1 · THỜI ĐIỂM B (SAU ĐỢT TRẢ TIẾT KIỆM A) – "LẦN CUỐI" ----
amb("room_tone", -2.0); bgm("investigative_story", -3.0)
scene("s02_son_visit", "assets/c02.jpg", "calm", tr="fade_black", trd=0.4)
chapter("HỒI 1 · TƯỞNG ĐÃ YÊN", "LẦN CUỐI")
sfx("chapter_sting", -0.1, -5)
beat(0.6)
line("l05_ah", "AH", "Tiền để dành của vợ chồng con vét trả hết đợt trước rồi. Má đừng mượn bên ngoài nữa nghen.",
     "mệt nhưng kìm nén, nói thật lòng")
line("l06_ma", "MA", "Ừ, má biết rồi.", "nhỏ, tránh nhìn con")
line("l07_ah", "AH", "Lần này là lần cuối con trả. Lần sau má tự chịu đó.",
     "không lớn tiếng nhưng chắc nịch, dứt khoát", pause=0.6)
line("l08_ma", "MA", "Má biết mà. Con lo đi làm đi.", "gượng cười, giấu chuyện")
sfx("footsteps", 0.0, -8, dur=1.6)
scene("s03_tet_photo", "assets/c03.jpg", "push", tr="dissolve", trd=0.35)
beat(2.6)
sfx("notification", 0.0, -4)
bubble("HẠNH", "Chị Tư cần xoay thì nói em nha. Em có cách.", side="left", y=500, stamp="TIN NHẮN", dur=5.0, offset=0.1)
beat(5.2)

# ---- HỒI 2 · C3 – NGƯỜI CÙNG CẢNH NGỘ ----
amb("street", -4.0); bgm("investigative_story", -3.5)
scene("s04_tea_stall", "assets/c04.jpg", "calm", tr="fade_black", trd=0.4)
chapter("HỒI 2 · QUÁN NƯỚC ĐẦU HẺM", "NGƯỜI CÙNG CẢNH NGỘ")
sfx("chapter_sting", -0.1, -5)
beat(0.6)
line("l09_ha", "HA", "Chị còn thiếu nhiều hông?", "ân cần, hạ giọng")
line("l10_ma", "MA", "Chỗ này một ít, chỗ kia một ít. Trả chỗ này lại hụt chỗ kia.", "mệt mỏi, thở ra")
line("l11_ha", "HA", "Em cũng từng y chang chị. Có bữa đứng giữa chợ mà muốn khóc.", "đồng cảm, ngọt, nắm tay")
line("l12_ha", "HA", "Chị ký giấy mười triệu, cầm về tám triệu sáu. Chia đôi, em góp mỗi ngày phụ chị.",
     "nhẹ tênh như chuyện thường", sub="Chị ký giấy 10 triệu, cầm về 8 triệu 6. Chia đôi, em góp mỗi ngày phụ chị.")
line("l13_ma", "MA", "Sao mười triệu mà cầm có tám triệu sáu?", "ngập ngừng thắc mắc",
     sub="Sao 10 triệu mà cầm có 8 triệu 6?")
line("l14_ha", "HA", "Phí hồ sơ đó chị. Bên nào cũng trừ, em làm hoài à.", "gạt đi nhanh, bình thường hóa")
line("l15_ma", "MA", "Mà giấy đứng tên ai?", "dè dặt")
line("l16_ha", "HA", "Tên chị. Chị em mình mà, em bỏ chị sao được.", "nhanh, ngọt, đẩy cây bút qua")
scene("s05_signing", "assets/c05.jpg", "push", tr="dissolve", trd=0.3)
beat(3.4)
scene("s06_hanh_alone", "assets/c06.jpg", "calm", tr="dissolve", trd=0.3)
mark("commission")
sfx("bank_ting", 0.3, -3)
bubble("LONG", "+500.000 · hh khách chị Tư", side="left", y=260, stamp="HOA HỒNG 5%", dur=3.6, offset=0.3)
beat(3.8)
sfx("message_send", 0.0, -5)
sfx("message_send", 0.6, -5)
bubble("HẠNH CHUYỂN ĐI", "–500.000  ·  –4.300.000", side="right", y=320, stamp="10 GIÂY SAU", dur=3.6, offset=0.1)
beat(3.8)
sfx("phone_vibrate", 0.0, -4, dur=1.6)
beat(2.0)

# ---- C4 – MONTAGE 5 NGÀY (không thoại) ----
amb("room_tone", -3.0); bgm("suspense_pulse", -5.0)
scene("s07_ledger_days", "assets/c07.jpg", "still", tr="fade_black", trd=0.35)
for i in range(3):
    sfx("bank_ting", 0.2 + i * 2.0, -5)
    bubble(f"NGÀY {i + 1}", "Hạnh chuyển +150.000", side="left", y=280, stamp="GÓP", dur=1.9,
           offset=0.2 + i * 2.0)
beat(6.4)
sfx("phone_ring", 0.0, -6, dur=3.0)
bubble("NGÀY 4", "Đang gọi Hạnh…", side="right", y=260, stamp="KHÔNG BẮT MÁY", dur=3.2)
beat(3.4)
sfx("message_send", 0.0, -5)
bubble("NGÀY 5", "Hạnh ơi?", side="right", y=320, stamp="KHÔNG GỬI ĐƯỢC", dur=3.4)
beat(4.0)

# ---- HỒI 3 · C5 – CUỘC GỌI TỚI XƯỞNG ----
amb("office", -3.0); bgm("tension_drone", -4.0)
scene("s08_workshop_call", "assets/c08.jpg", "hand", tr="flash_red", trd=0.3)
chapter("HỒI 3 · XƯỞNG LÀM VIỆC", "CÚ SẬP")
sfx("phone_ring", 0.0, -5, dur=1.4)
beat(1.2)
line("l17_long", "LONG_P", "Anh Hai phải hông? Má anh nợ bên tôi chín triệu mốt. Trễ ba bữa rồi.", "lịch sự, lạnh tanh",
     sub="Anh Hai phải hông? Má anh nợ bên tôi 9 triệu 1. Trễ ba bữa rồi.")
line("l18_ah", "AH", "Anh là ai?", "sững sờ, gằn giọng")
line("l19_long", "LONG_P", "Anh khỏi cần biết. Chiều nay không có, mai tôi ghé xưởng nói chuyện với quản lý anh.",
     "chậm, đều, không cần to tiếng")
sfx("call_end", 0.0, -4)
beat(1.2)
bubble("CÀI ĐẶT", "Tự động ghi âm cuộc gọi: BẬT", side="right", y=280, stamp="ANH HAI", dur=3.2)
beat(3.4)

# ---- C6 – "MƯỜI TRIỆU, CẦM TÁM TRIỆU SÁU" ----
amb("room_tone", -2.0); bgm("tension_drone", -6.0)
scene("s09_paper_found", "assets/c09.jpg", "push", tr="fade_black", trd=0.35)
beat(0.8)
line("l20_ah", "AH", "Giấy ghi mười triệu. Má cầm về có tám triệu sáu?", "chậm, không tin nổi",
     sub="Giấy ghi 10 triệu. Má cầm về có 8 triệu 6?")
line("l21_ma", "MA", "Hạnh nói phí hồ sơ…", "lí nhí")
line("l22_ah", "AH", "Rồi tiền đâu?", "dồn, gắt nhẹ")
line("l23_ma", "MA", "Má đưa nó một nửa. Nó nói góp mỗi ngày phụ má.", "cúi mặt")
line("l24_ah", "AH", "Nó góp được mấy bữa?", "lạnh đi, biết trước câu trả lời")
beat(3.2)

# ---- C7 – MÁ KHÔNG CÒN NHỚ NỔI (trọng tâm cảm xúc 1) ----
amb("night_room", -2.0); bgm("investigative_story", -8.0)
scene("s10_papers_ring", "assets/c10.jpg", "calm", tr="fade_black", trd=0.4)
beat(0.6)
line("l25_ah", "AH", "Khoản này của ai? Còn khoản này?", "cố giữ bình tĩnh")
line("l26_ma", "MA", "Má hông nhớ rõ nữa. Cứ mượn chỗ này đắp chỗ kia, riết rồi hông biết khoản nào còn bao nhiêu.",
     "xấu hổ, nhỏ dần")
beat(2.6)
mark("ring")
line("l27_ah", "AH", "Nhẫn của ba?", "khàn đi, gần như thì thầm", pause=1.2)
line("l28_ah", "AH", "Sao má hông nói với con?", "nghẹn, không trách mà đau")
line("l29_ma", "MA", "Đợt trước con vét hết tiền để dành trả cho má rồi, vợ chồng con còn nuôi thằng Tom nhỏ xíu.",
     "chậm, nước mắt lưng tròng nhưng giọng vẫn rõ")
line("l30_ma", "MA", "Má tưởng ráng xoay thêm một bận là êm, ai dè lãi đẻ ra lãi. Má sợ con biết.",
     "tự trách, nghẹn nhẹ nhưng rõ chữ", pause=1.0)
line("l31_ma", "MA", "Rồi con nói lần đó là lần cuối. Má đâu dám nói nữa.", "bật khóc nhẹ, không gào")
line("l32_ah_echo", "AH_MEM", "Lần này là lần cuối con trả.", "chắc nịch, vang lại như ký ức", pause=0.8)
scene("s11_son_beside", "assets/c11.jpg", "push", tr="dissolve", trd=0.5)
beat(0.4)
line("l33_ah", "AH", "Tại con nói câu đó, phải hông má?", "rất khẽ, vỡ ra, nhận lỗi")
beat(4.4)

# ---- HỒI 4 · TÍNH TOÁN, TƯ VẤN NGẮN GỌN (D) & CAO TRÀO RA ĐI (E) ----
amb("night_room", -3.0); bgm("investigative_story", -4.0)
scene("s12_couple_night", "assets/c12.jpg", "calm", tr="fade_black", trd=0.4)
chapter("HỒI 4 · LỐI THOÁT DUY NHẤT", "NGÀY MÁ RỜI ĐI")
sfx("chapter_sting", -0.1, -6)
beat(0.6)
line("l34_ch", "CH", "Bao nhiêu anh?", "nhẹ, đặt ly nước xuống")
line("l35_ah", "AH", "Bảy khoản lớn nhỏ. Tiền để dành đợt trước mình vét sạch rồi.", "mệt, thật thà")
line("l36_ah", "AH", "Riêng khoản của Hạnh: cầm tám triệu sáu, phải góp mười hai triệu trong bốn chục ngày.", "đọc từng con số",
     sub="Riêng khoản của Hạnh: cầm 8 triệu 6, phải góp 12 triệu trong 40 ngày.")
sfx("typing", 0.0, -6, dur=1.8)
beat(2.0)
line("l37_ah", "AH", "Tính ra hơn ba trăm phần trăm một năm.", "chậm, sững lại trước con số",
     sub="Tính ra hơn 300% một năm.", pause=0.6)
line("l38_ch", "CH", "Vậy mình rà lại từng khoản, rồi vay ngân hàng trả góp dài hạn đi anh.", "tỉnh táo, dứt khoát")
line("l39_ch", "CH", "Tính kéo dài chừng bảy năm, mỗi tháng gói ghém lại vẫn còn đủ nuôi thằng Tom.",
     "nhẹ mà chắc, đã tính kỹ", pause=0.8,
     sub="Tính kéo dài chừng 7 năm, mỗi tháng gói ghém lại vẫn còn đủ nuôi thằng Tom.")
beat(1.4)

# ---- THỜI ĐIỂM D – TƯ VẤN (cắt thật gọn, thực chiến, không giáo điều) ----
amb("office", -4.0); bgm("investigative_story", -5.0)
scene("s13_legal_aid", "assets/c13.jpg", "calm", tr="fade_black", trd=0.35)
beat(0.4)
line("l41_cb", "CB", "Khoản có giấy thì chốt số thực cầm, thu lại giấy gốc. Nhưng mấy mối bên ngoài chưa êm ngay đâu.",
     "điềm tĩnh, gọn, thực tế")
line("l42_cb", "CB", "Tạm thời nên đưa cô đi xa ở với người thân, cắt hết số cũ để họ khỏi tìm gặp ép ký tiếp.",
     "rõ ràng, dứt khoát")
beat(1.2)

# ---- THỜI ĐIỂM E – CAO TRÀO RA ĐI ----
amb("room_tone", -3.0); bgm("warm_outro", -5.5)
scene("s14_hand_over", "assets/c19.jpg", "calm", tr="fade_black", trd=0.45)
beat(0.6)
line("l58_ah", "AH", "Số mới. Con lưu số con, vợ con với dì Ba rồi.", "nhẹ nhàng, kìm nén")
beat(1.4)
line("l59_ah", "AH", "Má đưa con giữ. Trong đó là bằng chứng.", "ngăn lại, ân cần")
beat(1.8)
line("l60_ma", "MA", "Má đi vậy, có phải trốn nợ hông con?", "lo, ngập ngừng")
line("l61_ah", "AH", "Khoản nào đúng thì mình trả đủ. Nhưng má ở lại đây, tụi nó hông để má yên đâu.",
     "trầm, xót nhưng dứt khoát", pause=0.6)
scene("s14b_farewell_baby", "assets/c19b.jpg", "push", tr="dissolve", trd=0.45)
beat(0.8)
line("l61b_ma", "MA", "Má về dưới ít tháng, êm chuyện rồi má lên thăm thằng Tom liền nghen con.",
     "nghẹn nhẹ, khẽ chạm chân cháu đang ngủ, cố mỉm cười", pause=0.6)
line("l61c_ch", "CH", "Dạ, má đi giữ gìn sức khỏe. Ở trên này tụi con lo được.",
     "ấm áp, nén xúc động")
scene("s14c_walk_away", "assets/c19c.jpg", "pull", tr="dissolve", trd=0.5)
sfx("footsteps", 0.3, -7, dur=2.2)
beat(3.8)

# ---- ANH HAI Ở LẠI ĐỐI CHẤT HẠNH & LONG ----
amb("street", -5.0); bgm("tension_drone", -7.0)
scene("s15_hanh_door", "assets/c14.jpg", "calm", tr="fade_black", trd=0.4)
sfx("door_knock", 0.0, -5)
beat(1.4)
line("l45_ah", "AH", "Tôi là con trai chị Tư.", "bình tĩnh", pause=0.8)
line("l46_ah", "AH", "Tôi hông tới đòi tiền. Tôi chỉ hỏi: mỗi người cô dắt vô, Long trả cô bao nhiêu?", "bình thản, nhìn thẳng")
beat(2.4)
line("l47_ha", "HA", "Năm phần trăm.", "nhỏ, không nhìn lên", sub="5%.")
line("l48_ha", "HA", "Em mà ngưng xoay một bữa là sập hết. Em cũng nợ ổng. Nợ cả chục chỗ.",
     "nói nhanh, gấp, mệt rã, không bi lụy")
sfx("phone_vibrate", 0.0, -4, dur=1.4)
beat(1.6)
line("l49_ah", "AH", "Cô ghi giùm tôi một tờ: cô đã nhận bốn triệu ba của má tôi.", "điềm tĩnh, rõ chữ",
     sub="Cô ghi giùm tôi một tờ: cô đã nhận 4 triệu 3 của má tôi.")
beat(2.6)
line("l50_ah", "AH", "Cô đừng dắt thêm ai nữa.", "nhẹ, không trách")
sfx("phone_vibrate", 0.6, -5, dur=2.0)
beat(3.0)

# ---- PHẢN ĐÒN CHỦ NỢ (không nhạc) ----
amb("room_tone", -3.0); bgm("tension_drone", SILENT)
scene("s16_standoff", "assets/c15.jpg", "calm", tr="fade_black", trd=0.4)
beat(0.6)
line("l51_long", "LONG", "Chín triệu mốt. Anh mang đủ chưa?", "lịch sự, lạnh", sub="9 triệu 1. Anh mang đủ chưa?")
line("l52_ah", "AH", "Má tôi cầm về tám triệu sáu, đã góp ba triệu chín. Còn bốn triệu bảy.", "chậm, chắc, từng con số",
     sub="Má tôi cầm về 8 triệu 6, đã góp 3 triệu 9. Còn 4 triệu 7.")
line("l53_ah", "AH", "Tôi tính thêm lãi đúng luật, làm tròn năm triệu.", "bình thản", sub="Tôi tính thêm lãi đúng luật, làm tròn 5 triệu.")
line("l54_long", "LONG", "Anh giỡn hả?", "cười nhạt")
line("l55_ah", "AH", "Anh thấy hông đúng thì mình mang giấy này, với mấy cuộc gọi lên xưởng tôi, ra công an nhờ tính giùm.",
     "không lên giọng, đẩy điện thoại đang ghi âm ra giữa bàn")
mark("climax")
beat(3.0)
line("l56_ah", "AH", "Anh ký nhận đủ. Rồi trả tôi tờ giấy nợ.", "dứt khoát, đẩy tờ biên nhận qua")
beat(1.4)
sfx("footsteps", 0.0, -7, dur=2.0)
scene("s17_settled_paper", "assets/c16.jpg", "still", tr="dissolve", trd=0.35)
beat(3.8)

# ---- BẢY NĂM RÒNG RÃ · CÁI GIÁ PHẢI TRẢ ----
amb("street", -5.0); bgm("investigative_story", -7.0)
scene("s18_pawnshop", "assets/c17.jpg", "calm", tr="fade_black", trd=0.45)
chapter("BẢY NĂM RÒNG RÃ · 84 KỲ TRẢ GÓP", "CÁI GIÁ PHẢI TRẢ")
beat(5.2)

amb("night_room", -3.0); bgm("investigative_story", -8.0)
scene("s19_five_am", "assets/c18.jpg", "calm", tr="fade_black", trd=0.4)
beat(2.4)
line("l57_ch", "CH", "Nợ thì trả dần. Anh mà ngã xuống, mình lấy gì trả.", "nhẹ mà chắc, khoác áo lên vai chồng")
beat(2.8)

scene("s20_ledger_84m", "assets/c22.jpg", "still", tr="dissolve", trd=0.45)
bubble("NGÂN HÀNG GOM NỢ", "Kỳ 84 / 84  (7 NĂM)", side="left", y=250, stamp="HOÀN TẤT", dur=4.8, offset=0.3)
bubble("SỔ CHI TIÊU", "Khoản nợ cuối cùng – ĐÃ TẤT TOÁN", side="left", y=420, stamp="", dur=3.8, offset=1.3)
beat(5.4)

# ---- HỒI 5 · THỜI ĐIỂM F: 7 NĂM SAU – QUAY VỀ NGÀY TẾT BÌNH DỊ ----
amb("room_tone", -2.0); bgm("warm_outro", -4.0)
scene("s21_tet_return", "assets/c20.jpg", "pull", tr="fade_black", trd=0.6)
chapter("HỒI 5 · BẢY NĂM SAU", "NGÀY MÁ QUAY VỀ")
beat(3.2)
line("l62_ch", "CH", "Ăn cơm thôi cả nhà.", "vui vẻ, bình thường")
scene("s22_bare_finger", "assets/c21.jpg", "push", tr="dissolve", trd=0.4)
mark("finger")
beat(3.6)
scene("s23_tom_asks", "assets/c21b.jpg", "push", tr="dissolve", trd=0.4)
beat(0.5)
mark("tom_q")
line("l62b_tom", "TOM", "Bà nội ơi, sao hồi con còn nhỏ, con hông thấy bà vậy?",
     "ngây thơ, trong trẻo, hỏi khẽ thật thà giữa bữa cơm Tết, không nũng nịu", pause=1.2)
scene("s24_tet_silence", "assets/c21c.jpg", "calm", tr="dissolve", trd=0.45)
beat(1.2)
line("l62c_ma", "MA", "Tại hồi đó bà ở xa. Giờ bà về ở luôn với Tom rồi.",
     "dịu dàng, nghẹn nhẹ nhưng cố mỉm cười hiền hậu với cháu, nói gọn tự nhiên")
beat(3.6)

# ---- MÀN HÌNH ĐEN ----
amb("room_tone", -8.0); bgm("warm_outro", -10.0)
scene("s23_black_text", "assets/c23.jpg", "still", tr="fade_black", trd=0.6)
chapter("", "Có những khoản nợ phải mất nhiều năm mới trả hết.", offset=0.6, dur=3.6)
chapter("", "Và có những thứ, một khi đã mất, không thể lấy lại.", offset=4.4, dur=4.2)
beat(9.4)

# ---- THẺ KẾT · NGƯỜI BÓC TRẦN + NHỚ KỸ ----
amb("room_tone", -5.0); bgm("warm_outro", -4.0)
scene("s24_red_flags", EP01B + "scene18.jpg", "still", tr="fade_black", trd=0.4)
mark("rf_start")
sfx("bank_ting", 0.0, -5)
line("l63_narr", "N", "Người dắt bạn vào nợ có khi cũng đang chìm. Và tín dụng đen sống được là nhờ sự im lặng trong mỗi nhà.")
beat(5.0)
mark("rf_end")
scene("s25_disclaimer", EP01B + "scene18.jpg", "still", tr="fade_black", trd=0.3)
mark("disc_start")
beat(5.0)

# ================================================================ COMPILE
t = 0.0
scenes, dialogue, bubbles, foley, chapters = [], [], [], [], []
amb_runs, bgm_runs, marks = [], [], {}


def est(text):
    return len(text.split()) * SEC_PER_WORD + LINE_BASE


for kind, d in E:
    if kind == "scene":
        if scenes:
            scenes[-1]["end"] = round(t, 2)
        sc = {"id": d["id"], "image": d["image"], "start": round(t, 2), "end": None, "motion": d["motion"]}
        if d["tr"]:
            sc["transition_in"] = {"type": d["tr"], "dur": d["trd"]}
        if d["shake"] is not None:
            sc["shakes"] = [{"at": round(t + d["shake"], 2), "dur": 0.4, "amp": 18}]
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
        bubbles.append({"sender": d["sender"], "text": d["text"], "side": d["side"], "y": d["y"],
                        "stamp": d["stamp"], "start": round(s, 2), "end": round(s + d["dur"], 2)})
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


def mmss(x):
    return f"{int(x // 60):02d}:{int(x % 60):02d}"


_desc = [(0.0, "Mở đầu – Cuộc gọi lúc đêm")]
_desc += [(c["start"] - 0.2, f"{c['kicker'].split('·')[0].strip().title()} – {c['title'].capitalize()}")
          for c in chapters if c["kicker"]]
_desc += [(marks["rf_start"], "Nhớ kỹ – Dấu hiệu tín dụng đen & việc nên làm")]
desc_chapters = "\n".join(f"{mmss(s)} {label}" for s, label in sorted(_desc))

episode = {
    "episode_id": "EP27",
    "slug": "SauKhoanNoCuoiCung",
    "title": "Sau khoản nợ cuối cùng",
    "version": "v4-tet2027",
    "scam_family": "MIX – Tín dụng đen góp ngày + chim mồi 'chị em cùng cảnh' (hoa hồng 5%)",
    "duration_sec": total,
    "visual_style_lock": (
        "Horizontal 16:9 widescreen (1920x1080), semi-realistic cinematic 2D anime illustration, "
        "contemporary Southern Vietnam setting, warm-but-moody naturalistic lighting, clean bottom 15% for subtitles, "
        "no text, no letters, no numbers, no logos, no real uniforms"
    ),
    "hook": {
        "kicker": "TẬP ĐẶC BIỆT ĐÊM GIAO THỪA · MÙA VAY NÓNG",
        "title": "SAU KHOẢN NỢ CUỐI CÙNG",
        "start": 0.4,
        "end": 5.0,
    },
    "chapters": chapters,
    "scenes": scenes,
    "dialogue": dialogue,
    "chat_bubbles": bubbles,
    "callouts": [],
    "red_flags": {
        "title": "NHỚ KỸ – 5 DẤU HIỆU TÍN DỤNG ĐEN",
        "start": marks["rf_start"],
        "end": marks["rf_end"],
        "stagger_sec": 0.8,
        "items": [
            "KÝ MƯỜI, CẦM TÁM: Tiền bị trừ trước khi đưa là lãi trá hình",
            "GÓP NGÀY, PHẠT TRỄ: Quy ra lãi năm có thể lên tới hàng trăm phần trăm",
            "\"CHỊ EM CÙNG CẢNH\" RỦ KÝ VAY CHIA ĐÔI: Giấy đứng tên bạn – nợ là của bạn",
            "GỌI LÊN CHỖ LÀM, NHẮN NGƯỜI THÂN: Giữ ghi âm, tin nhắn và trình báo công an",
            "TRẢ NỢ: Có biên nhận, có người làm chứng, lấy lại giấy nợ gốc",
        ],
        "action": "Trước khi ký bất kỳ giấy vay nào, hãy nói với một người thân – và nếu bạn là người thân ấy, hãy nghe trước khi trách.",
    },
    "disclaimer": {
        "header": "LƯU Ý",
        "start": marks["disc_start"],
        "end": total,
        "lines": [
            "Tình huống trong phim được dựng lại nhằm mục đích cảnh báo cộng đồng; nhân vật, tên gọi và số liệu đều là hư cấu.",
            "Thông tin pháp lý trong phim chỉ mang tính tham khảo – hãy hỏi trực tiếp trung tâm trợ giúp pháp lý hoặc luật sư cho trường hợp cụ thể.",
        ],
    },
    "audio": {
        "ambience": amb_runs,
        "foley": foley,
        "bgm": bgm_runs,
        "duck_extra": [
            {"start": marks["ring"] - 0.2, "end": marks["ring"] + 3.0, "bgm_db": -14, "amb_db": -8},
            {"start": marks["climax"] - 0.2, "end": marks["climax"] + 3.0, "bgm_db": -14, "amb_db": -10},
            {"start": marks["tom_q"] - 0.2, "end": marks["tom_q"] + 4.8, "bgm_db": -12, "amb_db": -6},
            {"start": marks["disc_start"], "end": total - 0.05},
        ],
    },
    "forbidden_terms": [],
    "publish": {
        "titles": [
            "Ký Giấy 10 Triệu, Cầm Về 8 Triệu 6 – Chuyến Đi Lánh Nợ Bảy Năm Của Má | Bóc Trần Lừa Đảo",
            "Sau Khoản Nợ Cuối Cùng: \"Bà Nội Ơi, Sao Hồi Con Còn Nhỏ Con Hông Thấy Bà?\" | Bóc Trần Lừa Đảo",
            "Tín Dụng Đen Góp Ngày: Lãi Hơn 300% Một Năm Và Cái Giá Bảy Năm Xa Cháu | Bóc Trần Lừa Đảo",
        ],
        "description": (
            "Tập đặc biệt Đêm Giao Thừa Tết Đinh Mùi (05/02/2027). Sau khi con trai vét sạch tiền để dành trả dứt một đợt nợ, "
            "Cô Tư tưởng chỉ ráng xoay thêm một bận là êm — rồi sập bẫy người \"chị em cùng cảnh\" ký giấy mười triệu, "
            "cầm về tám triệu sáu, chia đôi. Để cắt đứt bủa vây, tờ mờ sáng hôm ấy bà xách túi rời thành phố về quê xa lánh tạm, "
            "hẹn vài tháng sẽ lên thăm đứa cháu nội mới đầy năm. Nhưng phải mất ròng rã bảy năm cày trả nợ và chờ sóng gió "
            "bên ngoài lắng hẳn, bà mới có ngày trở về bên mâm cơm Tết bình dị.\n\n"
            "⏱️ Các hồi trong phim:\n" + desc_chapters
        ),
        "pinned_comment": (
            "📌 Nếu bố mẹ bạn đang giấu một khoản nợ, điều gì sẽ khiến họ dám nói ra? Hãy chia sẻ ở bình luận "
            "(đừng đăng số điện thoại, số tài khoản hay tên người thật). Và nếu thấy video có ích, hãy gửi cho người thân trước Tết nhé."
        ),
        "hashtags": ["#bóctrầnlừađảo", "#cảnhgiáclừađảo", "#vạnchuyện", "#tíndụngđen", "#vaynóng"],
        "tags": [
            "tín dụng đen", "vay nóng cuối năm", "góp ngày", "lãi cắt cổ", "chim mồi vay tiền",
            "bóc trần lừa đảo", "cảnh giác lừa đảo", "vạn chuyện",
        ],
        "category": "Education (Giáo dục)",
        "playlist": "Hồ Sơ Bóc Trần Lừa Đảo – Phim Dài Chuyên Sâu",
        "thumbnail_sec": round(marks["ring"] + 0.6, 2),
    },
}

OUT.write_text(json.dumps(episode, ensure_ascii=False, indent=2), encoding="utf-8")
words = sum(len(l["text"].split()) for l in dialogue)
narr = sum(len(l["text"].split()) for l in dialogue if l["speaker"] == "nguoi_boc_tran")
maxw = max(len(l["text"].split()) for l in dialogue)
print(f"episode.json: {total:.1f}s ({mmss(total)}) · {len(scenes)} cảnh · {len(dialogue)} câu · {words} từ "
      f"({words / (total / 60):.0f} từ/phút) · câu dài nhất {maxw} từ · Người Bóc Trần {narr / words:.0%} lời thoại · "
      f"{'TTS thật' if real else 'ước tính'} ({len(real)} câu thật)")
print(desc_chapters)
