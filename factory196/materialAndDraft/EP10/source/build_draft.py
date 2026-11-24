# -*- coding: utf-8 -*-
"""
Trình biên dịch `factory196/materialAndDraft/EP10/episode.json` – Tập EP10:
"Giám đốc 100 Agent – Suất cuối giảm 80%" (16:9 Long-form · Cơn bão FOMO AI 2026 & Vũ trụ Chị Hai EP04/EP06/EP08b/EP10).

Chuẩn Visual Motion Upgrade Level 2 + Living-Character A/B/C (HRN-MOTION-L2.1):
  - Level B (2.5D Parallax + Breathing): 4 cảnh (s00, s04, s06, s08)
  - Level C (Living-Character eye_blink + 3-state mouth_sync từ WAV thật + breathing + detail_reveal/screen_glow/light_shift/focus_highlight): 13 cảnh
  - Level A (Static Hold sạch): 3 cảnh (s15, s17, s18)
  - 0 chuỗi lặp >= 3 push_in · 0 hiệu ứng bị loại trừ L480 · 100% foley khớp mốc sự kiện

Nguồn sự thật duy nhất của timeline:
    python factory196/materialAndDraft/EP10/source/build_draft.py
"""
from __future__ import annotations

import json
import wave
from pathlib import Path

HERE = Path(__file__).resolve().parent
EP = HERE.parent
ASSETS = EP / "assets"
TTS = EP / "audio" / "tts"
OUT = EP / "episode.json"

SEC_PER_WORD = 0.33
LINE_BASE = 0.85
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

# Optional auto-baked Living-Character ROI config produced after face_roi_prep.py
ROI_CFG_PATH = HERE / "face_rois.json"
FACE_ROIS: dict = json.loads(ROI_CFG_PATH.read_text(encoding="utf-8")) if ROI_CFG_PATH.is_file() else {}

# ---------------------------------------------------------------- GIỌNG
# 9 tuyến nhân vật = 9 voice hoàn toàn tách biệt trong 02_CAST/cast.json
NOT_OLD = "tuyệt đối không giả giọng ông già hay bà già run rẩy, không kéo dài chữ, không cải lương"

TUAN_BASE = (
    "Giọng nam miền Nam Sài Gòn 35 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
    "giữ cố định một âm sắc trầm chắc, thật thà đời thường kiểu chủ tiệm nhỏ, nói gọn rõ chữ, tự nhiên như đời thực, "
    + NOT_OLD
)
HUONG_BASE = (
    "Giọng phụ nữ miền Nam Sài Gòn 33 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
    "giữ cố định một âm sắc trầm vừa, sắc bén thực tế, điềm tĩnh gọn gàng, nói chắc chữ tự nhiên như đời thực, "
    + NOT_OLD
)
QUANG_BASE = (
    "Giọng nam miền Nam Sài Gòn 38 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
    "giữ cố định một âm sắc trầm mượt, vang gọn và đầy sức hút kiểu diễn giả công nghệ, nói rõ từng chữ, "
    + NOT_OLD
)
KHANH_BASE = (
    "Giọng nam thanh niên miền Nam Sài Gòn 27 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
    "giữ cố định một âm sắc sáng trẻ, lịch sự mượt mà kiểu trợ lý điều phối, nhịp nói nhanh gọn, "
    + NOT_OLD
)
LAN_BASE = (
    "Giọng phụ nữ miền Nam Sài Gòn 44 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
    "giữ cố định một âm sắc thân tình chân chất kiểu tiểu thương bán vải ngoài chợ, nói tự nhiên nhanh nhẹn, "
    + NOT_OLD
)
MC_BASE = (
    "Giọng nữ MC sân khấu miền Nam Sài Gòn 28 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
    "giữ cố định một âm sắc tông cao sáng, hồ hởi năng lượng mạnh đẩy nhịp gấp gáp trên sân khấu hội nghị, "
    + NOT_OLD
)
GUARD_BASE = (
    "Giọng chú bảo vệ miền Nam Sài Gòn ngoài 55 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
    "giữ cố định một âm sắc trầm khàn nhẹ, chậm rãi hiền hậu và thẳng thắn đời thường, "
    "tuyệt đối không giả giọng cụ già yếu ớt, không kéo dài chữ"
)
CHIHAI_BASE = (
    "Giọng phụ nữ miền Nam Sài Gòn 35 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
    "giữ cố định một âm sắc sắc lạnh, trầm tĩnh, kiệm lời đầy uy quyền, nói ngắn cắt gọn không chút cảm xúc, "
    + NOT_OLD
)

SPK = {
    "TUAN": dict(
        speaker="anh_hai",
        voice="Orus",
        af="default",
        label_short="TUẤN",
        speaker_label="Tuấn – chủ tiệm đồ gia dụng nhỏ 35 tuổi, chăm chỉ nhưng lo âu tụt hậu trước cơn bão AI",
        base=TUAN_BASE,
    ),
    "HUONG": dict(
        speaker="chi_hai",
        voice="Sulafat",
        af="default",
        label_short="HƯƠNG",
        speaker_label="Hương – vợ Tuấn 33 tuổi, thực tế, sắc bén, bình tĩnh kiểm chứng và cứu nhóm học viên",
        base=HUONG_BASE,
    ),
    "QUANG": dict(
        speaker="chu_no",
        voice="Algieba",
        af="default",
        label_short="THẦY QUANG",
        speaker_label="Thầy Quang – diễn giả công nghệ 38 tuổi trên sân khấu hội nghị và phòng họp VIP",
        base=QUANG_BASE,
    ),
    "QUANG_P": dict(
        speaker="chu_no",
        voice="Algieba",
        af="phone",
        label_short="THẦY QUANG",
        speaker_label="Thầy Quang qua loa điện thoại / tin nhắn riêng / cuộc gọi báo cáo cấp trên",
        base=QUANG_BASE,
    ),
    "KHANH": dict(
        speaker="ke_ngot_ngao_nam",
        voice="Achird",
        af="default",
        label_short="TRỢ LÝ KHÁNH",
        speaker_label="Trợ lý Khánh – điều phối VIP 27 tuổi bàn giao văn phòng ảo không gian",
        base=KHANH_BASE,
    ),
    "KHANH_P": dict(
        speaker="ke_ngot_ngao_nam",
        voice="Achird",
        af="phone",
        label_short="TRỢ LÝ KHÁNH",
        speaker_label="Trợ lý Khánh nghe điện thoại lạnh đều ép nạp thêm 40 triệu mở cổng rút",
        base=KHANH_BASE,
    ),
    "LAN": dict(
        speaker="co_hanh",
        voice="Despina",
        af="default",
        label_short="CHỊ LAN",
        speaker_label="Chị Lan – chim mồi 44 tuổi đóng vai chủ sạp vải bật dậy chốt suất đầu tiên",
        base=LAN_BASE,
    ),
    "LAN_P": dict(
        speaker="co_hanh",
        voice="Despina",
        af="phone",
        label_short="CHỊ LAN",
        speaker_label="Chị Lan khoe lãi gấp đôi tiền học trong nhóm kín VIP",
        base=LAN_BASE,
    ),
    "MC": dict(
        speaker="ke_ban_hang",
        voice="Zephyr",
        af="default",
        label_short="MC HỘI TRƯỜNG",
        speaker_label="MC Hội trường 28 tuổi đẩy nhịp đếm ngược 10 phút giảm 80%",
        base=MC_BASE,
    ),
    "GUARD": dict(
        speaker="ong_bay",
        voice="Algenib",
        af="default",
        label_short="CHÚ BẢO VỆ",
        speaker_label="Chú Bảo Vệ 55 tuổi sảnh tòa nhà tiết lộ hội trường và chiếc xe trắng đều là đồ thuê",
        base=GUARD_BASE,
    ),
    "CHIHAI": dict(
        speaker="chi_ba",
        voice="Kore",
        af="default",
        label_short="CHỊ HAI",
        speaker_label="Chị Hai – người phụ nữ bí ẩn giấu mặt (đồng bộ EP04 & EP08b), sắc lạnh kiệm lời",
        base=CHIHAI_BASE,
    ),
    "N": dict(speaker="nguoi_boc_tran"),
}

# ---------------------------------------------------------------- MOTION PRESETS (LEVEL 2)
MOTION = {
    "static_hold": {"preset": "static_hold"},
    "static_breathe": {"preset": "static_hold", "scale": [1.03, 1.03], "focus": [[0.50, 0.50], [0.50, 0.50]], "wobble": "breathe"},
    "pan_right": {"preset": "pan_right", "scale": [1.06, 1.06], "focus": [[0.46, 0.49], [0.54, 0.49]], "wobble": "none"},
    "pan_right_breathe": {"preset": "pan_right", "scale": [1.06, 1.06], "focus": [[0.46, 0.49], [0.54, 0.49]], "wobble": "breathe"},
    "pan_left": {"preset": "pan_left", "scale": [1.06, 1.06], "focus": [[0.54, 0.49], [0.46, 0.49]], "wobble": "none"},
    "pan_left_breathe": {"preset": "pan_left", "scale": [1.06, 1.06], "focus": [[0.54, 0.49], [0.46, 0.49]], "wobble": "breathe"},
    "pull_out": {"preset": "slow_pull_out", "scale": [1.08, 1.02], "focus": [[0.50, 0.48], [0.50, 0.50]], "wobble": "none"},
    "pull_out_breathe": {"preset": "slow_pull_out", "scale": [1.08, 1.02], "focus": [[0.50, 0.47], [0.50, 0.50]], "wobble": "breathe"},
    "push_in": {"preset": "slow_push_in", "scale": [1.02, 1.09], "focus": [[0.50, 0.49], [0.50, 0.46]], "wobble": "none", "easing": "ease_out"},
    "push_in_breathe": {"preset": "slow_push_in", "scale": [1.02, 1.09], "focus": [[0.50, 0.48], [0.52, 0.46]], "wobble": "breathe", "easing": "ease_out"},
    "push_right_breathe": {"preset": "subtle_push_right", "scale": [1.02, 1.09], "focus": [[0.51, 0.48], [0.55, 0.46]], "wobble": "breathe", "easing": "ease_out"},
}

