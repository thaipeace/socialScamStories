# -*- coding: utf-8 -*-
"""Builder cho EP08 (factory619 · 9:16 Short) – Bẫy biên lai báo nghẽn mạng (v4 – nhịp gọn sắc, Khung 4 câm lặng, chỉ bóc trần ở Khung 6).

Chạy lại sau Gate 2 để tự động dàn timeline khớp thời lượng WAV thật (Real-TTS Retiming):
    python factory619/materialAndDraft/EP08/source/build_episode.py
"""
from __future__ import annotations

import json
from pathlib import Path

EP_DIR = Path(__file__).resolve().parent.parent
TTS_MANIFEST = EP_DIR / "audio" / "tts" / "tts_manifest_gate2.json"
OUT = EP_DIR / "episode.json"

real: dict[str, float] = {}
if TTS_MANIFEST.is_file():
    for ln in json.loads(TTS_MANIFEST.read_text(encoding="utf-8")).get("lines", []):
        dur_s = ln.get("duration_sec") or ln.get("metrics", {}).get("duration_sec")
        if ln.get("engine") != "placeholder" and dur_s:
            real[ln["line_id"]] = float(dur_s)

STYLE_HR_CALM = (
    "Giọng nữ miền Nam Sài Gòn 30 tuổi, giữ cố định một âm sắc tự nhiên, lịch sự chuyên nghiệp "
    "như người thuê việc vừa duyệt bài xong, nhịp nói gọn gàng, rõ chữ."
)
STYLE_HR_PUSH = (
    "Giọng nữ miền Nam Sài Gòn 30 tuổi, giữ cố định âm sắc, điềm nhiên chuyên nghiệp khi hướng dẫn "
    "nhưng giục khéo tạo áp lực thời gian, nhịp nhanh gọn, rõ chữ."
)
STYLE_HR_URGENT = (
    "Giọng nữ miền Nam Sài Gòn 30 tuổi, giữ cố định âm sắc, chuyển sang gấp gáp thúc giục dồn dập "
    "vì sắp hết giờ giải ngân, nhịp nhanh, sắc, rõ chữ."
)
STYLE_TUNG_TIRED = (
    "Giọng nam thanh niên miền Nam Sài Gòn 20 tuổi, giữ cố định một âm sắc trẻ trung tự nhiên, "
    "hơi mệt sau ca làm khuya, thắc mắc ngắn gọn, rõ chữ."
)
STYLE_TUNG_RUSH = (
    "Giọng nam thanh niên miền Nam Sài Gòn 20 tuổi, giữ cố định âm sắc, luống cuống vội vàng "
    "bấm xác nhận cho kịp giờ, nhịp nhanh gọn, rõ chữ."
)
STYLE_TUNG_SHOCK = (
    "Giọng nam thanh niên miền Nam Sài Gòn 20 tuổi, giữ cố định âm sắc nhưng bàng hoàng sững sờ, "
    "thảng thốt nghẹn giọng khi thấy tài khoản bị trừ sạch tiền và gọi lại bị chặn số, rõ chữ."
)
STYLE_BOC_TRAN_SHARP = (
    "Giọng nam trung niên miền Nam Sài Gòn, trầm tĩnh, khách quan, sắc lạnh vạch trần bản chất cơ chế, "
    "nhịp gọn dứt khoát, rõ chữ, tuyệt đối không kéo dài giọng hay rao giảng dạy đời."
)

