# -*- coding: utf-8 -*-
"""
Script dựng & tự động kiểm tra bản nháp `factory196/materialAndDraft/EP04/episode.json`.
Khi quay lại sản xuất thật:
  1. Sinh 16 ảnh `assets/c01.jpg .. c16.jpg` theo `IMAGE_PROMPTS.md`.
  2. Chạy `python factory196/_engine/run.py gate0 EP04` -> `gate EP04 2` (TTS thật).
  3. Cập nhật lại mốc thời gian theo độ dài WAV thật rồi chạy Gate 3 -> Gate 5 (Staging).
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

EP_DIR = Path(__file__).resolve().parents[1]
ROOT = EP_DIR.parents[2]
sys.path.insert(0, str(ROOT / "03_ENGINE"))

from core import Episode, save_json  # noqa: E402
from cli import gate0  # noqa: E402
from gate5_render_audit import ACCOUNT_RE, PHONE_RE, URL_RE, _contains  # noqa: E402

STYLES = {
    "na": (
        "Giọng cô gái trẻ miền Nam Sài Gòn 23 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
        "giữ cố định một âm sắc trong trẻo tự nhiên đời thực, rõ chữ, nhiệt tình chân thật ở đầu phim "
        "và nghẹn giọng lo lắng khi gặp biến cố, tuyệt đối không gào khóc cải lương."
    ),
    "chi_hai": (
        "Giọng phụ nữ miền Nam Sài Gòn 35 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
        "giữ cố định một âm sắc sắc sảo, điềm tĩnh, dứt khoát và ấm áp khi bảo vệ em trong nhà."
    ),
    "anh_hai": (
        "Giọng nam miền Nam Sài Gòn 35 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
        "giữ cố định một âm sắc trầm ấm, điềm tĩnh, thẳng gọn, chững chạc."
    ),
    "tung": (
        "Giọng nam thanh niên miền Nam Sài Gòn 22 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
        "giữ cố định một âm sắc trẻ trung tông sáng, nhịp nhanh gọn, rõ chữ."
    ),
    "trang": (
        "Giọng nữ miền Nam Sài Gòn 30 tuổi, phát âm chuẩn phương ngữ miền Nam xuyên suốt mọi câu, "
        "giữ cố định một âm sắc êm mượt, lịch thiệp, thân tình như người làm truyền thông sự kiện chuyên nghiệp."
    ),
    "boc_tran": (
        "Giọng nam trung niên miền Nam Sài Gòn, điềm tĩnh, trầm ấm, rõ chữ, khách quan và sắc bén "
        "khi giải phẫu cơ chế tâm lý, nhịp vừa phải, nhấn từ khóa quan trọng."
    ),
}


def line(
    lid: str,
    role: str,
    start: float,
    window: float,
    text: str,
    *,
    phone: bool = False,
) -> dict:
    mapping = {
        "na": ("be_na", "Leda", "NA", "Na", STYLES["na"]),
        "chi_hai": ("chi_ba", "Kore", "CHỊ HAI", "Chị Hai", STYLES["chi_hai"]),
        "anh_hai": ("anh_hai", "Orus", "ANH HAI", "Anh Hai", STYLES["anh_hai"]),
        "tung": ("thang_tun", "Puck", "TÙNG", "Tùng", STYLES["tung"]),
        "trang": ("ke_ngot_ngao_nu", "Aoede", "TRANG", "Chị Trang", STYLES["trang"]),
        "boc_tran": ("nguoi_boc_tran", "Charon", "BÓC TRẦN", "Người Bóc Trần", STYLES["boc_tran"]),
    }
    spk, voice, short, label, style = mapping[role]
    d = {
        "id": lid,
        "speaker": spk,
        "model": "gemini-3.8-flash-tts",
        "voice": voice,
        "label_short": short,
        "speaker_label": label,
        "style": style,
        "start": round(start, 2),
        "window": round(window, 2),
        "text": text,
    }
    if phone:
        d["af"] = "phone"
    return d


def build() -> dict:
    duration = 285.0
    scenes = [
        {
            "id": "s01_hook_panic",
            "image": "assets/c01.jpg",
            "start": 0.0,
            "end": 9.0,
            "motion": {"scale": [1.04, 1.14], "focus": [[0.5, 0.5], [0.52, 0.46]], "wobble": "tense"},
            "shakes": [{"at": 0.45, "dur": 0.4, "amp": 18}],
        },
        {
            "id": "s02_hook_accused",
            "image": "assets/c02.jpg",
            "start": 9.0,
            "end": 20.0,
            "motion": {"scale": [1.02, 1.12], "focus": [[0.48, 0.5], [0.52, 0.46]], "wobble": "tense"},
            "transition_in": {"type": "flash_white", "dur": 0.28},
        },
        {
            "id": "s03_booth_heat",
            "image": "assets/c03.jpg",
            "start": 20.0,
            "end": 33.0,
            "motion": {"scale": [1.02, 1.09], "focus": [[0.5, 0.5], [0.5, 0.47]], "wobble": "calm"},
            "transition_in": {"type": "fade_black", "dur": 0.45},
        },
        {
            "id": "s04_trang_arrival",
            "image": "assets/c04.jpg",
            "start": 33.0,
            "end": 55.5,
            "motion": {"scale": [1.02, 1.10], "focus": [[0.52, 0.5], [0.48, 0.47]], "wobble": "calm"},
            "transition_in": {"type": "dissolve", "dur": 0.4},
        },
        {
            "id": "s05_sold_out_bait",
            "image": "assets/c05.jpg",
            "start": 55.5,
            "end": 74.0,
            "motion": {"scale": [1.03, 1.11], "focus": [[0.48, 0.5], [0.52, 0.46]], "wobble": "handheld"},
            "transition_in": {"type": "fade_black", "dur": 0.4},
        },
        {
            "id": "s06_collecting_orders",
            "image": "assets/c06.jpg",
            "start": 74.0,
            "end": 93.0,
            "motion": {"scale": [1.02, 1.09], "focus": [[0.5, 0.5], [0.5, 0.46]], "wobble": "calm"},
            "transition_in": {"type": "fade_black", "dur": 0.4},
        },
        {
            "id": "s07_chi_hai_warning",
            "image": "assets/c07.jpg",
            "start": 93.0,
            "end": 117.5,
            "motion": {"scale": [1.02, 1.10], "focus": [[0.46, 0.48], [0.54, 0.46]], "wobble": "handheld"},
            "transition_in": {"type": "dissolve", "dur": 0.35},
        },
        {
            "id": "s08_transfer_sent",
            "image": "assets/c08.jpg",
            "start": 117.5,
            "end": 128.0,
            "motion": {"scale": [1.0, 1.14], "focus": [[0.5, 0.5], [0.5, 0.45]], "wobble": "tense"},
            "transition_in": {"type": "dissolve", "dur": 0.3},
        },
        {
            "id": "s09_delay_excuse",
            "image": "assets/c09.jpg",
            "start": 128.0,
            "end": 141.5,
            "motion": {"scale": [1.02, 1.10], "focus": [[0.5, 0.5], [0.48, 0.46]], "wobble": "calm"},
            "transition_in": {"type": "fade_black", "dur": 0.4},
        },
        {
            "id": "s10_blocked_shock",
            "image": "assets/c10.jpg",
            "start": 141.5,
            "end": 152.5,
            "motion": {"scale": [1.04, 1.15], "focus": [[0.5, 0.5], [0.5, 0.44]], "wobble": "tense"},
            "transition_in": {"type": "flash_red", "dur": 0.28},
            "shakes": [{"at": 141.8, "dur": 0.4, "amp": 20}],
        },
        {
            "id": "s11_double_denial_tung",
            "image": "assets/c11.jpg",
            "start": 152.5,
            "end": 173.5,
            "motion": {"scale": [1.03, 1.12], "focus": [[0.52, 0.48], [0.48, 0.46]], "wobble": "handheld"},
            "transition_in": {"type": "dissolve", "dur": 0.35},
        },
        {
            "id": "s12_chi_hai_stops_lock",
            "image": "assets/c12.jpg",
            "start": 173.5,
            "end": 186.0,
            "motion": {"scale": [1.12, 1.03], "focus": [[0.5, 0.46], [0.5, 0.5]], "wobble": "tense"},
            "transition_in": {"type": "flash_white", "dur": 0.28},
            "shakes": [{"at": 179.6, "dur": 0.38, "amp": 22}],
        },
        {
            "id": "s13_compile_files",
            "image": "assets/c13.jpg",
            "start": 186.0,
            "end": 210.0,
            "motion": {"scale": [1.02, 1.08], "focus": [[0.5, 0.5], [0.5, 0.47]], "wobble": "calm"},
            "transition_in": {"type": "fade_black", "dur": 0.4},
        },
        {
            "id": "s14_outside_station",
            "image": "assets/c14.jpg",
            "start": 210.0,
            "end": 234.0,
            "motion": {"scale": [1.02, 1.08], "focus": [[0.5, 0.48], [0.5, 0.5]], "wobble": "calm"},
            "transition_in": {"type": "dissolve", "dur": 0.4},
        },
        {
            "id": "s15_narrator",
            "image": "factory196/materialAndDraft/EP01b/assets/scene15.jpg",
            "start": 234.0,
            "end": 241.5,
            "motion": {"scale": [1.02, 1.09], "focus": [[0.5, 0.5], [0.5, 0.47]], "wobble": "calm"},
            "transition_in": {"type": "glitch", "dur": 0.35},
        },
        {
            "id": "s16_diagram_3steps",
            "image": "assets/c15.jpg",
            "start": 241.5,
            "end": 256.5,
            "motion": {"scale": [1.0, 1.05], "focus": [[0.5, 0.5], [0.5, 0.5]], "wobble": "none"},
            "transition_in": {"type": "dissolve", "dur": 0.3},
        },
        {
            "id": "s17_diagram_middleman",
            "image": "assets/c16.jpg",
            "start": 256.5,
            "end": 264.5,
            "motion": {"scale": [1.0, 1.05], "focus": [[0.5, 0.5], [0.5, 0.5]], "wobble": "none"},
            "transition_in": {"type": "dissolve", "dur": 0.3},
        },
        {
            "id": "s18_red_flags",
            "image": "factory196/materialAndDraft/EP01b/assets/scene18.jpg",
            "start": 264.5,
            "end": 279.0,
            "motion": {"scale": [1.0, 1.04], "focus": [[0.5, 0.5], [0.5, 0.5]], "wobble": "none"},
            "transition_in": {"type": "fade_black", "dur": 0.4},
        },
        {
            "id": "s19_disclaimer",
            "image": "factory196/materialAndDraft/EP01b/assets/scene18.jpg",
            "start": 279.0,
            "end": 285.0,
            "motion": {"scale": [1.04, 1.0], "focus": [[0.5, 0.5], [0.5, 0.5]], "wobble": "none"},
            "transition_in": {"type": "dissolve", "dur": 0.3},
        },
    ]

    dialogue = [
        # HOOK (0–20s)
        line("l01_na", "na", 1.0, 7.6, "Em chuyển đủ ba trăm triệu cho chị Trang rồi… Sao giờ gọi khóa máy, nhắn tin chặn hết vậy?!"),
        line("l02_chihai", "chi_hai", 9.4, 5.0, "Ba trăm triệu tiền vé của trăm rưỡi người… đều chuyển vô tài khoản em hả Na?!"),
        line("l03_boctran", "boc_tran", 14.7, 5.0, "Không lấy lời một đồng, nhưng chỉ sau một đêm, Na bị cả trăm người tố lừa đảo."),
        # HỒI 1 (20–74s)
        line("l04_boctran", "boc_tran", 22.0, 5.2, "Mọi chuyện bắt đầu từ sáu tháng trước, giữa trưa nắng gắt trước cổng nhà thi đấu."),
        line("l05_tung", "tung", 27.6, 5.1, "Chị Na ơi, nắng gắt quá mà loa kéo hư, quạt cũng hết sạch pin rồi!"),
        line("l06_trang", "trang", 33.4, 7.4, "Chị Trang bên Kênh Hậu Trường nè Na. Đợt trước tặng áo, nay chị mang loa quạt qua phụ tụi em."),
        line("l07_na", "na", 41.2, 6.6, "Trời ơi chị Trang chu đáo quá! Hai đợt liền chị toàn bỏ tiền túi phụ không công, ngại ghê."),
        line("l08_trang", "trang", 48.2, 6.9, "Chỗ chị em quý ca sĩ cả mà, tính toán chi mấy chuyện nhỏ. Cần gì cứ nhắn chị."),
        line("l09_tung", "tung", 55.9, 5.5, "Mới mở bán năm phút đã cháy sạch vé khu sát sân khấu rồi chị Na ơi!"),
        line("l10_trang", "trang", 61.8, 6.0, "Na ơi, bên chị là đối tác truyền thông đêm nhạc nên có suất vé nội bộ giá gốc.", phone=True),
        line("l11_trang", "trang", 68.1, 5.6, "Em đứng ra gom đơn cho nhóm đi, chị giữ riêng suất đẹp cho tụi em.", phone=True),
        # HỒI 2 (74–128s)
        line("l12_tung", "tung", 76.0, 8.0, "Em gom luôn mười vé hai chục triệu cho đám bạn ngoài tỉnh bay vô nha! Tụi nó tin chị Na lắm!", phone=True),
        line("l13_na", "na", 84.4, 8.2, "Yên tâm nha Tùng, đúng giá gốc hai triệu một vé. Tuần sau đối tác xuất mã đoàn là chị gửi liền!"),
        line("l14_chihai", "chi_hai", 93.4, 7.6, "Khoan đã Na. Vé suất của kênh truyền thông, sao lại chuyển ba trăm triệu vô tài khoản cá nhân tên Trang?"),
        line("l15_na", "na", 101.4, 7.6, "Vé nội bộ đâu bán lẻ nên phải chuyển qua người phụ trách chị Hai. Bả giúp nhóm em nửa năm rồi!"),
        line("l16_chihai", "chi_hai", 109.4, 7.7, "Giúp cái quạt khác chuyện cầm ba trăm triệu không giấy tờ! Lỡ bả quỵt, trăm rưỡi người kia chỉ nắm đầu em thôi!"),
        line("l17_na", "na", 118.0, 6.4, "Chị Hai lo xa quá, kênh bả hơn trăm ngàn người theo dõi, ai đi lừa mấy đồng vé."),
        # HỒI 3 (128–186s)
        line("l18_trang", "trang", 133.2, 7.9, "Đối tác đang rà lại danh sách, thứ Tư chị gửi đủ một lượt nha. Đừng gọi giục chị rối.", phone=True),
        line("l19_na", "na", 142.0, 7.8, "Thứ Tư rồi… Sao số điện thoại khóa máy, tin nhắn chị Trang cũng chặn em luôn vậy nè?!"),
        line("l20_tung", "tung", 153.0, 8.2, "Chị Na ơi, Kênh Hậu Trường vừa báo bị mạo danh! Trên mạng đang tố trang chị lừa ba trăm triệu kìa!"),
        line("l21_tung", "tung", 161.6, 8.4, "Mười đứa bạn em đặt vé máy bay hết rồi! Giờ mất vé, tụi nó tưởng em ăn chặn hai chục triệu!"),
        line("l22_na", "na", 173.9, 5.5, "Người ta rủa xả em khắp nơi… Hay em tạm khóa trang lại nha chị Hai?!"),
        line("l23_chihai", "chi_hai", 179.8, 5.8, "Đừng dại! Giờ khóa trang im lặng là người ta tin em ôm tiền trốn thiệt đó!"),
        # HỒI 4 (186–234s)
        line("l24_anhhai", "anh_hai", 191.2, 8.2, "Em bị lợi dụng lòng tin, nhưng tiền trăm rưỡi bạn đều vô tài khoản em nên phải ra mặt đàng hoàng."),
        line("l25_chihai", "chi_hai", 199.8, 8.8, "Giữ nguyên tin nhắn gốc, in sao kê từng khoản nhận và chuyển. Đăng thông báo rõ ràng rồi đi trình báo công an ngay."),
        line("l26_anhhai", "anh_hai", 210.4, 8.2, "Kênh bị mạo danh không mất tiền trực tiếp, nên chính những người chuyển tiền như tụi em phải đi nộp đơn."),
        line("l27_na", "na", 219.0, 7.6, "Hồ sơ được tiếp nhận rồi… Nhưng tiền tiết kiệm hai năm đi làm, em phải rút ra trả dần cho các bạn."),
        line("l28_tung", "tung", 227.0, 6.6, "Em cũng phải gom tiền đền trước cho đám bạn. Chừa tới già chuyện gom đơn truyền miệng."),
        # HỒI 5 (234–285s)
        line("l29_boctran", "boc_tran", 235.0, 6.2, "Kẻ gian không đánh vào lòng tham của Na. Chúng đánh vào sự nhiệt tình và lòng tin người quen."),
        line("l30_boctran", "boc_tran", 242.0, 7.0, "Đầu tiên, chúng bỏ vài triệu tặng quà, mang loa quạt hỗ trợ ngoài đời nhiều tháng để tạo vỏ bọc tử tế."),
        line("l31_boctran", "boc_tran", 249.3, 6.9, "Khi đêm nhạc cháy vé, chúng mượn danh đối tác rao vé nội bộ, hẹn sát ngày xuất mã để gom trọn một cục."),
        line("l32_boctran", "boc_tran", 257.0, 7.0, "Độc hiểm nhất, chúng đẩy trưởng nhóm đứng ra gom tiền, biến người nhiệt tình thành tấm bia hứng trọn trách nhiệm."),
    ]

    cfg = {
        "episode_id": "EP04",
        "slug": "BayVeNoiBo300Trieu",
        "title": "Bẫy vé nội bộ – 300 triệu gom hộ và người đứng mũi chịu sào",
        "version": "v1-draft",
        "scam_family": "MIX-06",
        "duration_sec": duration,
        "visual_style_lock": (
            "Horizontal 16:9 widescreen (1920x1080), semi-realistic cinematic 2D anime illustration, "
            "contemporary Southern Vietnam urban setting, moody dramatic lighting, clean bottom 15% for subtitles, "
            "no text, no letters, no numbers, no logos, no real uniforms"
        ),
        "hook": {
            "kicker": "23 GIỜ 15 · BA NGÀY TRƯỚC ĐÊM DIỄN",
            "title": "GOM GIÙM TRĂM RƯỠI VÉ – CÔ TRƯỞNG NHÓM THÀNH BỊ CÁO",
            "start": 0.4,
            "end": 5.4,
        },
        "chapters": [
            {
                "kicker": "HỒI 1 · SÁU THÁNG TRƯỚC",
                "title": "MÓN QUÀ MIỄN PHÍ TỪ “ĐỐI TÁC TRUYỀN THÔNG”",
                "start": 20.2,
                "end": 24.8,
            },
            {
                "kicker": "HỒI 2 · MƯỜI NGÀY TRƯỚC ĐÊM DIỄN",
                "title": "TRĂM RƯỠI VÉ CHẢY QUA TÀI KHOẢN CÁ NHÂN",
                "start": 74.2,
                "end": 78.8,
            },
            {
                "kicker": "HỒI 3 · BA NGÀY TRƯỚC ĐÊM DIỄN",
                "title": "KHÓA MÁY, CHẶN TIN & CƠN BÃO ĐẤU TỐ",
                "start": 128.2,
                "end": 132.8,
            },
            {
                "kicker": "HỒI 4 · SÁNG HÔM SAU",
                "title": "ĐỨNG MŨI CHỊU SÀO & HỒ SƠ TRÌNH BÁO",
                "start": 186.2,
                "end": 190.8,
            },
            {
                "kicker": "HỒI 5 · BÓC TRẦN CƠ CHẾ",
                "title": "THẢ CON TÉP NGOÀI ĐỜI, BẮT CON TÔM TRĂM TRIỆU",
                "start": 234.2,
                "end": 238.8,
            },
        ],
        "scenes": scenes,
        "dialogue": dialogue,
        "chat_bubbles": [
            {
                "sender": "NHÓM FAN ÁNH SAO",
                "text": "Thứ Bảy diễn rồi vé đâu admin ơi?! Định ôm ba trăm triệu trốn hả?!",
                "side": "left",
                "y": 240,
                "stamp": "99+ TIN MỚI",
                "start": 5.8,
                "end": 8.8,
            },
            {
                "sender": "CHỊ TRANG",
                "text": "Chốt tiền tối nay kẻo ban tổ chức thu hồi suất nha Na.",
                "side": "left",
                "y": 220,
                "stamp": "GẤP",
                "start": 117.9,
                "end": 124.2,
            },
            {
                "sender": "NGÂN HÀNG X",
                "text": "TK …4512: −300.000.000 VND (Chuyển khoản thành công)",
                "side": "right",
                "y": 420,
                "stamp": "21:42",
                "start": 124.6,
                "end": 127.7,
            },
        ],
        "callouts": [
            {
                "text": "CÒN 3 NGÀY TRƯỚC ĐÊM DIỄN: KHÓA MÁY · CHẶN TIN NHẮN",
                "style": "danger",
                "y": 135,
                "start": 142.0,
                "end": 151.8,
            },
            {
                "text": "KÊNH HẬU TRƯỜNG ĐÍNH CHÍNH: BỊ CÁ NHÂN MẠO DANH GIAO DỊCH VÉ TRÁI PHÉP",
                "style": "warn",
                "y": 135,
                "start": 153.0,
                "end": 162.5,
            },
            {
                "text": "1. NUÔI TIN NGOÀI ĐỜI   →   2. MƯỢN DANH ĐỐI TÁC   →   3. HẸN SÁT NGÀY XUẤT MÃ",
                "style": "warn",
                "y": 135,
                "start": 242.0,
                "end": 256.0,
            },
            {
                "text": "NHẬN TIỀN QUA TÀI KHOẢN CÁ NHÂN = TỰ ĐỨNG MŨI CHỊU SÀO VỀ UY TÍN & DÂN SỰ",
                "style": "danger",
                "y": 135,
                "start": 257.0,
                "end": 264.1,
            },
        ],
        "red_flags": {
            "title": "NHỚ KỸ – 4 DẤU HIỆU BẪY GOM VÉ NỘI BỘ",
            "start": 264.8,
            "end": 279.0,
            "stagger_sec": 1.2,
            "items": [
                "Rao \"vé nội bộ, suất đối tác\" số lượng lớn ngay khi kênh chính thức vừa hết vé",
                "Mượn danh kênh truyền thông, công ty nhưng bảo chuyển vào tài khoản cá nhân",
                "Hứa \"sát ngày diễn mới xuất mã đoàn\" rồi liên tục viện cớ dời lịch giao",
                "Nhờ trưởng nhóm fan hoặc bạn bè đứng ra gom tiền hộ để thu một cục lớn",
            ],
            "action": "Chỉ mua trên kênh chính thức · Không lấy tài khoản cá nhân gom tiền hộ nguồn truyền miệng · Mất tiền: giữ sao kê, tin nhắn, trình báo công an ngay!",
        },
        "disclaimer": {
            "header": "LƯU Ý",
            "start": 279.0,
            "end": 285.0,
            "lines": [
                "Tình huống trong phim được dựng lại nhằm cảnh báo cộng đồng; nhân vật, đêm nhạc, trang cộng đồng và số liệu đều là hư cấu.",
                "Chỉ giao dịch vé qua kênh phân phối chính thức của ban tổ chức; không chuyển khoản lớn cho nguồn vé truyền miệng.",
            ],
        },
        "audio": {
            "ambience": [
                {"preset": "night_room", "start": 0.0, "end": 20.0, "gain_db": -1.5},
                {"preset": "crowd", "start": 20.0, "end": 55.5, "gain_db": -3.5},
                {"preset": "room_tone", "start": 55.5, "end": 128.0, "gain_db": -2.0},
                {"preset": "night_room", "start": 128.0, "end": 152.5, "gain_db": -1.5},
                {"preset": "street", "start": 152.5, "end": 173.5, "gain_db": -2.5},
                {"preset": "night_room", "start": 173.5, "end": 186.0, "gain_db": -1.5},
                {"preset": "room_tone", "start": 186.0, "end": 210.0, "gain_db": -2.5},
                {"preset": "street", "start": 210.0, "end": 234.0, "gain_db": -3.5},
                {"preset": "room_tone", "start": 234.0, "end": 285.0, "gain_db": -3.5},
            ],
            "foley": [
                {"preset": "phone_vibrate", "at": 0.35, "dur": 1.6, "gain_db": -3.0},
                {"preset": "notification", "at": 5.8, "gain_db": -4.0},
                {"preset": "impact", "at": 9.0, "gain_db": -3.5},
                {"preset": "riser", "at": 13.4, "dur": 1.2, "gain_db": -4.5},
                {"preset": "chapter_sting", "at": 20.25, "gain_db": -4.0},
                {"preset": "phone_ring", "at": 60.4, "dur": 1.2, "gain_db": -4.5},
                {"preset": "chapter_sting", "at": 74.25, "gain_db": -4.0},
                {"preset": "notification", "at": 75.3, "gain_db": -5.0},
                {"preset": "notification", "at": 117.85, "gain_db": -4.0},
                {"preset": "bank_ting", "at": 124.6, "gain_db": -3.0},
                {"preset": "chapter_sting", "at": 128.25, "gain_db": -4.0},
                {"preset": "call_end", "at": 141.65, "gain_db": -3.0},
                {"preset": "impact", "at": 141.8, "gain_db": -3.0},
                {"preset": "heartbeat", "at": 142.2, "dur": 9.5, "gain_db": -5.0},
                {"preset": "riser", "at": 172.2, "dur": 1.2, "gain_db": -4.5},
                {"preset": "impact", "at": 179.55, "gain_db": -3.0},
                {"preset": "chapter_sting", "at": 186.25, "gain_db": -4.0},
                {"preset": "typing", "at": 188.5, "dur": 2.0, "gain_db": -6.0},
                {"preset": "chapter_sting", "at": 234.25, "gain_db": -4.0},
                {"preset": "glitch", "at": 234.1, "gain_db": -4.0},
                {"preset": "bank_ting", "at": 264.8, "gain_db": -4.0},
            ],
            "bgm": [
                {"preset": "suspense_pulse", "start": 0.0, "end": 20.0, "gain_db": -1.0},
                {"preset": "investigative_story", "start": 20.0, "end": 93.0, "gain_db": -1.5},
                {"preset": "suspense_pulse", "start": 93.0, "end": 141.5, "gain_db": -1.5},
                {"preset": "tension_drone", "start": 141.5, "end": 173.5, "gain_db": -0.5},
                {"preset": "action_climax", "start": 173.5, "end": 186.0, "gain_db": 0.5},
                {"preset": "investigative_story", "start": 186.0, "end": 264.5, "gain_db": -1.5},
                {"preset": "warm_outro", "start": 264.5, "end": 285.0, "gain_db": -2.0},
            ],
            "duck_extra": [
                {"start": 141.5, "end": 143.2, "bgm_db": -14, "amb_db": -10},
                {"start": 279.0, "end": 284.9},
            ],
        },
        "forbidden_terms": [],
        "publish": {
            "titles": [
                "Bẫy \"Vé Nội Bộ\": Gom Hộ 300 Triệu, Trưởng Nhóm Fan Thành Bị Cáo Bất Đắc Dĩ | Bóc Trần Lừa Đảo",
                "Nuôi Lòng Tin 6 Tháng Để Ôm 300 Triệu Tiền Vé: Cái Giá Đắt Của Việc \"Gom Đơn Hộ\" | Bóc Trần Lừa Đảo",
                "300 Triệu Tiền Vé Bốc Hơi Trước Giờ Diễn – Vì Sao Người Gom Hộ Đứng Mũi Chịu Sào? | Bóc Trần Lừa Đảo",
            ],
            "description": (
                "Na, 23 tuổi – trưởng một nhóm cộng đồng người hâm mộ – không ăn chênh lệch một đồng khi đứng ra "
                "gom giúp 150 vé đêm nhạc qua lời giới thiệu \"suất vé nội bộ đối tác truyền thông\" của người chị quen biết "
                "từng mang loa, quạt hỗ trợ nhóm suốt nửa năm. Ba ngày trước giờ diễn, nguồn vé khóa máy chặn liên lạc, "
                "kênh truyền thông lên tiếng báo bị mạo danh, còn Na trở thành tâm điểm bị cả trăm người mua réo tên đòi 300 triệu.\n\n"
                "⏱️ Các hồi trong phim:\n"
                "00:00 Mở đầu – Gom giùm trăm rưỡi vé, cô trưởng nhóm thành bị cáo\n"
                "00:20 Hồi 1 – Sáu tháng trước: Món quà miễn phí từ \"đối tác truyền thông\"\n"
                "01:14 Hồi 2 – Điểm mù khi chuyển 300 triệu vào tài khoản cá nhân\n"
                "02:08 Hồi 3 – Ba ngày trước đêm diễn: Khóa máy, đính chính & bão đấu tố\n"
                "03:06 Hồi 4 – Đứng mũi chịu sào & quy trình trình báo công an\n"
                "03:54 Hồi 5 – Bóc trần 3 mắt xích bẫy \"vé nội bộ\" & 4 dấu hiệu nhận biết"
            ),
            "pinned_comment": (
                "📌 Cảnh báo mùa sự kiện & đêm nhạc: Không có \"suất vé nội bộ công ty\" nào lại thu hàng trăm triệu "
                "qua tài khoản cá nhân không hợp đồng. Đặc biệt, các bạn trưởng nhóm fan, lớp trưởng hay bạn bè nhiệt tình "
                "tuyệt đối đừng dùng tài khoản cá nhân đứng ra gom tiền hộ cho nguồn vé truyền miệng — khi kẻ gian cắt liên lạc, "
                "chính người gom hộ sẽ phải gánh khủng hoảng uy tín và trách nhiệm trực tiếp với người mua! "
                "(Chia sẻ kinh nghiệm cảnh giác bên dưới nhưng lưu ý không đăng tên thật, SĐT hay số tài khoản cá nhân nhé)."
            ),
            "hashtags": [
                "#bóctrầnlừađảo",
                "#cảnhgiáclừađảo",
                "#vạnchuyện",
                "#lừađảovéconcert",
                "#vénộibộ",
            ],
            "tags": [
                "lừa đảo vé đêm nhạc",
                "bẫy vé nội bộ",
                "gom đơn hộ",
                "mạo danh đối tác truyền thông",
                "bóc trần lừa đảo",
                "cảnh giác lừa đảo",
                "vạn chuyện",
            ],
            "category": "Education (Giáo dục)",
            "playlist": "Hồ Sơ Bóc Trần Lừa Đảo – Phim Dài Chuyên Sâu",
            "thumbnail_sec": 175.0,
        },
    }
    return cfg


def audit_draft(cfg: dict) -> None:
    save_json(EP_DIR / "episode.json", cfg)
    ep = Episode("EP04", "196")

    # 1. Word count & per-line limit check (target <= 26 words/line, 120-140 wpm)
    max_line = 0
    total_words = 0
    over_26 = []
    for ln in cfg["dialogue"]:
        w = len(ln["text"].split())
        total_words += w
        max_line = max(max_line, w)
        if w > 26:
            over_26.append((ln["id"], w, ln["text"]))
    wpm = total_words / (cfg["duration_sec"] / 60.0)
    print(f"[THỐNG KÊ THOẠI] {len(cfg['dialogue'])} câu | {total_words} từ | max {max_line} từ/câu | mật độ {wpm:.1f} từ/phút")
    if over_26:
        raise SystemExit(f"Có câu vượt 26 từ: {over_26}")

    # 2. Scene cut before voice (>= 0.25s) & non-overlapping dialogue windows
    scenes = cfg["scenes"]
    for i, ln in enumerate(cfg["dialogue"]):
        st, end = ln["start"], ln["start"] + ln["window"]
        if i + 1 < len(cfg["dialogue"]):
            nxt = cfg["dialogue"][i + 1]["start"]
            if end > nxt + 1e-6:
                raise SystemExit(f"Chồng cửa sổ thoại: {ln['id']} kết thúc {end} > {cfg['dialogue'][i+1]['id']} bắt đầu {nxt}")
        # Find scene active at ln["start"]
        sc = next((s for s in scenes if s["start"] <= st < s["end"]), None)
        if not sc:
            raise SystemExit(f"Câu {ln['id']} tại {st}s không nằm trong cảnh nào")
        if sc["start"] > 0 and (st - sc["start"]) < 0.25:
            # Check if previous line wasn't already in this scene
            prev_in_same = i > 0 and scenes and (sc["start"] <= cfg["dialogue"][i - 1]["start"] < sc["end"])
            if not prev_in_same:
                raise SystemExit(f"Câu {ln['id']} vào quá sát đầu cảnh {sc['id']} ({st - sc['start']:.2f}s < 0.25s)")

    # 3. Gate 5 text & policy wordlist scan across spoken + on_screen + metadata
    chunks = [ln["text"] for ln in cfg["dialogue"]]
    chunks += [b["text"] + " " + b.get("sender", "") for b in cfg["chat_bubbles"]]
    chunks += [c["text"] for c in cfg["callouts"]]
    chunks += [cfg["hook"]["kicker"], cfg["hook"]["title"]]
    chunks += [ch["kicker"] + " " + ch["title"] for ch in cfg["chapters"]]
    chunks += cfg["red_flags"]["items"] + [cfg["red_flags"]["title"], cfg["red_flags"]["action"]]
    chunks += cfg["disclaimer"]["lines"]
    pub = cfg["publish"]
    chunks += pub["titles"] + [pub["description"], pub["pinned_comment"]] + pub["hashtags"] + pub["tags"]
    all_text = "\n".join(chunks).lower()

    pol = ep.policy
    id_hard = [t for t in pol.get("identity_hard_block", []) if _contains(all_text, t)]
    id_soft = [t for t in pol.get("identity_soft_warn", []) if _contains(all_text, t)]
    asr_hard = [t for t in pol.get("asr_ocr_hard_block", []) if _contains(all_text, t)]
    asr_soft = [t for t in pol.get("asr_ocr_soft_warn", []) if _contains(all_text, t)]
    phones = PHONE_RE.findall(all_text)
    urls = URL_RE.findall(all_text)
    accts = [a for a in ACCOUNT_RE.findall(all_text) if not PHONE_RE.fullmatch(a)]

    # Also ensure zero real-case names leaked anywhere
    real_case_terms = ["chông gai", "cây bàng non", "duy nhất", "dustin", "dotg", "hưng yên", "144"]
    leaked = [t for t in real_case_terms if t in all_text]

    print(f"[QUÉT TỪ KHÓA GATE 5] id_hard={id_hard} | id_soft={id_soft} | asr_hard={asr_hard} | asr_soft={asr_soft}")
    print(f"[QUÉT REGEX & ẨN DANH] phones={phones} | urls={urls} | accts={accts} | real_case_leaks={leaked}")
    if any([id_hard, id_soft, asr_hard, asr_soft, phones, urls, accts, leaked]):
        raise SystemExit("Phát hiện vi phạm từ khóa hoặc định danh!")

    # 4. Run Gate 0 check (expect ONLY missing assets/c01..c16.jpg)
    errs = gate0(ep)
    non_asset_errs = [e for e in errs if not e.startswith("Thiếu ảnh/video assets/c")]
    print(f"[KIỂM TRA GATE 0] Tổng lỗi hiện tại: {len(errs)} (trong đó lỗi ngoài ảnh chưa sinh: {len(non_asset_errs)})")
    if non_asset_errs:
        raise SystemExit(f"Lỗi cấu trúc Gate 0: {non_asset_errs}")
    print("=> BẢN NHÁP EP04 ĐẠT 100% CHUẨN KỊCH BẢN, CẤU TRÚC, TỪ KHÓA & PHÁP LÝ! (Chỉ chờ sinh 16 ảnh assets/c01..c16.jpg).")


if __name__ == "__main__":
     audit_draft(build())