E: list[tuple[str, object]] = []


def scene(sid: str, img: str, m: str = "pan_right", beat_type: str = "normal", level: str = "A",
          intent: str = "", tr: str | None = None, trd: float = 0.4, shake: float | None = None,
          parallax: dict | None = None):
    # Only attach parallax if layer images exist; otherwise clean fallback during early pre-layer checks
    eff_px = parallax
    eff_lv = level
    if parallax:
        layers = parallax.get("layers") or []
        if not all(asset_exists(ly["image"]) for ly in layers):
            eff_px = None
            if level == "B":
                eff_lv = "A"
    E.append(("scene", dict(
        id=sid, image=img, motion=MOTION[m], beat_type=beat_type, level=eff_lv,
        intent=intent, tr=tr, trd=trd, shake=shake, parallax=eff_px,
    )))


def detail(fx_type: str, offset_start: float | None = None, offset_end: float | None = None,
           offset_at: float | None = None, dur: float | None = None, end_scene: bool = False, **kwargs):
    if fx_type == "detail_reveal" and "image" in kwargs and not asset_exists(kwargs["image"]):
        return
    E.append(("detail", dict(
        type=fx_type, offset_start=offset_start, offset_end=offset_end,
        offset_at=offset_at, dur=dur, end_scene=end_scene, kwargs=kwargs,
    )))


def attach_living_chars(scene_key: str, specs: list[dict]):
    """Attach pixel-locked eye_blink and mouth_sync from source/face_rois.json once baked."""
    cfg = FACE_ROIS.get(scene_key) or {}
    for sp in specs:
        char = sp["char"]
        c = cfg.get(char)
        if not c:
            continue
        if "blink" in c and asset_exists(c["blink"]["image"]):
            E.append(("blink", dict(
                image=c["blink"]["image"],
                region=c["blink"]["region"],
                first_offset=sp.get("first_offset", 1.7),
                interval=sp.get("interval", 4.1),
                feather=0.006,
                layer=sp.get("layer"),
                close_dur=0.055,
                hold_dur=0.045,
                open_dur=0.085,
            )))
        if sp.get("line_ids") and "mouth" in c:
            mc = c["mouth"]
            if all(asset_exists(mc[k]) for k in ("closed_image", "mid_image", "open_image")):
                E.append(("mouth", dict(
                    speaker=sp["speaker"],
                    line_ids=sp["line_ids"],
                    region=mc["region"],
                    default_state=mc.get("default_state", "closed"),
                    closed_image=mc["closed_image"],
                    mid_image=mc["mid_image"],
                    open_image=mc["open_image"],
                    feather=0.006,
                    layer=sp.get("layer"),
                    thresh_mid=0.14,
                    thresh_open=0.68,
                )))


def line(lid: str, spk: str, text: str, emo: str = "", sub: str | None = None, pause: float = 0.0):
    E.append(("line", dict(id=lid, spk=spk, text=text, emo=emo, sub=sub, pause=pause)))


def beat(sec: float):
    E.append(("beat", sec))


def chapter(kicker: str, title: str, offset: float = 0.2, dur: float = 4.4):
    E.append(("chapter", dict(kicker=kicker, title=title, offset=offset, dur=dur)))


def bubble(sender: str, text: str, side: str = "left", y: int = 240, stamp: str | None = None,
           dur: float = 4.6, offset: float = 0.0):
    E.append(("bubble", dict(sender=sender, text=text, side=side, y=y, stamp=stamp, dur=dur, offset=offset)))


def notif(title: str, text: str, y: int = 104, stamp: str = "", style: str = "neutral",
          dur: float = 5.0, offset: float = 0.0):
    E.append(("notif", dict(title=title, text=text, y=y, stamp=stamp, style=style, dur=dur, offset=offset)))


def sfx(preset: str, offset: float = 0.0, gain: float = -4.0, dur: float | None = None):
    E.append(("sfx", dict(preset=preset, offset=offset, gain=gain, dur=dur)))


def amb(preset: str, gain: float = -2.0):
    E.append(("amb", dict(preset=preset, gain=gain)))


def bgm(preset: str, gain: float = -3.0):
    E.append(("bgm", dict(preset=preset, gain=gain)))


def mark(name: str):
    E.append(("mark", name))


SILENT = -40.0

# ================================================================ STORY
# ---- HOOK · VĂN PHÒNG BAY TRÊN KHÔNG GIAN & VĂN PHÒNG TRỐNG TRƠN ----
amb("crowd", -3.0); bgm("action_climax", -2.5)
scene("s00_hook_space_stage", "assets/c00.jpg", "push_in", beat_type="climax", level="B",
      intent="2.5D parallax sân khấu LED xanh tím tách Thầy Quang & MC (Living-Char fg) trước văn phòng kính bay không gian",
      parallax={
          "camera": "push_in",
          "dolly": [1.02, 1.09],
          "shift_x": [0.0, 0.0],
          "shift_y": [0.0, -4.0],
          "focus": [0.54, 0.48],
          "strength": 0.90,
          "easing": "ease_out",
          "layers": [
              {"role": "bg", "image": "assets/s00_bg.jpg", "depth": 0.40, "blur": 0.5},
              {"role": "fg", "image": "assets/s00_fg.png", "depth": 1.28, "breathe_y": 1.8, "breathe_period": 3.4},
          ],
      })
sfx("riser", 0.05, -4.0, dur=0.9)
attach_living_chars("c00", [
    dict(char="quang", speaker="chu_no", line_ids=["l01_quang"], first_offset=1.6, interval=4.0, layer="fg"),
    dict(char="mc", speaker="ke_ban_hang", line_ids=["l02_mc"], first_offset=2.9, interval=4.3, layer="fg"),
])
detail("screen_glow", offset_start=0.20, end_scene=True, space="frame", pos=[0.46, 0.36], radius=[0.30, 0.24],
       color=[105, 195, 255], intensity=0.28, mode="pulse", fade=0.35)
bubble("SUẤT CUỐI HỘI NGHỊ AI", "300.000.000đ → 60.000.000đ (-80%) · 09:58",
       side="left", y=245, stamp="GIẢM SỐC 80%", dur=4.8, offset=0.25)
beat(0.45)
line("l01_quang", "QUANG",
     "Ba trăm triệu giảm tám mươi phần trăm còn sáu chục! Tặng ngay văn phòng ảo bay trên không gian với một trăm agent AI!",
     "vang dõng dạc đầy sức hút qua micro sân khấu, đẩy hưng phấn hội trường",
     sub="300 triệu giảm 80% còn 60 triệu! Tặng ngay văn phòng ảo bay trên không gian với 100 agent AI!")
line("l02_mc", "MC",
     "Nguyên công ty ảo đủ phòng bán hàng, chăm khách, kế toán vận hành tự động kiếm tiền cho bạn! Chỉ năm suất trong mười phút!",
     "hồ hởi bùng nổ trên sân khấu, đẩy nhịp gấp gáp mời gọi",
     sub="Nguyên công ty ảo đủ phòng bán hàng, chăm khách, kế toán tự động kiếm tiền cho bạn! Chỉ 5 suất trong 10 phút!",
     pause=0.15)

amb("room_tone", -2.5); bgm("tension_drone", SILENT)
scene("s01_hook_cut_empty", "assets/c01.jpg", "static_breathe", beat_type="aftermath", level="C",
      intent="Chớp trắng cắt rụp sang văn phòng thật trống trơn, giữ tĩnh lạnh với Living-Character Tuấn & ánh đỏ bảng khóa trên điện thoại",
      tr="flash_white", trd=0.20, shake=0.14)
mark("hook_empty")
sfx("impact", 0.0, -1.8)
sfx("low_accent", 0.25, -4.5)
attach_living_chars("c01", [
    dict(char="tuan", speaker="anh_hai", line_ids=["l03_tuan"], first_offset=1.3, interval=3.8),
])
detail("screen_glow", offset_start=0.20, end_scene=True, pos=[0.66, 0.62], radius=[0.18, 0.16],
       color=[255, 70, 75], intensity=0.30, mode="flicker", fade=0.25)
bubble("ĐÃ CHUYỂN: 240.000.000đ", "Văn phòng thật: Đã trả mặt bằng · Khóa cổng rút nạp 40tr",
       side="left", y=245, stamp="HAI THÁNG SAU", dur=4.8, offset=0.20)
