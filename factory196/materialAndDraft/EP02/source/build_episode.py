# -*- coding: utf-8 -*-
"""Builder cho EP02 (factory196) – sinh episode.json từ danh sách sự kiện.

Chạy lại sau Gate 2: nếu có tts_manifest_gate2.json, thời lượng thật của từng câu
được dùng để dàn lại toàn bộ timeline (Real-TTS Retiming) – cảnh, chương, bubble,
callout, foley, red_flags, disclaimer, chapters trong description, thumbnail.

    python factory196/materialAndDraft/EP02/source/build_episode.py
"""
from __future__ import annotations

import json
from pathlib import Path

EP_DIR = Path(__file__).resolve().parent.parent
TTS_MANIFEST = EP_DIR / "audio" / "tts" / "tts_manifest_gate2.json"
OUT = EP_DIR / "episode.json"

SEC_PER_WORD = 0.36
LINE_BASE = 0.45
GAP = 0.35            # nghỉ giữa hai câu
SCENE_LEAD = 0.35     # cảnh lên hình trước tiếng
WINDOW_MARGIN = 1.6   # cửa sổ cho phép TTS dài hơn ước tính

real = {}
if TTS_MANIFEST.is_file():
    for ln in json.loads(TTS_MANIFEST.read_text(encoding="utf-8")).get("lines", []):
        dur_s = ln.get("duration_sec") or ln.get("metrics", {}).get("duration_sec")
        if ln.get("engine") != "placeholder" and dur_s:
            real[ln["line_id"]] = float(dur_s)

# ---------------------------------------------------------------- speakers
SPK = {
    "M": dict(speaker="thang_tun", voice="Puck", label_short="MINH", speaker_label="Minh",
              base="Giọng nam miền Nam 30 tuổi, tông sáng, hiền, nhịp hơi nhanh, phát âm chuẩn phương ngữ miền Nam"),
    "H": dict(speaker="chi_ba", voice="Kore", label_short="HƯƠNG", speaker_label="Hương – vợ Minh",
              base="Giọng phụ nữ miền Nam 28 tuổi, sắc sảo, dứt khoát, tự nhiên như đời thực"),
    "ME": dict(speaker="co_tu", voice="Gacrux", label_short="MẸ MINH", speaker_label="Mẹ Minh",
               base="Giọng phụ nữ miền Nam 60 tuổi, hiền, chậm rãi, hơi yếu vì đang nằm viện, thương con"),
    "KG": dict(speaker="ke_ngot_ngao_nam", label_short="SỐ LẠ", speaker_label="Số lạ – xưng an ninh Ngân hàng X",
               af="phone",
               base="Giọng nam miền Nam 30 tuổi, mượt, lễ phép, nói nhanh, chuyên nghiệp như nhân viên ngân hàng"),
    "TD": dict(speaker="chi_tu", voice="Zephyr", label_short="TỔNG ĐÀI NGÂN HÀNG X", speaker_label="Tổng đài Ngân hàng X",
               af="phone",
               base="Giọng nữ miền Nam 30 tuổi, nhân viên tổng đài ngân hàng, lịch sự, chuẩn mực, bình tĩnh, đều giọng"),
    "N": dict(speaker="nguoi_boc_tran"),
}

# ---------------------------------------------------------------- helpers
def mo(kind: str) -> dict:
    return {
        "tense": {"scale": [1.04, 1.14], "focus": [[0.5, 0.5], [0.47, 0.45]], "wobble": "tense"},
        "calm": {"scale": [1.02, 1.09], "focus": [[0.5, 0.5], [0.5, 0.47]], "wobble": "calm"},
        "hand": {"scale": [1.02, 1.10], "focus": [[0.46, 0.48], [0.54, 0.46]], "wobble": "handheld"},
        "push": {"scale": [1.0, 1.16], "focus": [[0.5, 0.5], [0.5, 0.45]], "wobble": "tense"},
        "pull": {"scale": [1.12, 1.02], "focus": [[0.5, 0.46], [0.5, 0.5]], "wobble": "calm"},
        "still": {"scale": [1.0, 1.05], "focus": [[0.5, 0.5], [0.5, 0.5]], "wobble": "none"},
    }[kind]


