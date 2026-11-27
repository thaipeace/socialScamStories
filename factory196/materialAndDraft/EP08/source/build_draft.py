# -*- coding: utf-8 -*-
"""
Trình biên dịch `factory196/materialAndDraft/EP08/episode.json` – Tập EP08:
"Một vòng tiền, hai nửa sự thật" (16:9 Long-form · Visual Motion Level 3 + Living-Character 2.5).

Chuẩn Luật Kế Thừa Cộng Dồn HRN-MOTION-L3.0 (CHECK 1 -> CHECK 2 -> CHECK 3):
  - CHECK 1 (Level 1): Bảo toàn 100% 32 câu thoại TTS thật (242.15s), 9 chat bubbles, 1 notification,
    5 chapters, red_flags, disclaimer, ambience, bgm, duck_extra, toàn bộ foley gốc + detail_reveal gốc.
  - CHECK 2 (Level 2 cốt lõi):
      * 3 cảnh 2.5D Parallax Level B (s00, s03, s14b) + Breathing + Rack Focus + Head Micro-Tilt
      * 17 rig chớp mắt (eye_blink) & 15 rig chép miệng khớp .wav thật (mouth_sync, gồm 4 rig 4 trạng thái round_image)
        phủ 100% toàn bộ các cảnh thoại trực tiếp (kể cả khuôn mặt Anh Đạt giả trên màn hình điện thoại s04
        và lớp bg 2.5D của Khang ở s14b), khóa pixel qua 03_ENGINE/face_roi_prep.py với ngưỡng nhạy thresh_mid=0.11 / thresh_open=0.52.
  - CHECK 3 (Level 3 Đạo diễn & Không khí):
      * Đồ họa vật chứng: red_circle_draw, animated_counter, phone_waveform, typing_indicator
      * Không khí & Màu phim: ambient_particles, light_sweep, screen_glow, color_mood, chromatic_pulse
      * Chuyển cảnh điện ảnh: zoom_punch, whip_pan_left/right, film_burn, luma_wipe

Nguồn sự thật duy nhất của timeline:
    python factory196/materialAndDraft/EP08/source/build_draft.py
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


def asset_exists(rel_path: str) -> bool:
    return (EP / rel_path).is_file()


real = {p.stem: wav_dur(p.stem) for p in TTS.glob("*.wav")} if TTS.is_dir() else {}
real = {k: v for k, v in real.items() if v}

# Pixel-locked Living-Character ROI config produced by 03_ENGINE/face_roi_prep.py
ROI_CFG_PATH = HERE / "face_rois.json"
FACE_ROIS: dict = json.loads(ROI_CFG_PATH.read_text(encoding="utf-8")) if ROI_CFG_PATH.is_file() else {}

# ---------------------------------------------------------------- GIỌNG
# 7 tuyến nhân vật = 7 voice hoàn toàn tách biệt trong 02_CAST/cast.json (KHÔNG sửa chữ/style để giữ nguyên TTS Gate 2)
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


def build_char_fx(scene_key: str, specs: list[dict], region_space: str | None = None) -> list[dict]:
    """Build pixel-locked eye_blink and 3/4-state mouth_sync dicts from source/face_rois.json."""
    cfg = FACE_ROIS.get(scene_key) or {}
    out: list[dict] = []
    for sp in specs:
        ch = sp["char"]
        c = cfg.get(ch)
        if not c:
            continue
        if sp.get("blink", True) and "blink" in c and asset_exists(c["blink"]["image"]):
            fx_b: dict = {
                "type": "eye_blink",
                "image": c["blink"]["image"],
                "region": c["blink"]["region"],
                "first_offset": sp.get("first_offset", 1.5),
                "interval": sp.get("interval", 3.9),
                "feather": 0.006,
                "close_dur": 0.055,
                "hold_dur": 0.045,
                "open_dur": 0.085,
            }
            if sp.get("layer"):
                fx_b["layer"] = sp["layer"]
            if region_space:
                fx_b["region_space"] = region_space
            out.append(fx_b)
        if sp.get("line_ids") and "mouth" in c:
            mc = c["mouth"]
            if all(asset_exists(mc[k]) for k in ("closed_image", "mid_image", "open_image")):
                fx_m: dict = {
                    "type": "mouth_sync",
                    "speaker": sp["speaker"],
                    "line_ids": sp["line_ids"],
                    "region": mc["region"],
                    "default_state": mc.get("default_state", "closed"),
                    "closed_image": mc["closed_image"],
                    "mid_image": mc["mid_image"],
                    "open_image": mc["open_image"],
                    "feather": 0.006,
                    "thresh_mid": 0.11,
                    "thresh_open": 0.52,
                }
                if mc.get("round_image") and asset_exists(mc["round_image"]):
                    fx_m["round_image"] = mc["round_image"]
                if sp.get("layer"):
                    fx_m["layer"] = sp["layer"]
                if region_space:
                    fx_m["region_space"] = region_space
                out.append(fx_m)
    return out


MOTION = {
    "static_hold": {"preset": "static_hold"},
    "pan_right": {"preset": "pan_right", "scale": [1.06, 1.06], "focus": [[0.46, 0.49], [0.54, 0.49]], "wobble": "none", "easing": "smoothstep"},
    "pan_left": {"preset": "pan_left", "scale": [1.06, 1.06], "focus": [[0.54, 0.50], [0.47, 0.50]], "wobble": "none", "easing": "smoothstep"},
    "pull_out": {"preset": "slow_pull_out", "scale": [1.07, 1.02], "focus": [[0.50, 0.48], [0.50, 0.50]], "wobble": "none", "easing": "smoothstep"},
    "pull_out_right": {"preset": "slow_pull_out", "scale": [1.08, 1.02], "focus": [[0.58, 0.50], [0.51, 0.50]], "wobble": "none", "easing": "smoothstep"},
    "pull_confront": {"preset": "slow_pull_out", "scale": [1.08, 1.02], "focus": [[0.50, 0.52], [0.50, 0.49]], "wobble": "calm", "easing": "smoothstep"},
    "push_dark": {"preset": "slow_push_in", "scale": [1.02, 1.08], "focus": [[0.50, 0.50], [0.48, 0.55]], "wobble": "none", "easing": "ease_out"},
    "push_right_soft": {"preset": "subtle_push_right", "scale": [1.02, 1.08], "focus": [[0.50, 0.49], [0.56, 0.48]], "wobble": "breathe", "easing": "ease_out"},
    "push_left_coda": {"preset": "subtle_push_left", "scale": [1.02, 1.08], "focus": [[0.42, 0.44], [0.36, 0.40]], "wobble": "none", "easing": "ease_out"},
    "push_right_coda": {"preset": "subtle_push_right", "scale": [1.02, 1.08], "focus": [[0.60, 0.42], [0.66, 0.38]], "wobble": "none", "easing": "ease_out"},
    "tense_call": {"preset": "tense_push", "scale": [1.03, 1.09], "focus": [[0.50, 0.49], [0.50, 0.45]], "wobble": "tense", "easing": "ease_in"},
}

E: list[tuple[str, object]] = []


def scene(sid: str, img: str, m: str = "pan_right", beat_type: str = "normal", level: str = "C",
          intent: str = "", tr: str | None = None, trd: float = 0.4, shake: float | None = None,
          parallax: dict | None = None):
    E.append(("scene", dict(
        id=sid, image=img, motion=MOTION[m], beat_type=beat_type, level=level,
        intent=intent, tr=tr, trd=trd, shake=shake, parallax=parallax,
    )))


def living(scene_key: str, specs: list[dict]):
    E.append(("living", dict(scene_key=scene_key, specs=specs)))


def fx(fx_dict: dict):
    E.append(("fx", fx_dict))


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


def sfx_abs(preset: str, at: float, gain: float = -5.0, dur: float | None = None):
    E.append(("sfx_abs", dict(preset=preset, at=at, gain=gain, dur=dur)))


def amb(preset: str, gain: float = -2.0):
    E.append(("amb", dict(preset=preset, gain=gain)))


def bgm(preset: str, gain: float = -3.0):
    E.append(("bgm", dict(preset=preset, gain=gain)))


def mark(name: str):
    E.append(("mark", name))


SILENT = -40.0
EP01B = "factory196/materialAndDraft/EP01b/assets/"

# ================================================================ STORY
# ---- HOOK · CUỘC GỌI LẦN HAI & CÂU HỎI ĐÓNG BĂNG (00:00 – 00:18.73) ----
amb("office", -2.5); bgm("suspense_pulse", -2.5)
scene(
    "s00_hook_call", "assets/c00.jpg", "push_right_soft", beat_type="suspicion", level="B",
    intent="2.5D Parallax phòng xưởng chiều: Rack Focus mờ hậu cảnh + Breathing + Head Micro-Tilt + Anh Đạt chớp mắt & chép miệng 4 trạng thái (fg) + bộ đếm 45tr -> 75tr + sóng âm Khang + Chromatic Pulse",
    shake=0.2,
    parallax={
        "camera": "push_in",
        "dolly": [1.02, 1.08],
        "shift_x": [0.0, 0.0],
        "shift_y": [0.0, -3.5],
        "focus": [0.64, 0.46],
        "strength": 0.90,
        "easing": "ease_out",
        "layers": [
            {"role": "bg", "image": "assets/s00_bg.jpg", "depth": 0.40, "blur_from": 0.4, "blur_to": 3.2, "blur_at": 6.5, "blur_dur": 3.5},
            {"role": "fg", "image": "assets/s00_fg.png", "depth": 1.24, "breathe_y": 2.0, "breathe_period": 3.4,
             "head_tilt_deg": 1.0, "head_pivot": [0.66, 0.88], "tilt_speaker": "anh_hai", "tilt_line_ids": ["l01_dat", "l03_dat"]},
        ],
    },
)
living("c00", [dict(char="dat", speaker="anh_hai", line_ids=["l01_dat", "l03_dat"], first_offset=1.3, interval=3.8, layer="fg")])
fx({"type": "chromatic_pulse", "at": 0.25, "dur": 0.28, "shift_px": 6, "zoom_blur": 0.02})
fx({"type": "animated_counter", "start": 5.5, "end": 12.8, "count_dur": 1.6,
    "from_val": 45000000, "to_val": 75000000, "fmt": "vnd", "label": "TỔNG YÊU CẦU TRONG NGÀY",
    "pos": [0.24, 0.34], "style": "danger", "easing": "ease_out"})
fx({"type": "phone_waveform", "speaker": "thang_tun", "line_ids": ["l02_khang_p"],
    "start": 8.4, "end": 12.8, "pos": [0.24, 0.56], "size": [0.25, 0.058],
    "color": [255, 195, 80], "label": "KHANG · ĐIỆN THOẠI"})
fx({"type": "color_mood", "mood": "cold_suspicion", "strength": 0.32, "vignette": 0.16, "grain": 0.008})
sfx("phone_ring", 0.15, -4, dur=1.2)
sfx_abs("counter_tick", 5.50, -5.5)
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

scene(
    "s01_hook_freeze", "assets/c01.jpg", "static_hold", beat_type="anomaly", level="C",
    intent="Cú sốc Zoom Punch đứng hình: Khang chớp mắt sững người + focus_highlight + screen_glow + Chromatic Pulse lạnh gáy",
    tr="zoom_punch", trd=0.24, shake=0.15,
)
living("c01", [dict(char="khang", first_offset=1.0, interval=3.6)])
fx({"type": "chromatic_pulse", "at": 15.45, "dur": 0.30, "shift_px": 7, "zoom_blur": 0.025})
fx({"type": "color_mood", "mood": "high_tension", "strength": 0.45, "vignette": 0.22, "grain": 0.012})
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
scene(
    "s02_trust_coffee", "assets/c02.jpg", "pan_right", beat_type="establishing", level="C",
    intent="Chuyển hồi Film Burn về quán cà phê sáng 2 hôm trước: Anh Đạt & Khang đều chớp mắt + chép miệng đối thoại thân tình + hạt nắng sớm ấm áp",
    tr="film_burn", trd=0.45,
)
living("c02", [
    dict(char="dat", speaker="anh_hai", line_ids=["l04_dat", "l06_dat"], first_offset=1.4, interval=4.0),
    dict(char="khang", speaker="thang_tun", line_ids=["l05_khang", "l07_khang"], first_offset=2.3, interval=4.2),
])
fx({"type": "ambient_particles", "count": 20, "opacity": 0.24, "color": [255, 240, 190], "drift_dir": "float", "seed": 82})
fx({"type": "color_mood", "mood": "warm_daily", "strength": 0.56, "vignette": 0.08, "grain": 0.0})
chapter("HỒI 1 · HAI HÔM TRƯỚC", "CÁCH NÓI CHUYỆN & KẾ HOẠCH PHÒNG TỐI")
sfx("chapter_sting", -0.1, -5)
beat(0.8)
line("l04_dat", "DAT", "Nè cu Khang, mấy công trình đợt này mày chạy gọn ghẽ quá. Cuối tháng anh tính thêm cho.",
     "cười thoải mái bên ly cà phê sáng, nói cộc gọn đầy tin cậy")
line("l05_khang", "KHANG", "Anh em làm chung ba năm rồi, tính toán chi anh. Có việc gì cứ kêu em.",
     "cười tươi, lễ phép và rất quý sếp")
line("l06_dat", "DAT", "Ừ, tuần sau kỷ niệm mười năm ngày cưới. Rảnh phụ anh kiếm quà cho chị nhà, đừng để bả biết lộ bài nghen.",
     "hạ giọng vui vẻ, dặn dò thân mật đúng kiểu người đàn ông thực dụng",
     sub="Ừ, tuần sau kỷ niệm 10 năm ngày cưới. Rảnh phụ anh kiếm quà cho chị nhà, đừng để bả biết lộ bài nghen.")
line("l07_khang", "KHANG", "Dạ dễ ợt, anh chọn xong cứ nhắn em làm gọn.",
     "gật đầu nhanh nhẹn, tự tin", pause=0.3)

# Phòng tối ánh xanh lạnh: 2.5D Parallax + Rack Focus + Breathing + sóng âm đối thoại 2 kẻ gian
amb("night_room", -2.5); bgm("tension_drone", -2.8)
scene(
    "s03_dark_room_plan", "assets/c03.jpg", "push_dark", beat_type="suspicion", level="B",
    intent="2.5D Parallax phòng tối ánh xanh lạnh + Rack Focus + Breathing + sóng âm đối thoại kẻ đứng giữa & đàn em + Noir Evidence",
    tr="luma_wipe", trd=0.40,
    parallax={
        "camera": "push_in",
        "dolly": [1.02, 1.07],
        "shift_x": [0.0, 0.0],
        "shift_y": [0.0, -3.0],
        "focus": [0.48, 0.56],
        "strength": 0.85,
        "easing": "ease_out",
        "layers": [
            {"role": "bg", "image": "assets/s03_bg.jpg", "depth": 0.40, "blur_from": 0.5, "blur_to": 2.8, "blur_at": 45.0, "blur_dur": 4.0},
            {"role": "fg", "image": "assets/s03_fg.png", "depth": 1.35, "breathe_y": 1.6, "breathe_period": 3.8},
        ],
    },
)
fx({"type": "phone_waveform", "speaker": "chu_no", "line_ids": ["l08_tech", "l09_ke"],
    "start": 43.6, "end": 56.5, "pos": [0.22, 0.72], "size": [0.25, 0.056],
    "color": [95, 215, 245], "label": "PHÒNG TỐI · KẾ HOẠCH"})
fx({"type": "color_mood", "mood": "noir_evidence", "strength": 0.56, "vignette": 0.24, "grain": 0.014})
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
scene(
    "s04_fake_video_call", "assets/c04.jpg", "static_hold", beat_type="anomaly", level="C",
    intent="Cuộc gọi hình ghép 3 giây: Khang chớp mắt + khuôn mặt Đạt giả trên màn hình điện thoại chép miệng khớp giọng cắt ghép + khoanh đỏ màn hình + tắt kính đen detail_reveal",
    tr="whip_pan_left", trd=0.30,
)
# Đặt living() TRƯỚC detail_reveal để khi màn hình tắt đen (c04_call_off.jpg) phủ sạch lên trên
living("c04", [
    dict(char="khang", first_offset=1.2, interval=3.8),
    dict(char="fake_dat", speaker="anh_hai", line_ids=["l12_dat_fake"], blink=False),
])
fx({"type": "red_circle_draw", "region": [0.47, 0.25, 0.70, 0.79], "at": 59.3, "dur": 0.45, "end": 65.5,
    "style": "box", "width": 5, "color": [248, 60, 60]})
fx({"type": "chromatic_pulse", "at": 59.15, "dur": 0.28, "shift_px": 7, "zoom_blur": 0.022})
fx({"type": "color_mood", "mood": "cold_suspicion", "strength": 0.34, "vignette": 0.14, "grain": 0.010})
sfx_abs("marker_draw", 59.30, -5.0)
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
scene(
    "s05_fake_step1_dark", "assets/c05_dim.jpg", "pan_left", beat_type="information", level="C",
    intent="Phòng tối gõ Nhịp 1: màn hình bật sáng detail_reveal + typing_indicator + sóng âm kẻ đứng giữa + Noir Evidence",
    tr="dissolve", trd=0.30,
)
fx({"type": "typing_indicator", "start": 66.85, "end": 67.30, "side": "left", "y": 260})
fx({"type": "phone_waveform", "speaker": "chu_no", "line_ids": ["l13_ke", "l14_ke"],
    "start": 67.6, "end": 82.8, "pos": [0.24, 0.56], "size": [0.25, 0.058],
    "color": [95, 210, 245], "label": "KẺ ĐỨNG GIỮA · NHÁI GIỌNG"})
fx({"type": "color_mood", "mood": "noir_evidence", "strength": 0.50, "vignette": 0.20, "grain": 0.012})
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

# Cắt về văn phòng sáng nắng: Khang & Hân đối thoại tự nhiên
amb("office", -3.0); bgm("investigative_story", -4.0)
scene(
    "s06_office_relay", "assets/c06.jpg", "pull_out", beat_type="normal", level="C",
    intent="Văn phòng sáng nắng: cả Khang & Hân đều chớp mắt + chép miệng trò chuyện tự nhiên + hạt nắng ấm",
    tr="whip_pan_right", trd=0.30,
)
living("c06", [
    dict(char="han", speaker="chi_tu", line_ids=["l15_han", "l17_han"], first_offset=1.3, interval=3.9),
    dict(char="khang", speaker="thang_tun", line_ids=["l16_khang"], first_offset=2.1, interval=4.1),
])
fx({"type": "ambient_particles", "count": 18, "opacity": 0.22, "color": [255, 240, 195], "drift_dir": "float", "seed": 86})
fx({"type": "color_mood", "mood": "warm_daily", "strength": 0.50, "vignette": 0.08, "grain": 0.0})
beat(0.5)
line("l15_han", "HAN", "Ủa Khang, ôm điện thoại cười tủm tỉm gì đó? Có bồ rồi hả?",
     "ngước từ bàn bên nhìn qua, cười chọc nhẹ tự nhiên")
line("l16_khang", "KHANG", "Đâu có. Sếp nhờ phụ đặt quà cho chị nhà, kêu giữ kín kẻo lộ.",
     "cười xòa, hạ giọng thoải mái không chút nghi ngờ")
line("l17_han", "HAN", "Sếp chiều vợ ghê ha. Ráng làm gọn cho ổng đi.",
     "cười gật nhẹ quay lại màn hình, đời thường không kịch", pause=0.35)

# ---- HỒI 3 · BUỔI TRƯA: DÒNG TIỀN ĐI MỘT VÒNG ----
amb("room_tone", -3.0); bgm("investigative_story", -3.5)
scene(
    "s07_real_call_home", "assets/c07.jpg", "pan_right", beat_type="normal", level="C",
    intent="Mâm cơm trưa nhà Anh Đạt: Anh Đạt & Chị Quyên chớp mắt + chép miệng đối thoại + sóng âm Khang gọi + bộ đếm -45.000.000đ",
    tr="luma_wipe", trd=0.42,
)
living("c07", [
    dict(char="dat", speaker="anh_hai", line_ids=["l20_dat", "l22_dat"], first_offset=1.5, interval=4.0),
    dict(char="quyen", speaker="chi_hai", line_ids=["l21_quyen"], first_offset=2.4, interval=4.2),
])
fx({"type": "phone_waveform", "speaker": "thang_tun", "line_ids": ["l19_khang_p"],
    "start": 100.5, "end": 106.2, "pos": [0.24, 0.56], "size": [0.25, 0.058],
    "color": [105, 205, 245], "label": "KHANG · GỌI SỐ THẬT"})
fx({"type": "animated_counter", "start": 118.4, "end": 124.2, "count_dur": 1.6,
    "from_val": 0, "to_val": -45000000, "fmt": "vnd", "label": "BƯỚC 1 · ĐẠT → KHANG",
    "pos": [0.24, 0.58], "style": "warn", "easing": "ease_out"})
fx({"type": "ambient_particles", "count": 16, "opacity": 0.20, "color": [255, 238, 195], "drift_dir": "float", "seed": 87})
fx({"type": "color_mood", "mood": "warm_daily", "strength": 0.52, "vignette": 0.08, "grain": 0.0})
sfx_abs("counter_tick", 118.40, -5.5)
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

# Cắt chéo sang phòng tối: gửi STK lạ
amb("night_room", -2.5); bgm("suspense_pulse", -2.5)
scene(
    "s08_dark_step2_account", "assets/c08_dim.jpg", "push_right_soft", beat_type="information", level="C",
    intent="Phòng tối gửi STK lạ: màn hình bật sáng detail_reveal + sóng âm kẻ đứng giữa + Noir Evidence",
    tr="whip_pan_left", trd=0.28,
)
fx({"type": "phone_waveform", "speaker": "chu_no", "line_ids": ["l23_ke"],
    "start": 125.2, "end": 133.5, "pos": [0.24, 0.56], "size": [0.25, 0.058],
    "color": [255, 195, 85], "label": "KẺ ĐỨNG GIỮA · GỬI STK LẠ"})
fx({"type": "color_mood", "mood": "noir_evidence", "strength": 0.52, "vignette": 0.22, "grain": 0.012})
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
scene(
    "s09_khang_transfers", "assets/c09.jpg", "static_hold", beat_type="climax", level="C",
    intent="Khoảnh khắc Khang bấm chuyển 45 triệu: Khang chớp mắt vô tư + bộ đếm -45.000.000đ + Chromatic Pulse khớp bank_ting + focus_highlight",
    tr="dissolve", trd=0.30,
)
living("c09", [dict(char="khang", first_offset=0.9, interval=3.5)])
fx({"type": "animated_counter", "start": 135.2, "end": 138.3, "count_dur": 1.4,
    "from_val": 0, "to_val": -45000000, "fmt": "vnd", "label": "BƯỚC 3 · KHANG → KẺ GIAN",
    "pos": [0.24, 0.58], "style": "danger", "easing": "ease_out"})
fx({"type": "chromatic_pulse", "at": 135.25, "dur": 0.28, "shift_px": 6, "zoom_blur": 0.02})
fx({"type": "color_mood", "mood": "cold_suspicion", "strength": 0.34, "vignette": 0.16, "grain": 0.010})
sfx_abs("counter_tick", 135.20, -5.0)
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
scene(
    "s10_second_attempt_dark", "assets/c10.jpg", "pull_out_right", beat_type="suspicion", level="C",
    intent="Nhịp 2 phòng tối: typing_indicator + sóng âm đòi thêm 30 triệu + ánh sáng quét + High Tension",
    tr="luma_wipe", trd=0.40,
)
fx({"type": "typing_indicator", "start": 138.60, "end": 139.05, "side": "left", "y": 260})
fx({"type": "phone_waveform", "speaker": "chu_no", "line_ids": ["l24_ke"],
    "start": 139.4, "end": 147.8, "pos": [0.24, 0.56], "size": [0.25, 0.058],
    "color": [255, 95, 85], "label": "KẺ ĐỨNG GIỮA · ĐÒI THÊM 30TR"})
fx({"type": "light_sweep", "mode": "light", "color": [125, 195, 245], "intensity": 0.14, "width": 0.20, "angle_deg": -18.0, "repeat": 1})
fx({"type": "color_mood", "mood": "high_tension", "strength": 0.48, "vignette": 0.22, "grain": 0.012})
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
scene(
    "s11_real_call_suspect", "assets/c11.jpg", "tense_call", beat_type="climax", level="C",
    intent="Đẩy gấp cao trào: Anh Đạt chớp mắt & chép miệng 4 trạng thái quát gấp + Whip Pan + Chromatic Pulse + High Tension",
    tr="whip_pan_left", trd=0.26,
)
living("c11", [dict(char="dat", speaker="anh_hai", line_ids=["l25_dat"], first_offset=1.0, interval=3.8)])
fx({"type": "chromatic_pulse", "at": 148.55, "dur": 0.28, "shift_px": 6, "zoom_blur": 0.022})
fx({"type": "color_mood", "mood": "high_tension", "strength": 0.46, "vignette": 0.20, "grain": 0.012})
sfx("riser", 0.0, -4, dur=1.0)
beat(0.45)
line("l25_dat", "DAT", "Mày đứng yên đó, chạy thẳng qua phòng anh ngay! Đem cái điện thoại qua đây cho anh coi!",
     "gấp gáp, nghiêm giọng dứt khoát")
sfx("call_end", 0.0, -3)
beat(0.55)

# Đối chất trực diện: hai điện thoại đặt cạnh nhau trên bàn
amb("office", -3.0); bgm("action_climax", -2.2)
scene(
    "s12_confrontation_desk", "assets/c12.jpg", "pull_confront", beat_type="climax", level="C",
    intent="Cao trào đối chất Trái–Phải: Anh Đạt & Khang chớp mắt + chép miệng đối thoại căng thẳng + khoanh đỏ 2 điện thoại trên bàn + Zoom Punch + Chromatic Pulse",
    tr="zoom_punch", trd=0.26, shake=0.18,
)
living("c12", [
    dict(char="khang", speaker="thang_tun", line_ids=["l26_khang", "l29_khang"], first_offset=1.2, interval=3.8),
    dict(char="dat", speaker="anh_hai", line_ids=["l27_dat", "l28_dat", "l30_dat"], first_offset=2.1, interval=4.1),
])
fx({"type": "red_circle_draw", "region": [0.35, 0.82, 0.65, 0.94], "at": 162.2, "dur": 0.50, "end": 175.0,
    "style": "box", "width": 5, "color": [248, 58, 58]})
fx({"type": "chromatic_pulse", "at": 175.35, "dur": 0.30, "shift_px": 7, "zoom_blur": 0.024})
fx({"type": "color_mood", "mood": "high_tension", "strength": 0.42, "vignette": 0.18, "grain": 0.012})
sfx_abs("marker_draw", 162.20, -4.5)
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
scene(
    "s13_coffee_aftermath", "assets/c13.jpg", "pan_left", beat_type="aftermath", level="C",
    intent="Chuyển cảnh Film Burn về bàn cà phê cũ: quét ngược pan_left + Anh Đạt & Khang chớp mắt + chép miệng trầm buồn + Cold Suspicion dịu",
    tr="film_burn", trd=0.50,
)
living("c13", [
    dict(char="khang", speaker="thang_tun", line_ids=["l31_khang"], first_offset=1.4, interval=4.1),
    dict(char="dat", speaker="anh_hai", line_ids=["l32_dat"], first_offset=2.3, interval=4.2),
])
fx({"type": "color_mood", "mood": "cold_suspicion", "strength": 0.34, "vignette": 0.14, "grain": 0.008})
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
scene(
    "s16_red_flags", EP01B + "scene18.jpg", "static_hold", beat_type="ending", level="A",
    intent="Giữ tĩnh tuyệt đối để khán giả tập trung đọc thẻ Nhớ kỹ",
    tr="dissolve", trd=0.40,
)
mark("rf_start")
sfx("bank_ting", 0.0, -5)
line("l35_narr", "N", "Mặt, giọng hay cách nói đều giả được. Cứ dính tiền mà dặn giữ bí mật, hãy gọi số thật hỏi thẳng.")
beat(1.0)
mark("rf_end")

# ---- KẾT MỞ SAU THẺ NHỚ · CÚ LẬT RẠN NỨT LÒNG TIN ----
amb("street", -5.5); bgm("tension_drone", -1.4)
scene(
    "s14a_coda_dat_probe", "assets/c14a.jpg", "push_left_coda", beat_type="suspicion", level="C",
    intent="Cận mặt lạnh gáy Anh Đạt: chớp mắt & chép miệng 4 trạng thái bỏ chữ 'cu' + focus_highlight + Noir Evidence",
    tr="luma_wipe", trd=0.45,
)
living("c14a", [dict(char="dat", speaker="anh_hai", line_ids=["l33_dat"], first_offset=1.3, interval=4.0)])
fx({"type": "color_mood", "mood": "noir_evidence", "strength": 0.42, "vignette": 0.22, "grain": 0.012})
mark("silent_crack")
sfx("low_accent", 0.9, -4.0)
detail("focus_highlight", offset_start=0.8, end_scene=True, pos=[0.35, 0.38], radius=[0.28, 0.36], dim_outer=0.22, fade=0.55)
beat(1.6)
line("l33_dat", "DAT", "À Khang… Sao kê chỉ ghi anh cho em ứng lương. Đừng xóa tin nhắn giả hôm qua, gửi anh giữ làm bằng.",
     "bỏ hẳn chữ cu, hạ giọng trầm hẳn và lạnh băng, mắt dò xét, nhả từng chữ sắc và nặng như giữ bằng chứng phòng thân",
     pause=0.9)

amb("room_tone", -5.0); bgm("tension_drone", -1.2)
scene(
    "s14b_coda_khang_counter", "assets/c14b.jpg", "push_right_coda", beat_type="climax", level="B",
    intent="2.5D Parallax vượt vai mờ Anh Đạt tiến thẳng vào Khang + Rack Focus + Breathing + Khang chớp mắt & chép miệng 4 trạng thái (layer bg) + Chromatic Pulse + Noir Evidence",
    tr="whip_pan_right", trd=0.26,
    parallax={
        "camera": "push_in",
        "dolly": [1.02, 1.09],
        "shift_x": [-8.0, 10.0],
        "shift_y": [0.0, -4.0],
        "focus": [0.62, 0.40],
        "strength": 1.0,
        "easing": "ease_out",
        "layers": [
            {"role": "bg", "image": "assets/s14b_bg.jpg", "depth": 0.60, "breathe_y": 1.4, "breathe_period": 3.6},
            {"role": "fg", "image": "assets/s14b_fg.png", "depth": 1.45, "blur_from": 0.8, "blur_to": 3.4, "blur_at": 228.5, "blur_dur": 3.5},
        ],
    },
)
living("c14b", [dict(char="khang", speaker="thang_tun", line_ids=["l34_khang"], first_offset=1.2, interval=3.9, layer="bg")])
fx({"type": "chromatic_pulse", "at": 234.65, "dur": 0.28, "shift_px": 7, "zoom_blur": 0.025})
fx({"type": "color_mood", "mood": "noir_evidence", "strength": 0.48, "vignette": 0.24, "grain": 0.014})
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
scene(
    "s15_black_cut", "assets/c15.jpg", "static_hold", beat_type="aftermath", level="A",
    intent="Cắt đen tĩnh tuyệt đối tạo khoảng lặng sau cú chốt cuối phim",
    tr="cut", trd=0.0,
)
beat(2.2)

# ---- DISCLAIMER ----
amb("room_tone", -6.0); bgm("tension_drone", -8.0)
scene(
    "s17_disclaimer", EP01B + "scene18.jpg", "static_hold", beat_type="ending", level="A",
    intent="Giữ tĩnh sạch sẽ cho bảng Lưu ý cuối phim",
    tr="fade_black", trd=0.35,
)
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
        sc: dict = {
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
            px = d["parallax"]
            if all(asset_exists(ly["image"]) for ly in px.get("layers", [])):
                sc["parallax"] = px
            elif sc["motion_level"] == "B":
                sc["motion_level"] = "C"
        if d["tr"]:
            sc["transition_in"] = {"type": d["tr"], "dur": d["trd"]}
        if d["shake"] is not None:
            sc["shakes"] = [{"at": round(t + d["shake"], 2), "dur": 0.4, "amp": 16}]
        sc["detail_fx"] = []
        scenes.append(sc)
        t += SCENE_LEAD
    elif kind == "living":
        scenes[-1]["detail_fx"].extend(build_char_fx(d["scene_key"], d["specs"]))
    elif kind == "fx":
        scenes[-1]["detail_fx"].append(d)
    elif kind == "detail":
        fxd = {"type": d["type"], **d["kwargs"]}
        if d["offset_start"] is not None:
            fxd["start"] = round(max(0.0, t + d["offset_start"]), 2)
        if d["offset_end"] is not None:
            fxd["end"] = round(max(0.0, t + d["offset_end"]), 2)
        if d["offset_at"] is not None:
            fxd["at"] = round(max(0.0, t + d["offset_at"]), 2)
        if d["dur"] is not None:
            fxd["dur"] = d["dur"]
        if d["end_scene"]:
            fxd["_end_scene"] = True
        scenes[-1]["detail_fx"].append(fxd)
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
    elif kind == "sfx_abs":
        f = {"preset": d["preset"], "at": round(d["at"], 2), "gain_db": d["gain"]}
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
foley.sort(key=lambda item: float(item["at"]))


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
    "version": "v6-level3-full-abc-staging",
    "motion_upgrade": "level3",
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
    f"episode.json (v6-level3-full-abc-staging): {total:.2f}s ({mmss(total)}) · {len(scenes)} cảnh · "
    f"{len(dialogue)} câu · {words} từ ({words / (total / 60):.0f} từ/phút) · câu dài nhất {maxw} từ · "
    f"Bóc trần {len(narr_lines)} câu ({narr} từ, thẻ kết {rf_dur}s) · "
    f"{'TTS thật' if real else 'ước tính'} ({len(real)} câu thật)"
)
print(desc_chapters)
