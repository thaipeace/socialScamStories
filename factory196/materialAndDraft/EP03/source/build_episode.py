# -*- coding: utf-8 -*-
"""Builder cho EP03 (factory196) – sinh episode.json từ danh sách sự kiện.

Chạy lại sau Gate 2: nếu có tts_manifest_gate2.json, thời lượng thật của từng câu
được dùng để dàn lại toàn bộ timeline (Real-TTS Retiming) – cảnh, chương, bubble,
callout, foley, red_flags, disclaimer, chapters trong description, thumbnail.

    python3 factory196/materialAndDraft/EP03/source/build_episode.py
"""
from __future__ import annotations

import json
from pathlib import Path
from PIL import Image

EP_DIR = Path(__file__).resolve().parent.parent
TTS_MANIFEST = EP_DIR / "audio" / "tts" / "tts_manifest_gate2.json"
OUT = EP_DIR / "episode.json"

for sub in ("assets", "audio/tts", "audio/sfx", "audio/bgm", "audio/mix", "clearance", "script", "source"):
    (EP_DIR / sub).mkdir(parents=True, exist_ok=True)

# Tạo sẵn ảnh đen c18.jpg cho cảnh CUT TO BLACK
black_img = EP_DIR / "assets" / "c18.jpg"
if not black_img.is_file():
    Image.new("RGB", (1920, 1080), (6, 8, 14)).save(black_img, quality=92)

SEC_PER_WORD = 0.35
LINE_BASE = 0.42
GAP = 0.32            # nghỉ giữa hai câu
SCENE_LEAD = 0.32     # cảnh lên hình trước tiếng (0.25s - 0.4s theo Harness)
WINDOW_MARGIN = 1.6   # cửa sổ cho phép TTS dài hơn ước tính

real = {}
if TTS_MANIFEST.is_file():
    for ln in json.loads(TTS_MANIFEST.read_text(encoding="utf-8")).get("lines", []):
        dur_s = ln.get("duration_sec") or ln.get("metrics", {}).get("duration_sec")
        if ln.get("engine") != "placeholder" and dur_s:
            real[ln["line_id"]] = float(dur_s)

# ---------------------------------------------------------------- speakers (Tách biệt hoàn toàn âm sắc)
SPK = {
    "HG": dict(
        speaker="anh_hai",
        voice="Orus",
        label_short="HOÀNG",
        speaker_label="Hoàng – lập trình viên 32 tuổi",
        base="Giọng nam miền Nam Sài Gòn 32 tuổi, dân kỹ thuật điềm tĩnh, rõ chữ, tự nhiên đời thường",
    ),
    "L": dict(
        speaker="chi_ba",
        voice="Kore",
        label_short="LAN",
        speaker_label="Lan – vợ Hoàng",
        base="Giọng phụ nữ miền Nam Sài Gòn 30 tuổi, ấm áp, thực tế, tự nhiên như đời thực",
    ),
    "TOM": dict(
        speaker="be_tom",
        voice="Puck",
        label_short="BÉ TOM",
        speaker_label="Bé Tom – con trai 7 tuổi",
        base="Giọng cậu bé trai 7 tuổi người miền Nam, trong sáng, lễ phép, háo hức",
    ),
    "HA": dict(
        speaker="ke_ngot_ngao_nu",
        voice="Aoede",
        label_short="NHÂN SỰ HÀ",
        speaker_label="Hà – Nhân sự vòng 1 Tập đoàn X",
        af="phone",
        base="Giọng nữ miền Nam Sài Gòn 28 tuổi, nhân sự tuyển dụng online, ngọt ngào, chuyên nghiệp, nhịp nhanh",
    ),
    "KH": dict(
        speaker="ke_gia_danh",
        voice="Fenrir",
        label_short="QUẢN LÝ KHẢI",
        speaker_label="Khải – Quản lý dự án Bảo an xã hội",
        af="phone",
        base="Giọng nam miền Nam Sài Gòn 40 tuổi, trầm, đĩnh đạc, uy quyền kiểu quản lý dự án",
    ),
    "DUC": dict(
        speaker="ke_ngot_ngao_nam",
        voice="Achird",
        label_short="ỨNG VIÊN 04",
        speaker_label="Đức – Ứng viên số 04 (quân xanh)",
        af="phone",
        base="Giọng nam thanh niên miền Nam 25 tuổi, tông cao, nhanh nhảu, hào hứng tạo hiệu ứng đám đông",
    ),
    "TN": dict(
        speaker="thang_tun",
        voice="Puck",
        label_short="THANH NIÊN BÀN BÊN",
        speaker_label="Thanh niên bàn bên ở quán nước",
        base="Giọng nam thanh niên miền Nam 23 tuổi, lo âu, run rẩy vì đang bị kẹt tiền",
    ),
    "AI": dict(
        speaker="chi_tu",
        voice="Zephyr",
        label_short="TRỢ LÝ AI",
        speaker_label="Trợ lý AI",
        base="Giọng nữ miền Nam Sài Gòn 30 tuổi, trợ lý AI điềm tĩnh, trung tính, phân tích rõ ràng, mạch lạc, tốc độ vừa phải",
    ),
    "N": dict(speaker="nguoi_boc_tran"),
}