# (id, speaker, text, est_dur, style, af)
LINES = [
    ("l1", "ke_ngot_ngao_nu", "Bài đạt rồi nha! Chị mới chuyển ba triệu rưỡi, biên lai đó em.", 3.6, STYLE_HR_CALM, "phone"),
    ("l2", "thang_tun", "Ủa sao máy em chưa báo tiền vô chị?", 2.4, STYLE_TUNG_TIRED, None),
    ("l3", "ke_ngot_ngao_nu", "Cuối năm nghẽn liên ngân hàng. Bấm link xác nhận nhận tiền đi, quá giờ nó hoàn lệnh đó.", 4.9, STYLE_HR_PUSH, "phone"),
    ("l4", "ke_ngot_ngao_nu", "Mã giải ngân về máy rồi kìa, nhập lẹ đi em, sắp hết giờ!", 3.7, STYLE_HR_URGENT, "phone"),
    ("l5", "thang_tun", "Dạ có mã rồi, em bấm liền!", 2.1, STYLE_TUNG_RUSH, None),
    ("l6", "thang_tun", "Ủa, sao lại trừ sạch tiền của em?! Alo, chặn số mất rồi!", 4.1, STYLE_TUNG_SHOCK, None),
    ("l7", "nguoi_boc_tran", "Biên lai báo nghẽn chỉ là mồi nhử để dẫn bạn vào trang giả.", 3.9, STYLE_BOC_TRAN_SHARP, None),
    ("l8", "nguoi_boc_tran", "Link và mã OTP nhận lương đó thực chất trao quyền cho kẻ gian rút cạn tài khoản.", 4.9, STYLE_BOC_TRAN_SHARP, None),
]

GAP = 0.24
LEAD = 0.32


def dur_of(lid: str, est_d: float) -> float:
    return real.get(lid, est_d)


dialogue = []


def place(lid: str, spk: str, text: str, est_d: float, style: str | None, af: str | None, start_t: float) -> float:
    d = dur_of(lid, est_d)
    item: dict = {
        "id": lid,
        "speaker": spk,
        "start": round(start_t, 2),
        "window": round(max(d, est_d) + 1.5, 2),
        "text": text,
    }
    if style:
        item["style"] = style
    if af:
        item["af"] = af
    dialogue.append(item)
    return start_t + d


# Khung 1: Việc thật, biên lai mồi (l1, l2)
s1_start = 0.0
end_l1 = place(*LINES[0], s1_start + 0.38)
end_l2 = place(*LINES[1], end_l1 + GAP)
s1_end = round(end_l2 + 0.35, 2)

# Khung 2 (CAO TRÀO NHỎ): Bấm link & gõ mật khẩu đăng nhập (l3 + nhịp typing/glitch cuối cảnh)
s2_start = s1_end
end_l3 = place(*LINES[2], s2_start + LEAD)
s2_end = round(end_l3 + 1.15, 2)  # Dành ~1.15s cuối cảnh cho tiếng gõ mật khẩu & glitch sập bẫy bước 1

# Khung 3: Gộp nhịp đếm ngược ép OTP (l4, l5)
s3_start = s2_end
end_l4 = place(*LINES[3], s3_start + LEAD)
end_l5 = place(*LINES[4], end_l4 + 0.20)
s3_end = round(end_l5 + 0.28, 2)

# Khung 4 (CAO TRÀO LỚN): 5.80s KHÔNG LỜI THOẠI – thuần biến động số dư trừ sạch tiền & văng tài khoản
s4_start = s3_end
s4_dur = 5.80
s4_end = round(s4_start + s4_dur, 2)

# Khung 5: Dư chấn đêm khuya – chặn số & thu hồi biên lai (l6)
s5_start = s4_end
end_l6 = place(*LINES[5], s5_start + 0.45)
s5_end = round(end_l6 + 0.75, 2)

# Khung 6: CHỈ BÓC TRẦN Ở KHUNG 6 (l7, l8) -> nối thẳng sang Thẻ NHỚ KỸ + Disclaimer
s6_start = s5_end
end_l7 = place(*LINES[6], s6_start + 0.40)
end_l8 = place(*LINES[7], end_l7 + 0.26)
rf_start = round(end_l8 + 0.42, 2)

# Bảo đảm tổng thời lượng nằm gọn trong khoảng 47.5s – 52.0s (trên ngưỡng min 45.0s của factory619)
rf_dur = 3.80
disc_dur = 2.80
if rf_start + rf_dur + disc_dur < 47.5:
    rf_dur = round(47.5 - rf_start - disc_dur, 2)

rf_end = round(rf_start + rf_dur, 2)
total = round(rf_end + disc_dur, 2)