beat(0.55)
line("l03_tuan", "TUAN",
     "Văn phòng trên màn hình vẫn bay, mấy phòng ban ảo vẫn sáng đèn báo lãi… mà hai trăm bốn chục triệu tiền thật bay đâu mất rồi?!",
     "sững sờ chua xót giữa sáng mưa, giọng run nhẹ không tin nổi",
     sub="Văn phòng trên màn hình vẫn bay, mấy phòng ban ảo vẫn báo lãi… mà 240 triệu tiền thật bay đâu mất rồi?!",
     pause=0.30)

# ---- HỒI 1 · CƠN BÃO FOMO AI & CHIẾC XE TRẮNG TRƯỚC SẢNH ----
amb("night_room", -3.2); bgm("investigative_story", -3.8)
scene("s02_shop_ai_fomo", "assets/c02.jpg", "pan_right_breathe", beat_type="establishing", level="C",
      intent="Pan ngang tiệm gia dụng chật hàng tồn + cuốn sổ giấy cũ & 2 ly trà đá + Living-Character đối thoại Tuấn và Hương",
      tr="fade_black", trd=0.45)
chapter("HỒI 1 · HAI THÁNG TRƯỚC", "CƠN BÃO FOMO AI")
sfx("chapter_sting", -0.1, -5.0)
attach_living_chars("c02", [
    dict(char="tuan", speaker="anh_hai", line_ids=["l05_tuan", "l07_tuan"], first_offset=1.8, interval=4.1),
    dict(char="huong", speaker="chi_hai", line_ids=["l04_huong", "l06_huong"], first_offset=3.0, interval=4.5),
])
beat(0.50)
line("l04_huong", "HUONG",
     "Tháng này bán chậm quá anh ơi. Trừ tiền mặt bằng với hàng tồn là gần như huề vốn.",
     "ngồi ghi sổ thu chi, giọng trầm lo âu thực tế")
line("l05_tuan", "TUAN",
     "Trên mạng AI sa thải hàng loạt kìa! Người ta dựng nguyên công ty ảo đủ bộ phận bán hàng tự động, mình cứ ghi sổ tay sao theo kịp?!",
     "lướt điện thoại sốt ruột, giọng đầy áp lực tụt hậu",
     sub="Trên mạng AI sa thải hàng loạt kìa! Người ta dựng nguyên công ty ảo đủ bộ phận bán hàng, mình ghi sổ tay sao theo kịp?!")
line("l06_huong", "HUONG",
     "Thiệt hả anh? Nghe cái gì mà nguyên công ty tự chạy nghe lạ quá… nhưng coi chừng mấy chỗ trên mạng thổi phồng đó anh.",
     "ngẩng lên nhìn chồng tò mò xen chút lo âu đời thường, giọng dịu nhẹ không gắt, không lên lớp")
line("l07_tuan", "TUAN",
     "Anh coi cho khỏi tụt hậu thôi, có đóng đồng nào đâu mà em lo.",
     "xua tay chống chế nhẹ, cố giữ vẻ bình thản", pause=0.18)

amb("night_room", -2.8); bgm("suspense_pulse", -3.8)
scene("s03_space_office_ad", "assets/c03.jpg", "push_in_breathe", beat_type="information", level="C",
      intent="Đẩy chậm ánh xanh tím màn hình quảng cáo văn phòng bay hắt lên mặt Tuấn đêm khuya + Living-Character Tuấn",
      tr="fade_black", trd=0.40)
sfx("click", 0.15, -4.0)
sfx("notification", 0.30, -4.5)
attach_living_chars("c03", [
    dict(char="tuan", speaker="anh_hai", line_ids=["l09_tuan"], first_offset=1.6, interval=4.0),
])
detail("screen_glow", offset_start=0.20, end_scene=True, pos=[0.58, 0.56], radius=[0.24, 0.22],
       color=[115, 195, 255], intensity=0.34, mode="turn_on", fade=0.30)
bubble("HỘI NGHỊ CÔNG TY MỘT NGƯỜI THỜI AI", "Vé nghe thử giữ chỗ: 299.000đ · Tối thứ Bảy",
       side="left", y=240, stamp="CƠN BÃO FOMO AI", dur=4.8, offset=0.20)
beat(0.45)
line("l08_quang_p", "QUANG_P",
     "Ba năm nữa chỉ còn hai loại người: người làm chủ dàn nhân sự AI tự kiếm tiền, và người bị thời đại bỏ lại phía sau!",
     "trầm mượt đầy sức thuyết phục phát qua loa điện thoại",
     sub="3 năm nữa chỉ còn 2 loại người: người làm chủ dàn nhân sự AI tự kiếm tiền, và người bị bỏ lại phía sau!")
line("l09_tuan", "TUAN",
     "Vé nghe thử hai trăm chín chín ngàn… không đi cập nhật sớm chắc mình lỗi thời thiệt luôn.",
     "thì thầm nửa lo nửa bị cuốn hút, mắt dán vào màn hình",
     sub="Vé nghe thử 299 ngàn… không đi cập nhật sớm chắc mình lỗi thời thiệt luôn.", pause=0.18)

amb("street", -4.5); bgm("investigative_story", -3.2)
scene("s04_hotel_white_car", "assets/c04.jpg", "push_in", beat_type="establishing", level="B",
      intent="2.5D parallax trước sảnh khách sạn lớn tách Tuấn tiền cảnh (Living-Char fg) khỏi chiếc siêu xe trắng bóng loáng và Thầy Quang",
      tr="fade_black", trd=0.40,
      parallax={
          "camera": "push_in",
          "dolly": [1.02, 1.08],
          "shift_x": [0.0, 0.0],
          "shift_y": [0.0, -3.0],
          "focus": [0.54, 0.48],
          "strength": 0.88,
          "easing": "ease_out",
          "layers": [
              {"role": "bg", "image": "assets/s04_bg.jpg", "depth": 0.42, "blur": 0.6},
              {"role": "fg", "image": "assets/s04_fg.png", "depth": 1.26, "breathe_y": 1.6, "breathe_period": 3.8},
          ],
      })
sfx("low_accent", 0.20, -4.5)
attach_living_chars("c04", [
    dict(char="tuan", speaker="anh_hai", line_ids=["l10_tuan"], first_offset=1.4, interval=3.8, layer="fg"),
])
beat(0.45)
line("l10_tuan", "TUAN",
     "Diễn giả chạy siêu xe, mở hội nghị ngay khách sạn lớn… tầm cỡ này chắc chắn làm ăn thứ thiệt.",
     "trầm trồ thán phục trước vẻ hào nhoáng sang trọng", pause=0.20)

# ---- HỒI 2 · HỘI TRƯỜNG CÔNG NGHỆ: TẶNG VĂN PHÒNG BAY & NGƯỜI ĐẦU TIÊN GIƠ TAY ----
amb("crowd", -4.8); bgm("investigative_story", -3.8)
scene("s05_hall_lan_fomo", "assets/c05.jpg", "pan_left_breathe", beat_type="normal", level="C",
      intent="Pan trái nhẹ giữa hội trường xanh tím + Living-Character đối thoại đồng cảm giữa Chị Lan và Tuấn",
      tr="fade_black", trd=0.45)
chapter("HỒI 2 · HỘI TRƯỜNG CÔNG NGHỆ", "SUẤT CUỐI GIẢM 80%")
sfx("chapter_sting", -0.1, -5.0)
attach_living_chars("c05", [
    dict(char="lan", speaker="co_hanh", line_ids=["l11_lan"], first_offset=1.5, interval=4.0),
    dict(char="tuan", speaker="anh_hai", line_ids=["l12_tuan"], first_offset=2.8, interval=4.3),
])
beat(0.45)
line("l11_lan", "LAN",
     "Chú cũng sợ bị AI bỏ lại hả? Chị bán sạp vải ngoài chợ, mù công nghệ mà nghe mở công ty tự động hoài nên ráng đi.",
     "quay sang bắt chuyện mộc mạc chân chất, cực kỳ dễ tạo đồng cảm")
line("l12_tuan", "TUAN",
     "Dạ y chang em luôn chị. Nghe thầy chiếu mô hình công ty một người nãy giờ mở mang thiệt.",
     "gật đầu cởi mở, hoàn toàn mất cảnh giác", pause=0.18)

amb("crowd", -3.0); bgm("suspense_pulse", -2.5)
scene("s06_countdown_space_office", "assets/c06.jpg", "push_in", beat_type="climax", level="B",
      intent="2.5D parallax bùng nổ đèn sân khấu tách Chị Lan bật phắt dậy (Living-Char fg) khỏi màn LED văn phòng bay giảm 80%",
      tr="dissolve", trd=0.30,
      parallax={
          "camera": "push_in",
          "dolly": [1.02, 1.09],
          "shift_x": [0.0, 0.0],
          "shift_y": [0.0, -4.0],
          "focus": [0.54, 0.46],
          "strength": 0.90,
          "easing": "ease_out",
          "layers": [
              {"role": "bg", "image": "assets/s06_bg.jpg", "depth": 0.42, "blur": 0.5},
              {"role": "fg", "image": "assets/s06_fg.png", "depth": 1.28, "breathe_y": 1.8, "breathe_period": 2.8},
          ],
      })
