# -*- coding: utf-8 -*-
"""Builder cho EP07 (factory619 · 9:16 Short) – Mạo danh Ngày hội & Đêm văn hóa (v2 – nhịp nhanh, Chú Bảy sắc bén).

Chạy lại sau Gate 2 để tự động dàn timeline khớp thời lượng WAV thật (Real-TTS Retiming):
    python factory619/materialAndDraft/EP07/source/build_episode.py
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

CHU_BAY_SHARP_STYLE = (
    "Giọng nam miền Nam Sài Gòn 55 tuổi, chú tổ trưởng khu phố lanh lẹ, "
    "nhịp nói nhanh gọn, dứt khoát, sắc bén, rõ chữ, tuyệt đối không kéo dài hay ngân giọng."
)

# (id, speaker, text, est_dur, optional_style)
LINES = [
    ("l1", "ke_gia_danh", "Cô Tư ơi, chuyển liền tiền quỹ ngày hội vô số em gửi nha, sắp khóa sổ rồi!", 4.51, None),
    ("l2", "co_tu", "Ờ để cô chuyển liền năm trăm ngàn ủng hộ xóm mình!", 4.30, None),
    ("l3", "be_na", "Con cũng đang đóng tiền cọc với bảo hiểm tình nguyện viên đêm văn hóa!", 4.22, None),
    ("l4", "ong_bay", "Khoan bấm! Khu phố thu quỹ công khai, tình nguyện viên cũng không ai thu cọc!", 4.0, CHU_BAY_SHARP_STYLE),
    ("l5", "be_na", "Ủa chú Bảy, vậy trang sự kiện với người đang gọi cô Tư là ai?!", 3.8, None),
    ("l6", "ong_bay", "Nhìn kỹ tên người nhận trên hai máy kìa! Toàn tài khoản cá nhân lạ hoắc!", 4.0, CHU_BAY_SHARP_STYLE),
    ("l7", "be_na", "Trời ơi thiệt luôn! Trang mới lập hôm qua mà bắt chuyển cho cá nhân!", 4.2, None),
    ("l8", "co_tu", "Máy cô cũng tên cá nhân, nghe chú Bảy khui ra là nó cúp máy liền!", 4.2, None),
    ("l9", "nguoi_boc_tran", "Mùa lễ hội, đừng chuyển tiền quỹ hay phí sự kiện vô tài khoản cá nhân!", 4.74, None),
]

GAP = 0.22
LEAD = 0.30


def dur_of(lid: str, est_d: float) -> float:
    return real.get(lid, est_d)


dialogue = []


def place(lid: str, spk: str, text: str, est_d: float, style: str | None, start_t: float) -> float:
    d = dur_of(lid, est_d)
    item = {
        "id": lid,
        "speaker": spk,
        "start": round(start_t, 2),
        "window": round(max(d, est_d) + 1.5, 2),
        "text": text,
    }
    if style:
        item["style"] = style
    dialogue.append(item)
    return start_t + d


# Scene 1: l1
s1_start = 0.0
end_l1 = place(*LINES[0], s1_start + 0.4)
s1_end = round(max(4.8, end_l1 + 0.3), 2)

# Scene 2: l2, l3
s2_start = s1_end
end_l2 = place(*LINES[1], s2_start + LEAD)
end_l3 = place(*LINES[2], end_l2 + GAP)
s2_end = round(end_l3 + 0.35, 2)

# Scene 3: l4 (Chú Bảy chặn gọn), l5 (Bé Na ngơ ngác hỏi)
s3_start = s2_end
end_l4 = place(*LINES[3], s3_start + LEAD)
end_l5 = place(*LINES[4], end_l4 + GAP)
s3_end = round(end_l5 + 0.35, 2)

# Scene 4: l6 (Chú Bảy khui tên cá nhân), l7 (Bé Na bật ngửa), l8 (Cô Tư báo cúp máy)
s4_start = s3_end
end_l6 = place(*LINES[5], s4_start + 0.35)
end_l7 = place(*LINES[6], end_l6 + GAP)
end_l8 = place(*LINES[7], end_l7 + GAP)
s4_end = round(end_l8 + 0.4, 2)

# Scene 5: l9 (Người Bóc Trần)
s5_start = s4_end
end_l9 = place(*LINES[8], s5_start + 0.35)
s5_end = round(end_l9 + 0.4, 2)

# Scene 6: Red flags (3.3s) + Disclaimer (2.8s >= 2.5s min)
s6_start = s5_end
rf_end = round(s6_start + 3.3, 2)
total = round(rf_end + 2.8, 2)

scenes = [
    {
        "id": "s1_hook",
        "image": "assets/scene1.jpg",
        "start": s1_start,
        "end": s1_end,
        "motion": {"scale": [1.05, 1.14], "focus": [[0.5, 0.5], [0.5, 0.46]], "wobble": "tense"},
    },
    {
        "id": "s2_moi_nhu",
        "image": "assets/scene2.jpg",
        "start": s2_start,
        "end": s2_end,
        "motion": {"scale": [1.03, 1.11], "focus": [[0.5, 0.5], [0.48, 0.45]], "wobble": "calm"},
        "transition_in": {"type": "dissolve", "dur": 0.3},
    },
    {
        "id": "s3_ong_bay_chan",
        "image": "assets/scene3.jpg",
        "start": s3_start,
        "end": s3_end,
        "motion": {"scale": [1.04, 1.14], "focus": [[0.5, 0.48], [0.5, 0.44]], "wobble": "handheld"},
        "transition_in": {"type": "dissolve", "dur": 0.28},
    },
    {
        "id": "s4_cu_chot",
        "image": "assets/scene4.jpg",
        "start": s4_start,
        "end": s4_end,
        "motion": {"scale": [1.13, 1.03], "focus": [[0.5, 0.46], [0.5, 0.5]], "wobble": "handheld"},
        "transition_in": {"type": "flash_white", "dur": 0.25},
        "shakes": [{"at": round(s4_start + 0.18, 2), "amp": 28}],
    },
    {
        "id": "s5_boc_tran",
        "image": "assets/scene5.jpg",
        "start": s5_start,
        "end": s5_end,
        "motion": {"scale": [1.02, 1.09], "focus": [[0.5, 0.5], [0.5, 0.46]], "wobble": "calm"},
        "transition_in": {"type": "glitch", "dur": 0.3},
    },
    {
        "id": "s6_dau_hieu",
        "image": "assets/scene6.jpg",
        "start": s6_start,
        "end": total,
        "motion": {"scale": [1.02, 1.06], "focus": [[0.5, 0.5], [0.5, 0.5]], "wobble": "none"},
        "transition_in": {"type": "fade_black", "dur": 0.35},
    },
]

episode = {
    "episode_id": "EP07",
    "slug": "BayMuaLeHoi",
    "title": "Mạo danh Ngày hội & Đêm văn hóa – Lộ tẩy ở tên tài khoản nhận",
    "version": "v2",
    "scam_family": "ON-09",
    "duration_sec": total,
    "hook": {
        "kicker": "BẪY MẠO DANH MÙA LỄ HỘI",
        "title": "Giục đóng quỹ ngày hội & cọc tình nguyện viên: Chú Bảy chỉ 1 chỗ lộ ngay!",
        "start": 0.3,
        "end": round(min(4.2, s1_end - 0.2), 2),
    },
    "scenes": scenes,
    "dialogue": dialogue,
    "chat_bubbles": [],
    "callouts": [
        {
            "text": "TRANG SỰ KIỆN LẠ: ĐÒI TIỀN CỌC & PHÍ BẢO HIỂM TNV",
            "style": "warn",
            "start": round(end_l2 + 0.18, 2),
            "end": round(s2_end - 0.18, 2),
            "y": 190,
        },
        {
            "text": "CHÚ BẢY VẠCH MẶT: CẢ HAI ĐỀU LÀ TÀI KHOẢN CÁ NHÂN LẠ!",
            "style": "danger",
            "start": round(s4_start + 0.25, 2),
            "end": round(s4_end - 0.2, 2),
            "y": 190,
        },
    ],
    "red_flags": {
        "start": s6_start,
        "end": rf_end,
        "stagger_sec": 0.4,
        "title": "NHỚ KỸ",
        "items": [
            "Gọi điện, nhắn tin giục đóng quỹ ngày hội, khuyến học vào tài khoản cá nhân",
            "Trang giả sự kiện văn hóa bán vé ảo, thu \"tiền cọc / phí bảo hiểm\" tình nguyện viên",
        ],
        "action": "Quỹ khu phố luôn công khai · Sự kiện thật không thu cọc cá nhân · Hỏi tổ dân phố trước khi chuyển!",
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
            {"preset": "phone_ring", "at": 0.05, "dur": 1.1, "gain_db": -1.0},
            {"preset": "notification", "at": round(end_l2 + 0.12, 2), "gain_db": -1.5},
            {"preset": "heartbeat", "at": round(s3_start + 0.3, 2), "dur": round(s3_end - s3_start - 0.5, 2), "gain_db": -1.5},
            {"preset": "riser", "at": round(max(0.0, s4_start - 1.4), 2), "dur": 1.4, "gain_db": 1.5},
            {"preset": "impact", "at": round(s4_start + 0.1, 2), "dur": 1.6, "gain_db": 2.5},
            {"preset": "call_end", "at": round(end_l7 + 0.08, 2), "dur": 1.1, "gain_db": 0.8},
            {"preset": "glitch", "at": s5_start, "gain_db": 0.0},
        ],
        "bgm": [
            {"preset": "suspense_pulse", "start": 0.0, "end": s3_start},
            {"preset": "tension_drone", "start": s3_start, "end": s4_start, "gain_db": 1.5},
            {"preset": "action_climax", "start": s4_start, "end": s6_start, "gain_db": 2.0},
            {"preset": "warm_outro", "start": s6_start, "end": total},
        ],
        "duck_extra": [
            {"start": round(s4_start - 0.2, 2), "end": round(s4_start + 0.25, 2), "bgm_db": -14, "amb_db": -10},
        ],
    },
    "forbidden_terms": [],
    "publish": {
        "titles": [
            "Giục đóng quỹ ngày hội & cọc tình nguyện viên: Chú Bảy chỉ 1 chỗ lộ ngay! #shorts #bóctrầnlừađảo",
            "Suýt mất tiền oan vì cuộc gọi thu quỹ ngày hội và trang Đêm Văn Hóa giả! #shorts #cảnhgiáclừađảo",
            "2 chiêu mạo danh mùa lễ hội cuối năm: Đừng chuyển vào tài khoản cá nhân! #shorts #vạnchuyện",
        ],
        "description": "Cuối năm rộn ràng ngày hội khu phố và các đêm giao lưu văn hóa, kẻ gian lập tức tung 2 cái bẫy đánh thẳng vào lòng tốt của người lớn tuổi và sự nhiệt tình của giới trẻ:\n"
                       "1️⃣ Gọi điện, nhắn tin giục đóng góp \"quỹ ngày hội, quỹ khuyến học\" gấp trước giờ khóa sổ.\n"
                       "2️⃣ Lập trang mạng giả mạo chương trình văn hóa để bán vé ảo hoặc tuyển tình nguyện viên rồi thu \"tiền đặt cọc thẻ, phí bảo hiểm\".\n\n"
                       "May nhờ Chú Bảy tổ trưởng bước tới chỉ thẳng vào TÊN NGƯỜI NHẬN trên cả hai máy: Cả hai đều là TÀI KHOẢN CÁ NHÂN LẠ! Trong khi hoạt động vận động tự nguyện ở khu dân cư thật luôn công khai, minh bạch và tình nguyện viên sự kiện cộng đồng không bao giờ phải đóng tiền cọc cá nhân.\n\n"
                       "✅ Nhớ kỹ: Kiểm tra kỹ tên người nhận và hỏi trực tiếp tổ dân phố trước khi chuyển bất kỳ khoản tiền ủng hộ hay phí sự kiện nào!",
        "pinned_comment": "📌 Quỹ khu phố thật luôn công khai minh bạch; tình nguyện viên sự kiện thật không thu tiền cọc vào tài khoản cá nhân! Cả nhà nhớ dặn ba mẹ và các bạn sinh viên dịp lễ hội cuối năm nhé!",
        "hashtags": ["#shorts", "#bóctrầnlừađảo", "#cảnhgiáclừađảo"],
        "tags": [
            "mạo danh quỹ từ thiện",
            "lừa đảo sự kiện văn hóa",
            "tuyển tình nguyện viên lừa đảo",
            "vé sự kiện giả",
            "tài khoản cá nhân lừa đảo",
            "bóc trần lừa đảo",
            "vạn chuyện",
            "shorts",
        ],
        "category": "Education (Giáo dục)",
        "playlist": "Bóc Trần Lừa Đảo – Kỹ Năng Cảnh Giác & An Toàn Đời Thực",
        "thumbnail_sec": round(s4_start + 1.2, 2),
    },
}

OUT.write_text(json.dumps(episode, ensure_ascii=False, indent=2), encoding="utf-8")
words = sum(len(l["text"].split()) for l in dialogue)
print(f"episode.json [EP07 v2]: {total:.2f}s · {len(scenes)} cảnh · {len(dialogue)} câu · {words} từ · "
      f"{'TTS thật' if real else 'ước tính'} ({len(real)} câu thật)")