def mo(kind: str) -> dict:
    return {
        "tense": {"scale": [1.04, 1.14], "focus": [[0.5, 0.5], [0.47, 0.45]], "wobble": "tense"},
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


def bubble(sender, text, side="left", y=360, stamp="", dur=4.5, offset=0.0):
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
# ---- HOOK (00:00 - 00:22) ----
amb("office", -2.0); bgm("suspense_pulse", -1.0)
scene("s01_hook_ting", "assets/c01.jpg", "tense", shake=0.3)
sfx("bank_ting", 0.1, -3)
bubble("NGÂN HÀNG X", "TK …4910  +120.000 VND", side="right", y=280, stamp="TIỀN VÀO", dur=4.2, offset=0.1)
sfx("notification", 0.9, -4)
bubble("HỆ THỐNG BẢO AN", "Nhiệm vụ cuối: Chuyển 200.000 VND để kích hoạt điểm trên hệ thống xã hội bảo an (Còn 01:00).",
       side="left", y=440, stamp="PHÚT 89", dur=5.8, offset=0.9)
beat(0.25)
line("l01_khai", "KH", "Còn anh Hoàng thôi! Hết một phút hệ thống tự hủy hồ sơ nha!", "thúc ép, dồn dập")
line("l02_duc", "DUC", "Em chuyển hai trăm ngàn xong rồi anh ơi! Lên điểm liền luôn!", "khoe khoang, hào hứng",
     sub="Em chuyển 200.000đ xong rồi anh ơi! Lên điểm liền luôn!")
sfx("impact", 0.0, -4)
scene("s02_hook_finger", "assets/c02.jpg", "push", tr="flash_white", trd=0.25)
line("l03_hoang", "HG", "Nhận trăm hai rồi… chuyển lại hai trăm thì cùng lắm lỗ tám chục ngàn.",
     "ngập ngừng, tự nhủ", sub="Nhận 120 ngàn rồi… chuyển lại 200 ngàn thì cùng lắm lỗ 80 ngàn.")
line("l03b_hoang", "HG", "Hay cứ thử coi tụi nó diễn trò gì?", "tò mò, chần chừ")
mark("freeze")
line("l04_narr", "N", "Đi phỏng vấn được chuyển nóng một trăm hai mươi ngàn.",
     sub="Đi phỏng vấn được chuyển nóng 120.000đ.")
line("l04b_narr", "N", "Nhưng nếu tặc lưỡi bỏ ra hai trăm ngàn chỉ để xem kịch, cái giá ở phút thứ chín mươi sẽ không dừng ở đó.",
     sub="Nhưng nếu tặc lưỡi bỏ 200.000đ để 'xem kịch', cái giá ở phút thứ 90 sẽ không dừng ở đó.")
sfx("riser", -1.2, -5, dur=1.2)
beat(0.4)

# ---- HỒI 1: PHÒNG PHỎNG VẤN ĐÔNG NGƯỜI & MÀN ĐỔI SẾP ----
# Nhịp 1: Áp lực ứng viên mồi
amb("room_tone", -1.5); bgm("investigative_story", -1.5)
scene("s03_christmas_morning", "assets/c03.jpg", "calm", tr="fade_black", trd=0.4)
chapter("HỒI 1 · SÁNG GIÁNG SINH 25/12", "PHÒNG PHỎNG VẤN ĐÔNG NGƯỜI & MÀN “ĐỔI SẾP”")
sfx("chapter_sting", -0.1, -4)
beat(0.2)
line("l05_tom", "TOM", "Ba ơi, sáng Giáng Sinh ba hứa chở con đi chơi mà!", "nhõng nhẽo, háo hức")
line("l06_lan", "L", "Chín rưỡi mình đi nha anh.", "dịu dàng nhắc chồng", sub="9 rưỡi mình đi nha anh.")
line("l07_hoang", "HG", "Cho ba đúng một tiếng. Bên Tập đoàn Viễn thông X hẹn phỏng vấn lập trình viên rồi.", "ấm áp, tự tin")

amb("office", -2.0)
scene("s04_meeting_grid", "assets/c04.jpg", "hand", tr="dissolve", trd=0.35)
sfx("notification", 0.1, -5)
line("l08_ha", "HA", "Vòng một: đọc tài liệu trong mười phút và trả lời câu hỏi chung. Ai nhanh nhất được cộng điểm ưu tiên!",
     "nhanh, chuyên nghiệp")
scene("s05_ai_helper", "assets/c06.jpg", "calm", tr="dissolve", trd=0.3)
sfx("typing", 0.1, -6, dur=1.6)
line("l09_hoang", "HG", "Nhờ Trợ lý AI tóm tắt nhanh bộ tài liệu này coi.", "tập trung, nhanh nhạy")
line("l09b_ai", "AI", "Đã phân tích xong tài liệu. Đây là ba ý cốt lõi và đáp án để bạn trả lời vòng một.",
     "điềm tĩnh, rõ ràng")
scene("s06_stolen_mic", "assets/c05.jpg", "tense", tr="dissolve", trd=0.25)
line("l10_duc", "DUC", "Em xin trả lời câu hỏi vòng một theo đúng ba mục trong tài liệu tập đoàn ạ!", "nói cực nhanh, cướp lời")
line("l11_ha", "HA", "Xuất sắc! Ứng viên số bốn và anh Hoàng vượt qua vòng một!", "khen ngợi hồ hởi")

# Nhịp 2: Đổi người sang Quản lý dự án Bảo an xã hội & Bài test tương tác tài chính thật 120K
scene("s07_manager_khai", "assets/c07.jpg", "push", tr="dissolve", trd=0.35)
sfx("glitch", 0.1, -5)
line("l12_ha", "HA", "Vòng hai sẽ do anh Khải, Quản lý dự án Hệ thống Xã hội Bảo an trực tiếp đánh giá.",
     "trang trọng giới thiệu")
line("l13_khai", "KH", "Chào các bạn. Vòng hai có tương tác tài chính thật nhằm đánh giá khả năng quản trị ứng biến và kiến thức tài chính của ứng viên.",
     "trầm, uy quyền, chuyên nghiệp")
line("l13b_khai", "KH", "Mời các bạn vào nền tảng dự án. Hệ thống sẽ chuyển hỗ trợ mỗi bạn một trăm hai mươi ngàn để thực hiện thao tác.",
     "đĩnh đạc, dẫn dụ", sub="Mời vào nền tảng dự án. Hệ thống sẽ chuyển hỗ trợ mỗi bạn 120.000đ để thực hiện thao tác.")
scene("s08_broken_subpage", "assets/c08.jpg", "hand", tr="dissolve", trd=0.3)
callout("ĐỔI SANG “QUẢN LÝ DỰ ÁN”  ·  LÝ GIẢI “TEST TƯƠNG TÁC TÀI CHÍNH THẬT”", "warning", dur=7.5, offset=0.2)
line("l14_hoang", "HG", "Ủa, tuyển lập trình viên mà qua vòng hai lại kêu vào web dự án Bảo an xã hội? Trang con còn sai chính tả nữa…",
     "nhíu mày, gõ hỏi AI")
line("l14b_ai", "AI", "Hãy cẩn thận. Tuyển vị trí kỹ thuật nhưng lại dẫn sang trang web lỗi chính tả và lồng ghép thao tác tiền bạc là dấu hiệu bất thường.",
     "cảnh báo điềm tĩnh")

# ---- HỒI 2: 120 NGÀN TIỀN THẬT & CÚ CHỐT PHÚT 89 ----
# Nhịp 3: 120.000đ tiền thật đánh sập nghi ngờ & Cái bẫy "Lỗ 80 ngàn coi kịch"
amb("office", -1.5); bgm("tension_drone", -1.0)
scene("s09_real_120k", "assets/c09.jpg", "push", tr="fade_black", trd=0.35, shake=0.25)
chapter("HỒI 2 · PHÚT THỨ 85", "120 NGÀN TIỀN THẬT & LỆNH CHUYỂN NGƯỢC 200 NGÀN")
sfx("chapter_sting", -0.1, -4)
sfx("bank_ting", 0.25, -3)
bubble("NGÂN HÀNG X", "TK …4910  +120.000 VND (Hỗ trợ vòng 2)", side="right", y=340, stamp="TIỀN THẬT", dur=4.8, offset=0.25)
beat(0.3)
line("l15_hoang", "HG", "Ủa… họ chuyển một trăm hai mươi ngàn hỗ trợ vòng hai thật luôn?", "bất ngờ, hết nghi ngờ",
     sub="Ủa… họ chuyển 120.000đ hỗ trợ vòng 2 thật luôn?")
line("l16_duc", "DUC", "Em nhận được trăm hai rồi anh Khải ơi! Dự án lớn có khác, uy tín quá!", "reo lên phấn khích")
scene("s10_khai_200k_trap", "assets/c07.jpg", "push", tr="dissolve", trd=0.3)
line("l17_khai", "KH", "Giờ để chứng minh khả năng quản lý và giao tiếp, mỗi bạn chuyển ngược hai trăm ngàn vào tài khoản chỉ định.",
     "nghiêm giọng, dứt khoát", sub="Để chứng minh khả năng quản lý và giao tiếp, mỗi bạn chuyển ngược 200.000đ vào tài khoản chỉ định.")
line("l18_khai", "KH", "Tiền này được ghi nhận thành điểm trên hệ thống xã hội bảo an, rút ra bất cứ lúc nào.",
     "trấn an mượt mà")
line("l19_duc", "DUC", "Em chuyển hai trăm ngàn xong rồi nha anh! Hệ thống cộng điểm liền luôn!", "nhanh nhảu thúc đám đông",
     sub="Em chuyển 200.000đ xong rồi nha anh! Hệ thống cộng điểm liền luôn!")
scene("s11_hoang_hesitate", "assets/c01.jpg", "tense", tr="dissolve", trd=0.3)
line("l20_hoang", "HG", "Trừ đi trăm hai mới nhận thì lỗ có tám chục ngàn. Coi như mua vé xem kịch cũng được mà…",
     "chần chừ, suýt bấm", sub="Trừ đi 120 ngàn mới nhận thì lỗ có 80 ngàn. Coi như mua vé xem kịch cũng được mà…")

# Nhịp 4: CAO TRÀO LỚN - Hỏi AI về 120K & 200K, câu hỏi cốt tử & Phút 89 bấm THOÁT!
bgm("action_climax", -1.5)
scene("s12_ai_warning", "assets/c10.jpg", "tense", tr="flash_red", trd=0.3)
sfx("heartbeat", 0.0, -5, dur=10.0)
sfx("typing", 0.1, -5, dur=1.5)
bubble("HOÀNG → TRỢ LÝ AI", "Nhưng người ta đã chuyển cho mình 120 ngàn thật rồi, giờ chuyển lại 200 ngàn để tích điểm bảo an thì sao?",
       side="right", y=280, stamp="HỎI AI", dur=5.5, offset=0.1)
line("l20b_hoang", "HG", "Nhưng người ta chuyển cho mình một trăm hai mươi ngàn thật rồi, giờ chuyển lại hai trăm ngàn tích điểm bảo an thì sao?",
     "gõ hỏi AI, còn phân vân", sub="Nhưng người ta chuyển cho mình 120.000đ thật rồi, giờ chuyển lại 200.000đ tích điểm bảo an thì sao?")
sfx("notification", 0.1, -4)
bubble("TRỢ LÝ AI", "Chuyển trước 120k không làm nó hợp pháp – mà khẳng định là kịch bản dẫn dụ. Tuyệt đối không chuyển 200k, không làm nhiệm vụ tiếp theo.",
       side="left", y=450, stamp="CẢNH BÁO", dur=8.5, offset=0.1)
line("l20c_ai", "AI", "Việc họ chuyển trước một trăm hai mươi ngàn không làm nó hợp pháp, mà càng khẳng định là kịch bản dẫn dụ.",
     "đanh thép, dứt khoát", sub="Việc họ chuyển trước 120.000đ không làm nó hợp pháp – mà càng khẳng định là kịch bản dẫn dụ.")
line("l20d_ai", "AI", "Tuyệt đối không chuyển hai trăm ngàn, không làm nhiệm vụ tiếp theo và không cung cấp mã xác thực.",
     "nghiêm nghị cảnh báo", sub="Tuyệt đối không chuyển 200.000đ, không làm nhiệm vụ tiếp theo và không cung cấp mã xác thực.")
callout("TÔI ĐI XIN VIỆC. TẠI SAO TÔI PHẢI CHUYỂN TIỀN?", "danger", y=130, dur=7.5, offset=0.1)
line("l21_hoang", "HG", "Khoan… Mình đi ứng tuyển lập trình viên. Tại sao phải chuyển tiền để chứng minh khả năng giao tiếp?",
     "bừng tỉnh, đanh giọng")
line("l23_khai", "KH", "Anh Hoàng! Còn mười giây cuối, anh chuyển chưa?!", "gằn giọng, hối thúc")
sfx("riser", -1.0, -5, dur=1.0)
scene("s13_leave_meeting", "assets/c11.jpg", "push", tr="flash_white", trd=0.25, shake=0.15)
mark("climax")
sfx("impact", 0.0, -3)
sfx("call_end", 0.2, -4)
callout("PHÚT THỨ 89  ·  BẤM “RỜI CUỘC HỌP”", "safe", y=130, dur=3.2, offset=0.1)
beat(1.4)

# Nhịp 5: CẢ PHÒNG HỌP CHIA VAI NHẮN TIN NÍU KÉO (Hỏi thăm mạng, chỉ cách làm, khoe rút thưởng, mồi hợp đồng lớn)
bgm("tension_drone", -1.2)
scene("s14a_spam_ha", "assets/c12b.jpg", "hand", tr="dissolve", trd=0.3)
sfx("phone_vibrate", 0.05, -4, dur=1.6)
sfx("notification", 0.15, -4)
bubble("NHÂN SỰ HÀ", "Anh Hoàng ơi sao thoát vậy, mạng bên anh bị lỗi hả? Hồ sơ anh điểm cao nhất, cả nhóm đang đợi mình anh đó!",
       side="left", y=260, stamp="HỎI THĂM", dur=6.8, offset=0.15)
line("l24a_ha", "HA", "Anh Hoàng ơi sao thoát vậy, mạng bên anh bị lỗi hả? Hồ sơ anh điểm cao nhất, cả nhóm đang đợi mình anh đó!",
     "hốt hoảng, ngọt ngào níu kéo")

scene("s14b_spam_duc", "assets/c12b.jpg", "push", tr="dissolve", trd=0.25)
sfx("notification", 0.1, -4)
bubble("ỨNG VIÊN 07", "Ông ơi sao thoát ngang vậy? Bên ông bị vướng chỗ điền thông tin bảo an hả, cần tui chỉ cách làm không?",
       side="right", y=240, stamp="NHẮN RIÊNG", dur=7.5, offset=0.1)
sfx("bank_ting", 0.6, -4)
bubble("ỨNG VIÊN 04 (ĐỨC)", "Em vừa chuyển 200.000đ xong, rút về được luôn 380.000đ tiền thưởng nè! Vô lại lẹ đi anh!",
       side="left", y=430, stamp="KHOE TIỀN VỀ", dur=7.2, offset=0.6)
line("l24b_duc", "DUC", "Anh Hoàng ơi sao thoát uổng vậy?! Em vừa chuyển hai trăm ngàn xong, rút về được luôn ba trăm tám mươi ngàn tiền thưởng nè! Vô lại lẹ đi anh!",
     "hào hứng khoe tiền, thúc giục", sub="Anh Hoàng ơi sao thoát uổng vậy?! Em vừa chuyển 200.000đ xong, rút về được luôn 380.000đ tiền thưởng nè!")

scene("s14c_spam_khai", "assets/c12.jpg", "calm", tr="dissolve", trd=0.3)
sfx("phone_vibrate", 0.05, -4, dur=1.5)
sfx("notification", 0.2, -4)
bubble("QUẢN LÝ KHẢI", "Quay lại phòng họp gấp! Anh vừa được duyệt suất hợp đồng 3.000.000 VND, bỏ ngang là hủy toàn bộ quyền lợi!",
       side="left", y=320, stamp="MỒI HỢP ĐỒNG", dur=6.8, offset=0.2)
line("l24c_khai", "KH", "Anh Hoàng quay lại phòng họp gấp! Anh vừa được duyệt suất hợp đồng ba triệu đồng, bỏ ngang là hủy toàn bộ quyền lợi nhé!",
     "uy quyền, dọa nạt xen lẫn dụ dỗ", sub="Quay lại phòng họp gấp! Anh vừa được duyệt suất hợp đồng 3.000.000đ, bỏ ngang là hủy toàn bộ quyền lợi!")
callout("HỎI THĂM MẠNG  ·  CHỈ CÁCH LÀM  ·  KHOE TIỀN THƯỞNG  ·  HỨA HỢP ĐỒNG LỚN", "warning", y=130, dur=8.8, offset=0.1)
line("l24d_hoang", "HG", "Người hỏi thăm rớt mạng, người chỉ cách làm, người khoe rút được tiền, người hứa hợp đồng lớn… Cả một phòng họp chia vai diễn kịch chỉ để kéo mình quay lại.",
     "tỉnh táo, cười nhẹ")
line("l24_hoang", "HG", "Nghỉ khỏe.", "cười khẩy, dứt khoát", pause=0.3)

# ---- NHỚ KỸ (ĐÚNG 10 GIÂY – CÔ ĐỌNG, KHÔNG THUYẾT GIÁO) ----
amb("room_tone", -4.0); bgm("warm_outro", -2.0)
scene("s18_red_flags", EP01B + "scene18.jpg", "still", tr="fade_black", trd=0.35)
mark("rf_start")
sfx("notification", 0.1, -4)
beat(0.2)
line("l29_narr", "N", "Nhà tuyển dụng thật trả lương cho bạn, không bắt bạn nạp tiền. Thấy yêu cầu chuyển khoản: thoát phòng họp ngay.",
     pause=0.4)
mark("rf_end")

# ---- HỒI 3: BA LY NƯỚC SÁNG GIÁNG SINH & LỆNH CHUYỂN 7 TRIỆU BÀN BÊN (KẾT VUI + MỞ) ----
amb("street", -2.5); bgm("warm_outro", -1.5)
scene("s19_christmas_cafe", "assets/c15.jpg", "calm", tr="fade_black", trd=0.4)
chapter("HỒI 3 · 10 GIỜ SÁNG GIÁNG SINH", "LY NƯỚC 120 NGÀN & LỆNH CHUYỂN 7 TRIỆU BÀN BÊN")
sfx("chapter_sting", -0.1, -4)
beat(0.2)
line("l30_tom", "TOM", "Woa, nay ba khao con ly bự luôn! Giáng Sinh vui quá ba ơi!", "vui sướng, reo lên")
line("l31_lan", "L", "Phỏng vấn sao rồi mà nay hào phóng dữ vậy anh?", "vui vẻ trêu chồng")
line("l32_hoang", "HG", "Ba tự đánh rớt ở phút thứ tám mươi chín rồi.", "cười hóm hỉnh, nhẹ nhõm",
     sub="Ba tự đánh rớt ở phút thứ 89 rồi.")
line("l32b_hoang", "HG", "Mà bên đó… tài trợ nhà mình một trăm hai mươi ngàn uống nước Giáng Sinh nè.",
     "vui vẻ khoe vợ", sub="Mà bên đó… tài trợ nhà mình 120.000đ uống nước Giáng Sinh nè.")
line("l33_lan", "L", "Hả? Đi xin việc mà rớt vẫn được khao nước?", "ngạc nhiên, bật cười")
line("l34_hoang", "HG", "Tiền mồi đó em. Hên là anh không bỏ thêm hai trăm ngàn để coi tiếp vở kịch của tụi nó.",
     "vui vẻ nhưng thấm thía", pause=0.3)

bgm("tension_drone", -1.5)
scene("s20_next_table_turn", "assets/c16.jpg", "hand", tr="dissolve", trd=0.35)
line("l35_tn", "TN", "Anh ơi… từ nãy hai trăm ngàn em chuyển thêm mấy đợt rồi mà sao vẫn chưa rút về được vậy anh?",
     "lo lắng, sốt ruột, giọng run", sub="Anh ơi… từ nãy 200 ngàn em chuyển thêm mấy đợt rồi mà sao vẫn chưa rút về được vậy anh?")
line("l36_khai_cafe", "KH", "Chuyển thêm bảy triệu để hoàn tất hồ sơ đổi điểm bảo an thành tiền rút về em nhé!",
     "ngọt xớt, thúc giục qua loa tai nghe", sub="Chuyển thêm 7 triệu để hoàn tất hồ sơ đổi điểm bảo an thành tiền rút về em nhé!")
scene("s21_next_table_7m", "assets/c17.jpg", "push", tr="dissolve", trd=0.3)
sfx("heartbeat", 0.0, -5, dur=3.5)
bubble("CHUYỂN KHOẢN", "Số tiền chuyển: 7.000.000 VND  ·  Nội dung: Đổi điểm bảo an rút gốc",
       side="left", y=340, stamp="ĐANG BẤM", dur=3.6, offset=0.1)
beat(2.8)
scene("s22_black_cut", "assets/c18.jpg", "still", tr="fade_black", trd=0.15)
beat(0.4)
line("l37_narr", "N", "Bắt đầu từ hai trăm ngàn tưởng như chẳng đáng bao nhiêu.",
     sub="Bắt đầu từ 200.000đ tưởng như chẳng đáng bao nhiêu.")
line("l37b_narr", "N", "Nhưng khi đã bước vào vòng xoáy tiếc tiền, không ai biết mình sẽ dừng lại ở con số mấy triệu.",
     pause=0.4)
callout("TÔI ĐI XIN VIỆC. TẠI SAO TÔI PHẢI CHUYỂN TIỀN?", "danger", y=400, dur=6.0, offset=-4.5)
callout("120.000 đồng – Một khoản tiền nhỏ. Một bài học không nhỏ.", "safe", y=540, dur=5.0, offset=-3.5)
beat(2.0)

# ---- DISCLAIMER ----
amb("room_tone", -5.0); bgm("warm_outro", -3.0)
scene("s23_outro", EP01B + "scene18.jpg", "still", tr="fade_black", trd=0.4)
mark("disc_start")
beat(6.5)
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


_desc = [(0.0, "Mở đầu – 120 ngàn tiền thật & lệnh chuyển ngược 200 ngàn")]
_desc += [(c["start"], f"{c['kicker'].split('·')[0].strip().title()} – {c['title'].capitalize()}") for c in chapters]
_desc += [(marks["rf_start"], "Dấu hiệu nhận biết & việc nên làm")]
desc_chapters = "\n".join(f"{mmss(s)} {label}" for s, label in sorted(_desc))

episode = {
    "episode_id": "EP03",
    "slug": "120NganPhutThu89",
    "title": "120 ngàn – Phút thứ 89",
    "version": "v1",
    "scam_family": "ON-11",
    "duration_sec": total,
    "visual_style_lock": "Horizontal 16:9 widescreen (1920x1080), semi-realistic cinematic 2D anime illustration, "
                         "contemporary Southern Vietnam urban setting, moody dramatic lighting, clean bottom 15% for "
                         "subtitles, no text, no letters, no numbers, no logos, no real uniforms",
    "hook": {
        "kicker": "PHÚT THỨ 89 · PHỎNG VẤN TUYỂN DỤNG ONLINE",
        "title": "NHẬN 120 NGÀN TIỀN THẬT – ĐÒI CHUYỂN NGƯỢC 200 NGÀN ĐỂ NHẬN VIỆC",
        "start": 0.4,
        "end": 5.4,
    },
    "chapters": chapters,
    "scenes": scenes,
    "dialogue": dialogue,
    "chat_bubbles": bubbles,
    "callouts": callouts,
    "red_flags": {
        "title": "NHỚ KỸ – 3 DẤU HIỆU BẪY TUYỂN DỤNG ONLINE",
        "start": marks["rf_start"],
        "end": marks["rf_end"],
        "stagger_sec": 0.9,
        "items": [
            "ĐỔI NGƯỜI, LÁI CHỦ ĐỀ: Tuyển chuyên môn nhưng đẩy sang \"Quản lý dự án\" và phòng họp toàn quân xanh",
            "THẢ TIỀN MỒI THẬT: Chuyển trước vài chục đến vài trăm ngàn để xóa nghi ngờ, kích tâm lý \"thử xem sao\"",
            "ĐÒI NỘP TIỀN ĐỔI ĐIỂM: Bắt chuyển khoản để \"chứng minh năng lực\", \"tích điểm bảo an\" rồi nâng dần số tiền để rút gốc",
        ],
        "action": "Nhà tuyển dụng thật trả lương cho bạn, không bắt bạn nạp tiền · Thấy yêu cầu chuyển khoản: Rời cuộc họp & Chặn ngay!",
    },
    "disclaimer": {
        "header": "LƯU Ý",
        "start": marks["disc_start"],
        "end": total,
        "lines": [
            "Tình huống được dựng lại từ chất liệu có thật nhằm cảnh báo cộng đồng; nhân vật, tổ chức và giao diện đều là hư cấu.",
            "Nhà tuyển dụng chân chính không bao giờ yêu cầu ứng viên chuyển tiền để làm nhiệm vụ hay kích hoạt điểm hệ thống.",
        ],
    },
    "audio": {
        "ambience": amb_runs,
        "foley": foley,
        "bgm": bgm_runs,
        "duck_extra": [
            {"start": marks["climax"] - 0.2, "end": marks["climax"] + 1.8, "bgm_db": -14, "amb_db": -10},
            {"start": marks["disc_start"], "end": total - 0.05},
        ],
    },
    "forbidden_terms": [],
    "publish": {
        "titles": [
            "120 Ngàn – Phút Thứ 89: Tôi Đi Xin Việc, Tại Sao Tôi Phải Chuyển Tiền? | Bóc Trần Lừa Đảo",
            "Đi Phỏng Vấn Được Chuyển Nóng 120 Ngàn, Rồi Đòi Ngược 200 Ngàn Đổi Điểm Bảo An | Bóc Trần Lừa Đảo",
            "Đừng Tặc Lưỡi Bỏ 200 Ngàn “Xem Kịch” Trong Phòng Phỏng Vấn Online | Bóc Trần Lừa Đảo",
        ],
        "description": "Sáng Giáng Sinh 25/12, Hoàng – một lập trình viên có kinh nghiệm – bước vào buổi phỏng vấn trực tuyến "
                       "cho vị trí kỹ thuật của một \"tập đoàn lớn\". Sau vòng 1 có trợ lý AI hỗ trợ và hàng loạt ứng viên trả lời "
                       "siêu tốc, buổi phỏng vấn bất ngờ đổi sang \"Quản lý dự án Hệ thống Xã hội Bảo an\". Hoàng nhận được 120.000 đồng "
                       "tiền thật vào tài khoản, trước khi nhận yêu cầu chuyển ngược 200.000 đồng để \"kích hoạt điểm bảo an\". "
                       "Phim bóc trần vì sao không bao giờ được tặc lưỡi bỏ 200.000 đồng để \"xem kịch\".\n\n"
                       "⏱️ Các hồi trong phim:\n" + desc_chapters,
        "pinned_comment": "📌 Nhà tuyển dụng thật trả lương cho bạn – không bao giờ bắt bạn chuyển tiền để \"chứng minh khả năng quản lý, "
                          "giao tiếp\" hay \"kích hoạt điểm hệ thống bảo an\". Khoản 120.000đ chuyển thật ban đầu chỉ là tiền mồi để đánh vào "
                          "tâm lý \"thử 200.000đ cùng lắm lỗ 80.000đ xem kịch\", từ đó kéo nạn nhân vào vòng xoáy tiếc tiền nạp tiếp hàng triệu đồng.",
        "hashtags": ["#bóctrầnlừađảo", "#cảnhgiáclừađảo", "#vạnchuyện", "#lừađảotuyểndụng", "#phútthứ89"],
        "tags": [
            "lừa đảo tuyển dụng online",
            "hệ thống xã hội bảo an",
            "tiền mồi 120 ngàn",
            "phỏng vấn online lừa đảo",
            "bóc trần lừa đảo",
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