mark("countdown_stage")
sfx("riser", 0.05, -4.0, dur=0.95)
sfx("light_switch", 0.20, -4.0)
attach_living_chars("c06", [
    dict(char="lan", speaker="co_hanh", line_ids=["l14_lan"], first_offset=1.8, interval=4.0, layer="fg"),
])
detail("light_shift", offset_at=0.20, dur=0.18, end=1.10, end_dur=0.35,
       brightness=1.14, tint_rgb=[165, 210, 255], tint_strength=0.12)
bubble("GIẢM 80% TRONG 10 PHÚT", "300.000.000đ → 60.000.000đ · Chỉ còn 4 suất!",
       side="left", y=240, stamp="ĐẾM NGƯỢC 10:00", dur=5.2, offset=0.20)
beat(0.45)
line("l13_quang", "QUANG",
     "Cọc mười triệu trong mười phút giữ suất sáu chục! Tặng văn phòng không gian đủ phòng kinh doanh, tiếp thị, kế toán — gắn tên bạn làm giám đốc!",
     "bùng nổ đầy uy lực trên sân khấu, tạo cơn sốt chốt suất",
     sub="Cọc 10 triệu giữ suất 60 triệu! Tặng văn phòng không gian đủ phòng kinh doanh, tiếp thị, kế toán — gắn tên bạn làm giám đốc!")
line("l14_lan", "LAN",
     "Thầy ơi cho em chốt suất đầu tiên! Không rành máy tính mà có nguyên dàn nhân sự ảo làm giùm hết thế này em không bỏ lỡ đâu!",
     "bật dậy háo hức kêu to đầy thuyết phục giữa hội trường",
     sub="Thầy ơi cho em chốt suất đầu tiên! Có nguyên dàn nhân sự ảo làm giùm thế này em không bỏ lỡ đâu!")
line("l15_mc", "MC",
     "Suất giám đốc số một đã có chủ! Chỉ còn bốn suất giảm tám mươi phần trăm! Chậm tay là đứng ngoài kỷ nguyên AI!",
     "hô vang dồn dập đầy kích thích ép nhịp đếm ngược",
     sub="Suất giám đốc số 1 đã có chủ! Chỉ còn 4 suất giảm 80%! Chậm tay là đứng ngoài kỷ nguyên AI!",
     pause=0.18)

amb("crowd", -3.8); bgm("suspense_pulse", -2.2)
scene("s07_tuan_swipes_deposit", "assets/c07.jpg", "push_right_breathe", beat_type="suspicion", level="C",
      intent="Đẩy cận mặt Tuấn rịn mồ hôi dưới ánh LED xanh tím + Living-Character Tuấn nắm thẻ bật dậy chốt cọc",
      tr="dissolve", trd=0.25)
sfx("heartbeat", 0.10, -4.0, dur=2.2)
sfx("click", 0.35, -3.5)
sfx("bank_ting", 0.50, -2.5)
attach_living_chars("c07", [
    dict(char="tuan", speaker="anh_hai", line_ids=["l16_tuan"], first_offset=1.4, interval=3.5),
])
detail("screen_glow", offset_start=0.20, end_scene=True, pos=[0.66, 0.45], radius=[0.26, 0.24],
       color=[110, 180, 255], intensity=0.28, mode="pulse", fade=0.30)
bubble("CỌC GIỮ SUẤT VIP", "-10.000.000đ · Hôm sau chuyển đủ 50tr · Tổng: 60.000.000đ",
       side="left", y=240, stamp="ĐÃ LÊN TÀU", dur=4.8, offset=0.25)
beat(0.45)
line("l16_tuan", "TUAN",
     "Ba trăm triệu còn sáu chục lại có sẵn công ty đủ bộ phận tự chạy… chị bán vải còn dám chốt, mình chậm là tụt hậu!",
     "gấp gáp quyết liệt, tự thuyết phục mình lao theo đám đông",
     sub="300 triệu còn 60 triệu lại có sẵn công ty đủ bộ phận tự chạy… chị bán vải còn chốt, mình chậm là tụt hậu!",
     pause=0.22)

# ---- HỒI 3 · CƠN SAY "GIÁM ĐỐC TUẤN" GIỮA KHÔNG GIAN & CÚ MỒI 3 TRIỆU ----
amb("office", -4.0); bgm("investigative_story", -3.2)
scene("s08_floating_office_debut", "assets/c08.jpg", "pan_right", beat_type="information", level="B",
      intent="Cảnh 2.5D drift_push đắt giá nhất tập: tách văn phòng ảo bay lơ lửng trên bàn VIP khỏi bộ ba Living-Char Quang, Khánh và Tuấn (layer bg)",
      tr="fade_black", trd=0.45,
      parallax={
          "camera": "drift_push",
          "dolly": [1.03, 1.09],
          "shift_x": [-8.0, 8.0],
          "shift_y": [3.0, -4.0],
          "focus": [0.52, 0.48],
          "strength": 0.90,
          "easing": "smoothstep",
          "layers": [
              {"role": "bg", "image": "assets/s08_bg.jpg", "depth": 0.42, "blur": 0.6},
              {"role": "fg", "image": "assets/s08_fg.png", "depth": 1.30, "breathe_y": 2.2, "breathe_scale": 0.005, "breathe_period": 3.6},
          ],
      })
chapter("HỒI 3 · HAI TUẦN SAU", "GIÁM ĐỐC 100 AGENT")
mark("floating_office")
sfx("chapter_sting", -0.1, -5.0)
sfx("click", 0.45, -4.0)
sfx("notification", 4.65, -3.5)
attach_living_chars("c08", [
    dict(char="quang", speaker="chu_no", line_ids=["l18_quang"], first_offset=1.9, interval=4.3, layer="bg"),
    dict(char="khanh", speaker="ke_ngot_ngao_nam", line_ids=["l19_khanh"], first_offset=2.9, interval=4.5, layer="bg"),
    dict(char="tuan", speaker="anh_hai", line_ids=["l17_tuan"], first_offset=1.3, interval=3.9, layer="bg"),
])
detail("screen_glow", offset_start=0.25, end_scene=True, space="frame", pos=[0.54, 0.56], radius=[0.28, 0.24],
       color=[95, 225, 255], intensity=0.30, mode="pulse", fade=0.35)
notif("VĂN PHÒNG KHÔNG GIAN · SẾP TUẤN", "Đủ phòng kinh doanh, tiếp thị, kế toán · Báo lãi từng giây!",
      y=104, stamp="ẢO GIÁC LÀM SẾP", style="safe", dur=5.4, offset=4.65)
beat(0.50)
line("l17_tuan", "TUAN",
     "Trời ơi… văn phòng bay giữa không gian, từ phòng kinh doanh tới kế toán sáng đèn hết, gọi đúng tên mình là giám đốc luôn nè!",
     "mắt sáng rực lâng lâng tự hào như vừa lên chức thật sự")
line("l18_quang", "QUANG",
     "Đây mới là bản chạy thử. Muốn hệ thống nối khách thật đổ lãi về ngân hàng, em phải nạp gói máy chủ kích hoạt.",
     "điềm đạm mượt mà như chuyện nghiệp vụ hiển nhiên")
line("l19_khanh", "KHANH",
     "Anh kích hoạt gói thử hai chục triệu trước. Tụi nó chốt đơn tới đâu, sếp Tuấn thu tiền tới đó mỗi ngày!",
     "nhanh nhẹn ngọt ngào nâng tầm gọi sếp Tuấn cực kỳ khéo léo",
     sub="Anh kích hoạt gói thử 20 triệu trước. Tụi nó chốt đơn tới đâu, sếp Tuấn thu tiền tới đó mỗi ngày!",
     pause=0.20)

amb("room_tone", -3.2); bgm("investigative_story", -3.8)
scene("s09_boss_in_small_shop", "assets/c09.jpg", "pull_out_breathe", beat_type="information", level="C",
      intent="Lùi chậm bữa cơm ấm trong tiệm gia dụng chật chội cạnh 2 ly trà đá & tablet văn phòng bay + Living-Character Tuấn (lúng túng) và Hương",
      tr="fade_black", trd=0.40)
mark("bait_profit")
sfx("bank_ting", 0.18, -2.5)
sfx("low_accent", 0.45, -4.5)
attach_living_chars("c09", [
    dict(char="tuan", speaker="anh_hai", line_ids=["l21_tuan", "l22b_tuan"], first_offset=1.8, interval=4.1),
    dict(char="huong", speaker="chi_hai", line_ids=["l22_huong"], first_offset=3.1, interval=4.4),
])
detail("screen_glow", offset_start=0.20, end_scene=True, pos=[0.46, 0.66], radius=[0.20, 0.16],
       color=[100, 225, 255], intensity=0.28, mode="turn_on", fade=0.30)
bubble("BIẾN ĐỘNG SỐ DƯ", "+3.000.000đ · Rút thành công",
       side="left", y=102, stamp="LÃI MỒI THẬT", dur=4.8, offset=0.18)
beat(0.50)
line("l20_lan_p", "LAN_P",
     "Cảm ơn thầy Quang nhiều lắm! Em nâng máy chủ lớn hôm qua, dàn nhân sự chạy suốt đêm, lãi về gấp đôi tiền học rồi!",
     "hồ hởi phấn khởi qua tin nhắn thoại nhóm VIP")