E = []  # event list


def scene(sid, image, motion="calm", tr=None, trd=0.35, shake=None):
    E.append(("scene", dict(id=sid, image=image, motion=mo(motion), tr=tr, trd=trd, shake=shake)))


def line(lid, spk, text, emo="", sub=None, pause=0.0):
    E.append(("line", dict(id=lid, spk=spk, text=text, emo=emo, sub=sub, pause=pause)))


def beat(sec):
    E.append(("beat", sec))


def chapter(kicker, title):
    E.append(("chapter", dict(kicker=kicker, title=title)))


def bubble(sender, text, side="left", y=380, stamp="", dur=4.5, offset=0.0):
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
# ---- HOOK ----
amb("night_room", -1.5); bgm("suspense_pulse", -1.0)
scene("s01_hook_ting", "assets/c01.jpg", "tense", shake=0.35)
sfx("bank_ting", 0.1, -3)
bubble("NGÂN HÀNG X", "TK …8826  −80.000.000 VND", side="right", stamp="ĐÃ TRỪ TIỀN", dur=4.2, offset=0.1)
beat(0.25)
line("l01_minh", "M", "Không… Anh đâu có chuyển! Tám chục triệu!", "sững sờ rồi hoảng loạn, run giọng",
     sub="Không… Anh đâu có chuyển! 80 triệu!")
line("l02_huong", "H", "Anh! Tiền mổ của mẹ đó!", "thất thanh, hoảng hốt")
sfx("impact", 0.0, -4)
scene("s02_hook_phone", "assets/c02.jpg", "push", tr="flash_white", trd=0.28)
mark("freeze")
line("l03_narr", "N", "Minh vừa tự tay xác thực một giao dịch mà anh không hề thực hiện.")
line("l04_narr", "N", "Và mọi chuyện bắt đầu từ một chữ cái.")
sfx("riser", -1.4, -5, dur=1.2)
beat(0.6)

# ---- HỒI 1 ----
amb("room_tone", -1.5); bgm("investigative_story", -1.5)
scene("s03_hospital", "assets/c03.jpg", "calm", tr="fade_black", trd=0.45)
chapter("HỒI 1 · CHIỀU CÙNG NGÀY", "TIỀN MỔ CỦA MẸ")
sfx("chapter_sting", -0.1, -4)
beat(0.3)
line("l05_me", "ME", "Thôi con, mổ chi cho tốn. Mẹ về uống thuốc được rồi.", "ngại ngùng, xót tiền của con")
line("l06_minh", "M", "Mẹ đừng lo. Con để dành đủ rồi.", "dịu dàng, trấn an")
line("l07_minh", "M", "Tối nay con chuyển, sáng mai mẹ mổ.", "chắc chắn, ấm áp", pause=0.4)
scene("s04_hands", "assets/c04.jpg", "still", tr="dissolve", trd=0.4)
beat(3.2)

amb("street", -2.5)
scene("s05_cafe_call", "assets/c05.jpg", "calm", tr="fade_black", trd=0.4)
sfx("phone_vibrate", 0.0, -5, dur=1.2)
beat(0.9)
line("l08_huong", "H", "Bệnh viện nhắn rồi anh. Chín giờ sáng chưa có tạm ứng là dời ca mổ.",
     "qua điện thoại, sốt ruột, nói nhanh", sub="Bệnh viện nhắn rồi anh. 9 giờ sáng chưa có tạm ứng là dời ca mổ.")
line("l09_minh", "M", "Anh đang chuyển đây.", "vội, bận tay")
scene("s06_cafe_sms", "assets/c06.jpg", "push", tr="dissolve", trd=0.3)
sfx("notification", 0.1, -4)
bubble("NGÂN HÀNG X", "Phát hiện đăng nhập trên thiết bị lạ. Tài khoản sẽ tạm khóa sau 15 phút. Xác minh ngay tại đường link.",
       side="left", stamp="SMS", dur=6.0, offset=0.1)
