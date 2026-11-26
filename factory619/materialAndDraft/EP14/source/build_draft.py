# -*- coding: utf-8 -*-
"""
Single Source of Truth cho `factory619/materialAndDraft/EP14` (`BayBaoHanhMayLanh`).

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
        "l1": 5.0,
        "l2": 5.0,
        "l3": 5.2,
        "l4": 4.8,
        "l5": 5.2,
        "l6": 4.8,
        "l7": 5.4,
        "l8": 5.5,
        "l9": 4.67,
        "l10": 4.2,
        "l11": 3.8,
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
        "s1_anhhai_eye": [0.612, 0.593, 0.798, 0.647],
        "s1_anhhai_mouth": [0.642, 0.653, 0.748, 0.699],
        "s2_anhhai_eye": [0.612, 0.448, 0.838, 0.512],
        "s2_anhhai_mouth": [0.682, 0.548, 0.803, 0.605],
        "s3_chihai_eye": [0.257, 0.508, 0.453, 0.572],
        "s3_chihai_mouth": [0.316, 0.578, 0.434, 0.632],
        "s3_anhhai_eye": [0.577, 0.468, 0.793, 0.523],
        "s3_anhhai_mouth": [0.628, 0.533, 0.773, 0.587],
        "s4_anhhai_eye": [0.395, 0.360, 0.600, 0.435],
        "s4_anhhai_mouth": [0.450, 0.485, 0.565, 0.555],
        "s5_anhhai_eye": [0.542, 0.463, 0.808, 0.522],
        "s5_anhhai_mouth": [0.602, 0.548, 0.778, 0.627],
        "s6_chihai_eye": [0.257, 0.513, 0.453, 0.572],
        "s6_chihai_mouth": [0.327, 0.578, 0.433, 0.629],
        "s6_anhhai_eye": [0.587, 0.448, 0.798, 0.502],
        "s6_tech_eye": [0.587, 0.213, 0.693, 0.255],
        "s6_tech_mouth": [0.607, 0.245, 0.688, 0.285],
        # Detail / evidence region overrides
        "s2_ad_circle": [0.130, 0.680, 0.235, 0.728],
        "s6_seal_circle": [0.640, 0.095, 0.800, 0.155],
        "s7_ad_circle": [0.155, 0.186, 0.705, 0.256],
        "s7_safe_highlight": [0.505, 0.575, 0.845, 0.825],
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
    s2_end = r2(l2_start + durs["l2"] + 0.60)

    s3_start = s2_end
    l3_start = r2(s3_start + 0.40)
    l4_start = r2(l3_start + durs["l3"] + 0.30)
    s3_end = r2(l4_start + durs["l4"] + 0.55)

    # Scene 4: Split-screen sau 2 ngày im bặt -> báo giá 3tr -> đồng ý (l5 + l6)
    # Scene 5: Thêm 5 ngày nữa mất hút (tổng 7 ngày) -> gọi số đầu gào đòi ráp (s5.jpg · l7)
    s4_start = s3_end
    l5_start = r2(s4_start + 0.45)
    l6_start = r2(l5_start + durs["l5"] + 0.35)
    s4_end = r2(l6_start + durs["l6"] + 0.55)

    s5_start = s4_end
    l7_start = r2(s5_start + 0.45)
    s5_end = r2(l7_start + durs["l7"] + 0.55)

    s6_start = s5_end
    l8_start = r2(s6_start + 0.45)
    l9_start = r2(l8_start + durs["l8"] + 0.35)
    s6_end = r2(l9_start + durs["l9"] + 0.55)

    s7_start = s6_end
    l10_start = r2(s7_start + 0.35)
    s7_end = r2(l10_start + durs["l10"] + 0.55)

    s8_start = s7_end
    s8_end = r2(s8_start + 5.00)  # Thẻ NHỚ KỸ 5.0s (toàn bộ lời khuyên nằm gọn tại đây)

    s9_start = s8_end
    l11_start = r2(s9_start + 0.90)  # Nhịp lặng 0.9s lộ bóng lưng Ông Tám + lắc bạc + ánh xanh ngọc
    s9_end = r2(l11_start + durs["l11"] + 1.05)  # Dư âm quyền lực mềm trước khi cắt đen

    s10_start = s9_end
    s10_end = r2(s10_start + 2.70)  # Bảng LƯU Ý 2.7s

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
        "episode_id": "EP14",
        "slug": "BayBaoHanhMayLanh",
        "title": "Bẫy bảo hành máy lạnh giả – Mạo danh trung tâm lớn, giữ bo ép bỏ đề phòng!",
        "version": "v5-level3-ongtam-coda-real-tts" if has_real_tts else "v5-level3-ongtam-coda-draft",
        "scam_family": "VAR-MIX-01",
        "motion_upgrade": "level3",
        "duration_sec": total_dur,
        "hook": {
            "kicker": "BẪY BẢO HÀNH MÁY LẠNH",
            "title": "Mạo danh trung tâm lớn, giữ bo ép giá!",
            "start": 0.25,
            "end": r2(min(4.85, s1_end - 0.35)),
        },
        "scenes": [
            {
                "id": "s1_hook_thao_bung_ca_tuan",
                "image": "assets/s1.jpg",
                "start": s1_start,
                "end": s1_end,
                "beat_type": "establishing",
                "motion_level": "C",
                "motion_intent": "Phòng tối nóng nực, máy lạnh tháo bung trơ dây, Anh Hai cầm biên nhận gọi không ai nghe + animated_counter 7 NGÀY + screen_glow + high_tension",
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
                        "image": "assets/s1_anhhai_blink.jpg",
                        "region": rois["s1_anhhai_eye"],
                        "feather": 0.008,
                        "times": blink_times(s1_start, s1_end, 1.4, 3.0),
                        "close_dur": 0.055,
                        "hold_dur": 0.045,
                        "open_dur": 0.085,
                    },
                    {
                        "type": "mouth_sync",
                        "speaker": "anh_hai",
                        "line_ids": ["l1"],
                        "region": rois["s1_anhhai_mouth"],
                        "feather": 0.008,
                        "closed_image": "assets/s1_anhhai_mouth_closed.jpg",
                        "mid_image": "assets/s1.jpg",
                        "open_image": "assets/s1_anhhai_mouth_open.jpg",
                        "fps": 12,
                        "thresh_mid": 0.14,
                        "thresh_open": 0.64,
                    },
                    {
                        "type": "animated_counter",
                        "start": 0.45,
                        "end": r2(s1_end - 0.15),
                        "count_dur": 2.2,
                        "from_val": 1,
                        "to_val": 7,
                        "fmt": "int",
                        "suffix": " NGÀY",
                        "label": "ÔM BO · NÓNG NGỘP",
                        "pos": [0.26, 0.255],
                        "style": "danger",
                        "easing": "ease_out",
                    },
                    {
                        "type": "screen_glow",
                        "pos": [0.80, 0.65],
                        "radius": [0.18, 0.15],
                        "color": [255, 130, 80],
                        "intensity": 0.18,
                        "mode": "pulse",
                        "start": 0.20,
                        "end": r2(s1_end - 0.10),
                        "fade": 0.25,
                    },
                    {
                        "type": "color_mood",
                        "mood": "high_tension",
                        "strength": 0.28,
                        "vignette": 0.18,
                        "grain": 0.008,
                    },
                ],
            },
            {
                "id": "s2_bam_so_top_dau",
                "image": "assets/s2.jpg",
                "start": s2_start,
                "end": s2_end,
                "beat_type": "normal",
                "motion_level": "B",
                "motion_intent": "2.5D Parallax phòng khách ban ngày + Rack Focus mờ máy lạnh báo lỗi nền + Breathing + Head Micro-Tilt + Anh Hai chớp mắt & chép miệng 4 trạng thái (round_image) + red_circle_draw khoanh nhãn quảng cáo top đầu",
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
                            "blur_dur": 2.6,
                        },
                        {
                            "role": "fg",
                            "image": "assets/s2_fg.png",
                            "depth": 1.24,
                            "breathe_y": 2.0,
                            "breathe_period": 3.6,
                            "head_tilt_deg": 1.0,
                            "head_pivot": [0.74, 0.78],
                            "tilt_speaker": "anh_hai",
                            "tilt_line_ids": ["l2"],
                        },
                    ],
                },
                "detail_fx": [
                    {
                        "type": "eye_blink",
                        "image": "assets/s2_anhhai_blink.jpg",
                        "region": rois["s2_anhhai_eye"],
                        "feather": 0.008,
                        "times": blink_times(s2_start, s2_end, 1.1, 3.0),
                        "close_dur": 0.055,
                        "hold_dur": 0.045,
                        "open_dur": 0.085,
                        "layer": "fg",
                    },
                    {
                        "type": "mouth_sync",
                        "speaker": "anh_hai",
                        "line_ids": ["l2"],
                        "region": rois["s2_anhhai_mouth"],
                        "feather": 0.008,
                        "closed_image": "assets/s2_anhhai_mouth_closed.jpg",
                        "mid_image": "assets/s2.jpg",
                        "open_image": "assets/s2_anhhai_mouth_open.jpg",
                        "round_image": "assets/s2_anhhai_mouth_round.jpg",
                        "fps": 12,
                        "thresh_mid": 0.14,
                        "thresh_open": 0.64,
                        "layer": "fg",
                    },
                    {
                        "type": "red_circle_draw",
                        "region": rois["s2_ad_circle"],
                        "at": r2(s2_start + 2.40),
                        "dur": 0.50,
                        "style": "circle",
                    },
                ],
                "transition_in": {"type": "dissolve", "dur": 0.25},
            },
            {
                "id": "s3_nghi_nhung_ngai_duoi",
                "image": "assets/s3.jpg",
                "start": s3_start,
                "end": s3_end,
                "beat_type": "suspicion",
                "motion_level": "C",
                "motion_intent": "Quét trái phòng khách ban ngày: 2 thợ mặc đồ thường tháo máy phía sau, Chị Hai kéo áo thì thầm nghi ngờ và Anh Hai ái ngại lưỡng lự + Living-Char cả 2 vợ chồng",
                "motion": {
                    "preset": "pan_left",
                    "scale": [1.06, 1.06],
                    "focus": [[0.53, 0.50], [0.47, 0.50]],
                    "wobble": "none",
                    "easing": "smoothstep",
                },
                "detail_fx": [
                    {
                        "type": "eye_blink",
                        "image": "assets/s3_chihai_blink.jpg",
                        "region": rois["s3_chihai_eye"],
                        "feather": 0.008,
                        "times": blink_times(s3_start, s3_end, 1.3, 3.2),
                        "close_dur": 0.055,
                        "hold_dur": 0.045,
                        "open_dur": 0.085,
                    },
                    {
                        "type": "mouth_sync",
                        "speaker": "chi_hai",
                        "line_ids": ["l3"],
                        "region": rois["s3_chihai_mouth"],
                        "feather": 0.008,
                        "closed_image": "assets/s3_chihai_mouth_closed.jpg",
                        "mid_image": "assets/s3.jpg",
                        "open_image": "assets/s3_chihai_mouth_open.jpg",
                        "fps": 12,
                        "thresh_mid": 0.14,
                        "thresh_open": 0.64,
                    },
                    {
                        "type": "eye_blink",
                        "image": "assets/s3_anhhai_blink.jpg",
                        "region": rois["s3_anhhai_eye"],
                        "feather": 0.008,
                        "times": blink_times(s3_start, s3_end, 2.2, 3.4),
                        "close_dur": 0.055,
                        "hold_dur": 0.045,
                        "open_dur": 0.085,
                    },
                    {
                        "type": "mouth_sync",
                        "speaker": "anh_hai",
                        "line_ids": ["l4"],
                        "region": rois["s3_anhhai_mouth"],
                        "feather": 0.008,
                        "closed_image": "assets/s3_anhhai_mouth_closed.jpg",
                        "mid_image": "assets/s3.jpg",
                        "open_image": "assets/s3_anhhai_mouth_open.jpg",
                        "fps": 12,
                        "thresh_mid": 0.14,
                        "thresh_open": 0.64,
                    },
                    {
                        "type": "color_mood",
                        "mood": "cold_suspicion",
                        "strength": 0.22,
                        "vignette": 0.12,
                        "grain": 0.0,
                    },
                ],
                "transition_in": {"type": "dissolve", "dur": 0.25},
            },
            {
                "id": "s4_split_bao_gia_ba_trieu",
                "image": "assets/s4_scammer.jpg",
                "start": s4_start,
                "end": s4_end,
                "beat_type": "climax",
                "motion_level": "C",
                "motion_intent": "Level 3 split_screen trên-dưới: sau 2 ngày ôm bo im bặt cho nhà nóng ngộp, kẻ mạo danh mới gọi báo giá 3 triệu hứa làm liền (panel trên) & Anh Hai bỏ hết đề phòng đồng ý đại để có máy xài liền (panel dưới + Living-Char)",
                "split_screen": {
                    "layout": "horizontal",
                    "ratio": 0.40,
                    "divider_width": 6,
                    "inactive_dim": 0.18,
                    "slide_in_dur": 0.30,
                    "panels": [
                        {
                            "image": "assets/s4_scammer.jpg",
                            "speaker": "ke_gia_danh",
                            "line_ids": ["l5"],
                            "label": "",
                            "label_rgb": [245, 90, 95],
                            "waveform": True,
                            "waveform_rgb": [255, 110, 110],
                            "crop_x": 0.50,
                            "crop_y": 0.54,
                            "motion": {"preset": "slow_push_in", "scale": [1.02, 1.07], "focus": [[0.50, 0.52], [0.50, 0.50]]},
                            "detail_fx": [],
                        },
                        {
                            "image": "assets/s4_anhhai.jpg",
                            "speaker": "anh_hai",
                            "line_ids": ["l6"],
                            "label": "",
                            "label_rgb": [255, 200, 95],
                            "waveform": True,
                            "waveform_rgb": [255, 215, 120],
                            "crop_x": 0.50,
                            "crop_y": 0.42,
                            "motion": {"preset": "slow_pull_out", "scale": [1.08, 1.03], "focus": [[0.50, 0.48], [0.50, 0.50]]},
                            "detail_fx": [
                                {
                                    "type": "eye_blink",
                                    "image": "assets/s4_anhhai_blink.jpg",
                                    "region": rois["s4_anhhai_eye"],
                                    "region_space": "source",
                                    "feather": 0.008,
                                    "times": blink_times(s4_start, s4_end, 1.6, 3.3),
                                    "close_dur": 0.055,
                                    "hold_dur": 0.045,
                                    "open_dur": 0.085,
                                },
                                {
                                    "type": "mouth_sync",
                                    "speaker": "anh_hai",
                                    "line_ids": ["l6"],
                                    "region": rois["s4_anhhai_mouth"],
                                    "region_space": "source",
                                    "feather": 0.008,
                                    "closed_image": "assets/s4_anhhai_mouth_closed.jpg",
                                    "mid_image": "assets/s4_anhhai.jpg",
                                    "open_image": "assets/s4_anhhai_mouth_open.jpg",
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
                        "type": "animated_counter",
                        "start": r2(s4_start + 0.50),
                        "end": r2(s4_end - 0.15),
                        "count_dur": 1.8,
                        "from_val": 0,
                        "to_val": 3000000,
                        "fmt": "vnd",
                        "label": "SAU 2 NGÀY IM BẶT",
                        "pos": [0.30, 0.15],
                        "style": "danger",
                        "easing": "ease_out",
                    },
                ],
                "transition_in": {"type": "whip_pan_left", "dur": 0.26},
            },
            {
                "id": "s5_them_nam_ngay_mat_hut_goi_gao",
                "image": "assets/s5.jpg",
                "start": s5_start,
                "end": s5_end,
                "beat_type": "climax",
                "motion_level": "C",
                "motion_intent": "Đồng ý 3 triệu xong họ vẫn mất hút thêm 5 ngày (tổng 7 ngày), số biên nhận không ai nghe, Anh Hai phải gọi lại số đầu gào lên đòi ráp gấp + tense_push + chromatic_pulse + shakes + Living-Char Anh Hai",
                "motion": {
                    "preset": "tense_push",
                    "scale": [1.03, 1.11],
                    "focus": [[0.50, 0.52], [0.50, 0.48]],
                    "wobble": "breathe",
                    "easing": "ease_out",
                },
                "detail_fx": [
                    {
                        "type": "eye_blink",
                        "image": "assets/s5_anhhai_blink.jpg",
                        "region": rois["s5_anhhai_eye"],
                        "feather": 0.008,
                        "times": blink_times(s5_start, s5_end, 1.5, 2.9),
                        "close_dur": 0.055,
                        "hold_dur": 0.045,
                        "open_dur": 0.085,
                    },
                    {
                        "type": "mouth_sync",
                        "speaker": "anh_hai",
                        "line_ids": ["l7"],
                        "region": rois["s5_anhhai_mouth"],
                        "feather": 0.008,
                        "closed_image": "assets/s5_anhhai_mouth_closed.jpg",
                        "mid_image": "assets/s5.jpg",
                        "open_image": "assets/s5_anhhai_mouth_open.jpg",
                        "fps": 12,
                        "thresh_mid": 0.14,
                        "thresh_open": 0.64,
                    },
                    {
                        "type": "animated_counter",
                        "start": r2(s5_start + 0.35),
                        "end": r2(s5_end - 0.15),
                        "count_dur": 2.0,
                        "from_val": 2,
                        "to_val": 7,
                        "fmt": "int",
                        "prefix": "NGÀY THỨ ",
                        "label": "THÊM 5 NGÀY MẤT HÚT",
                        "pos": [0.28, 0.18],
                        "style": "danger",
                        "easing": "linear",
                    },
                    {
                        "type": "chromatic_pulse",
                        "at": r2(s5_start + 0.35),
                        "dur": 0.30,
                        "shift_px": 7,
                        "zoom_blur": 0.025,
                    },
                    {
                        "type": "color_mood",
                        "mood": "high_tension",
                        "strength": 0.45,
                        "vignette": 0.22,
                        "grain": 0.012,
                    },
                ],
                "shakes": [{"at": r2(s5_start + 0.35), "amp": 22}],
                "transition_in": {"type": "zoom_punch", "dur": 0.28},
            },
            {
                "id": "s6_tho_hang_boc_tran_tem_rach",
                "image": "assets/s6.jpg",
                "start": s6_start,
                "end": s6_end,
                "beat_type": "anomaly",
                "motion_level": "C",
                "motion_intent": "Quét phải ban ngày: kỹ thuật viên chính hãng soi đèn chỉ tem bảo hành bị rách cạnh bo mạch nguyên vẹn + detail_reveal + red_circle_draw + Living-Char vợ chồng Anh Hai – Chị Hai",
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
                        "image": "assets/s6_reveal.jpg",
                        "at": r2(l9_start - 0.15),
                        "dur": 0.45,
                    },
                    {
                        "type": "red_circle_draw",
                        "region": rois["s6_seal_circle"],
                        "at": r2(l9_start + 0.35),
                        "dur": 0.50,
                        "style": "circle",
                    },
                    {
                        "type": "eye_blink",
                        "image": "assets/s6_chihai_blink.jpg",
                        "region": rois["s6_chihai_eye"],
                        "feather": 0.008,
                        "times": blink_times(s6_start, s6_end, 1.4, 3.2),
                        "close_dur": 0.055,
                        "hold_dur": 0.045,
                        "open_dur": 0.085,
                    },
                    {
                        "type": "mouth_sync",
                        "speaker": "chi_hai",
                        "line_ids": ["l8"],
                        "region": rois["s6_chihai_mouth"],
                        "feather": 0.008,
                        "closed_image": "assets/s6_chihai_mouth_closed.jpg",
                        "mid_image": "assets/s6.jpg",
                        "open_image": "assets/s6_chihai_mouth_open.jpg",
                        "fps": 12,
                        "thresh_mid": 0.14,
                        "thresh_open": 0.64,
                    },
                    {
                        "type": "eye_blink",
                        "image": "assets/s6_anhhai_blink.jpg",
                        "region": rois["s6_anhhai_eye"],
                        "feather": 0.008,
                        "times": blink_times(s6_start, s6_end, 2.3, 3.4),
                        "close_dur": 0.055,
                        "hold_dur": 0.045,
                        "open_dur": 0.085,
                    },
                    {
                        "type": "eye_blink",
                        "image": "assets/s6_tech_blink.jpg",
                        "region": rois["s6_tech_eye"],
                        "feather": 0.006,
                        "times": blink_times(s6_start, s6_end, 1.9, 3.3),
                        "close_dur": 0.055,
                        "hold_dur": 0.045,
                        "open_dur": 0.085,
                    },
                    {
                        "type": "mouth_sync",
                        "speaker": "thang_tun",
                        "line_ids": ["l9"],
                        "region": rois["s6_tech_mouth"],
                        "feather": 0.006,
                        "closed_image": "assets/s6_tech_mouth_closed.jpg",
                        "mid_image": "assets/s6.jpg",
                        "open_image": "assets/s6_tech_mouth_open.jpg",
                        "fps": 12,
                        "thresh_mid": 0.14,
                        "thresh_open": 0.64,
                    },
                ],
                "transition_in": {"type": "whip_pan_left", "dur": 0.26},
            },
            {
                "id": "s7_boc_tran_quang_cao_top_dau",
                "image": "assets/s7.jpg",
                "start": s7_start,
                "end": s7_end,
                "beat_type": "anomaly",
                "motion_level": "C",
                "motion_intent": "Kính lúp đỏ bóc trần bẫy quảng cáo top đầu vs phiếu bảo hành & tem máy chính hãng + glitch + detail_reveal + red_circle_draw + highlighter_sweep",
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
                        "region": rois["s7_ad_circle"],
                        "at": r2(l10_start + 0.55),
                        "dur": 0.50,
                        "style": "circle",
                    },
                    {
                        "type": "highlighter_sweep",
                        "region": [0.04, 0.72, 0.47, 0.85],
                        "at": r2(l10_start + 1.85),
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
                        "strength": 0.42,
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
                "motion_intent": "Giữ tĩnh tuyệt đối trên nền phòng khách mát nắng dịu cho Thẻ Nhớ kỹ 5.0s",
                "motion": {"preset": "static_hold"},
                "transition_in": {"type": "fade_black", "dur": 0.28},
            },
            {
                "id": "s9_ket_mo_ong_tam_quyen_luc_mem",
                "image": "assets/s9.jpg",
                "start": s9_start,
                "end": s9_end,
                "beat_type": "suspicion",
                "motion_level": "B",
                "motion_intent": "Kết mở quyền lực mềm 2.5D Parallax (fade_black): chỉ lộ bóng lưng Ông Tám (tóc muối tiêu, áo polo đen, lắc bạc EP07) bên tách trà & điện thoại ánh xanh ngọc lục bảo (tín hiệu ngầm Chị Hai) + Rack Focus + Breathing + screen_glow + ambient_particles + noir_evidence",
                "motion": {
                    "preset": "slow_pull_out",
                    "scale": [1.07, 1.01],
                    "focus": [[0.52, 0.48], [0.50, 0.50]],
                    "wobble": "none",
                    "easing": "ease_out",
                },
                "parallax": {
                    "camera": "pull_out",
                    "dolly": [1.07, 1.01],
                    "shift_x": [0.0, 0.0],
                    "shift_y": [-2.0, 1.8],
                    "focus": [0.50, 0.50],
                    "strength": 0.85,
                    "easing": "ease_out",
                    "layers": [
                        {
                            "role": "bg",
                            "image": "assets/s9_bg.jpg",
                            "depth": 0.42,
                            "blur_from": 3.6,
                            "blur_to": 0.4,
                            "blur_at": r2(s9_start + 0.70),
                            "blur_dur": 1.5,
                        },
                        {
                            "role": "fg",
                            "image": "assets/s9_fg.png",
                            "depth": 1.28,
                            "breathe_y": 1.6,
                            "breathe_period": 3.8,
                        },
                    ],
                },
                "detail_fx": [
                    {
                        "type": "screen_glow",
                        "pos": [0.41, 0.54],
                        "radius": [0.14, 0.10],
                        "color": [24, 196, 142],
                        "intensity": 0.24,
                        "mode": "pulse",
                        "start": r2(s9_start + 0.25),
                        "end": r2(s9_end - 0.10),
                        "fade": 0.30,
                    },
                    {
                        "type": "ambient_particles",
                        "count": 18,
                        "opacity": 0.28,
                        "color": [205, 238, 226],
                        "drift_dir": "up",
                    },
                    {
                        "type": "color_mood",
                        "mood": "noir_evidence",
                        "strength": 0.30,
                        "vignette": 0.24,
                        "grain": 0.010,
                    },
                ],
                "transition_in": {"type": "fade_black", "dur": 0.35},
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
                "speaker": "anh_hai",
                "start": l1_start,
                "window": r2(s1_end - l1_start - 0.05),
                "text": "Mình ơi, họ ôm bo cả tuần rồi, nhà ống nóng ngộp chịu không nổi!",
                "style": "Giọng nam miền Nam Sài Gòn 35 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, giữ cố định một âm sắc rõ chữ tự nhiên; đang than thở sốt ruột trực tiếp với vợ giữa căn nhà ống nóng ngộp thở.",
            },
            {
                "id": "l2",
                "speaker": "anh_hai",
                "start": l2_start,
                "window": r2(s2_end - l2_start - 0.05),
                "text": "Máy mới mua tám tháng cứ ngắt! Để anh tìm trung tâm lớn trên mạng gọi liền!",
                "style": "Giọng nam miền Nam Sài Gòn 35 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, giữ cố định cùng một âm sắc tự nhiên; nói chuyện đời thường với vợ khi cúi bấm điện thoại tìm trung tâm bảo hành lớn.",
            },
            {
                "id": "l3",
                "speaker": "chi_hai",
                "start": l3_start,
                "window": r2(l4_start - l3_start - 0.05),
                "text": "Ủa anh ơi, sao họ mặc đồ thường chẳng có đồng phục siêu thị? Em thấy nghi nghi...",
                "style": "Giọng phụ nữ miền Nam Sài Gòn 34 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, giữ cố định một âm sắc ấm, trầm vừa, sắc sảo thực tế; hạ giọng thì thầm cảnh giác nhắc chồng.",
            },
            {
                "id": "l4",
                "speaker": "anh_hai",
                "start": l4_start,
                "window": r2(s3_end - l4_start - 0.05),
                "text": "Anh cũng thấy lạ, mà người ta lỡ xuống tận nhà rồi, ngại quá chẳng dám đuổi!",
                "style": "Giọng nam miền Nam Sài Gòn 35 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, giữ cố định cùng một âm sắc tự nhiên; hơi lúng túng ái ngại cả nể như ngoài đời thực.",
            },
            {
                "id": "l5",
                "speaker": "ke_gia_danh",
                "label_short": "SỐ LẠ",
                "af": "phone",
                "start": l5_start,
                "window": r2(l6_start - l5_start - 0.05),
                "text": "Alo, bo hư nặng lắm, sửa ba triệu nha anh! Đồng ý thì tụi tôi làm liền!",
                "style": "Giọng nam miền Nam Sài Gòn 40 tuổi qua điện thoại, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, giữ cố định một âm sắc trầm lạnh, dửng dưng và đầy sức ép ngầm sau hai ngày im bặt chờ khách nóng kiệt sức.",
            },
            {
                "id": "l6",
                "speaker": "anh_hai",
                "start": l6_start,
                "window": r2(s4_end - l6_start - 0.05),
                "text": "Im bặt hai ngày nhà nóng ngộp quá! Thôi đồng ý đại, có máy xài liền mình ơi!",
                "style": "Giọng nam miền Nam Sài Gòn 35 tuổi, phát âm chuẩn phương ngữ miền Nam rõ chữ từng tiếng, giữ cố định cùng một âm sắc tự nhiên; thở dài kiệt sức bỏ hết đề phòng quay sang nói với vợ chỉ mong có máy lạnh xài ngay.",
            },
            {
                "id": "l7",
                "speaker": "anh_hai",
                "start": l7_start,
                "window": r2(s5_end - l7_start - 0.05),
                "text": "Alo! Đồng ý rồi mà thêm năm ngày mất hút?! Gọi biên nhận không ai nghe, đem ráp liền!",
                "style": "Giọng nam miền Nam Sài Gòn 35 tuổi, phát âm chuẩn phương ngữ miền Nam rõ chữ từng tiếng, giữ cố định cùng một âm sắc; giận dữ bức bối tột độ sau năm ngày nữa vẫn mất hút, gọi thẳng vào số đầu tiên gào đòi mang máy xuống ráp gấp.",
            },
            {
                "id": "l8",
                "speaker": "chi_hai",
                "start": l8_start,
                "window": r2(l9_start - l8_start - 0.05),
                "text": "Họ mới xuống ráp lấy ba triệu, hai ngày lại ngắt y chang, anh coi kỹ giùm em!",
                "style": "Giọng phụ nữ miền Nam Sài Gòn 34 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, giữ cố định một âm sắc rõ chữ thực tế; đang đứng hỏi trực tiếp kỹ thuật viên chính hãng đầy lo lắng sốt ruột.",
            },
            {
                "id": "l9",
                "speaker": "thang_tun",
                "label_short": "THỢ HÃNG",
                "start": l9_start,
                "window": r2(s6_end - l9_start - 0.05),
                "text": "Bo mạch chẳng hư, họ cũng chưa sửa! Chỉ rách tem, mất bảo hành rồi anh chị!",
                "style": "Giọng kỹ thuật viên nam miền Nam Sài Gòn 28 tuổi, phát âm chuẩn phương ngữ miền Nam rõ chữ, điềm đạm, chân thành và chuyên nghiệp như thợ chính hãng đang trực tiếp giải thích cho khách hàng tại nhà.",
            },
            {
                "id": "l10",
                "speaker": "nguoi_boc_tran",
                "start": l10_start,
                "window": r2(s7_end - l10_start - 0.05),
                "text": "Mạo danh trung tâm lớn, giữ bo ép nóng, tự bạn gật đầu nên họ thoát êm!",
                "style": "Giọng nam trung niên miền Nam Sài Gòn 40 tuổi, phát âm chuẩn phương ngữ miền Nam, trầm tĩnh, sắc lạnh và gọn dứt khoát; nhấn rõ mạo danh trung tâm lớn, giữ bo ép nóng và họ thoát êm.",
            },
            {
                "id": "l11",
                "speaker": "ong_tam",
                "start": l11_start,
                "window": r2(s9_end - l11_start - 0.05),
                "text": "Chị thấy không, cũng chỉ là một trò chơi tâm lý.",
                "style": "Giọng nam miền Nam Sài Gòn khoảng 58 đến 60 tuổi, phát âm chuẩn phương ngữ miền Nam rõ chữ từng tiếng, trầm mượt, điềm đạm, trí thức và thong thả như một quân sư đang nhấp trà nói nhỏ nhẹ với cấp trên; tuyệt đối không gắt gỏng, toát ra quyền lực mềm lạnh tĩnh.",
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
                "Cố tình mạo danh trung tâm bảo hành lớn đứng đầu tìm kiếm; thợ tới mặc đồ thường, không thẻ hãng",
                "Tháo bo mạch giữ lại rồi im bặt 2 ngày giữa trời nóng ngộp, chờ bạn bỏ đề phòng mới báo giá 3 triệu",
                "Đồng ý xong vẫn câu giờ thêm 5 ngày không nghe số biên nhận, phải gào đòi mới xuống ráp và rách luôn tem hãng",
            ],
            "action": "Chỉ gọi đúng số in trên phiếu bảo hành hoặc tem dán trên thân máy · Sai nhận diện dừng ngay từ cửa — không giao bo mạch cho thợ lạ!",
        },
        "disclaimer": {
            "start": s10_start,
            "end": s10_end,
        },
        "audio": {
            "duck_ambience_db": -5.5,
            "ambience": [
                {"preset": "night_room", "start": s1_start, "end": s2_start, "gain_db": -5.5},
                {"preset": "room_tone", "start": s2_start, "end": s5_start, "gain_db": -6.5},
                {"preset": "night_room", "start": s5_start, "end": s6_start, "gain_db": -5.0},
                {"preset": "room_tone", "start": s6_start, "end": s9_start, "gain_db": -7.5},
                {"preset": "night_room", "start": s9_start, "end": s10_end, "gain_db": -5.5},
            ],
            "foley": [
                {"preset": "phone_ring", "at": 0.15, "dur": 1.1, "gain_db": -3.0},
                {"preset": "counter_tick", "at": 0.50, "gain_db": -1.5},
                {"preset": "counter_tick", "at": 1.50, "gain_db": -2.0},
                {"preset": "click", "at": r2(s2_start + 2.25), "gain_db": 0.5},
                {"preset": "marker_draw", "at": r2(s2_start + 2.40), "dur": 0.48, "gain_db": 0.8},
                {"preset": "low_accent", "at": r2(s3_start + 0.35), "dur": 0.9, "gain_db": 0.4},
                {"preset": "phone_vibrate", "at": r2(s4_start + 0.15), "dur": 0.55, "gain_db": -1.5},
                {"preset": "counter_tick", "at": r2(s4_start + 0.55), "gain_db": -1.0},
                {"preset": "counter_tick", "at": r2(s4_start + 1.35), "gain_db": -1.5},
                {"preset": "low_accent", "at": r2(l6_start - 0.10), "dur": 0.9, "gain_db": 0.6},
                {"preset": "impact", "at": r2(s5_start + 0.35), "dur": 0.95, "gain_db": 1.6},
                {"preset": "heartbeat", "at": r2(s5_start + 0.45), "dur": r2(max(1.5, s5_end - s5_start - 0.80)), "gain_db": -2.2},
                {"preset": "click", "at": r2(s6_start + 0.30), "gain_db": 0.6},
                {"preset": "impact", "at": r2(l9_start - 0.15), "dur": 0.9, "gain_db": 1.2},
                {"preset": "marker_draw", "at": r2(l9_start + 0.35), "dur": 0.48, "gain_db": 0.8},
                {"preset": "glitch", "at": r2(s7_start + 0.05), "dur": 0.34, "gain_db": 1.0},
                {"preset": "low_accent", "at": r2(s7_start + 0.55), "dur": 0.9, "gain_db": 0.8},
                {"preset": "marker_draw", "at": r2(l10_start + 0.55), "dur": 0.48, "gain_db": 0.8},
                {"preset": "marker_draw", "at": r2(l10_start + 1.85), "dur": 0.48, "gain_db": 0.8},
                {"preset": "notification", "at": r2(s9_start + 0.35), "gain_db": -3.5},
                {"preset": "click", "at": r2(s9_start + 0.75), "gain_db": -1.5},
                {"preset": "impact", "at": r2(s9_end - 0.35), "dur": 0.9, "gain_db": 1.4},
            ],
            "bgm": [
                {"preset": "suspense_pulse", "start": s1_start, "end": s4_start, "gain_db": -1.5},
                {"preset": "tension_drone", "start": s4_start, "end": s6_start, "gain_db": 0.8},
                {"preset": "investigative_story", "start": s6_start, "end": s8_start, "gain_db": 0.6},
                {"preset": "warm_outro", "start": s8_start, "end": s9_start, "gain_db": 0.0},
                {"preset": "tension_drone", "start": s9_start, "end": s10_start, "gain_db": 0.4},
            ],
            "duck_extra": [],
        },
        "forbidden_terms": [],
        "publish": {
            "titles": [
                "Bẫy bảo hành máy lạnh giả: Mạo danh trung tâm lớn, giữ bo ép giá! #shorts #bóctrầnlừađảo",
                "Giả trung tâm lớn: Im 2 ngày đòi 3tr, câu thêm 5 ngày mới ráp! #shorts #cảnhgiáclừađảo",
                "Gọi bảo hành mà bấm số đầu trên mạng coi chừng dính bẫy ôm bo mạch! #shorts #vạnchuyện",
            ],
            "description": (
                "Máy lạnh mới mua 8 tháng tự ngắt điện, nhiều gia đình lên mạng gõ tìm trung tâm bảo hành lớn rồi bấm ngay kết quả đứng đầu tiên mà không biết đó là trang cố tình mạo danh chạy quảng cáo.\n\n"
                "Chiêu tâm lý này cực kỳ thâm độc: họ KHÔNG lấy luôn bo mạch, mà tháo bo mang đi rồi im bặt 2 ngày giữa cái nóng ngột ngạt của nhà ống thành phố. Chờ nạn nhân chịu hết nổi, chỉ muốn có máy xài liền và bỏ hết đề phòng, họ mới gọi báo giá 3 triệu và hứa làm liền. Đồng ý xong, họ lại tiếp tục mất hút thêm 5 ngày (tổng cả tuần trời), gọi số biên nhận không ai nghe — đến khi nạn nhân nhớ số tổng đài ban đầu gọi gào lên thì họ mới xuống ráp lại, thu đủ 3 triệu. Hai ngày sau máy ngắt y chang, gọi đúng hãng tới mới vỡ lẽ: bo mạch chẳng hư gì, họ cũng chẳng sửa gì, chỉ rách luôn tem mất bảo hành!\n\n"
                "✅ Nhớ kỹ để bảo vệ cả gia đình:\n"
                "1. Không gọi số đứng đầu kết quả tìm kiếm (rất dễ là quảng cáo cố tình mạo danh trung tâm bảo hành lớn).\n"
                "2. Chỉ gọi đúng số tổng đài in trên phiếu bảo hành, hóa đơn mua hàng hoặc tem dán ngay trên thân máy.\n"
                "3. Thợ bảo hành chính hãng phải có đồng phục, thẻ nhân viên và khớp lịch hẹn tổng đài — sai nhận diện dừng ngay từ cửa.\n"
                "4. Tuyệt đối không giao bo mạch/linh kiện mang đi theo tờ giấy viết tay không rõ tên đơn vị."
            ),
            "pinned_comment": (
                "📌 Nhà ống thành phố có máy lạnh, máy giặt, tủ lạnh nhớ gửi ngay clip này cho cả nhà! "
                "Chiêu này thâm từ đầu: cố tình mạo danh trung tâm bảo hành lớn leo top tìm kiếm, tháo bo mạch rồi im bặt 2 ngày giữa trời nóng ngộp để bạn bỏ hết đề phòng đồng ý giá 3 triệu — đồng ý xong vẫn câu thêm 5 ngày mất hút, gọi số biên nhận không nghe, phải gào lên số ban đầu mới xuống ráp lấy tiền rồi 2 ngày lại hư y chang! "
                "Muốn gọi bảo hành, tuyệt đối không bấm số đứng đầu trên mạng; chỉ gọi đúng số tổng đài in trên phiếu bảo hành hoặc tem dán ngay trên thân máy! "
                "(Lưu ý: Không đăng SĐT, STK hay tên cá nhân/cửa hàng thật dưới phần bình luận nhé.)"
            ),
            "hashtags": ["#shorts", "#bóctrầnlừađảo", "#cảnhgiáclừađảo"],
            "tags": [
                "bẫy bảo hành máy lạnh giả",
                "lừa đảo bảo hành điện máy",
                "quảng cáo giả trung tâm bảo hành",
                "thợ sửa máy lạnh cầm bo mạch ép giá",
                "bóc trần lừa đảo",
                "vạn chuyện",
                "shorts",
            ],
            "category": "Education (Giáo dục)",
            "playlist": "Bóc Trần Lừa Đảo – Kỹ Năng Cảnh Giác & An Toàn Đời Thực",
            "thumbnail_sec": r2(s5_start + 2.55),
        },
    }

    OUT_JSON.write_text(json.dumps(ep, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Đã biên dịch {OUT_JSON} ({total_dur:.2f}s · mode={'REAL_TTS' if has_real_tts else 'DRAFT'})")
    return ep


if __name__ == "__main__":
    build()