line("l21_tuan", "TUAN",
     "Em coi nè! Nguyên văn phòng ảo gọi anh bằng sếp, mấy phòng ban chốt đơn báo lãi liên tục — rút được ba triệu thật luôn!",
     "hớn hở khoe vợ đầy tự hào",
     sub="Em coi nè! Nguyên văn phòng ảo gọi anh bằng sếp, báo lãi liên tục — rút được 3 triệu thật luôn!")
line("l22_huong", "HUONG",
     "Nguyên công ty ảo sáng đèn bay ngoài không gian… nhưng tụi nó bán món hàng gì, bán cho ai mà tiền tự chảy về túi anh?",
     "đặt đũa xuống nhìn thẳng chồng, giọng gọn lạnh đặt câu hỏi chí mạng",
     pause=0.35)
line("l22b_tuan", "TUAN",
     "Thì… thầy nói tụi nó chạy thuật toán kết nối sàn quốc tế gì đó… công nghệ cao lắm anh cũng không rành, miễn tiền về thật là được!",
     "ngập ngừng lúng túng rõ rệt, gãi đầu đánh trống lảng, giọng hơi lí nhí chống chế vì thật ra chính mình cũng không hiểu",
     pause=0.22)

amb("night_room", -2.5); bgm("tension_drone", -2.8)
scene("s10_fomo_server_all_in", "assets/c10.jpg", "push_in_breathe", beat_type="suspicion", level="C",
      intent="Đẩy căng nửa đêm tiệm tối khi Tuấn cắn môi tất tay 160 triệu dưới ánh xanh vàng văn phòng bay + Living-Character Tuấn",
      tr="fade_black", trd=0.40)
sfx("notification", 0.18, -3.5)
sfx("bank_ting", 0.45, -2.5)
attach_living_chars("c10", [
    dict(char="tuan", speaker="anh_hai", line_ids=["l24_tuan"], first_offset=1.5, interval=3.8),
])
detail("screen_glow", offset_start=0.20, end_scene=True, pos=[0.54, 0.64], radius=[0.24, 0.20],
       color=[255, 205, 110], intensity=0.30, mode="turn_on", fade=0.30)
bubble("TRẠM MÁY CHỦ LỚN", "-160.000.000đ · Tổng đã chuyển: 240.000.000đ",
       side="left", y=240, stamp="TẤT TAY", dur=4.8, offset=0.20)
beat(0.45)
line("l23_quang_p", "QUANG_P",
     "Sếp Tuấn có tố chất dẫn đầu. Chỉ còn đúng ba suất trạm máy chủ một trăm sáu mươi triệu trước khi khóa cổng.",
     "mượt mà tâng bốc xen áp lực khan hiếm qua tin nhắn thoại riêng",
     sub="Sếp Tuấn có tố chất dẫn đầu. Chỉ còn đúng 3 suất trạm máy chủ 160 triệu trước khi khóa cổng.")
line("l24_tuan", "TUAN",
     "Rút ba triệu thật rồi, mấy phòng ban trên kia vẫn chốt lãi ầm ầm… xoay gói lớn một đợt là đổi đời luôn!",
     "cắn môi háo hức pha căng thẳng tự thuyết phục mình tất tay",
     sub="Rút 3 triệu thật rồi, mấy phòng ban trên kia vẫn chốt lãi ầm ầm… xoay gói lớn một đợt là đổi đời luôn!",
     pause=0.25)

# ---- HỒI 4 · SỤP ĐỔ: NÔ LỆ HÓA, PHẢN PHÁO NGOẠI TUYẾN & ĐÒN BÓC 0 KB KHÔNG THỂ CHỐI CÃI ----
amb("room_tone", -2.5); bgm("tension_drone", -2.4)
scene("s11_frozen_agents_still_looping", "assets/c11.jpg", "pan_right_breathe", beat_type="anomaly", level="C",
      intent="Bật detail_reveal bảng đỏ khóa cổng 40 triệu + light_shift đỏ + Living-Character Tuấn vét sạch tiền van nài thương lượng trừ cấn",
      tr="fade_black", trd=0.40, shake=0.32)
chapter("HỒI 4 · HAI TUẦN SAU", "TẮT MẠNG VẪN CHẠY")
mark("gate_locked")
sfx("chapter_sting", -0.1, -5.0)
sfx("glitch", 0.25, -2.8, dur=0.45)
sfx("impact", 0.30, -2.5)
# Đặt detail_reveal TRƯỚC attach_living_chars để mắt & miệng Tuấn vẽ ĐÈ LÊN trên c11_reveal.jpg
detail("detail_reveal", offset_at=0.28, dur=0.32, image="assets/c11_reveal.jpg")
attach_living_chars("c11", [
    dict(char="tuan", speaker="anh_hai", line_ids=["l25_tuan", "l26b_tuan"], first_offset=1.6, interval=3.9),
])
detail("light_shift", offset_at=0.30, dur=0.14, end=1.10, end_dur=0.35,
       brightness=0.92, tint_rgb=[255, 75, 80], tint_strength=0.14)
bubble("CẢNH BÁO HỆ THỐNG", "Kẹt đối soát · Nạp 40.000.000đ mở cổng rút trước 12:00",
       side="left", y=240, stamp="KHÓA CỔNG RÚT", dur=5.0, offset=0.28)
beat(0.55)
line("l25_tuan", "TUAN",
     "Alo Khánh ơi! Trên màn hình vẫn báo chốt đơn ầm ầm mà sao anh bấm rút bị khóa, gọi thầy Quang cũng tắt máy rồi?!",
     "hoảng hốt gấp gáp, giọng lạc đi lo lắng")
line("l26_khanh_p", "KHANH_P",
     "Trạm máy chủ anh đang kẹt đối soát. Nạp thêm bốn chục triệu mở cổng trước trưa nay, không là hệ thống đóng băng hết.",
     "lạnh đều vô cảm dứt khoát qua điện thoại, mất sạch vẻ lịch sự ban đầu",
     sub="Trạm máy chủ đang kẹt đối soát. Nạp thêm 40 triệu mở cổng trước trưa nay, không là đóng băng hết.")
line("l26b_tuan", "TUAN",
     "Khánh ơi, nhà anh vét sạch hai trăm bốn chục triệu rồi, không còn đồng nào! Cho anh gặp thầy xin trừ đỡ bốn chục vô tiền lãi đi!",
     "giọng run hẳn xuống nước năn nỉ van vỉ, tuyệt vọng hoàn toàn vì nhà đã vét sạch không còn một đồng",
     sub="Khánh ơi, nhà anh vét sạch 240 triệu rồi, không còn đồng nào! Cho anh gặp thầy xin trừ đỡ 40 triệu vô tiền lãi đi!")
line("l26c_khanh_p", "KHANH_P",
     "Quy định hệ thống không trừ cấn. Kiếm đủ bốn chục trước trưa thì mở, không thì mất trắng!",
     "lạnh ngắt cắt ngang, trịch thượng vô cảm hoàn toàn khác hẳn lúc gọi sếp",
     sub="Quy định không trừ cấn. Kiếm đủ 40 triệu trước trưa thì mở, không thì mất trắng!",
     pause=0.10)
sfx("call_end", 0.0, -3.0, dur=1.2)
beat(0.75)

amb("rain", -4.0); bgm("tension_drone", -3.0)
scene("s12_empty_office_guard", "assets/c12.jpg", "pull_out_breathe", beat_type="aftermath", level="C",
      intent="Lùi chậm dưới mưa phùn trước sảnh tòa nhà + Living-Character Tuấn (tìm thầy thương lượng, chạm đáy nô lệ hóa) và Chú Bảo Vệ",
      tr="fade_black", trd=0.40)
sfx("footsteps", 0.15, -5.0, dur=0.9)
attach_living_chars("c12", [
    dict(char="guard", speaker="ong_bay", line_ids=["l28_guard"], first_offset=2.4, interval=4.5),
    dict(char="tuan", speaker="anh_hai", line_ids=["l27_tuan", "l28b_tuan"], first_offset=1.4, interval=3.8),
])
beat(0.45)
line("l27_tuan", "TUAN",
     "Chú ơi, học viện thầy Quang tầng năm đâu rồi chú? Cháu hết tiền rồi, chạy tới xin thầy trừ đỡ… chiếc xe trắng cũng không thấy nữa?",
     "thở gấp hốt hoảng dưới mưa, giọng cầu khẩn bám víu hy vọng cuối cùng đi tìm thầy thương lượng")
line("l28_guard", "GUARD",
     "Đoàn đó chỉ thuê hội trường với phòng họp theo ngày thôi chú ơi. Chiếc xe trắng cũng là xe thuê đậu chụp hình bốn tiếng!",
     "chậm rãi thẳng thắn, chút ái ngại cho người trẻ bị gạt",
     sub="Đoàn đó chỉ thuê hội trường với phòng họp theo ngày thôi chú ơi. Chiếc xe trắng cũng thuê chụp hình 4 tiếng!",
     pause=0.18)
sfx("low_accent", 0.0, -3.8)
line("l28b_tuan", "TUAN",
     "Bỏ hai trăm bốn chục triệu mơ làm giám đốc… hóa ra biến thành kẻ quỵ lụy đi năn nỉ xin lại chính tiền của mình!",
     "sững sờ chua chát nghẹn đắng, mắt trân trối nhận ra sự bẽ bàng của ảo giác làm sếp",
     sub="Bỏ 240 triệu mơ làm giám đốc… hóa ra biến thành kẻ quỵ lụy đi năn nỉ xin lại chính tiền của mình!",
     pause=0.25)