beat(1.6)
line("l10_minh", "M", "Trời đất, đúng lúc này.", "bực bội, cuống")
sfx("message_send", 0.1, -6)
callout("ĐƯỜNG LINK TRONG TIN NHẮN:  nganhаngx", "warning", dur=3.5, offset=0.2)
beat(1.0)
line("l11_minh", "M", "Ngân hàng X. Đúng rồi.", "lẩm bẩm, yên tâm", pause=0.2)
scene("s07_fake_site", "assets/c07.jpg", "push", tr="dissolve", trd=0.3)
bubble("TRANG XÁC MINH", "Phát hiện thiết bị mới. Nhập OTP để xác minh.", side="left", stamp="WEB", dur=2.3, offset=0.2)
sfx("typing", 0.4, -6, dur=1.8)
beat(2.6)
bubble("TRANG XÁC MINH", "Đang xử lý… Vui lòng không tắt màn hình.", side="left", stamp="WEB", dur=3.9, offset=0.1)
beat(1.0)
line("l12_minh", "M", "Sao lâu vậy trời…", "sốt ruột, thở dài")
beat(0.8)

# ---- HỒI 2 ----
amb("night_room", -1.5); bgm("tension_drone", -1.0)
scene("s08_home_ring", "assets/c08.jpg", "calm", tr="fade_black", trd=0.4)
chapter("HỒI 2 · 22 GIỜ 20", "CUỘC GỌI “HỖ TRỢ”")
sfx("chapter_sting", -0.1, -4)
sfx("phone_ring", 0.3, -4, dur=1.6)
beat(2.6)
scene("s09_scammer", "assets/c09.jpg", "calm", tr="dissolve", trd=0.3)
line("l13_kg", "KG", "Dạ, anh Minh phải không ạ? Em là Tuấn, bộ phận an ninh Ngân hàng X.", "niềm nở, lễ phép")
line("l14_kg", "KG", "Hệ thống thấy có người đang đăng nhập tài khoản anh từ một thiết bị lạ.", "nghiêm giọng, hơi gấp")
scene("s10_home_talk", "assets/c08.jpg", "hand", tr="dissolve", trd=0.3)
line("l15_minh", "M", "Anh vừa xác minh rồi mà em?", "ngơ ngác, lo")
line("l16_kg", "KG", "Dạ đúng, nên tụi em mới chặn kịp một phần.", "trấn an, mượt")
line("l17_kg", "KG", "Giờ anh cần xác thực khuôn mặt để em khóa thiết bị kia. Em gửi link liền.", "nhanh, chuyên nghiệp")
scene("s11_huong_doubt", "assets/c10.jpg", "hand", tr="dissolve", trd=0.3)
line("l18_huong", "H", "Ngân hàng gì mà bắt quay mặt qua đường link? Anh mở app ra coi thử.", "nghi ngờ, cau mày")
sfx("glitch", 0.2, -4)
bubble("APP NGÂN HÀNG X", "Phiên đăng nhập đã hết hạn.", side="left", stamp="LỖI", dur=2.9, offset=0.2)
beat(1.2)
line("l19_minh", "M", "App văng ra rồi nè em!", "hoảng, giọng cao")
scene("s12_scammer_push", "assets/c09.jpg", "push", tr="dissolve", trd=0.3)
line("l20_kg", "KG", "Đó anh thấy chưa, tụi nó đang chiếm quyền đó. Còn hai phút thôi.", "dồn dập, thúc ép",
     sub="Đó anh thấy chưa, tụi nó đang chiếm quyền đó. Còn 2 phút thôi.")
