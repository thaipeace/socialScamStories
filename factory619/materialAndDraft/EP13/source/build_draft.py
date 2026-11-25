# -*- coding: utf-8 -*-
"""
Single Source of Truth cho `factory619/materialAndDraft/EP13` (`TaiLieuOnThiMienPhi`).

Chức năng:
  - Biên dịch đầy đủ `episode.json` chuẩn Visual Motion Level 3 (`HRN-MOTION-L3.0`, CHECK 1 → 2 → 3).
  - Nếu đã chạy Gate 2 (`audio/tts/tts_manifest_gate2.json`), tự động căn lại toàn bộ mốc thời gian
    scenes / dialogue / detail_fx / foley / bgm / red_flags / disclaimer theo độ dài WAV thật!
  - Nếu đã chạy `source/face_rois.json` (từ bước bake `03_ENGINE/face_roi_prep.py`), tự động nạp tọa độ
    ROI khóa pixel chính xác tuyệt đối vào các rig `eye_blink` & `mouth_sync`.
"""
from __future__ import annotations

import json
from pathlib import Path

EP_DIR = Path(__file__).resolve().parent.parent
OUT_JSON = EP_DIR / "episode.json"
TTS_MANIFEST = EP_DIR / "audio" / "tts" / "tts_manifest_gate2.json"
FACE_ROIS_FILE = Path(__file__).resolve().parent / "face_rois.json"


def r2(x: float) -> float:
    return round(float(x), 2)


def load_wav_durations() -> dict[str, float]:
    """Đọc độ dài WAV thật sau Gate 2 (nếu có), ngược lại dùng ước lượng hợp lý."""
    defaults = {
        "l1": 4.5,
        "l2": 6.4,
        "l3": 5.5,
        "l4": 5.8,
        "l5": 5.5,
        "l6": 6.1,
        "l7": 5.3,
        "l8": 6.55,
        "l9": 6.4,
        "l10": 5.2,
    }
    if not TTS_MANIFEST.is_file():
        return defaults
    try:
        m = json.loads(TTS_MANIFEST.read_text(encoding="utf-8"))
        for ln in m.get("lines", []):
            lid = ln.get("line_id")
            dur = (ln.get("metrics") or {}).get("duration_sec")
            if lid and dur and float(dur) > 0.5:
                defaults[lid] = float(dur)
    except Exception:
        pass
    return defaults


def load_face_rois() -> dict:
    """Đọc tọa độ ROI đã bake qua `03_ENGINE/face_roi_prep.py` (nếu có)."""
    defaults = {
        "s2_bena_eye": [0.38, 0.28, 0.62, 0.36],
        "s2_bena_mouth": [0.42, 0.38, 0.58, 0.45],
        "s3_bena_eye": [0.36, 0.26, 0.62, 0.35],
        "s3_bena_mouth": [0.40, 0.37, 0.58, 0.45],
        "s4_chiba_eye": [0.36, 0.28, 0.62, 0.38],
        "s4_chiba_mouth": [0.40, 0.41, 0.58, 0.50],
        "s4_bena_eye": [0.36, 0.28, 0.62, 0.38],
        "s4_bena_mouth": [0.40, 0.41, 0.58, 0.50],
        "s5b_bena_eye": [0.34, 0.27, 0.64, 0.36],
        "s5b_bena_mouth": [0.38, 0.39, 0.60, 0.48],
    }
    if FACE_ROIS_FILE.is_file():
        try:
            saved = json.loads(FACE_ROIS_FILE.read_text(encoding="utf-8"))
            defaults.update(saved)
        except Exception:
            pass
    return defaults