amb("night_room", -3.0); bgm("action_climax", -3.2)
scene("s13_offline_clip_and_group_expose", "assets/c13.jpg", "pan_left_breathe", beat_type="anomaly", level="C",
      intent="Hiệp 1 lột tẩy: Hương bật Chế độ Máy bay (detail_reveal) thả clip nhóm VIP — lập tức bị quản trị viên phản pháo bằng chiêu 'tính năng ngoại tuyến'",
      tr="fade_black", trd=0.40)
mark("airplane_expose")
sfx("click", 0.25, -2.5)
sfx("low_accent", 0.40, -3.5)
# Đặt detail_reveal TRƯỚC attach_living_chars để cả Tuấn & Hương chớp mắt/nhép miệng ĐÈ LÊN c13_reveal.jpg
detail("detail_reveal", offset_at=0.28, dur=0.35, image="assets/c13_reveal.jpg")
attach_living_chars("c13", [
    dict(char="tuan", speaker="anh_hai", line_ids=["l29_tuan"], first_offset=1.6, interval=4.0),
    dict(char="huong", speaker="chi_hai", line_ids=["l30_huong"], first_offset=2.8, interval=4.3),
])
detail("screen_glow", offset_start=0.30, end_scene=True, pos=[0.50, 0.72], radius=[0.24, 0.16],
       color=[95, 225, 255], intensity=0.28, mode="pulse", fade=0.30)
notif("CHẾ ĐỘ MÁY BAY: ĐÃ NGẮT MẠNG", "Văn phòng ảo vẫn chạy báo lãi y chang!",
      y=98, stamp="HOẠT ẢNH VẼ SẴN", style="danger", dur=5.2, offset=0.28)
beat(0.55)
line("l29_tuan", "TUAN",
     "Tắt mạng rồi mà văn phòng bay với mấy bảng lãi vẫn nhảy y chang… Hóa ra chỉ là đoạn hoạt ảnh vẽ sẵn!",
     "sững sờ bàng hoàng nhận ra sự thật phũ phàng")
sfx("message_send", 0.05, -2.5)
line("l30_huong", "HUONG",
     "Em quay lại rồi! Quăng thẳng vô nhóm kín cho mấy trăm người kia coi mà dừng nạp tiền liền!",
     "dứt khoát nhanh gọn đầy bản lĩnh khi gửi clip cứu nhóm học viên", pause=0.10)
sfx("notification", 0.05, -2.6)
notif("QUẢN TRỊ VIÊN NHÓM VIP", "Đó là chế độ ngoại tuyến không gián đoạn! Đừng nghe phá đám!",
      y=98, stamp="PHẢN PHÁO", style="neutral", dur=6.0, offset=0.05)
line("l30b_khanh_p", "KHANH_P",
     "Mọi người bình tĩnh! Đó là tính năng chạy ngoại tuyến không gián đoạn, lát có mạng tự đồng bộ đơn thật — đừng nghe kẻ phá đám!",
     "gấp gáp sắc giọng trấn an đám đông qua tin nhắn thoại trong nhóm VIP, ngụy biện đầy tự tin",
     sub="Mọi người bình tĩnh! Đó là tính năng chạy ngoại tuyến không gián đoạn, có mạng tự đồng bộ đơn — đừng nghe phá đám!",
     pause=0.18)

amb("night_room", -2.8); bgm("action_climax", -2.5)
scene("s13b_undeniable_killshot", "assets/c13b.jpg", "push_in_breathe", beat_type="climax", level="C",
      intent="Hiệp 2 không thể chối cãi: Hương soi cài đặt dữ liệu mạng 0 KB cả tháng + chỉnh ngày về năm 2000 vẫn báo đơn mới → vỡ trận nhóm VIP + Living-Char đôi",
      tr="dissolve", trd=0.25)
sfx("click", 0.18, -2.4)
sfx("impact", 0.28, -3.2)
attach_living_chars("c13b", [
    dict(char="tuan", speaker="anh_hai", line_ids=["l31_tuan"], first_offset=1.8, interval=4.1),
    dict(char="huong", speaker="chi_hai", line_ids=["l30c_huong", "l32_huong"], first_offset=1.3, interval=4.0),
])
detail("screen_glow", offset_start=0.20, end_scene=True, pos=[0.50, 0.72], radius=[0.26, 0.18],
       color=[255, 85, 95], intensity=0.26, mode="pulse", fade=0.28)
notif("CÀI ĐẶT MẠNG · DỮ LIỆU APP: 0 KB", "Cả tháng chưa gửi dữ liệu · Chỉnh năm 2000 vẫn báo đơn mới!",
      y=98, stamp="KHÔNG THỂ CHỐI CÃI", style="danger", dur=6.0, offset=0.22)
beat(0.45)
line("l30c_huong", "HUONG",
     "Ngoại tuyến hả? Coi cài đặt mạng cả tháng của app: bằng không! Chỉnh ngày về năm hai ngàn vẫn nhảy đơn mới tinh kìa!",
     "sắc bén dứt khoát đầy uy lực khi quay clip bằng chứng thứ hai đập tan lời ngụy biện",
     sub="Ngoại tuyến hả? Coi dữ liệu mạng cả tháng của app: 0 KB! Chỉnh ngày về năm 2000 vẫn nhảy đơn mới tinh kìa!")
sfx("message_send", 0.05, -2.5)
sfx("notification", 0.35, -2.8)
notif("NHÓM KÍN VIP (300 NGƯỜI)", "0 KB cả tháng?! Năm 2000 vẫn chốt đơn?! Dừng chuyển tiền ngay!",
      y=98, stamp="VỠ TRẬN NHÓM VIP", style="danger", dur=5.6, offset=0.35)
beat(0.35)
line("l31_tuan", "TUAN",
     "Anh sai rồi Hương ơi… sáu chục tiền học, trăm tám gói máy chủ. Chuyển đi sạch hai trăm bốn chục triệu rồi.",
     "giọng trầm nghẹn đầy ân hận, thú nhận hết với vợ",
     sub="Anh sai rồi Hương ơi… 60 triệu tiền học, 180 triệu máy chủ. Chuyển đi sạch 240 triệu rồi.")
line("l32_huong", "HUONG",
     "Ngưng liền! Đừng nạp mở cổng, đừng tin tin nhắn lấy lại tiền giùm! Gom sao kê, biên nhận lên công an trình báo ngay!",
     "mạnh mẽ chặn tay chồng, dứt khoát từng ý xử lý đúng đắn", pause=0.25)

# ---- HỒI 5 · LÀM LẠI TỪ VIỆC THẬT & THẺ NHỚ KỸ (< 8 GIÂY) ----
amb("street", -5.5); bgm("warm_outro", -4.2)
scene("s14_next_morning_shop", "assets/c14.jpg", "pan_right_breathe", beat_type="aftermath", level="C",
      intent="Pan ngang nắng sáng tiệm gia dụng: cất văn phòng ảo, hai vợ chồng quay clip bán hàng thật bên cuốn sổ giấy cũ + Living-Character",
      tr="fade_black", trd=0.45)
chapter("HỒI 5 · SÁNG HÔM SAU", "LÀM LẠI TỪ VIỆC THẬT")
sfx("chapter_sting", -0.1, -5.0)
detail("light_shift", offset_at=0.20, dur=0.50, brightness=1.06, tint_rgb=[255, 232, 185], tint_strength=0.07)
attach_living_chars("c14", [
    dict(char="tuan", speaker="anh_hai", line_ids=["l33_tuan"], first_offset=1.7, interval=4.1),
    dict(char="huong", speaker="chi_hai", line_ids=[], first_offset=2.9, interval=4.4),
])
beat(0.50)
line("l33_tuan", "TUAN",
     "Bữa nay anh mới tỉnh… ngồi làm giám đốc cái công ty ảo đó, cuối cùng người giàu nhất vẫn là người đứng trên sân khấu.",
     "nhẹ nhõm trầm lắng chiêm nghiệm sau bài học đắt giá",
     sub="Bữa nay anh mới tỉnh… ngồi làm giám đốc công ty ảo đó, cuối cùng giàu nhất vẫn là người trên sân khấu.",
     pause=0.25)

# ---- THẺ NHỚ KỸ (< 8 GIÂY) ----
amb("room_tone", -5.0); bgm("warm_outro", -4.2)
scene("s15_red_flags", "assets/c15.jpg", "static_hold", beat_type="ending", level="A",
      intent="Khung tĩnh sạch trên nền tiệm gia dụng ấm dịu cho bảng NHỚ KỸ và đúng 1 câu của Người Bóc Trần (< 8s)",
      tr="fade_black", trd=0.40)
mark("rf_start")
sfx("bank_ting", 0.0, -5.0)
line("l34_narr", "N",
     "Giảm sốc tặng công ty ảo một trăm agent tự kiếm tiền chỉ là hoạt ảnh mồi. Kiểm chứng trước khi xuống tiền!",
     sub="Giảm sốc tặng công ty ảo 100 agent tự kiếm tiền chỉ là hoạt ảnh mồi. Kiểm chứng trước khi xuống tiền!")