line("l21_kg", "KG", "Anh làm theo hướng dẫn trên màn hình giùm em.", "gấp gáp nhưng vẫn lễ phép")
scene("s13_face_scan", "assets/c11.jpg", "tense", tr="flash_red", trd=0.3)
sfx("heartbeat", 0.0, -5, dur=9.0)
line("l22_huong", "H", "Anh, để em gọi tổng đài trước đã…", "lo lắng, níu lại")
line("l23_minh", "M", "Không kịp đâu em!", "cuống cuồng, gắt")
bubble("TRANG XÁC MINH", "Đưa khuôn mặt vào khung.", side="left", stamp="WEB", dur=3.4, offset=0.1)
beat(1.4)
line("l24_huong", "H", "Anh! Dừng lại!", "hét lên, lao tới giật điện thoại")
sfx("riser", -1.2, -5, dur=1.2)
scene("s14_too_late", "assets/c12.jpg", "push", tr="flash_white", trd=0.28, shake=0.15)
mark("climax")
sfx("bank_ting", 0.0, -3)
sfx("impact", 0.05, -3)
bubble("NGÂN HÀNG X", "TK …8826  −80.000.000 VND", side="right", stamp="ĐÃ TRỪ TIỀN", dur=4.4, offset=0.0)
sfx("call_end", 1.6, -5)
beat(4.6)

# ---- HỒI 3 ----
amb("room_tone", -3.0); bgm("investigative_story", -1.5)
scene("s15_narrator", EP01B + "scene15.jpg", "calm", tr="glitch", trd=0.35)
chapter("HỒI 3 · BÓC TRẦN", "CHỮ MA: MẮT THẤY MỘT CHỮ, MÁY ĐỌC MỘT CHỮ KHÁC")
sfx("chapter_sting", -0.1, -4)
beat(0.3)
line("l25_narr", "N", "Thứ đánh lừa Minh đầu tiên là một chữ cái.")
scene("s16_letters", "assets/c13.jpg", "still", tr="dissolve", trd=0.3)
callout("THẬT: nganhangx      GIẢ: nganhаngx", "danger", dur=11.0, offset=0.1)
callout("a (Latin)  ≠  а (Cyrillic)", "warning", y=250, dur=10.6, offset=0.5)
line("l26_narr", "N", "Bên trái là chữ a La tinh. Bên phải là chữ a hệ Kirin, nhìn giống hệt nhau.",
     sub="Bên trái là chữ a Latin. Bên phải là chữ а hệ Kirin (Cyrillic), nhìn giống hệt nhau.")
line("l27_narr", "N", "Mắt bạn nhìn thấy một chữ. Máy tính đọc một chữ khác.")
callout("rn ≈ m   ·   thêm đuôi giả   ·   link rút gọn", "warning", dur=10.5, offset=0.1)
line("l28_narr", "N", "Có khi chẳng cần chữ ngoại. Hai chữ r và n đứng sát nhau trông như chữ m.")
line("l29_narr", "N", "Hoặc gắn thêm đuôi giả, hay giấu cả địa chỉ sau một đường link rút gọn.")
scene("s17_flow", "assets/c14.jpg", "still", tr="dissolve", trd=0.3)
callout("CÓ MẬT KHẨU + OTP VẪN VƯỚNG SINH TRẮC HỌC  →  DỤ NẠN NHÂN TỰ QUÉT MẶT", "danger", dur=14.0, offset=0.1)
line("l30_narr", "N", "Hiện nay, đăng nhập máy lạ hay chuyển tiền vượt hạn mức cài đặt đều phải quét khuôn mặt.")
line("l31_narr", "N", "Có mật khẩu và mã OTP vẫn chưa qua được chốt này. Nên chúng gọi điện, dụ nạn nhân tự quét mặt giúp chúng.")
scene("s18_narrator_face", EP01B + "scene15.jpg", "pull", tr="dissolve", trd=0.3)
line("l32_narr", "N", "Mật khẩu thì đổi được. Nhưng khuôn mặt của bạn… là thật.", pause=0.4)

