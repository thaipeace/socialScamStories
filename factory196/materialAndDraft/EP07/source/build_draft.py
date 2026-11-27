# -*- coding: utf-8 -*-
"""
Trình biên dịch `factory196/materialAndDraft/EP07/episode.json` – Tập EP07:
"Sau hai trăm triệu" (16:9 Long-form · Visual Motion Level 3 + Living-Character 2.5).

Chuẩn Luật Kế Thừa Cộng Dồn HRN-MOTION-L3.0 (CHECK 1 -> CHECK 2 -> CHECK 3):
  - CHECK 1 (Level 1): Bảo toàn 100% 49 câu thoại TTS thật (463.61s), 16 chat bubbles,
    5 chapters + 2 epilogue titles, red_flags, disclaimer, ambience, bgm, duck_extra,
    toàn bộ foley gốc (+ foley Level 3: counter_tick, marker_draw, notification khớp bubble).
  - CHECK 2 (Level 2 cốt lõi):
      * 4 cảnh 2.5D Parallax Level B (s00, s01, s07, s12) + Breathing + Rack Focus + Head Micro-Tilt
      * 16 rig chớp mắt (eye_blink) & 13 rig chép miệng khớp .wav thật (mouth_sync, gồm 4 rig 4 trạng thái round_image)
        khóa pixel qua 03_ENGINE/face_roi_prep.py (cả trên lớp 2.5D fg lẫn các cảnh đối thoại 2–3 người)
  - CHECK 3 (Level 3 Đạo diễn & Không khí):
      * Đồ họa vật chứng: red_circle_draw, animated_counter, phone_waveform, typing_indicator
      * Không khí & Màu phim: ambient_particles, light_sweep, screen_glow, color_mood, chromatic_pulse
      * Chuyển cảnh điện ảnh: zoom_punch, whip_pan_left/right, film_burn, luma_wipe
      * Anti-Repetition: 0 chuỗi lặp >= 3 push_in trên toàn bộ 26 cảnh.

Nguồn sự thật duy nhất của timeline:
    python factory196/materialAndDraft/EP07/source/build_draft.py
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


def asset_exists(rel_path: str) -> bool:
    return (EP / rel_path).is_file()


real = {p.stem: wav_dur(p.stem) for p in TTS.glob("*.wav")} if TTS.is_dir() else {}
real = {k: v for k, v in real.items() if v}

# Pixel-locked Living-Character ROI config produced by 03_ENGINE/face_roi_prep.py
ROI_CFG_PATH = HERE / "face_rois.json"
FACE_ROIS: dict = json.loads(ROI_CFG_PATH.read_text(encoding="utf-8")) if ROI_CFG_PATH.is_file() else {}

# ---------------------------------------------------------------- GIỌNG
# 8 nhân vật = 8 voice hoàn toàn tách biệt trong 02_CAST/cast.json (KHÔNG sửa chữ/style để giữ nguyên TTS Gate 2)
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


E: list[tuple[str, object]] = []


def scene(sid: str, img: str, motion: dict | None = None, beat_type: str = "normal", level: str = "C",
          intent: str = "", tr: str | None = None, trd: float = 0.35, shake: float | None = None,
          parallax: dict | None = None, split_screen: dict | None = None):
    E.append(("scene", dict(
        id=sid, image=img, motion=motion, beat_type=beat_type, level=level,
        intent=intent, tr=tr, trd=trd, shake=shake, parallax=parallax, split_screen=split_screen,
    )))


def living(scene_key: str, specs: list[dict]):
    E.append(("living", dict(scene_key=scene_key, specs=specs)))


def fx(fx_dict: dict):
    E.append(("fx", fx_dict))


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
# ---- HOOK · 23:15 ĐÊM CẠN SẠCH TIỀN (00:00 – 00:25.53) ----
amb("night_room", -1.5); bgm("suspense_pulse", -2.5)
scene(
    "s00_hook_midnight", "assets/c00.jpg",
    motion={"preset": "slow_push_in", "scale": [1.02, 1.09], "focus": [[0.56, 0.46], [0.60, 0.44]], "wobble": "breathe", "easing": "ease_out"},
    beat_type="climax", level="B", shake=0.2,
    intent="2.5D Parallax phòng khách 23h15 + Rack Focus mờ nền + Breathing + Head Micro-Tilt + Ông Thành chớp mắt & chép miệng 4 trạng thái (fg) + bộ đếm 200.000.000đ khóa lệnh + sóng âm Khoa",
    parallax={
        "camera": "push_in",
        "dolly": [1.02, 1.09],
        "shift_x": [0.0, 0.0],
        "shift_y": [0.0, -4.0],
        "focus": [0.62, 0.44],
        "strength": 0.90,
        "easing": "ease_out",
        "layers": [
            {"role": "bg", "image": "assets/s00_bg.jpg", "depth": 0.40, "blur_from": 0.4, "blur_to": 3.4, "blur_at": 6.5, "blur_dur": 3.5},
            {"role": "fg", "image": "assets/s00_fg.png", "depth": 1.24, "breathe_y": 2.0, "breathe_period": 3.5,
             "head_tilt_deg": 1.0, "head_pivot": [0.68, 0.85], "tilt_speaker": "ong_bay", "tilt_line_ids": ["l01_thanh", "l03_thanh"]},
        ],
    },
)
living("c00", [dict(char="thanh", speaker="ong_bay", line_ids=["l01_thanh", "l03_thanh"], first_offset=1.4, interval=3.8, layer="fg")])
fx({"type": "chromatic_pulse", "at": 0.25, "dur": 0.28, "shift_px": 6, "zoom_blur": 0.02})
fx({"type": "screen_glow", "space": "frame", "pos": [0.60, 0.40], "radius": [0.14, 0.14],
    "color": [110, 215, 255], "intensity": 0.24, "mode": "pulse", "start": 0.3, "end": 22.2, "fade": 0.3})
fx({"type": "animated_counter", "start": 7.8, "end": 16.5, "count_dur": 1.8,
    "from_val": 0, "to_val": 200000000, "fmt": "vnd", "label": "LỆNH HOÀN TRẢ BỊ KHÓA",
    "pos": [0.24, 0.34], "style": "danger", "easing": "ease_out"})
fx({"type": "phone_waveform", "speaker": "ke_ngot_ngao_nam", "line_ids": ["l02_khoa"],
    "start": 8.3, "end": 14.8, "pos": [0.24, 0.56], "size": [0.25, 0.060],
    "color": [255, 95, 85], "label": "KHOA · NHÓM HỖ TRỢ"})
fx({"type": "color_mood", "mood": "cold_suspicion", "strength": 0.48, "vignette": 0.22, "grain": 0.012})
sfx("notification", 0.15, -2)
sfx_abs("counter_tick", 7.80, -5.5)
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

scene(
    "s01_hook_freeze", "assets/c01.jpg",
    motion={"preset": "slow_pull_out", "scale": [1.08, 1.02], "focus": [[0.60, 0.44], [0.56, 0.46]], "wobble": "tense", "easing": "smoothstep"},
    beat_type="climax", level="B", tr="zoom_punch", trd=0.25, shake=0.15,
    intent="2.5D Parallax cú đứng hình Hook: Rack Focus mở nền tối + Breathing + Ông Thành chớp mắt bàng hoàng (fg) + Chromatic Pulse + ánh màn hình lạnh",
    parallax={
        "camera": "pull_out",
        "dolly": [1.08, 1.02],
        "shift_x": [0.0, 0.0],
        "shift_y": [-3.5, 0.0],
        "focus": [0.60, 0.44],
        "strength": 0.85,
        "easing": "smoothstep",
        "layers": [
            {"role": "bg", "image": "assets/s01_bg.jpg", "depth": 0.42, "blur_from": 2.6, "blur_to": 0.5, "blur_at": 22.8, "blur_dur": 2.2},
            {"role": "fg", "image": "assets/s01_fg.png", "depth": 1.24, "breathe_y": 1.8, "breathe_period": 2.8},
        ],
    },
)
living("c01", [dict(char="thanh", first_offset=1.1, interval=3.5, layer="fg")])
fx({"type": "chromatic_pulse", "at": 22.55, "dur": 0.30, "shift_px": 7, "zoom_blur": 0.025})
fx({"type": "screen_glow", "space": "frame", "pos": [0.50, 0.78], "radius": [0.22, 0.18],
    "color": [95, 220, 255], "intensity": 0.28, "mode": "flicker", "start": 22.5, "end": 25.4, "fade": 0.2})
fx({"type": "color_mood", "mood": "high_tension", "strength": 0.54, "vignette": 0.26, "grain": 0.014})
mark("hook_freeze")
sfx("impact", 0.0, -3)
sfx("heartbeat", 0.3, -4.5, dur=2.4)
beat(2.8)

# ---- HỒI 1 · MỘT THÁNG TRƯỚC: VỪA VỀ HƯU, BÀN CÀ PHÊ SÁNG & HẬU QUẢ 200 TRIỆU ----
amb("room_tone", -2.5); bgm("warm_outro", -5.0)
scene(
    "s02_retirement_plan", "assets/c02.jpg",
    motion={"preset": "pan_right", "scale": [1.05, 1.05], "focus": [[0.47, 0.50], [0.53, 0.50]], "wobble": "none", "easing": "smoothstep"},
    beat_type="establishing", level="C", tr="film_burn", trd=0.48,
    intent="Chuyển hồi Film Burn về 1 tháng trước ấm áp: gia đình 3 thế hệ (Trang, Bé Bo, Ông Thành) đều chớp mắt + chép miệng đối thoại + hạt ánh sáng ấm",
)
living("c02", [
    dict(char="thanh", speaker="ong_bay", line_ids=["l05_thanh", "l07_thanh", "l08b_thanh"], first_offset=1.6, interval=4.1),
    dict(char="bo", speaker="be_tom", line_ids=["l06_bo"], first_offset=2.1, interval=3.8),
    dict(char="trang", speaker="chi_hai", line_ids=["l08_trang"], first_offset=2.8, interval=4.3),
])
fx({"type": "ambient_particles", "count": 20, "opacity": 0.26, "color": [255, 236, 185], "drift_dir": "float", "seed": 72})
fx({"type": "color_mood", "mood": "warm_daily", "strength": 0.58, "vignette": 0.08, "grain": 0.0})
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
scene(
    "s03_old_friends_cafe", "assets/c03.jpg",
    motion={"preset": "slow_pull_out", "scale": [1.06, 1.02], "focus": [[0.48, 0.48], [0.50, 0.50]], "wobble": "none", "easing": "smoothstep"},
    beat_type="normal", level="C", tr="dissolve", trd=0.45,
    intent="Quán cà phê sáng cài ngầm Ông Tám: cả Ông Tám & Ông Thành chớp mắt + chép miệng đối thoại + nắng sớm lấp lánh",
)
living("c03", [
    dict(char="tam", speaker="anh_hai", line_ids=["l09a_tam", "l09_tam"], first_offset=1.5, interval=4.0),
    dict(char="thanh", speaker="ong_bay", line_ids=["l10_thanh"], first_offset=2.4, interval=4.2),
])
fx({"type": "ambient_particles", "count": 22, "opacity": 0.24, "color": [255, 245, 200], "drift_dir": "float", "seed": 73})
fx({"type": "color_mood", "mood": "warm_daily", "strength": 0.50, "vignette": 0.08, "grain": 0.0})
beat(0.8)
line("l09a_tam", "TAM", "Mới lãnh cục tiền hưu về, tính sửa nhà cho cháu ngoại rồi để tiền nằm không vậy hả Thành?",
     "nhâm nhi cà phê, hỏi thăm tự nhiên mà ánh mắt dò xét kỹ từng chi tiết")
line("l09_tam", "TAM", "Chơi với mày tao khoái cái tính sòng phẳng. Có chuyện gì cứ gọi một tiếng, mấy thằng em ngoài đời của tao lo liền.",
     "sang sảng, vỗ vai bạn cũ ra vẻ quen rộng trên bàn cà phê sáng")
line("l10_thanh", "THANH", "Sống tới tuổi này hơn nhau chỗ biết rộng, quen nhiều! Chứ đụng chuyện mà đi làm đơn chờ thủ tục tới chừng nào.",
     "cười tự đắc, nâng ly cà phê đầy tin tưởng vào mối quan hệ ngoài đời", pause=0.5)

# Làm mờ quá trình dẫn dụ 3 tuần – đẩy thẳng vào hậu quả cao trào mất 200 triệu
amb("night_room", -2.5); bgm("tension_drone", -3.0)
scene(
    "s04_first_trap_aftermath", "assets/c04.jpg",
    motion={"preset": "slow_push_in", "scale": [1.02, 1.09], "focus": [[0.56, 0.52], [0.60, 0.58]], "wobble": "tense", "easing": "ease_out"},
    beat_type="climax", level="C", tr="zoom_punch", trd=0.30,
    intent="Cú sập ứng dụng sau 3 tuần: Ông Thành chớp mắt & chép miệng 4 trạng thái + Chromatic Pulse + khoanh đỏ màn hình app bị đóng băng + bộ đếm -200.000.000đ + ánh màn hình lạnh",
)
living("c04", [dict(char="thanh", speaker="ong_bay", line_ids=["l11_thanh"], first_offset=1.4, interval=3.9)])
fx({"type": "chromatic_pulse", "at": 95.55, "dur": 0.30, "shift_px": 7, "zoom_blur": 0.025})
fx({"type": "screen_glow", "pos": [0.65, 0.83], "radius": [0.16, 0.14],
    "color": [235, 95, 110], "intensity": 0.28, "mode": "flicker", "start": 95.2, "end": 108.4, "fade": 0.3})
fx({"type": "red_circle_draw", "region": [0.56, 0.77, 0.75, 0.90], "at": 97.2, "dur": 0.50, "end": 106.5,
    "style": "circle", "width": 5, "color": [245, 55, 55]})
fx({"type": "animated_counter", "start": 98.4, "end": 107.8, "count_dur": 1.8,
    "from_val": 0, "to_val": -200000000, "fmt": "vnd", "label": "TIỀN DƯỠNG GIÀ BỊ ĐÓNG BĂNG",
    "pos": [0.24, 0.72], "style": "danger", "easing": "ease_out"})
fx({"type": "color_mood", "mood": "high_tension", "strength": 0.54, "vignette": 0.24, "grain": 0.014})
sfx("glitch", 0.35, -3.5)
sfx("impact", 0.65, -3.5)
sfx("notification", 1.50, -4.5)
sfx_abs("marker_draw", 97.20, -4.5)
sfx_abs("counter_tick", 98.40, -5.5)
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
scene(
    "s05_reject_police", "assets/c05.jpg",
    motion={"preset": "pan_left", "scale": [1.05, 1.05], "focus": [[0.53, 0.48], [0.47, 0.48]], "wobble": "none", "easing": "smoothstep"},
    beat_type="suspicion", level="C", tr="luma_wipe", trd=0.40,
    intent="Xung đột cha – con gái sáng hôm sau: Trang & Ông Thành chớp mắt + chép miệng đối thoại căng thẳng + tông Cold Suspicion dịu",
)
living("c05", [
    dict(char="trang", speaker="chi_hai", line_ids=["l12_trang", "l14_trang"], first_offset=1.4, interval=3.9),
    dict(char="thanh", speaker="ong_bay", line_ids=["l13_thanh", "l15_thanh"], first_offset=2.3, interval=4.1),
])
fx({"type": "color_mood", "mood": "cold_suspicion", "strength": 0.30, "vignette": 0.14, "grain": 0.008})
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
beat(1.1)

amb("street", -5.0); bgm("investigative_story", -4.0)
scene(
    "s06_meet_tam", "assets/c06.jpg",
    motion={"preset": "static_hold"},
    beat_type="suspicion", level="C", tr="dissolve", trd=0.40,
    intent="Khung tĩnh có chủ đích tại quán cà phê trưa: Ông Tám & Ông Thành chép miệng đối thoại (Ông Tám chớp mắt dò xét) + khoanh đỏ phong bì & tờ biên lai + bụi nắng nhẹ",
)
living("c06", [
    dict(char="tam", speaker="anh_hai", line_ids=["l17a_tam", "l17c_tam"], first_offset=1.5, interval=4.0),
    dict(char="thanh", speaker="ong_bay", line_ids=["l16_thanh", "l17b_thanh"], blink=False),
])
fx({"type": "red_circle_draw", "region": [0.58, 0.67, 0.73, 0.79], "at": 151.0, "dur": 0.50, "end": 161.5,
    "style": "circle", "width": 5, "color": [242, 65, 65]})
fx({"type": "ambient_particles", "count": 14, "opacity": 0.18, "color": [255, 236, 190], "drift_dir": "float", "seed": 76})
fx({"type": "color_mood", "mood": "warm_daily", "strength": 0.35, "vignette": 0.12, "grain": 0.006})
sfx("notification", 0.25, -5.0)
sfx_abs("marker_draw", 151.00, -4.5)
bubble("BIÊN LAI CHUYỂN KHOẢN", "Người nhận: ••••• (TK ••••) · Tổng cộng 3 tuần: 200.000.000đ",
       side="left", y=260, stamp="ĐƯA 5 TRIỆU ĐI HỎI", dur=5.4, offset=0.25)
beat(1.2)
line("l16_thanh", "THANH", "Chút tiền xăng xe cho mấy đứa nhỏ đi việc. Mày coi quen ai rành, lần giùm tao cái tài khoản này nha Tám.",
     "nôn nóng, đẩy phong bì tiền mặt qua bàn")
line("l17a_tam", "TAM", "Mày chưa báo công an, cũng chưa nói kỹ với con Trang phải hông?",
     "hạ giọng nhẹ như hỏi thăm, ánh mắt dừng kỹ trên tờ biên lai")
line("l17b_thanh", "THANH", "Chưa, tao hẹn nó ba ngày tự lo.",
     "gật đầu chắc nịch vì sĩ diện")
line("l17c_tam", "TAM", "Ừ, để tao hỏi mấy đứa coi sao.",
     "cất gọn phong bì, nét mặt thoáng lạnh rồi điềm nhiên trở lại", pause=0.5)

amb("street", -4.5); bgm("tension_drone", -2.5)
scene(
    "s07_tam_brushoff", "assets/c07.jpg",
    motion={"preset": "slow_pull_out", "scale": [1.07, 1.02], "focus": [[0.62, 0.46], [0.56, 0.48]], "wobble": "none", "easing": "smoothstep"},
    beat_type="climax", level="B", tr="luma_wipe", trd=0.40,
    intent="2.5D Parallax cú phủi tay giữa chạng vạng: Rack Focus mở chiều sâu cổng sắt + Breathing + Head Micro-Tilt + Ông Thành chớp mắt & chép miệng 4 trạng thái (fg) + sóng âm Ông Tám + vệt sáng hoàng hôn",
    parallax={
        "camera": "pull_out",
        "dolly": [1.07, 1.02],
        "shift_x": [0.0, 0.0],
        "shift_y": [-3.0, 0.0],
        "focus": [0.64, 0.46],
        "strength": 0.85,
        "easing": "smoothstep",
        "layers": [
            {"role": "bg", "image": "assets/s07_bg.jpg", "depth": 0.42, "blur_from": 2.4, "blur_to": 0.5, "blur_at": 166.0, "blur_dur": 4.0},
            {"role": "fg", "image": "assets/s07_fg.png", "depth": 1.24, "breathe_y": 1.8, "breathe_period": 3.4,
             "head_tilt_deg": 1.0, "head_pivot": [0.68, 0.88], "tilt_speaker": "ong_bay", "tilt_line_ids": ["l19_thanh"]},
        ],
    },
)
living("c07", [dict(char="thanh", speaker="ong_bay", line_ids=["l19_thanh"], first_offset=1.6, interval=4.0, layer="fg")])
fx({"type": "phone_waveform", "speaker": "anh_hai", "line_ids": ["l18_tam", "l20_tam"],
    "start": 166.5, "end": 188.5, "pos": [0.24, 0.56], "size": [0.25, 0.058],
    "color": [255, 175, 80], "label": "ÔNG TÁM · ĐIỆN THOẠI"})
fx({"type": "light_sweep", "mode": "light", "color": [255, 190, 125], "intensity": 0.14, "width": 0.20, "angle_deg": -18.0, "repeat": 1})
fx({"type": "color_mood", "mood": "cold_suspicion", "strength": 0.36, "vignette": 0.18, "grain": 0.010})
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
beat(2.4)

# ---- HỒI 3 · CÁI BẪY LẦN HAI: NHỬ TỪNG ĐỢT NHỎ & ẢO GIÁC "TRONG LÒNG BÀN TAY" ----
amb("night_room", -2.0); bgm("tension_drone", -2.8)
scene(
    "s08_search_alone", "assets/c08.jpg",
    motion={"preset": "pan_right", "scale": [1.05, 1.05], "focus": [[0.48, 0.48], [0.54, 0.46]], "wobble": "none", "easing": "smoothstep"},
    beat_type="information", level="C", tr="whip_pan_left", trd=0.30,
    intent="Đêm khuya tìm nhóm hỗ trợ lấy lại tiền: Ông Thành chớp mắt & chép miệng 4 trạng thái hỏi vặn sắc bén + typing_indicator + sóng âm Khoa + ánh màn hình lạnh",
)
living("c08", [dict(char="thanh", speaker="ong_bay", line_ids=["l23_thanh"], first_offset=1.6, interval=4.0)])
fx({"type": "screen_glow", "pos": [0.58, 0.42], "radius": [0.16, 0.16],
    "color": [110, 210, 255], "intensity": 0.24, "mode": "pulse", "start": 191.9, "end": 218.5, "fade": 0.3})
fx({"type": "typing_indicator", "start": 192.60, "end": 193.70, "side": "left", "y": 480})
fx({"type": "phone_waveform", "speaker": "ke_ngot_ngao_nam", "line_ids": ["l22_khoa", "l24_khoa"],
    "start": 194.6, "end": 216.2, "pos": [0.24, 0.68], "size": [0.25, 0.058],
    "color": [95, 210, 245], "label": "KHOA · ĐỘI KỸ THUẬT"})
fx({"type": "color_mood", "mood": "cold_suspicion", "strength": 0.44, "vignette": 0.18, "grain": 0.012})
chapter("HỒI 3 · CÁI BẪY LẦN HAI", "NHÓM LẤY LẠI TIỀN & MỒI NHỬ TỪNG BƯỚC")
sfx("chapter_sting", -0.1, -5)
sfx("typing", 0.4, -5.5, dur=1.2)
sfx("notification", 1.8, -5.0)
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
scene(
    "s09_insider_detail", "assets/c09.jpg",
    motion={"preset": "slow_push_in", "scale": [1.02, 1.09], "focus": [[0.56, 0.46], [0.60, 0.44]], "wobble": "breathe", "easing": "ease_out"},
    beat_type="anomaly", level="C", tr="dissolve", trd=0.42,
    intent="Cú buông tên 'Ngọc' đánh sập cảnh giác: Ông Thành chớp mắt & chép miệng 4 trạng thái sững sờ + Chromatic Pulse + sóng âm Khoa + ánh điện thoại xanh",
)
living("c09", [dict(char="thanh", speaker="ong_bay", line_ids=["l26_thanh"], first_offset=1.5, interval=3.9)])
fx({"type": "screen_glow", "pos": [0.58, 0.42], "radius": [0.16, 0.16],
    "color": [105, 225, 245], "intensity": 0.25, "mode": "pulse", "start": 219.0, "end": 240.5, "fade": 0.3})
fx({"type": "phone_waveform", "speaker": "ke_ngot_ngao_nam", "line_ids": ["l25_khoa", "l26b_khoa"],
    "start": 220.2, "end": 239.2, "pos": [0.24, 0.56], "size": [0.25, 0.058],
    "color": [95, 220, 200], "label": "KHOA · KIỂM TRA DỮ LIỆU"})
fx({"type": "chromatic_pulse", "at": 226.40, "dur": 0.28, "shift_px": 6, "zoom_blur": 0.02})
fx({"type": "color_mood", "mood": "cold_suspicion", "strength": 0.46, "vignette": 0.20, "grain": 0.012})
sfx("notification", 0.2, -3)
sfx_abs("low_accent", 226.40, -6.5)
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

# Cảnh cận cực đắt: 1tr -> 2tr (phát lại ghi âm cũ của Ngọc) -> 7tr (mở cổng giải tỏa)
scene(
    "s09b_bait_proof", "assets/c09b.jpg",
    motion={"preset": "slow_pull_out", "scale": [1.07, 1.02], "focus": [[0.62, 0.48], [0.58, 0.50]], "wobble": "none", "easing": "smoothstep"},
    beat_type="information", level="C", tr="whip_pan_right", trd=0.28,
    intent="Cận mặt bẫy bằng chứng mồi: Ông Thành chớp mắt & chép miệng 4 trạng thái tin sái cổ + sóng âm Ghi âm Ngọc & Khoa + bộ đếm -10.000.000đ + ánh màn hình xanh sáng rực",
)
living("c09b", [dict(char="thanh", speaker="ong_bay", line_ids=["l26e_thanh"], first_offset=1.5, interval=3.9)])
fx({"type": "screen_glow", "pos": [0.62, 0.78], "radius": [0.20, 0.16],
    "color": [85, 240, 210], "intensity": 0.28, "mode": "pulse", "start": 241.0, "end": 266.6, "fade": 0.3})
fx({"type": "phone_waveform", "speaker": "ke_ngot_ngao_nu", "line_ids": ["l26d_ngoc_rec", "l27_khoa"],
    "start": 242.2, "end": 263.0, "pos": [0.24, 0.56], "size": [0.25, 0.058],
    "color": [90, 235, 195], "label": "GHI ÂM CŨ & KHOA"})
fx({"type": "animated_counter", "start": 262.8, "end": 266.6, "count_dur": 1.6,
    "from_val": 0, "to_val": -10000000, "fmt": "vnd", "label": "PHÍ NHỬ 3 ĐỢT ĐẦU",
    "pos": [0.24, 0.68], "style": "warn", "easing": "ease_out"})
fx({"type": "color_mood", "mood": "noir_evidence", "strength": 0.45, "vignette": 0.20, "grain": 0.012})
mark("bait_proof")
sfx("bank_ting", 0.15, -3.5)
sfx("notification", 0.55, -3)
sfx_abs("counter_tick", 262.80, -5.5)
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

# Trọng tâm tâm lý: sunk cost 10tr & thể diện trước con gái bên khe cửa vàng ấm
amb("night_room", -1.8); bgm("tension_drone", -2.0)
scene(
    "s10_doubt_and_lie", "assets/c10.jpg",
    motion={"preset": "static_hold"},
    beat_type="suspicion", level="C", tr="luma_wipe", trd=0.42,
    intent="Khung tĩnh nghẹt thở bên khe cửa phòng con gái: Ông Thành chớp mắt & chép miệng 4 trạng thái nói dối con + ánh màn hình lạnh đối lập khe cửa vàng ấm + sóng âm Khoa ép 95%",
)
living("c10", [dict(char="thanh", speaker="ong_bay", line_ids=["l28_thanh", "l31_thanh"], first_offset=1.5, interval=4.1)])
fx({"type": "screen_glow", "pos": [0.57, 0.80], "radius": [0.16, 0.14],
    "color": [125, 225, 255], "intensity": 0.25, "mode": "flicker", "start": 267.1, "end": 302.5, "fade": 0.3})
fx({"type": "phone_waveform", "speaker": "ke_ngot_ngao_nam", "line_ids": ["l29_khoa"],
    "start": 277.6, "end": 285.0, "pos": [0.24, 0.56], "size": [0.25, 0.058],
    "color": [255, 95, 85], "label": "KHOA · HỒ SƠ CHẠY TỚI 95%"})
fx({"type": "light_sweep", "mode": "light", "color": [255, 210, 140], "intensity": 0.12, "width": 0.18, "angle_deg": -15.0, "repeat": 2})
fx({"type": "color_mood", "mood": "high_tension", "strength": 0.44, "vignette": 0.22, "grain": 0.012})
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

# Cảnh câm: tháo đồng hồ cầm đồ gom 30tr cuối (tổng 55tr)
amb("street", -5.5); bgm("tension_drone", -2.2)
scene(
    "s11_pawn_watch", "assets/c11.jpg",
    motion={"preset": "pan_left", "scale": [1.05, 1.05], "focus": [[0.54, 0.56], [0.48, 0.60]], "wobble": "none", "easing": "smoothstep"},
    beat_type="aftermath", level="C", tr="film_burn", trd=0.45,
    intent="Cảnh câm tháo chiếc đồng hồ kỷ niệm đặt lên quầy kính: bộ đếm cộng dồn -10.000.000đ -> -55.000.000đ + Cold Suspicion",
)
fx({"type": "animated_counter", "start": 306.0, "end": 309.9, "count_dur": 1.8,
    "from_val": -10000000, "to_val": -55000000, "fmt": "vnd", "label": "TỔNG NỘP LẦN HAI (5 ĐỢT)",
    "pos": [0.24, 0.68], "style": "danger", "easing": "ease_out"})
fx({"type": "color_mood", "mood": "cold_suspicion", "strength": 0.42, "vignette": 0.18, "grain": 0.010})
sfx("notification", 0.25, -5.0)
sfx_abs("counter_tick", 306.00, -5.0)
bubble("LỆNH HOÀN TIỀN #094 · CHỜ DUYỆT", "Hiển thị +200.000.000đ chờ vào TK (không mã tra soát) · Nộp 30.000.000đ giải ngân",
       side="left", y=245, stamp="CHỈ CÒN 1 BƯỚC", dur=3.0, offset=0.25)
bubble("LỊCH SỬ CHUYỂN KHOẢN · 5 ĐỢT", "1tr + 2tr + 7tr + 15tr + 30tr · Tổng lần hai: -55.000.000đ",
       side="left", y=245, stamp="CẠN SẠCH TIỀN", dur=3.5, offset=3.4)
sfx("bank_ting", 3.5, -3.5)
sfx("heartbeat", 4.1, -4.5, dur=2.4)
beat(7.1)

# Cắt kết nối dứt khoát
amb("night_room", -1.5); bgm("tension_drone", SILENT)
scene(
    "s12_mask_off", "assets/c12.jpg",
    motion={"preset": "slow_push_in", "scale": [1.02, 1.09], "focus": [[0.56, 0.46], [0.58, 0.44]], "wobble": "tense", "easing": "ease_out"},
    beat_type="climax", level="B", tr="zoom_punch", trd=0.28,
    intent="2.5D Parallax cao trào sụp đổ: Rack Focus mờ phòng tối + Breathing nặng nề + sóng âm Khoa cắt kết nối + Chromatic Pulse cú chặn + vệt đèn quét lạnh",
    parallax={
        "camera": "push_in",
        "dolly": [1.02, 1.09],
        "shift_x": [0.0, 0.0],
        "shift_y": [0.0, -4.0],
        "focus": [0.58, 0.46],
        "strength": 0.90,
        "easing": "ease_out",
        "layers": [
            {"role": "bg", "image": "assets/s12_bg.jpg", "depth": 0.40, "blur_from": 0.4, "blur_to": 3.6, "blur_at": 312.5, "blur_dur": 4.5},
            {"role": "fg", "image": "assets/s12_fg.png", "depth": 1.24, "breathe_y": 2.0, "breathe_period": 3.0},
        ],
    },
)
fx({"type": "phone_waveform", "speaker": "ke_ngot_ngao_nam", "line_ids": ["l32_khoa"],
    "start": 311.0, "end": 316.8, "pos": [0.24, 0.56], "size": [0.25, 0.060],
    "color": [255, 85, 85], "label": "KHOA · HẾT HỖ TRỢ"})
fx({"type": "chromatic_pulse", "at": 317.45, "dur": 0.32, "shift_px": 7, "zoom_blur": 0.025})
fx({"type": "light_sweep", "mode": "light", "color": [140, 175, 225], "intensity": 0.12, "width": 0.22, "angle_deg": -20.0, "repeat": 1})
fx({"type": "color_mood", "mood": "high_tension", "strength": 0.56, "vignette": 0.28, "grain": 0.015})
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
scene(
    "s13_unanswered_call", "assets/c13.jpg",
    motion={"preset": "slow_pull_out", "scale": [1.07, 1.02], "focus": [[0.60, 0.50], [0.54, 0.50]], "wobble": "none", "easing": "smoothstep"},
    beat_type="aftermath", level="C", tr="luma_wipe", trd=0.45,
    intent="Cuộc gọi không ai bắt máy dưới ánh trăng: ánh điện thoại tắt dần + vệt trăng quét + tông Flashback lạnh lẽo vọng lời hứa Ông Tám",
)
fx({"type": "screen_glow", "pos": [0.64, 0.80], "radius": [0.14, 0.12],
    "color": [135, 195, 235], "intensity": 0.20, "mode": "pulse", "start": 321.4, "end": 326.5, "fade": 0.4})
fx({"type": "light_sweep", "mode": "light", "color": [175, 205, 245], "intensity": 0.14, "width": 0.20, "angle_deg": -22.0, "repeat": 1})
fx({"type": "color_mood", "mood": "flashback", "strength": 0.42, "vignette": 0.22, "grain": 0.012})
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
scene(
    "s14_bare_wrist_confession", "assets/c14.jpg",
    motion={"preset": "static_hold"},
    beat_type="aftermath", level="C", tr="dissolve", trd=0.50,
    intent="Khung tĩnh nhân văn cha – con gái: Trang chớp mắt & chép miệng + Ông Thành chép miệng nghẹn ngào sau bàn tay + ánh đèn hành lang ấm + hạt bụi ánh sáng",
)
living("c14", [
    dict(char="trang", speaker="chi_hai", line_ids=["l34_trang", "l36_trang"], first_offset=1.5, interval=4.2),
    dict(char="thanh", speaker="ong_bay", line_ids=["l35_thanh"], blink=False),
])
fx({"type": "ambient_particles", "count": 18, "opacity": 0.24, "color": [255, 224, 165], "drift_dir": "float", "seed": 84})
fx({"type": "color_mood", "mood": "warm_daily", "strength": 0.56, "vignette": 0.14, "grain": 0.006})
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
scene(
    "s15_police_truth", "assets/c15.jpg",
    motion={"preset": "pan_right", "scale": [1.05, 1.05], "focus": [[0.47, 0.50], [0.53, 0.50]], "wobble": "none", "easing": "smoothstep"},
    beat_type="information", level="C", tr="luma_wipe", trd=0.45,
    intent="Phòng tiếp nhận trình báo chuẩn mực: Cán bộ, Ông Thành & Trang chớp mắt + Cán bộ & Ông Thành chép miệng đối thoại rõ ràng + tông tỉnh táo",
)
living("c15", [
    dict(char="cb", speaker="chi_tu", line_ids=["l37_cb", "l39a_cb", "l39b_cb"], first_offset=1.4, interval=4.0),
    dict(char="thanh", speaker="ong_bay", line_ids=["l38_thanh"], first_offset=2.2, interval=4.2),
    dict(char="trang", first_offset=2.9, interval=4.4),
])
fx({"type": "color_mood", "mood": "cold_suspicion", "strength": 0.20, "vignette": 0.08, "grain": 0.0})
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
scene(
    "s16_drawer_seen", "assets/c16.jpg",
    motion={"preset": "slow_pull_out", "scale": [1.06, 1.02], "focus": [[0.54, 0.50], [0.50, 0.50]], "wobble": "none", "easing": "smoothstep"},
    beat_type="aftermath", level="C", tr="film_burn", trd=0.48,
    intent="Cảnh câm cất bản vẽ sửa nhà vào hộc tủ: tông Flashback trầm buồn + hạt bụi chiều muộn",
)
fx({"type": "ambient_particles", "count": 16, "opacity": 0.20, "color": [235, 220, 195], "drift_dir": "float", "seed": 86})
fx({"type": "color_mood", "mood": "flashback", "strength": 0.34, "vignette": 0.14, "grain": 0.008})
chapter("HỒI 5 · ĐỐI DIỆN SỰ THẬT", "BẢN VẼ TRONG HỘC TỦ")
sfx("chapter_sting", -0.1, -5)
sfx("notification", 0.6, -5.5)
bubble("ÔNG TÁM", "Tám ơi, tao đang kẹt xoay tiền, mày cho tao mượn tạm ít bữa…",
       side="left", y=270, stamp="ĐÃ XEM · 3 NGÀY TRƯỚC", dur=5.0, offset=0.6)
beat(5.8)

amb("room_tone", -3.0); bgm("warm_outro", -5.5)
scene(
    "s17_grandson_question", "assets/c17.jpg",
    motion={"preset": "pan_left", "scale": [1.05, 1.05], "focus": [[0.53, 0.50], [0.47, 0.50]], "wobble": "none", "easing": "smoothstep"},
    beat_type="aftermath", level="C", tr="dissolve", trd=0.45,
    intent="Pan ngang dịu nhẹ ngoài hiên chạng vạng: Bé Bo chớp mắt & chép miệng hỏi ông ngoại + Ông Thành chớp mắt lặng người",
)
living("c17", [
    dict(char="bo", speaker="be_tom", line_ids=["l40_bo"], first_offset=1.2, interval=3.8),
    dict(char="thanh", first_offset=2.1, interval=4.2),
])
mark("grandson_q")
beat(0.8)
line("l40_bo", "BO", "Ông ngoại ơi, chừng nào chú thợ qua làm phòng mới có cửa sổ cho con học lớp Một hả ông?",
     "trong trẻo, hồn nhiên, kéo gấu áo ông ngoại hỏi khẽ", pause=1.2)

scene(
    "s18_face_the_truth", "assets/c18.jpg",
    motion={"preset": "slow_push_in", "scale": [1.02, 1.07], "focus": [[0.50, 0.46], [0.50, 0.44]], "wobble": "none", "easing": "smoothstep"},
    beat_type="aftermath", level="C", tr="dissolve", trd=0.45,
    intent="Cái kết nhân văn bên cháu ngoại: Ông Thành & Bé Bo chớp mắt + Ông Thành chép miệng 4 trạng thái rưng rưng đối diện sự thật + hạt nắng hoàng hôn ấm áp",
)
living("c18", [
    dict(char="thanh", speaker="ong_bay", line_ids=["l41_thanh"], first_offset=1.5, interval=4.1),
    dict(char="bo", first_offset=2.4, interval=3.9),
])
fx({"type": "ambient_particles", "count": 24, "opacity": 0.28, "color": [255, 224, 155], "drift_dir": "float", "seed": 88})
fx({"type": "color_mood", "mood": "warm_daily", "strength": 0.66, "vignette": 0.10, "grain": 0.0})
beat(1.1)
line("l41_thanh", "THANH", "Chắc còn lâu lắm con… Ông ngoại tính sai rồi. Nhưng năm sau con vô lớp Một, ông vẫn tập viết với con mỗi tối.",
     "ngồi ngang tầm cháu, mắt đỏ hoe mà dịu lại, giọng khàn nén xúc động xoa đầu cháu trai", pause=1.0)
beat(2.8)

# ---- MÀN HÌNH ĐEN · CHỮ TRẮNG ----
amb("room_tone", -8.0); bgm("warm_outro", -9.5)
scene(
    "s19_black_epilogue", "assets/c20.jpg",
    motion={"preset": "static_hold"},
    beat_type="ending", level="A", tr="fade_black", trd=0.60,
    intent="Khung đen tĩnh tuyệt đối cho 2 câu kết lắng đọng cuối Hồi 5",
)
mark("black_text")
chapter("", "Kẻ lừa đầu tiên lấy tiền bằng lời hứa bạn sẽ có thêm.", offset=0.5, dur=3.8)
chapter("", "Kẻ thứ hai lấy nốt phần còn lại, bằng nỗi xấu hổ không dám nói ra.", offset=4.6, dur=4.5)
beat(9.8)

# ---- THẺ NHỚ KỸ (DƯỚI 10 GIÂY · NGƯỜI BÓC TRẦN ĐÚNG 1 CÂU) ----
amb("room_tone", -5.0); bgm("warm_outro", -4.5)
scene(
    "s20_red_flags", EP01B + "scene18.jpg",
    motion={"preset": "static_hold"},
    beat_type="ending", level="A", tr="dissolve", trd=0.40,
    intent="Khung tĩnh sạch tuyệt đối để khán giả đọc 5 nguyên tắc tránh bẫy lừa lần hai",
)
mark("rf_start")
sfx("bank_ting", 0.0, -5)
line("l42_narr", "N", "Giấu người nhà, nhờ người quen thay vì báo công an, là mở cửa cho lần lừa thứ hai.")
beat(1.0)
mark("rf_end")

# ---- KẾT MỞ · CÙNG MỘT ĐẦU MỐI & NHÂN VẬT BÍ ẨN ÔNG TÁM ----
amb("night_room", -3.0); bgm("tension_drone", -1.2)
scene(
    "s21_scam_ring_coda", "assets/c19.jpg",
    motion={"preset": "slow_push_in", "scale": [1.02, 1.10], "focus": [[0.58, 0.48], [0.66, 0.46]], "wobble": "breathe", "easing": "ease_in"},
    beat_type="climax", level="C", tr="luma_wipe", trd=0.38,
    intent="Coda lớp 1 phòng tối giấu mặt: ánh 2 màn hình cyan + sóng âm báo cáo của Khoa + Noir Evidence",
)
fx({"type": "screen_glow", "pos": [0.74, 0.42], "radius": [0.24, 0.20],
    "color": [95, 215, 240], "intensity": 0.26, "mode": "pulse", "start": 443.6, "end": 451.8, "fade": 0.25})
fx({"type": "phone_waveform", "speaker": "ke_ngot_ngao_nam", "line_ids": ["l43_khoa_coda"],
    "start": 445.2, "end": 451.5, "pos": [0.24, 0.56], "size": [0.25, 0.058],
    "color": [95, 225, 245], "label": "BÁO CÁO · CÙNG ĐẦU MỐI"})
fx({"type": "color_mood", "mood": "noir_evidence", "strength": 0.68, "vignette": 0.28, "grain": 0.018})
sfx("typing", 0.15, -5, dur=1.2)
bubble("HỒ SƠ TUẦN NÀY", "Vòng 1 (3 tuần): -200.000.000đ  ->  Vòng 2 (5 đợt): +55.000.000đ",
       side="left", y=250, stamp="CHUYỂN VÒNG 2", dur=5.6, offset=0.5)
beat(1.6)
mark("ring_coda")
line("l43_khoa_coda", "KHOA_ROOM", "Hồ sơ hai trăm triệu con Ngọc chuyển qua, nhử năm đợt bên em chốt thêm năm mươi lăm triệu rồi anh.",
     "bình thản báo cáo như xong một đơn hàng",
     sub="Hồ sơ 200 triệu con Ngọc chuyển qua, nhử 5 đợt bên em chốt thêm 55 triệu rồi anh.", pause=0.25)

# Cú lật tối giản hoàn toàn câm: bóng lưng Ông Tám + lắc bạc + màn hình app quen thuộc trên bàn
amb("street", -5.5); bgm("tension_drone", -0.8)
scene(
    "s21b_tam_coda", "assets/c19b.jpg",
    motion={"preset": "slow_pull_out", "scale": [1.08, 1.02], "focus": [[0.46, 0.56], [0.50, 0.50]], "wobble": "none", "easing": "ease_out"},
    beat_type="climax", level="C", tr="whip_pan_left", trd=0.28,
    intent="Cú lật câm quán cà phê ven biển: Whip Pan đột ngột + khoanh đỏ màn hình app quen thuộc trên bàn + Chromatic Pulse lạnh gáy",
)
fx({"type": "red_circle_draw", "region": [0.27, 0.80, 0.42, 0.96], "at": 453.2, "dur": 0.45, "end": 456.6,
    "style": "circle", "width": 5, "color": [250, 55, 55]})
fx({"type": "chromatic_pulse", "at": 456.25, "dur": 0.28, "shift_px": 7, "zoom_blur": 0.025})
fx({"type": "color_mood", "mood": "noir_evidence", "strength": 0.30, "vignette": 0.20, "grain": 0.012})
sfx_abs("marker_draw", 453.20, -4.0)
mark("tam_twist")
sfx("heartbeat", 0.6, -4.5, dur=2.6)
beat(4.4)

sfx("impact", 0.0, -1)
scene(
    "s22_black_cut", "assets/c20.jpg",
    motion={"preset": "static_hold"},
    beat_type="ending", level="A", tr="cut", trd=0.0,
    intent="Cú cắt đen đột ngột giữ dư âm lạnh sau cú lật bóng lưng Ông Tám",
)
beat(2.0)

# ---- DISCLAIMER ----
amb("room_tone", -6.0); bgm("tension_drone", -8.0)
scene(
    "s23_disclaimer", EP01B + "scene18.jpg",
    motion={"preset": "static_hold"},
    beat_type="ending", level="A", tr="fade_black", trd=0.35,
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
    "version": "v6-level3-full-abc-staging",
    "motion_upgrade": "level3",
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
    f"episode.json (v6-level3-full-abc-staging): {total:.2f}s ({mmss(total)}) · {len(scenes)} cảnh · "
    f"{len(dialogue)} câu · {words} từ ({words / (total / 60):.0f} từ/phút) · câu dài nhất {maxw} từ · "
    f"Bóc trần {len(narr_lines)} câu ({narr} từ, thẻ kết {rf_dur}s) · "
    f"{'TTS thật' if real else 'ước tính'} ({len(real)} câu thật)"
)
print(desc_chapters)