beat(0.50)
mark("rf_end")

# ---- KẾT MỞ SAU THẺ NHỚ KỸ · VŨ TRỤ CHỊ HAI (EP04 ↔ EP06 ↔ EP08b ↔ EP10) ----
amb("rain", -3.0); bgm("tension_drone", -2.2)
scene("s16a_coda_quang_report", "assets/c16a.jpg", "push_in_breathe", beat_type="suspicion", level="C",
      intent="Đêm mưa xám lạnh trong khoang xe: đẩy chậm cận Thầy Quang căng thẳng báo cáo sự cố & lột tay IT EP06 + Living-Character Quang",
      tr="fade_black", trd=0.40)
mark("coda_start")
sfx("phone_vibrate", 0.10, -4.5, dur=0.5)
sfx("heartbeat", 0.25, -4.8, dur=2.0)
attach_living_chars("c16a", [
    dict(char="quang", speaker="chu_no", line_ids=["l35_quang_p", "l36_quang_p"], first_offset=1.5, interval=3.8),
])
detail("screen_glow", offset_start=0.20, end_scene=True, pos=[0.28, 0.72], radius=[0.20, 0.16],
       color=[95, 210, 255], intensity=0.28, mode="pulse", fade=0.30)
bubble("CLIP LAN TRONG NHÓM VIP", "Tắt mạng · Lưu lượng 0 KB · Chỉnh năm 2000 vẫn báo đơn",
       side="left", y=125, stamp="LỘ TẨY TOÀN BỘ", dur=5.0, offset=0.20)
beat(0.45)
line("l35_quang_p", "QUANG_P",
     "Chị Hai… hỏng hết rồi! Khách quay clip tắt mạng, soi dữ liệu mạng bằng không quăng vô nhóm, học viên làm loạn đòi rút tiền sạch!",
     "mất sạch vẻ tự tin, giọng run căng thẳng hớt hải báo cáo cấp trên qua điện thoại",
     sub="Chị Hai… hỏng hết rồi! Khách quay clip tắt mạng, soi 0 KB quăng vô nhóm, học viên đòi rút tiền sạch!")
line("l36_quang_p", "QUANG_P",
     "Tay viết app đợt Bạn Thân bốn chấm không làm ẩu rồi! Nhận tiền dựng máy chủ mà nhét mỗi đoạn hoạt ảnh chạy chay!",
     "tức tối xen lo sợ bị quy trách nhiệm, nói gấp báo nguồn gốc mã nguồn",
     sub="Tay viết app đợt Bạn Thân 4.0 làm ẩu rồi! Nhận tiền dựng máy chủ mà nhét mỗi đoạn hoạt ảnh chạy chay!",
     pause=0.20)

scene("s16b_coda_chihai_order", "assets/c16b.jpg", "static_hold", beat_type="climax", level="C",
      intent="Giữ tĩnh lạnh góc sau vai Chị Hai (tóc bob đen & áo lụa xanh ngọc lục bảo, 100% đồng bộ EP04/EP08b) + detail_reveal tắt phụt màn hình hồ sơ EP06",
      tr="dissolve", trd=0.25)
sfx("heartbeat", 0.05, -4.5, dur=1.4)
detail("screen_glow", offset_start=0.05, end_at_mark="chihai_screen_off", pos=[0.30, 0.72], radius=[0.22, 0.18],
       color=[95, 210, 235], intensity=0.22, mode="pulse", fade=0.25)
bubble("HỒ SƠ KỸ THUẬT · NHÁNH BẠN THÂN 4.0", "Cảnh báo 1: Tha #410 · Cảnh báo 2: Qua mặt tổ chức",
       side="left", y=125, stamp="XỬ LÝ NỘI BỘ", dur=5.2, offset=0.18)
beat(0.45)
line("l37_chihai", "CHIHAI",
     "Đợt trước mềm lòng tha bạn cũ đã suýt lộ. Giờ còn dám qua mặt tôi.",
     "lạnh băng, trầm tĩnh chậm chắc, không chút cảm xúc", pause=0.22)
line("l38_chihai", "CHIHAI",
     "Đóng app. Rút hết đoàn. Còn tay đó… làm đi.",
     "giữ nguyên giọng phụ nữ sắc lạnh thanh gọn y hệt câu trước, ngắt gọn ba nhịp không cảm xúc, tuyệt đối giữ giọng nữ", pause=0.08)
mark("chihai_screen_off")
sfx("click", 0.0, -2.0)
detail("detail_reveal", offset_at=0.0, dur=0.14, image="assets/c16b_off.jpg")
detail("light_shift", offset_at=0.0, dur=0.16, brightness=0.70, tint_rgb=[30, 50, 75], tint_strength=0.18)
beat(0.55)

sfx("impact", 0.0, -1.2)
scene("s17_black_cut", "assets/c17.jpg", "static_hold", beat_type="ending", level="A",
      intent="Cú cắt đen đột ngột giữ dư âm lạnh sau lệnh loại thẳng và tiếng tắt màn hình",
      tr="fade_black", trd=0.08)
beat(1.20)

# ---- DISCLAIMER ----
amb("room_tone", -6.0); bgm("warm_outro", -7.5)
scene("s18_disclaimer", "assets/c15.jpg", "static_hold", beat_type="ending", level="A",
      intent="Khung tĩnh sạch hiển thị lưu ý miễn trừ trách nhiệm cuối phim",
      tr="fade_black", trd=0.35)
mark("disc_start")
beat(3.8)

# ================================================================ COMPILE
t = 0.0
scenes, dialogue, bubbles, notifications, foley, chapters = [], [], [], [], [], []
amb_runs, bgm_runs, marks = [], [], {}
pending_fx: list[tuple[int, str, dict]] = []


def est(text: str) -> float:
    return len(text.split()) * SEC_PER_WORD + LINE_BASE