# ---- HỒI 4 ----
amb("night_room", -1.5); bgm("tension_drone", -3.0)
scene("s19_hotline", "assets/c15.jpg", "calm", tr="fade_black", trd=0.4)
chapter("HỒI 4 · CUỘC GỌI THẬT", "NGÂN HÀNG KHÔNG GỬI LINK")
sfx("chapter_sting", -0.1, -4)
callout("GỌI SỐ IN SAU THẺ NGÂN HÀNG", "safe", dur=5.5, offset=5.0)
sfx("phone_ring", 0.4, -6, dur=1.0)
beat(1.4)
line("l33_td", "TD", "Kể cả tin nhắn hiện tên Ngân hàng X, chúng tôi cũng không bao giờ gửi đường link đăng nhập.")
line("l34_td", "TD", "Ngân hàng cũng không yêu cầu xác thực khuôn mặt qua đường link hay điện thoại.")
line("l35_td", "TD", "Tôi đã tạm khóa ngân hàng điện tử và thẻ của anh.")
scene("s19b_hotline_close", "assets/c15.jpg", "push", tr="dissolve", trd=0.3)
line("l36_minh", "M", "Còn tám chục triệu thì sao chị?", "nghẹn, run", sub="Còn 80 triệu thì sao chị?")
line("l37_td", "TD", "Tôi đã ghi nhận giao dịch bất thường để phối hợp kiểm tra.")
line("l38_td", "TD", "Anh đừng xóa tin nhắn hay lịch sử cuộc gọi, trình báo công an ngay và mang căn cước ra chi nhánh sớm nhất.", pause=0.3)
sfx("call_end", -0.2, -6)
scene("s20_silence", "assets/c16.jpg", "still", tr="dissolve", trd=0.5)
beat(2.2)
line("l39_huong", "H", "Tiền mổ của mẹ… có lấy lại được không anh?", "nhỏ, nghẹn ngào")
beat(0.8)
line("l40_minh", "M", "Anh không biết. Mai anh đi hỏi mượn.", "mệt mỏi, cay đắng, nói chậm", pause=0.6)

# ---- NHỚ KỸ ----
amb("room_tone", -4.0); bgm("warm_outro", -2.0)
scene("s21_red_flags", EP01B + "scene18.jpg", "still", tr="fade_black", trd=0.4)
mark("rf_start")
sfx("notification", 0.1, -4)
beat(0.3)
line("l41_narr", "N", "Ba dấu hiệu: khẩn cấp, link bất ngờ, và xác minh lạ.")
line("l42_narr", "N", "Ngân hàng không gửi link. Muốn kiểm tra, tự mở app hoặc gọi số in sau thẻ.")
line("l43_narr", "N", "Lỡ nhập rồi thì gọi ngân hàng khóa ngay, đừng chờ.", pause=0.8)
mark("rf_end")

# ---- HỒI 5 ----
amb("night_room", -1.5); bgm("tension_drone", -2.5)
scene("s22_texting", "assets/c17.jpg", "calm", tr="fade_black", trd=0.4)
chapter("HỒI 5 · 22 GIỜ 40", "TIN NHẮN CHƯA ĐỌC")
sfx("chapter_sting", -0.1, -4)
beat(0.3)
line("l44_huong", "H", "Anh gọi dặn mẹ liền đi. Mẹ hay bấm mấy tin đó lắm.", "lo lắng, thúc giục")
line("l45_minh", "M", "Giờ này mẹ ngủ rồi. Nhắn thôi, sáng mẹ đọc.", "mệt, nhẹ giọng")
sfx("typing", 0.2, -6, dur=2.0)
line("l46_minh", "M", "Mẹ ơi, tin nhắn ngân hàng có link thì đừng bấm nha. Có gì gọi con.", "vừa gõ vừa đọc, nhỏ nhẹ")
sfx("message_send", 0.0, -5)
beat(0.6)
amb("room_tone", -3.0)
scene("s23_mom_night", "assets/c18.jpg", "push", tr="dissolve", trd=0.45)
sfx("phone_vibrate", 0.2, -5, dur=1.0)
bubble("NGÂN HÀNG X", "Tài khoản quý khách sắp bị tạm khóa. Xác minh ngay tại đường link.", side="left", y=300,
       stamp="MỚI", dur=7.6, offset=0.4)
