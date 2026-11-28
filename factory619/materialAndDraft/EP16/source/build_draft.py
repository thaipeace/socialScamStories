# -*- coding: utf-8 -*-
"""
Single Source of Truth cho `factory619/materialAndDraft/EP16` (`BayTrangCaNhanKiemTien` · V3).

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
        "l1": 3.60,
        "l2": 3.40,
        "l3": 3.30,
        "l4": 4.20,
        "l5": 4.00,
        "l6": 4.40,
        "l7": 3.80,
        "l8": 4.50,
        "l8b": 3.50,
        "l9": 4.50,
        "l10": 4.10,
        "l11": 3.70,
        "l12": 4.20,
        "l13": 5.40,
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
        "s1_chiba_eye": [0.220, 0.360, 0.410, 0.420],
        "s1_chiba_mouth": [0.250, 0.435, 0.370, 0.490],
        "s1_anhhai_eye": [0.680, 0.330, 0.860, 0.390],
        "s2_chiba_eye": [0.540, 0.330, 0.720, 0.390],
        "s2_chiba_mouth": [0.575, 0.400, 0.685, 0.455],
        "s2_anhhai_eye": [0.160, 0.310, 0.340, 0.370],
        "s2_anhhai_mouth": [0.195, 0.380, 0.305, 0.435],
        "s3_chiba_eye": [0.480, 0.280, 0.680, 0.345],
        "s3_chiba_mouth": [0.515, 0.360, 0.635, 0.415],
        "s4_chiba_eye": [0.280, 0.270, 0.500, 0.335],
        "s4_chiba_mouth": [0.320, 0.355, 0.450, 0.415],
        "s5_chiba_eye": [0.320, 0.590, 0.520, 0.650],
        "s6_chitu_eye": [0.360, 0.280, 0.570, 0.365],
        "s6_chitu_mouth": [0.400, 0.385, 0.525, 0.455],
        "s6_chiba_eye": [0.380, 0.280, 0.590, 0.365],
        "s6_chiba_mouth": [0.415, 0.385, 0.540, 0.455],
        "s7_anhhai_eye": [0.220, 0.310, 0.410, 0.370],
        "s7_anhhai_mouth": [0.255, 0.385, 0.370, 0.440],
        "s7_chiba_eye": [0.640, 0.350, 0.820, 0.410],
        # Detail / evidence regions (calibrated after image inspection)
        "s1_phone_glow": [0.46, 0.63],
        "s3_pw_circle": [0.12, 0.56, 0.56, 0.78],
        "s4_email_circle": [0.44, 0.56, 0.88, 0.78],
        "s5_phone_glow": [0.52, 0.79],
        "s8_mask_circle": [0.22, 0.14, 0.78, 0.44],
        "s8_split_highlight": [0.10, 0.58, 0.90, 0.84],
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
    s1_end = r2(l1_start + durs["l1"] + 0.50)

    # Scene 2: Nguồn cơn (2.5D #1 · l2 Anh Hai, l3 Chị Ba)
    s2_start = s1_end
    l2_start = r2(s2_start + 0.35)
    l3_start = r2(l2_start + durs["l2"] + 0.28)
    s2_end = r2(l3_start + durs["l3"] + 0.50)

    # Scene 3: Nấc 1 — Mồi chuyên nghiệp & máy bắt nhập mật khẩu xác nhận chính chủ (l4, l5, l6)
    s3_start = s2_end
    l4_start = r2(s3_start + 0.40)
    l5_start = r2(l4_start + durs["l4"] + 0.45)
    l6_start = r2(l5_start + durs["l5"] + 0.30)
    s3_end = r2(l6_start + durs["l6"] + 0.55)

    # Scene 4: Nấc 2 — Email chính báo đổi quyền quản trị, "Cứ thong thả đọc kỹ!" → tự hạ phòng vệ bấm (l7, l8, l8b + 1.15s cú bấm & sập đỏ)
    s4_start = s3_end
    l7_start = r2(s4_start + 0.45)
    l8_start = r2(l7_start + durs["l7"] + 0.30)
    l8b_start = r2(l8_start + durs["l8"] + 0.35)
    s4_click_at = r2(l8b_start + durs["l8b"] + 0.22)
    s4_crash_at = r2(s4_click_at + 0.38)
    s4_end = r2(s4_crash_at + 0.85)

    # Scene 5: Lật mặt lạnh tĩnh đòi 20 triệu chuộc trang 10 năm (l9)
    s5_start = s4_end
    l9_start = r2(s5_start + 0.40)
    s5_end = r2(l9_start + durs["l9"] + 0.55)

    # Scene 6: Split-screen ngang — Vạ lây đời sống thật (l10 Chị Tư, l11 Chị Ba)
    s6_start = s5_end
    l10_start = r2(s6_start + 0.45)
    l11_start = r2(l10_start + durs["l10"] + 0.35)
    s6_end = r2(l11_start + durs["l11"] + 0.55)

    # Scene 7: Ứng phó kịp lúc — Không chuyển, chặn vạ lây & giữ chứng cứ (2.5D #2 · l12)
    s7_start = s6_end
    l12_start = r2(s7_start + 0.40)
    s7_end = r2(l12_start + durs["l12"] + 0.55)

    # Scene 8: Bóc trần siêu gọn đúng 1 câu (l13)
    s8_start = s7_end
    l13_start = r2(s8_start + 0.30)
    s8_end = r2(l13_start + durs["l13"] + 0.25)

    # Scene 9: Thẻ NHỚ KỸ gọn dứt khoát (2.65s không thoại)
    s9_start = s8_end
    s9_end = r2(s9_start + 2.65)

    # Scene 10: Cắt đen + Bảng LƯU Ý gọn sát chuẩn tối thiểu 2.5s (2.55s)
    s10_start = s9_end
    s10_end = r2(s10_start + 2.55)

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
        "episode_id": "EP16",
        "slug": "BayTrangCaNhanKiemTien",
        "title": "Xây kênh kiếm tiền trên trang cá nhân – Không hối một câu, 3 phút mất trắng, vạ lây người thân!",
        "version": "v5-level3-calm-scam-real-tts" if has_real_tts else "v5-level3-calm-scam-draft",
        "scam_family": "VAR-ACC-01",
        "motion_upgrade": "level3",
        "duration_sec": total_dur,
        "hook": {
            "kicker": "XÂY KÊNH TRÊN TRANG CÁ NHÂN",
            "title": "Không hối một câu, 3 phút mất trắng!",
            "start": 0.25,
            "end": r2(min(4.65, s1_end - 0.30)),
        },
        "scenes": [
            {
                "id": "s1_hook_3phut_mat_trang",
                "image": "assets/s1.jpg",
                "start": s1_start,
                "end": s1_end,
                "beat_type": "establishing",
                "motion_level": "C",
                "motion_intent": "Phòng tối: Chị Ba tái mặt chìa điện thoại đỏ rực ổ khóa vỡ nói gấp với Anh Hai + animated_counter 03:00→00:00 + screen_glow đỏ + Living-Char Chị Ba & Anh Hai",
                "motion": {
                    "preset": "slow_push_in",
                    "scale": [1.02, 1.09],
                    "focus": [[0.50, 0.50], [0.48, 0.47]],
                    "wobble": "none",
                    "easing": "ease_out",
                },
                "detail_fx": [
                    {
                        "type": "eye_blink",
                        "image": "assets/s1_chiba_blink.jpg",
                        "region": rois["s1_chiba_eye"],
                        "feather": 0.008,
                        "times": blink_times(s1_start, s1_end, 1.3, 3.0),
                        "close_dur": 0.055,
                        "hold_dur": 0.045,
                        "open_dur": 0.085,
                    },
                    {
                        "type": "mouth_sync",
                        "speaker": "chi_ba",
                        "line_ids": ["l1"],
                        "region": rois["s1_chiba_mouth"],
                        "feather": 0.008,
                        "closed_image": "assets/s1_chiba_mouth_closed.jpg",
                        "mid_image": "assets/s1.jpg",
                        "open_image": "assets/s1_chiba_mouth_open.jpg",
                        "fps": 12,
                        "thresh_mid": 0.14,
                        "thresh_open": 0.64,
                    },
                    {
                        "type": "eye_blink",
                        "image": "assets/s1_anhhai_blink.jpg",
                        "region": rois["s1_anhhai_eye"],
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
                        "count_dur": 2.4,
                        "from_val": 180,
                        "to_val": 0,
                        "fmt": "mmss",
                        "label": "MẤT QUYỀN TRANG CÁ NHÂN",
                        "pos": [0.68, 0.215],
                        "style": "danger",
                        "easing": "ease_out",
                    },
                    {
                        "type": "screen_glow",
                        "pos": rois["s1_phone_glow"],
                        "radius": [0.18, 0.15],
                        "color": [235, 55, 65],
                        "intensity": 0.26,
                        "mode": "pulse",
                        "start": 0.25,
                        "end": r2(s1_end - 0.10),
                        "fade": 0.25,
                    },
                    {
                        "type": "color_mood",
                        "mood": "cold_suspicion",
                        "strength": 0.26,
                        "vignette": 0.16,
                        "grain": 0.006,
                    },
                ],
            },
            {
                "id": "s2_nguon_con_xay_trang_ca_nhan",
                "image": "assets/s2.jpg",
                "start": s2_start,
                "end": s2_end,
                "beat_type": "normal",
                "motion_level": "B",
                "motion_intent": "2.5D Parallax #1 phòng khách ban ngày: hậu cảnh kệ ảnh gia đình chuyển nét Rack Focus + Breathing + Head Micro-Tilt + Chị Ba chép miệng 4 trạng thái (round_image) & Anh Hai đối đáp",
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
                            "head_pivot": [0.64, 0.50],
                            "tilt_speaker": "chi_ba",
                            "tilt_line_ids": ["l3"],
                        },
                    ],
                },
                "detail_fx": [
                    {
                        "type": "eye_blink",
                        "image": "assets/s2_anhhai_blink.jpg",
                        "region": rois["s2_anhhai_eye"],
                        "feather": 0.008,
                        "times": blink_times(s2_start, s2_end, 1.2, 3.1),
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
                        "fps": 12,
                        "thresh_mid": 0.14,
                        "thresh_open": 0.64,
                        "layer": "fg",
                    },
                    {
                        "type": "eye_blink",
                        "image": "assets/s2_chiba_blink.jpg",
                        "region": rois["s2_chiba_eye"],
                        "feather": 0.008,
                        "times": blink_times(s2_start, s2_end, 2.0, 3.0),
                        "close_dur": 0.055,
                        "hold_dur": 0.045,
                        "open_dur": 0.085,
                        "layer": "fg",
                    },
                    {
                        "type": "mouth_sync",
                        "speaker": "chi_ba",
                        "line_ids": ["l3"],
                        "region": rois["s2_chiba_mouth"],
                        "feather": 0.008,
                        "closed_image": "assets/s2_chiba_mouth_closed.jpg",
                        "mid_image": "assets/s2.jpg",
                        "open_image": "assets/s2_chiba_mouth_open.jpg",
                        "round_image": "assets/s2_chiba_mouth_round.jpg",
                        "fps": 12,
                        "thresh_mid": 0.14,
                        "thresh_open": 0.64,
                        "layer": "fg",
                    },
                    {
                        "type": "color_mood",
                        "mood": "warm_daily",
                        "strength": 0.22,
                        "vignette": 0.08,
                        "grain": 0.0,
                    },
                ],
                "transition_in": {"type": "dissolve", "dur": 0.28},
            },
            {
                "id": "s3_nac1_chuyen_nghiep_mat_khau",
                "image": "assets/s3.jpg",
                "start": s3_start,
                "end": s3_end,
                "beat_type": "suspicion",
                "motion_level": "C",
                "motion_intent": "Quét trái mượt: đại diện nhãn hàng chuyên nghiệp bảo thêm email kế toán → máy bật yêu cầu nhập mật khẩu xác nhận chính chủ + detail_reveal + red_circle_draw + phone_waveform êm ái không hối + Living-Char Chị Ba",
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
                        "at": r2(l5_start - 0.25),
                        "dur": 0.45,
                    },
                    {
                        "type": "red_circle_draw",
                        "region": rois["s3_pw_circle"],
                        "at": r2(l5_start + 0.15),
                        "dur": 0.50,
                        "style": "circle",
                    },
                    {
                        "type": "phone_waveform",
                        "speaker": "ke_ngot_ngao_nu",
                        "line_ids": ["l4", "l6"],
                        "start": r2(l4_start - 0.10),
                        "end": r2(s3_end - 0.15),
                        "pos": [0.28, 0.135],
                        "label": "ĐỐI TÁC NHÃN HÀNG",
                        "color": [70, 210, 165],
                    },
                    {
                        "type": "typing_indicator",
                        "start": r2(s3_start + 0.15),
                        "end": r2(l4_start + 0.80),
                        "pos": [0.22, 0.50],
                    },
                    {
                        "type": "eye_blink",
                        "image": "assets/s3_chiba_blink.jpg",
                        "region": rois["s3_chiba_eye"],
                        "feather": 0.008,
                        "times": blink_times(s3_start, s3_end, 1.4, 3.2),
                        "close_dur": 0.055,
                        "hold_dur": 0.045,
                        "open_dur": 0.085,
                    },
                    {
                        "type": "mouth_sync",
                        "speaker": "chi_ba",
                        "line_ids": ["l5"],
                        "region": rois["s3_chiba_mouth"],
                        "feather": 0.008,
                        "closed_image": "assets/s3_chiba_mouth_closed.jpg",
                        "mid_image": "assets/s3.jpg",
                        "open_image": "assets/s3_chiba_mouth_open.jpg",
                        "fps": 12,
                        "thresh_mid": 0.14,
                        "thresh_open": 0.64,
                    },
                    {
                        "type": "color_mood",
                        "mood": "warm_daily",
                        "strength": 0.18,
                        "vignette": 0.12,
                        "grain": 0.0,
                    },
                ],
                "transition_in": {"type": "dissolve", "dur": 0.26},
            },
            {
                "id": "s4_nac2_email_chinh_doi_quyen",
                "image": "assets/s4.jpg",
                "start": s4_start,
                "end": s4_end,
                "beat_type": "climax",
                "motion_level": "C",
                "motion_intent": "Cao trào Nấc 2 (KHÔNG đồng hồ hối thúc): hộp thư email chính báo đổi quyền quản trị → đối tác vẫn nhã nhặn khuyên 'Cứ thong thả đọc kỹ!' → Chị Ba hạ phòng vệ bấm xác nhận → detail_reveal bùng đỏ vỡ khóa + chromatic_pulse + shakes",
                "motion": {
                    "preset": "tense_push",
                    "scale": [1.02, 1.10],
                    "focus": [[0.48, 0.48], [0.46, 0.45]],
                    "wobble": "breathe",
                    "easing": "ease_out",
                },
                "detail_fx": [
                    {
                        "type": "red_circle_draw",
                        "region": rois["s4_email_circle"],
                        "at": r2(l7_start + 0.15),
                        "dur": 0.50,
                        "style": "circle",
                    },
                    {
                        "type": "phone_waveform",
                        "speaker": "ke_ngot_ngao_nu",
                        "line_ids": ["l8"],
                        "start": r2(l8_start - 0.10),
                        "end": r2(l8b_start - 0.05),
                        "pos": [0.66, 0.125],
                        "label": "ĐỐI TÁC NHÃN HÀNG",
                        "color": [70, 210, 165],
                    },
                    {
                        "type": "detail_reveal",
                        "image": "assets/s4_reveal.jpg",
                        "at": s4_crash_at,
                        "dur": 0.30,
                    },
                    {
                        "type": "chromatic_pulse",
                        "at": s4_crash_at,
                        "dur": 0.32,
                        "shift_px": 7,
                        "zoom_blur": 0.025,
                    },
                    {
                        "type": "eye_blink",
                        "image": "assets/s4_chiba_blink.jpg",
                        "region": rois["s4_chiba_eye"],
                        "feather": 0.008,
                        "times": blink_times(s4_start, s4_crash_at, 1.3, 3.1),
                        "close_dur": 0.055,
                        "hold_dur": 0.045,
                        "open_dur": 0.085,
                    },
                    {
                        "type": "mouth_sync",
                        "speaker": "chi_ba",
                        "line_ids": ["l7", "l8b"],
                        "region": rois["s4_chiba_mouth"],
                        "feather": 0.008,
                        "closed_image": "assets/s4_chiba_mouth_closed.jpg",
                        "mid_image": "assets/s4.jpg",
                        "open_image": "assets/s4_chiba_mouth_open.jpg",
                        "fps": 12,
                        "thresh_mid": 0.14,
                        "thresh_open": 0.64,
                    },
                    {
                        "type": "color_mood",
                        "mood": "high_tension",
                        "strength": 0.28,
                        "vignette": 0.18,
                        "grain": 0.008,
                    },
                ],
                "shakes": [{"at": s4_crash_at, "amp": 22}],
                "transition_in": {"type": "zoom_punch", "dur": 0.28},
            },
            {
                "id": "s5_lat_mat_lanh_tinh_doi_chuoc",
                "image": "assets/s5.jpg",
                "start": s5_start,
                "end": s5_end,
                "beat_type": "climax",
                "motion_level": "C",
                "motion_intent": "Cú lật lạnh tĩnh không la hét: bóng tối phòng kín + giọng nam đều đều đòi 20 triệu chuộc trang 10 năm ảnh gia đình + slow_pull_out + phone_waveform đỏ + screen_glow + Living-Char Chị Ba chớp mắt sững sờ",
                "motion": {
                    "preset": "slow_pull_out",
                    "scale": [1.08, 1.02],
                    "focus": [[0.50, 0.46], [0.50, 0.50]],
                    "wobble": "none",
                    "easing": "ease_out",
                },
                "detail_fx": [
                    {
                        "type": "phone_waveform",
                        "speaker": "ke_gia_danh",
                        "line_ids": ["l9"],
                        "start": r2(l9_start - 0.10),
                        "end": r2(s5_end - 0.15),
                        "pos": [0.50, 0.375],
                        "label": "SỐ LẠ",
                        "color": [240, 75, 80],
                    },
                    {
                        "type": "screen_glow",
                        "pos": rois["s5_phone_glow"],
                        "radius": [0.20, 0.14],
                        "color": [235, 55, 65],
                        "intensity": 0.24,
                        "mode": "pulse",
                        "start": s5_start,
                        "end": r2(s5_end - 0.10),
                        "fade": 0.20,
                    },
                    {
                        "type": "eye_blink",
                        "image": "assets/s5_chiba_blink.jpg",
                        "region": rois["s5_chiba_eye"],
                        "feather": 0.008,
                        "times": blink_times(s5_start, s5_end, 1.5, 3.0),
                        "close_dur": 0.060,
                        "hold_dur": 0.055,
                        "open_dur": 0.095,
                    },
                    {
                        "type": "color_mood",
                        "mood": "noir_evidence",
                        "strength": 0.34,
                        "vignette": 0.22,
                        "grain": 0.010,
                    },
                ],
                "transition_in": {"type": "whip_pan_left", "dur": 0.26},
            },
            {
                "id": "s6_split_va_lay_doi_song",
                "image": "assets/s6_chitu.jpg",
                "start": s6_start,
                "end": s6_end,
                "beat_type": "climax",
                "motion_level": "C",
                "motion_intent": "Level 3 split_screen trên-dưới: Chị Tư tin đúng trang cá nhân 10 năm nhắn bị giữ nên vừa chuyển 10 triệu (panel trên) & Chị Ba hoảng loạn trước hàng loạt cuộc gọi của họ hàng đồng nghiệp (panel dưới) + Living-Char cả 2 panel",
                "split_screen": {
                    "layout": "horizontal",
                    "ratio": 0.48,
                    "divider_width": 6,
                    "inactive_dim": 0.20,
                    "slide_in_dur": 0.28,
                    "panels": [
                        {
                            "image": "assets/s6_chitu.jpg",
                            "speaker": "chi_tu",
                            "line_ids": ["l10"],
                            "label": "",
                            "label_rgb": [185, 245, 215],
                            "waveform": False,
                            "crop_x": 0.50,
                            "crop_y": 0.44,
                            "motion": {"preset": "slow_push_in", "scale": [1.02, 1.07], "focus": [[0.50, 0.48], [0.50, 0.46]]},
                            "detail_fx": [
                                {
                                    "type": "eye_blink",
                                    "image": "assets/s6_chitu_blink.jpg",
                                    "region": rois["s6_chitu_eye"],
                                    "region_space": "source",
                                    "feather": 0.008,
                                    "times": blink_times(s6_start, s6_end, 1.2, 3.1),
                                    "close_dur": 0.055,
                                    "hold_dur": 0.045,
                                    "open_dur": 0.085,
                                },
                                {
                                    "type": "mouth_sync",
                                    "speaker": "chi_tu",
                                    "line_ids": ["l10"],
                                    "region": rois["s6_chitu_mouth"],
                                    "region_space": "source",
                                    "feather": 0.008,
                                    "closed_image": "assets/s6_chitu_mouth_closed.jpg",
                                    "mid_image": "assets/s6_chitu.jpg",
                                    "open_image": "assets/s6_chitu_mouth_open.jpg",
                                    "fps": 12,
                                    "thresh_mid": 0.14,
                                    "thresh_open": 0.64,
                                },
                            ],
                        },
                        {
                            "image": "assets/s6_chiba.jpg",
                            "speaker": "chi_ba",
                            "line_ids": ["l11"],
                            "label": "",
                            "label_rgb": [255, 235, 215],
                            "waveform": False,
                            "crop_x": 0.50,
                            "crop_y": 0.44,
                            "motion": {"preset": "slow_pull_out", "scale": [1.07, 1.02], "focus": [[0.50, 0.46], [0.50, 0.48]]},
                            "detail_fx": [
                                {
                                    "type": "eye_blink",
                                    "image": "assets/s6_chiba_blink.jpg",
                                    "region": rois["s6_chiba_eye"],
                                    "region_space": "source",
                                    "feather": 0.008,
                                    "times": blink_times(s6_start, s6_end, 2.0, 3.2),
                                    "close_dur": 0.055,
                                    "hold_dur": 0.045,
                                    "open_dur": 0.085,
                                },
                                {
                                    "type": "mouth_sync",
                                    "speaker": "chi_ba",
                                    "line_ids": ["l11"],
                                    "region": rois["s6_chiba_mouth"],
                                    "region_space": "source",
                                    "feather": 0.008,
                                    "closed_image": "assets/s6_chiba_mouth_closed.jpg",
                                    "mid_image": "assets/s6_chiba.jpg",
                                    "open_image": "assets/s6_chiba_mouth_open.jpg",
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
                        "mood": "high_tension",
                        "strength": 0.24,
                        "vignette": 0.16,
                        "grain": 0.006,
                    },
                ],
                "transition_in": {"type": "whip_pan_right", "dur": 0.26},
            },
            {
                "id": "s7_ung_pho_chan_va_lay",
                "image": "assets/s7.jpg",
                "start": s7_start,
                "end": s7_end,
                "beat_type": "information",
                "motion_level": "B",
                "motion_intent": "2.5D Parallax #2 phòng khách sáng ấm: Anh Hai chặn tay không cho Chị Ba chuyển chuộc, nhắn báo gấp người thân chặn vạ lây & chụp lưu chứng cứ + Rack Focus + Breathing + detail_reveal + Living-Char Anh Hai & Chị Ba",
                "motion": {
                    "preset": "slow_pull_out",
                    "scale": [1.07, 1.02],
                    "focus": [[0.50, 0.46], [0.50, 0.50]],
                    "wobble": "none",
                    "easing": "smoothstep",
                },
                "parallax": {
                    "camera": "pull_out",
                    "dolly": [1.07, 1.02],
                    "shift_x": [0.0, 0.0],
                    "shift_y": [-1.8, 1.5],
                    "focus": [0.50, 0.48],
                    "strength": 0.85,
                    "easing": "smoothstep",
                    "layers": [
                        {
                            "role": "bg",
                            "image": "assets/s7_bg.jpg",
                            "depth": 0.42,
                            "blur_from": 3.4,
                            "blur_to": 0.5,
                            "blur_at": r2(s7_start + 0.65),
                            "blur_dur": 2.0,
                        },
                        {
                            "role": "fg",
                            "image": "assets/s7_fg.png",
                            "depth": 1.24,
                            "breathe_y": 1.8,
                            "breathe_period": 3.6,
                        },
                    ],
                },
                "detail_fx": [
                    {
                        "type": "eye_blink",
                        "image": "assets/s7_anhhai_blink.jpg",
                        "region": rois["s7_anhhai_eye"],
                        "feather": 0.008,
                        "times": blink_times(s7_start, s7_end, 1.3, 3.0),
                        "close_dur": 0.055,
                        "hold_dur": 0.045,
                        "open_dur": 0.085,
                        "layer": "fg",
                    },
                    {
                        "type": "mouth_sync",
                        "speaker": "anh_hai",
                        "line_ids": ["l12"],
                        "region": rois["s7_anhhai_mouth"],
                        "feather": 0.008,
                        "closed_image": "assets/s7_anhhai_mouth_closed.jpg",
                        "mid_image": "assets/s7.jpg",
                        "open_image": "assets/s7_anhhai_mouth_open.jpg",
                        "fps": 12,
                        "thresh_mid": 0.14,
                        "thresh_open": 0.64,
                        "layer": "fg",
                    },
                    {
                        "type": "eye_blink",
                        "image": "assets/s7_chiba_blink.jpg",
                        "region": rois["s7_chiba_eye"],
                        "feather": 0.008,
                        "times": blink_times(s7_start, s7_end, 2.2, 3.2),
                        "close_dur": 0.055,
                        "hold_dur": 0.045,
                        "open_dur": 0.085,
                        "layer": "fg",
                    },
                    {
                        "type": "ambient_particles",
                        "count": 16,
                        "opacity": 0.24,
                        "color": [255, 240, 200],
                        "drift_dir": "up",
                    },
                    {
                        "type": "color_mood",
                        "mood": "warm_daily",
                        "strength": 0.24,
                        "vignette": 0.10,
                        "grain": 0.0,
                    },
                ],
                "transition_in": {"type": "dissolve", "dur": 0.28},
            },
            {
                "id": "s8_boc_tran_mat_na_lich_su",
                "image": "assets/s8.jpg",
                "start": s8_start,
                "end": s8_end,
                "beat_type": "anomaly",
                "motion_level": "C",
                "motion_intent": "Kính lúp đỏ soi vỡ mặt nạ lịch sự lộ 2 nấc khóa chiếm trang & bức tường khiên xanh ngọc tách đôi Trang cá nhân vs Trang làm nội dung riêng + glitch + detail_reveal + red_circle_draw + highlighter_sweep",
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
                        "image": "assets/s8_reveal.jpg",
                        "at": r2(s8_start + 0.50),
                        "dur": 0.45,
                    },
                    {
                        "type": "red_circle_draw",
                        "region": rois["s8_mask_circle"],
                        "at": r2(l13_start + 0.45),
                        "dur": 0.50,
                        "style": "circle",
                    },
                    {
                        "type": "highlighter_sweep",
                        "region": rois["s8_split_highlight"],
                        "at": r2(l13_start + 2.15),
                        "dur": 0.50,
                    },
                    {
                        "type": "focus_highlight",
                        "pos": [0.50, 0.48],
                        "radius": [0.46, 0.38],
                        "dim_outer": 0.20,
                        "start": r2(s8_start + 0.50),
                        "end": r2(s8_end - 0.10),
                        "fade": 0.30,
                    },
                    {
                        "type": "color_mood",
                        "mood": "noir_evidence",
                        "strength": 0.38,
                        "vignette": 0.20,
                        "grain": 0.010,
                    },
                ],
                "transition_in": {"type": "glitch", "dur": 0.34},
            },
            {
                "id": "s9_the_nho_ky",
                "image": "assets/s9.jpg",
                "start": s9_start,
                "end": s9_end,
                "beat_type": "ending",
                "motion_level": "A",
                "motion_intent": "Giữ tĩnh tuyệt đối trên nền phòng khách nắng ấm dịu mắt cho Thẻ Nhớ kỹ 5.0s",
                "motion": {"preset": "static_hold"},
                "transition_in": {"type": "fade_black", "dur": 0.28},
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
                "speaker": "chi_ba",
                "start": l1_start,
                "window": r2(s1_end - l1_start - 0.05),
                "text": "Anh Hai ơi, mới xác nhận xong, mất sạch trang rồi!",
                "style": "Giọng phụ nữ miền Nam Sài Gòn 35 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, giữ cố định một âm sắc rõ chữ; hốt hoảng run giọng gọi anh trai khi vừa bị đá văng khỏi trang cá nhân.",
            },
            {
                "id": "l2",
                "speaker": "anh_hai",
                "start": l2_start,
                "window": r2(l3_start - l2_start - 0.05),
                "text": "Làm kênh phải lập trang riêng, trang cá nhân rủi lắm!",
                "style": "Giọng nam miền Nam Sài Gòn 35 tuổi, thẳng tính, ấm áp và tỉnh táo như anh trai nhắc em gái; tốc độ vừa phải, rõ chữ.",
            },
            {
                "id": "l3",
                "speaker": "chi_ba",
                "start": l3_start,
                "window": r2(s2_end - l3_start - 0.05),
                "text": "Sẵn bạn bè lên tương tác lẹ, em bảo mật kỹ!",
                "style": "Giọng phụ nữ miền Nam Sài Gòn 35 tuổi, giữ cố định cùng một âm sắc rõ chữ; vui vẻ, tự tin và hơi chủ quan khi trả lời anh trai.",
            },
            {
                "id": "l4",
                "speaker": "ke_ngot_ngao_nu",
                "af": "phone",
                "start": l4_start,
                "window": r2(l5_start - l4_start - 0.05),
                "text": "Duyệt bài mười lăm triệu rồi! Chị thêm email kế toán giải ngân nha!",
                "style": "Giọng nữ miền Nam Sài Gòn 30 tuổi chuyên viên nhãn hàng cực kỳ lịch sự, điềm tĩnh, chuyên nghiệp và niềm nở tự nhiên như quy trình thanh toán thật; tuyệt đối không hối thúc, không gấp gáp.",
            },
            {
                "id": "l5",
                "speaker": "chi_ba",
                "start": l5_start,
                "window": r2(l6_start - l5_start - 0.05),
                "text": "Ủa kỳ vậy... sao máy bắt nhập mật khẩu xác nhận chính chủ?",
                "style": "Giọng phụ nữ miền Nam Sài Gòn 35 tuổi, giữ cố định cùng một âm sắc rõ chữ; khựng lại ngạc nhiên và nghi ngờ nhẹ, tự lẩm bẩm rồi hỏi lại đầu dây.",
            },
            {
                "id": "l6",
                "speaker": "ke_ngot_ngao_nu",
                "af": "phone",
                "start": l6_start,
                "window": r2(s3_end - l6_start - 0.05),
                "text": "Dạ hệ thống bắt chính chủ xác nhận, bên em đâu đụng máy chị được!",
                "style": "Giọng nữ miền Nam Sài Gòn 30 tuổi, giữ cố định cùng một âm sắc; cực kỳ lễ phép, điềm đạm, giải thích rành mạch hợp lý và tôn trọng, tuyệt đối không hối gấp hay gây áp lực.",
            },
            {
                "id": "l7",
                "speaker": "chi_ba",
                "start": l7_start,
                "window": r2(l8_start - l7_start - 0.05),
                "text": "Khoan! Email chính báo đổi quyền quản trị kìa, mất trang không?!",
                "style": "Giọng phụ nữ miền Nam Sài Gòn 35 tuổi, giữ cố định cùng một âm sắc rõ chữ; giật mình căng thẳng hẳn lên khi thấy cảnh báo ở hộp thư email chính, vội hỏi lại lần hai.",
            },
            {
                "id": "l8",
                "speaker": "ke_ngot_ngao_nu",
                "af": "phone",
                "start": l8_start,
                "window": r2(l8b_start - l8_start - 0.05),
                "text": "Dạ mẫu mặc định, nhận tiền xong chị gỡ liền! Cứ thong thả đọc kỹ!",
                "style": "Giọng nữ miền Nam Sài Gòn 30 tuổi, giữ cố định cùng một âm sắc; vô cùng nhã nhặn, kiên nhẫn, thong thả và chu đáo như nhân viên chăm sóc khách hàng cao cấp, tuyệt đối không thúc giục.",
            },
            {
                "id": "l8b",
                "speaker": "chi_ba",
                "start": l8b_start,
                "window": r2(s4_click_at - l8b_start - 0.02),
                "text": "Chẳng hối gì, nghe cũng hợp lý... chắc quy trình thật!",
                "style": "Giọng phụ nữ miền Nam Sài Gòn 35 tuổi, giữ cố định cùng một âm sắc rõ chữ; hạ giọng tự trấn an, thở nhẹ buông lỏng cảnh giác rồi quyết định bấm xác nhận.",
            },
            {
                "id": "l9",
                "speaker": "ke_gia_danh",
                "af": "phone",
                "start": l9_start,
                "window": r2(s5_end - l9_start - 0.05),
                "text": "Trang mười năm ảnh gia đình tôi đang giữ. Hai mươi triệu nhận lại.",
                "style": "Giọng nam miền Nam Sài Gòn 40 tuổi, trầm, đều, lạnh tĩnh và dửng dưng như đang báo giá một giao dịch thường ngày; tuyệt đối không la hét, không dồn dập, nói gọn mà rợn.",
            },
            {
                "id": "l10",
                "speaker": "chi_tu",
                "start": l10_start,
                "window": r2(l11_start - l10_start - 0.05),
                "text": "Ba nhận được chưa? Đúng trang bà nhắn mượn gấp, tui chuyển mười triệu rồi!",
                "style": "Giọng phụ nữ miền Nam Sài Gòn 36 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, giữ cố định một âm sắc ấm áp; gọi điện hỏi thăm gấp và lo lắng xác nhận bạn thân đã nhận được mười triệu vừa chuyển mượn gấp chưa.",
            },
            {
                "id": "l11",
                "speaker": "chi_ba",
                "start": l11_start,
                "window": r2(s6_end - l11_start - 0.05),
                "text": "Trời ơi! Mất trang rồi, họ hàng đồng nghiệp gọi quá trời!",
                "style": "Giọng phụ nữ miền Nam Sài Gòn 35 tuổi, giữ cố định cùng một âm sắc rõ chữ; bàng hoàng hoảng hốt rụng rời khi biết bạn thân đã mất tiền và cả đời sống bị kéo theo.",
            },
            {
                "id": "l12",
                "speaker": "anh_hai",
                "start": l12_start,
                "window": r2(s7_end - l12_start - 0.05),
                "text": "Đừng chuyển tiền chuộc! Báo người thân chặn vạ lây rồi trình báo!",
                "style": "Giọng nam miền Nam Sài Gòn 35 tuổi, giữ cố định cùng một âm sắc; bình tĩnh, dứt khoát ngăn em gái không chuyển tiền chuộc và vững chãi dẫn dắt xử lý đúng cách.",
            },
            {
                "id": "l13",
                "speaker": "nguoi_boc_tran",
                "start": l13_start,
                "window": r2(s8_end - l13_start - 0.05),
                "text": "Không hối, càng lịch sự càng dễ tin: xây kênh trang cá nhân, mất là sập cả đời!",
                "style": "Giọng nam trung niên miền Nam Sài Gòn 40 tuổi, phát âm chuẩn phương ngữ miền Nam, trầm tĩnh, sắc lạnh và gọn dứt khoát; nhấn rõ không hối, lịch sự và sập cả đời.",
            },
        ],
        "chat_bubbles": [],
        "notifications": [],
        "callouts": [],
        "red_flags": {
            "start": s9_start,
            "end": s9_end,
            "stagger_sec": 0.18,
            "title": "NHỚ KỸ",
            "items": [
                "Đối tác cực kỳ lịch sự, không hối gấp nhưng yêu cầu thêm email kế toán vào cài đặt, khiến máy đòi mật khẩu chính chủ",
                "Hộp thư email chính báo đổi quyền quản trị — dù đối phương giải thích hợp lý, bảo “cứ thong thả đọc kỹ” vẫn là bẫy chiếm trang",
                "Gộp kênh kiếm tiền vào trang cá nhân khiến mất trang là mất sạch ảnh gia đình và vạ lây người thân bị lừa tiền",
            ],
            "action": "Tách hẳn trang làm nội dung riêng (email riêng, bảo mật hai lớp bằng ứng dụng) · Thấy email chính báo đổi quyền là dừng tay ngay · Mất trang không chuyển tiền chuộc, báo gấp người thân chặn vạ lây và trình báo công an!",
        },
        "disclaimer": {
            "start": s10_start,
            "end": s10_end,
        },
        "audio": {
            "duck_ambience_db": -6.5,
            "ambience": [
                {"preset": "night_room", "start": s1_start, "end": s2_start, "gain_db": -8.0},
                {"preset": "room_tone", "start": s2_start, "end": s3_start, "gain_db": -8.5},
                {"preset": "night_room", "start": s3_start, "end": s7_start, "gain_db": -8.0},
                {"preset": "room_tone", "start": s7_start, "end": s10_end, "gain_db": -8.5},
            ],
            "foley": [
                # s1: hook mất trang
                {"preset": "phone_vibrate", "at": 0.18, "gain_db": 0.4},
                {"preset": "notification", "at": 0.35, "gain_db": -0.5},
                {"preset": "counter_tick", "at": 0.55, "gain_db": -1.8},
                {"preset": "counter_tick", "at": 1.65, "gain_db": -2.0},
                # s2: hồi tưởng ban ngày
                {"preset": "click", "at": r2(s2_start + 0.30), "gain_db": -1.0},
                # s3: nấc 1 — lời mời chuyên nghiệp + khung xác nhận mật khẩu
                {"preset": "notification", "at": r2(s3_start + 0.18), "gain_db": -0.5},
                {"preset": "typing", "at": r2(s3_start + 0.30), "dur": 0.80, "gain_db": -2.0},
                {"preset": "low_accent", "at": r2(l5_start - 0.25), "dur": 0.85, "gain_db": 0.4},
                {"preset": "marker_draw", "at": r2(l5_start + 0.15), "dur": 0.48, "gain_db": 0.7},
                {"preset": "click", "at": r2(s3_end - 0.35), "gain_db": 0.6},
                # s4: nấc 2 — email chính báo đổi quyền (không đồng hồ hối!) → bấm → sập đỏ
                {"preset": "notification", "at": r2(s4_start + 0.18), "gain_db": 0.4},
                {"preset": "marker_draw", "at": r2(l7_start + 0.15), "dur": 0.48, "gain_db": 0.8},
                {"preset": "heartbeat", "at": r2(l8_start + 0.80), "dur": r2(max(1.8, s4_click_at - l8_start - 0.85)), "gain_db": -2.8},
                {"preset": "click", "at": s4_click_at, "gain_db": 1.0},
                {"preset": "riser", "at": r2(s4_click_at + 0.05), "dur": 0.35, "gain_db": 0.2},
                {"preset": "impact", "at": s4_crash_at, "dur": 0.90, "gain_db": 1.6},
                {"preset": "glitch", "at": r2(s4_crash_at + 0.05), "dur": 0.30, "gain_db": 0.6},
                # s5: giọng lạnh đòi chuộc
                {"preset": "low_accent", "at": r2(s5_start + 0.20), "dur": 0.90, "gain_db": 0.6},
                {"preset": "heartbeat", "at": r2(s5_start + 0.50), "dur": r2(max(2.0, s5_end - s5_start - 0.80)), "gain_db": -2.8},
                # s6: split-screen vạ lây (bank_ting Chị Tư vừa chuyển 10tr + cuộc gọi dồn dập)
                {"preset": "bank_ting", "at": r2(s6_start + 0.20), "gain_db": 0.6},
                {"preset": "phone_ring", "at": r2(l11_start - 0.25), "dur": 0.85, "gain_db": -2.0},
                {"preset": "notification", "at": r2(l11_start + 1.20), "gain_db": -1.0},
                # s7: ứng phó kịp lúc
                {"preset": "click", "at": r2(s7_start + 0.30), "gain_db": 0.2},
                {"preset": "message_send", "at": r2(l12_start + 1.40), "gain_db": 0.4},
                {"preset": "low_accent", "at": r2(l12_start + 1.50), "dur": 0.80, "gain_db": 0.2},
                # s8: bóc trần
                {"preset": "glitch", "at": r2(s8_start + 0.05), "dur": 0.34, "gain_db": 1.0},
                {"preset": "low_accent", "at": r2(s8_start + 0.50), "dur": 0.90, "gain_db": 0.8},
                {"preset": "marker_draw", "at": r2(l13_start + 0.45), "dur": 0.48, "gain_db": 0.8},
                {"preset": "marker_draw", "at": r2(l13_start + 2.15), "dur": 0.48, "gain_db": 0.8},
            ],
            "bgm": [
                {"preset": "suspense_pulse", "start": s1_start, "end": s2_start, "gain_db": -1.5},
                {"preset": "investigative_story", "start": s2_start, "end": s4_start, "gain_db": -1.2},
                {"preset": "tension_drone", "start": s4_start, "end": s6_start, "gain_db": 0.4},
                {"preset": "action_climax", "start": s6_start, "end": s7_start, "gain_db": -1.0},
                {"preset": "investigative_story", "start": s7_start, "end": s9_start, "gain_db": 0.2},
                {"preset": "warm_outro", "start": s9_start, "end": s10_start, "gain_db": 0.0},
            ],
            "duck_extra": [],
        },
        "forbidden_terms": [],
        "publish": {
            "titles": [
                "Không hối một câu, càng lịch sự càng mất trắng: Bẫy xây kênh trang cá nhân! #shorts #bóctrầnlừađảo",
                "Thấy email chính báo đổi quyền quản trị mà vẫn bấm vì đối tác quá chuyên nghiệp! #shorts",
                "Đừng xây kênh kiếm tiền trên trang cá nhân: Mất một trang, vạ lây người thân! #shorts #vạnchuyện",
            ],
            "description": (
                "Chiêu lừa chiếm trang cá nhân của người làm nội dung thế hệ mới không còn hối thúc gấp gáp hay gây áp lực lộ liễu nữa — mà giả làm đối tác nhãn hàng cực kỳ lịch sự, giải thích hợp logic từng bước và còn chủ động khuyên “cứ thong thả đọc kỹ” để bạn tự hạ phòng vệ!\n\n"
                "Chính vì chủ quan xây kênh kiếm thu nhập ngay trên trang cá nhân dùng suốt 10 năm, nạn nhân vừa tự tay bấm qua 2 nấc xác nhận (nhập mật khẩu chính chủ & xác nhận đổi quyền ở hộp thư email chính) là mất trắng trang lẫn ảnh gia đình — kéo theo bạn thân bị mạo danh lừa mất 10 triệu và đảo lộn cả đời sống.\n\n"
                "3 nguyên tắc sống còn:\n"
                "1. Tách biệt hoàn toàn trang cá nhân (riêng tư) và trang làm nội dung/công việc (email riêng, bảo mật hai lớp bằng ứng dụng xác thực).\n"
                "2. Không đánh giá thật–giả qua thái độ lịch sự hay không hối thúc: hễ thấy yêu cầu thêm email lạ hoặc hộp thư email chính báo đổi quyền quản trị là dừng tay ngay lập tức.\n"
                "3. Nếu lỡ mất trang: tuyệt đối không chuyển tiền chuộc, không thuê dịch vụ “lấy lại trang” trên mạng — báo gấp cho gia đình, đồng nghiệp chặn vạ lây, giữ chứng cứ và trình báo cơ quan công an."
            ),
            "pinned_comment": (
                "📌 Ai đang làm nội dung kiếm thu nhập ngay trên trang cá nhân nhớ lưu và gửi cho bạn bè, người thân! "
                "Chiêu mới bây giờ KHÔNG HỐI GẤP — càng lịch sự, càng bảo “cứ thong thả đọc kỹ” càng khiến mình hạ phòng vệ tự bấm xác nhận đổi quyền trong email chính! "
                "Luôn tách riêng trang cá nhân và trang công việc (email riêng, bảo mật 2 lớp bằng ứng dụng). "
                "Nếu lỡ mất trang: tuyệt đối không chuyển tiền chuộc, không thuê dịch vụ “lấy lại trang” trên mạng — báo gấp gia đình, đồng nghiệp để chặn vạ lây và giữ chứng cứ trình báo cơ quan công an! "
                "(Lưu ý: không đăng SĐT, STK hay tên người thật dưới phần bình luận nhé.)"
            ),
            "hashtags": ["#shorts", "#bóctrầnlừađảo", "#cảnhgiáclừađảo"],
            "tags": [
                "bẫy xây kênh trên trang cá nhân",
                "chiếm trang cá nhân",
                "lừa đảo người làm nội dung",
                "thêm email đối tác mất trang",
                "bóc trần lừa đảo",
                "vạn chuyện",
                "shorts",
            ],
            "category": "Education (Giáo dục)",
            "playlist": "Bóc Trần Lừa Đảo – Kỹ Năng Cảnh Giác & An Toàn Đời Thực",
            "thumbnail_sec": r2(s4_crash_at + 0.48),
        },
    }

    OUT_JSON.write_text(json.dumps(ep, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Đã biên dịch {OUT_JSON} ({total_dur:.2f}s · mode={'REAL_TTS' if has_real_tts else 'DRAFT'})")
    return ep


if __name__ == "__main__":
    build()
