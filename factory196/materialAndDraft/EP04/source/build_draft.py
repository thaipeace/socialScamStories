# -*- coding: utf-8 -*-
"""
Trình biên dịch `factory196/materialAndDraft/EP04/episode.json` – Tập EP04:
"300 triệu gom vé hộ & Bí mật của Chị Hai" (16:9 Long-form).

Tự động đọc độ dài WAV thật trong `audio/tts/` (nếu đã chạy Gate 2) để căn khớp
100% thời lượng từng câu và từng cảnh (không dùng atempo/asetrate).
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
SCENE_LEAD = 0.35
WINDOW_MARGIN = 1.6


def wav_dur(lid: str) -> float | None:
    p = TTS / f"{lid}.wav"
    if not p.is_file():
        return None
    with wave.open(str(p), "rb") as wf:
        return round(wf.getnframes() / wf.getframerate(), 3)


real = {p.stem: wav_dur(p.stem) for p in TTS.glob("*.wav")} if TTS.is_dir() else {}
real = {k: v for k, v in real.items() if v}

SPK = {
    "NA": dict(
        speaker="be_na",
        voice="Leda",
        label_short="NA",
        speaker_label="Na – trưởng nhóm fan 23 tuổi",
        base=(
            "Giọng cô gái trẻ miền Nam Sài Gòn 23 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
            "giữ cố định một âm sắc trong trẻo tự nhiên đời thực, rõ chữ, tuyệt đối không gào khóc cải lương"
        ),
    ),
    "CH": dict(
        speaker="chi_ba",
        voice="Kore",
        label_short="CHỊ HAI",
        speaker_label="Chị Hai – chị ruột của Na, 35 tuổi",
        base=(
            "Giọng phụ nữ miền Nam Sài Gòn 35 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
            "giữ cố định một âm sắc sắc sảo, điềm tĩnh, dứt khoát và lạnh lùng"
        ),
    ),
    "TR": dict(
        speaker="ke_ngot_ngao_nu",
        voice="Aoede",
        label_short="TRANG",
        speaker_label="Trang – giả danh quản lý Kênh Hậu Trường",
        base=(
            "Giọng nữ miền Nam Sài Gòn 30 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
            "giữ cố định một âm sắc êm mượt, lịch thiệp, thân tình kiểu dân sự kiện chuyên nghiệp"
        ),
    ),
    "TR_P": dict(
        speaker="ke_ngot_ngao_nu",
        voice="Aoede",
        af="phone",
        label_short="TRANG",
        speaker_label="Trang – giả danh quản lý Kênh Hậu Trường (qua điện thoại)",
        base=(
            "Giọng nữ miền Nam Sài Gòn 30 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
            "êm mượt, chuyên nghiệp, dẫn dụ khéo léo qua điện thoại"
        ),
    ),
    "FNU": dict(
        speaker="chi_tu",
        voice="Zephyr",
        af="phone",
        label_short="FAN NỮ",
        speaker_label="Thành viên nữ trong nhóm fan",
        base=(
            "Giọng cô gái trẻ miền Nam Sài Gòn 21 tuổi, phát âm chuẩn phương ngữ miền Nam, "
            "tự nhiên đời thực, nói qua tin nhắn thoại"
        ),
    ),
    "FNAM": dict(
        speaker="thang_tun",
        voice="Puck",
        label_short="FAN NAM",
        speaker_label="Thành viên nam trong nhóm fan",
        base=(
            "Giọng nam thanh niên miền Nam Sài Gòn 22 tuổi, phát âm chuẩn phương ngữ miền Nam, "
            "tông sáng, nhịp nhanh, rõ chữ"
        ),
    ),
    "FNAM_P": dict(
        speaker="thang_tun",
        voice="Puck",
        af="phone",
        label_short="FAN NAM",
        speaker_label="Thành viên nam trong nhóm fan (qua tin nhắn thoại)",
        base=(
            "Giọng nam thanh niên miền Nam Sài Gòn 22 tuổi, phát âm chuẩn phương ngữ miền Nam, "
            "tông sáng, nhịp nhanh, rõ chữ"
        ),
    ),
    "KENH": dict(
        speaker="anh_hai",
        voice="Orus",
        af="phone",
        label_short="KÊNH HẬU TRƯỜNG",
        speaker_label="Đại diện Kênh Hậu Trường thật",
        base=(
            "Giọng nam miền Nam Sài Gòn 35 tuổi, phát âm chuẩn phương ngữ miền Nam, "
            "trầm tĩnh, rõ chữ, dứt khoát và nghiêm túc qua điện thoại"
        ),
    ),
    "SEC": dict(
        speaker="ke_gia_danh",
        voice="Fenrir",
        af="phone",
        label_short="ĐẦU DÂY BÍ ẨN",
        speaker_label="Giọng nam bí ẩn gọi cho Chị Hai",
        base=(
            "Giọng nam miền Nam Sài Gòn 40 tuổi, phát âm chuẩn phương ngữ miền Nam, "
            "trầm thấp, kín kẽ, bí ẩn qua điện thoại"
        ),
    ),
    "N": dict(speaker="nguoi_boc_tran"),
}


def mo(kind: str) -> dict:
    return {
        "tense": {"scale": [1.04, 1.14], "focus": [[0.5, 0.5], [0.48, 0.45]], "wobble": "tense"},
        "calm": {"scale": [1.02, 1.09], "focus": [[0.5, 0.5], [0.5, 0.47]], "wobble": "calm"},
        "hand": {"scale": [1.02, 1.10], "focus": [[0.46, 0.48], [0.54, 0.46]], "wobble": "handheld"},
        "push": {"scale": [1.0, 1.16], "focus": [[0.5, 0.5], [0.5, 0.45]], "wobble": "tense"},
        "pull": {"scale": [1.12, 1.02], "focus": [[0.5, 0.46], [0.5, 0.5]], "wobble": "calm"},
        "still": {"scale": [1.0, 1.05], "focus": [[0.5, 0.5], [0.5, 0.5]], "wobble": "none"},
    }[kind]


E = []


def scene(sid, image, motion="calm", tr=None, trd=0.35, shake=None):
    E.append(("scene", dict(id=sid, image=image, motion=mo(motion), tr=tr, trd=trd, shake=shake)))


def line(lid, spk, text, emo="", sub=None, pause=0.0):
    E.append(("line", dict(id=lid, spk=spk, text=text, emo=emo, sub=sub, pause=pause)))


def beat(sec):
    E.append(("beat", sec))


def chapter(kicker, title):
    E.append(("chapter", dict(kicker=kicker, title=title)))


def bubble(sender, text, side="left", y=340, stamp="", dur=5.0, offset=0.0):
    E.append(("bubble", dict(sender=sender, text=text, side=side, y=y, stamp=stamp, dur=dur, offset=offset)))


def callout(text, style="warning", y=130, dur=5.0, offset=0.0):
    E.append(("callout", dict(text=text, style=style, y=y, dur=dur, offset=offset)))


def sfx(preset, offset=0.0, gain=-4, dur=None):
    E.append(("sfx", dict(preset=preset, offset=offset, gain=gain, dur=dur)))


def amb(preset, gain=-2.0):
    E.append(("amb", dict(preset=preset, gain=gain)))


def bgm(preset, gain=-1.5):
    E.append(("bgm", dict(preset=preset, gain=gain)))


def mark(name):
    E.append(("mark", name))


EP01B = "factory196/materialAndDraft/EP01b/assets/"

# ================================================================ STORY
# ---- CẢNH 1: HOOK – CƠN CUỒNG NHIỆT ĐU IDOL & LỜI THÚ NHẬN 300 TRIỆU (00:00 – 00:30) ----
amb("crowd", 0.5); bgm("action_climax", -0.5)
scene("s00_idol_frenzy", "assets/c00.jpg", "tense", shake=0.2)
sfx("impact", 0.05, -2)
beat(0.15)
line("l00_fannam", "FNAM", "Đêm chung kết tháng Sáu có nhịn ăn nhịn mặc tụi em cũng phải săn bằng được vé! Sống chết gì cũng phải đu theo thần tượng tới cùng nha chị Na!",
     "gào thét khản giọng vì phấn khích giữa biển người cuồng nhiệt")

amb("night_room", -1.5); bgm("suspense_pulse", -1.0)
scene("s01_hook_panic", "assets/c01.jpg", "tense", tr="flash_white", trd=0.25, shake=0.2)
sfx("impact", 0.0, -2)
sfx("phone_vibrate", 0.15, -3, dur=1.8)
sfx("notification", 0.25, -4)
bubble("NHÓM FAN ÁNH SAO", "Thứ Bảy diễn rồi! Vé đâu hay chị định ôm tiền của tụi em trốn hả?!",
       side="left", y=260, stamp="ĐÒI VÉ", dur=5.8, offset=0.2)
beat(0.2)
line("l01_fannu", "FNU", "Tụi em chuyển tiền vé thẳng vô tài khoản tên chị! Thứ Bảy diễn rồi, vé đâu hay chị định ôm tiền của tụi em trốn hả?!",
     "gay gắt, bức xúc đòi vé")
line("l02_na", "NA", "Em thề em không ăn lời một đồng nào! Toàn bộ ba trăm triệu của một trăm rưỡi vé em đã chuyển hết cho chị Trang bên Kênh Hậu Trường rồi mà!",
     "hoảng loạn, thật thà thú nhận",
     sub="Em thề không ăn lời 1 đồng nào! Toàn bộ 300 triệu của 150 vé em đã chuyển hết cho chị Trang rồi mà!")
sfx("impact", 0.0, -3)
scene("s02_hook_freeze", "assets/c02.jpg", "push", tr="flash_white", trd=0.25)
bubble("FAN TRONG NHÓM", "Cái gì?! 300.000.000 VND mà chuyển không giấy tờ?! Chị phải đền cho tụi này!",
       side="right", y=300, stamp="PHẪN NỘ", dur=5.5, offset=0.1)
line("l03_fannam", "FNAM_P", "Cái gì?! Ba trăm triệu tiền mặt mà chị chuyển không giấy tờ cho người ta?! Giờ mất trắng thì chị phải đền!",
     "sốc, giận dữ quát lên",
     sub="Cái gì?! 300 triệu tiền mặt mà chị chuyển không giấy tờ?! Giờ mất trắng thì chị phải đền!")
mark("freeze")
line("l04_narr", "N", "Từ cơn cuồng nhiệt sống chết vì thần tượng đến vực thẳm chỉ cách nhau một cú bấm chuyển khoản ba trăm triệu.",
     sub="Từ cơn cuồng nhiệt sống chết vì thần tượng đến vực thẳm chỉ cách nhau một cú bấm chuyển khoản 300 triệu.")
sfx("riser", -1.2, -4, dur=1.2)
beat(0.5)

# ---- HỒI 1: 6 THÁNG NUÔI MỒI & CƠN SAY "QUYỀN LỰC TRƯỞNG NHÓM" ----
amb("crowd", -3.0); bgm("investigative_story", -1.5)
scene("s03_booth_heat", "assets/c03.jpg", "calm", tr="fade_black", trd=0.4)
chapter("HỒI 1 · SÁU THÁNG TRƯỚC", "MÓN QUÀ MIỄN PHÍ NGOÀI ĐỜI & CÁI BẪY “VÉ NỘI BỘ”")
sfx("chapter_sting", -0.1, -4)
beat(0.3)
line("l05_fannam", "FNAM", "Chị Na ơi, nắng gắt quá mà loa kéo hư, quạt cầm tay cũng hết sạch pin rồi!",
     "mệt mỏi, than thở giữa trời nắng")

scene("s04_trang_arrival", "assets/c04.jpg", "calm", tr="dissolve", trd=0.35)
line("l06_trang", "TR", "Chị Trang bên Kênh Hậu Trường nè Na. Đợt trước tặng áo, nay chị mang loa với quạt qua tiếp sức tụi em.",
     "thân thiện, hiền hậu, nhiệt tình")
line("l07_na", "NA", "Trời ơi chị Trang chu đáo quá! Mấy đợt liền chị toàn bỏ tiền túi phụ tụi em không công, ngại ghê luôn.",
     "cảm kích, tin tưởng tuyệt đối")
line("l08_trang", "TR", "Chỗ chị em quý nghệ sĩ cả mà, tính toán chi mấy chuyện nhỏ. Nhóm cần gì cứ nhắn chị.",
     "xởi lởi, tạo lòng tin", pause=0.4)

# Nhịp 2: Đêm cháy vé & Hào quang "Người hùng của cả nhóm"
amb("room_tone", -2.0)
scene("s05_sold_out_bait", "assets/c05.jpg", "hand", tr="fade_black", trd=0.35)
sfx("notification", 0.1, -4)
bubble("NHÓM FAN ÁNH SAO", "Mới mở bán 5 phút đã HẾT SẠCH VÉ rồi chị Na ơi! Cứu tụi em với!",
       side="left", y=260, stamp="CHÁY VÉ", dur=5.2, offset=0.1)
line("l09_fannu", "FNU", "Mới mở bán năm phút đã cháy sạch vé rồi chị Na ơi! Cứu tụi em với!",
     "tiếc nuối, cầu cứu")
sfx("phone_ring", 0.0, -4, dur=1.2)
beat(0.6)
line("l10_trang", "TR_P", "Na ơi, bên chị là đối tác truyền thông đêm nhạc nên có suất vé nội bộ giá gốc hai triệu.",
     "hào hứng, rỉ tai cơ hội hiếm",
     sub="Na ơi, bên chị là đối tác truyền thông đêm nhạc nên có suất vé nội bộ giá gốc 2 triệu.")
line("l11_trang", "TR_P", "Bên chị không xuất lẻ từng người. Em đứng ra gom tiền của nhóm về một mối rồi chuyển qua tài khoản chị giữ suất đoàn nha.",
     "dẫn dụ mượt mà", pause=0.4)

# ---- HỒI 2: 300 TRIỆU BẤM CHUYỂN & ÁNH MẮT LẠNH CỦA CHỊ HAI ----
amb("room_tone", -2.0); bgm("suspense_pulse", -1.5)
scene("s06_euphoria_collecting", "assets/c06.jpg", "calm", tr="fade_black", trd=0.4)
chapter("HỒI 2 · MƯỜI NGÀY TRƯỚC ĐÊM DIỄN", "HÀO QUANG TRƯỞNG NHÓM & ÁNH MẮT LẠNH CỦA CHỊ HAI")
sfx("chapter_sting", -0.1, -4)
sfx("bank_ting", 0.3, -4)
bubble("NGÂN HÀNG X", "+4.000.000 VND · +6.000.000 VND (150 vé gom về TK của Na)",
       side="left", y=340, stamp="TIỀN VỀ DỒN DẬP", dur=6.5, offset=4.6)
beat(0.3)
line("l12_fannu", "FNU", "Em vừa chuyển bốn triệu hai vé vô tài khoản chị Na nha! Chỉ có chị Na mới xin được suất nội bộ của đối tác lớn thôi!",
     "hào hứng, tâng bốc",
     sub="Em vừa chuyển 4 triệu 2 vé vô tài khoản chị Na nha! Chỉ có chị Na mới xin được suất nội bộ thôi!")
line("l13_fannam", "FNAM_P", "Em cũng chuyển sáu triệu ba vé rồi đó! Chị Na đúng là cứu tinh của cả nhóm!",
     "phấn khích, tung hô",
     sub="Em cũng chuyển 6 triệu 3 vé rồi đó! Chị Na đúng là cứu tinh của cả nhóm!")
line("l14_na", "NA", "Mọi người cứ yên tâm! Đúng giá gốc hai triệu một vé, tuần sau đối tác xuất mã đoàn là chị phát liền!",
     "say sưa trong hào quang, tự hào, hưng phấn",
     sub="Mọi người cứ yên tâm! Đúng giá gốc 2 triệu 1 vé, tuần sau đối tác xuất mã đoàn là chị phát liền!")

scene("s07_transfer_300m", "assets/c07.jpg", "push", tr="dissolve", trd=0.3)
sfx("notification", 0.1, -4)
bubble("CHỊ TRANG", "Chốt đủ 300.000.000 VND trong tối nay kẻo ban tổ chức thu hồi suất vé đoàn nha Na.",
       side="left", y=240, stamp="HỐI CHỐT TIỀN", dur=4.8, offset=0.1)
beat(1.2)
sfx("bank_ting", 0.1, -3)
bubble("NGÂN HÀNG X", "TK …4512 (NGUYỄN THỊ TRANG): -300.000.000 VND (Chuyển khoản thành công)",
       side="right", y=420, stamp="ĐÃ CHUYỂN 300TR", dur=4.5, offset=0.1)
beat(2.8)

scene("s08_chihai_secret_photo", "assets/c08.jpg", "push", tr="dissolve", trd=0.35)
sfx("notification", 0.4, -5)
callout("CHỊ HAI LẶNG LẼ QUAN SÁT  ·  ÂM THẦM CHỤP LẠI THÔNG TIN TÀI KHOẢN", "warning", y=130, dur=6.5, offset=0.2)
beat(0.8)
line("l15_chihai", "CH", "Suất vé của đối tác truyền thông lớn… mà lại thu ba trăm triệu qua tài khoản cá nhân?",
     "trầm thấp, đanh mặt lại, sắc lạnh",
     sub="Suất vé của đối tác truyền thông lớn… mà lại thu 300 triệu qua tài khoản cá nhân?", pause=0.6)

# ---- HỒI 3: CAO TRÀO – RƠI XUỐNG VỰC THẲM & CÔ ĐƠN CÙNG CỰC ----
amb("night_room", -1.5); bgm("tension_drone", -0.8)
scene("s09_blocked_shock", "assets/c09.jpg", "tense", tr="fade_black", trd=0.4, shake=0.3)
chapter("HỒI 3 · BA NGÀY TRƯỚC ĐÊM DIỄN", "CUỘC GỌI RƠI XUỐNG VỰC THẲM & SỰ CÔ ĐƠN CÙNG CỰC")
sfx("chapter_sting", -0.1, -4)
sfx("call_end", 0.2, -3)
beat(0.4)
line("l16_na", "NA", "Thứ Tư rồi… Sao số chị Trang thuê bao, tin nhắn cũng chặn em luôn vậy nè?!",
     "hơi thở gấp gáp, tay run bần bật", pause=0.4)

bgm("action_climax", -0.5)
scene("s10_call_channel_abyss", "assets/c10.jpg", "push", tr="flash_red", trd=0.3, shake=0.2)
sfx("heartbeat", 0.0, -4, dur=12.0)
sfx("phone_ring", 0.1, -4, dur=1.2)
beat(0.6)
line("l17_na", "NA", "Dạ… anh ơi cho em gặp chị Trang quản lý đối tác… Chị Trang nhận ba trăm triệu tiền vé nội bộ của nhóm em mà giờ khóa máy rồi anh ơi…",
     "lắp bắp, lạc giọng vì sợ hãi, cầu cứu",
     sub="Dạ… cho em gặp chị Trang… Chị Trang nhận 300 triệu tiền vé nội bộ của nhóm em mà giờ khóa máy rồi anh ơi…")
line("l18_kenh", "KENH", "Em nghe rõ này. Bên anh không có nhân sự nào tên Trang, và Kênh Hậu Trường tuyệt đối không bán vé nội bộ.",
     "điềm tĩnh nhưng đanh thép như búa giáng")
sfx("impact", 0.0, -3)
mark("climax")
callout("KÊNH HẬU TRƯỜNG: KHÔNG CÓ NHÂN SỰ TÊN TRANG · KHÔNG BÁN VÉ NỘI BỘ", "danger", y=130, dur=8.0, offset=0.1)
line("l19_na", "NA", "Không… không thể nào đâu anh! Bả đeo thẻ kênh mình, mang loa quạt ra nhà thi đấu phụ tụi em suốt sáu tháng nay mà!",
     "bật khóc nấc, hoảng loạn sững sờ",
     sub="Không… không thể nào đâu anh! Bả đeo thẻ kênh mình, mang loa quạt phụ tụi em suốt 6 tháng nay mà!")
line("l19b_na", "NA", "Anh kiểm tra lại giùm em đi, ba trăm triệu của một trăm rưỡi bạn trong nhóm em đó anh ơi…",
     "nghẹn ngào níu kéo trong tuyệt vọng",
     sub="Anh kiểm tra lại giùm em đi, 300 triệu của 150 bạn trong nhóm em đó anh ơi…")
line("l20_kenh", "KENH", "Bên anh vừa đăng cảnh báo bị mạo danh rồi. Kênh không nhận tiền nên công an không lập hồ sơ theo đơn của kênh được.",
     "dứt khoát, thực tế")
line("l20b_kenh", "KENH", "Chính em là người chuyển ba trăm triệu cho bả, nên em phải tự đi trình báo ngay đi.",
     "nghiêm túc, dứt khoát",
     sub="Chính em là người chuyển 300 triệu cho bả, nên em phải tự đi trình báo ngay đi.")
sfx("call_end", 0.1, -3)
beat(0.8)

# Nhịp 4: Bị đám đông quay lưng & Cô đơn cùng cực
scene("s11_begging_group_backlash", "assets/c11.jpg", "hand", tr="dissolve", trd=0.3)
sfx("phone_vibrate", 0.1, -3, dur=2.0)
line("l21_na", "NA", "Mọi người ơi… chị Trang lừa em rồi… Em thề em không giữ của mọi người một đồng nào hết, cho em thêm thời gian tìm bả nha mọi người…",
     "quỳ dưới sàn, nghẹn ngào van xin trong tuyệt vọng")
bubble("FAN TRONG NHÓM", "Đừng diễn nước mắt cá sấu! Chuyển 300 triệu không giấy tờ, chắc chắn chị ăn chia với bả!",
       side="left", y=260, stamp="QUAY LƯNG", dur=6.5, offset=0.1)
line("l22_fannu", "FNU", "Đừng có diễn nước mắt cá sấu! Làm gì có ai ngu tới mức chuyển ba trăm triệu không giấy tờ! Chắc chắn chị ăn chia với bả!",
     "lạnh lùng, cay nghiệt, tàn nhẫn",
     sub="Đừng có diễn nước mắt cá sấu! Làm gì có ai chuyển 300 triệu không giấy tờ! Chắc chắn chị ăn chia với bả!")

scene("s12_utter_isolation", "assets/c12.jpg", "pull", tr="dissolve", trd=0.35)
sfx("notification", 0.2, -4)
bubble("NHÓM FAN ÁNH SAO", "Sáng mai không ói đủ tiền ra, tụi này kéo tới tận nhà, cho chị khỏi nhìn mặt ai luôn!",
       side="right", y=300, stamp="DỌA KÉO TỚI NHÀ", dur=6.5, offset=0.2)
line("l23_fannam", "FNAM_P", "Tụi này chỉ biết tiền chuyển vô tài khoản tên chị! Sáng mai không ói đủ tiền ra, tụi này kéo tới tận nhà, cho chị khỏi nhìn mặt ai luôn!",
     "đanh giọng đe dọa", pause=1.2)

# ---- HỒI 4: SỰ CAO TAY CỦA CHỊ HAI & THUYẾT ÂM MƯU Ở CỔNG ĐỒN ----
amb("room_tone", -2.5); bgm("tension_drone", -1.2)
scene("s13_chihai_dossier", "assets/c13.jpg", "push", tr="fade_black", trd=0.4)
chapter("HỒI 4 · XẤP HỒ SƠ MẬT", "SỰ CAO TAY CỦA CHỊ HAI & CUỘC GỌI SAU LƯNG")
sfx("chapter_sting", -0.1, -4)
beat(0.4)
line("l24_chihai", "CH", "Lau mặt đi. Sáng mai cầm xấp hồ sơ này lên công an.",
     "bình thản, kiệm lời, lạnh lùng", pause=0.3)
line("l25_na", "NA", "Ủa chị Hai… sao chị có ảnh chụp màn hình lúc em chuyển khoản từ tuần trước vậy?",
     "ngước lên sững sờ, ngơ ngác", pause=0.5)
callout("TÀI KHOẢN ĐÃ ĐƯỢC CHỊ HAI ÂM THẦM GỬI ĐIỀU TRA TỪ MỘT TUẦN TRƯỚC", "warning", y=130, dur=6.5, offset=0.1)
line("l26_chihai", "CH", "Tài khoản đó chị đã gửi người bên điều tra từ đêm hôm ấy rồi. Cứ trình báo đúng như trong này… đừng hỏi thêm.",
     "trầm thấp, bí ẩn, sắc lạnh, dứt khoát", pause=0.6)

# ---- NHỚ KỸ TRONG 7 GIÂY (CÔ ĐỌNG, KHÔNG DẠY ĐỜI) ----
amb("room_tone", -4.0); bgm("warm_outro", -2.0)
scene("s17_red_flags", EP01B + "scene18.jpg", "still", tr="fade_black", trd=0.3)
mark("rf_start")
sfx("notification", 0.1, -4)
beat(0.2)
line("l27_narr", "N", "Hào quang đám đông và lòng tin người quen ngoài đời — đó là cái bẫy biến người gom hộ thành kẻ đứng mũi chịu sào.",
     pause=0.3)
mark("rf_end")

# ---- KẾT MỞ: CUỘC GỌI BÍ ẨN CỦA CHỊ HAI ("CỨ ĐỂ ĐÓ!") ----
amb("street", -3.0); bgm("tension_drone", -1.0)
scene("s14_leaving_station", "assets/c14.jpg", "calm", tr="fade_black", trd=0.4)
beat(0.3)
line("l28_na", "NA", "May mà chị Hai âm thầm báo trước một tuần nên bên điều tra đã kịp khoanh vùng dòng tiền… Không có chị Hai chắc em chết mất.",
     "thở phào nhẹ nhõm, biết ơn", pause=0.5)

scene("s15_chihai_conspiracy_call", "assets/c15.jpg", "push", tr="dissolve", trd=0.35)
sfx("phone_vibrate", 0.1, -3, dur=1.2)
beat(0.8)
callout("CUỘC GỌI MẬT VÀO MÁY PHỤ CỦA CHỊ HAI", "danger", y=120, dur=6.2, offset=0.1)
line("l29_secret", "SEC", "Con bé nộp đơn đúng như kịch bản rồi hả? Còn khoản ba trăm triệu bên nhánh con Trang, giờ tính sao?",
     "trầm thấp, bí ẩn qua điện thoại",
     sub="Con bé nộp đơn đúng như kịch bản rồi hả? Còn khoản 300 triệu bên nhánh con Trang, giờ tính sao?",
     pause=0.4)
sfx("heartbeat", 0.0, -4, dur=2.5)
line("l30_chihai", "CH", "Cứ để đó!", "lạnh băng, sắc lẹm, dứt khoát", pause=0.2)

sfx("impact", 0.0, -2)
scene("s16_black_cut", "assets/c16.jpg", "still", tr="fade_black", trd=0.1)
callout("CHỊ HAI ĐANG GIĂNG LƯỚI BẮT KẺ GIAN… HAY CÒN MỘT KỊCH BẢN NÀO KHÁC?", "danger", y=440, dur=3.2, offset=0.2)
beat(3.5)

# ---- DISCLAIMER ----
amb("room_tone", -5.0); bgm("warm_outro", -3.0)
scene("s18_disclaimer", EP01B + "scene18.jpg", "still", tr="fade_black", trd=0.35)
mark("disc_start")
beat(4.5)
mark("end")

# ================================================================ COMPILE
t = 0.0
scenes, dialogue, bubbles, callouts, foley, chapters = [], [], [], [], [], []
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
            ln["style"] = p["base"] + (", " + d["emo"] if d["emo"] else "") + "."
        ln["start"] = round(t, 2)
        ln["window"] = round(max(dur, est(d["text"])) + WINDOW_MARGIN, 2)
        ln["text"] = d["text"]
        if d["sub"]:
            ln["subtitle"] = [d["sub"]]
        dialogue.append(ln)
        t += dur
        t += GAP + d["pause"]
    elif kind == "beat":
        t += d
    elif kind == "chapter":
        start = scenes[-1]["start"]
        chapters.append({"kicker": d["kicker"], "title": d["title"], "start": round(start + 0.2, 2),
                         "end": round(start + 4.8, 2)})
    elif kind == "bubble":
        s = t + d["offset"]
        bubbles.append({"sender": d["sender"], "text": d["text"], "side": d["side"], "y": d["y"],
                        "stamp": d["stamp"], "start": round(s, 2), "end": round(s + d["dur"], 2)})
    elif kind == "callout":
        s = t + d["offset"]
        callouts.append({"text": d["text"], "style": d["style"], "y": d["y"],
                         "start": round(s, 2), "end": round(s + d["dur"], 2)})
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


_desc = [(0.0, "Mở đầu – Lời thú nhận 300 triệu & cơn giận của cả nhóm")]
_desc += [(c["start"], f"{c['kicker'].split('·')[0].strip().title()} – {c['title'].capitalize()}") for c in chapters]
_desc += [(marks["rf_start"], "Dấu hiệu nhận biết & cuộc gọi bí ẩn của Chị Hai")]
desc_chapters = "\n".join(f"{mmss(s)} {label}" for s, label in sorted(_desc))

episode = {
    "episode_id": "EP04",
    "slug": "BayVeNoiBo300Trieu",
    "title": "300 triệu gom vé hộ & Bí mật của Chị Hai",
    "version": "v2",
    "scam_family": "MIX-06",
    "duration_sec": total,
    "visual_style_lock": (
        "Horizontal 16:9 widescreen (1920x1080), semi-realistic cinematic 2D anime illustration, "
        "contemporary Southern Vietnam urban setting, moody dramatic lighting, clean bottom 15% for subtitles, "
        "no text, no letters, no numbers, no logos, no real uniforms"
    ),
    "hook": {
        "kicker": "CƠN SỐT SĂN VÉ ĐU THẦN TƯỢNG · ĐÊM CHUNG KẾT",
        "title": "SỐNG CHẾT GÀO THÉT VÌ THẦN TƯỢNG – CÚ RƠI 300 TRIỆU CỦA CÔ TRƯỞNG NHÓM",
        "start": 0.4,
        "end": 5.6,
    },
    "chapters": chapters,
    "scenes": scenes,
    "dialogue": dialogue,
    "chat_bubbles": bubbles,
    "callouts": callouts,
    "red_flags": {
        "title": "NHỚ KỸ – 3 DẤU HIỆU BẪY GOM VÉ NỘI BỘ",
        "start": marks["rf_start"],
        "end": marks["rf_end"],
        "stagger_sec": 0.8,
        "items": [
            "NUÔI LÒNG TIN NGOÀI ĐỜI: Tặng quà, hỗ trợ loa quạt nhiều tháng dưới mác \"người của kênh truyền thông\"",
            "MỒI VÉ ĐOÀN GIÁ GỐC: Đẩy trưởng nhóm đứng ra gom một cục hàng trăm triệu chuyển vào tài khoản cá nhân",
            "ĐỨNG MŨI CHỊU SÀO: Kênh thật không nhận tiền nên không thể đứng đơn; người gom hộ phải tự gánh cả hai đầu",
        ],
        "action": "Chỉ mua trên kênh chính thức · Tuyệt đối không dùng tài khoản cá nhân gom tiền hộ nguồn vé truyền miệng!",
    },
    "disclaimer": {
        "header": "LƯU Ý",
        "start": marks["disc_start"],
        "end": total,
        "lines": [
            "Tình huống trong phim được dựng lại nhằm mục đích cảnh báo cộng đồng; nhân vật, đêm nhạc, trang cộng đồng và số liệu đều là hư cấu.",
            "Chỉ giao dịch vé qua kênh phân phối chính thức của ban tổ chức; không chuyển khoản lớn cho nguồn vé truyền miệng.",
        ],
    },
    "audio": {
        "ambience": amb_runs,
        "foley": foley,
        "bgm": bgm_runs,
        "duck_extra": [
            {"start": marks["climax"] - 0.2, "end": marks["climax"] + 1.5, "bgm_db": -14, "amb_db": -10},
            {"start": marks["disc_start"], "end": total - 0.05},
        ],
    },
    "forbidden_terms": [],
    "publish": {
        "titles": [
            "300 Triệu Gom Vé Hộ & Cuộc Gọi Bí Ẩn Sau Lưng Của Chị Hai | Bóc Trần Lừa Đảo",
            "Bẫy \"Vé Nội Bộ\": Nuôi Lòng Tin 6 Tháng Để Biến Trưởng Nhóm Fan Thành Kẻ Đứng Mũi Chịu Sào | Bóc Trần Lừa Đảo",
            "Thú Nhận Đã Chuyển 300 Triệu Cho Người Quen – Cú Rơi Xuống Vực Thẳm Trước Giờ Diễn | Bóc Trần Lừa Đảo",
        ],
        "description": (
            "Na, 23 tuổi – trưởng một nhóm cộng đồng người hâm mộ – không ăn chênh lệch một đồng khi đứng ra "
            "gom giúp 150 vé đêm nhạc qua lời giới thiệu \"suất vé nội bộ đối tác truyền thông\" của người chị quen biết "
            "từng mang loa, quạt hỗ trợ nhóm suốt nửa năm. Trong cơn say hào quang trưởng nhóm, Na bấm chuyển 300 triệu "
            "mà không biết Chị Hai đã đứng sau cánh cửa lặng lẽ quan sát tất cả. Khi nguồn vé khóa máy và kênh truyền thông "
            "thật lên tiếng báo bị mạo danh, Na rơi xuống vực thẳm cô đơn — trước khi phát hiện bộ hồ sơ mật của Chị Hai "
            "và cuộc gọi lạnh gáy ở cổng cơ quan chức năng.\n\n"
            "⏱️ Các hồi trong phim:\n" + desc_chapters
        ),
        "pinned_comment": (
            "📌 Theo bạn, câu \"Cứ để đó!\" ở giây cuối cùng của Chị Hai là đang phối hợp ngầm để giăng lưới bắt trọn đường dây của Trang, "
            "hay còn một kịch bản nào khác đằng sau khoản 300 triệu? Và nhớ kỹ: tuyệt đối đừng bao giờ dùng tài khoản cá nhân đứng ra gom tiền hộ "
            "cho nguồn vé truyền miệng nhé!"
        ),
        "hashtags": [
            "#bóctrầnlừađảo",
            "#cảnhgiáclừađảo",
            "#vạnchuyện",
            "#lừađảovéconcert",
            "#vénộibộ",
        ],
        "tags": [
            "lừa đảo vé đêm nhạc",
            "bẫy vé nội bộ",
            "gom đơn hộ",
            "mạo danh đối tác truyền thông",
            "bóc trần lừa đảo",
            "cảnh giác lừa đảo",
            "vạn chuyện",
        ],
        "category": "Education (Giáo dục)",
        "playlist": "Hồ Sơ Bóc Trần Lừa Đảo – Phim Dài Chuyên Sâu",
        "thumbnail_sec": round(marks["climax"] + 0.5, 2),
    },
}

OUT.write_text(json.dumps(episode, ensure_ascii=False, indent=2), encoding="utf-8")
words = sum(len(l["text"].split()) for l in dialogue)
narr = sum(len(l["text"].split()) for l in dialogue if l["speaker"] == "nguoi_boc_tran")
print(f"episode.json: {total:.1f}s · {len(scenes)} cảnh · {len(dialogue)} câu · {words} từ "
      f"({words / (total / 60):.0f} từ/phút) · Người Bóc Trần {narr / words:.0%} lời thoại · "
      f"{'TTS thật' if real else 'ước tính'} ({len(real)} câu thật)")