bubble("MINH", "Mẹ ơi, tin nhắn ngân hàng có link thì đừng b…", side="left", y=470, stamp="CHƯA ĐỌC",
       dur=7.0, offset=1.0)
beat(2.4)
line("l47_me", "ME", "Ủa… ngân hàng nhắn gì đây ta…", "nheo mắt đọc, tò mò, ngây thơ", pause=0.3)
scene("s24_finger", "assets/c19.jpg", "push", tr="dissolve", trd=0.25)
sfx("heartbeat", 0.0, -6, dur=2.0)
beat(1.6)
scene("s25_black", "assets/c20.jpg", "still", tr="fade_black", trd=0.15)
beat(0.6)
line("l48_narr", "N", "Một ký tự giả. Một website giả. Nhưng số tiền mất đi… là thật.", pause=0.3)
callout("ĐỪNG BẤM LINK. HÃY TỰ MỞ APP.", "danger", y=420, dur=5.6, offset=-3.2)
callout("Chuyện gấp thì gọi, đừng chỉ nhắn.", "safe", y=560, dur=4.6, offset=-2.2)
beat(2.6)

# ---- DISCLAIMER ----
amb("room_tone", -5.0); bgm("warm_outro", -3.0)
scene("s26_outro", EP01B + "scene18.jpg", "still", tr="fade_black", trd=0.4)
mark("disc_start")
beat(7.0)
mark("end")

# ================================================================ COMPILE
t = 0.0
scenes, dialogue, bubbles, callouts, foley, chapters = [], [], [], [], [], []
amb_runs, bgm_runs, marks = [], [], {}
last_line_end = 0.0


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
        last_line_end = t
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


_desc = [(0.0, "Mở đầu – 80 triệu biến mất")]
_desc += [(c["start"], f"{c['kicker'].split('·')[0].strip().title()} – {c['title'].capitalize()}") for c in chapters]
_desc += [(marks["rf_start"], "Dấu hiệu nhận biết & việc nên làm")]
desc_chapters = "\n".join(f"{mmss(s)} {label}" for s, label in sorted(_desc))

