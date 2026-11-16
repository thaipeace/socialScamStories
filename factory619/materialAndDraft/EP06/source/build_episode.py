# -*- coding: utf-8 -*-
"""Builder cho EP06 (factory619 · 9:16 Short) – Check-in du lịch thời gian thực mời trộm vào nhà (v5).

Nâng cấp v5 theo phản hồi duyệt:
  1. Mở đầu trên xe trở về nhà xem lại ảnh check-in đi biển 4 ngày (thoại tự nhiên đời thường, bỏ câu cải lương ở cổng).
  2. Tăng tốc giọng Chú tổ an ninh (`ong_bay` & `chu_bao_ve`), xóa toàn bộ khoảng lặng câu giờ ở 0:25, nhịp dứt khoát ~47–49s.
  3. Cấu trúc `assets/` chuẩn EP01: đa ảnh keyframe (`scene1..6.jpg` + `scene1_b..6_b.jpg`) + video `30fps` (`scene1..6.mp4`).

Chạy lại sau Gate 2 và sau khi render `assets/scene*.mp4`:
    python factory619/materialAndDraft/EP06/source/build_episode.py
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

BURGLAR_SNEAK_STYLE = (
    "Giọng nam miền Nam Sài Gòn 28 tuổi, hạ giọng ranh mãnh, thì thầm gấp gáp với đồng bọn trong đêm, "
    "nhịp nói nhanh gọn, rõ chữ, tuyệt đối không kéo dài."
)

ONG_BAY_BRISK_STYLE = (
    "Giọng nam miền Nam Sài Gòn 58 tuổi, chú tổ trưởng an ninh khu phố lanh lẹ, "
    "nhịp nói nhanh gọn, dứt khoát, sắc bén, rõ chữ, tuyệt đối không kéo dài chữ hay ngân giọng chậm."
)

BAO_VE_BRISK_STYLE = (
    "Giọng nam miền Nam Sài Gòn 50 tuổi, chú tuần tra an ninh khu phố nhanh nhẹn, dứt khoát, "
    "nhịp nói nhanh gọn, rõ chữ, tự nhiên, tuyệt đối không nghỉ dài giữa câu hay kéo giọng."
)

# (id, speaker, text, est_dur, overrides_dict)
LINES: list[tuple[str, str, str, float, dict]] = [
    (
        "l1",
        "chi_ba",
        "Hình check-in cả nhà đi biển bốn ngày hôm bữa, quá trời người thả tim nè anh!",
        3.85,
        {},
    ),
    (
        "l1b",
        "anh_hai",
        "Xe tới cổng nhà mình rồi kìa, xuống mở khóa vô nhà thôi em!",
        3.40,
        {},
    ),
    (
        "l2",
        "ke_ngot_ngao_nam",
        "Nhà này đăng hình đi biển bốn ngày chưa về, vô cạy khóa lẹ!",
        3.35,
        {"af": "default", "style": BURGLAR_SNEAK_STYLE},
    ),
    (
        "l3",
        "anh_hai",
        "Ủa mình ơi, đi chơi về sao ổ khóa bị cạy xước hết?!",
        4.66,
        {},
    ),
    (
        "l4",
        "chi_ba",
        "Trời ơi, nhà suýt mất trộm mà đi chơi không biết gì!",
        4.02,
        {},
    ),
    (
        "l5",
        "ong_bay",
        "May mà tổ an ninh khu phố có kết bạn mạng với tụi con!",
        3.30,
        {"style": ONG_BAY_BRISK_STYLE},
    ),
    (
        "l6",
        "chu_bao_ve",
        "Thấy gia đình đăng bài đi vắng sơ hở, đêm qua mấy chú tuần tra canh giùm!",
        3.65,
        {"voice": "Fenrir", "af": "default", "style": BAO_VE_BRISK_STYLE},
    ),
    (
        "l7",
        "chi_ba",
        "Hú hồn! Không có các chú tuần tra giúp là mất sạch rồi!",
        3.70,
        {},
    ),
    (
        "l8",
        "nguoi_boc_tran",
        "Đi chơi thường về nhà mới biết mất trộm; về nhà hãy đăng ảnh!",
        5.10,
        {
            "subtitle": [
                "Đi chơi xa thường về nhà mới biết mất trộm;",
                "hãy đợi về đến nhà rồi mới đăng ảnh!",
            ]
        },
    ),
]

GAP = 0.20
LEAD = 0.28
dialogue: list[dict] = []


def dur_of(lid: str, est_d: float) -> float:
    return real.get(lid, est_d)


def place(lid: str, spk: str, text: str, est_d: float, extra: dict, start_t: float) -> float:
    d = dur_of(lid, est_d)
    item: dict = {
        "id": lid,
        "speaker": spk,
        "start": round(start_t, 2),
        "window": round(max(d, est_d) + 1.4, 2),
        "text": text,
    }
    item.update(extra)
    dialogue.append(item)
    return start_t + d


# Scene 1 (Hook – trên xe về nhà xem lại ảnh check-in): l1 + l1b
s1_start = 0.0
end_l1 = place(*LINES[0], s1_start + 0.32)
s1_split = round(end_l1 + 0.10, 2)
end_l1b = place(*LINES[1], end_l1 + GAP)
s1_end = round(end_l1b + 0.28, 2)

# Scene 2 (Đêm kẻ gian mò tới cạy khóa -> Ban ngày xe vừa dừng trước cổng thấy khóa trầy): l2 + l3
s2_start = s1_end
end_l2 = place(*LINES[2], s2_start + LEAD)
s2_split = round(end_l2 + 0.14, 2)
end_l3 = place(*LINES[3], end_l2 + 0.28)
s2_end = round(end_l3 + 0.30, 2)

# Scene 3 (Bàng hoàng trước cổng -> Chú tổ trưởng an ninh bước tới nói nhanh gọn, KHÔNG CÂU GIỜ): l4 + l5
s3_start = s2_end
end_l4 = place(*LINES[4], s3_start + LEAD)
s3_split = round(end_l4 + 0.12, 2)
end_l5 = place(*LINES[5], end_l4 + GAP)
s3_end = round(end_l5 + 0.30, 2)

# Scene 4 (Cú chốt: Tổ an ninh rọi đèn thổi còi đuổi trộm đêm qua -> Vợ chồng thở phào cảm ơn): l6 + l7
s4_start = s3_end
end_l6 = place(*LINES[6], s4_start + 0.30)
s4_split = round(end_l6 + 0.12, 2)
end_l7 = place(*LINES[7], end_l6 + GAP)
s4_end = round(end_l7 + 0.32, 2)

# Scene 5 (Bóc trần): l8
s5_start = s4_end
end_l8 = place(*LINES[8], s5_start + 0.30)
s5_split = round(s5_start + (end_l8 - s5_start) * 0.52, 2)
s5_end = round(end_l8 + 0.32, 2)

# Scene 6 (Thẻ Nhớ Kỹ + Disclaimer >= 2.5s)
s6_start = s5_end
rf_end = round(s6_start + 3.10, 2)
total = round(rf_end + 2.70, 2)
if total < 45.5:
    pad = round(45.5 - total, 2)
    rf_end = round(rf_end + pad, 2)
    total = round(rf_end + 2.70, 2)
s6_split = round(s6_start + 2.20, 2)


def scene_entry(idx: int, sid: str, start: float, end: float, motion: dict,
                transition_in: dict | None = None, shakes: list | None = None) -> dict:
    sc: dict = {
        "id": sid,
        "image": f"assets/scene{idx}.jpg",
    }
    v_rel = f"assets/scene{idx}.mp4"
    if (EP_DIR / v_rel).is_file():
        sc["video"] = v_rel
    sc["start"] = start
    sc["end"] = end
    sc["motion"] = motion
    if transition_in:
        sc["transition_in"] = transition_in
    if shakes:
        sc["shakes"] = shakes
    return sc


scenes = [
    scene_entry(
        1, "s1_hook", s1_start, s1_end,
        {"scale": [1.05, 1.13], "focus": [[0.5, 0.5], [0.5, 0.47]], "wobble": "calm"},
    ),
    scene_entry(
        2, "s2_moi_nhu", s2_start, s2_end,
        {"scale": [1.04, 1.13], "focus": [[0.5, 0.5], [0.47, 0.45]], "wobble": "tense"},
        transition_in={"type": "dissolve", "dur": 0.28},
    ),
    scene_entry(
        3, "s3_leo_thang", s3_start, s3_end,
        {"scale": [1.04, 1.14], "focus": [[0.5, 0.48], [0.5, 0.44]], "wobble": "handheld"},
        transition_in={"type": "dissolve", "dur": 0.28},
    ),
    scene_entry(
        4, "s4_cu_chot", s4_start, s4_end,
        {"scale": [1.13, 1.04], "focus": [[0.52, 0.46], [0.5, 0.5]], "wobble": "handheld"},
        transition_in={"type": "flash_white", "dur": 0.24},
        shakes=[{"at": round(s4_start + 0.16, 2), "amp": 30}],
    ),
    scene_entry(
        5, "s5_boc_tran", s5_start, s5_end,
        {"scale": [1.02, 1.09], "focus": [[0.5, 0.5], [0.5, 0.46]], "wobble": "calm"},
        transition_in={"type": "glitch", "dur": 0.30},
    ),
    scene_entry(
        6, "s6_dau_hieu", s6_start, total,
        {"scale": [1.02, 1.06], "focus": [[0.5, 0.5], [0.5, 0.5]], "wobble": "none"},
        transition_in={"type": "fade_black", "dur": 0.32},
    ),
]

episode = {
    "episode_id": "EP06",
    "slug": "CheckInDuLich",
    "title": "Thói quen check-in du lịch thời gian thực mời trộm vào nhà",
    "version": "v5",
    "scam_family": "MIX-05",
    "duration_sec": total,
    "hook": {
        "kicker": "SƠ HỞ CHECK-IN DU LỊCH",
        "title": "Trên xe về nhà xem lại ảnh check-in đi biển, mở cổng thấy ổ khóa bị cạy!",
        "start": 0.25,
        "end": round(min(4.1, end_l1), 2),
    },
    "scenes": scenes,
    "scene_splits_sec": {
        "scene1": round(s1_split - s1_start, 3),
        "scene2": round(s2_split - s2_start, 3),
        "scene3": round(s3_split - s3_start, 3),
        "scene4": round(s4_split - s4_start, 3),
        "scene5": round(s5_split - s5_start, 3),
        "scene6": round(s6_split - s6_start, 3),
    },
    "dialogue": dialogue,
    "chat_bubbles": [],
    "callouts": [],
    "red_flags": {
        "start": s6_start,
        "end": rf_end,
        "stagger_sec": 0.38,
        "title": "NHỚ KỸ",
        "items": [
            "Đăng công khai \"cả nhà đi du lịch dài ngày\" khiến kẻ gian biết chắc nhà không có ai",
            "Khi đi chơi xa thường chỉ phát hiện mất trộm lúc mọi chuyện đã rồi hoặc khi về đến nhà",
        ],
        "action": "Đi chơi cứ vui hết nấc, nhưng ảnh đẹp thì về nhà hãy đăng & báo an ninh khu phố khi đi xa!",
    },
    "disclaimer": {
        "start": rf_end,
        "end": total,
    },
    "audio": {
        "ambience": [
            {"preset": "street", "start": 0.0, "end": total, "gain_db": -3.0},
        ],
        "foley": [
            {"preset": "notification", "at": 0.30, "gain_db": -1.5},
            {"preset": "footsteps", "at": round(s2_split + 0.05, 2), "dur": 1.6, "gain_db": -2.0},
            {"preset": "heartbeat", "at": round(s3_start + 0.25, 2), "dur": round(max(2.0, s3_end - s3_start - 0.5), 2), "gain_db": -1.0},
            {"preset": "riser", "at": round(max(0.0, s4_start - 1.15), 2), "dur": 1.15, "gain_db": 2.0},
            {"preset": "impact", "at": round(s4_start + 0.08, 2), "dur": 1.9, "gain_db": 3.2},
            {"preset": "whistle", "at": round(s4_start + 0.22, 2), "gain_db": 2.0},
            {"preset": "glitch", "at": s5_start, "gain_db": 0.0},
        ],
        "bgm": [
            {"preset": "suspense_pulse", "start": 0.0, "end": s3_start},
            {"preset": "tension_drone", "start": s3_start, "end": s4_start, "gain_db": 1.8},
            {"preset": "action_climax", "start": s4_start, "end": s6_start, "gain_db": 2.6},
            {"preset": "warm_outro", "start": s6_start, "end": total},
        ],
        "duck_extra": [
            {"start": round(s4_start - 0.20, 2), "end": round(s4_start + 0.22, 2), "bgm_db": -14, "amb_db": -10},
        ],
    },
    "forbidden_terms": [],
    "publish": {
        "titles": [
            "Trên xe về nhà xem lại ảnh check-in đi biển, mở cổng thấy ổ khóa bị cạy! #shorts #bảomậtthôngtin",
            "Đi du lịch về mới tá hỏa biết nhà suýt mất trộm chỉ vì 1 bức ảnh check-in! #shorts #cảnhgiáclừađảo",
            "Tại sao ảnh đẹp đi du lịch nhất định phải đợi về đến nhà rồi mới đăng? #shorts #bóctrầnlừađảo",
        ],
        "description": (
            "Trên chuyến xe trở về sau 4 ngày đi biển, vợ chồng Anh Hai – Chị Ba vẫn vui vẻ lướt xem lại tấm ảnh "
            "check-in \"cả nhà đi biển 4 ngày\" đăng công khai từ hôm khởi hành với hàng chục lượt thả tim.\n\n"
            "Vừa bước xuống xe tới cổng nhà, hai vợ chồng tá hỏa phát hiện ổ khóa bị cạy trầy xước! May nhờ tổ an ninh "
            "khu phố có kết bạn mạng xã hội với gia đình, thấy bài đăng đi vắng quá sơ hở nên đêm qua đã chủ động rọi đèn "
            "tuần tra ngang nhà và thổi còi xua đuổi kẻ trộm kịp lúc!\n\n"
            "⚠️ 2 điều cần nhớ kỹ:\n"
            "1. Đăng công khai \"cả nhà đi vắng dài ngày\" chẳng khác nào báo cho kẻ gian biết nhà không có ai\n"
            "2. Khi đi chơi xa, gia đình thường chỉ biết chuyện khi đã về đến nhà\n\n"
            "✅ Việc nên làm: Đi chơi cứ vui hết nấc, nhưng ảnh đẹp thì về nhà hãy đăng & nhớ báo tổ an ninh khu phố khi vắng nhà dài ngày!"
        ),
        "pinned_comment": (
            "📌 Đi chơi xa thường chỉ biết chuyện khi về đến nhà thôi! Đừng đăng lịch trình \"cả nhà đang đi vắng\" "
            "theo thời gian thực, và nhớ báo tổ an ninh khu phố khi đi xa nhé!"
        ),
        "hashtags": ["#shorts", "#bảomậtthôngtin", "#cảnhgiáclừađảo"],
        "tags": [
            "bóc trần lừa đảo",
            "bảo mật thông tin",
            "du lịch an toàn",
            "check in du lịch",
            "an ninh khu phố",
            "phòng chống trộm cắp",
            "vạn chuyện",
            "shorts",
        ],
        "category": "Education (Giáo dục)",
        "playlist": "Bóc Trần Lừa Đảo – Kỹ Năng Cảnh Giác & An Toàn Đời Thực",
        "thumbnail_sec": round(s4_start + 1.0, 2),
    },
}

OUT.write_text(json.dumps(episode, ensure_ascii=False, indent=2), encoding="utf-8")
words = sum(len(l["text"].split()) for l in dialogue)
print(
    f"episode.json [EP06 v5]: {total:.2f}s · {len(scenes)} cảnh · {len(dialogue)} câu · {words} từ · "
    f"splits={episode['scene_splits_sec']} · {'TTS thật' if real else 'ước tính'} ({len(real)} câu thật)"
)
