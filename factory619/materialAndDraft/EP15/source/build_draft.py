# -*- coding: utf-8 -*-
"""
Single Source of Truth cho `factory619/materialAndDraft/EP15` (`BayAppNganHangGia`).

Chức năng:
  - Biên dịch đầy đủ `episode.json` chuẩn Visual Motion Level 3 (`HRN-MOTION-L3.0`, CHECK 1 → 2 → 3).
  - Tự động căn lại toàn bộ mốc thời gian scenes / dialogue / detail_fx / foley / bgm / red_flags / disclaimer
    theo độ dài WAV thật sau khi chạy Gate 2 (`audio/tts/tts_manifest_gate2.json`).
  - Tự động nạp tọa độ ROI khóa pixel chính xác từ `source/face_rois.json` sau bước bake `face_roi_prep.py`.
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
    defaults = {
        "l1": 3.55,
        "l2": 5.51,
        "l3": 6.38,
        "l4": 5.90,
        "l4b": 4.02,
        "l5": 5.60,
        "l6": 5.56,
        "l7": 3.07,
        "l8": 3.02,
        "l9": 5.52,
        "l10": 6.89,
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
    defaults = {
        "s1_scammer_eye": [0.220, 0.360, 0.380, 0.420],
        "s1_scammer_mouth": [0.250, 0.430, 0.355, 0.485],
        "s1_bena_eye": [0.640, 0.410, 0.800, 0.465],
        "s2_bena_eye": [0.460, 0.370, 0.650, 0.430],
        "s2_bena_mouth": [0.500, 0.445, 0.610, 0.500],
        "s3_cotu_eye": [0.480, 0.350, 0.670, 0.410],
        "s3_cotu_mouth": [0.515, 0.425, 0.630, 0.480],
        "s4_scammer_eye": [0.380, 0.340, 0.610, 0.415],
        "s4_scammer_mouth": [0.430, 0.445, 0.560, 0.515],
        "s4_bena_eye": [0.370, 0.350, 0.610, 0.425],
        "s4_bena_mouth": [0.430, 0.455, 0.560, 0.525],
        "s5_cotu_eye": [0.330, 0.350, 0.520, 0.410],
        "s5_cotu_mouth": [0.370, 0.425, 0.480, 0.480],
        "s6_scammer_eye": [0.200, 0.380, 0.360, 0.440],
        "s6_scammer_mouth": [0.230, 0.450, 0.335, 0.505],
        "s6_bena_eye": [0.640, 0.400, 0.800, 0.455],
        "s6_bena_mouth": [0.675, 0.470, 0.770, 0.520],
        "s6b_bena_eye": [0.520, 0.340, 0.680, 0.395],
        "s6b_bena_mouth": [0.550, 0.405, 0.645, 0.455],
        "s6b_cotu_eye": [0.740, 0.310, 0.890, 0.365],
        "s9a_cotu_eye": [0.360, 0.320, 0.560, 0.380],
        "s9a_cotu_mouth": [0.390, 0.400, 0.510, 0.455],
        # Detail / evidence regions (calibrated after image inspection)
        "s3_silent_circle": [0.100, 0.620, 0.490, 0.840],
        "s7_fake_circle": [0.220, 0.170, 0.780, 0.460],
        "s7_safe_highlight": [0.500, 0.600, 0.920, 0.840],
        "s1_phone_glow": [0.48, 0.58],
        "s9_phone_glow": [0.45, 0.64],
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

    # Cảnh lên hình trước thoại 0.35–0.45s, khoảng thở tự nhiên sau mỗi câu
    s1_start = 0.0
    l1_start = 0.40
    s1_end = r2(l1_start + durs["l1"] + 0.55)

    s2_start = s1_end
    l2_start = r2(s2_start + 0.35)
    s2_end = r2(l2_start + durs["l2"] + 0.55)

    s3_start = s2_end
    l3_start = r2(s3_start + 0.40)
    s3_end = r2(l3_start + durs["l3"] + 0.55)

    # Scene 4: Split-screen ngang — twist kì kèo "trả hai lần sao?!" + "lừa cả trăm cả tỷ" (l4 + l4b khách, l5 Na nao núng)
    s4_start = s3_end
    l4_start = r2(s4_start + 0.45)
    l4b_start = r2(l4_start + durs["l4"] + 0.25)
    l5_start = r2(l4b_start + durs["l4b"] + 0.35)
    s4_end = r2(l5_start + durs["l5"] + 0.55)

    # Scene 5: Cô Tư phản đòn sòng phẳng (l6 + l7)
    s5_start = s4_end
    l6_start = r2(s5_start + 0.40)
    l7_start = r2(l6_start + durs["l6"] + 0.30)
    s5_end = r2(l7_start + durs["l7"] + 0.55)

    # Scene 6A: Lộ khung nhập giả & giả bộ giận dỗi bỏ mua (s6.jpg · l8)
    s6a_start = s5_end
    l8_start = r2(s6a_start + 0.45)
    s6a_end = r2(l8_start + durs["l8"] + 0.45)

    # Scene 6B: Đã phóng xe máy vọt xa ngoài lối chợ, bỏ lại nguyên 2 túi hàng trên quầy (s6b.jpg · l9)
    s6b_start = s6a_end
    l9_start = r2(s6b_start + 0.40)
    s6b_end = r2(l9_start + durs["l9"] + 0.55)

    # Scene 7: Bóc trần siêu gọn đúng 1 câu (l10)
    s7_start = s6b_end
    l10_start = r2(s7_start + 0.35)
    s7_end = r2(l10_start + durs["l10"] + 0.55)

    # Scene 8: Thẻ NHỚ KỸ (5.0s không thoại)
    s8_start = s7_end
    s8_end = r2(s8_start + 5.00)

    # Scene 9A: Kết mở 100% CÂM THOẠI (nối tiếp Cô Tư EP12) — đổi ánh mắt lạnh, áp điện thoại báo kín không nói ra lệnh (3.5s)
    s9a_start = s8_end
    s9a_end = r2(s9a_start + 3.50)

    # Scene 9B: Kết mở 2.5D 100% CÂM THOẠI — 2 bóng lưng bí ẩn dưới mái hiên đầu chợ ra tín hiệu lăn bánh theo sau bóng áo xanh (3.8s)
    s9b_start = s9a_end
    s9b_end = r2(s9b_start + 3.80)

    # Scene 10: Cắt đen + Bảng LƯU Ý (2.7s)
    s10_start = s9b_end
    s10_end = r2(s10_start + 2.70)

    total_dur = s10_end

    def blink_times(start: float, end: float, offset: float = 1.3, step: float = 3.2) -> list[float]:
        pts = []
        t = start + offset
        while t < end - 0.55:
            pts.append(r2(t))
            t += step
        if not pts and (end - start) > 1.2:
            pts.append(r2((start + end) * 0.5))
        return pts

    ep = {
        "episode_id": "EP15",
        "slug": "BayAppNganHangGia",
        "title": "Bẫy app ngân hàng giả tại quầy – Thấy tận mắt bấm chuyển, tiền vẫn bằng không!",
        "version": "v4-level3-silent-coda-real-tts" if has_real_tts else "v4-level3-silent-coda-draft",
        "scam_family": "VAR-COM-02",
        "motion_upgrade": "level3",
        "duration_sec": total_dur,
        "hook": {
            "kicker": "BẪY APP NGÂN HÀNG GIẢ",
            "title": "Thấy tận mắt bấm chuyển, tiền vẫn bằng không!",
            "start": 0.25,
            "end": r2(min(4.85, s1_end - 0.35)),
        },
        "scenes": [
            {
                "id": "s1_hook_bam_chuyen_tan_mat",
                "image": "assets/s1.jpg",
                "start": s1_start,
                "end": s1_end,
                "beat_type": "establishing",
                "motion_level": "C",
                "motion_intent": "Chợ sáng đông đúc: khách lịch sự chìa màn hình bấm tích xanh Thành công trước mặt Bé Na + animated_counter 4.500.000đ + screen_glow xanh lá + Living-Char khách & Bé Na",
                "motion": {
                    "preset": "slow_push_in",
                    "scale": [1.02, 1.09],
                    "focus": [[0.50, 0.52], [0.50, 0.48]],
                    "wobble": "none",
                    "easing": "ease_out",
                },
                "detail_fx": [
                    {
                        "type": "eye_blink",
                        "image": "assets/s1_scammer_blink.jpg",
                        "region": rois["s1_scammer_eye"],
                        "feather": 0.008,
                        "times": blink_times(s1_start, s1_end, 1.4, 3.0),
                        "close_dur": 0.055,
                        "hold_dur": 0.045,
                        "open_dur": 0.085,
                    },
                    {
                        "type": "mouth_sync",
                        "speaker": "ke_ngot_ngao_nam",
                        "line_ids": ["l1"],
                        "region": rois["s1_scammer_mouth"],
                        "feather": 0.008,
                        "closed_image": "assets/s1_scammer_mouth_closed.jpg",
                        "mid_image": "assets/s1.jpg",
                        "open_image": "assets/s1_scammer_mouth_open.jpg",
                        "fps": 12,
                        "thresh_mid": 0.14,
                        "thresh_open": 0.64,
                    },
                    {
                        "type": "eye_blink",
                        "image": "assets/s1_bena_blink.jpg",
                        "region": rois["s1_bena_eye"],
                        "feather": 0.008,
                        "times": blink_times(s1_start, s1_end, 2.2, 3.1),
                        "close_dur": 0.055,
                        "hold_dur": 0.045,
                        "open_dur": 0.085,
                    },
                    {
                        "type": "animated_counter",
                        "start": 0.45,
                        "end": r2(s1_end - 0.15),
                        "count_dur": 1.8,
                        "from_val": 0,
                        "to_val": 4500000,
                        "fmt": "vnd",
                        "label": "MÀN HÌNH KHÁCH BÁO",
                        "pos": [0.68, 0.215],
                        "style": "safe",
                        "easing": "ease_out",
                    },
                    {
                        "type": "screen_glow",
                        "pos": rois["s1_phone_glow"],
                        "radius": [0.18, 0.15],
                        "color": [45, 225, 130],
                        "intensity": 0.22,
                        "mode": "pulse",
                        "start": 0.25,
                        "end": r2(s1_end - 0.10),
                        "fade": 0.25,
                    },
                    {
                        "type": "color_mood",
                        "mood": "warm_daily",
                        "strength": 0.22,
                        "vignette": 0.10,
                        "grain": 0.0,
                    },
                ],
            },
            {
                "id": "s2_na_suyt_tin_bam_tren_app",
                "image": "assets/s2.jpg",
                "start": s2_start,
                "end": s2_end,
                "beat_type": "normal",
                "motion_level": "B",
                "motion_intent": "2.5D Parallax quầy chợ sáng + Rack Focus mờ dãy sạp nền + Breathing + Head Micro-Tilt + Bé Na chớp mắt & chép miệng 4 trạng thái (round_image)",
                "motion": {
                    "preset": "slow_push_in",
                    "scale": [1.02, 1.07],
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
                            "blur_at": r2(s2_start + 0.9),
                            "blur_dur": 2.4,
                        },
                        {
                            "role": "fg",
                            "image": "assets/s2_fg.png",
                            "depth": 1.24,
                            "breathe_y": 2.0,
                            "breathe_period": 3.5,
                            "head_tilt_deg": 1.0,
                            "head_pivot": [0.72, 0.50],
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
                        "times": blink_times(s2_start, s2_end, 1.1, 3.0),
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
                ],
                "transition_in": {"type": "dissolve", "dur": 0.25},
            },
            {
                "id": "s3_co_tu_chan_lai_may_im_ru",
                "image": "assets/s3.jpg",
                "start": s3_start,
                "end": s3_end,
                "beat_type": "suspicion",
                "motion_level": "C",
                "motion_intent": "Quét trái giữ hàng: Cô Tư chỉ điện thoại trống thông báo & loa báo số dư im ru trên quầy + detail_reveal + red_circle_draw + Living-Char Cô Tư",
                "motion": {
                    "preset": "pan_left",
                    "scale": [1.06, 1.06],
                    "focus": [[0.53, 0.50], [0.47, 0.50]],
                    "wobble": "none",
                    "easing": "smoothstep",
                },
                "detail_fx": [
                    {
                        "type": "detail_reveal",
                        "image": "assets/s3_reveal.jpg",
                        "at": r2(s3_start + 1.15),
                        "dur": 0.45,
                    },
                    {
                        "type": "red_circle_draw",
                        "region": rois["s3_silent_circle"],
                        "at": r2(s3_start + 1.45),
                        "dur": 0.50,
                        "style": "circle",
                    },
                    {
                        "type": "eye_blink",
                        "image": "assets/s3_cotu_blink.jpg",
                        "region": rois["s3_cotu_eye"],
                        "feather": 0.008,
                        "times": blink_times(s3_start, s3_end, 1.2, 3.1),
                        "close_dur": 0.055,
                        "hold_dur": 0.045,
                        "open_dur": 0.085,
                    },
                    {
                        "type": "mouth_sync",
                        "speaker": "co_tu",
                        "line_ids": ["l3"],
                        "region": rois["s3_cotu_mouth"],
                        "feather": 0.008,
                        "closed_image": "assets/s3_cotu_mouth_closed.jpg",
                        "mid_image": "assets/s3.jpg",
                        "open_image": "assets/s3_cotu_mouth_open.jpg",
                        "fps": 12,
                        "thresh_mid": 0.14,
                        "thresh_open": 0.64,
                    },
                    {
                        "type": "color_mood",
                        "mood": "cold_suspicion",
                        "strength": 0.20,
                        "vignette": 0.12,
                        "grain": 0.0,
                    },
                ],
                "transition_in": {"type": "dissolve", "dur": 0.25},
            },
            {
                "id": "s4_split_twist_tra_hai_lan",
                "image": "assets/s4_scammer.jpg",
                "start": s4_start,
                "end": s4_end,
                "beat_type": "climax",
                "motion_level": "C",
                "motion_intent": "Level 3 split_screen trên-dưới: khách phản công kì kèo sợ trả tiền mặt thành hai lần (panel trên) & Bé Na nghe có lý nên khựng tay nao núng thật sự (panel dưới) + Living-Char cả 2 panel",
                "split_screen": {
                    "layout": "horizontal",
                    "ratio": 0.48,
                    "divider_width": 6,
                    "inactive_dim": 0.20,
                    "slide_in_dur": 0.28,
                    "panels": [
                        {
                            "image": "assets/s4_scammer.jpg",
                            "speaker": "ke_ngot_ngao_nam",
                            "line_ids": ["l4", "l4b"],
                            "label": "",
                            "label_rgb": [245, 90, 95],
                            "waveform": False,
                            "crop_x": 0.50,
                            "crop_y": 0.44,
                            "motion": {"preset": "slow_push_in", "scale": [1.02, 1.07], "focus": [[0.50, 0.48], [0.50, 0.46]]},
                            "detail_fx": [
                                {
                                    "type": "eye_blink",
                                    "image": "assets/s4_scammer_blink.jpg",
                                    "region": rois["s4_scammer_eye"],
                                    "region_space": "source",
                                    "feather": 0.008,
                                    "times": blink_times(s4_start, s4_end, 1.2, 3.1),
                                    "close_dur": 0.055,
                                    "hold_dur": 0.045,
                                    "open_dur": 0.085,
                                },
                                {
                                    "type": "mouth_sync",
                                    "speaker": "ke_ngot_ngao_nam",
                                    "line_ids": ["l4", "l4b"],
                                    "region": rois["s4_scammer_mouth"],
                                    "region_space": "source",
                                    "feather": 0.008,
                                    "closed_image": "assets/s4_scammer_mouth_closed.jpg",
                                    "mid_image": "assets/s4_scammer.jpg",
                                    "open_image": "assets/s4_scammer_mouth_open.jpg",
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
                            "label_rgb": [255, 215, 120],
                            "waveform": False,
                            "crop_x": 0.50,
                            "crop_y": 0.44,
                            "motion": {"preset": "slow_pull_out", "scale": [1.07, 1.02], "focus": [[0.50, 0.46], [0.50, 0.48]]},
                            "detail_fx": [
                                {
                                    "type": "eye_blink",
                                    "image": "assets/s4_bena_blink.jpg",
                                    "region": rois["s4_bena_eye"],
                                    "region_space": "source",
                                    "feather": 0.008,
                                    "times": blink_times(s4_start, s4_end, 2.0, 3.2),
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
                "detail_fx": [
                    {
                        "type": "color_mood",
                        "mood": "cold_suspicion",
                        "strength": 0.20,
                        "vignette": 0.14,
                        "grain": 0.006,
                    },
                ],
                "transition_in": {"type": "whip_pan_left", "dur": 0.26},
            },
            {
                "id": "s5_co_tu_phan_don_song_phang",
                "image": "assets/s5.jpg",
                "start": s5_start,
                "end": s5_end,
                "beat_type": "climax",
                "motion_level": "C",
                "motion_intent": "Quét phải dứt khoát: Cô Tư đặt sổ ký giấy nhận tiền mặt hoàn lại + chìa lịch sử máy mình trống trơn đòi coi lịch sử trừ số dư hoặc đứng chờ + detail_reveal + Living-Char Cô Tư",
                "motion": {
                    "preset": "pan_right",
                    "scale": [1.06, 1.06],
                    "focus": [[0.47, 0.50], [0.53, 0.50]],
                    "wobble": "none",
                    "easing": "smoothstep",
                },
                "detail_fx": [
                    {
                        "type": "detail_reveal",
                        "image": "assets/s5_reveal.jpg",
                        "at": r2(l6_start + 1.20),
                        "dur": 0.45,
                    },
                    {
                        "type": "eye_blink",
                        "image": "assets/s5_cotu_blink.jpg",
                        "region": rois["s5_cotu_eye"],
                        "feather": 0.008,
                        "times": blink_times(s5_start, s5_end, 1.4, 3.1),
                        "close_dur": 0.055,
                        "hold_dur": 0.045,
                        "open_dur": 0.085,
                    },
                    {
                        "type": "mouth_sync",
                        "speaker": "co_tu",
                        "line_ids": ["l6", "l7"],
                        "region": rois["s5_cotu_mouth"],
                        "feather": 0.008,
                        "closed_image": "assets/s5_cotu_mouth_closed.jpg",
                        "mid_image": "assets/s5.jpg",
                        "open_image": "assets/s5_cotu_mouth_open.jpg",
                        "fps": 12,
                        "thresh_mid": 0.14,
                        "thresh_open": 0.64,
                    },
                    {
                        "type": "color_mood",
                        "mood": "warm_daily",
                        "strength": 0.24,
                        "vignette": 0.10,
                        "grain": 0.0,
                    },
                ],
                "transition_in": {"type": "whip_pan_left", "dur": 0.26},
            },
            {
                "id": "s6a_lo_app_gia_gian_doi",
                "image": "assets/s6.jpg",
                "start": s6a_start,
                "end": s6a_end,
                "beat_type": "climax",
                "motion_level": "C",
                "motion_intent": "Cú lật 1: gã khách cứng họng trượt tay lộ khung nhập giả đỏ rực, giả bộ giận dỗi đòi bỏ mua + zoom_punch + tense_push + detail_reveal + chromatic_pulse + shakes + Living-Char khách & Bé Na",
                "motion": {
                    "preset": "tense_push",
                    "scale": [1.03, 1.10],
                    "focus": [[0.46, 0.50], [0.44, 0.47]],
                    "wobble": "breathe",
                    "easing": "ease_out",
                },
                "detail_fx": [
                    {
                        "type": "detail_reveal",
                        "image": "assets/s6_reveal.jpg",
                        "at": r2(s6a_start + 0.35),
                        "dur": 0.40,
                    },
                    {
                        "type": "chromatic_pulse",
                        "at": r2(s6a_start + 0.35),
                        "dur": 0.30,
                        "shift_px": 7,
                        "zoom_blur": 0.025,
                    },
                    {
                        "type": "eye_blink",
                        "image": "assets/s6_scammer_blink.jpg",
                        "region": rois["s6_scammer_eye"],
                        "feather": 0.008,
                        "times": blink_times(s6a_start, s6a_end, 1.2, 2.8),
                        "close_dur": 0.055,
                        "hold_dur": 0.045,
                        "open_dur": 0.085,
                    },
                    {
                        "type": "mouth_sync",
                        "speaker": "ke_ngot_ngao_nam",
                        "line_ids": ["l8"],
                        "region": rois["s6_scammer_mouth"],
                        "feather": 0.008,
                        "closed_image": "assets/s6_scammer_mouth_closed.jpg",
                        "mid_image": "assets/s6.jpg",
                        "open_image": "assets/s6_scammer_mouth_open.jpg",
                        "fps": 12,
                        "thresh_mid": 0.14,
                        "thresh_open": 0.64,
                    },
                    {
                        "type": "eye_blink",
                        "image": "assets/s6_bena_blink.jpg",
                        "region": rois["s6_bena_eye"],
                        "feather": 0.008,
                        "times": blink_times(s6a_start, s6a_end, 1.9, 2.9),
                        "close_dur": 0.055,
                        "hold_dur": 0.045,
                        "open_dur": 0.085,
                    },
                    {
                        "type": "color_mood",
                        "mood": "high_tension",
                        "strength": 0.34,
                        "vignette": 0.18,
                        "grain": 0.010,
                    },
                ],
                "shakes": [{"at": r2(s6a_start + 0.35), "amp": 20}],
                "transition_in": {"type": "zoom_punch", "dur": 0.28},
            },
            {
                "id": "s6b_bo_hang_leo_xe_vot_mat",
                "image": "assets/s6b.jpg",
                "start": s6b_start,
                "end": s6b_end,
                "beat_type": "climax",
                "motion_level": "C",
                "motion_intent": "Cú lật 2 (đúng logic không gian): trước quầy trống trơn còn nguyên 2 túi hàng, phía xa gã khách đã leo xe máy phóng vọt ra lối chợ, Bé Na sững sờ chỉ theo nói với Cô Tư + whip_pan_right + slow_pull_out + Living-Char Bé Na & Cô Tư",
                "motion": {
                    "preset": "slow_pull_out",
                    "scale": [1.08, 1.02],
                    "focus": [[0.50, 0.48], [0.50, 0.50]],
                    "wobble": "none",
                    "easing": "ease_out",
                },
                "detail_fx": [
                    {
                        "type": "eye_blink",
                        "image": "assets/s6b_bena_blink.jpg",
                        "region": rois["s6b_bena_eye"],
                        "feather": 0.008,
                        "times": blink_times(s6b_start, s6b_end, 1.3, 3.0),
                        "close_dur": 0.055,
                        "hold_dur": 0.045,
                        "open_dur": 0.085,
                    },
                    {
                        "type": "mouth_sync",
                        "speaker": "be_na",
                        "line_ids": ["l9"],
                        "region": rois["s6b_bena_mouth"],
                        "feather": 0.008,
                        "closed_image": "assets/s6b_bena_mouth_closed.jpg",
                        "mid_image": "assets/s6b.jpg",
                        "open_image": "assets/s6b_bena_mouth_open.jpg",
                        "fps": 12,
                        "thresh_mid": 0.14,
                        "thresh_open": 0.64,
                    },
                    {
                        "type": "eye_blink",
                        "image": "assets/s6b_cotu_blink.jpg",
                        "region": rois["s6b_cotu_eye"],
                        "feather": 0.008,
                        "times": blink_times(s6b_start, s6b_end, 2.2, 3.2),
                        "close_dur": 0.055,
                        "hold_dur": 0.045,
                        "open_dur": 0.085,
                    },
                    {
                        "type": "color_mood",
                        "mood": "warm_daily",
                        "strength": 0.20,
                        "vignette": 0.12,
                        "grain": 0.0,
                    },
                ],
                "transition_in": {"type": "whip_pan_right", "dur": 0.25},
            },
            {
                "id": "s7_boc_tran_app_ngan_hang_gia",
                "image": "assets/s7.jpg",
                "start": s7_start,
                "end": s7_end,
                "beat_type": "anomaly",
                "motion_level": "C",
                "motion_intent": "Kính lúp đỏ soi vỡ vỏ tích xanh app ngân hàng giả vs điện thoại chính chủ + loa báo số dư + khiên bảo vệ xanh + glitch + detail_reveal + red_circle_draw + highlighter_sweep",
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
                        "at": r2(s7_start + 0.55),
                        "dur": 0.45,
                    },
                    {
                        "type": "red_circle_draw",
                        "region": rois["s7_fake_circle"],
                        "at": r2(l10_start + 0.60),
                        "dur": 0.50,
                        "style": "circle",
                    },
                    {
                        "type": "highlighter_sweep",
                        "region": rois["s7_safe_highlight"],
                        "at": r2(l10_start + 2.20),
                        "dur": 0.50,
                    },
                    {
                        "type": "focus_highlight",
                        "pos": [0.50, 0.48],
                        "radius": [0.46, 0.38],
                        "dim_outer": 0.20,
                        "start": r2(s7_start + 0.55),
                        "end": r2(s7_end - 0.10),
                        "fade": 0.30,
                    },
                    {
                        "type": "color_mood",
                        "mood": "noir_evidence",
                        "strength": 0.40,
                        "vignette": 0.20,
                        "grain": 0.010,
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
                "motion_intent": "Giữ tĩnh tuyệt đối trên nền sạp chợ nắng ấm dịu mắt cho Thẻ Nhớ kỹ 5.0s",
                "motion": {"preset": "static_hold"},
                "transition_in": {"type": "fade_black", "dur": 0.28},
            },
            {
                "id": "s9a_ket_mo_co_tu_an_y",
                "image": "assets/s9a_cotu_mouth_closed.jpg",
                "start": s9a_start,
                "end": s9a_end,
                "beat_type": "suspicion",
                "motion_level": "C",
                "motion_intent": "Kết mở 100% câm thoại (cùng nhân vật Cô Tư EP12 — không thoại ra lệnh, an toàn pháp lý): tắt vẻ hiền hậu, khép môi ánh mắt lạnh sắc áp điện thoại báo kín + 1 cái chớp mắt chậm + slow_pull_out + noir_evidence",
                "motion": {
                    "preset": "slow_pull_out",
                    "scale": [1.08, 1.02],
                    "focus": [[0.48, 0.44], [0.50, 0.48]],
                    "wobble": "none",
                    "easing": "ease_out",
                },
                "detail_fx": [
                    {
                        "type": "eye_blink",
                        "image": "assets/s9a_cotu_blink.jpg",
                        "region": rois["s9a_cotu_eye"],
                        "feather": 0.008,
                        "times": [r2(s9a_start + 1.15)],
                        "close_dur": 0.070,
                        "hold_dur": 0.065,
                        "open_dur": 0.110,
                    },
                    {
                        "type": "color_mood",
                        "mood": "noir_evidence",
                        "strength": 0.36,
                        "vignette": 0.24,
                        "grain": 0.010,
                    },
                ],
                "transition_in": {"type": "fade_black", "dur": 0.32},
            },
            {
                "id": "s9b_ket_mo_hai_bong_lung_bi_an",
                "image": "assets/s9b.jpg",
                "start": s9b_start,
                "end": s9b_end,
                "beat_type": "climax",
                "motion_level": "B",
                "motion_intent": "Kết mở 2.5D Parallax 100% câm thoại bí ẩn: dưới bóng râm cổng chợ, hai bóng lưng đội nón bảo hiểm kính râm (không lộ rõ mặt, không sắc phục) tắt máy điện thoại khẽ ra tín hiệu rồi hòa vào dòng xe phía sau bóng áo xanh + Rack Focus + Breathing + light_sweep + ambient_particles",
                "motion": {
                    "preset": "slow_push_in",
                    "scale": [1.02, 1.08],
                    "focus": [[0.50, 0.50], [0.50, 0.46]],
                    "wobble": "none",
                    "easing": "ease_out",
                },
                "parallax": {
                    "camera": "push_in",
                    "dolly": [1.02, 1.08],
                    "shift_x": [0.0, 0.0],
                    "shift_y": [1.8, -2.0],
                    "focus": [0.50, 0.48],
                    "strength": 0.85,
                    "easing": "ease_out",
                    "layers": [
                        {
                            "role": "bg",
                            "image": "assets/s9b_bg.jpg",
                            "depth": 0.42,
                            "blur_from": 3.4,
                            "blur_to": 0.4,
                            "blur_at": r2(s9b_start + 0.65),
                            "blur_dur": 1.6,
                        },
                        {
                            "role": "fg",
                            "image": "assets/s9b_fg.png",
                            "depth": 1.26,
                            "breathe_y": 1.6,
                            "breathe_period": 3.4,
                        },
                    ],
                },
                "detail_fx": [
                    {
                        "type": "ambient_particles",
                        "count": 18,
                        "opacity": 0.28,
                        "color": [230, 240, 255],
                        "drift_dir": "up",
                    },
                    {
                        "type": "light_sweep",
                        "mode": "light",
                        "intensity": 0.22,
                        "repeat": 1,
                    },
                    {
                        "type": "color_mood",
                        "mood": "cold_suspicion",
                        "strength": 0.30,
                        "vignette": 0.22,
                        "grain": 0.008,
                    },
                ],
                "transition_in": {"type": "dissolve", "dur": 0.25},
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
                "speaker": "ke_ngot_ngao_nam",
                "af": "default",
                "start": l1_start,
                "window": r2(s1_end - l1_start - 0.05),
                "text": "Chuyển bốn triệu rưỡi thành công rồi nè em! Xe đậu ngoài đường, giao hàng lẹ giùm!",
                "style": "Giọng nam thanh niên miền Nam Sài Gòn 28 tuổi nói trực tiếp tại quầy hàng, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, giữ cố định một âm sắc; hồ hởi lịch sự nhưng cố tình thúc giục gấp gáp để lấy hàng nhanh.",
            },
            {
                "id": "l2",
                "speaker": "be_na",
                "start": l2_start,
                "window": r2(s2_end - l2_start - 0.05),
                "text": "Cô Tư yên tâm, đâu phải hình chụp! Con đứng nhìn tận mắt ảnh bấm chuyển trên app luôn!",
                "style": "Giọng cô gái trẻ miền Nam Sài Gòn 20 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, giữ cố định một âm sắc trong trẻo tự nhiên; vui vẻ tự tin trấn an Cô Tư vì vừa thấy tận mắt khách thao tác trên điện thoại.",
            },
            {
                "id": "l3",
                "speaker": "co_tu",
                "start": l3_start,
                "window": r2(s3_end - l3_start - 0.05),
                "text": "Khoan đã Na! Máy cô im ru chưa báo tiền vô, anh chờ tiền nổi rồi hãy lấy!",
                "style": "Giọng phụ nữ miền Nam Sài Gòn ngoài 50 tuổi bán hàng chợ, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, giữ cố định một âm sắc rõ chữ, điềm tĩnh, dứt khoát và tỉnh táo khi cản cháu lại.",
            },
            {
                "id": "l4",
                "speaker": "ke_ngot_ngao_nam",
                "af": "default",
                "start": l4_start,
                "window": r2(l4b_start - l4_start - 0.05),
                "text": "Trời ơi, máy tôi báo trừ tiền rồi! Giờ trả tiền mặt, lát tiền nổi thành hai lần sao?!",
                "style": "Giọng nam thanh niên miền Nam Sài Gòn 28 tuổi nói trực tiếp tại quầy, giữ cố định cùng một âm sắc; giọng đẩy cao hơi bực bội đầy lý lẽ, cố tình gây áp lực khiến người bán áy náy sợ làm khó khách.",
            },
            {
                "id": "l4b",
                "speaker": "ke_ngot_ngao_nam",
                "af": "default",
                "start": l4b_start,
                "window": r2(l5_start - l4b_start - 0.05),
                "text": "Lừa cả trăm cả tỷ, ai lừa mấy đồng bạc cô ơi!",
                "style": "Giọng nam thanh niên miền Nam Sài Gòn 28 tuổi nói trực tiếp tại quầy, giữ cố định cùng một âm sắc; giọng châm biếm tỏ vẻ tự ái phóng khoáng để đánh vào tâm lý cả nể của người bán hàng.",
            },
            {
                "id": "l5",
                "speaker": "be_na",
                "start": l5_start,
                "window": r2(s4_end - l5_start - 0.05),
                "text": "Cô ơi... lỡ nghẽn mạng thiệt, ảnh trả tiền mặt rồi lát tiền vô nữa sao cô?",
                "style": "Giọng cô gái trẻ miền Nam Sài Gòn 20 tuổi, giữ cố định cùng một âm sắc trong trẻo tự nhiên; hạ giọng bối rối ngập ngừng lo lắng quay sang hỏi Cô Tư vì thấy lý lẽ của khách nghe quá hợp lý.",
            },
            {
                "id": "l6",
                "speaker": "co_tu",
                "start": l6_start,
                "window": r2(l7_start - l6_start - 0.05),
                "text": "Sạp cô ngồi đây có chạy đâu! Anh đưa tiền mặt cô ký giấy, tiền nổi cô hoàn đủ!",
                "style": "Giọng phụ nữ miền Nam Sài Gòn ngoài 50 tuổi, giữ cố định cùng một âm sắc rõ chữ; giọng chắc nịch, sòng phẳng, đàng hoàng và đầy bản lĩnh của người bán hàng lâu năm.",
            },
            {
                "id": "l7",
                "speaker": "co_tu",
                "start": l7_start,
                "window": r2(s5_end - l7_start - 0.05),
                "text": "Hay đọc số tài khoản, cô gọi ngân hàng hỏi!",
                "style": "Giọng phụ nữ miền Nam Sài Gòn ngoài 50 tuổi, giữ cố định cùng một âm sắc rõ chữ; điềm tĩnh, sắc sảo và dứt khoát kiểm chứng qua tổng đài ngân hàng chứ tuyệt đối không nhìn màn hình tay khách.",
            },
            {
                "id": "l8",
                "speaker": "ke_ngot_ngao_nam",
                "af": "default",
                "start": l8_start,
                "window": r2(s6a_end - l8_start - 0.05),
                "text": "Thôi... bán buôn khó khăn quá, khỏi mua nữa!",
                "style": "Giọng nam thanh niên miền Nam Sài Gòn 28 tuổi nói trực tiếp, giữ cố định cùng một âm sắc; chột dạ cứng họng, cố giả bộ gắt gỏng khó chịu để quay lưng chuồn nhanh.",
            },
            {
                "id": "l9",
                "speaker": "be_na",
                "start": l9_start,
                "window": r2(s6b_end - l9_start - 0.05),
                "text": "Ủa... tiền chuyển rồi mà ảnh bỏ luôn hàng, leo xe vọt thẳng luôn kìa cô!",
                "style": "Giọng cô gái trẻ miền Nam Sài Gòn 20 tuổi, giữ cố định cùng một âm sắc trong trẻo tự nhiên; bàng hoàng sửng sốt khi chợt hiểu ra sự thật trước mắt.",
            },
            {
                "id": "l10",
                "speaker": "nguoi_boc_tran",
                "start": l10_start,
                "window": r2(s7_end - l10_start - 0.05),
                "text": "Không còn ảnh cắt ghép: app ngân hàng giả bấm thành công như thật, nhưng tiền không về máy bạn!",
                "style": "Giọng nam trung niên miền Nam Sài Gòn 40 tuổi, phát âm chuẩn phương ngữ miền Nam, trầm tĩnh, sắc lạnh và gọn dứt khoát; nhấn rõ app ngân hàng giả và tiền không về máy bạn.",
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
                "Khách chủ động chìa màn hình cho nhìn tận mắt bấm “Thành công” bằng app ngân hàng giả giống thật",
                "Kì kèo “trả tiền mặt thành hai lần sao”, “ai lừa mấy đồng bạc” để đánh vào tâm lý cả nể",
                "App giả dựng được cả màn hình lịch sử — hễ đòi đọc STK gọi ngân hàng hỏi hoặc ký giấy nhận tiền mặt là bỏ chạy",
            ],
            "action": "Nguyên tắc “Kiểm trước, tin sau”: tiền chưa nổi trên máy mình hoặc loa báo số dư thì chưa giao hàng · Khách vội cứ nhận tiền mặt có giấy hẹn hoàn hoặc xin STK gọi tổng đài ngân hàng tra soát!",
        },
        "disclaimer": {
            "start": s10_start,
            "end": s10_end,
        },
        "audio": {
            "duck_ambience_db": -6.0,
            "ambience": [
                {"preset": "crowd", "start": s1_start, "end": s7_start, "gain_db": -8.5},
                {"preset": "room_tone", "start": s7_start, "end": s9b_start, "gain_db": -7.5},
                {"preset": "street", "start": s9b_start, "end": s10_start, "gain_db": -7.5},
                {"preset": "room_tone", "start": s10_start, "end": s10_end, "gain_db": -10.0},
            ],
            "foley": [
                # s1: bấm app giả (CHỈ click + counter_tick — tuyệt đối KHÔNG bank_ting!)
                {"preset": "click", "at": 0.25, "gain_db": 0.8},
                {"preset": "counter_tick", "at": 0.50, "gain_db": -1.5},
                {"preset": "counter_tick", "at": 1.35, "gain_db": -2.0},
                # s3: máy Cô Tư & loa im ru
                {"preset": "low_accent", "at": r2(s3_start + 1.15), "dur": 0.9, "gain_db": 0.6},
                {"preset": "marker_draw", "at": r2(s3_start + 1.45), "dur": 0.48, "gain_db": 0.8},
                # s4: twist kì kèo căng thẳng
                {"preset": "heartbeat", "at": r2(s4_start + 0.40), "dur": r2(max(2.0, s4_end - s4_start - 0.70)), "gain_db": -2.6},
                # s5: Cô Tư đặt sổ bút dứt khoát
                {"preset": "click", "at": r2(l6_start + 1.15), "gain_db": 0.8},
                {"preset": "low_accent", "at": r2(l6_start + 1.25), "dur": 0.85, "gain_db": 0.5},
                # s6a/s6b: lộ màn hình app giả + chạy vọt ra xe máy
                {"preset": "impact", "at": r2(s6a_start + 0.35), "dur": 0.90, "gain_db": 1.4},
                {"preset": "glitch", "at": r2(s6a_start + 0.40), "dur": 0.28, "gain_db": 0.4},
                {"preset": "footsteps", "at": r2(s6a_end - 0.55), "dur": 1.35, "gain_db": -0.8},
                {"preset": "low_accent", "at": r2(s6b_start + 0.25), "dur": 0.85, "gain_db": 0.4},
                # s7: bóc trần
                {"preset": "glitch", "at": r2(s7_start + 0.05), "dur": 0.34, "gain_db": 1.0},
                {"preset": "low_accent", "at": r2(s7_start + 0.55), "dur": 0.9, "gain_db": 0.8},
                {"preset": "marker_draw", "at": r2(l10_start + 0.60), "dur": 0.48, "gain_db": 0.8},
                {"preset": "marker_draw", "at": r2(l10_start + 2.20), "dur": 0.48, "gain_db": 0.8},
                # s9a/s9b: kết mở 100% câm thoại đầy ẩn ý (Cô Tư EP12 + 2 bóng lưng bí ẩn)
                {"preset": "click", "at": r2(s9a_start + 0.45), "gain_db": -0.5},
                {"preset": "heartbeat", "at": r2(s9a_start + 0.55), "dur": r2(max(2.0, s9a_end - s9a_start - 0.70)), "gain_db": -2.6},
                {"preset": "low_accent", "at": r2(s9b_start + 0.30), "dur": 0.90, "gain_db": 0.8},
                {"preset": "click", "at": r2(s9b_start + 1.05), "gain_db": -1.0},
                {"preset": "impact", "at": r2(s9b_end - 0.35), "dur": 0.90, "gain_db": 1.4},
            ],
            "bgm": [
                {"preset": "suspense_pulse", "start": s1_start, "end": s4_start, "gain_db": -1.8},
                {"preset": "tension_drone", "start": s4_start, "end": s7_start, "gain_db": 0.4},
                {"preset": "investigative_story", "start": s7_start, "end": s8_start, "gain_db": 0.5},
                {"preset": "warm_outro", "start": s8_start, "end": s9a_start, "gain_db": 0.0},
                {"preset": "tension_drone", "start": s9a_start, "end": s10_start, "gain_db": 0.6},
            ],
            "duck_extra": [],
        },
        "forbidden_terms": [],
        "publish": {
            "titles": [
                "Thấy tận mắt khách bấm chuyển, kì kèo \"trả tiền mặt thành 2 lần sao?\" — Lật mặt app ngân hàng giả! #shorts #bóctrầnlừađảo",
                "Không còn là ảnh bill cắt ghép: App ngân hàng giả bấm thành công ngay trước mặt chủ quán! #shorts #cảnhgiáclừađảo",
                "Gửi ngay cho người nhà buôn bán: Khách giục lấy hàng khi máy mình chưa báo tiền, xử lý sao cho khéo? #shorts #vạnchuyện",
            ],
            "description": (
                "Kẻ gian giờ không chỉ chỉnh sửa ảnh chụp biên lai nữa, mà cài hẳn ứng dụng ngân hàng giả mạo giống gần như y hệt thật: chủ động chìa màn hình cho người bán nhìn tận mắt bấm nút chuyển khoản hiện dấu tích xanh “Thành công” rồi giục giao hàng ngay!\n\n"
                "Cao tay hơn, khi chủ quán giữ hàng vì máy mình chưa báo tiền, chúng còn phản công bằng đòn tâm lý rất dễ khiến người bán áy náy: “Máy tôi báo trừ tiền rồi, giờ trả tiền mặt nữa lát tiền nổi thành hai lần sao?!”.\n\n"
                "Cách xử lý vừa sòng phẳng với khách thật, vừa lật mặt kẻ gian ngay lập tức:\n"
                "1. Nguyên tắc vàng “Kiểm trước, tin sau”: tiền chưa nổi trên chính ứng dụng ngân hàng hoặc loa báo biến động số dư của mình thì chưa giao hàng.\n"
                "2. Nếu khách vội: quán cố định cứ nhận tiền mặt và ghi giấy ký nhận — cam kết hoàn lại đủ 100% nếu lát nữa tiền chuyển khoản nổi về.\n"
                "3. Không xem lịch sử trên máy khách (app giả vẫn dựng giả lập được cả mục lịch sử): muốn đối chiếu thì xin số tài khoản người gửi để tự gọi tổng đài ngân hàng hỏi, hoặc mời đứng chờ tiền nổi.\n"
                "4. Đã lỡ bị lừa: lưu giữ bằng chứng, trích xuất camera và trình báo ngay cơ quan công an nơi gần nhất."
            ),
            "pinned_comment": (
                "📌 Gửi ngay video này cho ba mẹ, cô chú bán hàng và bạn bè làm kinh doanh! "
                "Kẻ gian giờ dùng app ngân hàng giả bấm “Thành công” (thậm chí dựng luôn cả màn hình lịch sử trừ tiền) rồi kì kèo “trả tiền mặt thành hai lần sao?”, “lừa cả trăm cả tỷ ai lừa mấy đồng bạc” để đánh vào tâm lý cả nể. "
                "Nhớ đúng nguyên tắc Kiểm trước, tin sau: tiền chưa nổi máy mình thì chưa giao hàng — khách vội cứ nhận tiền mặt ký giấy hẹn hoàn lại, hoặc xin STK gọi tổng đài ngân hàng hỏi trực tiếp! "
                "Lưu ý: Vài giây kết mở mang tính mạch phim hư cấu; ngoài đời khi phát hiện dấu hiệu lừa đảo hãy giữ an toàn, lưu bằng chứng và trình báo cơ quan công an (không tự ý theo dõi, không đăng SĐT/STK hay tên người thật dưới phần bình luận nhé)."
            ),
            "hashtags": ["#shorts", "#bóctrầnlừađảo", "#cảnhgiáclừađảo"],
            "tags": [
                "bẫy app ngân hàng giả",
                "biên lai chuyển khoản giả",
                "kiểm trước tin sau",
                "lừa đảo tiểu thương",
                "bóc trần lừa đảo",
                "vạn chuyện",
                "shorts",
            ],
            "category": "Education (Giáo dục)",
            "playlist": "Bóc Trần Lừa Đảo – Kỹ Năng Cảnh Giác & An Toàn Đời Thực",
            "thumbnail_sec": r2(s6a_start + 1.15),
        },
    }

    OUT_JSON.write_text(json.dumps(ep, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Đã biên dịch {OUT_JSON} ({total_dur:.2f}s · mode={'REAL_TTS' if has_real_tts else 'DRAFT'})")
    return ep


if __name__ == "__main__":
    build()