episode = {
    "episode_id": "EP02",
    "slug": "ChuMa80TrieuVaMotCuClick",
    "title": "Chữ ma – 80 triệu và một cú click",
    "version": "v1",
    "scam_family": "ON-03",
    "duration_sec": total,
    "visual_style_lock": "Horizontal 16:9 widescreen (1920x1080), semi-realistic cinematic 2D anime illustration, "
                         "contemporary Southern Vietnam urban setting, moody dramatic lighting, clean bottom 15% for "
                         "subtitles, no text, no letters, no numbers, no logos, no real uniforms",
    "hook": {"kicker": "22 GIỜ 30 · MỘT TIN NHẮN NGÂN HÀNG",
             "title": "TÁM CHỤC TRIỆU BIẾN MẤT – CHỈ VÌ MỘT CHỮ CÁI", "start": 0.4, "end": 5.4},
    "chapters": chapters,
    "scenes": scenes,
    "dialogue": dialogue,
    "chat_bubbles": bubbles,
    "callouts": callouts,
    "red_flags": {
        "title": "NHỚ KỸ – 3 DẤU HIỆU LINK GIẢ NGÂN HÀNG",
        "start": marks["rf_start"], "end": marks["rf_end"], "stagger_sec": 1.3,
        "items": [
            "KHẨN CẤP: \"Tài khoản sẽ bị khóa sau 15 phút!\"",
            "LINK BẤT NGỜ qua SMS hoặc mạng xã hội, kể cả hiện đúng tên ngân hàng",
            "XÁC MINH LẠ: đòi OTP, mật khẩu hay quét khuôn mặt qua link, điện thoại",
        ],
        "action": "Ngân hàng không gửi link · Tự mở app hoặc gọi số in sau thẻ · Lỡ nhập: gọi ngân hàng khóa ngay!",
    },
    "disclaimer": {
        "header": "LƯU Ý",
        "start": marks["disc_start"], "end": total,
        "lines": [
            "Tình huống được dựng lại nhằm cảnh báo cộng đồng; nhân vật, ngân hàng, tên miền và số liệu đều là hư cấu.",
            "Không cung cấp OTP, mật khẩu hay khuôn mặt qua link. Nghi ngờ: gọi số in sau thẻ ngân hàng.",
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
            "Chữ Ma: Một Chữ Cái Giả, 80 Triệu Tiền Mổ Của Mẹ Bay Mất | Bóc Trần Lừa Đảo",
            "Link Ngân Hàng Giả Giống Hệt Thật – Mắt Thấy Một Chữ, Máy Đọc Một Chữ Khác | Bóc Trần Lừa Đảo",
            "Vì Sao Đã Cài Sinh Trắc Học Mà 80 Triệu Vẫn Bốc Hơi? | Bóc Trần Lừa Đảo",
        ],
        "description": "Minh, 30 tuổi, đang chuyển tiền tạm ứng mổ cho mẹ thì nhận tin nhắn hiện tên \"ngân hàng\" báo tài khoản "
                       "sắp bị khóa. Một đường link giống hệt thật – chỉ khác một chữ cái – và một cuộc gọi \"hỗ trợ\" dụ tự quét "
                       "khuôn mặt qua đường link đã khiến 80 triệu biến mất. Phim bóc trần thủ đoạn \"chữ ma\" (tên miền giả mạo "
                       "bằng ký tự giống nhau) và lý do dù đã có sinh trắc học, kẻ gian vẫn dụ chính nạn nhân mở nốt chốt khóa cuối.\n\n"
                       "⏱️ Các hồi trong phim:\n" + desc_chapters,
        "pinned_comment": "📌 Kể cả tin nhắn hiện đúng tên ngân hàng, ngân hàng cũng KHÔNG gửi link yêu cầu đăng nhập, không xin OTP "
                          "và không yêu cầu xác thực khuôn mặt qua link hay điện thoại. Nghi ngờ: tự mở app chính thức hoặc gọi số in "
                          "sau thẻ. Nếu lỡ bị trừ tiền: khóa tài khoản ngay, giữ nguyên tin nhắn/lịch sử cuộc gọi và trình báo công an "
                          "sớm nhất. Chuyện gấp với người thân lớn tuổi – hãy gọi, đừng chỉ nhắn.",
        "hashtags": ["#bóctrầnlừađảo", "#cảnhgiáclừađảo", "#vạnchuyện", "#linkgiả", "#chữma"],
        "tags": ["link giả mạo ngân hàng", "tên miền giả", "chữ ma", "lừa đảo OTP", "xác thực khuôn mặt",
                 "bóc trần lừa đảo", "vạn chuyện"],
        "category": "Education (Giáo dục)",
        "playlist": "Hồ Sơ Bóc Trần Lừa Đảo – Phim Dài Chuyên Sâu",
        "thumbnail_sec": round(marks["climax"] + 0.6, 2),
    },
}

OUT.write_text(json.dumps(episode, ensure_ascii=False, indent=2), encoding="utf-8")
words = sum(len(l["text"].split()) for l in dialogue)
narr = sum(len(l["text"].split()) for l in dialogue if l["speaker"] == "nguoi_boc_tran")
print(f"episode.json: {total:.1f}s · {len(scenes)} cảnh · {len(dialogue)} câu · {words} từ "
      f"({words / (total / 60):.0f} từ/phút) · Người Bóc Trần {narr / words:.0%} lời thoại · "
      f"{'TTS thật' if real else 'ước tính'} ({len(real)} câu thật)")
