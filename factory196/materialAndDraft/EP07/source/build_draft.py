# -*- coding: utf-8 -*-
"""
Trình biên dịch `factory196/materialAndDraft/EP07/episode.json` – Tập EP07:
"Sau hai trăm triệu" (16:9 Long-form · v2-draft sau phản biện pháp lý).

Nguồn sự thật duy nhất của timeline: sửa thoại/nhịp ở phần STORY rồi chạy lại
    python factory196/materialAndDraft/EP07/source/build_draft.py
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
GAP = 0.36
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
# 8 nhân vật = 8 voice hoàn toàn tách biệt trong 02_CAST/cast.json
NOT_OLD = "tuyệt đối không giả giọng ông già hay bà già run rẩy, không kéo dài chữ, không cải lương"
TAM_BASE = (
    "Giọng nam miền Nam Sài Gòn 42 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
    "trầm khàn sương gió kiểu người va chạm ngoài đời, rõ chữ, tốc độ vừa phải, " + NOT_OLD
)
SPK = {
    "HUNG": dict(
        speaker="anh_hai",
        voice="Orus",
        label_short="HÙNG",
        speaker_label="Hùng – chủ xưởng sửa xe 38 tuổi, tự tin, nóng tính, sĩ diện cao rồi sụp đổ",
        base=(
            "Giọng nam miền Nam Sài Gòn 38 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
            "giữ cố định một âm sắc trầm vang, thẳng tính, rõ chữ, tự nhiên như đời thực, " + NOT_OLD
        ),
    ),
    "LAN": dict(
        speaker="chi_hai",
        voice="Sulafat",
        label_short="LAN",
        speaker_label="Lan – vợ Hùng 36 tuổi, thực tế, kiệm lời, dịu dàng, không chì chiết chồng",
        base=(
            "Giọng phụ nữ miền Nam Sài Gòn 36 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
            "giữ cố định một âm sắc ấm, trầm vừa, ít lời, nói gọn rõ chữ, tự nhiên như đời thực, " + NOT_OLD
        ),
    ),
    "MY": dict(
        speaker="be_bong",
        voice="Leda",
        label_short="BÉ MY",
        speaker_label="Bé My – con gái Hùng và Lan, 6 tuổi, hồn nhiên trong trẻo",
        base=(
            "Giọng một bé gái 6 tuổi miền Nam Sài Gòn, phát âm chuẩn phương ngữ miền Nam, "
            "trong, hồn nhiên, nói tốc độ vừa phải, rõ chữ, đồng nhất một tông giọng duy nhất, không nũng nịu giả tạo"
        ),
    ),
    "TAM": dict(
        speaker="ong_bay",
        voice="Algenib",
        label_short="ANH TÁM",
        speaker_label="Anh Tám – người quen ngoài xã hội 42 tuổi, bàn nhậu hào sảng nhưng đụng chuyện phủi tay",
        base=TAM_BASE,
    ),
    "TAM_P": dict(
        speaker="ong_bay",
        voice="Algenib",
        af="phone",
        label_short="ANH TÁM",
        speaker_label="Anh Tám nói qua điện thoại",
        base=TAM_BASE,
    ),
    "TAM_MEM": dict(
        speaker="ong_bay",
        voice="Algenib",
        af="memory",
        label_short="ANH TÁM (VỌNG)",
        speaker_label="Tiếng vọng lời hứa trên bàn nhậu của Anh Tám trong ký ức của Hùng",
        base=TAM_BASE,
    ),
    "TUAN_P": dict(
        speaker="ke_ngot_ngao_nam",
        voice="Achird",
        af="phone",
        label_short="TUẤN",
        speaker_label="Tuấn – người lạ tự xưng thuộc nhóm hỗ trợ lấy lại tiền, nói qua điện thoại",
        base=(
            "Giọng nam miền Nam Sài Gòn 31 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
            "âm sắc sáng gọn, mượt mà, lịch sự trơn tru, kiên nhẫn; lúc lật mặt thì lạnh băng sắc nhọn"
        ),
    ),
    "TUAN_ROOM": dict(
        speaker="ke_ngot_ngao_nam",
        voice="Achird",
        label_short="TUẤN",
        speaker_label="Tuấn trong căn phòng tối báo cáo lên đầu dây trên ở cảnh kết mở",
        base=(
            "Giọng nam miền Nam Sài Gòn 31 tuổi, phát âm chuẩn phương ngữ miền Nam, "
            "âm sắc sáng gọn, hạ giọng bình thản và lạnh nhạt như đang báo cáo công việc thường ngày"
        ),
    ),
    "CB": dict(
        speaker="chi_tu",
        voice="Zephyr",
        label_short="CÁN BỘ",
        speaker_label="Cán bộ tiếp nhận trình báo, 35 tuổi, điềm tĩnh, công tâm",
        base=(
            "Giọng phụ nữ miền Nam Sài Gòn 35 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
            "điềm tĩnh, rõ ràng, chuẩn mực, công tâm, không lên lớp hay mỉa mai, " + NOT_OLD
        ),
    ),
    "BOSS_P": dict(
        speaker="chu_no",
        voice="Fenrir",
        af="phone",
        label_short="ĐẦU DÂY TRÊN",
        speaker_label="Giọng người điều hành phía trên gọi qua điện thoại ở cảnh kết mở",
        base=(
            "Giọng nam miền Nam Sài Gòn 45 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
            "trầm sâu, đều, lạnh băng, nói chậm chắc từng chữ, " + NOT_OLD
        ),
    ),
    "N": dict(speaker="nguoi_boc_tran"),
}

MOTION = {
    "calm": {"scale": [1.02, 1.09], "focus": [[0.50, 0.50], [0.50, 0.47]], "wobble": "calm"},
    "tense": {"scale": [1.04, 1.14], "focus": [[0.50, 0.50], [0.48, 0.45]], "wobble": "tense"},
    "push": {"scale": [1.00, 1.16], "focus": [[0.50, 0.50], [0.50, 0.45]], "wobble": "calm"},
    "pull": {"scale": [1.13, 1.01], "focus": [[0.50, 0.46], [0.50, 0.50]], "wobble": "calm"},
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


def bubble(sender: str, text: str, side: str = "left", y: int = 270, stamp: str | None = None,
           dur: float = 4.8, offset: float = 0.0):
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
# ---- HOOK · ĐÊM THỨ TÁM (00:00 – ~00:25) ----
amb("night_room", -1.5); bgm("suspense_pulse", -2.5)
scene("s00_hook_midnight", "assets/c00.jpg", "push", shake=0.2)
sfx("notification", 0.15, -2)
bubble("NHÓM HỖ TRỢ LẤY LẠI TIỀN", "Lệnh hoàn trả 200.000.000đ bị lỗi mã xác thực · Cần bổ sung 40.000.000đ",
       side="left", y=290, stamp="TREO LỆNH", dur=5.6, offset=0.2)
beat(1.8)
line("l01_hung", "HUNG", "Đủ rồi! Tao vừa chuyển ba chục triệu cuối cùng xong, sao lại đòi thêm bốn chục triệu nữa?!",
     "khàn gắt, bức xúc dồn nén, tay siết điện thoại",
     sub="Đủ rồi! Tao vừa chuyển 30 triệu cuối cùng xong, sao lại đòi thêm 40 triệu nữa?!")
line("l02_tuan", "TUAN_P", "Anh Hùng bình tĩnh. Sai mã xác thực thì hệ thống khóa lệnh hoàn trả hai trăm triệu, bên em đâu mở được.",
     "mượt mà, lạnh đều như quy trình sẵn",
     sub="Anh Hùng bình tĩnh. Sai mã xác thực thì hệ thống khóa lệnh hoàn trả 200 triệu, bên em đâu mở được.")
line("l03_hung", "HUNG", "Tao biết tụi bây lừa tao rồi! Tao quen anh em ngoài đời, tụi bây trốn đâu tao cũng tìm ra!",
     "giận dữ, cố giữ uy thế đàn anh nhưng giọng bắt đầu run", pause=0.2)

scene("s01_hook_freeze", "assets/c01.jpg", "tense", tr="flash_white", trd=0.25, shake=0.15)
mark("hook_freeze")
sfx("impact", 0.0, -3)
sfx("heartbeat", 0.3, -4.5, dur=2.4)
beat(2.8)

# ---- HỒI 1 · CHIẾC ĐỒNG HỒ, BẢN VẼ XƯỞNG MỚI & LỜI HỨA BÀN NHẬU ----
amb("room_tone", -2.5); bgm("warm_outro", -5.0)
scene("s02_workshop_dream", "assets/c02.jpg", "calm", tr="fade_black", trd=0.5)
chapter("HỒI 1 · MỘT TUẦN TRƯỚC", "GIẤC MƠ XƯỞNG MỚI & SỰ TỰ TIN")
sfx("chapter_sting", -0.1, -5)
beat(1.0)
line("l05_hung", "HUNG", "Sáu năm vợ chồng mình gom góp mới đủ hai trăm triệu. Cuối tháng này ký cọc sang mặt bằng ngoài lộ lớn luôn.",
     "tự hào, giọng vang ấm, chỉ tay lên bản vẽ xưởng mới",
     sub="6 năm vợ chồng mình gom góp mới đủ 200 triệu. Cuối tháng này ký cọc sang mặt bằng ngoài lộ lớn luôn.")
line("l06_my", "MY", "Xưởng mới có cái sân rộng cho con chạy chơi hông ba?",
     "hào hứng, ngước mắt trong veo hỏi ba")
line("l07_hung", "HUNG", "Có chứ con gái! Sân rộng gấp ba lần ở đây luôn.",
     "cười lớn, xoa đầu con gái đầy thương yêu")
line("l08_lan", "LAN", "Tiền cọc đủ rồi thì anh cứ giữ yên trong ngân hàng, đừng xoay qua chỗ nào nữa nghen anh.",
     "dịu dàng, thực tế, nhắc chồng một câu nhẹ nhàng", pause=0.5)

amb("crowd", -5.5); bgm("investigative_story", -4.5)
scene("s03_drinking_table", "assets/c03.jpg", "hand", tr="dissolve", trd=0.45)
beat(0.8)
line("l09_tam", "TAM", "Chơi với thằng Hùng tao khoái cái tính sòng phẳng. Khu này có chuyện gì cứ gọi một tiếng, anh em tao lo liền.",
     "sang sảng, khoác vai vỗ mạnh ra vẻ nghĩa khí trên bàn ăn")
line("l10_hung", "HUNG", "Sống ngoài đời hơn nhau chỗ có anh em! Chứ đụng chuyện mà chạy đi làm đơn chờ giấy tờ tới chừng nào.",
     "cười tự đắc, nâng ly đầy kiêu hãnh", pause=0.5)

amb("night_room", -2.5); bgm("tension_drone", -3.0)
scene("s04_first_trap_200m", "assets/c04.jpg", "push", tr="fade_black", trd=0.45)
sfx("bank_ting", 0.25, -4)
# Cài tên "Ngọc" – người chăm sóc bên ứng dụng đầu tư lạ (trả ở s09 và kết mở)
bubble("CHUYÊN VIÊN NGỌC", "Lệnh thử đã rút +6.500.000đ · Gói chốt tuần: nạp 200.000.000đ trước 21h nha anh",
       side="left", y=250, stamp="RÚT LÃI THỬ", dur=4.4, offset=0.25)
sfx("typing", 2.0, -5, dur=1.2)
sfx("glitch", 3.6, -3)
sfx("impact", 3.9, -3.5)
bubble("ỨNG DỤNG ĐẦU TƯ LẠ", "Tài khoản đã bị đóng băng · Không thể kết nối máy chủ",
       side="left", y=470, stamp="MẤT 200 TRIỆU", dur=5.2, offset=3.8)
beat(4.8)
line("l11_hung", "HUNG", "Mấy triệu đầu rút thử trơn tru vậy mà… Ủa, sao vừa đẩy hai trăm triệu vô là sập trang luôn?!",
     "từ tự tin bỗng khựng lại, giọng hụt hơi bàng hoàng",
     sub="Mấy triệu đầu rút thử trơn tru vậy mà… Ủa, sao vừa đẩy 200 triệu vô là sập trang luôn?!", pause=0.6)

# ---- HỒI 2 · CHÊ CÔNG AN, NHỜ NGƯỜI QUEN & CÚ PHỦI TAY ----
amb("room_tone", -2.5); bgm("investigative_story", -3.5)
scene("s05_reject_police", "assets/c05.jpg", "tense", tr="fade_black", trd=0.45)
chapter("HỒI 2 · CÚ TÁT ĐẦU TIÊN", "NGƯỜI QUEN NGOÀI ĐỜI & CÁI TÀI KHOẢN MƯỢN TÊN")
sfx("chapter_sting", -0.1, -5)
beat(1.0)
line("l12_lan", "LAN", "Ngưng lại liền đi anh! Gọi ngân hàng khóa giao dịch, rồi cầm sao kê ra công an trình báo ngay sáng nay.",
     "lo âu nhưng dứt khoát, nắm tay chồng khuyên thật lòng")
line("l13_hung", "HUNG", "Báo công an?! Làm đơn chờ tới mùa quýt nào mới thấy lại tiền? Tiệm mình cuối tháng ký cọc rồi!",
     "nóng nảy, tự ái, gạt phắt lời vợ")
line("l14_lan", "LAN", "Hai trăm triệu là tiền sáu năm mình dành dụm. Ngoài ngân hàng với công an, ai truy được tiền trên mạng hả anh?",
     "nhìn thẳng chồng, giọng nghẹn nhẹ mà tỉnh táo",
     sub="200 triệu là tiền 6 năm mình dành dụm. Ngoài ngân hàng với công an, ai truy được tiền trên mạng hả anh?")
line("l15_hung", "HUNG", "Tài khoản đứng tên anh, để anh lo! Cho anh ba ngày, anh nhờ anh Tám ngoài xã hội tìm tới tận cửa.",
     "đứng bật dậy, vênh mặt cố giữ sĩ diện đàn anh", pause=0.6)
beat(1.0)   # nhịp câm: Lan nhìn chồng rất lâu, im lặng chấp nhận

amb("street", -5.0); bgm("investigative_story", -4.0)
scene("s06_meet_tam", "assets/c06.jpg", "calm", tr="fade_black", trd=0.4)
bubble("BIÊN LAI CHUYỂN KHOẢN", "Người nhận: ••••• (TK ••••) · Tổng 3 đợt: 200.000.000đ",
       side="left", y=260, stamp="ĐƯA 5 TRIỆU ĐI HỎI", dur=5.4, offset=0.25)
beat(1.2)
line("l16_hung", "HUNG", "Chút tiền xăng xe anh em đi việc. Anh Tám coi quen ai rành, lần giùm em cái tài khoản này nha.",
     "nôn nóng, đẩy phong bì tiền mặt qua bàn")
line("l17_tam", "TAM", "Ừ, để anh hỏi thử mấy đứa coi sao.",
     "cất gọn phong bì, hơi khựng mặt khi nghe chuyện tiền trên mạng", pause=0.5)

amb("street", -4.5); bgm("tension_drone", -2.5)
scene("s07_tam_brushoff", "assets/c07.jpg", "push", tr="fade_black", trd=0.45)
mark("tam_betray")
sfx("phone_ring", 0.3, -4, dur=1.4)
beat(1.8)
line("l18_tam", "TAM_P", "Tao hỏi mấy đứa rành chuyện này rồi. Tài khoản kiểu đó toàn đứng tên người bán giấy tờ, lần theo chẳng tới đầu nậu.",
     "thái độ đổi hẳn, lạnh nhạt, không còn thân tình")
line("l19_hung", "HUNG", "Vậy anh nhờ anh em lần tiếp đi anh! Hai trăm triệu của em đó!",
     "sững sờ, giọng chới với hỏi dồn",
     sub="Vậy anh nhờ anh em lần tiếp đi anh! 200 triệu của em đó!")
line("l20_tam", "TAM_P", "Dính lừa trên mạng là dính pháp luật, anh em tao hông đụng. Mày tự ra công an đi.",
     "phủi tay lạnh tanh, nói xong cúp máy luôn", pause=0.3)
sfx("call_end", 0.0, -3)
beat(2.4)   # nhịp câm: không ai nhắc tới 5 triệu; Hùng nhìn màn hình tắt ngấm

# ---- HỒI 3 · NHÓM "LẤY LẠI TIỀN" & VÒNG XOÁY KHÔNG THỂ DỪNG ----
amb("night_room", -2.0); bgm("tension_drone", -2.8)
scene("s08_search_alone", "assets/c08.jpg", "hand", tr="fade_black", trd=0.5)
chapter("HỒI 3 · CÁI BẪY LẦN HAI", "NHÓM LẤY LẠI TIỀN & LỜI HỨA VỀ QUÁ KHỨ")
sfx("chapter_sting", -0.1, -5)
sfx("typing", 0.4, -5.5, dur=1.2)
bubble("NHÓM HỖ TRỢ LẤY LẠI TIỀN", "Cam kết lấy lại tiền bị treo trên sàn · Không cần chờ thủ tục",
       side="left", y=260, stamp="QUẢNG CÁO", dur=5.2, offset=0.4)
bubble("BÌNH LUẬN DƯỚI BÀI ĐĂNG", "Cảm ơn nhóm đã lấy lại 180 triệu cho em sau 3 ngày!",
       side="left", y=480, stamp="TÀI KHOẢN ẢO", dur=4.8, offset=1.8)
beat(2.8)
line("l22_tuan", "TUAN_P", "Nói thật với anh Hùng, chờ thủ tục lâu lắm. Bên em có đội kỹ thuật chuyên kéo tiền bị treo trên sàn về.",
     "mượt mà, hạ giọng thân tình vuốt đúng cái tôi người sành đời")
line("l23_hung", "HUNG", "Tao mới mất hai trăm triệu xong, đừng hòng dụ tao lần nữa. Tụi bây có gì chứng minh làm được thật?",
     "cảnh giác cao độ, hỏi vặn gắt gỏng",
     sub="Tao mới mất 200 triệu xong, đừng hòng dụ tao lần nữa. Tụi bây có gì chứng minh làm được thật?")
line("l24_tuan", "TUAN_P", "Anh cảnh giác là đúng. Bên em hông thu đồng nào trước. Anh cứ gửi sao kê qua kiểm tra.",
     "kiên nhẫn, bình tĩnh, không hề thúc ép để đánh gục sự đề phòng")
sfx("typing", 0.1, -5, dur=1.0)
sfx("message_send", 1.2, -4)
beat(1.8)

scene("s09_insider_detail", "assets/c09.jpg", "push", tr="dissolve", trd=0.45)
sfx("notification", 0.2, -3)
bubble("HỒ SƠ #094", "Đã khóa nguồn tiền treo: 200.000.000đ · Chuyên viên phụ trách bên sàn: Ngọc",
       side="left", y=250, stamp="KHỚP DỮ LIỆU", dur=5.6, offset=0.25)
beat(1.4)
line("l25_tuan", "TUAN_P", "Đội kỹ thuật khóa được hai trăm triệu của anh rồi. Bên sàn đó, chuyên viên chăm sóc anh tên Ngọc, đúng hông?",
     "tự tin, chậm rãi, cố ý buông một chi tiết Hùng chưa từng gửi",
     sub="Đội kỹ thuật khóa được 200 triệu của anh rồi. Bên sàn đó, chuyên viên chăm sóc anh tên Ngọc, đúng hông?")
line("l26_hung", "HUNG", "Sao… sao mày biết tên con nhỏ đó? Tao đâu có gửi tin nhắn nào…",
     "sững người, nghi ngờ tan biến thành kinh ngạc")
line("l26b_tuan", "TUAN_P", "Bên em truy tới tận người chăm sóc bên sàn mà anh.",
     "nhẹ tênh, tự tin như chuyện thường")
line("l26c_hung", "HUNG", "Giỏi thiệt… hơn hẳn mấy ông anh ngoài đời.",
     "mắt sáng lên, thở ra, tin sái cổ rằng mình đã tìm đúng cao thủ")
line("l27_tuan", "TUAN_P", "Lệnh khóa chỉ giữ hai mươi bốn tiếng. Anh đóng mười triệu mở hồ sơ, tiền về là hoàn lại đủ.",
     "nhẹ nhàng, hợp lý hóa khoản phí đầu tiên",
     sub="Lệnh khóa chỉ giữ 24 tiếng. Anh đóng 10 triệu mở hồ sơ, tiền về là hoàn lại đủ.")
sfx("typing", 0.1, -5.5, dur=0.9)
sfx("bank_ting", 1.1, -3.5)
beat(1.6)

# Trọng tâm tâm lý: đã nghi ngờ nhưng không thể dừng vì tiền đã bỏ ra & lời hứa "ba ngày" với vợ
amb("night_room", -1.8); bgm("tension_drone", -2.0)
scene("s10_doubt_and_lie", "assets/c10.jpg", "tense", tr="fade_black", trd=0.45)
mark("sunk_cost_lie")
sfx("notification", 0.2, -3.5)
bubble("NHÓM HỖ TRỢ LẤY LẠI TIỀN", "Cổng thanh toán yêu cầu bổ sung 15.000.000đ phí xác minh giải tỏa",
       side="left", y=250, stamp="PHÁT SINH PHÍ", dur=5.4, offset=0.25)
beat(1.0)
line("l28_hung", "HUNG", "Khoan đã! Hôm qua mày nói đóng mười triệu là xong, sao nay đẻ thêm mười lăm triệu?! Tụi bây giở trò phải hông?",
     "nghi ngờ thật sự, đập nhẹ tay xuống bàn, giọng gắt",
     sub="Khoan đã! Hôm qua mày nói đóng 10 triệu là xong, sao nay đẻ thêm 15 triệu?! Tụi bây giở trò phải hông?")
line("l29_tuan", "TUAN_P", "Anh nghi thì cứ hủy hồ sơ, bên em đâu ép. Chỉ tiếc hai trăm triệu với mười triệu vừa đóng mất trắng thôi.",
     "lạnh tĩnh, không nài nỉ, khóa chặt nỗi sợ mất trắng",
     sub="Anh nghi thì cứ hủy hồ sơ, bên em đâu ép. Chỉ tiếc 200 triệu với 10 triệu vừa đóng mất trắng thôi.")
sfx("heartbeat", 0.1, -4, dur=2.2)
beat(2.0)
line("l30_lan", "LAN", "Anh Hùng ơi, mai là hết ba ngày rồi. Bên anh Tám lo tới đâu rồi anh?",
     "vọng nhẹ từ phòng bên, dịu dàng và tin tưởng chồng", pause=0.5)
line("l31_hung", "HUNG", "Ờ… sắp xong rồi em. Em ngủ trước đi.",
     "nuốt khan, giọng khô khốc nói dối vì không dám thú thật", pause=0.3)
sfx("typing", 0.1, -5.5, dur=1.0)
sfx("bank_ting", 1.2, -3.5)
beat(1.8)

# Cảnh câm: tháo đồng hồ cầm đồ gom 30 triệu cuối -> tổng lần hai 55 triệu
amb("street", -5.5); bgm("tension_drone", -2.2)
scene("s11_pawn_watch", "assets/c11.jpg", "push", tr="fade_black", trd=0.5)
bubble("LỊCH SỬ CHUYỂN KHOẢN", "Đợt 1: -10.000.000đ · Đợt 2: -15.000.000đ · Đợt 3: -30.000.000đ (Tổng lần hai: -55.000.000đ)",
       side="left", y=250, stamp="CẠN SẠCH TIỀN", dur=5.6, offset=0.4)
sfx("bank_ting", 2.0, -3.5)
sfx("heartbeat", 2.8, -4.5, dur=2.4)
beat(6.2)

# Cú lật mặt (nối tiếp ngay câu đe dọa cuối Hook)
amb("night_room", -1.5); bgm("tension_drone", SILENT)
scene("s12_mask_off", "assets/c12.jpg", "tense", tr="fade_black", trd=0.4)
mark("mask_off")
beat(0.8)
line("l32a_tuan", "TUAN_P", "Anh biết có mùi từ bữa đóng mười lăm triệu rồi, đúng hông?",
     "buông từng chữ chậm rãi, sắc lạnh",
     sub="Anh biết có mùi từ bữa đóng 15 triệu rồi, đúng hông?", pause=0.4)
line("l32b_tuan", "TUAN_P", "Anh vẫn tự nộp thêm ba chục triệu… chỉ vì hông dám về nói thật với vợ thôi.",
     "cười nhạt lạnh băng, chạm đúng nỗi xấu hổ",
     sub="Anh vẫn tự nộp thêm 30 triệu… chỉ vì hông dám về nói thật với vợ thôi.", pause=0.3)
sfx("call_end", 0.0, -2.5)
sfx("impact", 0.3, -3)
bubble("HỆ THỐNG TIN NHẮN", "Không thể gửi tin nhắn · Trang và tài khoản đã bị xóa",
       side="left", y=290, stamp="ĐÃ CHẶN", dur=4.6, offset=0.4)
beat(3.0)

# ---- HỒI 4 · CUỘC GỌI KHÔNG AI NGHE & TRÌNH BÁO MUỘN ----
amb("night_room", -2.0); bgm("investigative_story", -6.5)
scene("s13_unanswered_call", "assets/c13.jpg", "pull", tr="fade_black", trd=0.55)
chapter("HỒI 4 · TRÌNH BÁO MUỘN MÀNG", "CUỘC GỌI KHÔNG AI NGHE & SỰ THẬT")
sfx("chapter_sting", -0.1, -5)
sfx("phone_ring", 0.5, -4, dur=2.6)
bubble("DANH BẠ · ANH TÁM", "Đang gọi… Không có câu trả lời",
       side="left", y=260, stamp="KHÔNG BẮT MÁY", dur=5.2, offset=0.6)
beat(3.2)
sfx("call_end", 0.0, -4)
beat(0.5)
line("l33_tam_mem", "TAM_MEM", "Khu này có chuyện gì cứ gọi một tiếng, anh em tao lo liền.",
     "vang vọng từ ký ức bàn nhậu, lạnh lẽo và chua chát", pause=0.8)
beat(1.2)

amb("night_room", -2.5); bgm("warm_outro", -7.5)
scene("s14_bare_wrist_confession", "assets/c14.jpg", "calm", tr="dissolve", trd=0.5)
mark("wife_confession")
beat(1.4)
line("l34_lan", "LAN", "Hết sạch rồi hả anh?",
     "giọng rất khẽ, nghẹn nhẹ, không một lời trách móc", pause=0.7)
line("l35_hung", "HUNG", "Hai trăm triệu ban đầu… cộng thêm sáu chục triệu anh tự đi lo bên ngoài… mất hết rồi Lan ơi.",
     "gục đầu, giọng khàn vỡ ra lần đầu tiên trong đời",
     sub="200 triệu ban đầu… cộng thêm 60 triệu anh tự đi lo bên ngoài… mất hết rồi Lan ơi.", pause=1.0)
beat(1.0)
line("l36_lan", "LAN", "Giờ gọi tổng đài ngân hàng liền đi anh. Sáng mai vợ chồng mình ra công an.",
     "chậm rãi, xót xa nhưng vững vàng nắm tay chồng", pause=0.8)

amb("office", -4.5); bgm("investigative_story", -5.5)
scene("s15_police_truth", "assets/c15.jpg", "calm", tr="fade_black", trd=0.5)
mark("police_truth")
beat(1.0)
line("l37_cb", "CB", "Anh để gần năm ngày mới trình báo. Hai trăm triệu đầu chuyển đi lâu quá, xác minh khó hơn nhiều rồi.",
     "điềm tĩnh, nghiêm túc, rõ từng chữ, không mỉa mai",
     sub="Anh để gần năm ngày mới trình báo. 200 triệu đầu chuyển đi lâu quá, xác minh khó hơn nhiều rồi.", pause=0.4)
line("l38_hung", "HUNG", "Còn mấy khoản em nộp cho nhóm lấy lại tiền…",
     "cúi gằm mặt, giọng nghẹn nhỏ lại", pause=0.3)
line("l39a_cb", "CB", "Mấy khoản đó còn mới. Tôi đề nghị ngân hàng phối hợp xác minh ngay.",
     "dứt khoát, chuyên nghiệp, bắt tay vào việc", pause=0.3)
line("l39b_cb", "CB", "Người lạ hứa kéo tiền về rồi đòi phí trước, đó là lừa lần hai.",
     "trầm tĩnh, thẳng thắn, không lên lớp", pause=0.8)
beat(1.4)

# ---- HỒI 5 · BẢN VẼ TRONG HỘC TỦ & CÂU HỎI CỦA CON GÁI ----
amb("street", -5.5); bgm("warm_outro", -6.5)
scene("s16_drawer_seen", "assets/c16.jpg", "pull", tr="fade_black", trd=0.55)
chapter("HỒI 5 · LÀM LẠI TỪ ĐẦU", "BẢN VẼ TRONG HỘC TỦ")
sfx("chapter_sting", -0.1, -5)
bubble("ANH TÁM", "Anh Tám ơi, em kẹt tiền nhập đồ, anh cho em xoay tạm ít bữa…",
       side="left", y=270, stamp="ĐÃ XEM · 3 NGÀY TRƯỚC", dur=5.0, offset=0.6)
beat(5.8)   # cảnh câm: Hùng cuộn bản vẽ xưởng mới cất sâu vô hộc tủ cũ, đóng ngăn kéo

amb("room_tone", -3.0); bgm("warm_outro", -5.5)
scene("s17_daughter_question", "assets/c17.jpg", "push", tr="dissolve", trd=0.45)
mark("daughter_q")
beat(0.8)
line("l40_my", "MY", "Ba ơi, chừng nào mình dọn qua xưởng lớn có sân rộng cho con chạy chơi hả ba?",
     "trong trẻo, hồn nhiên, kéo gấu áo ba hỏi khẽ", pause=1.2)

scene("s18_start_over", "assets/c18.jpg", "calm", tr="dissolve", trd=0.45)
beat(1.1)
line("l41_hung", "HUNG", "Chắc còn lâu lắm con… Ba làm sai rồi. Giờ ba phải làm lại từ đầu.",
     "ngồi ngang tầm con, giọng khàn nén xúc động, xoa đầu con gái", pause=1.0)
beat(2.8)

# ---- MÀN HÌNH ĐEN · CHỮ TRẮNG ----
amb("room_tone", -8.0); bgm("warm_outro", -9.5)
scene("s19_black_epilogue", "assets/c20.jpg", "still", tr="fade_black", trd=0.6)
mark("black_text")
chapter("", "Kẻ lừa đầu tiên lấy tiền bằng lời hứa bạn sẽ có thêm.", offset=0.5, dur=3.8)
chapter("", "Kẻ thứ hai lấy nốt phần còn lại, bằng nỗi xấu hổ không dám nói ra.", offset=4.6, dur=4.5)
beat(9.8)

# ---- THẺ NHỚ KỸ (DƯỚI 10 GIÂY · NGƯỜI BÓC TRẦN ĐÚNG 1 CÂU) ----
amb("room_tone", -5.0); bgm("warm_outro", -4.5)
scene("s20_red_flags", EP01B + "scene18.jpg", "still", tr="fade_black", trd=0.4)
mark("rf_start")
sfx("bank_ting", 0.0, -5)
line("l42_narr", "N", "Giấu người nhà, nhờ người quen thay vì báo công an, là mở cửa cho lần lừa thứ hai.")
beat(1.0)
mark("rf_end")

# ---- KẾT MỞ · CÙNG MỘT ĐẦU MỐI ----
amb("night_room", -3.0); bgm("tension_drone", -1.2)
scene("s21_scam_ring_coda", "assets/c19.jpg", "push", tr="fade_black", trd=0.45)
sfx("typing", 0.15, -5, dur=1.2)
bubble("HỒ SƠ TUẦN NÀY", "Ứng dụng đầu tư: -200.000.000đ  ->  Nhóm lấy lại tiền: +55.000.000đ",
       side="left", y=250, stamp="CHUYỂN VÒNG 2", dur=5.6, offset=0.5)
beat(1.6)
mark("ring_coda")
line("l43_tuan_coda", "TUAN_ROOM", "Hồ sơ hai trăm triệu con Ngọc chuyển qua, bên em chốt thêm được năm mươi lăm triệu rồi anh.",
     "bình thản báo cáo như xong một đơn hàng",
     sub="Hồ sơ 200 triệu con Ngọc chuyển qua, bên em chốt thêm được 55 triệu rồi anh.", pause=0.35)
sfx("heartbeat", 0.0, -4, dur=2.2)
line("l44_boss_coda", "BOSS_P", "Lọc tiếp danh sách tuần này. Ưu tiên mấy người giấu vợ con, chưa chịu đi trình báo.",
     "trầm sâu, lạnh băng, chậm chắc từng chữ", pause=0.25)

sfx("impact", 0.0, -1)
scene("s22_black_cut", "assets/c20.jpg", "still", tr="fade_black", trd=0.08)
beat(2.0)

# ---- DISCLAIMER ----
amb("room_tone", -6.0); bgm("tension_drone", -8.0)
scene("s23_disclaimer", EP01B + "scene18.jpg", "still", tr="fade_black", trd=0.35)
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


_desc = [(0.0, "Mở đầu – Đêm thứ tám sau hai trăm triệu")]
_desc += [(c["start"] - 0.2, f"{c['kicker'].split('·')[0].strip().title()} – {c['title'].capitalize()}")
          for c in chapters if c["kicker"]]
_desc += [(marks["rf_start"], "Nhớ kỹ – 5 nguyên tắc tránh bẫy lừa lần hai")]
_desc += [(marks["ring_coda"] - 1.5, "Kết mở – Cùng một đầu mối")]
desc_chapters = "\n".join(f"{mmss(max(0.0, s))} {label}" for s, label in sorted(_desc))

episode = {
    "episode_id": "EP07",
    "slug": "SauHaiTramTrieu",
    "title": "Sau hai trăm triệu",
    "version": "v2-draft",
    "scam_family": "MIX-RECOVERY – Bẫy lừa lần hai: mất 200 triệu, giấu người nhà, nhờ người quen rồi tin nhóm tự xưng lấy lại tiền trên mạng",
    "duration_sec": total,
    "visual_style_lock": (
        "Horizontal 16:9 widescreen (1920x1080), semi-realistic cinematic 2D anime illustration, "
        "contemporary Southern Vietnam urban setting, naturalistic dramatic lighting, clean bottom 15% for subtitles, "
        "no text, no letters, no numbers, no license plates, no logos, no real app interface, "
        "no real police or bank uniforms or insignia, no weapons, no blood, no gore, no violence"
    ),
    "hook": {
        "kicker": "BẪY LỪA LẦN HAI · SAU KHI ĐÃ MẤT TIỀN",
        "title": "SAU HAI TRĂM TRIỆU",
        "start": 0.4,
        "end": 5.0,
    },
    "chapters": chapters,
    "scenes": scenes,
    "dialogue": dialogue,
    "chat_bubbles": bubbles,
    "callouts": [],
    "red_flags": {
        "title": "NHỚ KỸ – BẪY LỪA LẦN HAI",
        "start": marks["rf_start"],
        "end": marks["rf_end"],
        "stagger_sec": 0.45,
        "items": [
            "AI HỨA CHẮC KÉO TIỀN VỀ RỒI ĐÒI PHÍ TRƯỚC: Đó là bẫy lừa lần hai, dù họ xưng là nhóm hỗ trợ, chuyên gia hay người từng bị lừa",
            "NGƯỜI QUEN NGOÀI ĐỜI KHÔNG TRUY ĐƯỢC TIỀN: Truy vết dòng tiền là việc của ngân hàng và cơ quan điều tra",
            "BIẾT ĐÚNG CHUYỆN CỦA BẠN CHƯA CHẮC ĐÁNG TIN: Kẻ gian có thể chung một đầu mối với nhóm đã lừa bạn lần đầu",
            "DỪNG TỪ KHOẢN PHÍ ĐẦU TIÊN: Không bỏ thêm tiền thật để cứu khoản tiền đã mất",
            "BÁO CÀNG SỚM CÀNG CÓ CƠ HỘI: Gọi tổng đài ngân hàng, lưu sao kê, trình báo công an và đừng giấu người nhà",
        ],
        "action": "Ngay khi phát hiện bị lừa: dừng chuyển tiền, gọi tổng đài ngân hàng yêu cầu hỗ trợ khóa giao dịch, nói thật với người thân và trình báo cơ quan công an sớm nhất.",
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
            {"start": marks["hook_freeze"] - 0.2, "end": marks["hook_freeze"] + 4.5, "bgm_db": -12, "amb_db": -8},
            {"start": marks["tam_betray"] - 0.2, "end": marks["tam_betray"] + 9.0, "bgm_db": -12, "amb_db": -7},
            {"start": marks["sunk_cost_lie"] - 0.2, "end": marks["sunk_cost_lie"] + 12.0, "bgm_db": -10, "amb_db": -6},
            {"start": marks["mask_off"] - 0.2, "end": marks["mask_off"] + 10.0, "bgm_db": -18, "amb_db": -10},
            {"start": marks["wife_confession"] - 0.2, "end": marks["wife_confession"] + 14.0, "bgm_db": -12, "amb_db": -7},
            {"start": marks["police_truth"] - 0.2, "end": marks["police_truth"] + 16.0, "bgm_db": -12, "amb_db": -8},
            {"start": marks["daughter_q"] - 0.2, "end": marks["black_text"] - 0.2, "bgm_db": -11, "amb_db": -7},
            {"start": marks["ring_coda"] - 0.2, "end": marks["disc_start"] - 0.2, "bgm_db": -10, "amb_db": -7},
            {"start": marks["disc_start"], "end": total - 0.05},
        ],
    },
    "forbidden_terms": [],
    "publish": {
        "titles": [
            "Mất 200 Triệu, Rồi Mất Thêm 60 Triệu Để 'Lấy Lại' – Cái Bẫy Sau Khi Bạn Bị Lừa | Bóc Trần Lừa Đảo",
            "Sau Hai Trăm Triệu: Khi Nỗi Xấu Hổ Khiến Người Ta Tự Nộp Tiền Lần Hai | Bóc Trần Lừa Đảo",
            "Nhờ Người Quen, Tin Nhóm 'Lấy Lại Tiền' Trên Mạng: Bẫy Lừa Lần Hai | Bóc Trần Lừa Đảo",
        ],
        "description": (
            "Mất 200 triệu đồng tiền tích góp 6 năm vào một ứng dụng đầu tư lạ, Hùng gạt lời vợ khuyên trình báo, "
            "nhờ người quen ngoài đời rồi tin một nhóm tự xưng lấy lại tiền trên mạng. "
            "Thứ giữ anh lại trong vòng xoáy không phải sự ngây thơ, mà là nỗi xấu hổ không dám nói thật với gia đình.\n\n"
            "⏱️ Các hồi trong phim:\n" + desc_chapters
        ),
        "pinned_comment": (
            "📌 Bạn hay người thân từng gặp người lạ hứa chắc lấy lại tiền bị lừa rồi đòi phí trước chưa? "
            "Chia sẻ góc nhìn ở bình luận để mọi người cùng cảnh giác nhé (lưu ý không đăng SĐT, STK, đường dẫn hay tên người thật)."
        ),
        "hashtags": ["#bóctrầnlừađảo", "#cảnhgiáclừađảo", "#vạnchuyện", "#antoànmạng", "#bẫythuhồitiền"],
        "tags": [
            "cảnh giác lừa đảo", "bóc trần lừa đảo", "vạn chuyện", "bẫy thu hồi tiền bị lừa",
            "lừa đảo lấy lại tiền", "bẫy lừa lần hai", "trình báo sớm", "an toàn mạng",
        ],
        "category": "Education (Giáo dục)",
        "playlist": "Hồ Sơ Bóc Trần Lừa Đảo – Phim Dài Chuyên Sâu",
        "thumbnail_sec": round(marks["mask_off"] + 1.5, 2),
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