for kind, d in E:
    if kind == "scene":
        if scenes:
            scenes[-1]["end"] = round(t, 2)
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
        if d["tr"]:
            sc["transition_in"] = {"type": d["tr"], "dur": d["trd"]}
        if d["shake"] is not None:
            sc["shakes"] = [{"at": round(t + d["shake"], 2), "dur": 0.4, "amp": 16}]
        if d["parallax"]:
            sc["parallax"] = d["parallax"]
        scenes.append(sc)
        t += SCENE_LEAD
    elif kind == "detail":
        pending_fx.append((len(scenes) - 1, "detail", dict(d, anchor=t)))
    elif kind == "blink":
        pending_fx.append((len(scenes) - 1, "blink", dict(d)))
    elif kind == "mouth":
        pending_fx.append((len(scenes) - 1, "mouth", dict(d)))
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
    elif kind == "notif":
        s = t + d["offset"]
        notifications.append({
            "title": d["title"],
            "text": d["text"],
            "y": d["y"],
            "stamp": d["stamp"],
            "style": d["style"],
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

# Resolve scene-scoped detail_fx, eye_blink, and mouth_sync with real scene boundaries
for sc_idx, fx_kind, item in pending_fx:
    sc = scenes[sc_idx]
    sc_s, sc_e = float(sc["start"]), float(sc["end"])
    dfx = sc.setdefault("detail_fx", [])
    if fx_kind == "blink":
        bt = sc_s + float(item["first_offset"])
        btimes = []
        k = 0
        while bt < sc_e - 0.50:
            btimes.append(round(bt, 2))
            jitter = ((k * 37) % 11 - 5) * 0.07
            bt += max(2.2, float(item["interval"]) + jitter)
            k += 1
        if not btimes and (sc_e - sc_s) > 1.2:
            btimes = [round((sc_s + sc_e) * 0.5, 2)]
        fx_obj = {
            "type": "eye_blink",
            "image": item["image"],
            "region": item["region"],
            "times": btimes,
            "feather": item["feather"],
            "close_dur": item["close_dur"],
            "hold_dur": item["hold_dur"],
            "open_dur": item["open_dur"],
        }
        if item.get("layer"):
            fx_obj["layer"] = item["layer"]
        dfx.append(fx_obj)
    elif fx_kind == "mouth":
        fx_obj = {
            "type": "mouth_sync",
            "speaker": item["speaker"],
            "line_ids": item["line_ids"],
            "default_state": item["default_state"],
            "closed_image": item["closed_image"],
            "mid_image": item["mid_image"],
            "open_image": item["open_image"],
            "region": item["region"],
            "fps": 12,
            "thresh_mid": item["thresh_mid"],
            "thresh_open": item["thresh_open"],
            "feather": item["feather"],
        }
        if item.get("layer"):
            fx_obj["layer"] = item["layer"]
        dfx.append(fx_obj)
    elif fx_kind == "detail":
        anchor = float(item["anchor"])
        kw = dict(item["kwargs"])
        end_mark = kw.pop("end_at_mark", None)
        fx_obj = {"type": item["type"], **kw}
        if item["offset_start"] is not None:
            fx_obj["start"] = round(anchor + float(item["offset_start"]), 2)
        if end_mark is not None and end_mark in marks:
            fx_obj["end"] = round(float(marks[end_mark]), 2)
        elif item["offset_end"] is not None:
            fx_obj["end"] = round(anchor + float(item["offset_end"]), 2)
        elif item["end_scene"]:
            fx_obj["end"] = round(sc_e, 2)
        if item["offset_at"] is not None:
            fx_obj["at"] = round(anchor + float(item["offset_at"]), 2)
        if item["dur"] is not None:
            fx_obj["dur"] = float(item["dur"])
        if item["type"] == "light_shift" and "end" in kw and item["offset_at"] is not None:
            fx_obj["end"] = round(anchor + float(kw["end"]), 2)
        dfx.append(fx_obj)


def mmss(x: float) -> str:
    return f"{int(x // 60):02d}:{int(x % 60):02d}"


def _title_case_vi(s: str) -> str:
    out = s.capitalize()
    for abbr in ("AI", "FOMO", "VIP"):
        out = out.replace(abbr.lower(), abbr)
    return out


_desc = [(0.0, "Mở đầu – Văn phòng bay 100 agent và 240 triệu bốc hơi")]
_desc += [(c["start"] - 0.2, f"{c['kicker'].split('·')[0].strip().title()} – {_title_case_vi(c['title'])}")
          for c in chapters if c["kicker"]]
_desc += [(marks["rf_start"], "Nhớ kỹ – 4 dấu hiệu phễu khóa học công nghệ ảo")]
desc_chapters = "\n".join(f"{mmss(max(0.0, s))} {label}" for s, label in sorted(_desc))

episode = {
    "episode_id": "EP10",
    "slug": "GiamDoc100Agent",
    "title": "Giám đốc 100 Agent – Suất cuối giảm 80%",
    "version": "v5-level2-abc-staging",
    "motion_upgrade": "level2",
    "scam_family": "VAR-FUNNEL-01 / VAR-AI-01 · AI-AGENT-VIRTUAL-OFFICE-FUNNEL – Phễu khóa học công nghệ giảm sốc 80% trong 10 phút + chim mồi hội trường + tặng văn phòng ảo bay ngoài không gian 100 AI agent (hoạt ảnh vẽ sẵn chạy ngoại tuyến) dụ nạp gói trạm máy chủ",
    "duration_sec": total,
    "visual_style_lock": (
        "Horizontal 16:9 widescreen (1920x1080), semi-realistic cinematic 2D anime illustration, "
        "contemporary Southern Vietnam urban setting, clean crisp dark ink outlines, naturalistic dramatic lighting, "
        "clean bottom 15% for subtitles, no text, no letters, no numbers, no license plates, no logos, no real app interface, no real uniforms"
    ),
    "hook": {
        "kicker": "GIẢM 80% TRONG 10 PHÚT",
        "title": "GIÁM ĐỐC 100 AGENT – TIỀN THẬT ĐI ĐÂU?",
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
        "title": "NHỚ KỸ – PHỄU CÔNG TY ẢO 100 AGENT",
        "start": marks["rf_start"],
        "end": marks["rf_end"],
        "stagger_sec": 0.45,
        "items": [
            "Đánh vào nỗi sợ tụt hậu AI & giảm sốc 80%: Hù bị đào thải rồi ép cọc trong 10 phút để bạn không kịp kiểm chứng",
            "Văn phòng ảo đủ phòng ban tự kiếm tiền: Thử ngắt mạng, soi dữ liệu mạng 0 KB hoặc chỉnh ngày máy sẽ lột ngay hoạt ảnh chạy chay",
            "Phông bạt siêu xe & chim mồi hội trường: Xe sang, hội trường có thể thuê theo giờ; người bật dậy chốt suất đầu dễ là diễn viên",
            "Trả lãi mồi đợt đầu rồi khóa cổng nô lệ hóa: Cho rút khoản nhỏ xóa nghi ngờ, nạp gói lớn liền báo kẹt đối soát ép nộp thêm",
        ],
        "action": "Luôn hỏi thẳng 'bán hàng gì, cho ai' và kiểm chứng pháp nhân trước khi xuống tiền; lỡ sập bẫy phải dừng cắt lỗ ngay, cảnh giác dịch vụ 'thu hồi vốn' và gom sao kê trình báo công an!",
    },
    "disclaimer": {
        "header": "LƯU Ý",
        "start": marks["disc_start"],
        "end": total,
        "lines": [
            "Tình huống trong phim được dựng lại nhằm mục đích cảnh báo cộng đồng; nhân vật, tên gọi và số liệu đều là hư cấu.",
            "AI chân chính là công cụ hỗ trợ làm việc thật — hãy tỉnh táo trước mọi lời hứa hẹn tự động sinh lời và kiểm chứng kỹ trước khi chuyển tiền.",
        ],
    },
    "audio": {
        "ambience": amb_runs,
        "foley": foley,
        "bgm": bgm_runs,
        "duck_extra": [
            {"start": marks["hook_empty"] - 0.2, "end": marks["hook_empty"] + 3.0, "bgm_db": -12, "amb_db": -8},
            {"start": marks["countdown_stage"] - 0.2, "end": marks["countdown_stage"] + 8.0, "bgm_db": -10, "amb_db": -7},
            {"start": marks["floating_office"] - 0.2, "end": marks["floating_office"] + 9.0, "bgm_db": -10, "amb_db": -7},
            {"start": marks["bait_profit"] - 0.2, "end": marks["bait_profit"] + 8.0, "bgm_db": -10, "amb_db": -7},
            {"start": marks["gate_locked"] - 0.2, "end": marks["gate_locked"] + 9.0, "bgm_db": -11, "amb_db": -8},
            {"start": marks["airplane_expose"] - 0.2, "end": marks["airplane_expose"] + 12.0, "bgm_db": -11, "amb_db": -7},
            {"start": marks["coda_start"] - 0.2, "end": marks["disc_start"] - 0.2, "bgm_db": -10, "amb_db": -7},
            {"start": marks["disc_start"], "end": total - 0.05},
        ],
    },
    "forbidden_terms": [],
    "publish": {
        "titles": [
            "Giám Đốc 100 Agent AI – Suất Cuối Giảm 80%: Bật Chế Độ Máy Bay Mới Tái Mặt! | Bóc Trần Lừa Đảo",
            "Tặng Văn Phòng Bay 100 Agent Báo Lãi Từng Giây – Sao Tắt Mạng Vẫn Chạy? | Bóc Trần Lừa Đảo",
            "Từ Vé 299 Ngàn Tới 240 Triệu: Giải Phẫu Phễu Khóa Học Công Nghệ 100 Agent | Bóc Trần Lừa Đảo",
        ],
        "description": (
            "Giữa cơn bão lo âu bị thời đại công nghệ bỏ lại, một chủ tiệm đồ gia dụng nhỏ bị cuốn vào hội nghị giảm sốc 80% trong 10 phút "
            "cùng món quà 'văn phòng ảo bay trên không gian với 100 agent AI đủ phòng bán hàng, chăm khách, kế toán tự động kiếm tiền'.\n\n"
            "Khi vét sạch 240 triệu thì cổng rút bị khóa đòi thêm 40 triệu, biến 'Giám đốc' thành kẻ đi năn nỉ xin lại chính tiền của mình. "
            "Chỉ đến khi người vợ bật Chế độ Máy bay, rồi đập tan chiêu phản pháo 'chế độ ngoại tuyến' bằng dữ liệu mạng 0 KB cả tháng và chỉnh ngày về năm 2000 vẫn nhảy đơn mới, lớp vỏ công nghệ mới sụp đổ hoàn toàn.\n\n"
            "AI là công cụ hỗ trợ làm việc thật — nhưng hễ gặp mô hình hứa hẹn tự đẻ tiền, giảm giá ảo ép cọc nhanh và đòi nạp thêm phí mở cổng, hãy dừng ngay!\n\n"
            "⏱️ Các hồi trong phim:\n" + desc_chapters
        ),
        "pinned_comment": (
            "📌 Câu hỏi của Hương ở Hồi 3 ('Nguyên công ty ảo đó bán món hàng gì, cho ai?') khiến ngay cả người trong cuộc cũng lúng túng — đó chính là bộ lọc mạnh nhất cho mọi mô hình gắn mác công nghệ. "
            "Còn cú bóc trần dữ liệu mạng 0 KB và lời chốt cuối phim của Chị Hai — bạn có nhận ra móc nối với các tập trước không?\n"
            "⚠️ Lưu ý: Không đăng SĐT, STK hay tên cá nhân/doanh nghiệp thật; tuyệt đối cảnh giác mọi bình luận mời chào dịch vụ 'hỗ trợ thu hồi vốn'."
        ),
        "hashtags": ["#bóctrầnlừađảo", "#cảnhgiáclừađảo", "#vạnchuyện", "#aiagent", "#phễukhóahọc"],
        "tags": [
            "cảnh giác lừa đảo", "bóc trần lừa đảo", "vạn chuyện", "lừa đảo khóa học AI",
            "giám đốc 100 agent", "suất cuối giảm 80 phần trăm", "văn phòng ảo 100 agent",
            "phễu hội thảo công nghệ", "công ty một người AI", "chế độ máy bay lật tẩy app giả",
        ],
        "category": "Education (Giáo dục)",
        "playlist": "Hồ Sơ Bóc Trần Lừa Đảo – Phim Dài Chuyên Sâu",
        "thumbnail_sec": round(marks["floating_office"] + 1.2, 2),
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
