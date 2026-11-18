# -*- coding: utf-8 -*-
"""
Trình biên dịch `factory196/materialAndDraft/EP05/episode.json` – Tập EP05:
"Tờ năm trăm và sáu giây nhìn thẳng" (16:9 Long-form · v2 Open-Ending).

Nguồn sự thật duy nhất của timeline: sửa thoại/nhịp ở phần STORY rồi chạy lại
    python factory196/materialAndDraft/EP05/source/build_draft.py
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
# 9 nhân vật = 9 voice hoàn toàn tách biệt trong 02_CAST/cast.json
NOT_OLD = "tuyệt đối không giả giọng bà già run rẩy, không kéo dài chữ, không cải lương"
SPK = {
    "AH": dict(
        speaker="anh_hai",
        voice="Orus",
        label_short="ANH HAI",
        speaker_label="Anh Hai – người cha 35 tuổi, đàng hoàng, hay giúp người",
        base=(
            "Giọng nam miền Nam Sài Gòn 35 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
            "giữ cố định một âm sắc trầm ấm, thẳng tính, rõ chữ, tự nhiên như đời thực"
        ),
    ),
    "AH_CLIP": dict(
        speaker="anh_hai",
        voice="Orus",
        af="phone",
        label_short="CLIP QUAY LÉN",
        speaker_label="Giọng Anh Hai trong đoạn clip 6 giây phát qua điện thoại",
        base=(
            "Giọng nam miền Nam Sài Gòn 35 tuổi, phát âm chuẩn phương ngữ miền Nam, "
            "đọc to rõ từng chữ một cách vô tư ngoài trời nắng"
        ),
    ),
    "CH": dict(
        speaker="chi_hai",
        voice="Sulafat",
        label_short="CHỊ HAI",
        speaker_label="Chị Hai – vợ Anh Hai, 34 tuổi, kiệm lời, tỉnh táo",
        base=(
            "Giọng phụ nữ miền Nam Sài Gòn 34 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
            "giữ cố định một âm sắc ấm, trầm vừa, ít lời; nói gọn, chắc, không chì chiết, không ngân dài"
        ),
    ),
    "TOM": dict(
        speaker="be_tom",
        voice="Puck",
        label_short="TOM",
        speaker_label="Bé Tom – con trai 8 tuổi",
        base=(
            "Giọng cậu bé trai 8 tuổi người miền Nam Sài Gòn, phát âm chuẩn phương ngữ miền Nam, "
            "trong sáng, lễ phép, nói tốc độ vừa phải, rõ chữ, tự nhiên như đời thực, giữ đúng một tông giọng duy nhất"
        ),
    ),
    "LANH": dict(
        speaker="co_hanh",
        voice="Despina",
        label_short="CÔ LÀNH",
        speaker_label="Cô Lành – vỏ bọc phụ nữ trung niên mắt mờ ngoài bãi xe",
        base=(
            "Giọng phụ nữ miền Nam Sài Gòn khoảng 50 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
            "giữ cố định một âm sắc mượt, hiền lành, thân tình, hơi rối nhẹ lúc nhờ giúp; " + NOT_OLD
        ),
    ),
    "LANH_BOSS": dict(
        speaker="co_hanh",
        voice="Despina",
        label_short="NGƯỜI ĐÀN BÀ",
        speaker_label="Bà trùm thu thập mẫu sinh trắc học (bộ mặt thật của Cô Lành)",
        base=(
            "Giọng phụ nữ miền Nam Sài Gòn khoảng 50 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
            "hạ tông trầm lạnh, chậm rãi, sắc bén và đầy quyền lực ngầm trong bóng tối; " + NOT_OLD
        ),
    ),
    "SUB_P": dict(
        speaker="ke_ngot_ngao_nam",
        voice="Achird",
        af="phone",
        label_short="ĐẦU DÂY DƯỚI",
        speaker_label="Đàn em báo cáo qua điện thoại",
        base=(
            "Giọng nam thanh niên miền Nam Sài Gòn 28 tuổi, phát âm chuẩn phương ngữ miền Nam, "
            "hạ giọng cung kính, dè dặt, báo cáo ngắn gọn qua điện thoại"
        ),
    ),
    "CN_P": dict(
        speaker="chu_no",
        voice="Fenrir",
        af="phone",
        label_short="SỐ LẠ",
        speaker_label="Đầu dây đòi nợ nhánh ngoài qua điện thoại",
        base=(
            "Giọng nam miền Nam Sài Gòn 40 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
            "giữ cố định một âm sắc trầm, đều, lịch sự mà lạnh băng; không la hét, không gào thét"
        ),
    ),
    "VY": dict(
        speaker="ke_ngot_ngao_nu",
        voice="Aoede",
        label_short="QUẦY QUÀ",
        speaker_label="Nhân viên quầy tặng quà khai trương",
        base=(
            "Giọng nữ trẻ miền Nam Sài Gòn 26 tuổi, phát âm chuẩn phương ngữ miền Nam, "
            "tươi tắn, lịch sự, chuyên nghiệp, nói gọn tự nhiên"
        ),
    ),
    "GDV": dict(
        speaker="chi_tu",
        voice="Zephyr",
        label_short="NGÂN HÀNG",
        speaker_label="Nữ giao dịch viên ngân hàng",
        base=(
            "Giọng phụ nữ miền Nam Sài Gòn 34 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
            "giữ cố định một âm sắc điềm tĩnh, rõ ràng, chuẩn mực nghiệp vụ và trấn an khách hàng"
        ),
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


SILENT = -40.0
EP01B = "factory196/materialAndDraft/EP01b/assets/"

# ================================================================ STORY
# ---- HOOK · MÓN NỢ TỪ CHÍNH GƯƠNG MẶT MÌNH (00:00 – 00:28) ----
amb("night_room", -1.5); bgm("suspense_pulse", -2.5)
scene("s00_night_ping", "assets/c00.jpg", "push", shake=0.2)
sfx("bank_ting", 0.15, -2)
bubble("NGÂN HÀNG X", "+3.500.000 VND · ND: GIAI NGAN HD 6.000.000",
       side="left", y=280, stamp="TIỀN LẠ VỀ", dur=5.2, offset=0.2)
sfx("phone_ring", 1.1, -4, dur=1.4)
beat(2.2)
line("l01_ah", "AH", "Alo, ai mới chuyển nhầm tiền vậy?", "ngơ ngác, hỏi thẳng")
line("l02_cn", "CN_P", "Không ai chuyển nhầm hết anh Hai. Hợp đồng sáu triệu của anh tới hạn thứ Sáu.",
     "trầm đều, lịch sự lạnh băng",
     sub="Không ai chuyển nhầm hết anh Hai. Hợp đồng 6 triệu của anh tới hạn thứ Sáu.")
line("l03_ah", "AH", "Anh nói bậy gì đó, tôi vay hồi nào?", "nhíu mày, gắt nhẹ")

scene("s01_mirror_shock", "assets/c01.jpg", "tense", tr="flash_white", trd=0.25, shake=0.15)
mark("hook_clip")
sfx("impact", 0.0, -3)
sfx("notification", 0.2, -4)
bubble("SỐ LẠ GỬI TỆP ĐÍNH KÈM", "Ảnh căn cước 2 mặt  +  Video quay cận mặt (00:06)",
       side="left", y=260, stamp="HỒ SƠ VAY", dur=5.6, offset=0.15)
beat(0.4)
line("l04_ah_clip", "AH_CLIP", "Tôi xác nhận đồng ý thực hiện hồ sơ…",
     "đọc to rõ ràng nhưng vô tư trong đoạn băng quay lén", pause=0.4)
line("l05_cn", "CN_P", "Mặt anh, tiếng anh, căn cước của anh đủ hết. Trễ hẹn thì sáng thứ Bảy cả xưởng anh xem clip này.",
     "chậm rãi, lạnh tanh, buông từng chữ")
sfx("call_end", 0.0, -3)
sfx("heartbeat", 0.2, -5, dur=2.2)
beat(2.6)

# ---- HỒI 1 · MẢNH GHÉP THỨ NHẤT: CHIẾC HỘP CAM & SỰ NGẬP NGỪNG ----
amb("street", -3.5); bgm("investigative_story", -3.5)
scene("s02_promo_desk", "assets/c02.jpg", "calm", tr="fade_black", trd=0.45)
chapter("HỒI 1 · BỐN NGÀY TRƯỚC", "CHIẾC HỘP CAM & TẤM HÌNH CĂN CƯỚC")
sfx("chapter_sting", -0.1, -5)
beat(1.0)
line("l06_tom", "TOM", "Ba ơi, mình đăng ký lấy cái bình màu cam nghen ba!",
     "háo hức, ôm hộp màu cam ngước nhìn ba")
line("l07_vy", "VY", "Dạ quà tặng cho bé, anh cho em chụp căn cước với số điện thoại để tránh nhận trùng nha.",
     "tươi cười, lịch sự, tự nhiên như nhân viên phát quà bình thường")
beat(1.8)   # nhịp ngập ngừng thật: Anh Hai khựng tay trên ví nhưng thấy con đã ôm chặt hộp quà
line("l08_ah", "AH", "Ờ… vậy em chụp lẹ giùm anh nha.",
     "ngập ngừng một nhịp rồi miễn cưỡng đồng ý vì con trai đã ôm hộp quà", pause=0.4)
sfx("notification", 0.1, -6)
beat(1.2)

# ---- HỒI 2 · MẢNH GHÉP THỨ HAI: TỜ NĂM TRĂM TIỀN THẬT & GÓC NÉ CAM ----
amb("street", -3.0); bgm("investigative_story", -3.0)
scene("s03_parking_approach", "assets/c03.jpg", "calm", tr="dissolve", trd=0.4)
chapter("HỒI 2 · BÃI GIỮ XE", "TỜ NĂM TRĂM TIỀN THẬT & SÁU GIÂY NHÌN THẲNG")
sfx("chapter_sting", -0.1, -5)
beat(2.2)   # nhịp câm: ánh mắt Cô Lành liếc chiếc hộp màu cam trên tay bé Tom
line("l09_la", "LANH", "Chú ơi, làm ơn giúp chị với. Chị đóng tiền thuốc mà thẻ lỗi hoài, chú đổi giùm chị năm trăm tiền mặt nghen.",
     "bối rối, hiền lành, đưa tờ 500 ngàn ra trước",
     sub="Chú ơi, làm ơn giúp chị với. Chị đóng tiền thuốc mà thẻ lỗi hoài, chú đổi giùm chị 500 tiền mặt nghen.")
beat(1.4)
line("l10_ah", "AH", "Dạ được chị. Chị đọc số tài khoản đi em chuyển cho.",
     "cởi mở, sẵn lòng giúp sau khi thấy tiền mặt thật và con trai đứng nhìn")
sfx("typing", 0.1, -6, dur=1.4)
sfx("bank_ting", 1.6, -4)
beat(2.2)

scene("s04_six_seconds_face", "assets/c04.jpg", "hand", tr="dissolve", trd=0.35)
beat(0.5)
line("l11_la", "LANH", "Khổ thiệt, mắt chị mờ quá… Chú đọc giùm chị dòng chữ nhỏ ngay ngón tay chị chỉ nè.",
     "luống cuống chỉ tay vào màn hình đưa trước mặt Anh Hai, khéo léo nghiêng đầu né khỏi camera")
beat(1.0)
mark("six_sec")
line("l12_ah", "AH", "Tôi xác nhận đồng ý thực hiện hồ sơ… Rồi, em bấm thoát giùm chị luôn rồi đó.",
     "cúi nhìn thẳng vào chỗ bà chỉ đọc rõ từng chữ, rồi vui vẻ bấm thoát", pause=0.4)
line("l13_la", "LANH", "Cảm ơn hai cha con nhiều lắm, đúng là gặp quý nhân!",
     "cảm kích rối rít", pause=0.6)
beat(0.8)

# Bếp nhà Anh Hai buổi trưa
amb("room_tone", -2.5); bgm("investigative_story", -5.0)
scene("s05_home_noon", "assets/c05.jpg", "calm", tr="fade_black", trd=0.4)
beat(0.6)
line("l14_tom", "TOM", "Mẹ ơi, sáng nay ba mới giúp một bà cô mắt mờ ngoài bãi xe đó!",
     "khoe mẹ hồn nhiên, tự hào về ba")
line("l15_ch", "CH", "Giúp sao vậy anh?", "hỏi gọn, tay vẫn nhặt rau")
line("l16_ah", "AH", "Bả đưa tờ năm trăm trước, nhờ anh chuyển khoản rồi bấm tắt giùm cái màn hình đơ.",
     "bình thản, đặt tờ tiền lên bàn",
     sub="Bả đưa tờ 500 trước, nhờ anh chuyển khoản rồi bấm tắt giùm cái màn hình đơ.")
beat(2.4)   # nhịp câm: tay Chị Hai khựng lại nửa giây

# Cảnh câm điện ảnh: Cô Lành tháo kính lão sau bãi xe – ra lệnh cho nhánh ngoài "thử nước"
amb("street", -4.5); bgm("tension_drone", -2.5)
scene("s06_glasses_off", "assets/c06.jpg", "push", tr="fade_black", trd=0.4)
mark("glasses_off")
beat(1.6)
sfx("message_send", 0.0, -4)
bubble("GỬI NHÁNH NGOÀI", "Mẫu hộp cam áo xám: Đã khớp căn cước quầy trong. Sáu giây mặt với tiếng nét căng.",
       side="left", y=250, stamp="ĐỦ HỒ SƠ", dur=5.2, offset=0.2)
beat(4.8)
sfx("message_send", 0.2, -4)
bubble("GỬI NHÁNH NGOÀI", "Chuyển bộ nháp cho tụi bây thử nước trước đi.",
       side="left", y=430, stamp="LỆNH ĐIỀU PHỐI", dur=4.0, offset=0.2)
beat(4.4)

# ---- HỒI 3 · THẾ KẸT LÚC NỬA ĐÊM: CÁI BẪY "TRẢ CHO ÊM CHUYỆN" ----
amb("night_room", -2.0); bgm("tension_drone", -2.0)
scene("s07_midnight_temptation", "assets/c07.jpg", "tense", tr="fade_black", trd=0.45)
chapter("HỒI 3 · NỬA ĐÊM TẠI NHÀ", "CÁI BẪY “TRẢ CHO ÊM CHUYỆN”")
sfx("chapter_sting", -0.1, -5)
beat(4.8)
sfx("notification", 0.0, -4)
bubble("SỐ LẠ", "Tất toán 6.000.000 vào TK cá nhân …9104 trước 23h đêm nay để xóa hồ sơ.",
       side="left", y=260, stamp="HỐI CHUYỂN", dur=5.2, offset=0.1)
sfx("typing", 1.2, -6, dur=1.6)
beat(3.4)
line("l17_ch", "CH", "Anh chuyển vô tài khoản cá nhân đó, lấy gì chắc tụi nó xóa clip?",
     "giữ cổ tay chồng lại, giọng trầm tĩnh")
line("l18_ah", "AH", "Bù có hai triệu rưỡi tiền mình thôi em… Chứ mai nó rải clip khắp xưởng, anh nhìn mặt ai?",
     "nghẹn giọng, căng thẳng vì sĩ diện",
     sub="Bù có 2 triệu rưỡi tiền mình thôi em… Chứ mai nó rải clip khắp xưởng, anh nhìn mặt ai?")
mark("chihai_truth")
line("l19_ch", "CH", "Nó thấy anh sợ mất mặt mà chịu trả lần đầu, tuần sau chính cái clip đó sẽ đẻ ra khoản thứ hai.",
     "nhìn thẳng chồng, chậm, sắc và chắc nịch", pause=0.8)
beat(1.0)

# Tinh gọn tối đa phản ứng thực tế: khóa thẻ + báo nhóm xưởng
scene("s08_lockdown_first_strike", "assets/c08.jpg", "calm", tr="dissolve", trd=0.35)
beat(0.4)
line("l20_ch", "CH", "Anh khóa thẻ trước đi.", "ngắn gọn, thực tế")
sfx("typing", 0.1, -6, dur=1.2)
beat(1.2)
line("l21_ah", "AH", "Ừ… Để anh nhắn lên nhóm xưởng báo trước một tiếng luôn.",
     "gọn, dứt khoát, tự nhiên")
sfx("message_send", 0.2, -4)
bubble("NHÓM XƯỞNG CƠ KHÍ", "Hình căn cước và mặt tôi vừa bị quay lén. Ai nhận tin vay mượn đừng chuyển.",
       side="right", y=280, stamp="BÁO TRƯỚC", dur=3.8, offset=0.2)
beat(4.2)

# ---- HỒI 4 · GỠ BẪY ĐÚNG LUẬT & CÚ CÚP MÁY Ở CỔNG ĐỒN ----
amb("office", -3.5); bgm("investigative_story", -4.5)
scene("s09_bank_counter", "assets/c09.jpg", "calm", tr="fade_black", trd=0.45)
chapter("HỒI 4 · SÁNG HÔM SAU", "KHOANH GIỮ TIỀN LẠ & LẬP BIÊN BẢN")
sfx("chapter_sting", -0.1, -5)
beat(1.0)
line("l22_gdv", "GDV", "Ngân hàng chính thống bắt buộc quét chip căn cước thật, nên kẻ gian không mở trộm khoản vay ngân hàng dưới tên anh được.",
     "điềm tĩnh, rõ ràng, giải thích chuẩn nghiệp vụ")
line("l23a_gdv", "GDV", "Em đã cập nhật lại khuôn mặt và tra tín dụng cá nhân của anh, hoàn toàn không có nợ vay.",
     "chắc chắn, trấn an")
line("l23b_gdv", "GDV", "Còn khoản ba triệu rưỡi chuyển vào không rõ nguồn, ngân hàng sẽ khoanh giữ chờ công an xử lý.",
     "chuẩn mực, dứt khoát",
     sub="Còn khoản 3 triệu rưỡi chuyển vào không rõ nguồn, ngân hàng sẽ khoanh giữ chờ công an xử lý.")
beat(1.6)

# Cổng trụ sở cơ quan công an – Không nhạc nền lúc đối chất
amb("street", -4.0); bgm("tension_drone", SILENT)
scene("s10_police_gate_call", "assets/c10.jpg", "calm", tr="fade_black", trd=0.4)
sfx("phone_ring", 0.2, -4, dur=1.4)
beat(1.6)
line("l24_cn", "CN_P", "Quá giờ rồi đó anh Hai. Chuyển sáu triệu hay để tôi gửi clip vô xưởng?",
     "lạnh, thúc ép",
     sub="Quá giờ rồi đó anh Hai. Chuyển 6 triệu hay để tôi gửi clip vô xưởng?")
mark("climax_counter")
line("l25_ah", "AH", "Xưởng tôi báo hết từ tối qua rồi. Khoản ba triệu rưỡi bên anh chuyển vô, tôi cũng vừa lập biên bản ngoài công an.",
     "điềm tĩnh, rõ từng chữ, không lên gân",
     sub="Xưởng tôi báo hết từ tối qua rồi. Khoản 3 triệu rưỡi bên anh chuyển vô, tôi cũng vừa lập biên bản ngoài công an.")
line("l26_ah", "AH", "Anh muốn nhận lại tiền thì mang giấy tờ ra cơ quan công an làm việc.",
     "dứt khoát, bình thản", pause=0.6)
beat(2.4)
sfx("call_end", 0.0, -2)
bubble("CUỘC GỌI ĐÃ KẾT THÚC", "Số máy này hiện không liên lạc được",
       side="left", y=280, stamp="ĐÃ CHẶN SỐ", dur=3.6, offset=0.2)
beat(4.0)

# ---- HỒI 5 · CÂU HỎI CỦA ĐỨA CON TRAI ----
amb("street", -4.5); bgm("warm_outro", -3.5)
scene("s11_school_pickup", "assets/c11.jpg", "calm", tr="fade_black", trd=0.5)
chapter("HỒI 5 · CHIỀU TAN HỌC", "GIỮ LÒNG TỐT, NHƯNG ĐỪNG ĐƯA ĐIỆN THOẠI")
sfx("school_bell", 0.0, -7)
beat(1.6)
mark("tom_q")
line("l27_tom", "TOM", "Ba ơi… Vậy mốt gặp người lớn tuổi ngoài đường nhờ giúp, mình giả bộ hông thấy hả ba?",
     "ngước nhìn ba, hỏi khẽ thật thà, hơi buồn", pause=1.0)
beat(0.8)
line("l28_ah", "AH", "Đâu có con. Người ta lạc đường hay mệt thì mình vẫn gọi bảo vệ, gọi người nhà phụ họ.",
     "trầm ấm, hiền hậu, cài nón bảo hiểm cho con")
line("l29_ah", "AH", "Chỉ có căn cước của mình với cái điện thoại người lạ… là ba con mình không đưa, không cầm thôi.",
     "nhẹ nhàng mà dứt khoát", pause=0.8)
beat(2.6)

# ---- THẺ NHỚ KỸ (DƯỚI 10 GIÂY) ----
amb("room_tone", -5.0); bgm("warm_outro", -4.0)
scene("s12_red_flags", EP01B + "scene18.jpg", "still", tr="fade_black", trd=0.4)
mark("rf_start")
sfx("bank_ting", 0.0, -5)
line("l30_narr", "N", "Thứ chúng lấy không phải tiền lẻ trên tay, mà là khuôn mặt và lòng tốt của bạn.")
beat(1.6)
mark("rf_end")

# ---- KẾT MỞ ĐƯỜNG DÂY NGẦM: BÀ GIÀ NGUY HIỂM KHÚC CUỐI (CẮT ĐÚNG 4:15) ----
amb("rain", -4.0); bgm("tension_drone", -1.2)
scene("s13_backseat_boss", "assets/c12.jpg", "push", tr="fade_black", trd=0.45)
sfx("phone_vibrate", 0.2, -3, dur=1.2)
beat(1.4)
mark("mafia_coda")
line("l31_sub", "SUB_P", "Dì ơi, thằng hộp cam đem khoản ba triệu rưỡi ra công an rồi. Nhánh ngoài cắt số rút êm rồi dì.",
     "cung kính, dè dặt báo cáo",
     sub="Dì ơi, thằng hộp cam đem khoản 3 triệu rưỡi ra công an rồi. Nhánh ngoài cắt số rút êm rồi dì.",
     pause=0.5)
sfx("heartbeat", 0.0, -4, dur=2.2)
line("l32_lanh_boss", "LANH_BOSS", "Mấy đồng bạc lẻ đó… thả cho nhánh ngoài thử phản ứng thôi.",
     "trầm lạnh, chậm rãi, bình thản đầy quyền lực", pause=0.25)

sfx("impact", 0.0, -1)
scene("s14_black_cut", "assets/c13.jpg", "still", tr="fade_black", trd=0.08)
beat(2.0)

# ---- DISCLAIMER ----
amb("room_tone", -6.0); bgm("tension_drone", -8.0)
scene("s15_disclaimer", EP01B + "scene18.jpg", "still", tr="fade_black", trd=0.35)
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


_desc = [(0.0, "Mở đầu – Khoản giải ngân lạ & đoạn clip 6 giây")]
_desc += [(c["start"] - 0.2, f"{c['kicker'].split('·')[0].strip().title()} – {c['title'].capitalize()}")
          for c in chapters if c["kicker"]]
_desc += [(marks["rf_start"], "Nhớ kỹ – 5 nguyên tắc bảo vệ khuôn mặt & căn cước")]
_desc += [(marks["mafia_coda"] - 1.2, "Kết mở – Cuộc gọi đêm mưa trên chiếc xe đen")]
desc_chapters = "\n".join(f"{mmss(max(0.0, s))} {label}" for s, label in sorted(_desc))

episode = {
    "episode_id": "EP05",
    "slug": "ToNamTramVaSauGiayNhinThang",
    "title": "Tờ năm trăm và sáu giây nhìn thẳng",
    "version": "v3-staging",
    "scam_family": "MIX – Dàn cảnh 2 chốt thu căn cước & quay lén 6 giây khuôn mặt sống + kết mở đường dây ngầm",
    "duration_sec": total,
    "visual_style_lock": (
        "Horizontal 16:9 widescreen (1920x1080), semi-realistic cinematic 2D anime illustration, "
        "contemporary Southern Vietnam urban setting, naturalistic dramatic lighting, clean bottom 15% for subtitles, "
        "no text, no letters, no numbers, no license plates, no logos, no real app interface, no real uniforms"
    ),
    "hook": {
        "kicker": "BẪY LÒNG TỐT NGOÀI ĐỜI · ĐÊM THỨ NĂM",
        "title": "TỜ NĂM TRĂM & SÁU GIÂY NHÌN THẲNG",
        "start": 0.4,
        "end": 5.0,
    },
    "chapters": chapters,
    "scenes": scenes,
    "dialogue": dialogue,
    "chat_bubbles": bubbles,
    "callouts": [],
    "red_flags": {
        "title": "NHỚ KỸ – BẢO VỆ CĂN CƯỚC & KHUÔN MẶT",
        "start": marks["rf_start"],
        "end": marks["rf_end"],
        "stagger_sec": 0.45,
        "items": [
            "KHÔNG CHO CHỤP CĂN CƯỚC ở các quầy tặng quà, khảo sát dọc đường",
            "KHÔNG CẦM ĐIỆN THOẠI NGƯỜI LẠ đưa ngang mặt hay đọc theo chữ trên màn hình",
            "NHẬN TIỀN “GIẢI NGÂN” LẠ: Giữ nguyên, tuyệt đối không tự chuyển trả vào tài khoản cá nhân",
            "KHÓA THẺ ONLINE & HẠ HẠN MỨC, báo trước nơi làm việc và kiểm tra tín dụng tại quầy ngân hàng",
            "LẬP BIÊN BẢN TẠI CƠ QUAN CÔNG AN để bảo vệ mình trước mọi tranh chấp vay mạo danh",
        ],
        "action": "Giúp người lớn tuổi ngoài đường bằng cách gọi bảo vệ hoặc người thân hỗ trợ — tuyệt đối không đưa căn cước và không nhìn vào màn hình điện thoại người lạ.",
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
            {"start": marks["hook_clip"] - 0.2, "end": marks["hook_clip"] + 3.5, "bgm_db": -12, "amb_db": -8},
            {"start": marks["chihai_truth"] - 0.2, "end": marks["chihai_truth"] + 4.5, "bgm_db": -14, "amb_db": -8},
            {"start": marks["climax_counter"] - 0.2, "end": marks["climax_counter"] + 6.0, "bgm_db": -16, "amb_db": -10},
            {"start": marks["tom_q"] - 0.2, "end": marks["tom_q"] + 4.8, "bgm_db": -12, "amb_db": -6},
            {"start": marks["mafia_coda"] - 0.2, "end": marks["disc_start"] - 0.2, "bgm_db": -10, "amb_db": -7},
            {"start": marks["disc_start"], "end": total - 0.05},
        ],
    },
    "forbidden_terms": [],
    "publish": {
        "titles": [
            "Đọc Giùm Dòng Chữ 6 Giây Ngoài Bãi Xe – Đêm Khuya Lộ Diện Chiếc Xe Đen | Bóc Trần Lừa Đảo",
            "Tờ Năm Trăm Tiền Thật, Sáu Giây Nhìn Thẳng & Người Đàn Bà Sau Kính Lão | Bóc Trần Lừa Đảo",
            "Đổi Tiền Mặt Giúp Người Lớn Tuổi Ngoài Đường: Cái Bẫy Phía Sau Ngón Tay Chỉ Chữ | Bóc Trần Lừa Đảo",
        ],
        "description": (
            "Đưa tờ 500.000đ tiền mặt thật vào tay bạn trước, rồi chỉ tay vào dòng chữ nhỏ trên màn hình nhờ đọc giùm — "
            "nhưng liệu khoản đòi nợ 6 triệu tối hôm đó đã phải là toàn bộ câu chuyện phía sau người phụ nữ mắt mờ ngoài bãi xe?\n\n"
            "⏱️ Các hồi trong phim:\n" + desc_chapters
        ),
        "pinned_comment": (
            "📌 Bạn từng gặp ai đưa tiền mặt thật ra trước rồi nhờ chuyển khoản hoặc nhờ đọc giùm màn hình điện thoại ngoài đường chưa? "
            "Hãy chia sẻ để mọi người cùng cảnh giác (lưu ý không đăng SĐT, STK hay tên người thật nhé)."
        ),
        "hashtags": ["#bóctrầnlừađảo", "#cảnhgiáclừađảo", "#vạnchuyện", "#antoànmạng", "#bảovệthôngtin"],
        "tags": [
            "cảnh giác lừa đảo", "bóc trần lừa đảo", "vạn chuyện", "nhờ bấm hộ điện thoại",
            "đổi tiền mặt chuyển khoản", "giải ngân mồi", "lộ căn cước", "bảo vệ sinh trắc học",
        ],
        "category": "Education (Giáo dục)",
        "playlist": "Hồ Sơ Bóc Trần Lừa Đảo – Phim Dài Chuyên Sâu",
        "thumbnail_sec": round(marks["six_sec"] + 0.5, 2),
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
