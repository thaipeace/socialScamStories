# -*- coding: utf-8 -*-
"""
Trình biên dịch `factory196/materialAndDraft/EP07/episode.json` – Tập EP07:
"Sau hai trăm triệu" (16:9 Long-form · v5-draft:
  - Làm mờ quá trình lừa lần 1 kéo dài 3 tuần, đẩy thẳng vào hậu quả cao trào;
  - Hồi 3 nhử từng đợt nhỏ (1tr -> 2tr -> 7tr -> 15tr -> 30tr) kèm bằng chứng mồi vô giá trị xác thực;
  - s12 chốt dứt khoát đúng bản chất thực dụng (hết tiền là cắt kết nối, không chọc tức thừa lời);
  - Cán bộ s15 chuẩn mực nghiệp vụ ("tiếp nhận ngay để phối hợp ngân hàng xác minh theo quy trình");
  - Kết mở s21b tối giản hoàn toàn câm: bóng lưng Ông Tám vẫy chào bạn già mới ở quán cà phê ven biển
    (địa bàn khác), trên bàn là màn hình ứng dụng quen thuộc đã sập ở Hồi 1;
  - Giữ trọn 11 thành quả pháp lý v2 và trục Ông 65t về hưu – Con gái 26t – Cháu trai 5t).

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
# 8 nhân vật = 8 voice hoàn toàn tách biệt trong 02_CAST/cast.json (100% gemini-3.8-flash-tts)
NOT_SHAKY = "tuyệt đối không giả giọng ông già run rẩy yếu ớt, không kéo dài chữ, không cải lương"
TAM_BASE = (
    "Giọng nam miền Nam Sài Gòn 60 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
    "trầm vang chắc khỏe kiểu người từng trải quen rộng ngoài đời, rõ chữ, tốc độ vừa phải, " + NOT_SHAKY
)
SPK = {
    "THANH": dict(
        speaker="ong_bay",
        voice="Algenib",
        label_short="ÔNG THÀNH",
        speaker_label="Ông Thành – người đàn ông 65 tuổi vừa về hưu, cả đời đi làm nên tự tin từng trải rồi dần sụp đổ",
        base=(
            "Giọng đàn ông miền Nam Sài Gòn 65 tuổi vừa về hưu, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
            "âm sắc trầm hơi khàn từng trải, đĩnh đạc tự tin và chắc chữ, tự nhiên như đời thực, " + NOT_SHAKY
        ),
    ),
    "TRANG": dict(
        speaker="chi_hai",
        voice="Sulafat",
        label_short="TRANG",
        speaker_label="Trang – con gái Ông Thành 26 tuổi, thực tế, thương ba, kiệm lời và không chì chiết",
        base=(
            "Giọng phụ nữ trẻ miền Nam Sài Gòn 26 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
            "giữ cố định một âm sắc ấm, trầm vừa, lễ phép nhưng chín chắn, nói gọn rõ chữ, tự nhiên như đời thực, " + NOT_SHAKY
        ),
    ),
    "BO": dict(
        speaker="be_tom",
        voice="Puck",
        label_short="BÉ BO",
        speaker_label="Bé Bo – cháu ngoại 5 tuổi (con trai của Trang), hồn nhiên, quấn ông ngoại",
        base=(
            "Giọng cậu bé trai 5 tuổi miền Nam Sài Gòn, phát âm chuẩn phương ngữ miền Nam, "
            "trong sáng, hồn nhiên, nói tốc độ vừa phải, rõ chữ, đồng nhất một tông giọng duy nhất, không nũng nịu giả tạo"
        ),
    ),
    "TAM": dict(
        speaker="anh_hai",
        voice="Orus",
        label_short="ÔNG TÁM",
        speaker_label="Ông Tám – bạn cũ 60 tuổi ngoài bàn cà phê sáng, nhân vật bí ẩn rút êm sau khi đã đủ",
        base=TAM_BASE,
    ),
    "TAM_P": dict(
        speaker="anh_hai",
        voice="Orus",
        af="phone",
        label_short="ÔNG TÁM",
        speaker_label="Ông Tám nói qua điện thoại",
        base=TAM_BASE,
    ),
    "TAM_MEM": dict(
        speaker="anh_hai",
        voice="Orus",
        af="memory",
        label_short="ÔNG TÁM (VỌNG)",
        speaker_label="Tiếng vọng lời hứa ở quán cà phê của Ông Tám trong ký ức của Ông Thành",
        base=TAM_BASE,
    ),
    "KHOA_P": dict(
        speaker="ke_ngot_ngao_nam",
        voice="Achird",
        af="phone",
        label_short="KHOA",
        speaker_label="Khoa – người lạ 31 tuổi tự xưng thuộc nhóm hỗ trợ lấy lại tiền, nói qua điện thoại",
        base=(
            "Giọng nam miền Nam Sài Gòn 31 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
            "âm sắc sáng gọn, mượt mà, lễ phép trơn tru, kiên nhẫn; lúc lật mặt thì lạnh băng sắc nhọn"
        ),
    ),
    "KHOA_ROOM": dict(
        speaker="ke_ngot_ngao_nam",
        voice="Achird",
        label_short="KHOA",
        speaker_label="Khoa trong căn phòng tối báo cáo lên đầu dây trên ở cảnh kết mở",
        base=(
            "Giọng nam miền Nam Sài Gòn 31 tuổi, phát âm chuẩn phương ngữ miền Nam, "
            "âm sắc sáng gọn, hạ giọng bình thản và lạnh nhạt như đang báo cáo công việc thường ngày"
        ),
    ),
    "NGOC_REC": dict(
        speaker="ke_ngot_ngao_nu",
        voice="Aoede",
        af="phone",
        label_short="GHI ÂM · NGỌC",
        speaker_label="Đoạn ghi âm cuộc gọi cũ của chuyên viên Ngọc (sàn đầu tư lạ) phát lại qua loa điện thoại",
        base=(
            "Giọng nữ miền Nam Sài Gòn 27 tuổi, phát âm chuẩn phương ngữ miền Nam, "
            "âm sắc ngọt ngào, thân mật, tự tin kiểu nhân viên chăm sóc khách hàng qua điện thoại"
        ),
    ),
    "CB": dict(
        speaker="chi_tu",
        voice="Zephyr",
        label_short="CÁN BỘ",
        speaker_label="Cán bộ tiếp nhận trình báo, 35 tuổi, điềm tĩnh, công tâm",
        base=(
            "Giọng phụ nữ miền Nam Sài Gòn 35 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
            "điềm tĩnh, rõ ràng, chuẩn mực, công tâm, không lên lớp hay mỉa mai, " + NOT_SHAKY
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
# ---- HOOK · 23:15 ĐÊM CẠN SẠCH TIỀN (00:00 – ~00:28) ----
amb("night_room", -1.5); bgm("suspense_pulse", -2.5)
scene("s00_hook_midnight", "assets/c00.jpg", "push", shake=0.2)
sfx("notification", 0.15, -2)
bubble("NHÓM HỖ TRỢ LẤY LẠI TIỀN", "Lệnh hoàn trả 200.000.000đ bị lỗi mã xác thực · Cần bổ sung 40.000.000đ",
       side="left", y=290, stamp="TREO LỆNH", dur=5.6, offset=0.2)
beat(1.8)
line("l01_thanh", "THANH", "Đủ rồi! Tôi vừa chuyển ba chục triệu cuối cùng xong, sao lại đòi thêm bốn chục triệu nữa?!",
     "khàn gắt, bức xúc dồn nén nhưng cố hạ giọng sợ con cháu trong phòng nghe thấy",
     sub="Đủ rồi! Tôi vừa chuyển 30 triệu cuối cùng xong, sao lại đòi thêm 40 triệu nữa?!")
line("l02_khoa", "KHOA_P", "Chú Thành bình tĩnh. Sai mã xác thực thì hệ thống khóa lệnh hoàn trả hai trăm triệu, bên em đâu mở được.",
     "mượt mà, lễ phép nhưng lạnh đều như quy trình sẵn",
     sub="Chú Thành bình tĩnh. Sai mã xác thực thì hệ thống khóa lệnh hoàn trả 200 triệu, bên em đâu mở được.")
line("l03_thanh", "THANH", "Tôi biết tụi cậu lừa tôi rồi! Tôi quen biết ngoài đời hông thiếu, tụi cậu trốn đâu tôi cũng tìm ra!",
     "giận dữ, cố giữ khí thế người từng trải nhưng giọng bắt đầu run", pause=0.2)

scene("s01_hook_freeze", "assets/c01.jpg", "tense", tr="flash_white", trd=0.25, shake=0.15)
mark("hook_freeze")
sfx("impact", 0.0, -3)
sfx("heartbeat", 0.3, -4.5, dur=2.4)
beat(2.8)

# ---- HỒI 1 · MỘT THÁNG TRƯỚC: VỪA VỀ HƯU, BÀN CÀ PHÊ SÁNG & HẬU QUẢ 200 TRIỆU ----
amb("room_tone", -2.5); bgm("warm_outro", -5.0)
scene("s02_retirement_plan", "assets/c02.jpg", "calm", tr="fade_black", trd=0.5)
chapter("HỒI 1 · MỘT THÁNG TRƯỚC", "VỪA VỀ HƯU & BÀN CÀ PHÊ SÁNG")
sfx("chapter_sting", -0.1, -5)
beat(1.0)
line("l05_thanh", "THANH", "Mới về hưu rảnh tay, gom hai trăm triệu sửa lại nhà, làm phòng riêng cho thằng Bo năm sau vô lớp Một.",
     "tự hào, giọng trầm ấm, chỉ tay lên bản vẽ sửa nhà",
     sub="Mới về hưu rảnh tay, gom 200 triệu sửa lại nhà, làm phòng riêng cho thằng Bo năm sau vô lớp Một.")
line("l06_bo", "BO", "Phòng mới có cái cửa sổ bự cho con để đồ chơi với học bài hông ông ngoại?",
     "hào hứng, ngước mắt tròn xoe hỏi ông ngoại")
line("l07_thanh", "THANH", "Có chứ cháu ngoại! Rảnh tay lướt mạng ông tính xoay thêm một cú cho dư dả, sửa xong vẫn còn tiền dưỡng già.",
     "cười sảng khoái đầy tự tin, xoa đầu cháu trai")
line("l08_trang", "TRANG", "Ba mới nghỉ, rảnh coi tin cho vui thôi nha ba. Tiền hưu cứ để yên ngân hàng, trên mạng giờ đủ thứ bẫy lắm.",
     "dịu dàng, thực tế, nhắc ba một câu nhẹ nhàng")
line("l08b_thanh", "THANH", "Trời, cả một đời ba đi làm, chuyện gì ba chưa gặp qua? Tới giờ con còn sợ ba bị gạt nữa hả?",
     "cười phẩy tay tự đắc, tin chắc vào kinh nghiệm sống cả đời mình", pause=0.5)

# Cài ngầm nhân vật bí ẩn Ông Tám: dò trọn hoàn cảnh, tiền hưu & tính cách từ bàn cà phê sáng
amb("crowd", -5.5); bgm("investigative_story", -4.5)
scene("s03_old_friends_cafe", "assets/c03.jpg", "hand", tr="dissolve", trd=0.45)
beat(0.8)
line("l09a_tam", "TAM", "Mới lãnh cục tiền hưu về, tính sửa nhà cho cháu ngoại rồi để tiền nằm không vậy hả Thành?",
     "nhâm nhi cà phê, hỏi thăm tự nhiên mà ánh mắt dò xét kỹ từng chi tiết")
line("l09_tam", "TAM", "Chơi với mày tao khoái cái tính sòng phẳng. Có chuyện gì cứ gọi một tiếng, mấy thằng em ngoài đời của tao lo liền.",
     "sang sảng, vỗ vai bạn cũ ra vẻ quen rộng trên bàn cà phê sáng")
line("l10_thanh", "THANH", "Sống tới tuổi này hơn nhau chỗ biết rộng, quen nhiều! Chứ đụng chuyện mà đi làm đơn chờ thủ tục tới chừng nào.",
     "cười tự đắc, nâng ly cà phê đầy tin tưởng vào mối quan hệ ngoài đời", pause=0.5)

# Làm mờ quá trình dẫn dụ 3 tuần – đẩy thẳng vào hậu quả cao trào mất 200 triệu (tránh cảm giác chuyển "cái èo")
amb("night_room", -2.5); bgm("tension_drone", -3.0)
scene("s04_first_trap_aftermath", "assets/c04.jpg", "push", tr="fade_black", trd=0.5)
sfx("glitch", 0.35, -3.5)
sfx("impact", 0.65, -3.5)
# Cài tên "Ngọc" – chuyên viên chăm sóc suốt 3 tuần của ứng dụng đầu tư lạ (trả ở s09, s09b và kết mở)
bubble("LỊCH SỬ NẠP · 3 TUẦN", "Nhiều đợt cộng dồn: 200.000.000đ · Chuyên viên chăm sóc: Ngọc",
       side="left", y=250, stamp="SAU BA TUẦN", dur=4.8, offset=0.25)
bubble("ỨNG DỤNG ĐẦU TƯ LẠ", "Tài khoản đã bị đóng băng · Không thể kết nối máy chủ",
       side="left", y=470, stamp="MẤT 200 TRIỆU", dur=5.2, offset=1.5)
beat(3.0)
line("l11_thanh", "THANH", "Ba tuần nay làm từng bước đều rút được lời… Sao vừa gom đủ hai trăm triệu chốt gói cuối là sập trang luôn?!",
     "bàng hoàng chết lặng dưới ánh màn hình, giọng hụt hơi vì cú sập đột ngột",
     sub="3 tuần nay làm từng bước đều rút được lời… Sao vừa gom đủ 200 triệu chốt gói cuối là sập trang luôn?!", pause=0.6)

# ---- HỒI 2 · CHÊ CÔNG AN, NHỜ BẠN CŨ & CÚ PHỦI TAY ----
amb("room_tone", -2.5); bgm("investigative_story", -3.5)
scene("s05_reject_police", "assets/c05.jpg", "tense", tr="fade_black", trd=0.45)
chapter("HỒI 2 · CÚ TÁT ĐẦU TIÊN", "NGƯỜI QUEN NGOÀI ĐỜI & CÁI TÀI KHOẢN MƯỢN TÊN")
sfx("chapter_sting", -0.1, -5)
beat(1.0)
line("l12_trang", "TRANG", "Ba dừng lại liền đi! Gọi tổng đài ngân hàng khóa giao dịch, rồi con chở ba ra công an trình báo ngay sáng nay.",
     "lo âu nhưng dứt khoát, nắm tay ba khuyên thật lòng")
line("l13_thanh", "THANH", "Báo công an?! Chờ thủ tục tới chừng nào? Rồi người ta cười vô mặt, nói ông già mới về hưu đã bị gạt!",
     "tự ái nóng nảy, sợ mất thể diện người cha từng trải, gạt phắt lời con gái")
line("l14_trang", "TRANG", "Hai trăm triệu là tiền cả đời ba làm cực khổ. Ngoài ngân hàng với công an, ai truy được tiền trên mạng hả ba?",
     "nhìn thẳng ba, giọng nghẹn nhẹ mà tỉnh táo",
     sub="200 triệu là tiền cả đời ba làm cực khổ. Ngoài ngân hàng với công an, ai truy được tiền trên mạng hả ba?")
line("l15_thanh", "THANH", "Tiền ba làm ra, tài khoản đứng tên ba, để ba tự lo! Cho ba ba ngày, ba nhờ chú Tám lần tới tận cửa.",
     "đứng bật dậy, cứng cỏi giữ sĩ diện người làm cha", pause=0.6)
beat(1.1)   # nhịp câm: Trang nhìn ba rất lâu, làm con không thể giật điện thoại hay nặng lời

amb("street", -5.0); bgm("investigative_story", -4.0)
scene("s06_meet_tam", "assets/c06.jpg", "calm", tr="fade_black", trd=0.4)
bubble("BIÊN LAI CHUYỂN KHOẢN", "Người nhận: ••••• (TK ••••) · Tổng cộng 3 tuần: 200.000.000đ",
       side="left", y=260, stamp="ĐƯA 5 TRIỆU ĐI HỎI", dur=5.4, offset=0.25)
beat(1.2)
line("l16_thanh", "THANH", "Chút tiền xăng xe cho mấy đứa nhỏ đi việc. Mày coi quen ai rành, lần giùm tao cái tài khoản này nha Tám.",
     "nôn nóng, đẩy phong bì tiền mặt qua bàn")
# Chi tiết cài ngầm Ông Tám: hỏi kiểm tra tình trạng báo công an và gia đình
line("l17a_tam", "TAM", "Mày chưa báo công an, cũng chưa nói kỹ với con Trang phải hông?",
     "hạ giọng nhẹ như hỏi thăm, ánh mắt dừng kỹ trên tờ biên lai")
line("l17b_thanh", "THANH", "Chưa, tao hẹn nó ba ngày tự lo.",
     "gật đầu chắc nịch vì sĩ diện")
line("l17c_tam", "TAM", "Ừ, để tao hỏi mấy đứa coi sao.",
     "cất gọn phong bì, nét mặt thoáng lạnh rồi điềm nhiên trở lại", pause=0.5)

amb("street", -4.5); bgm("tension_drone", -2.5)
scene("s07_tam_brushoff", "assets/c07.jpg", "push", tr="fade_black", trd=0.45)
mark("tam_betray")
sfx("phone_ring", 0.3, -4, dur=1.4)
beat(1.8)
line("l18_tam", "TAM_P", "Tao hỏi mấy đứa rành chuyện này rồi. Tài khoản kiểu đó toàn đứng tên người bán giấy tờ, lần theo chẳng tới đầu nậu.",
     "đổi hẳn thái độ sang xa cách lạnh nhạt, cố ý đẩy trách nhiệm gọn gàng")
line("l19_thanh", "THANH", "Vậy mày nhờ tụi nó lần tiếp giùm tao đi Tám! Tiền dưỡng già cả đời tao đó!",
     "sững sờ, giọng chới với hỏi dồn")
line("l20_tam", "TAM_P", "Dính lừa trên mạng là dính pháp luật, mấy đứa nó hông đụng đâu. Mày tự ra công an đi.",
     "phủi tay lạnh tanh đúng kiểu rút êm, nói xong cúp máy luôn", pause=0.3)
sfx("call_end", 0.0, -3)
beat(2.4)   # nhịp câm: không ai nhắc tới 5 triệu; Ông Thành nhìn màn hình tắt ngấm

# ---- HỒI 3 · CÁI BẪY LẦN HAI: NHỬ TỪNG ĐỢT NHỎ & ẢO GIÁC "TRONG LÒNG BÀN TAY" ----
amb("night_room", -2.0); bgm("tension_drone", -2.8)
scene("s08_search_alone", "assets/c08.jpg", "hand", tr="fade_black", trd=0.5)
chapter("HỒI 3 · CÁI BẪY LẦN HAI", "NHÓM LẤY LẠI TIỀN & MỒI NHỬ TỪNG BƯỚC")
sfx("chapter_sting", -0.1, -5)
sfx("typing", 0.4, -5.5, dur=1.2)
bubble("NHÓM HỖ TRỢ LẤY LẠI TIỀN", "Cam kết lấy lại tiền bị treo trên sàn · Không thu tiền công trước",
       side="left", y=260, stamp="QUẢNG CÁO", dur=5.2, offset=0.4)
bubble("BÌNH LUẬN DƯỚI BÀI ĐĂNG", "Cảm ơn nhóm đã lấy lại 180 triệu cho chú tôi sau 3 ngày!",
       side="left", y=480, stamp="TÀI KHOẢN ẢO", dur=4.8, offset=1.8)
beat(2.8)
line("l22_khoa", "KHOA_P", "Nói thật với chú Thành, chờ thủ tục lâu lắm. Bên em có đội kỹ thuật chuyên kéo tiền bị treo trên sàn về.",
     "mượt mà, lễ phép, vuốt đúng tâm lý muốn giải quyết gọn của người từng trải")
line("l23_thanh", "THANH", "Tôi mới mất hai trăm triệu xong, cậu đừng hòng dụ ông già này lần nữa. Tụi cậu có gì chứng minh làm được thật?",
     "cảnh giác cao độ, hỏi vặn sắc bén và đề phòng",
     sub="Tôi mới mất 200 triệu xong, cậu đừng hòng dụ ông già này lần nữa. Tụi cậu có gì chứng minh làm được thật?")
line("l24_khoa", "KHOA_P", "Chú cảnh giác là quá đúng. Bên em hông thu tiền công trước. Chú cứ gửi sao kê qua kiểm tra miễn phí.",
     "kiên nhẫn, bình tĩnh, không hề thúc ép để đánh gục sự đề phòng")
sfx("typing", 0.1, -5, dur=1.0)
sfx("message_send", 1.2, -4)
beat(1.8)

# Bước nhử 0 (miễn phí tên Ngọc) -> Bước nhử 1 (chỉ 1 triệu xem ảnh luồng tiền)
scene("s09_insider_detail", "assets/c09.jpg", "push", tr="dissolve", trd=0.45)
sfx("notification", 0.2, -3)
bubble("HỒ SƠ #094 · KIỂM TRA MIỄN PHÍ", "Khoanh nguồn tiền treo: 200.000.000đ · Chuyên viên bên sàn: Ngọc",
       side="left", y=250, stamp="KHỚP DỮ LIỆU", dur=5.6, offset=0.25)
beat(1.4)
line("l25_khoa", "KHOA_P", "Bên em kiểm tra xong rồi. Bên sàn đó, chuyên viên chăm sóc chú ba tuần nay tên Ngọc, đúng hông chú?",
     "tự tin, chậm rãi, cố ý buông chi tiết Ông Thành chưa từng gửi")
line("l26_thanh", "THANH", "Sao… sao cậu biết tên con nhỏ đó? Tôi đâu có gửi tin nhắn nào…",
     "sững người, nghi ngờ bắt đầu rạn nứt vì bất ngờ")
line("l26b_khoa", "KHOA_P", "Bên em vẫn chưa lấy công. Chú thử nạp một triệu phí trích cổng, coi ảnh luồng tiền rồi hãy tính tiếp.",
     "nhẹ tênh, hợp lý hóa khoản mồi siêu nhỏ để vượt qua cảnh giác",
     sub="Bên em vẫn chưa lấy công. Chú thử nạp 1 triệu phí trích cổng, coi ảnh luồng tiền rồi hãy tính tiếp.")
sfx("typing", 0.1, -5.5, dur=0.8)
sfx("bank_ting", 1.0, -3.5)
beat(1.2)

# Cảnh mới cực đắt: 1tr (ảnh luồng tiền che số) -> 2tr (chat cũ + phát lại ghi âm cũ của Ngọc) -> 7tr (mở cổng giải tỏa)
scene("s09b_bait_proof", "assets/c09b.jpg", "push", tr="dissolve", trd=0.45)
mark("bait_proof")
sfx("bank_ting", 0.15, -3.5)
sfx("notification", 0.55, -3)
bubble("GÓI TRÍCH DỮ LIỆU · 1TR -> 2TR", "Ảnh luồng tiền (TK •••••) · Lịch sử chat cũ · Ghi âm cuộc gọi với Ngọc",
       side="left", y=245, stamp="BẰNG CHỨNG MỒI", dur=6.0, offset=0.25)
beat(1.3)
line("l26d_ngoc_rec", "NGOC_REC", "Chú Thành yên tâm, chốt đủ hai trăm triệu là tối nay rút gốc luôn nha chú.",
     "giọng ghi âm cuộc gọi cũ phát lại từ loa điện thoại, ngọt ngào quen thuộc",
     sub="[Ghi âm cũ] Chú Thành yên tâm, chốt đủ 200 triệu là tối nay rút gốc luôn nha chú.", pause=0.45)
line("l26e_thanh", "THANH", "Trời… cả đoạn ghi âm bữa trước tôi nói chuyện với nó mà tụi cậu cũng kéo ra được! Coi như trong lòng bàn tay rồi!",
     "mắt sáng rực, xúc động tin sái cổ rằng tiền đã nắm chắc trong tay", pause=0.3)
line("l27_khoa", "KHOA_P", "Mọi thứ nằm gọn trong tay rồi chú. Lệnh khóa giữ hai mươi bốn tiếng, chú đóng nốt bảy triệu mở cổng giải tỏa nha chú.",
     "êm ái, dứt khoát đẩy lên đợt 7 triệu (tổng 1 + 2 + 7 = 10 triệu)",
     sub="Mọi thứ nằm gọn trong tay rồi chú. Lệnh khóa giữ 24 tiếng, chú đóng nốt 7 triệu mở cổng giải tỏa nha chú.")
bubble("TỔNG CÁC ĐỢT NHỬ BAN ĐẦU", "Trích luồng tiền: -1tr · Chat & ghi âm: -2tr · Mở cổng: -7tr (= -10.000.000đ)",
       side="left", y=260, stamp="ĐÃ ĐÓNG 10 TRIỆU", dur=3.4, offset=0.15)
sfx("typing", 0.1, -5.5, dur=0.9)
sfx("bank_ting", 1.1, -3.5)
beat(3.6)

# Trọng tâm tâm lý: đã nghi ngờ nhưng không thể dừng vì "chạy tới 95%", sunk cost 10tr & thể diện trước con gái
amb("night_room", -1.8); bgm("tension_drone", -2.0)
scene("s10_doubt_and_lie", "assets/c10.jpg", "tense", tr="fade_black", trd=0.45)
mark("sunk_cost_lie")
sfx("notification", 0.2, -3.5)
bubble("LỆNH CHỜ GIẢI NGÂN #094 · 95%", "Biên bản treo 200.000.000đ (mã cổng che mờ) · Bổ sung 15.000.000đ phí xác minh",
       side="left", y=250, stamp="PHÁT SINH PHÍ", dur=5.6, offset=0.25)
beat(1.0)
line("l28_thanh", "THANH", "Khoan đã! Từ một triệu, hai triệu, bảy triệu… sao nay lại đẻ thêm mười lăm triệu?! Tụi cậu giở trò phải hông?",
     "nghi ngờ thật sự, giọng gắt dồn lên nhưng vẫn nén âm lượng vì đêm khuya",
     sub="Khoan đã! Từ 1 triệu, 2 triệu, 7 triệu… sao nay lại đẻ thêm 15 triệu?! Tụi cậu giở trò phải hông?")
line("l29_khoa", "KHOA_P", "Hồ sơ chạy tới chín mươi lăm phần trăm rồi chú. Chú nghi thì cứ hủy, tiếc hai trăm triệu với mười triệu vừa đóng thôi.",
     "lạnh tĩnh, không nài nỉ, khóa chặt nỗi sợ mất trắng",
     sub="Hồ sơ chạy tới 95% rồi chú. Chú nghi thì cứ hủy, tiếc 200 triệu với 10 triệu vừa đóng thôi.")
sfx("heartbeat", 0.1, -4, dur=2.2)
beat(2.0)
line("l30_trang", "TRANG", "Ba ơi, khuya rồi vô ngủ đi ba. Mai là hết ba ngày rồi, bên chú Tám lo tới đâu rồi ba?",
     "vọng nhẹ qua khe cửa phòng, dịu dàng lo lắng và vẫn tin ba", pause=0.5)
line("l31_thanh", "THANH", "Ờ… sắp xong rồi con. Con với thằng Bo ngủ trước đi.",
     "nuốt khan, giọng khô khốc nói dối vì không dám thú thật trước mặt con gái", pause=0.3)
sfx("typing", 0.1, -5.5, dur=1.0)
sfx("bank_ting", 1.2, -3.5)
beat(1.8)

# Cảnh câm: Khoa show màn hình lệnh cộng +200tr (không mã tra soát) -> tháo đồng hồ cầm đồ gom 30tr cuối (tổng 55tr)
amb("street", -5.5); bgm("tension_drone", -2.2)
scene("s11_pawn_watch", "assets/c11.jpg", "push", tr="fade_black", trd=0.5)
bubble("LỆNH HOÀN TIỀN #094 · CHỜ DUYỆT", "Hiển thị +200.000.000đ chờ vào TK (không mã tra soát) · Nộp 30.000.000đ giải ngân",
       side="left", y=245, stamp="CHỈ CÒN 1 BƯỚC", dur=3.0, offset=0.25)
bubble("LỊCH SỬ CHUYỂN KHOẢN · 5 ĐỢT", "1tr + 2tr + 7tr + 15tr + 30tr · Tổng lần hai: -55.000.000đ",
       side="left", y=245, stamp="CẠN SẠCH TIỀN", dur=3.5, offset=3.4)
sfx("bank_ting", 3.5, -3.5)
sfx("heartbeat", 4.1, -4.5, dur=2.4)
beat(7.1)

# Cắt kết nối dứt khoát (nối tiếp ngay câu cảnh cáo cuối Hook; hết giá trị khai thác là cắt rụp, không thừa lời)
amb("night_room", -1.5); bgm("tension_drone", SILENT)
scene("s12_mask_off", "assets/c12.jpg", "tense", tr="fade_black", trd=0.4)
mark("mask_off")
beat(0.7)
line("l32_khoa", "KHOA_P", "Chú hông đóng đủ bốn chục triệu trong tối nay thì hồ sơ tự hủy. Bên em hết hỗ trợ.",
     "lạnh đều, vô cảm tuyệt đối, chốt gọn dứt khoát không đôi co",
     sub="Chú hông đóng đủ 40 triệu trong tối nay thì hồ sơ tự hủy. Bên em hết hỗ trợ.", pause=0.25)
sfx("call_end", 0.0, -2.5)
sfx("impact", 0.3, -3)
bubble("HỆ THỐNG TIN NHẮN", "Không thể gửi tin nhắn · Trang và tài khoản đã bị xóa",
       side="left", y=290, stamp="ĐÃ CHẶN", dur=3.2, offset=0.25)
beat(3.6)

# ---- HỒI 4 · CUỘC GỌI KHÔNG AI NGHE & TRÌNH BÁO MUỘN ----
amb("night_room", -2.0); bgm("investigative_story", -6.5)
scene("s13_unanswered_call", "assets/c13.jpg", "pull", tr="fade_black", trd=0.55)
chapter("HỒI 4 · TRÌNH BÁO MUỘN MÀNG", "CUỘC GỌI KHÔNG AI NGHE & SỰ THẬT")
sfx("chapter_sting", -0.1, -5)
sfx("phone_ring", 0.5, -4, dur=2.6)
bubble("DANH BẠ · ÔNG TÁM", "Đang gọi… Không có câu trả lời",
       side="left", y=260, stamp="KHÔNG BẮT MÁY", dur=5.2, offset=0.6)
beat(3.2)
sfx("call_end", 0.0, -4)
beat(0.5)
line("l33_tam_mem", "TAM_MEM", "Có chuyện gì cứ gọi một tiếng, mấy thằng em ngoài đời của tao lo liền.",
     "vang vọng từ ký ức bàn cà phê, lạnh lẽo và chua chát", pause=0.8)
beat(1.2)

amb("night_room", -2.5); bgm("warm_outro", -7.5)
scene("s14_bare_wrist_confession", "assets/c14.jpg", "calm", tr="dissolve", trd=0.5)
mark("daughter_confession")
beat(1.4)
line("l34_trang", "TRANG", "Hết sạch rồi hả ba?",
     "giọng rất khẽ, nghẹn nhẹ, không một lời trách móc", pause=0.7)
line("l35_thanh", "THANH", "Hai trăm triệu tiền dưỡng già… cộng thêm sáu chục triệu tiền phòng thân với cả chiếc đồng hồ… mất hết rồi con ơi.",
     "gục đầu, giọng khàn vỡ ra lần đầu tiên trước mặt con gái",
     sub="200 triệu tiền dưỡng già… cộng thêm 60 triệu tiền phòng thân với cả chiếc đồng hồ… mất hết rồi con ơi.", pause=1.0)
beat(1.0)
line("l36_trang", "TRANG", "Giờ ba gọi tổng đài ngân hàng liền đi. Sáng mai con chở ba ra công an.",
     "chậm rãi, xót xa nhưng vững vàng nắm chặt tay ba", pause=0.8)

amb("office", -4.5); bgm("investigative_story", -5.5)
scene("s15_police_truth", "assets/c15.jpg", "calm", tr="fade_black", trd=0.5)
mark("police_truth")
beat(1.0)
line("l37_cb", "CB", "Chú để gần năm ngày mới trình báo. Hai trăm triệu đầu chuyển đi lâu quá, xác minh khó hơn nhiều rồi.",
     "điềm tĩnh, nghiêm túc, rõ từng chữ, không mỉa mai",
     sub="Chú để gần năm ngày mới trình báo. 200 triệu đầu chuyển đi lâu quá, xác minh khó hơn nhiều rồi.", pause=0.4)
line("l38_thanh", "THANH", "Tôi có mấy hình luồng tiền với ghi âm cũ nhóm kia gửi… còn mấy khoản mới nộp thì sao cô?",
     "ôm chút hy vọng cuối, chìa màn hình rồi cúi mặt giọng nghẹn nhỏ", pause=0.3)
line("l39a_cb", "CB", "Mấy khoản mới chuyển chú đưa đủ sao kê, chúng tôi tiếp nhận ngay để phối hợp ngân hàng xác minh theo quy trình.",
     "dứt khoát, chuẩn mực nghiệp vụ, bắt tay vào việc", pause=0.3)
line("l39b_cb", "CB", "Còn hình che số với ghi âm cũ không đủ cơ sở xác thực bên kia. Nhử phí từng đợt nhỏ, đó là lừa lần hai.",
     "trầm tĩnh, thẳng thắn, không lên lớp", pause=0.8)
beat(1.4)

# ---- HỒI 5 · BẢN VẼ TRONG HỘC TỦ & CÂU HỎI CỦA CHÁU NGOẠI ----
amb("street", -5.5); bgm("warm_outro", -6.5)
scene("s16_drawer_seen", "assets/c16.jpg", "pull", tr="fade_black", trd=0.55)
chapter("HỒI 5 · ĐỐI DIỆN SỰ THẬT", "BẢN VẼ TRONG HỘC TỦ")
sfx("chapter_sting", -0.1, -5)
bubble("ÔNG TÁM", "Tám ơi, tao đang kẹt xoay tiền, mày cho tao mượn tạm ít bữa…",
       side="left", y=270, stamp="ĐÃ XEM · 3 NGÀY TRƯỚC", dur=5.0, offset=0.6)
beat(5.8)   # cảnh câm: Ông Thành cuộn bản vẽ sửa nhà cất sâu vô hộc tủ gỗ cũ, đóng ngăn kéo

amb("room_tone", -3.0); bgm("warm_outro", -5.5)
scene("s17_grandson_question", "assets/c17.jpg", "push", tr="dissolve", trd=0.45)
mark("grandson_q")
beat(0.8)
line("l40_bo", "BO", "Ông ngoại ơi, chừng nào chú thợ qua làm phòng mới có cửa sổ cho con học lớp Một hả ông?",
     "trong trẻo, hồn nhiên, kéo gấu áo ông ngoại hỏi khẽ", pause=1.2)

scene("s18_face_the_truth", "assets/c18.jpg", "calm", tr="dissolve", trd=0.45)
beat(1.1)
line("l41_thanh", "THANH", "Chắc còn lâu lắm con… Ông ngoại tính sai rồi. Nhưng năm sau con vô lớp Một, ông vẫn tập viết với con mỗi tối.",
     "ngồi ngang tầm cháu, mắt đỏ hoe mà dịu lại, giọng khàn nén xúc động xoa đầu cháu trai", pause=1.0)
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

# ---- KẾT MỞ · CÙNG MỘT ĐẦU MỐI & NHÂN VẬT BÍ ẨN ÔNG TÁM ----
amb("night_room", -3.0); bgm("tension_drone", -1.2)
scene("s21_scam_ring_coda", "assets/c19.jpg", "push", tr="fade_black", trd=0.45)
sfx("typing", 0.15, -5, dur=1.2)
bubble("HỒ SƠ TUẦN NÀY", "Vòng 1 (3 tuần): -200.000.000đ  ->  Vòng 2 (5 đợt): +55.000.000đ",
       side="left", y=250, stamp="CHUYỂN VÒNG 2", dur=5.6, offset=0.5)
beat(1.6)
mark("ring_coda")
line("l43_khoa_coda", "KHOA_ROOM", "Hồ sơ hai trăm triệu con Ngọc chuyển qua, nhử năm đợt bên em chốt thêm năm mươi lăm triệu rồi anh.",
     "bình thản báo cáo như xong một đơn hàng",
     sub="Hồ sơ 200 triệu con Ngọc chuyển qua, nhử 5 đợt bên em chốt thêm 55 triệu rồi anh.", pause=0.25)

# Chuyển liền sang cú lật tối giản hoàn toàn câm: quán cà phê ven biển (địa bàn khác), bóng lưng Ông Tám vẫy chào bạn già mới,
# trên bàn là chiếc điện thoại hiện giao diện ứng dụng quen thuộc đã sập ở Hồi 1
amb("street", -5.5); bgm("tension_drone", -0.8)
scene("s21b_tam_coda", "assets/c19b.jpg", "push", tr="dissolve", trd=0.35)
mark("tam_twist")
sfx("heartbeat", 0.6, -4.5, dur=2.6)
beat(4.4)

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


_desc = [(0.0, "Mở đầu – 23:15 sau khi mất hai trăm triệu")]
_desc += [(c["start"] - 0.2, f"{c['kicker'].split('·')[0].strip().title()} – {c['title'].capitalize()}")
          for c in chapters if c["kicker"]]
_desc += [(marks["rf_start"], "Nhớ kỹ – 5 nguyên tắc tránh bẫy lừa lần hai")]
_desc += [(marks["ring_coda"] - 1.5, "Kết mở – Cùng một đầu mối & bóng lưng quen thuộc")]
desc_chapters = "\n".join(f"{mmss(max(0.0, s))} {label}" for s, label in sorted(_desc))

episode = {
    "episode_id": "EP07",
    "slug": "SauHaiTramTrieu",
    "title": "Sau hai trăm triệu",
    "version": "v5-draft",
    "scam_family": "MIX-RECOVERY – Bẫy lừa lần hai: mất 200 triệu sau 3 tuần dẫn dụ, người bạn bàn cà phê sáng rút êm, nhóm tự xưng lấy lại tiền nhử phí từng đợt nhỏ bằng ảnh che số và ghi âm cũ",
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
            "AI HỨA CHẮC KÉO TIỀN VỀ RỒI NHỬ PHÍ TỪNG ĐỢT: Dù bắt đầu chỉ 1–2 triệu hay xưng nhóm hỗ trợ, chuyên gia, đó vẫn là bẫy lừa lần hai",
            "NGƯỜI QUEN NGOÀI ĐỜI KHÔNG TRUY ĐƯỢC TIỀN: Truy vết dòng tiền là việc của ngân hàng và cơ quan điều tra; cẩn trọng cả với người dò hỏi hoàn cảnh gia đình",
            "ẢNH CHE SỐ, TIN NHẮN CŨ, GHI ÂM CŨ KHÔNG XÁC THỰC ĐƯỢC BÊN KIA: Kẻ gian có thể chung một đầu mối với nhóm đã lừa bạn lần đầu",
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
            {"start": marks["bait_proof"] - 0.2, "end": marks["bait_proof"] + 12.0, "bgm_db": -11, "amb_db": -7},
            {"start": marks["sunk_cost_lie"] - 0.2, "end": marks["sunk_cost_lie"] + 12.0, "bgm_db": -10, "amb_db": -6},
            {"start": marks["mask_off"] - 0.2, "end": marks["mask_off"] + 10.0, "bgm_db": -18, "amb_db": -10},
            {"start": marks["daughter_confession"] - 0.2, "end": marks["daughter_confession"] + 14.0, "bgm_db": -12, "amb_db": -7},
            {"start": marks["police_truth"] - 0.2, "end": marks["police_truth"] + 16.0, "bgm_db": -12, "amb_db": -8},
            {"start": marks["grandson_q"] - 0.2, "end": marks["black_text"] - 0.2, "bgm_db": -11, "amb_db": -7},
            {"start": marks["ring_coda"] - 0.2, "end": marks["disc_start"] - 0.2, "bgm_db": -10, "amb_db": -7},
            {"start": marks["disc_start"], "end": total - 0.05},
        ],
    },
    "forbidden_terms": [],
    "publish": {
        "titles": [
            "Mất 200 Triệu Tiền Dưỡng Già, Rồi Mất Thêm 60 Triệu Để 'Lấy Lại' – Bẫy Lừa Lần Hai | Bóc Trần Lừa Đảo",
            "Sau Hai Trăm Triệu: Khi Nỗi Xấu Hổ Khiến Người Cha Tự Nộp Tiền Lần Hai | Bóc Trần Lừa Đảo",
            "Ghi Âm Cũ, Ảnh Luồng Tiền & Cái Bẫy Lấy Lại Tiền Trên Mạng | Bóc Trần Lừa Đảo",
        ],
        "description": (
            "Vừa về hưu ở tuổi 65, rảnh rỗi lướt mạng và tin vào kinh nghiệm cả một đời đi làm, ông Thành mất sạch 200 triệu đồng tiền dưỡng già "
            "sau ba tuần bị dẫn dụ vào một ứng dụng đầu tư lạ. "
            "Ngại mất thể diện trước con gái, ông gạt lời khuyên trình báo, nhờ bạn cũ ngoài đời rồi tin một nhóm tự xưng lấy lại tiền trên mạng "
            "khi chúng nhử từng đợt nhỏ bằng ảnh luồng tiền che số, tin nhắn cũ và cả đoạn ghi âm cuộc gọi cũ.\n\n"
            "⏱️ Các hồi trong phim:\n" + desc_chapters
        ),
        "pinned_comment": (
            "📌 Hãy gửi tập phim này cho ba mẹ hoặc người thân trong nhà cùng xem nhé. "
            "Cảnh cuối phim có chi tiết nào khiến bạn giật mình nhận ra không? "
            "Chia sẻ góc nhìn ở bình luận để mọi người cùng cảnh giác (lưu ý không đăng SĐT, STK, đường dẫn hay tên người thật)."
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
