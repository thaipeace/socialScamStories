# -*- coding: utf-8 -*-
"""
Trình biên dịch `factory196/materialAndDraft/EP08/episode.json` – Tập EP08:
"Một vòng tiền, hai nửa sự thật" (16:9 Long-form · v2-draft).

Nguồn sự thật duy nhất của timeline: sửa thoại/nhịp ở phần STORY rồi chạy lại
    python3 factory196/materialAndDraft/EP08/source/build_draft.py
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
# 7 tuyến nhân vật = 7 voice hoàn toàn tách biệt trong 02_CAST/cast.json
# (DAT_FAKE chủ đích dùng đúng voice Orus + af="phone" để thể hiện giọng cắt ghép giống Anh Đạt)
NOT_OLD = "tuyệt đối không giả giọng ông già hay bà già run rẩy, không kéo dài chữ, không cải lương"
DAT_BASE = (
    "Giọng nam miền Nam Sài Gòn 38 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
    "giữ cố định một âm sắc trầm chắc, điềm tĩnh, thẳng tính, nói gọn cộc thực dụng, rõ chữ, tự nhiên như đời thực, "
    + NOT_OLD
)
KHANG_BASE = (
    "Giọng nam thanh niên miền Nam Sài Gòn 26 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
    "giữ cố định một âm sắc sáng trẻ, nhịp nhanh gọn, thật thà lễ phép, rõ chữ, tự nhiên như đời thực, " + NOT_OLD
)
KE_BASE = (
    "Giọng nam miền Nam Sài Gòn 40 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
    "giữ cố định một âm sắc trầm đều, lạnh tĩnh, điềm nhiên như kẻ cầm quân cờ, không la hét, " + NOT_OLD
)
SPK = {
    "DAT": dict(
        speaker="anh_hai",
        voice="Orus",
        label_short="ANH ĐẠT",
        speaker_label="Anh Đạt – chủ xưởng nội thất nhỏ 38 tuổi, điềm tĩnh, sòng phẳng, quý nhân viên",
        base=DAT_BASE,
    ),
    "DAT_FAKE": dict(
        speaker="anh_hai",
        voice="Orus",
        af="phone",
        label_short="ANH ĐẠT (HÌNH GHÉP)",
        speaker_label="Giọng cắt ghép giống Anh Đạt trong cuộc gọi video 3 giây chập chờn",
        base=DAT_BASE,
    ),
    "KHANG": dict(
        speaker="thang_tun",
        voice="Puck",
        label_short="KHANG",
        speaker_label="Khang – kỹ thuật viên 26 tuổi, theo Anh Đạt 3 năm, chịu khó, rất nể sếp",
        base=KHANG_BASE,
    ),
    "KHANG_P": dict(
        speaker="thang_tun",
        voice="Puck",
        af="phone",
        label_short="KHANG",
        speaker_label="Khang gọi qua điện thoại cho Anh Đạt",
        base=KHANG_BASE,
    ),
    "QUYEN": dict(
        speaker="chi_hai",
        voice="Sulafat",
        label_short="CHỊ QUYÊN",
        speaker_label="Chị Quyên – vợ Anh Đạt 36 tuổi, thực tế, kiệm lời, quản lý tài khoản chung gia đình",
        base=(
            "Giọng phụ nữ miền Nam Sài Gòn 36 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
            "giữ cố định một âm sắc ấm, trầm vừa, nói gọn chắc, điềm tĩnh, tự nhiên như đời thực, " + NOT_OLD
        ),
    ),
    "HAN": dict(
        speaker="chi_tu",
        voice="Zephyr",
        label_short="HÂN",
        speaker_label="Hân – đồng nghiệp nữ 27 tuổi ngồi bàn kế Khang ở văn phòng xưởng",
        base=(
            "Giọng nữ trẻ miền Nam Sài Gòn 27 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
            "giữ cố định một âm sắc sáng gọn, thân thiện, tự nhiên kiểu đồng nghiệp văn phòng, " + NOT_OLD
        ),
    ),
    "KE_ROOM": dict(
        speaker="chu_no",
        voice="Fenrir",
        af="default",
        label_short="KẺ ĐỨNG GIỮA",
        speaker_label="Kẻ đứng giữa giấu mặt trong phòng tối – bàn kế hoạch với cấp dưới",
        base=KE_BASE,
    ),
    "KE_MSG": dict(
        speaker="chu_no",
        voice="Fenrir",
        af="phone",
        label_short="KẺ ĐỨNG GIỮA",
        speaker_label="Kẻ đứng giữa gõ tin nhắn điều phối từ phòng tối, nhái đúng văn phong Anh Đạt",
        base=KE_BASE,
    ),
    "TECH": dict(
        speaker="ke_ngot_ngao_nam",
        voice="Achird",
        af="default",
        label_short="ĐÀN EM",
        speaker_label="Cấp dưới giấu mặt trong phòng tối – đọc lén tin nhắn và lo phần hình/giọng ghép",
        base=(
            "Giọng nam miền Nam Sài Gòn 28 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
            "giữ cố định một âm sắc gọn, hơi nhanh, tỉnh bơ kiểu dân kỹ thuật làm việc trong phòng tối, " + NOT_OLD
        ),
    ),
    "N": dict(speaker="nguoi_boc_tran"),
}

# Visual Motion Upgrade (Level 2 Full · Level A đa dạng + Level B 2.5D Parallax + Level C+ detail_reveal & notification)
MOTION = {
    "static_hold": {"preset": "static_hold"},
    "pan_right": {"preset": "pan_right", "scale": [1.07, 1.07], "focus": [[0.46, 0.49], [0.54, 0.49]], "wobble": "none"},
    "pan_left": {"preset": "pan_left", "scale": [1.06, 1.06], "focus": [[0.54, 0.50], [0.47, 0.50]], "wobble": "none"},
    "pull_out": {"preset": "slow_pull_out", "scale": [1.08, 1.02], "focus": [[0.50, 0.48], [0.50, 0.50]], "wobble": "none"},
    "pull_out_right": {"preset": "slow_pull_out", "scale": [1.08, 1.02], "focus": [[0.58, 0.50], [0.51, 0.50]], "wobble": "none"},
    "pull_confront": {"preset": "slow_pull_out", "scale": [1.09, 1.02], "focus": [[0.50, 0.52], [0.50, 0.49]], "wobble": "calm"},
    "push_dark": {"preset": "slow_push_in", "scale": [1.02, 1.09], "focus": [[0.50, 0.50], [0.48, 0.55]], "wobble": "none", "easing": "ease_out"},
    "push_right_soft": {"preset": "subtle_push_right", "scale": [1.02, 1.09], "focus": [[0.50, 0.49], [0.56, 0.48]], "wobble": "none", "easing": "ease_out"},
    "push_left_coda": {"preset": "subtle_push_left", "scale": [1.02, 1.09], "focus": [[0.42, 0.44], [0.36, 0.40]], "wobble": "none", "easing": "ease_out"},
    "push_right_coda": {"preset": "subtle_push_right", "scale": [1.02, 1.09], "focus": [[0.60, 0.42], [0.66, 0.38]], "wobble": "none", "easing": "ease_out"},
    "tense_call": {"preset": "tense_push", "scale": [1.03, 1.10], "focus": [[0.50, 0.49], [0.50, 0.45]], "wobble": "tense", "easing": "ease_in"},
}

E: list[tuple[str, object]] = []


def scene(sid: str, img: str, m: str = "pan_right", beat_type: str = "normal", level: str = "A",
          intent: str = "", tr: str | None = None, trd: float = 0.4, shake: float | None = None,
          parallax: dict | None = None):
    E.append(("scene", dict(
        id=sid, image=img, motion=MOTION[m], beat_type=beat_type, level=level,
        intent=intent, tr=tr, trd=trd, shake=shake, parallax=parallax,
    )))


def detail(fx_type: str, offset_start: float | None = None, offset_end: float | None = None,
           offset_at: float | None = None, dur: float | None = None, end_scene: bool = False, **kwargs):
    E.append(("detail", dict(
        type=fx_type, offset_start=offset_start, offset_end=offset_end,
        offset_at=offset_at, dur=dur, end_scene=end_scene, kwargs=kwargs,
    )))


def notif(title: str, text: str, stamp: str = "vừa xong", y: int | None = None, style: str = "neutral",
          dur: float = 4.8, offset: float = 0.0, anim: str = "slide_down"):
    E.append(("notif", dict(
        title=title, text=text, stamp=stamp, y=y, style=style, dur=dur, offset=offset, anim=anim,
    )))


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
# ---- HOOK · CUỘC GỌI LẦN HAI & CÂU HỎI ĐÓNG BĂNG (00:00 – 00:24) ----
amb("office", -2.5); bgm("suspense_pulse", -2.5)
scene("s00_hook_call", "assets/c00.jpg", "push_right_soft", beat_type="suspicion", level="A",
      intent="Đẩy nhẹ về phía Anh Đạt bên phải khi nghi ngờ cuộc gọi lần 2", shake=0.2)
sfx("phone_ring", 0.15, -4, dur=1.2)
bubble("CUỘC GỌI ĐẾN · KHANG", "Lần 2 trong ngày · Xin mượn thêm 30.000.000đ",
       side="left", y=260, stamp="LẦN THỨ HAI", dur=4.6, offset=0.2)
beat(1.4)
line("l01_dat", "DAT", "Sáng mày mới xin ứng bốn lăm triệu. Giờ mới chiều đã hỏi thêm ba chục… Mày vướng chuyện gì nói thiệt anh coi!",
     "giọng đanh lại, nhíu mày lo lắng lẫn nghi ngờ",
     sub="Sáng mày mới xin ứng 45 triệu. Giờ mới chiều đã hỏi thêm 30… Mày vướng chuyện gì nói thiệt anh coi!")
line("l02_khang_p", "KHANG_P", "Ủa anh… em đang gọi diễn đúng như lời anh nhắn hồi nãy mà!",
     "ngơ ngác qua điện thoại, tưởng sếp đang đóng kịch trước mặt vợ")
line("l03_dat", "DAT", "Tao nhắn cho mày hồi nào?!",
     "sững lại, cắt ngang dứt khoát")

scene("s01_hook_freeze", "assets/c01.jpg", "static_hold", beat_type="anomaly", level="C",
      intent="Giữ tĩnh lạnh sau cú impact, gom ánh sáng vào ánh mắt sốc và ánh điện thoại hắt cằm Khang",
      tr="flash_white", trd=0.22, shake=0.15)
mark("hook_freeze")
sfx("impact", 0.0, -2.5)
detail("focus_highlight", offset_start=0.05, end_scene=True, pos=[0.64, 0.44], radius=[0.30, 0.36], dim_outer=0.26, fade=0.30)
detail("screen_glow", offset_start=0.10, end_scene=True, pos=[0.63, 0.45], radius=[0.16, 0.20], color=[115, 190, 255], intensity=0.22, mode="turn_on", fade=0.35)
bubble("ANH ĐẠT (NICK MỚI)", "Mượn anh thêm 30.000.000đ · Như sáng nay",
       side="left", y=260, stamp="AI ĐANG NHẮN?", dur=2.5, offset=0.15)
sfx("heartbeat", 0.2, -5, dur=2.2)
beat(3.1)

# ---- HỒI 1 · HAI HÔM TRƯỚC: CÁCH NÓI CHUYỆN ĐẶC TRƯNG & KẾ HOẠCH PHÒNG TỐI ----
amb("street", -5.0); bgm("investigative_story", -3.8)
scene("s02_trust_coffee", "assets/c02.jpg", "pan_right", beat_type="establishing", level="A",
      intent="Pan ngang ấm áp mở bối cảnh quán cà phê sáng 2 hôm trước (đối lập với pan_left lúc rạn nứt ở s13)",
      tr="fade_black", trd=0.45)
chapter("HỒI 1 · HAI HÔM TRƯỚC", "CÁCH NÓI CHUYỆN & KẾ HOẠCH PHÒNG TỐI")
sfx("chapter_sting", -0.1, -5)
beat(0.8)
# Cài rõ khẩu ngữ đặc trưng của Anh Đạt: "Nè cu Khang", "gọn ghẽ", "anh tính", "chị nhà", "lộ bài"
line("l04_dat", "DAT", "Nè cu Khang, mấy công trình đợt này mày chạy gọn ghẽ quá. Cuối tháng anh tính thêm cho.",
     "cười thoải mái bên ly cà phê sáng, nói cộc gọn đầy tin cậy")
line("l05_khang", "KHANG", "Anh em làm chung ba năm rồi, tính toán chi anh. Có việc gì cứ kêu em.",
     "cười tươi, lễ phép và rất quý sếp")
line("l06_dat", "DAT", "Ừ, tuần sau kỷ niệm mười năm ngày cưới. Rảnh phụ anh kiếm quà cho chị nhà, đừng để bả biết lộ bài nghen.",
     "hạ giọng vui vẻ, dặn dò thân mật đúng kiểu người đàn ông thực dụng",
     sub="Ừ, tuần sau kỷ niệm 10 năm ngày cưới. Rảnh phụ anh kiếm quà cho chị nhà, đừng để bả biết lộ bài nghen.")
line("l07_khang", "KHANG", "Dạ dễ ợt, anh chọn xong cứ nhắn em làm gọn.",
     "gật đầu nhanh nhẹn, tự tin", pause=0.3)

# Phòng tối ánh xanh lạnh: thoại cực gọn đúng chất ám hiệu/cách làm, không giảng bài 3s hay mạng yếu
amb("night_room", -2.5); bgm("tension_drone", -2.8)
scene("s03_dark_room_plan", "assets/c03.jpg", "push_dark", beat_type="suspicion", level="B",
      intent="Parallax 2.5D hai lớp đẩy qua hai bóng lưng kẻ gian tiến sâu vào bàn laptop & 2 điện thoại phòng tối kết hợp nhịp sáng màn hình",
      tr="fade_black", trd=0.4,
      parallax={
          "camera": "push_in",
          "dolly": [1.02, 1.07],
          "shift_x": [0.0, 0.0],
          "shift_y": [0.0, -3.0],
          "focus": [0.48, 0.56],
          "strength": 0.85,
          "easing": "ease_out",
          "layers": [
              {"role": "bg", "image": "assets/s03_bg.jpg", "depth": 0.40, "blur": 0.8},
              {"role": "fg", "image": "assets/s03_fg.png", "depth": 1.35},
          ],
      })
mark("two_phones")
sfx("typing", 0.2, -5, dur=1.2)
detail("screen_glow", offset_start=0.2, end_scene=True, space="frame", pos=[0.46, 0.56], radius=[0.24, 0.20], color=[95, 195, 245], intensity=0.24, mode="pulse", fade=0.45)
beat(1.1)
line("l08_tech", "TECH", "Xong máy ông Đạt rồi. Lọc hết tin cũ, nắm thói quen xưng hô của ổng luôn.",
     "vừa lướt màn hình bên trái vừa báo cáo gọn bơ")
line("l09_ke", "KE_ROOM", "Ừ. Mai lên nick mới, nhớ gọi nhá nó một cái rồi mới nhắn. Đánh vòng qua thằng Khang cho gọn.",
     "lạnh tĩnh ra lệnh gọn bằng tiếng lóng nghiệp vụ, không dài dòng",
     pause=0.8)

# ---- HỒI 2 · SÁNG HÔM SAU: CUỘC GỌI HÌNH GHÉP 3 GIÂY & VĂN PHONG Y HỆT ----
amb("office", -3.0); bgm("suspense_pulse", -3.0)
scene("s04_fake_video_call", "assets/c04.jpg", "static_hold", beat_type="anomaly", level="C",
      intent="Giữ khung tĩnh để lộ rõ màn hình cuộc gọi hình ghép chớp giật 3 giây rồi tắt tối kính đen đúng nhịp cúp máy",
      tr="fade_black", trd=0.4)
chapter("HỒI 2 · SÁNG HÔM SAU", "CUỘC GỌI HÌNH GHÉP & NHÁI GIỌNG SẾP")
sfx("chapter_sting", -0.1, -5)
sfx("phone_ring", 0.3, -4, dur=1.1)
beat(1.3)
sfx("glitch", 0.0, -3)
detail("screen_glow", offset_start=0.0, offset_end=6.8, pos=[0.58, 0.51], radius=[0.17, 0.28], color=[110, 225, 255], intensity=0.26, mode="flicker", fade=0.20)
bubble("CUỘC GỌI VIDEO · ANH ĐẠT (NICK MỚI)", "Tín hiệu yếu · Đã kết thúc (00:03)",
       side="left", y=260, stamp="HÌNH GHÉP 3 GIÂY", dur=4.8, offset=0.1)
line("l12_dat_fake", "DAT_FAKE", "Nè cu Khang! Mạng chỗ xưởng gỗ yếu quá hình giật hết trơn… Thôi cúp nha, anh nhắn tin cho gọn!",
     "gấp gáp, hơi đứt quãng như sóng yếu qua cuộc gọi video ngắn")
sfx("glitch", 0.0, -3)
sfx("call_end", 0.2, -3)
detail("detail_reveal", image="assets/c04_call_off.jpg", offset_at=0.10, dur=0.16, region=[0.47, 0.21, 0.71, 0.83], feather=0.01)
detail("light_shift", offset_at=0.2, dur=0.22, brightness=0.92, tint_rgb=[195, 215, 235], tint_strength=0.07)
beat(0.5)

# Cắt chéo phòng tối: gã điều phối gõ Nhịp 1 nhái Y HỆT cách nói chuyện của Anh Đạt
amb("night_room", -2.8); bgm("suspense_pulse", -3.2)
scene("s05_fake_step1_dark", "assets/c05_dim.jpg", "pan_left", beat_type="information", level="C",
      intent="Pan ngang dịu qua đôi bàn tay phòng tối kèm màn hình điện thoại phải bừng sáng từ trạng thái tối khớp nhịp chạm gửi tin",
      tr="dissolve", trd=0.3)
sfx("click", 0.05, -5)
sfx("message_send", 0.2, -4)
detail("detail_reveal", image="assets/c05.jpg", offset_at=0.12, dur=0.28, region=[0.515, 0.595, 0.728, 0.705], feather=0.01)
detail("screen_glow", offset_start=0.2, end_scene=True, pos=[0.61, 0.65], radius=[0.18, 0.14], color=[115, 212, 255], intensity=0.28, mode="turn_on", fade=0.30)
bubble("ANH ĐẠT (NICK MỚI)", "Gọi số cũ xin ứng 45tr · Giữ bí mật cho chị nhà",
       side="left", y=260, stamp="NHỊP 1 · NHÁI GIỌNG", dur=5.6, offset=0.2)
beat(0.6)
line("l13_ke", "KE_MSG", "Nè cu Khang, anh đặt đồng hồ kỷ niệm cho chị nhà rồi. Tài khoản chung anh tự chuyển là lộ bài liền.",
     "cộc gọn đúng nhịp nói của Anh Đạt")
line("l14_ke", "KE_MSG", "Trưa nay gọi số cũ xin ứng bốn lăm triệu, nói dưới quê có việc gấp. Làm gọn giùm anh, xong việc anh tính.",
     "nhái y hệt câu cửa miệng của Anh Đạt",
     sub="Trưa nay gọi số cũ xin ứng 45 triệu, nói dưới quê có việc gấp. Làm gọn giùm anh, xong việc anh tính.",
     pause=0.3)

# Cắt về văn phòng sáng nắng: Khang ngồi tại bàn cười tủm tỉm, Hân chọc nhẹ — ngắn gọn tự nhiên, không nhắc lại thông tin thừa
amb("office", -3.0); bgm("investigative_story", -4.0)
scene("s06_office_relay", "assets/c06.jpg", "pull_out", beat_type="normal", level="A",
      intent="Lùi nhẹ mở không gian văn phòng ban ngày tự nhiên giữa Khang và Hân",
      tr="dissolve", trd=0.35)
beat(0.5)
line("l15_han", "HAN", "Ủa Khang, ôm điện thoại cười tủm tỉm gì đó? Có bồ rồi hả?",
     "ngước từ bàn bên nhìn qua, cười chọc nhẹ tự nhiên")
line("l16_khang", "KHANG", "Đâu có. Sếp nhờ phụ đặt quà cho chị nhà, kêu giữ kín kẻo lộ.",
     "cười xòa, hạ giọng thoải mái không chút nghi ngờ")
line("l17_han", "HAN", "Sếp chiều vợ ghê ha. Ráng làm gọn cho ổng đi.",
     "cười gật nhẹ quay lại màn hình, đời thường không kịch", pause=0.35)

# ---- HỒI 3 · BUỔI TRƯA: DÒNG TIỀN ĐI MỘT VÒNG ----
amb("room_tone", -3.0); bgm("investigative_story", -3.5)
scene("s07_real_call_home", "assets/c07.jpg", "pan_right", beat_type="normal", level="A",
      intent="Quét ngang nhẹ từ mâm cơm trưa sang sự đồng thuận bình thản của vợ chồng Anh Đạt",
      tr="fade_black", trd=0.45)
chapter("HỒI 3 · BUỔI TRƯA", "DÒNG TIỀN ĐI MỘT VÒNG")
sfx("chapter_sting", -0.1, -5)
sfx("phone_ring", 0.3, -4, dur=1.1)
beat(1.3)
line("l19_khang_p", "KHANG_P", "Alo anh Đạt… Dưới quê nhà em đột xuất có việc gấp, anh cho em ứng trước bốn mươi lăm triệu được hông?",
     "hơi vội vã nhập vai qua điện thoại",
     sub="Alo anh Đạt… Dưới quê nhà em đột xuất có việc gấp, anh cho em ứng trước 45 triệu được hông?")
line("l20_dat", "DAT", "Chuyện gấp hả cu Khang? Rồi, để anh chuyển qua tài khoản của mày liền, lo xong rồi tính.",
     "không chút nghi ngờ vì nghe đúng giọng người em quen")
line("l21_quyen", "QUYEN", "Thằng Khang làm với mình ba năm nay đàng hoàng. Anh cứ ghi rõ nội dung ứng lương rồi chuyển cho nó đi.",
     "ngồi bên mâm cơm, điềm tĩnh gật đầu thực tế")
sfx("bank_ting", 0.1, -3)
bubble("NGÂN HÀNG CỦA ĐẠT", "Chuyển sang Khang: -45.000.000đ · ND: Ung luong",
       side="left", y=260, stamp="1 · ĐẠT → KHANG", dur=4.8, offset=0.1)
beat(0.7)
line("l22_dat", "DAT", "Rồi, anh mới chuyển bốn lăm triệu xong đó. Lo gọn việc dưới quê đi nghen.",
     "bấm xong điện thoại, dặn gọn rồi tắt máy",
     sub="Rồi, anh mới chuyển 45 triệu xong đó. Lo gọn việc dưới quê đi nghen.")
sfx("call_end", 0.0, -4)
beat(0.35)

# Cắt chéo sang phòng tối: kẻ đứng giữa tiếp tục nhái văn phong cộc gọn của Đạt
amb("night_room", -2.5); bgm("suspense_pulse", -2.5)
scene("s08_dark_step2_account", "assets/c08_dim.jpg", "push_right_soft", beat_type="information", level="C",
      intent="Đẩy nhẹ vào màn hình phải nơi đầu ngón tay gửi STK lạ: màn hình bật sáng từ trạng thái tối khớp click và ánh vàng-xanh",
      tr="dissolve", trd=0.35)
sfx("click", 0.05, -5)
sfx("message_send", 0.2, -3)
detail("detail_reveal", image="assets/c08.jpg", offset_at=0.12, dur=0.28, region=[0.550, 0.318, 0.768, 0.655], feather=0.01)
detail("screen_glow", offset_start=0.15, end_scene=True, pos=[0.66, 0.50], radius=[0.18, 0.22], color=[255, 205, 125], intensity=0.26, mode="turn_on", fade=0.28)
bubble("ANH ĐẠT (NICK MỚI)", "Chuyển 45.000.000đ vô TK cửa hàng này",
       side="left", y=260, stamp="2 · GỬI STK LẠ", dur=5.2, offset=0.2)
beat(0.6)
line("l23_ke", "KE_MSG", "Tiền vô rồi hả cu Khang? Đẩy bốn lăm triệu vô số tài khoản cửa hàng này gọn giùm anh, họ giao thẳng về xưởng.",
     "bình thản, giữ đúng kiểu nói cộc gọn của Anh Đạt",
     sub="Tiền vô rồi hả cu Khang? Đẩy 45 triệu vô số tài khoản cửa hàng này gọn giùm anh, họ giao thẳng về xưởng.",
     pause=0.25)

# Khang bấm chuyển tiền ngay — dòng tiền 3 bước hoàn tất
amb("office", -3.5); bgm("tension_drone", -2.8)
scene("s09_khang_transfers", "assets/c09.jpg", "static_hold", beat_type="climax", level="C",
      intent="Giữ tĩnh tương phản ngay khoảnh khắc Khang bấm chuyển 45 triệu, ánh màn hình sáng khớp bank_ting",
      tr="dissolve", trd=0.3)
mark("money_loop")
sfx("typing", 0.15, -5, dur=0.75)
sfx("click", 0.95, -4)
sfx("bank_ting", 1.1, -2.5)
detail("screen_glow", offset_start=1.05, end_scene=True, pos=[0.55, 0.58], radius=[0.14, 0.16], color=[130, 228, 215], intensity=0.28, mode="turn_on", fade=0.25)
detail("focus_highlight", offset_start=0.8, end_scene=True, pos=[0.60, 0.46], radius=[0.30, 0.34], dim_outer=0.20, fade=0.35)
bubble("NGÂN HÀNG CỦA KHANG", "Đã chuyển: -45.000.000đ → TK ••••",
       side="left", y=260, stamp="3 · KHANG → KẺ GIAN", dur=3.0, offset=1.1)
beat(4.3)

# ---- HỒI 4 · BỐN GIỜ CHIỀU: NHỊP THỨ HAI & PHÚT VỠ LẼ ----
amb("night_room", -2.5); bgm("tension_drone", -2.0)
scene("s10_second_attempt_dark", "assets/c10.jpg", "pull_out_right", beat_type="suspicion", level="C",
      intent="Lùi chậm từ điện thoại đang gõ lộ ra chiếc điện thoại thứ 2 trên bàn tối, màn hình thở sáng theo nhịp",
      tr="fade_black", trd=0.4)
chapter("HỒI 4 · BỐN GIỜ CHIỀU", "NHỊP THỨ HAI & PHÚT VỠ LẼ")
sfx("chapter_sting", -0.1, -5)
sfx("keyboard", 0.15, -6, dur=0.9)
sfx("message_send", 0.3, -4)
detail("screen_glow", offset_start=0.25, end_scene=True, pos=[0.62, 0.49], radius=[0.18, 0.20], color=[115, 215, 255], intensity=0.26, mode="pulse", fade=0.35)
bubble("ANH ĐẠT (NICK MỚI)", "Gọi số cũ mượn anh thêm 30.000.000đ",
       side="left", y=260, stamp="NHỊP 2 · ĐÒI THÊM", dur=5.0, offset=0.3)
beat(0.7)
line("l24_ke", "KE_MSG", "Cu Khang, cửa hàng còn thêm món quà kèm đẹp quá. Gọi số cũ mượn anh thêm ba chục triệu, làm gọn giùm anh nha.",
     "thản nhiên lặp lại đúng văn phong cũ",
     sub="Cu Khang, cửa hàng còn thêm món quà kèm đẹp quá. Gọi số cũ mượn anh thêm 30 triệu, làm gọn giùm anh nha.")

# Nối tiếp ngay sau câu hỏi ở Hook
amb("office", -2.5); bgm("action_climax", -2.5)
scene("s11_real_call_suspect", "assets/c11.jpg", "tense_call", beat_type="climax", level="A",
      intent="Đẩy gấp tạo xung lực dẫn thẳng vào cảnh đối chất",
      tr="dissolve", trd=0.3)
sfx("riser", 0.0, -4, dur=1.0)
beat(0.45)
line("l25_dat", "DAT", "Mày đứng yên đó, chạy thẳng qua phòng anh ngay! Đem cái điện thoại qua đây cho anh coi!",
     "gấp gáp, nghiêm giọng dứt khoát")
sfx("call_end", 0.0, -3)
beat(0.55)

# Đối chất trực diện: hai điện thoại đặt cạnh nhau trên bàn
amb("office", -3.0); bgm("action_climax", -2.2)
scene("s12_confrontation_desk", "assets/c12.jpg", "pull_confront", beat_type="climax", level="C",
      intent="Mở khung rộng đối chất Trái–Phải, 2 điện thoại sáng giữa bàn và ánh sáng chùng lạnh đúng giây phát hiện bị chặn",
      tr="flash_white", trd=0.22, shake=0.18)
mark("confrontation")
sfx("impact", 0.0, -2.5)
detail("screen_glow", offset_start=0.3, end_scene=True, pos=[0.50, 0.88], radius=[0.22, 0.10], color=[145, 215, 255], intensity=0.24, mode="steady", fade=0.4)
beat(0.45)
line("l26_khang", "KHANG", "Anh coi nè! Hồi sáng nó còn gọi hình đúng mặt đúng giọng anh, nhắn y chang kiểu cu Khang, chị nhà luôn mà!",
     "hốt hoảng đặt điện thoại xuống bàn, giọng run lên")
line("l27_dat", "DAT", "Tài khoản này đâu phải của anh! Mà sao nó có clip mặt anh với biết tuần sau kỷ niệm ngày cưới?!",
     "sững sờ nhìn màn hình, giọng trầm nặng")
sfx("notification", 0.45, -7.0)
notif("CẢNH BÁO BẢO MẬT", "Phát hiện đăng nhập từ thiết bị lạ · 02:14",
      stamp="Đã bỏ qua", y=None, style="danger", dur=5.6, offset=0.45)
line("l28_dat", "DAT", "Khoan… hồi khuya máy anh có báo đăng nhập từ thiết bị khác. Anh tưởng lỗi mạng nên bấm bỏ qua mất tiêu rồi!",
     "mở máy mình lên, chợt giật mình nhận ra lỗ hổng", pause=0.2)
sfx("phone_ring", 0.0, -5, dur=0.9)
sfx("call_end", 0.95, -3)
sfx("low_accent", 0.95, -3.5)
detail("light_shift", offset_at=0.95, dur=0.45, brightness=0.90, tint_rgb=[195, 215, 240], tint_strength=0.08)
beat(1.05)
line("l29_khang", "KHANG", "Nó chặn mất rồi anh Đạt ơi… Bốn mươi lăm triệu em vừa chuyển qua tài khoản lạ rồi!",
     "tái mặt, giọng nghẹn lại khi gọi nick giả không còn liên lạc được",
     sub="Nó chặn mất rồi anh Đạt ơi… 45 triệu em vừa chuyển qua tài khoản lạ rồi!")
line("l30_dat", "DAT", "Bình tĩnh lại. Gọi tổng đài ngân hàng liền đi, rồi gom hết sao kê với tin nhắn đi trình báo công an!",
     "kìm giọng dứt khoát, xử lý ngay lập tức", pause=0.7)

# ---- HỒI 5 · CHIỀU HÔM SAU: THỨ MẤT ĐI KHÔNG CHỈ LÀ TIỀN ----
amb("street", -5.5); bgm("warm_outro", -5.2)
scene("s13_coffee_aftermath", "assets/c13.jpg", "pan_left", beat_type="aftermath", level="A",
      intent="Quét ngược chiều (pan_left đối lập s02 pan_right) trên đúng bàn cà phê cũ – ẩn dụ khoảng cách rạn nứt",
      tr="fade_black", trd=0.55)
chapter("HỒI 5 · CHIỀU HÔM SAU", "THỨ MẤT ĐI KHÔNG CHỈ LÀ TIỀN")
sfx("chapter_sting", -0.1, -6)
beat(1.1)
mark("quiet_aftermath")
line("l31_khang", "KHANG", "Bên ngân hàng nói tiền đi qua nhiều lớp rồi, khó giữ kịp… Bốn lăm triệu đó để em góp lương trả dần.",
     "ngồi cúi mắt bên ly cà phê đá, giọng trầm buồn áy náy",
     sub="Bên ngân hàng nói tiền đi qua nhiều lớp rồi, khó giữ kịp… 45 triệu đó để em góp lương trả dần.")
line("l32_dat", "DAT", "Thôi, coi như hai anh em xui. Chuyện tiền nong cứ để từ từ tính.",
     "lắc đầu nhẹ, giọng điềm tĩnh không một lời trách móc", pause=0.8)
beat(2.0)

# ---- THẺ NHỚ KỸ (< 10 GIÂY · NGƯỜI BÓC TRẦN ĐÚNG 1 CÂU) ----
amb("room_tone", -5.0); bgm("warm_outro", -4.2)
scene("s16_red_flags", EP01B + "scene18.jpg", "static_hold", beat_type="ending", level="A",
      intent="Giữ tĩnh tuyệt đối để khán giả tập trung đọc thẻ Nhớ kỹ",
      tr="fade_black", trd=0.4)
mark("rf_start")
sfx("bank_ting", 0.0, -5)
line("l35_narr", "N", "Mặt, giọng hay cách nói đều giả được. Cứ dính tiền mà dặn giữ bí mật, hãy gọi số thật hỏi thẳng.")
beat(1.0)
mark("rf_end")

# ---- KẾT MỞ SAU THẺ NHỚ · CÚ LẬT RẠN NỨT LÒNG TIN (GỌI THẲNG TÊN & GIỮ LÀM BẰNG) ----
amb("street", -5.5); bgm("tension_drone", -1.4)
scene("s14a_coda_dat_probe", "assets/c14a.jpg", "push_left_coda", beat_type="suspicion", level="C",
      intent="Đẩy tĩnh lạnh vào ánh mắt dò xét của Anh Đạt bên trái kết hợp gom sáng nhẹ khi bỏ chữ 'cu'",
      tr="fade_black", trd=0.5)
mark("silent_crack")
sfx("low_accent", 0.9, -4.0)
detail("focus_highlight", offset_start=0.8, end_scene=True, pos=[0.35, 0.38], radius=[0.28, 0.36], dim_outer=0.22, fade=0.55)
beat(1.6)
line("l33_dat", "DAT", "À Khang… Sao kê chỉ ghi anh cho em ứng lương. Đừng xóa tin nhắn giả hôm qua, gửi anh giữ làm bằng.",
     "bỏ hẳn chữ cu, hạ giọng trầm hẳn và lạnh băng, mắt dò xét, nhả từng chữ sắc và nặng như giữ bằng chứng phòng thân",
     pause=0.9)

amb("room_tone", -5.0); bgm("tension_drone", -1.2)
scene("s14b_coda_khang_counter", "assets/c14b.jpg", "push_right_coda", beat_type="climax", level="B",
      intent="Parallax 2.5D vượt vai mờ của Anh Đạt tiến thẳng vào đôi mắt lạnh ngang hàng của Khang kèm gom sáng",
      tr="dissolve", trd=0.25,
      parallax={
          "camera": "push_in",
          "dolly": [1.02, 1.09],
          "shift_x": [-8.0, 10.0],
          "shift_y": [0.0, -4.0],
          "focus": [0.62, 0.40],
          "strength": 1.0,
          "easing": "ease_out",
          "layers": [
              {"role": "bg", "image": "assets/s14b_bg.jpg", "depth": 0.60},
              {"role": "fg", "image": "assets/s14b_fg.png", "depth": 1.45, "blur": 1.0},
          ],
      })
sfx("heartbeat", 0.1, -3.5, dur=2.6)
detail("focus_highlight", offset_start=0.6, end_scene=True, pos=[0.67, 0.36], radius=[0.28, 0.36], dim_outer=0.24, fade=0.55)
bubble("SAO KÊ NGÂN HÀNG", "Anh Đạt → Khang: +45.000.000đ · ND: Ung luong",
       side="left", y=245, stamp="CHỨNG TỪ DUY NHẤT", dur=7.4, offset=0.15)
beat(1.9)
line("l34_khang", "KHANG", "Được anh. Vậy anh cũng chụp cái báo đăng nhập lạ hôm kia… gửi em giữ làm bằng luôn đi.",
     "mất hẳn vẻ áy náy lễ phép, bỏ chữ dạ, ngước nhìn thẳng đối mặt, giọng lạnh ngang hàng sắc như dao",
     pause=1.0)

# Cắt đen đột ngột!
sfx("impact", 0.0, -1.2)
scene("s15_black_cut", "assets/c15.jpg", "static_hold", beat_type="aftermath", level="A",
      intent="Cắt đen tĩnh tuyệt đối tạo khoảng lặng sau cú chốt cuối phim",
      tr="fade_black", trd=0.08)
beat(2.2)

# ---- DISCLAIMER ----
amb("room_tone", -6.0); bgm("tension_drone", -8.0)
scene("s17_disclaimer", EP01B + "scene18.jpg", "static_hold", beat_type="ending", level="A",
      intent="Giữ tĩnh sạch sẽ cho bảng Lưu ý cuối phim",
      tr="fade_black", trd=0.35)
mark("disc_start")
beat(4.2)

# ================================================================ COMPILE
t = 0.0
scenes, dialogue, bubbles, notifications, foley, chapters = [], [], [], [], [], []
amb_runs, bgm_runs, marks = [], [], {}


def est(text: str) -> float:
    return len(text.split()) * SEC_PER_WORD + LINE_BASE


for kind, d in E:
    if kind == "scene":
        if scenes:
            scenes[-1]["end"] = round(t, 2)
            for fx_ in scenes[-1].get("detail_fx", []):
                if fx_.pop("_end_scene", False):
                    fx_["end"] = round(t, 2)
        sc = {
            "id": d["id"],
            "image": d["image"],
            "start": round(t, 2),
            "end": None,
            "beat_type": d["beat_type"],
            "motion_level": d["level"],
            "motion_intent": d["intent"],
            "motion": d["motion"],
        }
        if d.get("parallax"):
            sc["parallax"] = d["parallax"]
        if d["tr"]:
            sc["transition_in"] = {"type": d["tr"], "dur": d["trd"]}
        if d["shake"] is not None:
            sc["shakes"] = [{"at": round(t + d["shake"], 2), "dur": 0.4, "amp": 16}]
        scenes.append(sc)
        t += SCENE_LEAD
    elif kind == "detail":
        fx = {"type": d["type"], **d["kwargs"]}
        if d["offset_start"] is not None:
            fx["start"] = round(max(0.0, t + d["offset_start"]), 2)
        if d["offset_end"] is not None:
            fx["end"] = round(max(0.0, t + d["offset_end"]), 2)
        if d["offset_at"] is not None:
            fx["at"] = round(max(0.0, t + d["offset_at"]), 2)
        if d["dur"] is not None:
            fx["dur"] = d["dur"]
        if d["end_scene"]:
            fx["_end_scene"] = True
        scenes[-1].setdefault("detail_fx", []).append(fx)
    elif kind == "notif":
        s = t + d["offset"]
        nt = {
            "title": d["title"],
            "text": d["text"],
            "stamp": d["stamp"],
            "style": d["style"],
            "start": round(s, 2),
            "end": round(s + d["dur"], 2),
            "anim": d["anim"],
        }
        if d["y"] is not None:
            nt["y"] = d["y"]
        notifications.append(nt)
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
            "anim": "slide_up",
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
for fx_ in scenes[-1].get("detail_fx", []):
    if fx_.pop("_end_scene", False):
        fx_["end"] = total
amb_runs[-1]["end"] = total
bgm_runs[-1]["end"] = total


def mmss(x: float) -> str:
    return f"{int(x // 60):02d}:{int(x % 60):02d}"


_desc = [(0.0, "Mở đầu – Cuộc gọi lần hai & câu hỏi đóng băng")]
_desc += [(c["start"] - 0.2, f"{c['kicker'].split('·')[0].strip().title()} – {c['title'].capitalize()}")
          for c in chapters if c["kicker"]]
_desc += [(marks["rf_start"], "Nhớ kỹ – 5 nguyên tắc chặn bẫy người đứng giữa")]
desc_chapters = "\n".join(f"{mmss(max(0.0, s))} {label}" for s, label in sorted(_desc))

episode = {
    "episode_id": "EP08",
    "slug": "MotVongTienHaiNuaSuThat",
    "title": "Một vòng tiền, hai nửa sự thật",
    "version": "v5-level2-full-staging",
    "motion_upgrade": "level2",
    "scam_family": "IMPERSONATION-MITM – Người đứng giữa đọc lén trò chuyện, nhái đúng văn phong + nhá video hình/giọng ghép 3 giây để điều phối hai người quen tự chuyển tiền đường vòng",
    "duration_sec": total,
    "visual_style_lock": (
        "Horizontal 16:9 widescreen (1920x1080), semi-realistic cinematic 2D anime illustration, "
        "contemporary Southern Vietnam urban setting, naturalistic dramatic lighting, clean bottom 15% for subtitles, "
        "no text, no letters, no numbers, no license plates, no logos, no real app interface, no real uniforms"
    ),
    "hook": {
        "kicker": "BẪY NGƯỜI ĐỨNG GIỮA · BỐN GIỜ CHIỀU",
        "title": "MỘT VÒNG TIỀN, HAI NỬA SỰ THẬT",
        "start": 0.4,
        "end": 5.0,
    },
    "chapters": chapters,
    "scenes": scenes,
    "dialogue": dialogue,
    "chat_bubbles": bubbles,
    "notifications": notifications,
    "callouts": [],
    "red_flags": {
        "title": "NHỚ KỸ – BẪY NGƯỜI ĐỨNG GIỮA",
        "start": marks["rf_start"],
        "end": marks["rf_end"],
        "stagger_sec": 0.45,
        "items": [
            "HỎI THẲNG ĐÚNG VIỆC ĐƯỢC NHỜ: Gọi số thật vẫn dính bẫy nếu bạn diễn theo kịch bản giữ bí mật của kẻ gian",
            "CUỘC GỌI HÌNH MỜ 3 GIÂY RỒI CÚP ĐỔ MẠNG YẾU: Có thể là hình ghép và giọng cắt ghép từ tin nhắn cũ",
            "ĐÚNG GIỌNG ĐIỆU VẪN CHƯA CHẮC CHÍNH CHỦ: Kẻ đọc lén tài khoản có thể bắt chước cả cách xưng hô lẫn chuyện riêng",
            "KHÔNG CHUYỂN TIỀN ĐƯỜNG VÒNG QUA TÀI KHOẢN LẠ: Nhận tiền người quen rồi chuyển tiếp cho bên thứ ba là kẽ hở cực lớn",
            "ĐỪNG BỎ QUA CẢNH BÁO ĐĂNG NHẬP LẠ: Kiểm tra thiết bị ngay; nếu đã lỡ chuyển tiền, gọi tổng đài ngân hàng và trình báo công an",
        ],
        "action": "Trước mọi yêu cầu tiền bạc kèm lời dặn 'giữ bí mật, đừng nói với ai', hãy gọi trực tiếp số thật hoặc gặp mặt và hỏi thẳng đúng yêu cầu đó.",
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
            {"start": marks["hook_freeze"] - 0.2, "end": marks["hook_freeze"] + 3.0, "bgm_db": -12, "amb_db": -8},
            {"start": marks["two_phones"] - 0.2, "end": marks["two_phones"] + 10.0, "bgm_db": -11, "amb_db": -8},
            {"start": marks["money_loop"] - 0.2, "end": marks["money_loop"] + 4.0, "bgm_db": -10, "amb_db": -7},
            {"start": marks["confrontation"] - 0.2, "end": marks["confrontation"] + 14.0, "bgm_db": -11, "amb_db": -7},
            {"start": marks["quiet_aftermath"] - 0.2, "end": marks["rf_start"] - 0.2, "bgm_db": -10, "amb_db": -7},
            {"start": marks["silent_crack"] - 0.2, "end": marks["disc_start"] - 0.2, "bgm_db": -5, "amb_db": -9},
            {"start": marks["disc_start"], "end": total - 0.05},
        ],
    },
    "forbidden_terms": [],
    "publish": {
        "titles": [
            "Thấy Đúng Mặt, Gọi Đúng Số Thật Vẫn Mất 45 Triệu – Bẫy Người Đứng Giữa | Bóc Trần Lừa Đảo",
            "Một Vòng Tiền, Hai Nửa Sự Thật: Khi Sếp Và Nhân Viên Cùng Tự Tay Chuyển Tiền Cho Kẻ Gian | Bóc Trần Lừa Đảo",
            "Nick Mới Nhái Y Chang Cách Nói Chuyện Của Sếp – Gọi Số Thật Sao Vẫn Sập Bẫy? | Bóc Trần Lừa Đảo",
        ],
        "description": (
            "Thấy đúng mặt sếp qua cuộc gọi hình 3 giây chập chờn, tin nhắn nhái y hệt cách xưng hô thường ngày, "
            "rồi chính nhân viên gọi thẳng vào số điện thoại thật của sếp — nhưng 45 triệu đồng vẫn đi trọn một vòng rồi biến mất vào tài khoản lạ.\n\n"
            "⏱️ Các hồi trong phim:\n" + desc_chapters
        ),
        "pinned_comment": (
            "📌 Theo bạn, sau câu nói ở cuối phim trên bàn cà phê, hai anh em có còn làm việc chung với nhau được nữa không? "
            "Chia sẻ góc nhìn ở bình luận để mọi người cùng cảnh giác nhé (lưu ý không đăng SĐT, STK hay tên người thật)."
        ),
        "hashtags": ["#bóctrầnlừađảo", "#cảnhgiáclừađảo", "#vạnchuyện", "#antoànmạng", "#ngườiđứnggiữa"],
        "tags": [
            "cảnh giác lừa đảo", "bóc trần lừa đảo", "vạn chuyện", "lừa đảo người đứng giữa",
            "cuộc gọi hình ghép", "giả mạo tài khoản người quen", "chuyển tiền đường vòng", "an toàn mạng",
        ],
        "category": "Education (Giáo dục)",
        "playlist": "Hồ Sơ Bóc Trần Lừa Đảo – Phim Dài Chuyên Sâu",
        "thumbnail_sec": round(marks["confrontation"] + 21.1, 2),
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