scenes = [
    {
        "id": "s1_viec_that_bien_lai",
        "image": "assets/scene1.jpg",
        "start": s1_start,
        "end": s1_end,
        "beat_type": "establishing",
        "motion_level": "C",
        "motion_intent": "Đẩy chậm tạo nhịp mở đầu kết hợp chớp mắt tự nhiên, miệng nói khớp WAV thật ở câu l2 và ánh sáng biên lai xanh bật lên",
        "motion": {"preset": "slow_push_in", "scale": [1.02, 1.09], "focus": [[0.50, 0.47], [0.52, 0.44]], "wobble": "breathe", "easing": "ease_out"},
        "detail_fx": [
            {
                "type": "eye_blink",
                "image": "assets/scene1_blink.jpg",
                "region": [0.522, 0.357, 0.698, 0.399],
                "feather": 0.008,
                "times": [1.85, 4.55, 7.65],
                "close_dur": 0.055,
                "hold_dur": 0.045,
                "open_dur": 0.085,
            },
            {
                "type": "mouth_sync",
                "speaker": "thang_tun",
                "region": [0.541, 0.415, 0.663, 0.455],
                "feather": 0.008,
                "closed_image": "assets/scene1_mouth_closed.jpg",
                "mid_image": "assets/scene1.jpg",
                "open_image": "assets/scene1_mouth_open.jpg",
                "fps": 12,
                "thresh_mid": 0.14,
                "thresh_open": 0.68,
            },
            {
                "type": "screen_glow",
                "pos": [0.68, 0.50],
                "radius": [0.22, 0.14],
                "color": [95, 245, 175],
                "intensity": 0.24,
                "mode": "turn_on",
                "start": 0.12,
                "end": s1_end,
                "fade": 0.35,
            },
        ],
    },
    {
        "id": "s2_cao_trao_nho_link",
        "image": "assets/scene2.jpg",
        "start": s2_start,
        "end": s2_end,
        "beat_type": "suspicion",
        "motion_level": "B",
        "motion_intent": "Parallax 2.5D hai lớp kết hợp nhịp thở thân trên, chớp mắt khóa cứng theo layer FG và ánh sáng link xanh cyan chớp khi glitch",
        "motion": {"preset": "slow_push_in", "scale": [1.03, 1.10], "focus": [[0.50, 0.46], [0.50, 0.43]], "wobble": "none"},
        "parallax": {
            "camera": "push_in",
            "dolly": [1.03, 1.10],
            "shift_x": [0.0, 0.0],
            "shift_y": [0.0, -6.0],
            "focus": [0.50, 0.44],
            "strength": 0.90,
            "easing": "ease_out",
            "layers": [
                {"role": "bg", "image": "assets/s2_bg.jpg", "depth": 0.42, "blur": 0.8},
                {"role": "fg", "image": "assets/s2_fg.png", "depth": 1.24, "breathe_y": 2.3, "breathe_scale": 0.005, "breathe_period": 3.6},
            ],
        },
        "detail_fx": [
            {
                "type": "eye_blink",
                "image": "assets/scene2_blink.jpg",
                "region": [0.307, 0.240, 0.691, 0.297],
                "feather": 0.010,
                "times": [round(s2_start + 1.80, 2), round(s2_start + 4.75, 2)],
                "close_dur": 0.055,
                "hold_dur": 0.045,
                "open_dur": 0.085,
                "layer": "fg",
            },
            {
                "type": "screen_glow",
                "space": "frame",
                "pos": [0.56, 0.69],
                "radius": [0.28, 0.18],
                "color": [95, 235, 255],
                "intensity": 0.24,
                "mode": "pulse",
                "start": round(s2_start + 0.25, 2),
                "end": s2_end,
                "fade": 0.30,
            },
            {
                "type": "light_shift",
                "at": round(s2_end - 0.38, 2),
                "dur": 0.12,
                "end": round(s2_end - 0.08, 2),
                "end_dur": 0.12,
                "brightness": 1.14,
                "tint_rgb": [140, 240, 255],
                "tint_strength": 0.10,
            },
        ],
        "transition_in": {"type": "dissolve", "dur": 0.28},
    },
    {
        "id": "s3_ep_ma_otp",
        "image": "assets/scene3.jpg",
        "start": s3_start,
        "end": s3_end,
        "beat_type": "anomaly",
        "motion_level": "C",
        "motion_intent": "Trượt lên đổi nhịp (tránh lặp zoom-in) kèm chớp mắt căng thẳng, miệng nói gấp khớp câu l5 và ánh sáng đồng hồ đếm ngược đỏ cam",
        "motion": {"preset": "drift_up", "scale": [1.05, 1.06], "focus": [[0.50, 0.49], [0.50, 0.44]], "wobble": "breathe", "easing": "smoothstep"},
        "detail_fx": [
            {
                "type": "eye_blink",
                "image": "assets/scene3_blink.jpg",
                "region": [0.307, 0.240, 0.691, 0.297],
                "feather": 0.010,
                "times": [round(s3_start + 1.25, 2), round(s3_start + 3.35, 2)],
                "close_dur": 0.050,
                "hold_dur": 0.040,
                "open_dur": 0.075,
            },
            {
                "type": "mouth_sync",
                "speaker": "thang_tun",
                "region": [0.376, 0.355, 0.615, 0.414],
                "feather": 0.010,
                "closed_image": "assets/scene3_mouth_closed.jpg",
                "mid_image": "assets/scene3.jpg",
                "open_image": "assets/scene3_mouth_open.jpg",
                "fps": 12,
                "thresh_mid": 0.14,
                "thresh_open": 0.68,
            },
            {
                "type": "screen_glow",
                "pos": [0.54, 0.77],
                "radius": [0.24, 0.16],
                "color": [255, 110, 65],
                "intensity": 0.28,
                "mode": "pulse",
                "start": round(s3_start + 0.12, 2),
                "end": s3_end,
                "fade": 0.25,
            },
        ],
        "transition_in": {"type": "dissolve", "dur": 0.24},
    },
    {
        "id": "s4_cao_trao_lon_cam_lang",
        "image": "assets/scene4.jpg",
        "start": s4_start,
        "end": s4_end,
        "beat_type": "climax",
        "motion_level": "B",
        "motion_intent": "Cao trào câm lặng 2.5D: nhịp thở dồn dập khớp heartbeat, 2 cú shake + chớp đỏ khớp 2 tiếng bank_ting và 1 cái chớp mắt bàng hoàng",
        "motion": {"preset": "tense_push", "scale": [1.06, 1.16], "focus": [[0.50, 0.44], [0.50, 0.40]], "wobble": "tense"},
        "parallax": {
            "camera": "push_in",
            "dolly": [1.04, 1.13],
            "shift_x": [0.0, 0.0],
            "shift_y": [0.0, -8.0],
            "focus": [0.50, 0.42],
            "strength": 0.95,
            "easing": "ease_in",
            "layers": [
                {"role": "bg", "image": "assets/s4_bg.jpg", "depth": 0.42, "blur": 0.8},
                {"role": "fg", "image": "assets/s4_fg.png", "depth": 1.28, "breathe_y": 2.2, "breathe_scale": 0.006, "breathe_period": 2.1},
            ],
        },
        "detail_fx": [
            {
                "type": "eye_blink",
                "image": "assets/scene4_blink.jpg",
                "region": [0.307, 0.240, 0.691, 0.297],
                "feather": 0.010,
                "times": [round(s4_start + 4.15, 2)],
                "close_dur": 0.060,
                "hold_dur": 0.065,
                "open_dur": 0.110,
                "layer": "fg",
            },
            {
                "type": "screen_glow",
                "space": "frame",
                "pos": [0.55, 0.78],
                "radius": [0.28, 0.18],
                "color": [255, 75, 65],
                "intensity": 0.30,
                "mode": "flicker",
                "start": round(s4_start + 0.78, 2),
                "end": s4_end,
                "fade": 0.15,
            },
            {
                "type": "light_shift",
                "at": round(s4_start + 0.78, 2),
                "dur": 0.08,
                "end": round(s4_start + 1.05, 2),
                "end_dur": 0.18,
                "brightness": 1.15,
                "tint_rgb": [255, 95, 85],
                "tint_strength": 0.14,
            },
            {
                "type": "light_shift",
                "at": round(s4_start + 2.25, 2),
                "dur": 0.08,
                "end": round(s4_start + 2.60, 2),
                "end_dur": 0.22,
                "brightness": 1.18,
                "tint_rgb": [255, 80, 75],
                "tint_strength": 0.16,
            },
            {
                "type": "focus_highlight",
                "pos": [0.50, 0.45],
                "radius": [0.40, 0.38],
                "dim_outer": 0.22,
                "start": round(s4_start + 0.80, 2),
                "end": s4_end,
                "fade": 0.30,
            },
        ],
        "transition_in": {"type": "flash_white", "dur": 0.22},
        "shakes": [
            {"at": round(s4_start + 0.78, 2), "amp": 26},
            {"at": round(s4_start + 2.25, 2), "amp": 32},
        ],
    },
    {
        "id": "s5_du_chan_chan_so",
        "image": "assets/scene5.jpg",
        "start": s5_start,
        "end": s5_end,
        "beat_type": "aftermath",
        "motion_level": "C",
        "motion_intent": "Lùi chậm mở không gian phòng trọ lạnh lẽo kèm chớp mắt mệt mỏi, miệng nói thảng thốt khớp l6 và chùng sáng lạnh đúng tiếng call_end",
        "motion": {"preset": "slow_pull_out", "scale": [1.11, 1.02], "focus": [[0.54, 0.43], [0.50, 0.50]], "wobble": "breathe", "easing": "smoothstep"},
        "detail_fx": [
            {
                "type": "eye_blink",
                "image": "assets/scene5_blink.jpg",
                "region": [0.522, 0.357, 0.698, 0.399],
                "feather": 0.008,
                "times": [round(s5_start + 2.35, 2), round(s5_start + 5.35, 2)],
                "close_dur": 0.060,
                "hold_dur": 0.055,
                "open_dur": 0.095,
            },
            {
                "type": "mouth_sync",
                "speaker": "thang_tun",
                "region": [0.541, 0.415, 0.663, 0.455],
                "feather": 0.008,
                "closed_image": "assets/scene5_mouth_closed.jpg",
                "mid_image": "assets/scene5.jpg",
                "open_image": "assets/scene5_mouth_open.jpg",
                "fps": 12,
                "thresh_mid": 0.14,
                "thresh_open": 0.68,
            },
            {
                "type": "light_shift",
                "at": round(max(s5_start + 0.2, end_l6 - 1.35), 2),
                "dur": 0.35,
                "brightness": 0.88,
                "tint_rgb": [175, 205, 235],
                "tint_strength": 0.09,
            },
            {
                "type": "focus_highlight",
                "pos": [0.56, 0.44],
                "radius": [0.38, 0.32],
                "dim_outer": 0.18,
                "start": round(s5_start + 0.30, 2),
                "end": s5_end,
                "fade": 0.45,
            },
        ],
        "transition_in": {"type": "dissolve", "dur": 0.30},
    },
    {
        "id": "s6_boc_tran_cuoi",
        "image": "assets/scene6.jpg",
        "start": s6_start,
        "end": total,
        "beat_type": "ending",
        "motion_level": "C",
        "motion_intent": "Đẩy nhẹ mượt về hình tượng móc câu & biên lai rách kèm ánh sáng cyan nhấp nhô rồi lắng tĩnh sạch sẽ khi thẻ Nhớ kỹ hiện ra",
        "motion": {"preset": "slow_push_in", "scale": [1.02, 1.08], "focus": [[0.50, 0.46], [0.50, 0.42]], "wobble": "none", "easing": "ease_out"},
        "detail_fx": [
            {
                "type": "screen_glow",
                "pos": [0.76, 0.34],
                "radius": [0.22, 0.16],
                "color": [110, 230, 255],
                "intensity": 0.22,
                "mode": "pulse",
                "start": round(s6_start + 0.20, 2),
                "end": round(rf_start - 0.15, 2),
                "fade": 0.40,
            },
        ],
        "transition_in": {"type": "glitch", "dur": 0.30},
    },
]