def build() -> dict:
    durs = load_wav_durations()
    rois = load_face_rois()
    has_real_tts = TTS_MANIFEST.is_file()

    # Quy tắc chuẩn: cảnh lên hình trước giọng 0.30–0.40s, có khoảng thở tự nhiên sau mỗi câu.
    s1_start = 0.0
    l1_start = 0.40
    s1_end = r2(l1_start + durs["l1"] + 0.55)

    s2_start = s1_end
    l2_start = r2(s2_start + 0.35)
    s2_end = r2(l2_start + durs["l2"] + 0.65)

    s3_start = s2_end
    l3_start = r2(s3_start + 0.65)  # 0.65s cho cú sốc zoom_punch + đỏ màn hình trước khi Na la lên
    s3_end = r2(l3_start + durs["l3"] + 0.55)

    s4_start = s3_end
    l4_start = r2(s4_start + 0.45)
    l5_start = r2(l4_start + durs["l4"] + 0.35)
    s4_end = r2(l5_start + durs["l5"] + 0.55)

    s5a_start = s4_end
    l6_start = r2(s5a_start + 0.45)
    s5a_end = r2(l6_start + durs["l6"] + 0.55)

    s5b_start = s5a_end
    l7_start = r2(s5b_start + 0.35)
    s5b_end = r2(l7_start + durs["l7"] + 0.50)

    s6_start = s5b_end
    l8_start = r2(s6_start + 0.35)
    s6_end = r2(l8_start + durs["l8"] + 0.55)

    s7_start = s6_end
    l9_start = r2(s7_start + 0.40)
    l10_start = r2(l9_start + durs["l9"] + 0.30)
    s7_end = r2(l10_start + durs["l10"] + 0.55)

    s8_start = s7_end
    s8_end = r2(s8_start + 4.80)  # Thẻ NHỚ KỸ 4.8s đủ đọc kỹ ý SSO + tệp lạ

    s9_start = s8_end
    s9_end = r2(s9_start + 4.50)  # Kết mở câm thoại 2.5D cảnh báo nhóm lớp 4.5s

    s10_start = s9_end
    s10_end = r2(s10_start + 2.70)  # Cắt đen & LƯU Ý 2.7s

    total_dur = s10_end

    def blink_times(start: float, end: float, offset: float = 1.4, step: float = 3.2) -> list[float]:
        pts = []
        t = start + offset
        while t < end - 0.55:
            pts.append(r2(t))
            t += step
        if not pts and (end - start) > 1.2:
            pts.append(r2((start + end) * 0.5))
        return pts

    ep = {
        "episode_id": "EP13",
        "slug": "TaiLieuOnThiMienPhi",
        "title": "Tài liệu ôn thi miễn phí – Bấm tải 1 giây, mất sạch tài khoản lẫn ảnh riêng tư!",
        "version": "v2-level3-sso-real-tts" if has_real_tts else "v2-level3-sso-draft",
        "scam_family": "VAR-DOC-01",
        "motion_upgrade": "level3",
        "duration_sec": total_dur,
        "hook": {
            "kicker": "TÀI LIỆU ÔN THI MIỄN PHÍ",
            "title": "Chỉ 1 cú bấm tải, mất trắng tài khoản!",
            "start": 0.25,
            "end": r2(min(4.85, s1_end - 0.35)),
        },
        "scenes": [
            {
                "id": "s1_hook_link_de_thi",
                "image": "assets/s1.jpg",
                "start": s1_start,
                "end": s1_end,
                "beat_type": "establishing",
                "motion_level": "C",
                "motion_intent": "POV bàn học khuya 23h30, điện thoại sáng link đề thi miễn phí kèm screen_glow + typing_indicator + tông cold_suspicion",
                "motion": {
                    "preset": "slow_push_in",
                    "scale": [1.02, 1.09],
                    "focus": [[0.50, 0.52], [0.50, 0.49]],
                    "wobble": "none",
                    "easing": "ease_out",
                },
                "detail_fx": [
                    {
                        "type": "screen_glow",
                        "pos": [0.50, 0.56],
                        "radius": [0.26, 0.22],
                        "color": [125, 205, 255],
                        "intensity": 0.28,
                        "mode": "pulse",
                        "start": 0.20,
                        "end": r2(s1_end - 0.10),
                        "fade": 0.25,
                    },
                    {
                        "type": "typing_indicator",
                        "start": 0.35,
                        "end": 1.85,
                        "side": "left",
                        "y": 760,
                        "sender": "Nhóm chia sẻ đề thi",
                    },
                    {
                        "type": "color_mood",
                        "mood": "cold_suspicion",
                        "strength": 0.35,
                        "vignette": 0.16,
                        "grain": 0.008,
                    },
                ],
            },
            {
                "id": "s2_na_nhap_mat_khau",
                "image": "assets/s2.jpg",
                "start": s2_start,
                "end": s2_end,
                "beat_type": "normal",
                "motion_level": "B",
                "motion_intent": "2.5D Parallax phòng trọ khuya + Rack Focus mờ kệ sách + Breathing + Head Micro-Tilt + Bé Na chớp mắt & chép miệng 4 trạng thái (round_image) trên fg",
                "motion": {
                    "preset": "slow_push_in",
                    "scale": [1.02, 1.08],
                    "focus": [[0.50, 0.48], [0.50, 0.46]],
                    "wobble": "none",
                    "easing": "smoothstep",
                },
                "parallax": {
                    "camera": "push_in",
                    "dolly": [1.02, 1.07],
                    "shift_x": [0.0, 0.0],
                    "shift_y": [1.5, -2.0],
                    "focus": [0.50, 0.46],
                    "strength": 0.85,
                    "easing": "smoothstep",
                    "layers": [
                        {
                            "role": "bg",
                            "image": "assets/s2_bg.jpg",
                            "depth": 0.40,
                            "blur_from": 0.4,
                            "blur_to": 3.8,
                            "blur_at": r2(s2_start + 1.0),
                            "blur_dur": 3.0,
                        },
                        {
                            "role": "fg",
                            "image": "assets/s2_fg.png",
                            "depth": 1.24,
                            "breathe_y": 2.0,
                            "breathe_period": 3.6,
                            "head_tilt_deg": 1.1,
                            "head_pivot": [0.50, 0.78],
                            "tilt_speaker": "be_na",
                            "tilt_line_ids": ["l2"],
                        },
                    ],
                },
                "detail_fx": [
                    {
                        "type": "eye_blink",
                        "image": "assets/s2_bena_blink.jpg",
                        "region": rois["s2_bena_eye"],
                        "feather": 0.008,
                        "times": blink_times(s2_start, s2_end, 1.2, 3.1),
                        "close_dur": 0.055,
                        "hold_dur": 0.045,
                        "open_dur": 0.085,
                        "layer": "fg",
                    },
                    {
                        "type": "mouth_sync",
                        "speaker": "be_na",
                        "line_ids": ["l2"],
                        "region": rois["s2_bena_mouth"],
                        "feather": 0.008,
                        "closed_image": "assets/s2_bena_mouth_closed.jpg",
                        "mid_image": "assets/s2.jpg",
                        "open_image": "assets/s2_bena_mouth_open.jpg",
                        "round_image": "assets/s2_bena_mouth_round.jpg",
                        "fps": 12,
                        "thresh_mid": 0.14,
                        "thresh_open": 0.64,
                        "layer": "fg",
                    },
                    {
                        "type": "screen_glow",
                        "pos": [0.50, 0.66],
                        "radius": [0.24, 0.18],
                        "color": [125, 210, 255],
                        "intensity": 0.24,
                        "mode": "pulse",
                        "start": r2(s2_start + 0.15),
                        "end": r2(s2_end - 0.10),
                        "fade": 0.25,
                    },
                ],
                "transition_in": {"type": "dissolve", "dur": 0.25},
            },
            {
                "id": "s3_mat_quyen_3_giay",
                "image": "assets/s3.jpg",
                "start": s3_start,
                "end": s3_end,
                "beat_type": "climax",
                "motion_level": "C",
                "motion_intent": "Cú zoom_punch bật đỏ cảnh báo văng tài khoản + chromatic_pulse + shakes + red_circle_draw khoanh lỗi xâm nhập + Living-Char Bé Na hoảng hốt",
                "motion": {
                    "preset": "tense_push",
                    "scale": [1.03, 1.11],
                    "focus": [[0.50, 0.48], [0.50, 0.46]],
                    "wobble": "breathe",
                    "easing": "ease_out",
                },
                "detail_fx": [
                    {
                        "type": "detail_reveal",
                        "image": "assets/s3_reveal.jpg",
                        "at": r2(s3_start + 0.40),
                        "dur": 0.30,
                    },
                    {
                        "type": "eye_blink",
                        "image": "assets/s3_bena_blink.jpg",
                        "region": rois["s3_bena_eye"],
                        "feather": 0.008,
                        "times": blink_times(s3_start, s3_end, 1.6, 2.9),
                        "close_dur": 0.055,
                        "hold_dur": 0.045,
                        "open_dur": 0.085,
                    },
                    {
                        "type": "mouth_sync",
                        "speaker": "be_na",
                        "line_ids": ["l3"],
                        "region": rois["s3_bena_mouth"],
                        "feather": 0.008,
                        "closed_image": "assets/s3_bena_mouth_closed.jpg",
                        "mid_image": "assets/s3.jpg",
                        "open_image": "assets/s3_bena_mouth_open.jpg",
                        "fps": 12,
                        "thresh_mid": 0.14,
                        "thresh_open": 0.64,
                    },
                    {
                        "type": "chromatic_pulse",
                        "at": r2(s3_start + 0.40),
                        "dur": 0.30,
                        "shift_px": 7,
                        "zoom_blur": 0.025,
                    },
                    {
                        "type": "light_shift",
                        "at": r2(s3_start + 0.40),
                        "dur": 0.16,
                        "brightness": 0.94,
                        "tint_rgb": [255, 70, 75],
                        "tint_strength": 0.14,
                    },
                    {
                        "type": "red_circle_draw",
                        "region": [0.75, 0.62, 0.96, 0.80],
                        "at": r2(s3_start + 1.35),
                        "dur": 0.50,
                        "style": "circle",
                    },
                ],
                "shakes": [{"at": r2(s3_start + 0.40), "amp": 24}],
                "transition_in": {"type": "zoom_punch", "dur": 0.28},
            },
            {
                "id": "s4_split_cuoc_goi_chi_ba_na",
                "image": "assets/s4_chiba.jpg",
                "start": s4_start,
                "end": s4_end,
                "beat_type": "suspicion",
                "motion_level": "C",
                "motion_intent": "Level 3 split_screen trên-dưới cuộc gọi giữa Chị Ba (panel 0) và Bé Na (panel 1), sáng viền + sóng âm + chớp mắt & chép miệng độc lập cả 2 nhân vật",
                "split_screen": {
                    "layout": "horizontal",
                    "ratio": 0.40,
                    "divider_width": 6,
                    "inactive_dim": 0.18,
                    "slide_in_dur": 0.32,
                    "panels": [
                        {
                            "image": "assets/s4_chiba.jpg",
                            "speaker": "chi_ba",
                            "line_ids": ["l4"],
                            "label": "",
                            "label_rgb": [70, 205, 145],
                            "waveform": True,
                            "waveform_rgb": [105, 235, 175],
                            "crop_x": 0.50,
                            "crop_y": 0.35,
                            "motion": {"preset": "slow_push_in", "scale": [1.02, 1.07], "focus": [[0.50, 0.44], [0.50, 0.42]]},
                            "detail_fx": [
                                {
                                    "type": "eye_blink",
                                    "image": "assets/s4_chiba_blink.jpg",
                                    "region": rois["s4_chiba_eye"],
                                    "region_space": "source",
                                    "feather": 0.008,
                                    "times": blink_times(s4_start, s4_end, 1.3, 3.4),
                                    "close_dur": 0.055,
                                    "hold_dur": 0.045,
                                    "open_dur": 0.085,
                                },
                                {
                                    "type": "mouth_sync",
                                    "speaker": "chi_ba",
                                    "line_ids": ["l4"],
                                    "region": rois["s4_chiba_mouth"],
                                    "region_space": "source",
                                    "feather": 0.008,
                                    "closed_image": "assets/s4_chiba_mouth_closed.jpg",
                                    "mid_image": "assets/s4_chiba.jpg",
                                    "open_image": "assets/s4_chiba_mouth_open.jpg",
                                    "fps": 12,
                                    "thresh_mid": 0.14,
                                    "thresh_open": 0.64,
                                },
                            ],
                        },
                        {
                            "image": "assets/s4_bena.jpg",
                            "speaker": "be_na",
                            "line_ids": ["l5"],
                            "label": "",
                            "label_rgb": [245, 110, 145],
                            "waveform": True,
                            "waveform_rgb": [255, 145, 175],
                            "crop_x": 0.50,
                            "crop_y": 0.68,
                            "motion": {"preset": "slow_pull_out", "scale": [1.10, 1.05], "focus": [[0.50, 0.64], [0.50, 0.62]]},
                            "detail_fx": [
                                {
                                    "type": "eye_blink",
                                    "image": "assets/s4_bena_blink.jpg",
                                    "region": rois["s4_bena_eye"],
                                    "region_space": "source",
                                    "feather": 0.008,
                                    "times": blink_times(s4_start, s4_end, 2.2, 3.3),
                                    "close_dur": 0.055,
                                    "hold_dur": 0.045,
                                    "open_dur": 0.085,
                                },
                                {
                                    "type": "mouth_sync",
                                    "speaker": "be_na",
                                    "line_ids": ["l5"],
                                    "region": rois["s4_bena_mouth"],
                                    "region_space": "source",
                                    "feather": 0.008,
                                    "closed_image": "assets/s4_bena_mouth_closed.jpg",
                                    "mid_image": "assets/s4_bena.jpg",
                                    "open_image": "assets/s4_bena_mouth_open.jpg",
                                    "fps": 12,
                                    "thresh_mid": 0.14,
                                    "thresh_open": 0.64,
                                },
                            ],
                        },
                    ],
                },
                "transition_in": {"type": "whip_pan_left", "dur": 0.26},
            },
            {
                "id": "s5a_ke_gian_uy_hiep",
                "image": "assets/s5a.jpg",
                "start": s5a_start,
                "end": s5a_end,
                "beat_type": "climax",
                "motion_level": "C",
                "motion_intent": "Quét ngang hang ổ tối ánh xanh-đỏ + animated_counter đếm ngược 00:59→00:00 + phone_waveform đỏ cho giọng kẻ gian uy hiếp",
                "motion": {
                    "preset": "pan_left",
                    "scale": [1.07, 1.07],
                    "focus": [[0.54, 0.50], [0.46, 0.50]],
                    "wobble": "tense",
                    "easing": "smoothstep",
                },
                "detail_fx": [
                    {
                        "type": "animated_counter",
                        "start": r2(s5a_start + 0.30),
                        "end": r2(s5a_end - 0.15),
                        "count_dur": r2(max(2.0, s5a_end - s5a_start - 0.60)),
                        "from_val": 59,
                        "to_val": 0,
                        "fmt": "mmss",
                        "label": "THỜI HẠN ÉP CHUYỂN",
                        "pos": [0.46, 0.22],
                        "style": "danger",
                        "easing": "linear",
                    },
                    {
                        "type": "phone_waveform",
                        "speaker": "ke_gia_danh",
                        "line_ids": ["l6"],
                        "start": r2(s5a_start + 0.25),
                        "end": r2(s5a_end - 0.15),
                        "pos": [0.46, 0.62],
                        "size": [0.58, 0.044],
                        "color": [255, 90, 90],
                        "label": "SỐ LẠ · UY HIẾP",
                    },
                    {
                        "type": "screen_glow",
                        "pos": [0.50, 0.44],
                        "radius": [0.30, 0.22],
                        "color": [255, 85, 85],
                        "intensity": 0.24,
                        "mode": "flicker",
                        "start": r2(s5a_start + 0.20),
                        "end": r2(s5a_end - 0.10),
                        "fade": 0.20,
                    },
                    {
                        "type": "color_mood",
                        "mood": "high_tension",
                        "strength": 0.52,
                        "vignette": 0.24,
                        "grain": 0.015,
                    },
                ],
                "transition_in": {"type": "cut", "dur": 0.0},
            },
            {
                "id": "s5b_na_bang_hoang",
                "image": "assets/s5b.jpg",
                "start": s5b_start,
                "end": s5b_end,
                "beat_type": "suspicion",
                "motion_level": "C",
                "motion_intent": "Kéo lùi chậm cận gương mặt Bé Na rụng rời toát mồ hôi + Living-Char chớp mắt, chép miệng & nhịp thở dưới ánh đỏ cảnh báo",
                "motion": {
                    "preset": "slow_pull_out",
                    "scale": [1.09, 1.02],
                    "focus": [[0.50, 0.46], [0.50, 0.49]],
                    "wobble": "breathe",
                    "easing": "smoothstep",
                },
                "detail_fx": [
                    {
                        "type": "eye_blink",
                        "image": "assets/s5b_bena_blink.jpg",
                        "region": rois["s5b_bena_eye"],
                        "feather": 0.008,
                        "times": blink_times(s5b_start, s5b_end, 1.4, 2.9),
                        "close_dur": 0.055,
                        "hold_dur": 0.045,
                        "open_dur": 0.085,
                    },
                    {
                        "type": "mouth_sync",
                        "speaker": "be_na",
                        "line_ids": ["l7"],
                        "region": rois["s5b_bena_mouth"],
                        "feather": 0.008,
                        "closed_image": "assets/s5b_bena_mouth_closed.jpg",
                        "mid_image": "assets/s5b.jpg",
                        "open_image": "assets/s5b_bena_mouth_open.jpg",
                        "fps": 12,
                        "thresh_mid": 0.14,
                        "thresh_open": 0.64,
                    },
                    {
                        "type": "screen_glow",
                        "pos": [0.46, 0.64],
                        "radius": [0.24, 0.18],
                        "color": [255, 95, 95],
                        "intensity": 0.25,
                        "mode": "pulse",
                        "start": r2(s5b_start + 0.15),
                        "end": r2(s5b_end - 0.10),
                        "fade": 0.25,
                    },
                    {
                        "type": "color_mood",
                        "mood": "high_tension",
                        "strength": 0.42,
                        "vignette": 0.22,
                        "grain": 0.012,
                    },
                ],
                "transition_in": {"type": "cut", "dur": 0.0},
            },
            {
                "id": "s6_xu_ly_binh_tinh",
                "image": "assets/s6.jpg",
                "start": s6_start,
                "end": s6_end,
                "beat_type": "information",
                "motion_level": "C",
                "motion_intent": "Quét phải sang ánh đèn vàng ấm: Bé Na bình tĩnh nghe loa ngoài Chị Ba, bấm lưu bằng chứng & bật khiên bảo vệ (detail_reveal + phone_waveform)",
                "motion": {
                    "preset": "pan_right",
                    "scale": [1.06, 1.06],
                    "focus": [[0.46, 0.50], [0.54, 0.50]],
                    "wobble": "none",
                    "easing": "smoothstep",
                },
                "detail_fx": [
                    {
                        "type": "detail_reveal",
                        "image": "assets/s6_reveal.jpg",
                        "at": r2(s6_start + 1.35),
                        "dur": 0.50,
                    },
                    {
                        "type": "phone_waveform",
                        "speaker": "chi_ba",
                        "line_ids": ["l8"],
                        "start": r2(s6_start + 0.25),
                        "end": r2(s6_end - 0.15),
                        "pos": [0.46, 0.22],
                        "size": [0.58, 0.044],
                        "color": [90, 230, 165],
                        "label": "CHỊ BA · LOA NGOÀI",
                    },
                    {
                        "type": "color_mood",
                        "mood": "warm_daily",
                        "strength": 0.40,
                        "vignette": 0.12,
                        "grain": 0.0,
                    },
                ],
                "transition_in": {"type": "dissolve", "dur": 0.25},
            },
            {
                "id": "s7_boc_tran_hai_mui_bay",
                "image": "assets/s7.jpg",
                "start": s7_start,
                "end": s7_end,
                "beat_type": "anomaly",
                "motion_level": "C",
                "motion_intent": "1 khung kính lúp đỏ bóc trần 2 mũi bẫy (link móc câu mật khẩu + tệp nứt vỏ mã độc) kèm detail_reveal + red_circle_draw + highlighter_sweep",
                "motion": {
                    "preset": "slow_push_in",
                    "scale": [1.02, 1.09],
                    "focus": [[0.50, 0.48], [0.50, 0.46]],
                    "wobble": "none",
                    "easing": "ease_out",
                },
                "detail_fx": [
                    {
                        "type": "detail_reveal",
                        "image": "assets/s7_reveal.jpg",
                        "at": r2(s7_start + 0.65),
                        "dur": 0.60,
                    },
                    {
                        "type": "red_circle_draw",
                        "region": [0.53, 0.66, 0.74, 0.79],
                        "at": r2(s7_start + 1.45),
                        "dur": 0.50,
                        "style": "circle",
                    },
                    {
                        "type": "highlighter_sweep",
                        "region": [0.07, 0.56, 0.41, 0.66],
                        "at": r2(s7_start + 2.40),
                        "dur": 0.45,
                    },
                    {
                        "type": "focus_highlight",
                        "pos": [0.50, 0.48],
                        "radius": [0.46, 0.38],
                        "dim_outer": 0.22,
                        "start": r2(s7_start + 0.70),
                        "end": r2(s7_end - 0.10),
                        "fade": 0.35,
                    },
                    {
                        "type": "color_mood",
                        "mood": "noir_evidence",
                        "strength": 0.45,
                        "vignette": 0.22,
                        "grain": 0.012,
                    },
                ],
                "transition_in": {"type": "glitch", "dur": 0.34},
            },
            {
                "id": "s8_the_nho_ky",
                "image": "assets/s8.jpg",
                "start": s8_start,
                "end": s8_end,
                "beat_type": "ending",
                "motion_level": "A",
                "motion_intent": "Giữ tĩnh tuyệt đối trên nền phòng học sáng nắng dịu để khán giả đọc gọn Thẻ Nhớ kỹ trong 4.5s",
                "motion": {"preset": "static_hold"},
                "transition_in": {"type": "fade_black", "dur": 0.28},
            },
            {
                "id": "s9_ket_mo_canh_bao_nhom_lop",
                "image": "assets/s9.jpg",
                "start": s9_start,
                "end": s9_end,
                "beat_type": "climax",
                "motion_level": "B",
                "motion_intent": "Kết mở câm thoại 2.5D Parallax (film_burn): tay Bé Na tiền cảnh bấm gửi cảnh báo vào nhóm lớp + Rack Focus rõ bạn học hậu cảnh kịp khựng tay + ambient_particles + light_sweep",
                "motion": {
                    "preset": "slow_pull_out",
                    "scale": [1.08, 1.02],
                    "focus": [[0.50, 0.48], [0.50, 0.50]],
                    "wobble": "none",
                    "easing": "ease_out",
                },
                "parallax": {
                    "camera": "pull_out",
                    "dolly": [1.08, 1.02],
                    "shift_x": [0.0, 0.0],
                    "shift_y": [-3.0, 2.0],
                    "focus": [0.50, 0.50],
                    "strength": 0.88,
                    "easing": "ease_out",
                    "layers": [
                        {
                            "role": "bg",
                            "image": "assets/s9_bg.jpg",
                            "depth": 0.42,
                            "blur_from": 4.2,
                            "blur_to": 0.4,
                            "blur_at": r2(s9_start + 1.15),
                            "blur_dur": 1.4,
                        },
                        {
                            "role": "fg",
                            "image": "assets/s9_fg.png",
                            "depth": 1.32,
                            "breathe_y": 1.8,
                            "breathe_period": 3.4,
                        },
                    ],
                },
                "detail_fx": [
                    {
                        "type": "ambient_particles",
                        "count": 24,
                        "opacity": 0.36,
                        "color": [255, 240, 200],
                        "drift_dir": "up",
                    },
                    {
                        "type": "light_sweep",
                        "mode": "light",
                        "color": [255, 236, 185],
                        "intensity": 0.24,
                        "repeat": 1,
                        "start": r2(s9_start + 0.80),
                        "end": r2(s9_end - 0.30),
                    },
                ],
                "transition_in": {"type": "film_burn", "dur": 0.36},
            },
            {
                "id": "s10_black_disclaimer",
                "image": "assets/s10_black.jpg",
                "start": s10_start,
                "end": s10_end,
                "beat_type": "ending",
                "motion_level": "A",
                "motion_intent": "Cắt đen tĩnh tuyệt đối cho bảng Lưu ý cuối video",
                "motion": {"preset": "static_hold"},
                "transition_in": {"type": "cut", "dur": 0.0},
            },
        ],
        "dialogue": [
            {
                "id": "l1",
                "speaker": "be_na",
                "start": l1_start,
                "window": r2(s1_end - l1_start - 0.05),
                "text": "Sát giờ thi rồi! Có bộ đề tủ miễn phí nè, đăng nhập tải cho lẹ!",
                "style": "Giọng cô gái sinh viên miền Nam Sài Gòn 20 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, giữ cố định một âm sắc trong trẻo tự nhiên; háo hức pha chút vội vã mừng rỡ vì đang cần tài liệu ôn thi gấp.",
            },
            {
                "id": "l2",
                "speaker": "be_na",
                "start": l2_start,
                "window": r2(s2_end - l2_start - 0.05),
                "text": "Ủa đang dùng app mà sao bấm link lại bắt đăng nhập lại? Thôi kệ, miễn phí đâu mất tiền!",
                "style": "Giọng cô gái sinh viên miền Nam Sài Gòn 20 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, giữ cố định cùng một âm sắc trong trẻo tự nhiên; hơi thắc mắc thoáng qua rồi tặc lưỡi chủ quan nhẹ bẫng.",
            },
            {
                "id": "l3",
                "speaker": "be_na",
                "start": l3_start,
                "window": r2(s3_end - l3_start - 0.05),
                "text": "Khoan... sao tài liệu đâu chưa thấy mà nick bị đá văng, đổi mật khẩu hết rồi?!",
                "style": "Giọng cô gái sinh viên miền Nam Sài Gòn 20 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, giữ cố định cùng một âm sắc trong trẻo; khựng lại hốt hoảng bàng hoàng khi phát hiện tài khoản bị chiếm.",
            },
            {
                "id": "l4",
                "speaker": "chi_ba",
                "start": l4_start,
                "window": r2(l5_start - l4_start - 0.05),
                "text": "Alo Na hả? Em mới nhắn mượn chị năm triệu gấp, giọng lạ quá nên chị gọi liền!",
                "style": "Giọng phụ nữ miền Nam Sài Gòn 35 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, giữ cố định một âm sắc rõ chữ, chín chắn và tỉnh táo; hỏi dứt khoát pha chút lo lắng cảnh giác.",
            },
            {
                "id": "l5",
                "speaker": "be_na",
                "start": l5_start,
                "window": r2(s4_end - l5_start - 0.05),
                "text": "Chị Ba đừng chuyển nha! Em vừa bấm link tải đề thi miễn phí, bị cướp nick rồi!",
                "style": "Giọng cô gái sinh viên miền Nam Sài Gòn 20 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, giữ cố định cùng một âm sắc trong trẻo; gấp gáp hốt hoảng ngăn chị họ kịp lúc.",
            },
            {
                "id": "l6",
                "speaker": "ke_gia_danh",
                "label_short": "SỐ LẠ",
                "af": "phone",
                "start": l6_start,
                "window": r2(s5a_end - l6_start - 0.05),
                "text": "Đổi mật khẩu cũng vô ích! Ảnh riêng tư trong máy cô tôi giữ hết, chuyển tiền liền đi!",
                "style": "Giọng nam miền Nam Sài Gòn 40 tuổi qua điện thoại, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, giữ cố định một âm sắc trầm lạnh, đều và đầy sức ép đe nén, không gào thét thái quá.",
            },
            {
                "id": "l7",
                "speaker": "be_na",
                "start": l7_start,
                "window": r2(s5b_end - l7_start - 0.05),
                "text": "Trời ơi... chỉ tải đề ôn thi mà nó lấy sạch nick lẫn hình riêng tư luôn!",
                "style": "Giọng cô gái sinh viên miền Nam Sài Gòn 20 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, giữ cố định cùng một âm sắc trong trẻo; nghẹn giọng run rẩy bàng hoàng khi nhận ra hậu quả kép.",
            },
            {
                "id": "l8",
                "speaker": "chi_ba",
                "af": "phone",
                "start": l8_start,
                "window": r2(s6_end - l8_start - 0.05),
                "text": "Tuyệt đối không chuyển một đồng! Báo ngay người thân, lưu hết link tin nhắn lại rồi đi trình báo!",
                "style": "Giọng phụ nữ miền Nam Sài Gòn 35 tuổi qua loa điện thoại, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, giữ cố định cùng một âm sắc chín chắn, bình tĩnh, dứt khoát và vững vàng trấn an em họ.",
            },
            {
                "id": "l9",
                "speaker": "nguoi_boc_tran",
                "start": l9_start,
                "window": r2(l10_start - l9_start - 0.05),
                "text": "Mạng xã hội đang dùng không bao giờ bắt đăng nhập lại: chỉ đăng nhập trong chính app mạng xã hội đó!",
                "style": "Giọng nam trung niên miền Nam Sài Gòn 40 tuổi, phát âm chuẩn phương ngữ miền Nam, trầm tĩnh, rõ chữ và sắc gọn như câu phân tích kỹ thuật dễ hiểu; nhấn chắc vào nguyên tắc chỉ đăng nhập trong chính app gốc.",
            },
            {
                "id": "l10",
                "speaker": "nguoi_boc_tran",
                "start": l10_start,
                "window": r2(s7_end - l10_start - 0.05),
                "text": "Tài liệu sạch không đòi mật khẩu hay tệp lạ: miễn phí là cái bẫy đắt nhất!",
                "style": "Giọng nam trung niên miền Nam Sài Gòn 40 tuổi, phát âm chuẩn phương ngữ miền Nam, giữ nguyên cùng âm sắc trầm tĩnh sắc lạnh, chốt gọn dứt khoát như câu kết điện ảnh, tuyệt đối không rao giảng dạy đời.",
            },
        ],
        "chat_bubbles": [],
        "notifications": [],
        "callouts": [],
        "red_flags": {
            "start": s8_start,
            "end": s8_end,
            "stagger_sec": 0.38,
            "title": "NHỚ KỸ",
            "items": [
                "Mạng xã hội đang dùng có cơ chế đăng nhập một lần (SSO) — không bao giờ bắt đăng nhập lại qua link ngoài",
                "Tài liệu sạch không bao giờ đòi nhập mật khẩu hay tải tệp chạy lạ giấu mã độc",
                "Mất quyền tài khoản lập tức bị mạo danh vay tiền người thân hoặc uy hiếp bằng ảnh riêng tư",
            ],
            "action": "Chỉ đăng nhập lại trong chính app của mạng xã hội đó · Bật 2FA · Mất nick phải báo người thân, lưu bằng chứng trình báo công an ngay!",
        },
        "disclaimer": {
            "start": s10_start,
            "end": s10_end,
        },
        "audio": {
            "duck_ambience_db": -5.5,
            "ambience": [
                {"preset": "night_room", "start": s1_start, "end": s6_end, "gain_db": -5.5},
                {"preset": "room_tone", "start": s6_end, "end": s8_end, "gain_db": -7.0},
                {"preset": "office", "start": s8_end, "end": s9_end, "gain_db": -8.0},
                {"preset": "room_tone", "start": s9_end, "end": s10_end, "gain_db": -12.0},
            ],
            "foley": [
                {"preset": "phone_vibrate", "at": 0.12, "dur": 0.6, "gain_db": -1.5},
                {"preset": "notification", "at": 0.35, "gain_db": -1.0},
                {"preset": "typing", "at": r2(s2_start + 0.50), "dur": 1.6, "gain_db": -4.0},
                {"preset": "click", "at": r2(s2_end - 0.45), "gain_db": 0.5},
                {"preset": "glitch", "at": r2(s3_start + 0.38), "dur": 0.40, "gain_db": 1.2},
                {"preset": "impact", "at": r2(s3_start + 0.40), "dur": 1.0, "gain_db": 1.8},
                {"preset": "marker_draw", "at": r2(s3_start + 1.35), "dur": 0.48, "gain_db": 0.8},
                {"preset": "phone_ring", "at": r2(s4_start - 0.45), "dur": 0.95, "gain_db": -3.0},
                {"preset": "click", "at": r2(s4_start + 0.40), "gain_db": 0.2},
                {"preset": "low_accent", "at": r2(l5_start - 0.10), "dur": 0.9, "gain_db": 0.4},
                {"preset": "keyboard", "at": r2(s5a_start + 0.10), "dur": 1.2, "gain_db": -4.0},
                {"preset": "counter_tick", "at": r2(s5a_start + 0.35), "gain_db": -1.0},
                {"preset": "counter_tick", "at": r2(s5a_start + 1.35), "gain_db": -1.5},
                {"preset": "counter_tick", "at": r2(s5a_start + 2.35), "gain_db": -1.5},
                {"preset": "heartbeat", "at": r2(s5a_start + 0.40), "dur": r2(s5b_end - s5a_start - 0.60), "gain_db": -2.0},
                {"preset": "notification", "at": r2(s5b_start + 0.25), "gain_db": -0.5},
                {"preset": "notification", "at": r2(s5b_start + 1.15), "gain_db": -1.5},
                {"preset": "click", "at": r2(s6_start + 1.35), "gain_db": 0.6},
                {"preset": "low_accent", "at": r2(s6_start + 1.40), "dur": 0.9, "gain_db": 0.6},
                {"preset": "glitch", "at": r2(s7_start + 0.05), "dur": 0.36, "gain_db": 1.0},
                {"preset": "impact", "at": r2(s7_start + 0.12), "dur": 1.0, "gain_db": 1.6},
                {"preset": "low_accent", "at": r2(s7_start + 0.65), "dur": 0.9, "gain_db": 0.8},
                {"preset": "marker_draw", "at": r2(s7_start + 1.45), "dur": 0.48, "gain_db": 0.8},
                {"preset": "marker_draw", "at": r2(s7_start + 2.40), "dur": 0.48, "gain_db": 0.8},
                {"preset": "click", "at": r2(s9_start + 0.85), "gain_db": 0.8},
                {"preset": "message_send", "at": r2(s9_start + 1.00), "gain_db": 0.8},
                {"preset": "notification", "at": r2(s9_start + 1.35), "gain_db": -0.8},
                {"preset": "low_accent", "at": r2(s9_start + 1.50), "dur": 1.0, "gain_db": 0.8},
                {"preset": "riser", "at": r2(s9_end - 0.85), "dur": 0.75, "gain_db": 0.8},
                {"preset": "impact", "at": r2(s9_end - 0.12), "dur": 1.1, "gain_db": 2.0},
            ],
            "bgm": [
                {"preset": "suspense_pulse", "start": s1_start, "end": s4_end, "gain_db": -1.5},
                {"preset": "tension_drone", "start": s4_end, "end": s6_start, "gain_db": 0.8},
                {"preset": "investigative_story", "start": s6_start, "end": s8_start, "gain_db": 0.6},
                {"preset": "warm_outro", "start": s8_start, "end": s8_end},
                {"preset": "action_climax", "start": s9_start, "end": s9_end, "gain_db": -1.0},
            ],
            "duck_extra": [
                {"start": s9_start, "end": r2(s9_end - 0.15), "bgm_db": -2.0, "amb_db": -3.0},
            ],
        },
        "forbidden_terms": [],
        "publish": {
            "titles": [
                "Tài liệu ôn thi miễn phí: Bấm tải 1 giây, mất sạch tài khoản lẫn ảnh riêng tư! #shorts #bóctrầnlừađảo",
                "Sao tải đề cương miễn phí lại bắt nhập mật khẩu? Cái bẫy mùa thi đắt giá nhất! #shorts #cảnhgiáclừađảo",
                "Cẩn thận link đề thi miễn phí: Đổi mật khẩu vẫn bị uy hiếp vì mã độc giấu trong tệp! #shorts #vạnchuyện",
            ],
            "description": (
                "Sát ngày thi thấy đường link chia sẻ đề thi, đề cương ôn tập miễn phí, nhiều bạn học sinh, sinh viên chủ quan bấm vào và nhập lại mật khẩu mạng xã hội dù đang mở sẵn ứng dụng trên máy.\n\n"
                "Chi tiết kỹ thuật quan trọng nhiều người chưa biết: các nền tảng mạng xã hội đều áp dụng cơ chế đăng nhập một lần (SSO). Khi bạn đang dùng sẵn ứng dụng trên máy, hệ thống KHÔNG BAO GIỜ mở trang web lạ bắt bạn nhập lại mật khẩu — bạn chỉ đăng nhập lại khi ở trong chính app của mạng xã hội đó! Nguy hiểm hơn, nhiều tệp giả dạng tài liệu còn giấu mã độc chạy ngầm lấy sạch mật khẩu và ảnh riêng tư để uy hiếp ép chuyển tiền.\n\n"
                "✅ Nhớ kỹ để không sập bẫy mùa thi:\n"
                "1. Mạng xã hội đang dùng không bao giờ bắt đăng nhập lại qua link ngoài (cơ chế SSO) — chỉ đăng nhập trong chính app mạng xã hội đó.\n"
                "2. Tài liệu sạch không bao giờ đòi nhập mật khẩu hay bắt tải tệp chạy lạ.\n"
                "3. Bật xác thực hai lớp (2FA), thường xuyên kiểm tra và đăng xuất thiết bị lạ.\n"
                "4. Lỡ mất tài khoản phải báo ngay cho gia đình, nhóm lớp; tuyệt đối không chuyển tiền khi bị uy hiếp — lưu link, tin nhắn làm bằng chứng và trình báo cơ quan công an ngay."
            ),
            "pinned_comment": (
                "📌 Đang mùa thi nhớ gửi ngay video này cho con em, bạn học và nhóm lớp! Nhớ kỹ nguyên tắc SSO: mạng xã hội bạn đang dùng KHÔNG BAO GIỜ bắt đăng nhập lại qua đường link bên ngoài — chỉ đăng nhập khi ở trong chính app của mạng xã hội đó! "
                "Tài liệu sạch cũng không bao giờ đòi mật khẩu hay bắt tải tệp chạy lạ (`.exe`, `.scr`, `.dll`, `.ps1`). Bật ngay 2FA và tuyệt đối không chuyển tiền khi bị uy hiếp — báo người thân, lưu bằng chứng và trình báo cơ quan công an! "
                "(Lưu ý: Không đăng SĐT, STK hay tên người thật dưới phần bình luận; cảnh giác bẫy mạo danh 'hỗ trợ lấy lại nick/lấy lại tiền'.)"
            ),
            "hashtags": ["#shorts", "#bóctrầnlừađảo", "#cảnhgiáclừađảo"],
            "tags": [
                "lừa đảo tài liệu miễn phí",
                "link đề thi miễn phí lừa đảo",
                "chiếm đoạt tài khoản mạng xã hội",
                "mã độc trong file tài liệu",
                "bóc trần lừa đảo",
                "vạn chuyện",
                "shorts",
            ],
            "category": "Education (Giáo dục)",
            "playlist": "Bóc Trần Lừa Đảo – Kỹ Năng Cảnh Giác & An Toàn Đời Thực",
            "thumbnail_sec": r2(s3_start + 0.55),
        },
    }

    OUT_JSON.write_text(json.dumps(ep, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Đã biên dịch {OUT_JSON} ({total_dur:.2f}s · mode={'REAL_TTS' if has_real_tts else 'DRAFT'})")
    return ep


if __name__ == "__main__":
    build()
