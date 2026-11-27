# -*- coding: utf-8 -*-
"""
Trình biên dịch `factory196/materialAndDraft/EP08b/episode.json` – Tập EP08b:
"Tiền nổi rồi, tên lại khác" (16:9 Long-form · Nối tiếp trực tiếp dòng tiền 45 triệu từ EP08 · v2-level2-abc-staging).

Chuẩn Visual Motion Upgrade Level 2 + Living-Character A/B/C (HRN-MOTION-L2.1):
  - Level B (2.5D Parallax + Breathing + Layer-Locked Blink/Mouth): 4 cảnh (s09, s11, s13, s17b)
  - Level C (Living-Character eye_blink + 3-state mouth_sync từ WAV thật + breathing + detail_reveal/screen_glow/light_shift/focus_highlight): 14 cảnh (23 character rigs trên toàn bộ 12 cảnh rõ mặt!)
  - Level A (Static Hold / Pan sạch): 5 cảnh (s06, s15, s16, s18, s19)
  - 0 chuỗi lặp >= 3 push_in · 0 hiệu ứng bị loại trừ L480 · 100% foley khớp mốc sự kiện

Nguồn sự thật duy nhất của timeline:
    python factory196/materialAndDraft/EP08b/source/build_draft.py
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
# 10 tuyến nhân vật = 10 voice hoàn toàn tách biệt trong 02_CAST/cast.json
NOT_OLD = "tuyệt đối không giả giọng ông già hay bà già run rẩy, không kéo dài chữ, không cải lương"
KHANG_BASE = (
    "Giọng nam thanh niên miền Nam Sài Gòn 26 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
    "giữ cố định một âm sắc sáng trẻ, nhịp nhanh gọn, thật thà lễ phép, rõ chữ, tự nhiên như đời thực, "
    + NOT_OLD
)
MINH_BASE = (
    "Giọng nam miền Nam Sài Gòn 39 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
    "giữ cố định một âm sắc trầm chắc, thẳng tính, đời thường, nói gọn rõ chữ, tự nhiên như đời thực, "
    + NOT_OLD
)
THAO_BASE = (
    "Giọng phụ nữ miền Nam Sài Gòn 36 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
    "giữ cố định một âm sắc ấm, trầm vừa, cẩn thận thực tế, nói gọn chắc, tự nhiên như đời thực, "
    + NOT_OLD
)
NAM_BASE = (
    "Giọng nam thanh niên miền Nam Sài Gòn 28 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
    "giữ cố định một âm sắc gọn, sáng vừa, nhanh nhẹn, thật thà gần gũi, rõ chữ, tự nhiên như đời thực, "
    + NOT_OLD
)
BUYER_BASE = (
    "Giọng nam miền Nam Sài Gòn 40 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
    "giữ cố định một âm sắc trầm đều, lịch sự mà lạnh tĩnh như kẻ cầm quân cờ, không la hét, "
    + NOT_OLD
)
PROXY_NU_BASE = (
    "Giọng nữ miền Nam Sài Gòn 31 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
    "giữ cố định một âm sắc ngọt ngào lịch sự nhưng nhanh chóng chột dạ lúng túng khi bị chặn, "
    + NOT_OLD
)

SPK = {
    "KHANG_ECHO": dict(
        speaker="thang_tun",
        voice="Puck",
        af="memory",
        label_short="KHANG (EP08)",
        speaker_label="Khang (EP08) – tiếng vọng hồi ức từ khoảnh khắc chuyển 45 triệu sang tài khoản lạ",
        base=KHANG_BASE,
    ),
    "MINH": dict(
        speaker="anh_hai",
        voice="Orus",
        label_short="ANH MINH",
        speaker_label="Anh Minh – chủ tiệm điện lạnh 39 tuổi, thẳng tính, bán chiếc xe máy tay ga 45 triệu",
        base=MINH_BASE,
    ),
    "MINH_P": dict(
        speaker="anh_hai",
        voice="Orus",
        af="phone",
        label_short="ANH MINH",
        speaker_label="Anh Minh gọi qua điện thoại cản gấp Nam ở phòng công chứng",
        base=MINH_BASE,
    ),
    "THAO": dict(
        speaker="chi_hai",
        voice="Sulafat",
        label_short="CHỊ THẢO",
        speaker_label="Chị Thảo – vợ Anh Minh 36 tuổi, tinh ý, thực tế, bình tĩnh xử lý đúng luật",
        base=THAO_BASE,
    ),
    "NAM": dict(
        speaker="thang_tun",
        voice="Achird",
        label_short="NAM",
        speaker_label="Nam – em họ 28 tuổi, thật thà, phản ứng nhanh khi được nhắc kịp thời",
        base=NAM_BASE,
    ),
    "BUYER_MSG": dict(
        speaker="chu_no",
        voice="Fenrir",
        af="phone",
        label_short="KHÁCH MUA",
        speaker_label="Kẻ đứng giữa (từ EP08) đóng vai nick 'Anh Hùng' nhắn chốt mua xe máy 45 triệu",
        base=BUYER_BASE,
    ),
    "BUYER_ROOM": dict(
        speaker="chu_no",
        voice="Fenrir",
        af="default",
        label_short="KẺ ĐỨNG GIỮA",
        speaker_label="Kẻ đứng giữa giấu mặt trong phòng tối – khớp giọng và bối cảnh 2 điện thoại của EP08",
        base=BUYER_BASE,
    ),
    "LONG": dict(
        speaker="ke_ngot_ngao_nam",
        voice="Algieba",
        af="default",
        label_short="LONG",
        speaker_label="Long – người 32 tuổi lịch sự đứng tên mua hộ (khớp giọng Algieba ở EP08 s08)",
        base=(
            "Giọng nam miền Nam Sài Gòn 32 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
            "giữ cố định một âm sắc sáng vừa, mượt mà, lịch sự khéo léo kiểu dân văn phòng, nói nhanh gọn, "
            + NOT_OLD
        ),
    ),
    "LONG_P": dict(
        speaker="ke_ngot_ngao_nam",
        voice="Algieba",
        af="phone",
        label_short="LONG",
        speaker_label="Long báo cáo qua cuộc gọi nhóm đường dây ngầm ở kết mở",
        base=(
            "Giọng nam miền Nam Sài Gòn 32 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
            "giữ cố định một âm sắc sáng vừa, mượt mà, gọn gàng kiểu tay chân báo cáo sếp, "
            + NOT_OLD
        ),
    ),
    "BANK_P": dict(
        speaker="chi_tu",
        voice="Zephyr",
        af="phone",
        label_short="NGÂN HÀNG",
        speaker_label="Nhân viên ngân hàng 29 tuổi gọi xác minh dòng tiền 45 triệu từ đơn trình báo của Khang",
        base=(
            "Giọng nữ miền Nam Sài Gòn 29 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
            "giữ cố định một âm sắc rõ ràng, chuẩn mực, điềm tĩnh kiểu tổng đài viên ngân hàng, "
            + NOT_OLD
        ),
    ),
    "PROXY_NU": dict(
        speaker="ke_ngot_ngao_nu",
        voice="Aoede",
        af="default",
        label_short="NGƯỜI MUA HỘ",
        speaker_label="Người phụ nữ 31 tuổi lịch sự đóng vai đứng tên mua hộ ở Hồi 5",
        base=PROXY_NU_BASE,
    ),
    "PROXY_NU_P": dict(
        speaker="ke_ngot_ngao_nu",
        voice="Aoede",
        af="phone",
        label_short="NGƯỜI MUA HỘ",
        speaker_label="Người mua hộ nữ gọi điện báo động cho bà trùm ở kết mở",
        base=PROXY_NU_BASE,
    ),
    "BOSS_NU": dict(
        speaker="chi_ba",
        voice="Kore",
        af="default",
        label_short="NGƯỜI PHỤ NỮ BÍ ẨN",
        speaker_label="Nhân vật nữ bí mật giấu mặt – hơi liên đới âm sắc & thần thái sắc lạnh kiệm lời của Chị Hai (EP04)",
        base=(
            "Giọng phụ nữ miền Nam Sài Gòn 35 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
            "giữ cố định một âm sắc sắc lạnh, trầm tĩnh, kiệm lời đầy uy quyền, nói ngắn cắt gọn không chút cảm xúc, "
            + NOT_OLD
        ),
    ),
    "N": dict(speaker="nguoi_boc_tran"),
}

# ---------------------------------------------------------------- MOTION PRESETS (LEVEL 2)
MOTION = {
    "static_hold": {"preset": "static_hold"},
    "pan_right": {"preset": "pan_right", "scale": [1.06, 1.06], "focus": [[0.46, 0.49], [0.54, 0.49]], "wobble": "none"},
    "pan_right_breathe": {"preset": "pan_right", "scale": [1.06, 1.06], "focus": [[0.46, 0.49], [0.54, 0.49]], "wobble": "breathe"},
    "pan_left": {"preset": "pan_left", "scale": [1.06, 1.06], "focus": [[0.54, 0.49], [0.46, 0.49]], "wobble": "none"},
    "pull_out": {"preset": "slow_pull_out", "scale": [1.08, 1.02], "focus": [[0.50, 0.48], [0.50, 0.50]], "wobble": "none"},
    "pull_out_breathe": {"preset": "slow_pull_out", "scale": [1.08, 1.02], "focus": [[0.50, 0.47], [0.50, 0.50]], "wobble": "breathe"},
    "pull_right_breathe": {"preset": "slow_pull_out", "scale": [1.09, 1.02], "focus": [[0.56, 0.47], [0.51, 0.49]], "wobble": "breathe"},
    "push_in": {"preset": "slow_push_in", "scale": [1.02, 1.09], "focus": [[0.50, 0.49], [0.50, 0.46]], "wobble": "none", "easing": "ease_out"},
    "push_in_breathe": {"preset": "slow_push_in", "scale": [1.02, 1.09], "focus": [[0.50, 0.48], [0.52, 0.46]], "wobble": "breathe", "easing": "ease_out"},
    "push_right_breathe": {"preset": "subtle_push_right", "scale": [1.02, 1.09], "focus": [[0.51, 0.48], [0.55, 0.46]], "wobble": "breathe", "easing": "ease_out"},
    "drift_up_breathe": {"preset": "drift_up", "scale": [1.05, 1.06], "focus": [[0.52, 0.51], [0.52, 0.45]], "wobble": "breathe", "easing": "smoothstep"},
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


def blink(image: str, region: list[float], first_offset: float = 1.6, interval: float = 4.0,
          feather: float = 0.006, layer: str | None = None, close_dur: float = 0.055,
          hold_dur: float = 0.045, open_dur: float = 0.085):
    E.append(("blink", dict(
        image=image, region=region, first_offset=first_offset, interval=interval,
        feather=feather, layer=layer, close_dur=close_dur, hold_dur=hold_dur, open_dur=open_dur,
    )))


def mouth(speaker: str, line_ids: list[str], region: list[float], default_state: str,
          closed_image: str, mid_image: str, open_image: str,
          feather: float = 0.006, layer: str | None = None,
          thresh_mid: float = 0.11, thresh_open: float = 0.52,
          round_image: str | None = None):
    E.append(("mouth", dict(
        speaker=speaker, line_ids=line_ids, region=region, default_state=default_state,
        closed_image=closed_image, mid_image=mid_image, open_image=open_image,
        feather=feather, layer=layer, thresh_mid=thresh_mid, thresh_open=thresh_open,
        round_image=round_image,
    )))


def fx(fx_dict: dict):
    E.append(("fx", fx_dict))


def sfx_abs(preset: str, at: float, gain: float = -5.0, dur: float | None = None):
    E.append(("sfx_abs", dict(preset=preset, at=at, gain=gain, dur=dur)))


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
# ---- HOOK · MÔ-TÍP MÀU SẮC 12:05 (CHƯA LỘ TÊN) & CÚ GỌI XÁC MINH 45 TRIỆU ----
amb("office", -3.0); bgm("suspense_pulse", -2.5)
scene("s00a_pulse_1205", "assets/c00a.jpg", "pan_right", beat_type="establishing", level="C",
      intent="Quét ngang theo dải sáng dòng tiền cyan-amber + bộ đếm +45.000.000đ + Chromatic Pulse nối EP08 sang điện thoại Anh Minh")
sfx("typing", 0.1, -5, dur=0.6)
sfx("message_send", 0.75, -3)
sfx("bank_ting", 1.2, -2.5)
sfx_abs("counter_tick", 0.55, -5.5)
fx({"type": "animated_counter", "start": 0.55, "end": 2.55, "count_dur": 1.1,
    "from_val": 0, "to_val": 45000000, "fmt": "vnd", "label": "TIỀN THẬT ĐÃ NỔI · 12:05",
    "pos": [0.24, 0.68], "style": "safe", "easing": "ease_out"})
fx({"type": "chromatic_pulse", "at": 1.20, "dur": 0.25, "shift_px": 5, "zoom_blur": 0.018})
fx({"type": "color_mood", "mood": "warm_daily", "strength": 0.45, "vignette": 0.10, "grain": 0.006})
detail("screen_glow", offset_start=0.05, end_scene=True, pos=[0.32, 0.56], radius=[0.18, 0.20],
       color=[105, 220, 255], intensity=0.28, mode="pulse", fade=0.25)
detail("screen_glow", offset_start=0.95, end_scene=True, pos=[0.73, 0.50], radius=[0.20, 0.22],
       color=[255, 205, 110], intensity=0.38, mode="turn_on", fade=0.22)
detail("light_shift", offset_at=1.20, dur=0.10, end=1.48, end_dur=0.22,
       brightness=1.14, tint_rgb=[255, 220, 150], tint_strength=0.10)
bubble("BIẾN ĐỘNG SỐ DƯ · 12:05", "+45.000.000đ · Đã vào tài khoản · Công chứng xong",
       side="left", y=260, stamp="TIỀN THẬT ĐÃ NỔI", dur=2.2, offset=0.2)
beat(2.3)

amb("room_tone", -2.5); bgm("suspense_pulse", -2.5)
scene("s00b_hook_call", "assets/c00.jpg", "push_right_breathe", beat_type="suspicion", level="C",
      intent="Zoom Punch vào Anh Minh + chớp mắt & chép miệng 4 trạng thái + sóng âm Ngân hàng xác minh 45 triệu + Cold Suspicion",
      tr="zoom_punch", trd=0.24, shake=0.18)
sfx("phone_ring", 0.1, -4, dur=0.8)
blink("assets/c00_minh_blink.jpg", [0.476, 0.193, 0.630, 0.357], first_offset=1.9, interval=4.1)
mouth("anh_hai", ["l02_minh"], [0.511, 0.306, 0.630, 0.450], "mid",
      "assets/c00_minh_mouth_closed.jpg", "assets/c00.jpg", "assets/c00_minh_mouth_open.jpg",
      round_image="assets/c00_minh_mouth_round.jpg")
fx({"type": "phone_waveform", "speaker": "chi_tu", "line_ids": ["l01_bank_p", "l03_bank_p"],
    "start": 3.8, "end": 21.4, "pos": [0.24, 0.56], "size": [0.25, 0.058],
    "color": [255, 95, 85], "label": "NGÂN HÀNG · XÁC MINH 45TR"})
fx({"type": "color_mood", "mood": "cold_suspicion", "strength": 0.38, "vignette": 0.16, "grain": 0.008})
bubble("XÁC MINH DÒNG TIỀN · NGÂN HÀNG", "Đơn trình báo vụ lừa 45.000.000đ · Chảy thẳng vào TK này",
       side="left", y=260, stamp="YÊU CẦU XÁC MINH", dur=4.5, offset=0.15)
beat(0.85)
line("l01_bank_p", "BANK_P",
     "Chào anh Minh. Có đơn trình báo vụ lừa bốn lăm triệu, tiền chảy thẳng vô tài khoản anh.",
     "chuẩn mực, bình tĩnh qua điện thoại",
     sub="Chào anh Minh. Có đơn trình báo vụ lừa 45 triệu, tiền chảy thẳng vô tài khoản anh.")
line("l02_minh", "MINH",
     "Khoan chị! Bốn lăm triệu đó khách mua xe máy chuyển tại phòng công chứng mà! Tôi giao xe rồi!",
     "sững người, giọng gấp gáp khó tin",
     sub="Khoan chị! 45 triệu đó khách mua xe máy chuyển tại phòng công chứng mà! Tôi giao xe rồi!")
line("l03_bank_p", "BANK_P",
     "Nhưng người chuyển báo bị lừa, không mua xe của anh. Nội dung cũng không ghi mua xe.",
     "rõ ràng, dứt khoát đúng nghiệp vụ")

scene("s01_hook_freeze", "assets/c01.jpg", "static_hold", beat_type="anomaly", level="C",
      intent="Zoom Punch đứng hình: Anh Minh chớp mắt sững sờ + khoanh đỏ màn hình sao kê + Chromatic Pulse + High Tension",
      tr="zoom_punch", trd=0.24, shake=0.15)
mark("hook_freeze")
sfx("impact", 0.0, -2.5)
sfx_abs("marker_draw", 22.10, -5.0)
blink("assets/c01_minh_blink.jpg", [0.603, 0.206, 0.764, 0.343], first_offset=1.15, interval=3.5)
fx({"type": "red_circle_draw", "region": [0.51, 0.63, 0.65, 0.84], "at": 22.1, "dur": 0.40, "end": 23.9,
    "style": "circle", "width": 5, "color": [248, 58, 58]})
fx({"type": "chromatic_pulse", "at": 21.95, "dur": 0.28, "shift_px": 7, "zoom_blur": 0.024})
fx({"type": "color_mood", "mood": "high_tension", "strength": 0.50, "vignette": 0.24, "grain": 0.012})
detail("focus_highlight", offset_start=0.05, end_scene=True, pos=[0.66, 0.48], radius=[0.32, 0.38], dim_outer=0.26, fade=0.30)
detail("screen_glow", offset_start=0.10, end_scene=True, pos=[0.57, 0.72], radius=[0.18, 0.20],
       color=[110, 225, 255], intensity=0.28, mode="turn_on", fade=0.30)
bubble("SAO KÊ NGÂN HÀNG · 12:05", "+45.000.000đ · Từ: TÊN LẠ · ND: Chuyen tien",
       side="left", y=260, stamp="TIỀN TỪ VỤ LỪA?", dur=2.0, offset=0.15)
sfx("heartbeat", 0.2, -5, dur=1.6)
beat(1.9)

# ---- HỒI 1 · BA HÔM TRƯỚC: KHÁCH CHỐT KHÔNG MẶC CẢ ----
amb("street", -5.0); bgm("investigative_story", -3.8)
scene("s02_sell_bike_cafe", "assets/c02.jpg", "pan_right_breathe", beat_type="establishing", level="C",
      intent="Chuyển hồi Film Burn về quán trà đá sáng: 3 nhân vật (Minh, Thảo, Nam) chớp mắt & chép miệng + hạt nắng sớm ấm áp",
      tr="film_burn", trd=0.45)
fx({"type": "ambient_particles", "count": 20, "opacity": 0.24, "color": [255, 240, 190], "drift_dir": "float", "seed": 82})
fx({"type": "color_mood", "mood": "warm_daily", "strength": 0.56, "vignette": 0.08, "grain": 0.0})
chapter("HỒI 1 · BA HÔM TRƯỚC", "KHÁCH CHỐT KHÔNG MẶC CẢ")
sfx("chapter_sting", -0.1, -5)
blink("assets/c02_minh_blink.jpg", [0.365, 0.266, 0.471, 0.373], first_offset=2.1, interval=4.3)
blink("assets/c02_thao_blink.jpg", [0.540, 0.305, 0.644, 0.444], first_offset=3.4, interval=4.6)
blink("assets/c02_nam_blink.jpg", [0.719, 0.278, 0.841, 0.419], first_offset=1.5, interval=3.9)
mouth("anh_hai", ["l05_minh", "l07_minh"], [0.367, 0.348, 0.462, 0.481], "mid",
      "assets/c02_minh_mouth_closed.jpg", "assets/c02.jpg", "assets/c02_minh_mouth_open.jpg")
mouth("chi_hai", ["l06_thao"], [0.541, 0.395, 0.630, 0.511], "closed",
      "assets/c02.jpg", "assets/c02_thao_mouth_mid.jpg", "assets/c02_thao_mouth_open.jpg")
mouth("thang_tun", ["l04_nam", "l08_nam"], [0.732, 0.371, 0.849, 0.512], "mid",
      "assets/c02_nam_mouth_closed.jpg", "assets/c02.jpg", "assets/c02_nam_mouth_open.jpg")
beat(0.55)
line("l04_nam", "NAM",
     "Chiếc tay ga rao bốn lăm triệu cả tuần, thợ trả bốn chục. Chắc bớt chút mới trôi.",
     "uống trà đá nói chuyện thoải mái",
     sub="Chiếc tay ga rao 45 triệu cả tuần, thợ trả 40. Chắc bớt chút mới trôi.")
line("l05_minh", "MINH",
     "Sáng nay có anh Hùng hỏi mua. Coi hình xong chốt thẳng bốn lăm triệu, hông trả giá một đồng!",
     "mừng rỡ khoe với em họ và vợ",
     sub="Sáng nay có anh Hùng hỏi mua. Coi hình xong chốt thẳng 45 triệu, hông trả giá một đồng!")
line("l06_thao", "THAO",
     "Nghe dễ quá cũng lạ nha anh. Sao ổng hông qua coi xe trực tiếp?",
     "nhíu mày nhẹ, đặt câu hỏi thực tế")
line("l07_minh", "MINH",
     "Ổng công tác xa, thấy xe hợp màu nên chốt. Tiền nổi vô tài khoản anh mới ký công chứng, sợ gì!",
     "xua tay tự tin tuyệt đối vào quy tắc cũ")
line("l08_nam", "NAM",
     "Gặp khách sộp vậy sướng ha! Ít bữa em bán xe máy chắc cũng lên nhóm rao thử.",
     "cười trầm trồ thật thà", pause=0.15)

amb("night_room", -2.8); bgm("tension_drone", -3.0)
scene("s03_buyer_chat_dark", "assets/c03_dim.jpg", "pan_left", beat_type="information", level="C",
      intent="Luma Wipe sang phòng tối EP08: màn hình bừng sáng detail_reveal + typing_indicator + sóng âm khách mua + Noir Evidence",
      tr="luma_wipe", trd=0.38)
fx({"type": "typing_indicator", "start": 55.30, "end": 55.70, "side": "left", "y": 260})
fx({"type": "phone_waveform", "speaker": "chu_no", "line_ids": ["l09_buyer_msg", "l10_buyer_msg"],
    "start": 56.0, "end": 68.5, "pos": [0.24, 0.56], "size": [0.25, 0.058],
    "color": [95, 215, 245], "label": "ANH HÙNG · CHỐT MUA NHANH"})
fx({"type": "color_mood", "mood": "noir_evidence", "strength": 0.52, "vignette": 0.22, "grain": 0.012})
sfx("typing", 0.15, -5, dur=0.8)
sfx("message_send", 0.9, -4)
detail("detail_reveal", offset_at=0.22, dur=0.30, image="assets/c03.jpg")
detail("screen_glow", offset_start=0.32, end_scene=True, pos=[0.61, 0.66], radius=[0.20, 0.16],
       color=[115, 215, 255], intensity=0.28, mode="turn_on", fade=0.30)
bubble("KHÁCH MUA · ANH HÙNG", "Chốt 45tr · Nhờ em họ Long đứng tên mua hộ",
       side="left", y=260, stamp="MỒI CHỐT NHANH", dur=4.8, offset=0.15)
beat(0.5)
line("l09_buyer_msg", "BUYER_MSG",
     "Anh bận công tác xa chưa về kịp, nên nhờ em họ tên Long ra công chứng đứng tên mua hộ.",
     "lịch sự, bình thản đầy tin cậy")
line("l10_buyer_msg", "BUYER_MSG",
     "Chú yên tâm. Bao giờ tiền nổi đủ bốn lăm triệu trong tài khoản rồi hẵng ký giao xe!",
     "chủ động trấn an để hạ cảnh giác",
     sub="Chú yên tâm. Bao giờ tiền nổi đủ 45 triệu trong tài khoản rồi hẵng ký giao xe!",
     pause=0.15)

# ---- HỒI 2 · 12 GIỜ TRƯA HÔM SAU: PHÒNG CÔNG CHỨNG ĐÔNG ĐÚC & MỘT THOÁNG GỢN LẠ ----
amb("crowd", -5.5); bgm("investigative_story", -4.0)
scene("s04_notary_meeting", "assets/c04.jpg", "pull_out_breathe", beat_type="normal", level="C",
      intent="Whip Pan sang phòng công chứng đông người + 3 nhân vật (Minh, Thảo, Long) chớp mắt & chép miệng + hạt sáng dịu",
      tr="whip_pan_right", trd=0.30)
fx({"type": "ambient_particles", "count": 16, "opacity": 0.20, "color": [255, 242, 205], "drift_dir": "float", "seed": 84})
fx({"type": "color_mood", "mood": "warm_daily", "strength": 0.45, "vignette": 0.08, "grain": 0.0})
chapter("HỒI 2 · TRƯA HÔM SAU", "TIỀN ĐÃ NỔI TRONG TÀI KHOẢN")
sfx("chapter_sting", -0.1, -5)
blink("assets/c04_minh_blink.jpg", [0.191, 0.218, 0.291, 0.352], first_offset=2.6, interval=4.5)
blink("assets/c04_thao_blink.jpg", [0.373, 0.271, 0.462, 0.404], first_offset=1.8, interval=4.1)
blink("assets/c04_long_blink.jpg", [0.715, 0.241, 0.817, 0.349], first_offset=3.2, interval=4.4)
mouth("chi_hai", ["l12_thao"], [0.377, 0.348, 0.460, 0.476], "closed",
      "assets/c04.jpg", "assets/c04_thao_mouth_mid.jpg", "assets/c04_thao_mouth_open.jpg")
mouth("ke_ngot_ngao_nam", ["l11_long", "l13_long"], [0.727, 0.332, 0.818, 0.461], "mid",
      "assets/c04_long_mouth_closed.jpg", "assets/c04.jpg", "assets/c04_long_mouth_open.jpg")
beat(0.55)
line("l11_long", "LONG",
     "Em là Long, em họ anh Hùng. Hồ sơ nộp quầy rồi, chờ gọi tên thôi anh chị.",
     "cười lịch sự, gọn gàng giữa sảnh công chứng đông người")
line("l12_thao", "THAO",
     "Rồi chút nữa bên anh Hùng chuyển thẳng qua luôn hả cậu?",
     "hỏi xã giao bình thường, không chút căng thẳng")
line("l13_long", "LONG",
     "Dạ ảnh đang bấm chuyển đó chị, tiền vô là mình vô ký gọn.",
     "trấn an nhẹ nhàng, hoàn toàn tự nhiên", pause=0.15)

amb("crowd", -5.5); bgm("suspense_pulse", -4.2)
scene("s05_money_arrives_mismatch", "assets/c05.jpg", "push_in_breathe", beat_type="anomaly", level="C",
      intent="Nhịp 12:05 tiếng ting vang lên + bộ đếm +45.000.000đ lệch tên Khang + Chromatic Pulse + đối thoại 3 nhân vật",
      tr="dissolve", trd=0.3)
mark("money_mismatch")
sfx("bank_ting", 0.15, -2.5)
sfx_abs("counter_tick", 84.30, -5.5)
fx({"type": "animated_counter", "start": 84.3, "end": 91.2, "count_dur": 1.4,
    "from_val": 0, "to_val": 45000000, "fmt": "vnd", "label": "NGƯỜI GỬI: KHANG (LỆCH TÊN)",
    "pos": [0.24, 0.72], "style": "warn", "easing": "ease_out"})
fx({"type": "chromatic_pulse", "at": 88.35, "dur": 0.26, "shift_px": 5, "zoom_blur": 0.018})
fx({"type": "color_mood", "mood": "cold_suspicion", "strength": 0.26, "vignette": 0.12, "grain": 0.006})
blink("assets/c05_thao_blink.jpg", [0.221, 0.329, 0.303, 0.444], first_offset=2.4, interval=4.2)
blink("assets/c05_minh_blink.jpg", [0.389, 0.227, 0.485, 0.366], first_offset=1.5, interval=3.9)
blink("assets/c05_long_blink.jpg", [0.715, 0.243, 0.817, 0.380], first_offset=3.1, interval=4.5)
mouth("chi_hai", ["l15_thao"], [0.219, 0.399, 0.301, 0.531], "closed",
      "assets/c05.jpg", "assets/c05_thao_mouth_mid.jpg", "assets/c05_thao_mouth_open.jpg")
mouth("anh_hai", ["l14_minh"], [0.376, 0.347, 0.479, 0.463], "closed",
      "assets/c05.jpg", "assets/c05_minh_mouth_mid.jpg", "assets/c05_minh_mouth_open.jpg")
mouth("ke_ngot_ngao_nam", ["l16_long"], [0.727, 0.331, 0.817, 0.457], "mid",
      "assets/c05_long_mouth_closed.jpg", "assets/c05.jpg", "assets/c05_long_mouth_open.jpg")
detail("screen_glow", offset_start=0.15, end_scene=True, pos=[0.50, 0.58], radius=[0.18, 0.18],
       color=[255, 210, 115], intensity=0.32, mode="turn_on", fade=0.25)
detail("light_shift", offset_at=0.15, dur=0.10, end=0.45, end_dur=0.25,
       brightness=1.12, tint_rgb=[255, 225, 165], tint_strength=0.09)
bubble("NGÂN HÀNG CỦA MINH · 12:05", "+45.000.000đ · Đã vào tài khoản",
       side="left", y=108, stamp="ĐÃ NHẬN TIỀN", dur=4.2, offset=0.15)
beat(0.6)
line("l14_minh", "MINH",
     "Đủ bốn lăm triệu rồi. Ra ký đi em.",
     "nhìn thoáng số dư, giọng nhẹ hẳn xuống đầy yên tâm và kiệm lời",
     sub="Đủ 45 triệu rồi. Ra ký đi em.")
line("l15_thao", "THAO",
     "Ủa… người gửi sao tên Khang lạ vậy anh?",
     "liếc màn hình đúng nửa giây, khựng nhẹ hỏi nhỏ")
line("l16_long", "LONG",
     "Kế toán bên công ty ảnh chuyển đó chị. Tới số mình vô ký rồi.",
     "cười nhẹ lịch sự, gật gọn tự nhiên hướng về quầy công chứng", pause=0.15)

amb("street", -4.5); bgm("investigative_story", -3.8)
scene("s06_sign_handover", "assets/c06.jpg", "pan_left", beat_type="normal", level="C",
      intent="Pan ngang sáng trưa trước sảnh công chứng: Long chớp mắt & chép miệng nhận chìa khóa chạy xe đi + hạt nắng trưa",
      tr="dissolve", trd=0.35)
sfx("footsteps", 0.15, -5, dur=1.0)
blink("assets/c06_long_blink.jpg", [0.740, 0.208, 0.799, 0.287], first_offset=1.3, interval=3.8)
mouth("ke_ngot_ngao_nam", ["l17_long"], [0.742, 0.273, 0.799, 0.347], "mid",
      "assets/c06_long_mouth_closed.jpg", "assets/c06.jpg", "assets/c06_long_mouth_open.jpg")
fx({"type": "ambient_particles", "count": 18, "opacity": 0.22, "color": [255, 244, 205], "drift_dir": "float", "seed": 86})
fx({"type": "color_mood", "mood": "warm_daily", "strength": 0.48, "vignette": 0.08, "grain": 0.0})
bubble("HỢP ĐỒNG CÔNG CHỨNG", "Bên mua: Long · Đã nhận đủ 45.000.000đ · Đã giao xe",
       side="left", y=260, stamp="XONG TRÊN GIẤY", dur=4.0, offset=0.15)
beat(0.5)
line("l17_long", "LONG",
     "Cảm ơn anh chị nha. Em chạy xe về nhà anh Hùng đây!",
     "tươi cười nhận chìa khóa, nổ máy chạy chiếc tay ga đi", pause=0.2)

# ---- HỒI 3 · HAI NGÀY SAU: NICK ĐÃ XÓA, DÒNG TIỀN TỪ VỤ LỪA KHÁC ----
amb("room_tone", -2.5); bgm("tension_drone", -2.5)
scene("s07_call_blocked", "assets/c07.jpg", "pull_right_breathe", beat_type="climax", level="C",
      intent="Luma Wipe sang 2 ngày sau: mất dấu cả hai + ánh đỏ nhấp nháy + Chromatic Pulse + chớp mắt & chép miệng Minh/Thảo",
      tr="luma_wipe", trd=0.38, shake=0.15)
fx({"type": "chromatic_pulse", "at": 103.10, "dur": 0.28, "shift_px": 6, "zoom_blur": 0.022})
fx({"type": "color_mood", "mood": "high_tension", "strength": 0.48, "vignette": 0.22, "grain": 0.012})
chapter("HỒI 3 · HAI NGÀY SAU", "NICK ĐÃ XÓA, XE ĐÃ SANG TAY")
sfx("chapter_sting", -0.1, -5)
sfx("phone_ring", 0.2, -5, dur=0.7)
sfx("call_end", 0.95, -3)
blink("assets/c07_minh_blink.jpg", [0.540, 0.347, 0.647, 0.452], first_offset=2.1, interval=3.8)
blink("assets/c07_thao_blink.jpg", [0.733, 0.274, 0.841, 0.390], first_offset=3.2, interval=4.4)
mouth("anh_hai", ["l18_minh", "l20_minh"], [0.546, 0.440, 0.652, 0.581], "mid",
      "assets/c07_minh_mouth_closed.jpg", "assets/c07.jpg", "assets/c07_minh_mouth_open.jpg")
mouth("chi_hai", ["l19_thao"], [0.737, 0.369, 0.843, 0.503], "closed",
      "assets/c07.jpg", "assets/c07_thao_mouth_mid.jpg", "assets/c07_thao_mouth_open.jpg")
detail("screen_glow", offset_start=0.95, end_scene=True, pos=[0.56, 0.73], radius=[0.18, 0.14],
       color=[255, 65, 70], intensity=0.34, mode="flicker", fade=0.22)
bubble("LIÊN HỆ NGƯỜI MUA", "Nick khách mua đã xóa · Số của Long tắt máy",
       side="left", y=260, stamp="MẤT DẤU CẢ HAI", dur=4.2, offset=0.25)
beat(1.0)
line("l18_minh", "MINH",
     "Trời đất ơi! Nick ông Hùng xóa rồi! Gọi số thằng Long cũng tắt máy luôn!",
     "tái mặt hoảng hốt, giọng run lên")
line("l19_thao", "THAO",
     "Lúc ký em thoáng thấy tên Khang lạ mà tưởng tiền vô là xong… Người đó là ai?",
     "sững người lo lắng, chợt nhớ lại khoảnh khắc hôm công chứng")
line("l20_minh", "MINH",
     "Công an nói anh Khang bị giả sếp nhờ mua quà kỷ niệm cho vợ, lừa chuyển bốn lăm triệu vô máy mình!",
     "giọng trầm nặng, bàng hoàng không tin nổi",
     sub="Công an nói anh Khang bị giả sếp nhờ mua quà kỷ niệm cho vợ, lừa chuyển 45 triệu vô máy mình!")

# CÚ NỔ TWIST HỒI 3: Hồi ức trực tiếp mặt Khang & Anh Đạt (EP08) + khẩu hình Khang khớp voice Puck!
amb("office", -4.5); bgm("tension_drone", -2.0)
scene("s08a_ep08_twist", "assets/c08a.jpg", "push_in_breathe", beat_type="climax", level="C",
      intent="Zoom Punch hồi ức EP08: Khang & Anh Đạt với khẩu hình Khang khớp giọng Puck + Chromatic Pulse + tông Flashback",
      tr="zoom_punch", trd=0.24, shake=0.18)
fx({"type": "chromatic_pulse", "at": 123.25, "dur": 0.30, "shift_px": 7, "zoom_blur": 0.025})
fx({"type": "color_mood", "mood": "flashback", "strength": 0.44, "vignette": 0.20, "grain": 0.014})
mark("ep08_twist")
sfx("impact", 0.0, -2.0)
blink("assets/c08a_dat_blink.jpg", [0.350, 0.238, 0.454, 0.358], first_offset=2.3, interval=4.2)
blink("assets/c08a_khang_blink.jpg", [0.577, 0.231, 0.682, 0.357], first_offset=1.4, interval=3.6)
mouth("thang_tun", ["l20b_khang_echo"], [0.602, 0.329, 0.692, 0.459], "mid",
      "assets/c08a_khang_mouth_closed.jpg", "assets/c08a.jpg", "assets/c08a_khang_mouth_open.jpg")
detail("screen_glow", offset_start=0.15, end_scene=True, pos=[0.50, 0.88], radius=[0.24, 0.14],
       color=[115, 210, 255], intensity=0.26, mode="pulse", fade=0.30)
bubble("12:05 · MẢNH GHÉP", "Khang (-45tr) → TK Anh Minh",
       side="left", y=115, stamp="CÙNG MỘT VỤ LỪA", dur=5.0, offset=0.15)
beat(0.35)
line("l20b_khang_echo", "KHANG_ECHO",
     "Nó chặn mất rồi anh Đạt ơi… Bốn mươi lăm triệu em vừa chuyển qua tài khoản lạ rồi!",
     "tái mặt nghẹn giọng — trích nguyên khoảnh khắc vỡ lẽ từ EP08 (voice Puck)",
     sub="Nó chặn mất rồi anh Đạt ơi… 45 triệu em vừa chuyển qua tài khoản lạ rồi!", pause=0.2)

amb("room_tone", -2.5); bgm("tension_drone", -2.5)
scene("s08b_paper_trap", "assets/c08.jpg", "pull_out", beat_type="information", level="C",
      intent="Cận bàn phòng khách phơi bày bẫy giấy tờ lệch tên: khoanh đỏ cụm sao kê & điện thoại + Noir Evidence",
      tr="dissolve", trd=0.35)
mark("paper_trap")
sfx("heartbeat", 0.2, -5, dur=1.6)
sfx_abs("marker_draw", 132.00, -4.5)
fx({"type": "red_circle_draw", "region": [0.64, 0.36, 0.90, 0.68], "at": 132.0, "dur": 0.50, "end": 141.8,
    "style": "box", "width": 5, "color": [248, 58, 58]})
fx({"type": "color_mood", "mood": "noir_evidence", "strength": 0.46, "vignette": 0.20, "grain": 0.012})
detail("focus_highlight", offset_start=0.20, end_scene=True, pos=[0.54, 0.50], radius=[0.42, 0.36], dim_outer=0.22, fade=0.45)
detail("screen_glow", offset_start=0.25, end_scene=True, pos=[0.85, 0.53], radius=[0.14, 0.18],
       color=[125, 220, 255], intensity=0.26, mode="pulse", fade=0.35)
beat(0.35)
line("l21_thao", "THAO",
     "Hợp đồng bán xe cho Long ghi nhận đủ, còn tiền lại từ anh Khang bị lừa!",
     "đặt hai tờ giấy cạnh nhau trên bàn, giọng trầm căng")
line("l22_minh", "MINH",
     "Nội dung chỉ ghi chuyển tiền, không biển số, không ngày hợp đồng… Cả hai đều là nạn nhân!",
     "ôm trán bàng hoàng nhận ra cái bẫy kế trùng kế", pause=0.15)

# ---- HỒI 4 · LỘ DIỆN CƠ CHẾ: MỘT DÒNG TIỀN, HAI NẠN NHÂN & XỬ LÝ ĐÚNG LUẬT ----
amb("night_room", -2.5); bgm("suspense_pulse", -2.5)
scene("s09_triangle_reveal", "assets/c09.jpg", "push_in", beat_type="information", level="B",
      intent="2.5D Parallax phòng tối + Rack Focus + Breathing + bộ đếm 45.000.000đ rửa tiền tam giác + sóng âm kẻ đứng giữa + Noir Evidence",
      tr="luma_wipe", trd=0.36, shake=0.14,
      parallax={
          "camera": "push_in",
          "dolly": [1.02, 1.08],
          "shift_x": [0.0, 0.0],
          "shift_y": [0.0, -4.0],
          "focus": [0.54, 0.52],
          "strength": 0.88,
          "easing": "ease_out",
          "layers": [
              {"role": "bg", "image": "assets/s09_bg.jpg", "depth": 0.42, "blur_from": 0.4, "blur_to": 3.0, "blur_at": 145.5, "blur_dur": 4.0},
              {"role": "fg", "image": "assets/s09_fg.png", "depth": 1.28, "breathe_y": 1.6, "breathe_period": 3.8},
          ],
      })
sfx_abs("counter_tick", 145.00, -5.5)
fx({"type": "animated_counter", "start": 145.0, "end": 156.5, "count_dur": 1.6,
    "from_val": 0, "to_val": 45000000, "fmt": "vnd", "label": "TIỀN BẨN → XE THẬT (12:05)",
    "pos": [0.24, 0.56], "style": "danger", "easing": "ease_out"})
fx({"type": "phone_waveform", "speaker": "chu_no", "line_ids": ["l23_buyer_room", "l24_buyer_room"],
    "start": 143.2, "end": 156.8, "pos": [0.24, 0.72], "size": [0.25, 0.056],
    "color": [95, 220, 245], "label": "KẺ ĐỨNG GIỮA · BẪY TAM GIÁC"})
fx({"type": "color_mood", "mood": "noir_evidence", "strength": 0.58, "vignette": 0.26, "grain": 0.014})
chapter("HỒI 4 · LỘ DIỆN CƠ CHẾ", "TAM GIÁC LỆCH DÒNG TIỀN")
mark("triangle_reveal")
sfx("impact", 0.0, -2.5)
detail("screen_glow", offset_start=0.20, end_scene=True, space="frame", pos=[0.50, 0.64], radius=[0.24, 0.24],
       color=[105, 215, 255], intensity=0.26, mode="pulse", fade=0.40)
bubble("BẪY TAM GIÁC · 12:05 TRƯA", "Khang chuyển 45tr → TK Minh · Long công chứng lấy xe máy",
       side="left", y=260, stamp="RỬA TIỀN SẠCH", dur=5.2, offset=0.2)
beat(0.5)
line("l23_buyer_room", "BUYER_ROOM",
     "Đầu kia lừa thằng Khang đẩy bốn lăm triệu. Đầu này cho Long công chứng hốt chiếc xe máy.",
     "trầm lạnh điềm nhiên từ phòng tối hai điện thoại",
     sub="Đầu kia lừa thằng Khang đẩy 45 triệu. Đầu này cho Long công chứng hốt chiếc xe máy.")
line("l24_buyer_room", "BUYER_ROOM",
     "Tiền bẩn đổi ra xe thật trong một buổi trưa. Hai nạn nhân tự giải trình với nhau!",
     "lạnh tĩnh chốt gọn ván cờ hai đầu dây", pause=0.15)

amb("room_tone", -3.0); bgm("investigative_story", -3.6)
scene("s10_response_action", "assets/c10.jpg", "pan_right_breathe", beat_type="aftermath", level="C",
      intent="Chuyển cảnh Film Burn về sáng sớm: Minh & Thảo chớp mắt + chép miệng cản rút tiền đúng luật + hạt sáng ấm",
      tr="film_burn", trd=0.45)
fx({"type": "ambient_particles", "count": 18, "opacity": 0.22, "color": [255, 238, 195], "drift_dir": "float", "seed": 90})
fx({"type": "color_mood", "mood": "warm_daily", "strength": 0.52, "vignette": 0.10, "grain": 0.0})
mark("response_action")
blink("assets/c10_minh_blink.jpg", [0.321, 0.169, 0.439, 0.311], first_offset=1.8, interval=4.1)
blink("assets/c10_thao_blink.jpg", [0.619, 0.223, 0.720, 0.346], first_offset=2.9, interval=4.5)
mouth("anh_hai", ["l25_minh", "l27_minh"], [0.327, 0.290, 0.421, 0.422], "mid",
      "assets/c10_minh_mouth_closed.jpg", "assets/c10.jpg", "assets/c10_minh_mouth_open.jpg")
mouth("chi_hai", ["l26_thao"], [0.627, 0.316, 0.713, 0.442], "closed",
      "assets/c10.jpg", "assets/c10_thao_mouth_mid.jpg", "assets/c10_thao_mouth_open.jpg")
beat(0.3)
line("l25_minh", "MINH",
     "Hay anh rút bốn lăm triệu cất trước, chừng nào kiếm lại được xe rồi mới tính?",
     "sốt ruột định làm theo phản xạ",
     sub="Hay anh rút 45 triệu cất trước, chừng nào kiếm lại được xe rồi mới tính?")
line("l26_thao", "THAO",
     "Khoan! Đừng rút hay chuyển đi đâu! Tiền đang xác minh vụ án mà tự tẩu tán còn rắc rối nặng hơn!",
     "cản ngay lập tức, giọng điềm tĩnh kiên quyết")
line("l27_minh", "MINH",
     "Vậy giữ nguyên tiền trong tài khoản, gom hợp đồng, sao kê với tin nhắn trình báo công an liền!",
     "hít sâu lấy lại bình tĩnh, gật đầu dứt khoát", pause=0.2)

# ---- HỒI 5 · HAI TUẦN SAU: CÚ GỌI CHẶN BẪY & NGUYÊN TẮC 2 PHẢI – 3 KHÔNG ----
amb("crowd", -5.5); bgm("suspense_pulse", -3.0)
scene("s11_nam_calls_notary", "assets/c11.jpg", "push_in", beat_type="establishing", level="B",
      intent="2.5D Parallax tách Nam tiền cảnh + Rack Focus + Breathing + Head Micro-Tilt + Nam chớp mắt & chép miệng 4 trạng thái (fg) + sóng âm Anh Minh cản gấp",
      tr="luma_wipe", trd=0.42,
      parallax={
          "camera": "push_in",
          "dolly": [1.02, 1.08],
          "shift_x": [0.0, 0.0],
          "shift_y": [0.0, -3.0],
          "focus": [0.36, 0.46],
          "strength": 0.86,
          "easing": "ease_out",
          "layers": [
              {"role": "bg", "image": "assets/s11_bg.jpg", "depth": 0.42, "blur_from": 0.4, "blur_to": 2.8, "blur_at": 178.0, "blur_dur": 4.0},
              {"role": "fg", "image": "assets/s11_fg.png", "depth": 1.26, "breathe_y": 1.8, "breathe_period": 3.4,
               "head_tilt_deg": 1.0, "head_pivot": [0.25, 0.85], "tilt_speaker": "thang_tun", "tilt_line_ids": ["l28_nam"]},
          ],
      })
chapter("HỒI 5 · HAI TUẦN SAU", "NGUYÊN TẮC HAI PHẢI, BA KHÔNG")
sfx("chapter_sting", -0.1, -5)
sfx("phone_ring", 0.25, -4, dur=0.8)
blink("assets/c11_nam_blink.jpg", [0.147, 0.197, 0.309, 0.359], first_offset=1.7, interval=3.9, layer="fg")
mouth("thang_tun", ["l28_nam"], [0.191, 0.330, 0.311, 0.480], "mid",
      "assets/c11_nam_mouth_closed.jpg", "assets/c11.jpg", "assets/c11_nam_mouth_open.jpg", layer="fg",
      round_image="assets/c11_nam_mouth_round.jpg")
fx({"type": "phone_waveform", "speaker": "anh_hai", "line_ids": ["l29_minh_p"],
    "start": 182.6, "end": 188.0, "pos": [0.56, 0.72], "size": [0.25, 0.058],
    "color": [255, 95, 85], "label": "ANH MINH · CẢN KÝ GẤP"})
fx({"type": "color_mood", "mood": "cold_suspicion", "strength": 0.24, "vignette": 0.12, "grain": 0.006})
beat(0.95)
line("l28_nam", "NAM",
     "Alo anh Minh! Em đang công chứng bán xe máy. Khách chốt nhanh, nhờ người thân đứng tên hộ!",
     "vui vẻ gọi khoe anh họ ngay trước khi ký")
line("l29_minh_p", "MINH_P",
     "Khoan ký! Dừng lại liền! Anh mới dính bẫy tam giác kẹt cứng bốn lăm triệu đây nè!",
     "quát gấp qua điện thoại để chặn ngay lập tức",
     sub="Khoan ký! Dừng lại liền! Anh mới dính bẫy tam giác kẹt cứng 45 triệu đây nè!")

amb("street", -4.5); bgm("action_climax", -3.2)
scene("s12_minh_warns_rule", "assets/c12.jpg", "drift_up_breathe", beat_type="climax", level="C",
      intent="Whip Pan sang Anh Minh giơ 2 ngón tay dặn nguyên tắc 2 Phải: chớp mắt & chép miệng 4 trạng thái + Chromatic Pulse + High Tension",
      tr="whip_pan_left", trd=0.28)
mark("two_musts")
sfx("low_accent", 0.15, -4.5)
blink("assets/c12_minh_blink.jpg", [0.635, 0.192, 0.791, 0.344], first_offset=1.6, interval=3.8)
mouth("anh_hai", ["l30_minh", "l31_minh"], [0.659, 0.309, 0.781, 0.460], "mid",
      "assets/c12_minh_mouth_closed.jpg", "assets/c12.jpg", "assets/c12_minh_mouth_open.jpg",
      round_image="assets/c12_minh_mouth_round.jpg")
fx({"type": "chromatic_pulse", "at": 188.70, "dur": 0.26, "shift_px": 5, "zoom_blur": 0.018})
fx({"type": "color_mood", "mood": "high_tension", "strength": 0.32, "vignette": 0.14, "grain": 0.008})
bubble("NGUYÊN TẮC 2 PHẢI", "1. Ai ký HĐ, người đó chuyển · 2. Ghi tên, mua xe, BSX, ngày HĐ",
       side="left", y=260, stamp="CHẶN BẪY NGAY", dur=5.2, offset=0.15)
beat(0.3)
line("l30_minh", "MINH",
     "Ai ký hợp đồng chính người đó chuyển tiền. Tuyệt đối không nhận tài khoản thứ ba chuyển giùm!",
     "dặn nhanh, rõ từng chữ đầy khẩn thiết")
line("l31_minh", "MINH",
     "Nội dung ghi rõ họ tên, mua xe, biển số và ngày hợp đồng. Lệch tên là dừng ký!",
     "nhấn mạnh nguyên tắc sống còn", pause=0.15)

amb("crowd", -5.5); bgm("action_climax", -2.5)
scene("s13_nam_tests_proxy", "assets/c13.jpg", "push_in", beat_type="climax", level="B",
      intent="Cảnh đối mặt đinh: 2.5D Parallax + Rack Focus + Breathing + Nam chép miệng 4 trạng thái & người mua hộ chép miệng đôi trên fg",
      tr="whip_pan_right", trd=0.28,
      parallax={
          "camera": "push_in",
          "dolly": [1.01, 1.07],
          "shift_x": [0.0, 0.0],
          "shift_y": [0.0, 0.0],
          "focus": [0.50, 0.44],
          "strength": 0.84,
          "easing": "smoothstep",
          "layers": [
              {"role": "bg", "image": "assets/s13_bg.jpg", "depth": 0.44, "blur_from": 0.4, "blur_to": 2.6, "blur_at": 203.0, "blur_dur": 4.5},
              {"role": "fg", "image": "assets/s13_fg.png", "depth": 1.22, "breathe_y": 1.4, "breathe_period": 3.6},
          ],
      })
mark("confrontation")
sfx("riser", 0.0, -4.5, dur=0.8)
blink("assets/c13_nam_blink.jpg", [0.231, 0.161, 0.354, 0.291], first_offset=2.1, interval=4.3, layer="fg")
blink("assets/c13_proxy_blink.jpg", [0.737, 0.265, 0.839, 0.365], first_offset=1.4, interval=3.8, layer="fg")
mouth("thang_tun", ["l32_nam", "l34_nam"], [0.248, 0.272, 0.337, 0.407], "mid",
      "assets/c13_nam_mouth_closed.jpg", "assets/c13.jpg", "assets/c13_nam_mouth_open.jpg", layer="fg",
      round_image="assets/c13_nam_mouth_round.jpg")
mouth("ke_ngot_ngao_nu", ["l33_proxy_nu"], [0.742, 0.350, 0.832, 0.469], "closed",
      "assets/c13.jpg", "assets/c13_proxy_mouth_mid.jpg", "assets/c13_proxy_mouth_open.jpg", layer="fg")
fx({"type": "color_mood", "mood": "high_tension", "strength": 0.28, "vignette": 0.14, "grain": 0.008})
beat(0.3)
line("l32_nam", "NAM",
     "Hợp đồng tên chị nên chị dùng đúng tài khoản tên chị chuyển, ghi rõ biển số với ngày hợp đồng nha!",
     "bình tĩnh dứt khoát, nhìn thẳng đối phương")
line("l33_proxy_nu", "PROXY_NU",
     "Ủa… chồng chị ở xa chuyển giùm cho nhanh, tiền vô rồi cần gì rắc rối?",
     "hơi khựng lại nhưng cố cười trấn an")
line("l34_nam", "NAM",
     "Không được chị. Lệch tên hay mập mờ em không ký, tiền lỡ vô em cũng ra ngân hàng hoàn lại.",
     "kiên quyết đóng chặt mọi kẽ hở", pause=0.15)

scene("s14_scammer_flees", "assets/c14.jpg", "pull_out_breathe", beat_type="aftermath", level="C",
      intent="Zoom Punch giải tỏa khi người mua hộ vội rút lui + Nam thở phào với khẩu hình & chớp mắt đôi + hạt nắng ấm",
      tr="zoom_punch", trd=0.22, shake=0.14)
fx({"type": "chromatic_pulse", "at": 218.90, "dur": 0.26, "shift_px": 5, "zoom_blur": 0.018})
fx({"type": "ambient_particles", "count": 18, "opacity": 0.22, "color": [255, 240, 195], "drift_dir": "float", "seed": 94})
fx({"type": "color_mood", "mood": "warm_daily", "strength": 0.54, "vignette": 0.08, "grain": 0.0})
sfx("impact", 0.0, -2.5)
sfx("footsteps", 0.35, -4, dur=1.1)
blink("assets/c14_nam_blink.jpg", [0.151, 0.192, 0.309, 0.319], first_offset=2.2, interval=4.2)
blink("assets/c14_proxy_blink.jpg", [0.764, 0.307, 0.846, 0.426], first_offset=1.3, interval=3.7)
mouth("ke_ngot_ngao_nu", ["l35_proxy_nu"], [0.764, 0.367, 0.838, 0.468], "mid",
      "assets/c14_proxy_mouth_closed.jpg", "assets/c14.jpg", "assets/c14_proxy_mouth_open.jpg")
mouth("thang_tun", ["l36_nam"], [0.185, 0.327, 0.307, 0.480], "closed",
      "assets/c14.jpg", "assets/c14_nam_mouth_mid.jpg", "assets/c14_nam_mouth_open.jpg")
beat(0.35)
line("l35_proxy_nu", "PROXY_NU",
     "À… thôi để chị ra ngoài gọi hỏi lại chồng chút nha!",
     "lúng túng chột dạ, vội gom giấy đứng dậy đi thẳng")
line("l36_nam", "NAM",
     "Đi mất tiêu rồi! May gọi kịp anh Minh… suýt chút nữa mất trắng chiếc xe!",
     "thở phào nhẹ nhõm nhìn theo bóng người kia rời khỏi cửa", pause=0.2)

amb("room_tone", -5.0); bgm("investigative_story", SILENT)
scene("s15_outro_still", "assets/c15.jpg", "static_hold", beat_type="aftermath", level="A",
      intent="Khoảng lặng tĩnh trên bàn tiệm điện lạnh chuyển nhịp sang thẻ tổng kết",
      tr="fade_black", trd=0.4)
beat(0.8)

# ---- THẺ NHỚ KỸ (< 10 GIÂY) ----
amb("room_tone", -5.0); bgm("warm_outro", -4.2)
scene("s16_red_flags", EP01B + "scene18.jpg", "static_hold", beat_type="information", level="A",
      intent="Giữ khung tĩnh sạch để người xem đọc trọn vẹn bảng 5 nguyên tắc 2 Phải – 3 Không",
      tr="fade_black", trd=0.4)
mark("rf_start")
sfx("bank_ting", 0.0, -5)
line("l37_narr", "N",
     "Tiền nổi rồi vẫn mất nếu lệch tên. Ai ký hợp đồng người đó chuyển, ghi rõ mục đích.")
beat(0.5)
mark("rf_end")

# ---- KẾT MỞ ĐƯỜNG DÂY NGẦM (CỘC GỌN SẮC LẠNH · HỘI TỤ MẮT XÍCH EP08 & EP08b · LIÊN ĐỚI MỜ CHỊ HAI EP04) ----
amb("rain", -3.2); bgm("tension_drone", -2.4)
scene("s17a_syndicate_grid", "assets/c16a.jpg", "push_in", beat_type="suspicion", level="C",
      intent="Luma Wipe sang lưới 4 ô đêm mưa hội tụ đường dây EP08 & EP08b: lớp mưa rain_layer + sóng âm đường dây + Noir Evidence",
      tr="luma_wipe", trd=0.38)
fx({"type": "rain_layer", "opacity": 0.26, "density": 0.85, "angle_deg": -14.0, "speed": 1120.0, "seed": 97})
fx({"type": "phone_waveform", "speaker": "chu_no", "line_ids": ["l38a_ke_p", "l38b_long_p", "l38c_proxy_p"],
    "start": 239.0, "end": 249.2, "pos": [0.24, 0.50], "size": [0.25, 0.056],
    "color": [95, 225, 245], "label": "ĐƯỜNG DÂY · BÁO ĐỘNG"})
fx({"type": "color_mood", "mood": "noir_evidence", "strength": 0.60, "vignette": 0.26, "grain": 0.016})
mark("boss_coda")
sfx("phone_vibrate", 0.1, -5, dur=0.5)
detail("screen_glow", offset_start=0.15, end_scene=True, pos=[0.21, 0.35], radius=[0.14, 0.14],
       color=[95, 210, 255], intensity=0.24, mode="pulse", fade=0.35)
detail("screen_glow", offset_start=0.25, end_scene=True, pos=[0.68, 0.83], radius=[0.16, 0.12],
       color=[95, 225, 255], intensity=0.26, mode="pulse", fade=0.35)
beat(0.3)
line("l38a_ke_p", "BUYER_MSG",
     "Bên ông Đạt với Khang… công an vào cuộc.",
     "báo cáo cộc gọn, lạnh tĩnh qua điện thoại từ phòng tối EP08", pause=0.12)
line("l38b_long_p", "LONG_P",
     "Chiếc tay ga đẩy xong. Số hủy sạch.",
     "ngắn gọn, dứt khoát qua điện thoại", pause=0.12)
line("l38c_proxy_p", "PROXY_NU_P",
     "Khu này động. Chủ xe đòi chính chủ chuyển.",
     "gấp gáp, cộc gọn báo động qua điện thoại", pause=0.2)

scene("s17b_boss_order", "assets/c16b.jpg", "push_in", beat_type="ending", level="B",
      intent="Kết mở 2.5D lạnh sống lưng + Rack Focus + Breathing + mưa đêm rain_layer + ánh đèn xe quét + Chromatic Pulse cú chốt 3 nhịp",
      tr="whip_pan_left", trd=0.25,
      parallax={
          "camera": "push_in",
          "dolly": [1.02, 1.10],
          "shift_x": [0.0, 0.0],
          "shift_y": [0.0, -3.0],
          "focus": [0.62, 0.44],
          "strength": 0.88,
          "easing": "ease_out",
          "layers": [
              {"role": "bg", "image": "assets/s16b_bg.jpg", "depth": 0.42, "blur_from": 0.4, "blur_to": 3.2, "blur_at": 250.2, "blur_dur": 3.2},
              {"role": "fg", "image": "assets/s16b_fg.png", "depth": 1.28, "breathe_y": 1.4, "breathe_period": 3.8},
          ],
      })
fx({"type": "rain_layer", "opacity": 0.28, "density": 0.90, "angle_deg": -12.0, "speed": 1150.0, "seed": 98})
fx({"type": "light_sweep", "mode": "light", "color": [125, 215, 240], "intensity": 0.16, "width": 0.22, "angle_deg": -20.0, "repeat": 1})
fx({"type": "chromatic_pulse", "at": 253.75, "dur": 0.28, "shift_px": 7, "zoom_blur": 0.025})
fx({"type": "color_mood", "mood": "noir_evidence", "strength": 0.65, "vignette": 0.28, "grain": 0.018})
sfx("heartbeat", 0.0, -5, dur=0.9)
detail("screen_glow", offset_start=0.05, end_scene=True, space="frame", pos=[0.31, 0.79], radius=[0.16, 0.14],
       color=[95, 210, 235], intensity=0.22, mode="pulse", fade=0.30)
detail("light_shift", offset_at=0.20, dur=0.50, brightness=0.88, tint_rgb=[95, 145, 195], tint_strength=0.14)
beat(0.35)
line("l39_boss_nu", "BOSS_NU",
     "Bỏ xe. Dời vùng. Sang kèo đất.",
     "lạnh băng, cắt gọn ba nhịp dứt khoát, không chút cảm xúc — gợi âm hưởng 'Cứ để đó!' ở EP04", pause=0.15)

sfx("impact", 0.0, -1.5)
scene("s18_black_cut", "assets/c17.jpg", "static_hold", beat_type="ending", level="A",
      intent="Cú cắt đen đột ngột giữ dư âm lạnh sau 3 nhịp mệnh lệnh",
      tr="fade_black", trd=0.08)
beat(1.3)

# ---- DISCLAIMER ----
amb("room_tone", -6.0); bgm("warm_outro", -7.5)
scene("s19_disclaimer", EP01B + "scene18.jpg", "static_hold", beat_type="ending", level="A",
      intent="Khung tĩnh sạch hiển thị lưu ý miễn trừ trách nhiệm cuối phim",
      tr="fade_black", trd=0.35)
mark("disc_start")
beat(4.0)

# ================================================================ COMPILE
t = 0.0
scenes, dialogue, bubbles, foley, chapters = [], [], [], [], []
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
    elif kind == "fx":
        pending_fx.append((len(scenes) - 1, "raw_fx", dict(d)))
    elif kind == "sfx_abs":
        f = {"preset": d["preset"], "at": round(d["at"], 2), "gain_db": d["gain"]}
        if d["dur"]:
            f["dur"] = d["dur"]
        foley.append(f)
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
        if item.get("round_image"):
            fx_obj["round_image"] = item["round_image"]
        if item.get("layer"):
            fx_obj["layer"] = item["layer"]
        dfx.append(fx_obj)
    elif fx_kind == "raw_fx":
        dfx.append(item)
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
        if item.get("round_image"):
            fx_obj["round_image"] = item["round_image"]
        if item.get("layer"):
            fx_obj["layer"] = item["layer"]
        dfx.append(fx_obj)
    elif fx_kind == "raw_fx":
        dfx.append(item)
    elif fx_kind == "detail":
        anchor = float(item["anchor"])
        fx_obj = {"type": item["type"], **item["kwargs"]}
        if item["offset_start"] is not None:
            fx_obj["start"] = round(anchor + float(item["offset_start"]), 2)
        if item["offset_end"] is not None:
            fx_obj["end"] = round(anchor + float(item["offset_end"]), 2)
        elif item["end_scene"]:
            fx_obj["end"] = round(sc_e, 2)
        if item["offset_at"] is not None:
            fx_obj["at"] = round(anchor + float(item["offset_at"]), 2)
        if item["dur"] is not None:
            fx_obj["dur"] = float(item["dur"])
        # Convert relative end on light_shift if passed in kwargs as small offset
        if item["type"] == "light_shift" and "end" in item["kwargs"] and item["offset_at"] is not None:
            fx_obj["end"] = round(anchor + float(item["kwargs"]["end"]), 2)
        dfx.append(fx_obj)


def mmss(x: float) -> str:
    return f"{int(x // 60):02d}:{int(x % 60):02d}"


_desc = [(0.0, "Mở đầu – Tiền 45 triệu đã nổi, công chứng rồi sao vẫn mất?")]
_desc += [(c["start"] - 0.2, f"{c['kicker'].split('·')[0].strip().title()} – {c['title'].capitalize()}")
          for c in chapters if c["kicker"]]
_desc += [(marks["rf_start"], "Nhớ kỹ – Nguyên tắc 2 Phải, 3 Không khi bán xe, bán đất")]
desc_chapters = "\n".join(f"{mmss(max(0.0, s))} {label}" for s, label in sorted(_desc))

foley.sort(key=lambda item: float(item["at"]))

episode = {
    "episode_id": "EP08b",
    "slug": "TienNoiRoiTenLaiKhac",
    "title": "Tiền nổi rồi, tên lại khác",
    "version": "v3-level3-full-abc-staging",
    "motion_upgrade": "level3",
    "scam_family": "VAR-MITM-02 / VAR-COM-04 · TRIANGULATION-PAYMENT-MISMATCH – Nửa bên kia dòng tiền 45 triệu từ EP08: bẫy tam giác đẩy tiền của nạn nhân vụ lừa khác vào tài khoản người bán xe máy công chứng",
    "duration_sec": total,
    "visual_style_lock": (
        "Horizontal 16:9 widescreen (1920x1080), semi-realistic cinematic 2D anime illustration, "
        "contemporary Southern Vietnam urban setting, naturalistic dramatic lighting, clean bottom 15% for subtitles, "
        "no text, no letters, no numbers, no license plates, no logos, no real app interface, no real uniforms"
    ),
    "hook": {
        "kicker": "12:05 TRƯA · CÔNG CHỨNG THẬT",
        "title": "TIỀN NỔI RỒI, TÊN LẠI KHÁC",
        "start": 0.4,
        "end": 5.0,
    },
    "chapters": chapters,
    "scenes": scenes,
    "dialogue": dialogue,
    "chat_bubbles": bubbles,
    "callouts": [],
    "red_flags": {
        "title": "NHỚ KỸ – NGUYÊN TẮC 2 PHẢI, 3 KHÔNG",
        "start": marks["rf_start"],
        "end": marks["rf_end"],
        "stagger_sec": 0.42,
        "items": [
            "PHẢI TRÙNG KHỚP 100%: Ai đứng tên ký hợp đồng mua bán thì chính chủ tài khoản đó chuyển tiền",
            "PHẢI GHI RÕ NỘI DUNG: Họ tên người mua + thanh toán mua xe + biển số + theo hợp đồng ngày ký",
            "KHÔNG NHẬN NGƯỜI THỨ BA CHUYỂN HỘ: Từ chối mọi lý do tài khoản người thân hay công ty chuyển giùm",
            "LỆCH TÊN HAY MẬP MỜ LÀ DỪNG KÝ NGAY: Tiền đã lỡ vào thì không giao xe và phối hợp ngân hàng hoàn trả",
            "CẢNH GIÁC KHÁCH CHỐT QUÁ DỄ: Không mặc cả, né gặp mặt, nhờ người khác đứng tên mua hộ",
        ],
        "action": "Nếu đã lỡ giao tài sản và nhận báo tiền từ vụ lừa khác, giữ nguyên tiền trong tài khoản, gom hợp đồng, sao kê và tin nhắn trình báo công an ngay.",
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
            {"start": marks["hook_freeze"] - 0.2, "end": marks["hook_freeze"] + 2.4, "bgm_db": -12, "amb_db": -8},
            {"start": marks["money_mismatch"] - 0.2, "end": marks["money_mismatch"] + 5.0, "bgm_db": -10, "amb_db": -7},
            {"start": marks["ep08_twist"] - 0.2, "end": marks["ep08_twist"] + 6.0, "bgm_db": -12, "amb_db": -8},
            {"start": marks["paper_trap"] - 0.2, "end": marks["paper_trap"] + 8.0, "bgm_db": -11, "amb_db": -7},
            {"start": marks["triangle_reveal"] - 0.2, "end": marks["triangle_reveal"] + 12.0, "bgm_db": -11, "amb_db": -8},
            {"start": marks["confrontation"] - 0.2, "end": marks["confrontation"] + 14.0, "bgm_db": -11, "amb_db": -7},
            {"start": marks["boss_coda"] - 0.2, "end": marks["disc_start"] - 0.2, "bgm_db": -10, "amb_db": -7},
            {"start": marks["disc_start"], "end": total - 0.05},
        ],
    },
    "forbidden_terms": [],
    "publish": {
        "titles": [
            "Tiền Nổi Đủ 45 Triệu Mới Ký Công Chứng Bán Xe Máy – Sao Hai Ngày Sau Vẫn Kẹt Cứng? | Bóc Trần Lừa Đảo",
            "Tiền Nổi Rồi, Tên Lại Khác: Cái Bẫy Ngay Tại Phòng Công Chứng Đông Người | Bóc Trần Lừa Đảo",
            "Bán Xe Máy Thấy Tiền Nổi Đủ 45 Triệu Mới Giao Xe – Sự Thật Đằng Sau Dòng Tiền Lạ | Bóc Trần Lừa Đảo",
        ],
        "description": (
            "Đúng 12 giờ 05 trưa tại phòng công chứng đông người, chủ xe máy thấy tiền thật nổi đủ 45 triệu trong tài khoản mới đặt bút ký giao xe — "
            "vậy mà hai ngày sau lại nhận thông báo khoản tiền đó chảy thẳng từ một vụ lừa đảo khác.\n\n"
            "Ghi nhớ nguyên tắc 2 Phải – 3 Không khi mua bán xe máy, ô tô, đất đai: ai ký hợp đồng thì chính người đó chuyển tiền, "
            "và nội dung chuyển khoản phải ghi rõ họ tên, tài sản/biển số cùng ngày hợp đồng.\n\n"
            "⏱️ Các hồi trong phim:\n" + desc_chapters
        ),
        "pinned_comment": (
            "📌 Tới Hồi 3 bạn có giật mình nhận ra cái tên 'Khang' và câu gọi 'anh Đạt ơi' nối thẳng từ tập trước không? "
            "Chia sẻ cảm nhận và kinh nghiệm đi công chứng mua bán xe bên dưới nhé!\n"
            "⚠️ Lưu ý: Không đăng SĐT, STK hay tên người thật; tuyệt đối cảnh giác mọi bình luận mời chào dịch vụ 'hỗ trợ lấy lại tiền'."
        ),
        "hashtags": ["#bóctrầnlừađảo", "#cảnhgiáclừađảo", "#vạnchuyện", "#bẫytamgiác", "#muabánxe"],
        "tags": [
            "cảnh giác lừa đảo", "bóc trần lừa đảo", "vạn chuyện", "lừa đảo tam giác",
            "lệch dòng tiền giao dịch", "lừa đảo mua bán xe công chứng", "nguyên tắc 2 phải 3 không",
            "rửa tiền mua xe máy", "an toàn giao dịch",
        ],
        "category": "Education (Giáo dục)",
        "playlist": "Hồ Sơ Bóc Trần Lừa Đảo – Phim Dài Chuyên Sâu",
        "thumbnail_sec": round(marks["confrontation"] + 1.5, 2),
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
