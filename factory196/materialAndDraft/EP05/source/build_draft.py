# -*- coding: utf-8 -*-
"""
Trình biên dịch `factory196/materialAndDraft/EP05/episode.json` – Tập EP05:
"Tờ năm trăm và sáu giây nhìn thẳng" (16:9 Long-form · Visual Motion Level 3 + Living-Character 2.5).

Chuẩn Luật Kế Thừa Cộng Dồn HRN-MOTION-L3.0 (CHECK 1 -> CHECK 2 -> CHECK 3):
  - CHECK 1 (Level 1): Bảo toàn 100% 34 câu thoại TTS thật (262.08s), 7 chat bubbles, 5 chapters,
    red_flags, disclaimer, ambience, bgm, duck_extra, 26 foley gốc (+ 10 foley Level 3 = 36).
  - CHECK 2 (Level 2 cốt lõi):
      * 4 cảnh 2.5D Parallax Level B (s00, s01, s06, s10b) + Breathing + Rack Focus + Head Micro-Tilt
      * 25 rig chớp mắt (eye_blink) & 19 rig chép miệng khớp .wav thật (mouth_sync, gồm 6 cảnh 4 trạng thái round_image)
        khóa pixel qua 03_ENGINE/face_roi_prep.py (cả trên lớp 2.5D fg/bg lẫn trong Split-Screen s10a!)
  - CHECK 3 (Level 3 Đạo diễn & Không khí):
      * Split-Screen đối đầu s10a (kèm eye_blink & mouth_sync 4 trạng thái trực tiếp trên 2 panel)
      * Đồ họa vật chứng: red_circle_draw, animated_counter, phone_waveform, typing_indicator
      * Không khí & Màu phim: rain_layer, light_sweep, ambient_particles, color_mood, chromatic_pulse
      * Chuyển cảnh điện ảnh: zoom_punch, whip_pan_left/right, film_burn, luma_wipe

Nguồn sự thật duy nhất của timeline:
    python factory196/materialAndDraft/EP05/source/build_draft.py
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
# 9 nhân vật = 9 voice hoàn toàn tách biệt trong 02_CAST/cast.json (KHÔNG sửa chữ/style để giữ nguyên TTS Gate 2)
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
                    "thresh_mid": 0.14,
                    "thresh_open": 0.62,
                }
                if mc.get("round_image") and asset_exists(mc["round_image"]):
                    fx_m["round_image"] = mc["round_image"]
                if sp.get("layer"):
                    fx_m["layer"] = sp["layer"]
                if region_space:
                    fx_m["region_space"] = region_space
                out.append(fx_m)
    return out


E: list = []


def scene(sid, image, motion=None, beat_type="normal", level="C", intent="",
          tr=None, trd=0.35, shake=None, parallax=None, split_screen=None):
    E.append(("scene", dict(
        id=sid, image=image, motion=motion, beat_type=beat_type, level=level,
        intent=intent, tr=tr, trd=trd, shake=shake, parallax=parallax, split_screen=split_screen,
    )))


def living(scene_key: str, specs: list[dict]):
    E.append(("living", dict(scene_key=scene_key, specs=specs)))


def fx(fx_dict: dict):
    E.append(("fx", fx_dict))


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


def sfx_abs(preset, at: float, gain=-5.0, dur=None):
    E.append(("sfx_abs", dict(preset=preset, at=at, gain=gain, dur=dur)))


def amb(preset, gain=-2.0):
    E.append(("amb", dict(preset=preset, gain=gain)))


def bgm(preset, gain=-1.5):
    E.append(("bgm", dict(preset=preset, gain=gain)))


def mark(name):
    E.append(("mark", name))


SILENT = -40.0
EP01B = "factory196/materialAndDraft/EP01b/assets/"

# ================================================================ STORY
# ---- HOOK · MÓN NỢ TỪ CHÍNH GƯƠNG MẶT MÌNH (00:00 – 00:31.38) ----
amb("night_room", -1.5); bgm("suspense_pulse", -2.5)
scene(
    "s00_night_ping", "assets/c00.jpg",
    motion={"preset": "slow_push_in", "scale": [1.02, 1.09], "focus": [[0.52, 0.48], [0.56, 0.44]], "wobble": "breathe", "easing": "ease_out"},
    beat_type="climax", level="B", shake=0.2,
    intent="2.5D Parallax phòng đêm + Rack Focus mờ nền + Breathing + Head Micro-Tilt + Anh Hai chớp mắt & chép miệng 4 trạng thái (fg) + sóng âm đòi nợ + bộ đếm 6.000.000đ",
    parallax={
        "camera": "push_in",
        "dolly": [1.02, 1.09],
        "shift_x": [0.0, 0.0],
        "shift_y": [0.0, -4.0],
        "focus": [0.56, 0.46],
        "strength": 0.90,
        "easing": "ease_out",
        "layers": [
            {"role": "bg", "image": "assets/s00_bg.jpg", "depth": 0.40, "blur_from": 0.4, "blur_to": 3.4, "blur_at": 4.8, "blur_dur": 3.6},
            {"role": "fg", "image": "assets/s00_fg.png", "depth": 1.24, "breathe_y": 2.0, "breathe_period": 3.5,
             "head_tilt_deg": 1.0, "head_pivot": [0.78, 0.85], "tilt_speaker": "anh_hai", "tilt_line_ids": ["l01_ah", "l03_ah"]},
        ],
    },
)
living("c00", [dict(char="anh_hai", speaker="anh_hai", line_ids=["l01_ah", "l03_ah"], first_offset=1.4, interval=3.8, layer="fg")])
fx({"type": "chromatic_pulse", "at": 0.50, "dur": 0.28, "shift_px": 6, "zoom_blur": 0.02})
fx({"type": "screen_glow", "space": "frame", "pos": [0.73, 0.38], "radius": [0.16, 0.18],
    "color": [130, 200, 255], "intensity": 0.26, "mode": "pulse", "start": 0.5, "end": 13.9, "fade": 0.3})
fx({"type": "phone_waveform", "speaker": "chu_no", "line_ids": ["l02_cn"],
    "start": 5.5, "end": 10.8, "pos": [0.24, 0.58], "size": [0.25, 0.060],
    "color": [255, 95, 85], "label": "SỐ LẠ · ĐÒI NỢ"})
fx({"type": "animated_counter", "start": 5.85, "end": 13.7, "count_dur": 2.2,
    "from_val": 3500000, "to_val": 6000000, "fmt": "vnd", "label": "HỢP ĐỒNG ÉP TRẢ",
    "pos": [0.24, 0.34], "style": "danger", "easing": "ease_out"})
fx({"type": "color_mood", "mood": "cold_suspicion", "strength": 0.48, "vignette": 0.22, "grain": 0.012})
sfx("bank_ting", 0.15, -2)
sfx_abs("counter_tick", 5.85, -5.5)
bubble("NGÂN HÀNG X", "+3.500.000 VND · ND: GIAI NGAN HD 6.000.000",
       side="left", y=280, stamp="TIỀN LẠ VỀ", dur=5.2, offset=0.2)
sfx("phone_ring", 1.1, -4, dur=1.4)
beat(2.2)
line("l01_ah", "AH", "Alo, ai mới chuyển nhầm tiền vậy?", "ngơ ngác, hỏi thẳng")
line("l02_cn", "CN_P", "Không ai chuyển nhầm hết anh Hai. Hợp đồng sáu triệu của anh tới hạn thứ Sáu.",
     "trầm đều, lịch sự lạnh băng",
     sub="Không ai chuyển nhầm hết anh Hai. Hợp đồng 6 triệu của anh tới hạn thứ Sáu.")
line("l03_ah", "AH", "Anh nói bậy gì đó, tôi vay hồi nào?", "nhíu mày, gắt nhẹ")

scene(
    "s01_mirror_shock", "assets/c01.jpg",
    motion={"preset": "static_hold", "scale": [1.03, 1.05], "focus": [[0.52, 0.46], [0.54, 0.44]], "wobble": "tense"},
    beat_type="climax", level="B", tr="zoom_punch", trd=0.28, shake=0.15,
    intent="2.5D Parallax cú sốc xem clip quay lén: Rack Focus mở nét Chị Hai sau rèm + Anh Hai (fg) & Chị Hai (bg) chớp mắt + Chromatic Pulse + sóng âm clip",
    parallax={
        "camera": "push_in",
        "dolly": [1.02, 1.08],
        "shift_x": [0.0, 0.0],
        "shift_y": [0.0, -3.5],
        "focus": [0.58, 0.46],
        "strength": 0.85,
        "easing": "smoothstep",
        "layers": [
            {"role": "bg", "image": "assets/s01_bg.jpg", "depth": 0.42, "blur_from": 2.8, "blur_to": 0.4, "blur_at": 19.0, "blur_dur": 4.2},
            {"role": "fg", "image": "assets/s01_fg.png", "depth": 1.24, "breathe_y": 1.8, "breathe_period": 3.0},
        ],
    },
)
living("c01", [
    dict(char="anh_hai", first_offset=2.1, interval=4.4, layer="fg"),
    dict(char="chi_hai", first_offset=3.4, interval=4.1, layer="bg"),
])
fx({"type": "chromatic_pulse", "at": 14.27, "dur": 0.34, "shift_px": 8, "zoom_blur": 0.030})
fx({"type": "screen_glow", "space": "frame", "pos": [0.55, 0.60], "radius": [0.22, 0.24],
    "color": [95, 225, 255], "intensity": 0.30, "mode": "flicker", "start": 14.4, "end": 31.2, "fade": 0.25})
fx({"type": "phone_waveform", "speaker": "chu_no", "line_ids": ["l04_ah_clip", "l05_cn"],
    "start": 14.6, "end": 28.6, "pos": [0.23, 0.56], "size": [0.25, 0.060],
    "color": [255, 90, 85], "label": "CLIP ĐE DỌA · 00:06"})
fx({"type": "focus_highlight", "pos": [0.60, 0.44], "radius": [0.36, 0.36],
    "dim_outer": 0.24, "start": 14.5, "end": 31.3, "fade": 0.4})
fx({"type": "color_mood", "mood": "high_tension", "strength": 0.52, "vignette": 0.24, "grain": 0.014})
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
scene(
    "s02_promo_desk", "assets/c02.jpg",
    motion={"preset": "pan_right", "scale": [1.05, 1.05], "focus": [[0.47, 0.50], [0.53, 0.50]], "wobble": "none", "easing": "smoothstep"},
    beat_type="establishing", level="C", tr="film_burn", trd=0.45,
    intent="Chuyển hồi Film Burn về 4 ngày trước: cả 3 nhân vật (Bé Tôm, Vy, Anh Hai) chớp mắt & chép miệng khớp thoại + khoanh đỏ thẻ CCCD + hạt nắng",
)
living("c02", [
    dict(char="be_tom", speaker="be_tom", line_ids=["l06_tom"], first_offset=1.3, interval=3.8),
    dict(char="vy", speaker="ke_ngot_ngao_nu", line_ids=["l07_vy"], first_offset=2.2, interval=4.1),
    dict(char="anh_hai", speaker="anh_hai", line_ids=["l08_ah"], first_offset=3.1, interval=4.4),
])
fx({"type": "red_circle_draw", "region": [0.530, 0.458, 0.595, 0.548], "at": 38.2, "dur": 0.55, "end": 46.8,
    "style": "circle", "width": 6, "color": [242, 48, 52]})
fx({"type": "ambient_particles", "count": 20, "opacity": 0.30, "color": [255, 236, 185], "drift_dir": "float", "seed": 52})
fx({"type": "color_mood", "mood": "warm_daily", "strength": 0.65, "vignette": 0.08, "grain": 0.0})
sfx_abs("marker_draw", 38.20, -4.0)
chapter("HỒI 1 · BỐN NGÀY TRƯỚC", "CHIẾC HỘP CAM & TẤM HÌNH CĂN CƯỚC")
sfx("chapter_sting", -0.1, -5)
beat(1.0)
line("l06_tom", "TOM", "Ba ơi, mình đăng ký lấy cái bình màu cam nghen ba!",
     "háo hức, ôm hộp màu cam ngước nhìn ba")
line("l07_vy", "VY", "Dạ quà tặng cho bé, anh cho em chụp căn cước với số điện thoại để tránh nhận trùng nha.",
     "tươi cười, lịch sự, tự nhiên như nhân viên phát quà bình thường")
beat(1.8)
line("l08_ah", "AH", "Ờ… vậy em chụp lẹ giùm anh nha.",
     "ngập ngừng một nhịp rồi miễn cưỡng đồng ý vì con trai đã ôm hộp quà", pause=0.4)
sfx("notification", 0.1, -6)
beat(1.2)

# ---- HỒI 2 · MẢNH GHÉP THỨ HAI: TỜ NĂM TRĂM TIỀN THẬT & GÓC NÉ CAM ----
amb("street", -3.0); bgm("investigative_story", -3.0)
scene(
    "s03_parking_approach", "assets/c03.jpg",
    motion={"preset": "slow_pull_out", "scale": [1.08, 1.02], "focus": [[0.52, 0.48], [0.50, 0.50]], "wobble": "none", "easing": "smoothstep"},
    beat_type="normal", level="C", tr="whip_pan_left", trd=0.28,
    intent="Hồi 2 bãi giữ xe: Cô Lành & Anh Hai đối thoại chép miệng + 3 người chớp mắt + khoanh hộp đỏ tờ 500 nghìn tiền thật + bụi nắng",
)
living("c03", [
    dict(char="be_tom", first_offset=1.8, interval=4.0),
    dict(char="co_lanh", speaker="co_hanh", line_ids=["l09_la"], first_offset=1.2, interval=4.2),
    dict(char="anh_hai", speaker="anh_hai", line_ids=["l10_ah"], first_offset=2.9, interval=4.3),
])
fx({"type": "red_circle_draw", "region": [0.505, 0.472, 0.580, 0.566], "at": 56.8, "dur": 0.55, "end": 65.2,
    "style": "box", "width": 6, "color": [242, 48, 52]})
fx({"type": "ambient_particles", "count": 22, "opacity": 0.32, "color": [255, 234, 175], "drift_dir": "float", "seed": 53})
fx({"type": "color_mood", "mood": "warm_daily", "strength": 0.58, "vignette": 0.10, "grain": 0.0})
sfx_abs("marker_draw", 56.80, -4.0)
chapter("HỒI 2 · BÃI GIỮ XE", "TỜ NĂM TRĂM TIỀN THẬT & SÁU GIÂY NHÌN THẲNG")
sfx("chapter_sting", -0.1, -5)
beat(2.2)
line("l09_la", "LANH", "Chú ơi, làm ơn giúp chị với. Chị đóng tiền thuốc mà thẻ lỗi hoài, chú đổi giùm chị năm trăm tiền mặt nghen.",
     "bối rối, hiền lành, đưa tờ 500 ngàn ra trước",
     sub="Chú ơi, làm ơn giúp chị với. Chị đóng tiền thuốc mà thẻ lỗi hoài, chú đổi giùm chị 500 tiền mặt nghen.")
beat(1.4)
line("l10_ah", "AH", "Dạ được chị. Chị đọc số tài khoản đi em chuyển cho.",
     "cởi mở, sẵn lòng giúp sau khi thấy tiền mặt thật và con trai đứng nhìn")
sfx("typing", 0.1, -6, dur=1.4)
sfx("bank_ting", 1.6, -4)
beat(2.2)

scene(
    "s04_six_seconds_face", "assets/c04.jpg",
    motion={"preset": "slow_push_in", "scale": [1.02, 1.09], "focus": [[0.50, 0.46], [0.50, 0.42]], "wobble": "breathe", "easing": "ease_out"},
    beat_type="anomaly", level="C", tr="zoom_punch", trd=0.28,
    intent="Cảnh điểm nhấn 'Sáu giây nhìn thẳng': Anh Hai chép miệng 4 trạng thái đọc từng chữ vào camera + cả 3 chớp mắt + khung đỏ nhận diện + đồng hồ quay lén 00:00→00:06",
)
living("c04", [
    dict(char="be_tom", first_offset=1.9, interval=4.1),
    dict(char="anh_hai", speaker="anh_hai", line_ids=["l12_ah"], first_offset=1.4, interval=4.5),
    dict(char="co_lanh", first_offset=2.7, interval=4.0),
])
fx({"type": "screen_glow", "pos": [0.50, 0.58], "radius": [0.20, 0.22],
    "color": [110, 220, 255], "intensity": 0.28, "mode": "turn_on", "start": 74.8, "end": 84.8, "fade": 0.4})
fx({"type": "red_circle_draw", "region": [0.415, 0.085, 0.585, 0.445], "at": 76.2, "dur": 0.55, "end": 84.2,
    "style": "box", "width": 5, "color": [245, 50, 52]})
fx({"type": "animated_counter", "start": 76.2, "end": 84.2, "count_dur": 6.0,
    "from_val": 0, "to_val": 6, "fmt": "mmss", "label": "QUAY LÉN KHUÔN MẶT",
    "pos": [0.14, 0.21], "style": "danger", "easing": "linear"})
fx({"type": "focus_highlight", "pos": [0.50, 0.36], "radius": [0.34, 0.36],
    "dim_outer": 0.26, "start": 75.5, "end": 84.8, "fade": 0.45})
sfx_abs("low_accent", 74.80, -5.5)
sfx_abs("marker_draw", 76.20, -3.8)
sfx_abs("counter_tick", 76.25, -5.0)
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
scene(
    "s05_home_noon", "assets/c05.jpg",
    motion={"preset": "pan_left", "scale": [1.06, 1.06], "focus": [[0.53, 0.50], [0.47, 0.50]], "wobble": "none", "easing": "smoothstep"},
    beat_type="normal", level="C", tr="film_burn", trd=0.45,
    intent="Bữa cơm trưa ấm áp: cả 3 thành viên (Bé Tôm, Chị Hai, Anh Hai) chép miệng đối đáp tự nhiên + chớp mắt + hạt bụi nắng cửa sổ",
)
living("c05", [
    dict(char="be_tom", speaker="be_tom", line_ids=["l14_tom"], blink=False),
    dict(char="chi_hai", speaker="chi_hai", line_ids=["l15_ch"], first_offset=1.6, interval=4.1),
    dict(char="anh_hai", speaker="anh_hai", line_ids=["l16_ah"], first_offset=2.6, interval=4.3),
])
fx({"type": "ambient_particles", "count": 24, "opacity": 0.34, "color": [255, 232, 165], "drift_dir": "float", "seed": 55})
fx({"type": "color_mood", "mood": "warm_daily", "strength": 0.72, "vignette": 0.08, "grain": 0.0})
beat(0.6)
line("l14_tom", "TOM", "Mẹ ơi, sáng nay ba mới giúp một bà cô mắt mờ ngoài bãi xe đó!",
     "khoe mẹ hồn nhiên, tự hào về ba")
line("l15_ch", "CH", "Giúp sao vậy anh?", "hỏi gọn, tay vẫn nhặt rau")
line("l16_ah", "AH", "Bả đưa tờ năm trăm trước, nhờ anh chuyển khoản rồi bấm tắt giùm cái màn hình đơ.",
     "bình thản, đặt tờ tiền lên bàn",
     sub="Bả đưa tờ 500 trước, nhờ anh chuyển khoản rồi bấm tắt giùm cái màn hình đơ.")
beat(2.4)

# Cảnh câm điện ảnh: Cô Lành tháo kính lão sau bãi xe (2.5D Level B!)
amb("street", -4.5); bgm("tension_drone", -2.5)
scene(
    "s06_glasses_off", "assets/c06.jpg",
    motion={"preset": "slow_push_in", "scale": [1.02, 1.10], "focus": [[0.58, 0.46], [0.64, 0.40]], "wobble": "none", "easing": "ease_in"},
    beat_type="suspicion", level="B", tr="luma_wipe", trd=0.36,
    intent="2.5D Parallax cú lật mặt lạnh gáy khi Cô Lành tháo kính: Rack Focus xóa nhòe Anh Hai phía sau + Cô Lành (fg) thở & chớp mắt lạnh + typing indicator + tông xanh lạnh",
    parallax={
        "camera": "push_in",
        "dolly": [1.02, 1.09],
        "shift_x": [0.0, 0.0],
        "shift_y": [0.0, -3.0],
        "focus": [0.64, 0.42],
        "strength": 0.90,
        "easing": "ease_in",
        "layers": [
            {"role": "bg", "image": "assets/s06_bg.jpg", "depth": 0.40, "blur_from": 0.5, "blur_to": 3.8, "blur_at": 108.0, "blur_dur": 3.8},
            {"role": "fg", "image": "assets/s06_fg.png", "depth": 1.24, "breathe_y": 1.8, "breathe_period": 4.0},
        ],
    },
)
living("c06", [dict(char="co_lanh", first_offset=2.0, interval=4.2, layer="fg")])
fx({"type": "typing_indicator", "start": 107.9, "end": 109.25, "side": "left", "y": 265})
fx({"type": "screen_glow", "space": "frame", "pos": [0.56, 0.56], "radius": [0.16, 0.16],
    "color": [115, 215, 255], "intensity": 0.24, "mode": "pulse", "start": 107.5, "end": 118.2, "fade": 0.35})
fx({"type": "color_mood", "mood": "cold_suspicion", "strength": 0.66, "vignette": 0.24, "grain": 0.012})
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
scene(
    "s07_midnight_temptation", "assets/c07.jpg",
    motion={"preset": "slow_pull_out", "scale": [1.09, 1.02], "focus": [[0.60, 0.46], [0.54, 0.48]], "wobble": "breathe", "easing": "smoothstep"},
    beat_type="suspicion", level="C", tr="film_burn", trd=0.42,
    intent="Hồi 3 nửa đêm giằng co 28s: Anh Hai (4 trạng thái miệng) & Chị Hai đối thoại chép miệng + chớp mắt + typing indicator + bộ đếm 6.000.000đ + high_tension",
)
living("c07", [
    dict(char="anh_hai", speaker="anh_hai", line_ids=["l18_ah"], first_offset=1.6, interval=4.1),
    dict(char="chi_hai", speaker="chi_hai", line_ids=["l17_ch", "l19_ch"], first_offset=2.8, interval=4.4),
])
fx({"type": "typing_indicator", "start": 122.2, "end": 123.5, "side": "left", "y": 270})
fx({"type": "screen_glow", "pos": [0.51, 0.66], "radius": [0.16, 0.18],
    "color": [125, 225, 255], "intensity": 0.26, "mode": "pulse", "start": 118.6, "end": 146.2, "fade": 0.35})
fx({"type": "animated_counter", "start": 129.0, "end": 145.8, "count_dur": 2.4,
    "from_val": 3500000, "to_val": 6000000, "fmt": "vnd", "label": "ĐÒI TẤT TOÁN TRƯỚC 23H",
    "pos": [0.22, 0.34], "style": "danger", "easing": "ease_out"})
fx({"type": "color_mood", "mood": "high_tension", "strength": 0.50, "vignette": 0.24, "grain": 0.012})
sfx_abs("counter_tick", 129.00, -5.5)
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

# Khóa thẻ + nhắn báo trước nhóm xưởng
scene(
    "s08_lockdown_first_strike", "assets/c08.jpg",
    motion={"preset": "pan_right", "scale": [1.06, 1.06], "focus": [[0.47, 0.48], [0.53, 0.48]], "wobble": "none", "easing": "smoothstep"},
    beat_type="information", level="C", tr="whip_pan_right", trd=0.26,
    intent="Phản ứng khóa thẻ & báo nhóm xưởng: Chị Hai & Anh Hai chớp mắt + chép miệng + typing indicator bên phải + ánh điện thoại + Noir Evidence",
)
living("c08", [
    dict(char="chi_hai", speaker="chi_hai", line_ids=["l20_ch"], first_offset=1.3, interval=4.0),
    dict(char="anh_hai", speaker="anh_hai", line_ids=["l21_ah"], first_offset=2.4, interval=4.2),
])
fx({"type": "screen_glow", "pos": [0.49, 0.88], "radius": [0.18, 0.12],
    "color": [130, 225, 255], "intensity": 0.28, "mode": "pulse", "start": 146.7, "end": 158.4, "fade": 0.25})
fx({"type": "typing_indicator", "start": 153.2, "end": 154.5, "side": "right", "y": 290})
fx({"type": "color_mood", "mood": "noir_evidence", "strength": 0.46, "vignette": 0.22, "grain": 0.010})
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
scene(
    "s09_bank_counter", "assets/c09.jpg",
    motion={"preset": "pan_left", "scale": [1.05, 1.05], "focus": [[0.52, 0.48], [0.48, 0.48]], "wobble": "none", "easing": "smoothstep"},
    beat_type="information", level="C", tr="film_burn", trd=0.44,
    intent="Hồi 4 sáng hôm sau tại ngân hàng: Giao dịch viên chép miệng 4 trạng thái giải thích nghiệp vụ + cả 2 chớp mắt + khoanh xanh thẻ CCCD chip + huy hiệu khoanh giữ 3.500.000đ",
)
living("c09", [
    dict(char="anh_hai", first_offset=2.1, interval=4.4),
    dict(char="gdv", speaker="chi_tu", line_ids=["l22_gdv", "l23a_gdv", "l23b_gdv"], first_offset=1.4, interval=4.0),
])
fx({"type": "red_circle_draw", "region": [0.432, 0.748, 0.496, 0.820], "at": 161.2, "dur": 0.55, "end": 168.5,
    "style": "circle", "width": 5, "color": [45, 205, 125]})
fx({"type": "animated_counter", "start": 172.6, "end": 179.6, "count_dur": 1.6,
    "from_val": 0, "to_val": 3500000, "fmt": "vnd", "label": "NGÂN HÀNG KHOANH GIỮ",
    "pos": [0.24, 0.22], "style": "safe", "easing": "ease_out"})
fx({"type": "ambient_particles", "count": 18, "opacity": 0.26, "color": [255, 240, 200], "drift_dir": "float", "seed": 59})
fx({"type": "color_mood", "mood": "warm_daily", "strength": 0.55, "vignette": 0.06, "grain": 0.0})
sfx_abs("marker_draw", 161.20, -4.2)
sfx_abs("counter_tick", 172.60, -5.5)
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

# Cổng trụ sở cơ quan công an – Tách 2 nhịp: Split-Screen phản đòn (s10a, gắn blink+mouth 4-state trên panel!) -> Toàn khung 2.5D (s10b)
amb("street", -4.0); bgm("tension_drone", SILENT)
scene(
    "s10a_split_counterstrike", "assets/c10.jpg",
    beat_type="climax", level="C", tr="whip_pan_left", trd=0.28,
    intent="Đột phá Split-Screen cuộc gọi phản đòn trước cổng Công an: Phe đòi nợ (trái, c06 + blink) đối đầu Anh Hai ôm biên bản (phải, c10 + blink + chép miệng 4 trạng thái ngay trên panel!), tự sáng viền & nhảy sóng âm",
    split_screen={
        "layout": "vertical",
        "ratio": 0.50,
        "divider_width": 6,
        "divider_rgb": [242, 246, 255],
        "active_glow_rgb": [255, 205, 70],
        "inactive_dim": 0.22,
        "slide_in_dur": 0.30,
        "panels": [
            {
                "image": "assets/c06.jpg",
                "crop_x": 0.72,
                "speaker": "chu_no",
                "line_ids": ["l24_cn"],
                "label": "SỐ LẠ · ĐÒI NỢ",
                "label_rgb": [240, 62, 62],
                "waveform": True,
                "waveform_rgb": [255, 95, 85],
                "motion": {"preset": "slow_push_in", "scale": [1.04, 1.11], "focus": [[0.50, 0.44], [0.50, 0.42]], "wobble": "none"},
                "detail_fx": build_char_fx("c06", [dict(char="co_lanh", first_offset=1.8, interval=4.0)], region_space="source"),
            },
            {
                "image": "assets/c10.jpg",
                "crop_x": 0.72,
                "speaker": "anh_hai",
                "line_ids": ["l25_ah", "l26_ah"],
                "label": "ANH HAI · CỔNG CÔNG AN",
                "label_rgb": [45, 205, 130],
                "waveform": True,
                "waveform_rgb": [85, 225, 165],
                "motion": {"preset": "slow_pull_out", "scale": [1.09, 1.02], "focus": [[0.50, 0.46], [0.50, 0.48]], "wobble": "none"},
                "detail_fx": build_char_fx("c10", [
                    dict(char="anh_hai", speaker="anh_hai", line_ids=["l25_ah", "l26_ah"], first_offset=1.5, interval=4.1)
                ], region_space="source"),
            },
        ],
    },
)
fx({"type": "animated_counter", "start": 187.4, "end": 201.4, "count_dur": 1.4,
    "from_val": 0, "to_val": 3500000, "fmt": "vnd", "label": "ĐÃ LẬP BIÊN BẢN CÔNG AN",
    "pos": [0.50, 0.16], "style": "safe", "easing": "ease_out"})
sfx_abs("counter_tick", 187.40, -5.5)
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
beat(2.05)  # 2.05 + SCENE_LEAD(0.35) = 2.40s -> giữ đúng mốc call_end 201.92s & tổng 262.08s

scene(
    "s10b_scammer_blocked", "assets/c10.jpg",
    motion={"preset": "slow_pull_out", "scale": [1.07, 1.02], "focus": [[0.62, 0.46], [0.54, 0.50]], "wobble": "none", "easing": "ease_out"},
    beat_type="aftermath", level="B", tr="whip_pan_right", trd=0.24,
    intent="2.5D Parallax mở toàn khung Anh Hai bình tĩnh trước cổng cơ quan Công an sáng rực + Rack Focus + Breathing + chớp mắt (fg) + Chromatic Pulse cú chặn số",
    parallax={
        "camera": "pull_out",
        "dolly": [1.08, 1.02],
        "shift_x": [0.0, 0.0],
        "shift_y": [-4.0, 0.0],
        "focus": [0.62, 0.46],
        "strength": 0.90,
        "easing": "ease_out",
        "layers": [
            {"role": "bg", "image": "assets/s10_bg.jpg", "depth": 0.42, "blur_from": 2.4, "blur_to": 0.4, "blur_at": 201.9, "blur_dur": 2.4},
            {"role": "fg", "image": "assets/s10_fg.png", "depth": 1.24, "breathe_y": 1.8, "breathe_period": 3.8},
        ],
    },
)
living("c10", [dict(char="anh_hai", first_offset=1.3, interval=3.8, layer="fg")])
fx({"type": "chromatic_pulse", "at": 201.92, "dur": 0.24, "shift_px": 5, "zoom_blur": 0.018})
fx({"type": "color_mood", "mood": "warm_daily", "strength": 0.55, "vignette": 0.08, "grain": 0.0})
sfx("call_end", 0.0, -2)
bubble("CUỘC GỌI ĐÃ KẾT THÚC", "Số máy này hiện không liên lạc được",
       side="left", y=280, stamp="ĐÃ CHẶN SỐ", dur=3.6, offset=0.2)
beat(4.0)

# ---- HỒI 5 · CÂU HỎI CỦA ĐỨA CON TRAI ----
amb("street", -4.5); bgm("warm_outro", -3.5)
scene(
    "s11_school_pickup", "assets/c11.jpg",
    motion={"preset": "pan_right", "scale": [1.05, 1.05], "focus": [[0.47, 0.48], [0.53, 0.48]], "wobble": "none", "easing": "smoothstep"},
    beat_type="aftermath", level="C", tr="film_burn", trd=0.48,
    intent="Hồi 5 chiều tan học ấm áp: hai cha con Bé Tôm & Anh Hai chớp mắt + chép miệng trò chuyện + chuyển cảnh Film Burn + hạt nắng chiều",
)
living("c11", [
    dict(char="be_tom", speaker="be_tom", line_ids=["l27_tom"], first_offset=1.6, interval=4.0),
    dict(char="anh_hai", speaker="anh_hai", line_ids=["l28_ah", "l29_ah"], first_offset=2.5, interval=4.3),
])
fx({"type": "ambient_particles", "count": 26, "opacity": 0.36, "color": [255, 226, 150], "drift_dir": "float", "seed": 61})
fx({"type": "color_mood", "mood": "warm_daily", "strength": 0.78, "vignette": 0.08, "grain": 0.0})
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
scene(
    "s12_red_flags", EP01B + "scene18.jpg",
    motion={"preset": "static_hold"},
    beat_type="ending", level="A", tr="dissolve", trd=0.40,
    intent="Khung tĩnh sạch tuyệt đối để khán giả đọc 5 dấu hiệu bảo vệ căn cước & khuôn mặt",
)
mark("rf_start")
sfx("bank_ting", 0.0, -5)
line("l30_narr", "N", "Thứ chúng lấy không phải tiền lẻ trên tay, mà là khuôn mặt và lòng tốt của bạn.")
beat(1.6)
mark("rf_end")

# ---- KẾT MỞ ĐƯỜNG DÂY NGẦM: DÌ LÀNH TRONG XE ĐÊM MƯA ----
amb("rain", -4.0); bgm("tension_drone", -1.2)
scene(
    "s13_backseat_boss", "assets/c12.jpg",
    motion={"preset": "slow_push_in", "scale": [1.02, 1.11], "focus": [[0.62, 0.46], [0.66, 0.40]], "wobble": "breathe", "easing": "ease_in"},
    beat_type="climax", level="C", tr="luma_wipe", trd=0.38,
    intent="Coda phim hình sự trong xe đêm mưa: Dì Lành chớp mắt lạnh & chép miệng 4 trạng thái chốt câu cuối + mưa ngoài kính + đèn phố quét + sóng âm đàn em + ánh tablet + Noir Evidence",
)
living("c12", [
    dict(char="co_lanh", speaker="co_hanh", line_ids=["l32_lanh_boss"], first_offset=2.1, interval=4.4),
])
fx({"type": "rain_layer", "opacity": 0.30, "density": 0.90, "angle_deg": -16.0, "speed": 1180.0, "seed": 63})
fx({"type": "light_sweep", "mode": "light", "color": [255, 210, 145], "intensity": 0.20, "width": 0.20, "angle_deg": -20.0, "repeat": 2})
fx({"type": "phone_waveform", "speaker": "ke_ngot_ngao_nam", "line_ids": ["l31_sub"],
    "start": 242.3, "end": 248.4, "pos": [0.24, 0.38], "size": [0.25, 0.058],
    "color": [255, 100, 90], "label": "NHÁNH NGOÀI · BÁO CÁO"})
fx({"type": "screen_glow", "pos": [0.56, 0.72], "radius": [0.20, 0.18],
    "color": [125, 205, 235], "intensity": 0.22, "mode": "pulse", "start": 241.0, "end": 255.1, "fade": 0.4})
fx({"type": "chromatic_pulse", "at": 254.90, "dur": 0.28, "shift_px": 7, "zoom_blur": 0.025})
fx({"type": "color_mood", "mood": "noir_evidence", "strength": 0.72, "vignette": 0.30, "grain": 0.020})
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
scene(
    "s14_black_cut", "assets/c13.jpg",
    motion={"preset": "static_hold"},
    beat_type="ending", level="A", tr="cut", trd=0.0,
    intent="Cú cắt đen đột ngột giữ dư âm lạnh sau câu chốt của Dì Lành",
)
beat(2.0)

# ---- DISCLAIMER ----
amb("room_tone", -6.0); bgm("tension_drone", -8.0)
scene(
    "s15_disclaimer", EP01B + "scene18.jpg",
    motion={"preset": "static_hold"},
    beat_type="ending", level="A", tr="fade_black", trd=0.40,
    intent="Khung tĩnh sạch hiển thị lưu ý miễn trừ trách nhiệm cuối phim",
)
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
        sc: dict = {
            "id": d["id"],
            "image": d["image"],
            "start": round(t, 2),
            "end": None,
            "beat_type": d["beat_type"],
            "motion_level": d["level"],
            "motion_intent": d["intent"],
        }
        if d["motion"] is not None:
            sc["motion"] = d["motion"]
        if d["tr"]:
            sc["transition_in"] = {"type": d["tr"], "dur": d["trd"]}
        if d["shake"] is not None:
            sc["shakes"] = [{"at": round(t + d["shake"], 2), "dur": 0.4, "amp": 16}]
        if d["parallax"]:
            px = d["parallax"]
            if all(asset_exists(ly["image"]) for ly in px.get("layers", [])):
                sc["parallax"] = px
            elif sc["motion_level"] == "B":
                sc["motion_level"] = "C"
        if d["split_screen"]:
            sc["split_screen"] = d["split_screen"]
        sc["detail_fx"] = []
        scenes.append(sc)
        t += SCENE_LEAD
    elif kind == "living":
        scenes[-1]["detail_fx"].extend(build_char_fx(d["scene_key"], d["specs"]))
    elif kind == "fx":
        scenes[-1]["detail_fx"].append(d)
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
amb_runs[-1]["end"] = total
bgm_runs[-1]["end"] = total
foley.sort(key=lambda item: float(item["at"]))


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
    "version": "v5-level3-full-abc-staging",
    "motion_upgrade": "level3",
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
    f"episode.json (v5-level3-full-abc-staging): {total:.2f}s ({mmss(total)}) · {len(scenes)} cảnh · "
    f"{len(dialogue)} câu · {words} từ ({words / (total / 60):.0f} từ/phút) · câu dài nhất {maxw} từ · "
    f"Bóc trần {len(narr_lines)} câu ({narr} từ, thẻ kết {rf_dur}s) · "
    f"{'TTS thật' if real else 'ước tính'} ({len(real)} câu thật)"
)