episode = {
    "episode_id": "EP08",
    "slug": "BayBienLaiNghienMang",
    "title": "Biên lai báo nghẽn mạng – Chỉ bấm nhận lương mà trắng tay",
    "version": "v5-level2-abc-test",
    "motion_upgrade": "level2",
    "scam_family": "ON-03",
    "duration_sec": total,
    "hook": {
        "kicker": "BẪY BIÊN LAI BÁO NGHẼN MẠNG",
        "title": "Làm xong việc thật, chỉ bấm \"nhận lương\" mà bay sạch 18 triệu trong 5 giây!",
        "start": 0.25,
        "end": round(min(4.2, s1_end - 0.3), 2),
    },
    "scenes": scenes,
    "dialogue": dialogue,
    "chat_bubbles": [],
    "callouts": [
        {
            "text": "CHỦ QUAN \"CHỈ NHẬN LƯƠNG\": ĐĂNG NHẬP VÀO LINK LẠ",
            "style": "warn",
            "start": round(s2_start + 0.35, 2),
            "end": round(s2_end - 0.15, 2),
            "y": 190,
        },
        {
            "text": "VĂNG TÀI KHOẢN · 2 LỆNH RÚT SẠCH 18 TRIỆU TRONG TÍCH TẮC!",
            "style": "danger",
            "start": round(s4_start + 0.82, 2),
            "end": round(s4_end - 0.20, 2),
            "y": 190,
        },
    ],
    "red_flags": {
        "start": rf_start,
        "end": rf_end,
        "stagger_sec": 0.4,
        "title": "NHỚ KỸ",
        "items": [
            "Mua hàng hoặc thuê việc thật, gửi ảnh biên lai rồi báo \"nghẽn liên ngân hàng\"",
            "Gửi link xác nhận nhận tiền để lấy mật khẩu & mã OTP kích hoạt thiết bị lạ",
        ],
        "action": "Tiền chuyển thật tự vào tài khoản, không cần link hay OTP · Lỡ bấm: gọi ngân hàng khóa khẩn cấp ngay!",
    },
    "disclaimer": {
        "start": rf_end,
        "end": total,
    },
    "audio": {
        "ambience": [
            {"preset": "night_room", "start": 0.0, "end": total, "gain_db": -3.5},
        ],
        "foley": [
            {"preset": "notification", "at": 0.08, "gain_db": -0.5},
            {"preset": "typing", "at": round(end_l3 - 0.35, 2), "dur": 1.15, "gain_db": 0.5},
            {"preset": "glitch", "at": round(s2_end - 0.38, 2), "dur": 0.45, "gain_db": 0.0},
            {"preset": "notification", "at": round(s3_start + 0.12, 2), "gain_db": 0.5},
            {"preset": "riser", "at": round(max(0.0, s4_start - 1.8), 2), "dur": 1.8, "gain_db": 1.5},
            {"preset": "message_send", "at": round(s4_start + 0.05, 2), "gain_db": 1.0},
            {"preset": "bank_ting", "at": round(s4_start + 0.78, 2), "gain_db": 2.5},
            {"preset": "impact", "at": round(s4_start + 0.80, 2), "dur": 1.5, "gain_db": 2.2},
            {"preset": "bank_ting", "at": round(s4_start + 2.25, 2), "gain_db": 2.8},
            {"preset": "glitch", "at": round(s4_start + 2.28, 2), "dur": 0.85, "gain_db": 1.8},
            {"preset": "heartbeat", "at": round(s4_start + 2.55, 2), "dur": 3.1, "gain_db": 2.2},
            {"preset": "call_end", "at": round(max(s5_start + 0.2, end_l6 - 1.35), 2), "dur": 1.45, "gain_db": 1.8},
            {"preset": "glitch", "at": s6_start, "dur": 0.65, "gain_db": 0.5},
        ],
        "bgm": [
            {"preset": "suspense_pulse", "start": 0.0, "end": s2_end},
            {"preset": "tension_drone", "start": s2_end, "end": s6_start, "gain_db": 1.2},
            {"preset": "action_climax", "start": s6_start, "end": rf_start, "gain_db": 1.2},
            {"preset": "warm_outro", "start": rf_start, "end": total},
        ],
        "duck_extra": [
            # Khoảng lặng nghẹt thở ở Khung 4: dìm sâu nhạc nền để 2 tiếng ting trừ tiền & nhịp tim cắt sắc vào tai
            {"start": round(s4_start - 0.05, 2), "end": s4_end, "bgm_db": -16.5, "amb_db": -8.0},
        ],
    },
    "forbidden_terms": [],
    "publish": {
        "titles": [
            "Làm xong việc thật, chỉ bấm nhận lương mà bay sạch 18 triệu trong 5 giây! #shorts #bóctrầnlừađảo",
            "Bẫy biên lai báo nghẽn liên ngân hàng: Link nhận tiền hay chìa khóa rút cạn ví? #shorts #cảnhgiáclừađảo",
            "Thức khuya làm thêm cuối năm, trắng tay vì 1 đường link xác nhận nhận lương! #shorts #vạnchuyện",
        ],
        "description": (
            "Thức trắng đêm hoàn thành công việc làm thêm cuối năm (hoặc đóng xong đơn hàng online), "
            "bên kia gửi ngay ảnh biên lai đã chuyển khoản nhưng báo \"cuối năm nghẽn liên ngân hàng, lệnh đang treo\".\n\n"
            "Đánh trúng tâm lý chủ quan \"mình chỉ bấm nhận lương chứ đâu có chuyển tiền đi\", kẻ gian đẩy nạn nhân vào một đường link xác nhận nhận tiền. "
            "Thực chất, mật khẩu và mã OTP bạn nhập vào trang giả đó chính là chìa khóa kích hoạt thiết bị lạ để kẻ gian rút sạch tài khoản chỉ trong vài giây!\n\n"
            "✅ Nhớ kỹ: Tiền chuyển khoản thật sẽ tự động vào tài khoản, ngân hàng không bao giờ yêu cầu người nhận bấm link hay nhập mã OTP. "
            "Nếu lỡ bấm và nhập mã, hãy gọi ngay tổng đài chính thức của ngân hàng để khóa khẩn cấp và trình báo cơ quan chức năng nơi gần nhất!"
        ),
        "pinned_comment": (
            "📌 Nhiều người rất cảnh giác chuyện chuyển tiền đi, nhưng lại sập bẫy vì nghĩ \"chỉ bấm link nhận tiền công của mình\". "
            "Nhận tiền thật không bao giờ cần bấm link hay nhập mã OTP — cả nhà chia sẻ cho người bán hàng online và các bạn sinh viên làm thêm cuối năm nhé!"
        ),
        "hashtags": ["#shorts", "#bóctrầnlừađảo", "#cảnhgiáclừađảo"],
        "tags": [
            "biên lai chuyển khoản giả",
            "lừa đảo nghẽn mạng ngân hàng",
            "link xác nhận nhận tiền giả",
            "việc làm thêm cuối năm lừa đảo",
            "shop online biên lai giả",
            "mã otp kích hoạt thiết bị lạ",
            "bóc trần lừa đảo",
            "vạn chuyện",
            "shorts",
        ],
        "category": "Education (Giáo dục)",
        "playlist": "Bóc Trần Lừa Đảo – Kỹ Năng Cảnh Giác & An Toàn Đời Thực",
        "thumbnail_sec": round(s4_start + 2.4, 2),
    },
}

OUT.write_text(json.dumps(episode, ensure_ascii=False, indent=2), encoding="utf-8")
words = sum(len(l["text"].split()) for l in dialogue)
print(f"episode.json [EP08 v4]: {total:.2f}s · {len(scenes)} cảnh · {len(dialogue)} câu · {words} từ · "
      f"{'TTS thật' if real else 'ước tính'} ({len(real)} câu thật)")

