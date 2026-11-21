# -*- coding: utf-8 -*-
"""
Shared GATE 4 Service (`03_ENGINE/gate4_timeline.py`) – Dựng timeline, chuyển động camera,
đồ họa chữ trong Safe Zone dùng chung cho cả hai nhà máy:
  * `factory619` (9:16 dọc – 1080x1920)
  * `factory196` (16:9 ngang – 1920x1080, hỗ trợ thêm thẻ chuyển hồi `chapters`)

Tự động thích ứng tọa độ, kích thước chữ, độ rộng hộp thoại theo `cv.is_landscape` và `channel_config.json`,
đồng thời áp dụng ghép lớp cục bộ theo bounding-box (`_paste_rgba_crop`) giúp tăng tốc độ render cho cả 2 nhà máy.
"""
from __future__ import annotations

import math
import re
import subprocess
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from core import FFMPEG, Episode, GateError, load_json, rel, save_json
from motion_fx import (
    HARDWARE_PROFILE,
    apply_post_camera_fx,
    apply_pre_camera_fx,
    audit_episode_motion,
    collect_fx_qa_timestamps,
    ease_u,
    fit_aspect_crop,
    prepare_detail_fx,
    prepare_parallax,
    render_parallax_frame,
    resolve_motion_params,
    unload_scene_runtime,
)

# ----------------------------------------------------------------------------
# Fonts & text helpers
# ----------------------------------------------------------------------------
_FONT_CACHE: dict = {}


def font(size: int, bold: bool = True) -> ImageFont.FreeTypeFont:
    key = (size, bold)
    if key in _FONT_CACHE:
        return _FONT_CACHE[key]
    cands = (
        [
            r"C:\Windows\Fonts\segoeuib.ttf",
            r"C:\Windows\Fonts\arialbd.ttf",
            r"C:\Windows\Fonts\tahomabd.ttf",
            "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
            "/System/Library/Fonts/Supplemental/Tahoma Bold.ttf",
        ]
        if bold
        else [
            r"C:\Windows\Fonts\segoeui.ttf",
            r"C:\Windows\Fonts\arial.ttf",
            r"C:\Windows\Fonts\tahoma.ttf",
            "/System/Library/Fonts/Supplemental/Arial.ttf",
            "/System/Library/Fonts/Supplemental/Tahoma.ttf",
        ]
    )
    f = None
    for c in cands:
        if Path(c).is_file():
            f = ImageFont.truetype(c, size=size)
            break
    _FONT_CACHE[key] = f or ImageFont.load_default()
    return _FONT_CACHE[key]


def text_w(draw: ImageDraw.ImageDraw, s: str, f, stroke: int = 0) -> int:
    b = draw.textbbox((0, 0), s, font=f, stroke_width=stroke)
    return b[2] - b[0]


def wrap(draw: ImageDraw.ImageDraw, s: str, f, max_w: int, stroke: int = 0) -> list[str]:
    words, lines, cur = s.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if text_w(draw, trial, f, stroke) <= max_w or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def smoothstep(u: float) -> float:
    u = max(0.0, min(1.0, u))
    return u * u * (3.0 - 2.0 * u)


class Canvas:
    def __init__(self, ep: Episode):
        self.W, self.H = ep.width, ep.height
        self.is_landscape = ep.is_landscape
        s = ep.safe
        self.L, self.R, self.MAXY, self.TOPY = s["left_x"], s["right_x"], s["max_y"], s["top_hook_y"]
        self.UIBOT = s.get("platform_ui_bottom_y", self.MAXY)
        self.pal = ep.channel["palette"]
        self.ch = ep.channel["channel"]
        self.fmt = ep.channel["format"]

    def blank(self) -> Image.Image:
        return Image.new("RGBA", (self.W, self.H), (0, 0, 0, 0))

    def compliant(self, x0, y0, x1, y1) -> bool:
        return x0 >= self.L and x1 <= self.R and y1 <= self.MAXY and y0 >= 0


# ----------------------------------------------------------------------------
# Overlay plate renderers (Adaptive 9:16 & 16:9)
# ----------------------------------------------------------------------------

def plate_branding(cv: Canvas) -> tuple[Image.Image, dict]:
    img = cv.blank()
    d = ImageDraw.Draw(img)
    base = min(cv.W, cv.H)
    badge_h = max(24, round(base * (0.034 if cv.is_landscape else 0.032)))
    lf = font(max(14, round(badge_h * 0.62)))
    lt = cv.ch["logo_text"]
    lb = d.textbbox((0, 0), lt, font=lf)
    tw, th = lb[2] - lb[0], lb[3] - lb[1]
    pad = round(badge_h * 0.45)
    bw = tw + pad * 2
    mx = 48 if cv.is_landscape else round(base * 0.028)
    my = 34 if cv.is_landscape else mx
    d.rounded_rectangle((mx, my, mx + bw, my + badge_h), radius=max(4, round(badge_h * 0.22)),
                        fill=(*cv.ch["logo_color_rgb"], round(255 * cv.ch["logo_opacity"])))
    d.text((mx + (bw - tw) / 2 - lb[0], my + (badge_h - th) / 2 - lb[1]), lt, font=lf, fill=(255, 255, 255, 255))
    sf = font(max(12, round(badge_h * 0.50)))
    d.text((mx + bw + 12, my + badge_h / 2), cv.ch.get("series_name", ""), font=sf, anchor="lm",
           fill=(255, 255, 255, 200), stroke_width=2, stroke_fill=(0, 0, 0, 160))
    wt = cv.ch["watermark_text"]
    wf = font(max(16, round(base * 0.024)))
    wb = d.textbbox((0, 0), wt, font=wf)
    wx = cv.W - (wb[2] - wb[0]) - (54 if cv.is_landscape else int(base * 0.06))
    wy = (cv.MAXY - 38) if cv.is_landscape else int(cv.H * 0.742)
    a = cv.ch["watermark_opacity"]
    d.text((wx + 2, wy + 2), wt, font=wf, fill=(0, 0, 0, round(255 * a * 0.65)))
    d.text((wx, wy), wt, font=wf, fill=(255, 255, 255, round(255 * a)))
    return img, {"type": "channel_branding", "logo_text": lt, "watermark_text": wt, "safe_zone_compliant": True}


def plate_hook(cv: Canvas, title: str, kicker: str = "") -> tuple[Image.Image, dict]:
    img = cv.blank()
    d = ImageDraw.Draw(img)
    fm = font(42 if cv.is_landscape else 46)
    fk = font(22 if cv.is_landscape else 24)
    max_w = min(cv.R - cv.L - 60, 1360 if cv.is_landscape else (cv.R - cv.L - 60))
    lines = wrap(d, title, fm, max_w, 4)
    lh = 52 if cv.is_landscape else 56
    box_h = 26 + (38 if kicker else 0) + lh * len(lines) + 14
    box_w = min(cv.R - cv.L, max([text_w(d, ln, fm, 4) for ln in lines] + [text_w(d, kicker, fk, 2)]) + 60)
    cx = (cv.L + cv.R) // 2
    x0, y0 = max(cv.L, cx - box_w // 2), cv.TOPY
    x1, y1 = min(cv.R, x0 + box_w), cv.TOPY + box_h
    danger = tuple(cv.pal["danger_rgb"])
    d.rounded_rectangle([x0, y0, x1, y1], radius=16, fill=(10, 12, 18, 130), outline=(*danger, 210), width=3)
    y = y0 + 16
    if kicker:
        kw = text_w(d, kicker, fk, 0) + 26
        d.rounded_rectangle([cx - kw // 2, y - 2, cx + kw // 2, y + 32], radius=8, fill=(*danger, 230))
        d.text((cx, y + 15), kicker, font=fk, anchor="mm", fill=(255, 255, 255, 255))
        y += 42
    for ln in lines:
        d.text((cx, y + lh // 2 - 4), ln, font=fm, anchor="mm", fill=(255, 255, 255, 255), stroke_width=4, stroke_fill=(0, 0, 0, 255))
        y += lh
    return img, {"type": "text_hook", "text": f"{kicker} — {title}".strip(" —"), "bbox_px": [x0, y0, x1, y1],
                 "safe_zone_compliant": cv.compliant(x0, y0, x1, y1)}


def plate_chapter(cv: Canvas, title: str, kicker: str = "") -> tuple[Image.Image, dict]:
    """Thẻ chuyển Hồi / Chương (Chapter Card) cho phim dài."""
    img = cv.blank()
    d = ImageDraw.Draw(img)
    fm, fk = font(36), font(20)
    max_w = min(cv.R - cv.L - 80, 1200)
    lines = wrap(d, title, fm, max_w, 3)
    lh = 46
    box_h = 22 + (32 if kicker else 0) + lh * len(lines) + 12
    box_w = min(cv.R - cv.L, max([text_w(d, ln, fm, 3) for ln in lines] + [text_w(d, kicker, fk, 2)]) + 64)
    cx = (cv.L + cv.R) // 2
    x0, y0 = max(cv.L, cx - box_w // 2), cv.TOPY
    x1, y1 = min(cv.R, x0 + box_w), cv.TOPY + box_h
    acc = tuple(cv.pal["accent_rgb"])
    d.rounded_rectangle([x0, y0, x1, y1], radius=14, fill=(10, 14, 22, 155), outline=(*acc, 210), width=2)
    y = y0 + 12
    if kicker:
        kw = text_w(d, kicker, fk, 0) + 24
        d.rounded_rectangle([cx - kw // 2, y - 1, cx + kw // 2, y + 27], radius=6, fill=(*acc, 235))
        d.text((cx, y + 13), kicker, font=fk, anchor="mm", fill=(15, 18, 24, 255))
        y += 34
    for ln in lines:
        d.text((cx, y + lh // 2 - 3), ln, font=fm, anchor="mm", fill=(255, 255, 255, 255), stroke_width=3, stroke_fill=(0, 0, 0, 240))
        y += lh
    return img, {"type": "chapter_card", "text": f"{kicker} — {title}".strip(" —"), "bbox_px": [x0, y0, x1, y1],
                 "safe_zone_compliant": cv.compliant(x0, y0, x1, y1)}


def plate_subtitle(cv: Canvas, text: str, color: tuple, speaker_label: str = "") -> tuple[Image.Image, dict]:
    """Phụ đề điện ảnh thuần túy (boxless outline): chữ có bóng đổ & viền đen sắc nét ở cạnh dưới Safe Zone."""
    img = cv.blank()
    d = ImageDraw.Draw(img)
    f = font(40 if cv.is_landscape else 44)
    max_w = min(cv.R - cv.L - 40, 1440 if cv.is_landscape else (cv.R - cv.L - 40))
    lines = wrap(d, text, f, max_w, 5)
    lh = 52 if cv.is_landscape else 56
    box_h = lh * len(lines)
    box_w = min(cv.R - cv.L, max(text_w(d, ln, f, 5) for ln in lines) + 24)
    cx = (cv.L + cv.R) // 2
    x0 = max(cv.L, cx - box_w // 2)
    x1 = min(cv.R, x0 + box_w)
    y1 = (cv.MAXY - 22) if cv.is_landscape else 1380
    y0 = y1 - box_h
    y = y0
    for ln in lines:
        cy = y + lh // 2
        d.text((cx + 3, cy + 4), ln, font=f, anchor="mm", fill=(0, 0, 0, 180), stroke_width=6, stroke_fill=(0, 0, 0, 180))
        d.text((cx, cy), ln, font=f, anchor="mm", fill=(*color, 255), stroke_width=5, stroke_fill=(0, 0, 0, 255))
        y += lh
    return img, {"type": "subtitle", "lines": lines, "bbox_px": [x0, y0, x1, y1],
                 "safe_zone_compliant": cv.compliant(x0, y0, x1, y1)}


def plate_chat(cv: Canvas, text: str, side: str = "left", sender: str = "", y_top: int | None = None,
               stamp: str = "") -> tuple[Image.Image, dict]:
    """Bong bóng tin nhắn trung tính (không logo, không giao diện app thật)."""
    img = cv.blank()
    d = ImageDraw.Draw(img)
    f = font(32 if cv.is_landscape else 38, bold=False)
    fs = font(24 if cv.is_landscape else 26)
    max_w = min(720, int((cv.R - cv.L) * 0.48)) if cv.is_landscape else int((cv.R - cv.L) * 0.78)
    lines = wrap(d, text, f, max_w - 56)
    lh = 44 if cv.is_landscape else 50
    bw = max([text_w(d, ln, f) for ln in lines] + ([text_w(d, sender, fs)] if sender else [0])) + 56
    bh = lh * len(lines) + 34 + (34 if sender else 0)
    margin_in = 60 if cv.is_landscape else 0
    if side == "right":
        x1 = cv.R - margin_in
        x0 = x1 - bw
        fill, txt = (0, 132, 255, 240), (255, 255, 255, 255)
    else:
        x0 = cv.L + margin_in
        x1 = x0 + bw
        fill, txt = (245, 245, 247, 245), (20, 20, 24, 255)
    default_y = 220 if cv.is_landscape else 520
    y0 = max(cv.TOPY, min(cv.MAXY - bh - 34, int(y_top if y_top is not None else default_y)))
    y1 = y0 + bh
    d.rounded_rectangle([x0 + 4, y0 + 6, x1 + 4, y1 + 6], radius=26, fill=(0, 0, 0, 90))
    d.rounded_rectangle([x0, y0, x1, y1], radius=26, fill=fill)
    y = y0 + 17
    if sender:
        d.text((x0 + 28, y + 12), sender, font=fs, anchor="lm",
               fill=(230, 40, 45, 255) if side == "left" else (220, 235, 255, 255))
        y += 34
    for ln in lines:
        d.text((x0 + 28, y + lh // 2), ln, font=f, anchor="lm", fill=txt)
        y += lh
    if stamp:
        d.text((x1 - 16, y1 + 18), stamp, font=font(20 if cv.is_landscape else 22, bold=False), anchor="rm",
               fill=(255, 255, 255, 210), stroke_width=2, stroke_fill=(0, 0, 0, 200))
    return img, {"type": "chat_bubble", "text": text, "sender": sender, "bbox_px": [x0, y0, x1 + 4, y1 + 30],
                 "safe_zone_compliant": cv.compliant(x0, y0, x1 + 4, y1 + 30)}


def plate_notification(cv: Canvas, title: str, text: str, stamp: str = "vừa xong",
                       y_top: int | None = None, style: str = "neutral") -> tuple[Image.Image, dict]:
    """Thanh thông báo điện thoại trung tính (Level C detail motion – không logo, không UI app thật)."""
    img = cv.blank()
    d = ImageDraw.Draw(img)
    ft = font(24 if cv.is_landscape else 27)
    fb = font(27 if cv.is_landscape else 31, bold=False)
    fs = font(20 if cv.is_landscape else 22, bold=False)
    card_w = min(760, int((cv.R - cv.L) * 0.56)) if cv.is_landscape else min(cv.R - cv.L - 12, 820)
    inner_w = card_w - 116
    lines = wrap(d, text, fb, inner_w)
    lh = 35 if cv.is_landscape else 40
    bh = 26 + 34 + lh * len(lines) + 14
    cx = (cv.L + cv.R) // 2
    x0 = max(cv.L, cx - card_w // 2)
    x1 = min(cv.R, x0 + card_w)
    default_y = (cv.TOPY + 10) if cv.is_landscape else (cv.TOPY + 20)
    y0 = max(cv.TOPY, min(cv.MAXY - bh - 12, int(y_top if y_top is not None else default_y)))
    y1 = y0 + bh

    accent = (
        tuple(cv.pal["danger_rgb"]) if style == "danger"
        else tuple(cv.pal["safe_rgb"]) if style == "safe"
        else tuple(cv.pal["accent_rgb"])
    )
    d.rounded_rectangle([x0 + 4, y0 + 6, x1 + 4, y1 + 6], radius=22, fill=(0, 0, 0, 105))
    d.rounded_rectangle([x0, y0, x1, y1], radius=22, fill=(22, 26, 36, 232), outline=(*accent, 210), width=2)
    # Neutral indicator badge (no brand icon)
    icx, icy = x0 + 44, (y0 + y1) // 2
    d.ellipse([icx - 20, icy - 20, icx + 20, icy + 20], fill=(*accent, 235))
    d.ellipse([icx - 7, icy - 7, icx + 7, icy + 7], fill=(255, 255, 255, 245))

    tx = x0 + 82
    d.text((tx, y0 + 28), title or "Thông báo mới", font=ft, anchor="lm", fill=(255, 255, 255, 255))
    if stamp:
        d.text((x1 - 24, y0 + 28), stamp, font=fs, anchor="rm", fill=(195, 205, 220, 225))
    y = y0 + 54
    for ln in lines:
        d.text((tx, y + lh // 2), ln, font=fb, anchor="lm", fill=(235, 240, 248, 250))
        y += lh
    return img, {"type": "notification", "title": title, "text": text, "bbox_px": [x0, y0, x1 + 4, y1 + 6],
                 "safe_zone_compliant": cv.compliant(x0, y0, x1 + 4, y1 + 6)}


def _warn_icon(d: ImageDraw.ImageDraw, cx: int, cy: int, r: int, color) -> None:
    d.polygon([(cx, cy - r), (cx + r, cy + int(r * 0.8)), (cx - r, cy + int(r * 0.8))], fill=color)
    d.text((cx, cy + int(r * 0.15)), "!", font=font(int(r * 1.1)), anchor="mm", fill=(20, 20, 20, 255))


def plate_callout(cv: Canvas, text: str, style: str = "danger", y_center: int | None = None,
                  size: str = "normal", kicker: str = "") -> tuple[Image.Image, dict]:
    """Tag ghi chú ở mép trên; hỗ trợ size='large' + kicker để nhấn mạnh cao trào."""
    img = cv.blank()
    d = ImageDraw.Draw(img)
    color = {"danger": cv.pal["danger_rgb"], "safe": cv.pal["safe_rgb"], "info": cv.pal["accent_rgb"], "warn": cv.pal["accent_rgb"]}.get(style, cv.pal["danger_rgb"])
    if size == "large":
        f = font(42 if cv.is_landscape else 46)
        fk = font(22 if cv.is_landscape else 25)
        max_w = min(cv.R - cv.L - 56, 1340 if cv.is_landscape else (cv.R - cv.L - 56))
        lines = wrap(d, text, f, max_w, 4)
        lh = 52 if cv.is_landscape else 58
        kh = 46 if kicker else 0
        bh = 28 + kh + lh * len(lines) + 18
        text_max_w = max([text_w(d, ln, f, 4) for ln in lines] + ([text_w(d, kicker, fk, 2) + 36] if kicker else [0]))
        bw = min(cv.R - cv.L, text_max_w + 60)
        cx = (cv.L + cv.R) // 2
        x0 = max(cv.L, cx - bw // 2)
        x1 = min(cv.R, x0 + bw)
        yc = int(y_center if y_center is not None else (210 if cv.is_landscape else 320))
        min_y = cv.TOPY if cv.is_landscape else 155
        y0 = max(min_y, min(cv.MAXY - bh, yc - bh // 2))
        y1 = y0 + bh
        d.rounded_rectangle([x0, y0, x1, y1], radius=18, fill=(12, 14, 22, 195), outline=(*color, 245), width=4)
        y = y0 + 18
        if kicker:
            kw = text_w(d, kicker, fk, 0) + 34
            d.rounded_rectangle([cx - kw // 2, y - 2, cx + kw // 2, y + 36], radius=10, fill=(*color, 245))
            k_fill = (18, 18, 22, 255) if style in ("warn", "info") else (255, 255, 255, 255)
            d.text((cx, y + 17), kicker, font=fk, anchor="mm", fill=k_fill)
            y += kh
        txt_fill = (255, 232, 110, 255) if style == "warn" else (255, 255, 255, 255)
        for ln in lines:
            d.text((cx, y + lh // 2 - 4), ln, font=f, anchor="mm", fill=txt_fill, stroke_width=4, stroke_fill=(0, 0, 0, 255))
            y += lh
        return img, {"type": "callout", "style": style, "text": f"{kicker} — {text}".strip(" —"), "bbox_px": [x0, y0, x1, y1],
                     "safe_zone_compliant": cv.compliant(x0, y0, x1, y1)}
    f = font(30 if cv.is_landscape else 32)
    max_w = min(cv.R - cv.L - 110, 1280 if cv.is_landscape else (cv.R - cv.L - 110))
    lines = wrap(d, text, f, max_w, 3)
    lh = 40 if cv.is_landscape else 42
    bh = lh * len(lines) + 22
    text_max_w = max(text_w(d, ln, f, 3) for ln in lines)
    bw = min(cv.R - cv.L, text_max_w + 96)
    cx = (cv.L + cv.R) // 2
    x0 = max(cv.L, cx - bw // 2)
    x1 = min(cv.R, x0 + bw)
    yc = int(y_center if y_center is not None else (135 if cv.is_landscape else 185))
    min_y = cv.TOPY if cv.is_landscape else 130
    y0 = max(min_y, min(cv.MAXY - bh, yc - bh // 2))
    y1 = y0 + bh
    d.rounded_rectangle([x0, y0, x1, y1], radius=14, fill=(12, 14, 20, 140), outline=(*color, 220), width=3)
    if style == "danger":
        _warn_icon(d, x0 + 40, (y0 + y1) // 2, 18, (*color, 255))
    else:
        d.ellipse([x0 + 22, (y0 + y1) // 2 - 17, x0 + 58, (y0 + y1) // 2 + 17], fill=(*color, 255))
        d.text((x0 + 40, (y0 + y1) // 2), "!" if style == "warn" else ("i" if style == "info" else "✓"), font=font(24), anchor="mm", fill=(20, 20, 20, 255))
    y = y0 + 11
    for ln in lines:
        d.text((x0 + 74, y + lh // 2), ln, font=f, anchor="lm", fill=(255, 255, 255, 255), stroke_width=3, stroke_fill=(0, 0, 0, 255))
        y += lh
    return img, {"type": "callout", "style": style, "text": text, "bbox_px": [x0, y0, x1, y1],
                 "safe_zone_compliant": cv.compliant(x0, y0, x1, y1)}


def plate_red_flags(cv: Canvas, title: str, items: list[str], action: str, n_visible: int,
                    show_action: bool) -> tuple[Image.Image, dict]:
    img = cv.blank()
    d = ImageDraw.Draw(img)
    danger, safe = tuple(cv.pal["danger_rgb"]), tuple(cv.pal["safe_rgb"])
    cx = (cv.L + cv.R) // 2

    if cv.is_landscape:
        card_w = min(1380, cv.R - cv.L)
        x0, x1 = cx - card_w // 2, cx + card_w // 2
        compact = len(items) >= 5
        ft = font(36 if compact else 40)
        fi = font(28 if compact else 32)
        fa = font(27 if compact else 30)
        lh_i = 36 if compact else 42
        gap_i = 14 if compact else 20
        lh_a = 36 if compact else 40
        header_h = 72
    else:
        x0, x1 = cv.L, cv.R
        card_w = x1 - x0
        compact = False
        ft, fi, fa = font(42), font(34), font(32)
        lh_i, gap_i, lh_a = 44, 24, 42
        header_h = 80

    inner_w = card_w - 130
    item_lines = [wrap(d, it, fi, inner_w, 3) for it in items]
    action_lines = wrap(d, action, fa, card_w - 80, 3) if action else []
    h_items = sum(len(ls) * lh_i + gap_i for ls in item_lines)
    h_action = (len(action_lines) * lh_a + (36 if cv.is_landscape else 54)) if action else 0
    total_h = header_h + 20 + h_items + h_action + 20

    if cv.is_landscape:
        avail_h = cv.MAXY - cv.TOPY
        y0 = max(cv.TOPY, cv.TOPY + (avail_h - total_h) // 2)
        y1 = min(cv.MAXY, y0 + total_h)
    else:
        y0 = 420
        y1 = min(cv.MAXY, y0 + total_h)

    d.rounded_rectangle([x0, y0, x1, y1], radius=22, fill=(14, 16, 24, 195), outline=(*danger, 230), width=4)
    d.rounded_rectangle([x0, y0, x1, y0 + header_h], radius=22, fill=(*danger, 235))
    d.rectangle([x0, y0 + header_h - 28, x1, y0 + header_h], fill=(*danger, 235))
    _warn_icon(d, x0 + 52, y0 + header_h // 2, 21, (255, 220, 60, 255))
    d.text((cx + 18, y0 + header_h // 2), title, font=ft, anchor="mm", fill=(255, 255, 255, 255))

    y = y0 + header_h + 18
    for k, ls in enumerate(item_lines):
        if k >= n_visible:
            break
        cy = y + lh_i // 2
        d.ellipse([x0 + 28, cy - 21, x0 + 70, cy + 21], fill=(*danger, 255))
        d.text((x0 + 49, cy), str(k + 1), font=font(24 if compact else 28), anchor="mm", fill=(255, 255, 255, 255))
        for ln in ls:
            d.text((x0 + 90, y + lh_i // 2), ln, font=fi, anchor="lm", fill=(255, 255, 255, 255))
            y += lh_i
        y += gap_i

    if action and show_action:
        y = y0 + header_h + 18 + h_items
        ay1 = min(y1 - 12, y + len(action_lines) * lh_a + (28 if cv.is_landscape else 40))
        box_fill = tuple(int(0.28 * c + 0.72 * b) for c, b in zip(safe, (14, 16, 24))) + (255,)
        d.rounded_rectangle([x0 + 20, y, x1 - 20, ay1], radius=14, fill=box_fill, outline=(*safe, 255), width=2)
        yy = y + (14 if cv.is_landscape else 20)
        for ln in action_lines:
            d.text((cx, yy + 18), ln, font=fa, anchor="mm", fill=(255, 255, 255, 255))
            yy += lh_a

    return img, {"type": "red_flags", "title": title, "lines": items + ([action] if action else []),
                 "bbox_px": [x0, y0, x1, y1], "safe_zone_compliant": cv.compliant(x0, y0, x1, y1)}


def plate_disclaimer(cv: Canvas, header: str, lines: list[str]) -> tuple[Image.Image, dict]:
    img = cv.blank()
    d = ImageDraw.Draw(img)
    fh, fb = font(22), font(25 if cv.is_landscape else 26)
    cx = (cv.L + cv.R) // 2
    if cv.is_landscape:
        card_w = min(1160, cv.R - cv.L)
        x0, x1 = cx - card_w // 2, cx + card_w // 2
    else:
        x0, x1 = cv.L, cv.R
        card_w = x1 - x0
    wrapped = [w for ln in lines for w in wrap(d, ln, fb, card_w - 60, 3)]
    bh = 54 + 38 * len(wrapped)
    y0 = (cv.MAXY - bh - 16) if cv.is_landscape else 210
    y1 = y0 + bh
    acc = tuple(cv.pal["accent_rgb"])
    d.rounded_rectangle([x0, y0, x1, y1], radius=14, fill=(10, 14, 22, 165), outline=(*acc, 180), width=2)
    d.text((cx, y0 + 22), header, font=fh, anchor="mm", fill=(*acc, 255), stroke_width=2, stroke_fill=(0, 0, 0, 220))
    y = y0 + 50
    for ln in wrapped:
        d.text((cx, y + 4), ln, font=fb, anchor="mm", fill=(245, 247, 250, 255), stroke_width=3, stroke_fill=(0, 0, 0, 230))
        y += 38
    return img, {"type": "disclaimer", "text": " ".join(lines), "bbox_px": [x0, y0, x1, y1],
                 "safe_zone_compliant": cv.compliant(x0, y0, x1, y1)}


# ----------------------------------------------------------------------------
# Camera / scenes
# ----------------------------------------------------------------------------
WOBBLE = {
    "none": (0.0, 0.0, 0.0, 0.0),
    "calm": (4.0, 0.18, 6.0, 0.25),
    "handheld": (6.0, 1.3, 8.0, 1.8),
    "tense": (3.0, 2.6, 4.0, 3.1),
}


def camera_frame(src: Image.Image, W: int, H: int, scale: float, fx: float, fy: float, dx: float, dy: float) -> Image.Image:
    sw, sh = src.size
    cw, ch = sw / max(scale, 1.001), sh / max(scale, 1.001)
    left = max(0.0, min(sw - cw, fx * sw + dx - cw * 0.5))
    top = max(0.0, min(sh - ch, fy * sh + dy - ch * 0.5))
    return src.transform((W, H), Image.Transform.EXTENT, (left, top, left + cw, top + ch), resample=Image.Resampling.BILINEAR)


class SceneVideoReader:
    def __init__(self, vpath: Path, W: int, H: int, fps: int, n_frames: int):
        self.vpath = vpath
        self.W, self.H, self.fps, self.n_frames = W, H, fps, max(1, n_frames)
        self.frame_sz = W * H * 3
        self._proc = None
        self._cur_idx = -1
        self._cur_img = None

    def get_frame(self, idx: int) -> Image.Image:
        idx = max(0, min(self.n_frames - 1, idx))
        if idx == self._cur_idx and self._cur_img is not None:
            return self._cur_img
        if getattr(self, "_eof", False) and idx >= self._cur_idx and self._cur_img is not None:
            return self._cur_img
        if self._proc is None or idx < self._cur_idx:
            self.close()
            self._proc = subprocess.Popen([
                FFMPEG, "-v", "error", "-i", str(self.vpath),
                "-vf", f"scale={self.W}:{self.H}:force_original_aspect_ratio=increase,crop={self.W}:{self.H},fps={self.fps}",
                "-f", "rawvideo", "-pix_fmt", "rgb24", "-"
            ], stdout=subprocess.PIPE)
            self._cur_idx = -1
            self._eof = False
        last_buf = None
        while self._cur_idx < idx:
            buf = self._proc.stdout.read(self.frame_sz)
            if len(buf) < self.frame_sz:
                self._eof = True
                break
            self._cur_idx += 1
            last_buf = buf
            if self._cur_idx == idx:
                self._cur_img = Image.frombytes("RGB", (self.W, self.H), buf)
                last_buf = None
        if last_buf is not None:
            self._cur_img = Image.frombytes("RGB", (self.W, self.H), last_buf)
        return self._cur_img if self._cur_img is not None else Image.new("RGB", (self.W, self.H))

    def close(self):
        if self._proc is not None:
            try:
                self._proc.stdout.close()
                self._proc.kill()
                self._proc.wait()
            except Exception:
                pass
            self._proc = None


def scene_frame(sc: dict, t: float, W: int, H: int) -> Image.Image:
    s, e = sc["start"], sc["end"]
    mp = sc.get("_motion") or resolve_motion_params(sc)
    dfx = sc.get("_detail_fx") or []

    # Shared wobble + intentional shakes calculation
    ax, fqx, ay, fqy = WOBBLE.get(mp.get("wobble", "none"), WOBBLE["none"])
    lt = t - s
    dx = ax * math.sin(2 * math.pi * fqx * lt) + (ax * 0.5 * math.cos(2 * math.pi * fqx * 2.1 * lt) if ax else 0)
    dy = ay * math.cos(2 * math.pi * fqy * lt)
    for sh in sc.get("shakes", []):
        dt = t - float(sh.get("at", sh.get("t", 0.0)))
        if 0.0 <= dt <= 0.7:
            amp = float(sh.get("amp", 30))
            dec = math.exp(-dt * float(sh.get("decay", 8.5)))
            dx += amp * dec * math.sin(2 * math.pi * 24 * dt)
            dy += amp * 0.75 * dec * math.cos(2 * math.pi * 31 * dt)

    # Level D — Optional external pre-rendered clip (or legacy video scene)
    if sc.get("_vreader"):
        try:
            vr: SceneVideoReader = sc["_vreader"]
            if sc.get("video_fit") == "natural_hold":
                v_off = float(sc.get("video_start_offset", 0.0))
                v_idx = max(0, min(vr.n_frames - 1, int(round((t - s - v_off) * vr.fps))))
            else:
                lin_u = max(0.0, min(1.0, (t - s) / max(e - s, 1e-4)))
                v_idx = min(vr.n_frames - 1, max(0, int(round(lin_u * (vr.n_frames - 1)))))
            frame = vr.get_frame(v_idx)
            return apply_post_camera_fx(frame, dfx, t, W, H) if dfx else frame
        except Exception as exc:
            if sc.get("_img") is None:
                raise
            print(f"    [motion fallback · {sc.get('id', '?')}] Lỗi đọc clip Level D ({exc}) -> hạ cấp Level A")
            sc["_vreader"].close()
            sc["_vreader"] = None
            sc["_effective_level"] = "A"

    # Level B — Lightweight 2.5D Multi-Layer Parallax (max 2–3 layers)
    if sc.get("_parallax"):
        try:
            frame = render_parallax_frame(sc["_parallax"], sc, t, W, H, extra_dx=dx, extra_dy=dy)
            return apply_post_camera_fx(frame, dfx, t, W, H) if dfx else frame
        except Exception as exc:
            if sc.get("_img") is None:
                raise
            print(f"    [motion fallback · {sc.get('id', '?')}] Lỗi parallax Level B ({exc}) -> hạ cấp Level A")
            sc["_parallax"] = None
            sc["_effective_level"] = "A"

    # Level A / Level C — Static Cinematic Motion + optional lightweight Object/Detail Motion
    u = ease_u((max(s, min(e, t)) - s) / max(e - s, 1e-4), mp.get("easing", "smoothstep"))
    s0, s1 = mp["scale"]
    (fx0, fy0), (fx1, fy1) = mp["focus"]
    scale = s0 + (s1 - s0) * u
    fx, fy = fx0 + (fx1 - fx0) * u, fy0 + (fy1 - fy0) * u
    src_img = sc["_img"]
    if dfx:
        try:
            src_img = apply_pre_camera_fx(src_img, dfx, t)
        except Exception as exc:
            print(f"    [motion warn · {sc.get('id', '?')}] Bỏ qua pre-camera detail_fx lỗi ({exc})")
    frame = camera_frame(src_img, W, H, scale, fx, fy, dx, dy)
    if dfx:
        try:
            frame = apply_post_camera_fx(frame, dfx, t, W, H)
        except Exception as exc:
            print(f"    [motion warn · {sc.get('id', '?')}] Bỏ qua post-camera detail_fx lỗi ({exc})")
    return frame


def _validate_scene_paths(ep: Episode, sc: dict) -> None:
    """Fast path-only check before render starts (decodes ZERO images into RAM)."""
    has_img = bool(sc.get("image")) and ep.resolve_asset(sc["image"]).is_file()
    has_vid = bool(sc.get("video")) and sc.get("video_enabled", True) and ep.resolve_asset(sc["video"]).is_file()
    px_layers = (sc.get("parallax") or {}).get("layers") or []
    has_px = len(px_layers) >= 2 and all(
        bool(ly.get("image")) and ep.resolve_asset(ly["image"]).is_file() for ly in px_layers[:3]
    )
    if not (has_img or has_vid or has_px):
        ref = sc.get("image") or sc.get("video") or "parallax.layers"
        raise GateError(f"Cảnh {sc.get('id', '?')} thiếu tài nguyên hình ảnh/video hợp lệ: {ref}")


def _load_scene_runtime(ep: Episode, sc: dict, W: int, H: int, FPS: int, oversample: float,
                        safe_motion: bool, fallbacks: list[dict], detail_warnings: list[dict]) -> None:
    """Lazy-load exactly ONE scene into RAM right before it enters the timeline window."""
    if sc.get("_loaded"):
        return
    sc["_loaded"] = True
    sid = sc.get("id", "?")
    logged = sc.get("_logged_once", False)
    sc["_logged_once"] = True

    def record_fb(msg: str) -> None:
        if not logged:
            print(f"    [motion fallback · {sid}] {msg}")
            fallbacks.append({"scene_id": sid, "reason": msg})

    # Optional safe_motion mode: force lightweight Level A Ken Burns wherever a static image exists
    if safe_motion:
        sc["_detail_fx"] = []
        if sc.get("image") and ep.resolve_asset(sc["image"]).is_file():
            with Image.open(ep.resolve_asset(sc["image"])) as raw_im:
                img = fit_aspect_crop(raw_im.convert("RGB"), W, H)
                sc["_img"] = img.resize((int(W * oversample), int(H * oversample)), Image.Resampling.BILINEAR)
            if sc.get("parallax") or sc.get("detail_fx") or (sc.get("video") and sc.get("video_enabled", True)):
                record_fb("Chế độ --safe-motion -> hạ cấp an toàn về Level A Ken Burns")
            sc["_effective_level"] = "A"
            return

    sc["_detail_fx"] = prepare_detail_fx(ep, sc, W, H, oversample)
    if sc.get("_detail_warnings") and not logged:
        for w_msg in sc["_detail_warnings"]:
            print(f"    [motion warn · {sid}] {w_msg}")
            detail_warnings.append({"scene_id": sid, "warning": w_msg})

    # Level D — External pre-rendered clip
    video_enabled = sc.get("video_enabled", True)
    vpath = ep.resolve_asset(sc["video"]) if (sc.get("video") and video_enabled) else None
    if vpath and vpath.is_file():
        dur_s = max(0.5, sc["end"] - sc["start"])
        n_vf = max(2, int(round(dur_s * FPS)))
        sc["_vreader"] = SceneVideoReader(vpath, W, H, FPS, n_vf)
        sc["_effective_level"] = "D"
        return
    elif sc.get("video") and not video_enabled:
        record_fb("Level D tắt (video_enabled=false) -> hạ cấp an toàn về ảnh tĩnh")
    elif sc.get("video") and sc.get("image"):
        record_fb(f"Thiếu clip '{sc['video']}' -> hạ cấp an toàn về ảnh tĩnh '{sc['image']}'")

    # Level B — Lightweight 2–3 layer 2.5D parallax
    if sc.get("parallax"):
        px_rt = prepare_parallax(ep, sc, W, H, oversample)
        if px_rt is not None:
            sc["_parallax"] = px_rt
            sc["_effective_level"] = "B"
            return
        elif sc.get("_motion_fallback"):
            record_fb(sc["_motion_fallback"])

    # Level A / Level C — Base static image
    if not sc.get("image"):
        raise GateError(f"Cảnh {sid} thiếu cả ảnh lẫn video/parallax hợp lệ.")
    p = ep.resolve_asset(sc["image"])
    if not p.is_file():
        raise GateError(f"Thiếu ảnh cảnh: {rel(p)}")
    with Image.open(p) as raw_im:
        img = fit_aspect_crop(raw_im.convert("RGB"), W, H)
        sc["_img"] = img.resize((int(W * oversample), int(H * oversample)), Image.Resampling.LANCZOS)
    sc["_effective_level"] = "C" if sc["_detail_fx"] else "A"


def composite_scene(scenes: list[dict], t: float, W: int, H: int) -> Image.Image:
    idx = 0
    for i, sc in enumerate(scenes):
        if t >= sc["start"]:
            idx = i
    sc = scenes[idx]
    frame = scene_frame(sc, t, W, H)
    tr = sc.get("transition_in", {"type": "dissolve", "dur": 0.3})
    ttype, tdur = tr.get("type", "dissolve"), float(tr.get("dur", 0.3))
    if idx > 0 and ttype != "cut" and t < sc["start"] + tdur:
        u = (t - sc["start"]) / max(tdur, 1e-3)
        prev = scene_frame(scenes[idx - 1], t, W, H)
        if ttype == "dissolve":
            return Image.blend(prev, frame, smoothstep(u))
        if ttype in ("flash_white", "flash_red"):
            col = (255, 255, 255) if ttype == "flash_white" else (200, 20, 30)
            flash = Image.new("RGB", (W, H), col)
            return Image.blend(flash, frame, smoothstep(u))
        if ttype == "fade_black":
            black = Image.new("RGB", (W, H), (0, 0, 0))
            return Image.blend(black, frame, smoothstep(u))
        if ttype == "glitch":
            k = int(u * 10)
            base = prev if k % 2 == 0 and u < 0.6 else frame
            r, g, b = base.split()
            off = int(24 * (1 - u))
            r = r.transform((W, H), Image.Transform.AFFINE, (1, 0, off, 0, 1, 0))
            b = b.transform((W, H), Image.Transform.AFFINE, (1, 0, -off, 0, 1, 0))
            return Image.merge("RGB", (r, g, b))
    return frame


def safe_zone_guide(img: Image.Image, cv: Canvas) -> Image.Image:
    out = img.copy().convert("RGBA")
    ov = Image.new("RGBA", out.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)
    if cv.is_landscape:
        d.rectangle([0, 0, cv.L, cv.H], fill=(220, 40, 40, 50))
    d.rectangle([cv.R, 0, cv.W, cv.H], fill=(220, 40, 40, 60))
    d.rectangle([0, cv.UIBOT, cv.W, cv.H], fill=(220, 40, 40, 60))
    d.rectangle([cv.L, cv.TOPY if cv.is_landscape else 120, cv.R, cv.MAXY], outline=(40, 235, 120, 220), width=3)
    return Image.alpha_composite(out, ov).convert("RGB")


def srt_time(sec: float) -> str:
    ms = int(round(sec * 1000))
    return f"{ms // 3600000:02d}:{ms % 3600000 // 60000:02d}:{ms % 60000 // 1000:02d},{ms % 1000:03d}"


def split_subtitle(text: str, custom: list[str] | None, max_merge_chars: int = 26) -> list[str]:
    if custom:
        return custom
    parts = [p.strip() for p in re.split(r"(?<=[.!?…])\s+|(?<=\.\.\.)\s*", text) if p and p.strip()]
    merged: list[str] = []
    for p in parts:
        if merged and len(merged[-1]) + len(p) < max_merge_chars:
            merged[-1] = f"{merged[-1]} {p}"
        else:
            merged.append(p)
    return merged or [text]


def _paste_rgba_crop(dst_rgb: Image.Image, crop_rgba: Image.Image, pos: tuple[int, int], alpha_mul: float = 1.0) -> None:
    """Fast localized alpha composite onto an RGB frame."""
    if alpha_mul <= 0.01:
        return
    if alpha_mul < 0.99:
        _, _, _, al = crop_rgba.split()
        al = al.point(lambda p, a=alpha_mul: int(p * a))
        dst_rgb.paste(crop_rgba.convert("RGB"), pos, al)
    else:
        dst_rgb.paste(crop_rgba.convert("RGB"), pos, crop_rgba.getchannel("A"))


# ----------------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------------

def run(ep: Episode, preview_only: bool = False, safe_motion: bool = False) -> dict:
    mode_tag = " · SAFE-MOTION (Level A)" if safe_motion else ""
    print(f"=== GATE 4: TIMELINE & SAFE ZONE [{ep.factory_name} · {ep.aspect_label}{mode_tag}] – {ep.id} ===")
    cfg = ep.cfg
    cv = Canvas(ep)
    W, H, FPS, DUR = ep.width, ep.height, ep.fps, ep.duration
    stg = ep.staging_dir
    ovl_dir, prv_dir = stg / "overlays", stg / "preview_frames"
    for d_ in (stg, ovl_dir, prv_dir, ep.srt_path.parent):
        d_.mkdir(parents=True, exist_ok=True)

    if not ep.tts_manifest_path.is_file():
        raise GateError("Chưa có manifest Gate 2.")
    tts = load_json(ep.tts_manifest_path)

    # --- scenes: validate paths ONLY (lazy sliding-window load keeps max 1–2 scenes in RAM) ---
    is_level2 = str(cfg.get("motion_upgrade", "")).lower() in ("level2", "v2", "2") or bool(cfg.get("motion_plan"))
    scenes = []
    fallbacks: list[dict] = []
    detail_warnings: list[dict] = []
    oversample = 1.25 if cv.is_landscape else 1.3333
    for sc in cfg["scenes"]:
        sc2 = dict(sc)
        sc2["start"], sc2["end"] = float(sc["start"]), float(sc["end"])
        sc2["_motion"] = resolve_motion_params(sc2)
        sc2["_loaded"] = False
        _validate_scene_paths(ep, sc2)
        sc2["_effective_level"] = "A"
        scenes.append(sc2)
    scenes.sort(key=lambda s: s["start"])
    if abs(scenes[0]["start"]) > 1e-3 or abs(scenes[-1]["end"] - DUR) > 0.05:
        raise GateError(f"Cảnh phải phủ kín 0 → {DUR}s (hiện {scenes[0]['start']} → {scenes[-1]['end']}).")

    # --- overlays ---
    events: list[dict] = []

    def add(img: Image.Image, meta: dict, name: str, start: float, end: float, fade: float = 0.15,
            slide_y: int = 0, anim_dur: float = 0.0):
        path = ovl_dir / f"{len(events):03d}_{name}.png"
        img.save(path)
        bbox = img.getbbox()
        crop = img.crop(bbox) if bbox else None
        pos = (bbox[0], bbox[1]) if bbox else (0, 0)
        events.append({"id": path.stem, "start_sec": round(start, 3), "end_sec": round(end, 3), "fade_sec": fade,
                       "png_path": rel(path), "_crop": crop, "_pos": pos, "_slide_y": slide_y,
                       "_anim_dur": anim_dur, **meta})

    brand_img, brand_meta = plate_branding(cv)
    brand_img.save(ovl_dir / "branding.png")
    brand_bbox = brand_img.getbbox()
    brand_crop = brand_img.crop(brand_bbox) if brand_bbox else None
    brand_pos = (brand_bbox[0], brand_bbox[1]) if brand_bbox else (0, 0)

    hk = cfg.get("hook")
    if hk:
        im, me = plate_hook(cv, hk["title"], hk.get("kicker", ""))
        add(im, me, "hook", hk.get("start", 0.3), hk.get("end", 4.5), 0.3)

    for i, chp in enumerate(cfg.get("chapters", [])):
        im, me = plate_chapter(cv, chp["title"], chp.get("kicker", f"HỒI {i + 1}"))
        add(im, me, f"chapter{i + 1}", float(chp["start"]), float(chp.get("end", float(chp["start"]) + 4.5)), 0.3)

    srt_entries = []
    sub_rgb = tuple(ep.channel["palette"]["subtitle_rgb"])
    merge_chars = int(cv.fmt.get("subtitle_merge_chars", 44 if cv.is_landscape else 26))
    for ln in tts["lines"]:
        chunks = split_subtitle(ln["text"], ln.get("subtitle"), max_merge_chars=merge_chars)
        s, e = ln["timeline_start_sec"], ln["timeline_end_sec"]
        total_chars = sum(len(c) for c in chunks)
        cur = s
        spk = ep.cast.get(ln["speaker"], {})
        color = tuple(spk.get("subtitle_rgb", sub_rgb))
        lbl_short = ln.get("label_short") or spk.get("label_short", "")
        for c in chunks:
            dur = (e - s) * len(c) / max(total_chars, 1)
            im, me = plate_subtitle(cv, c, color, lbl_short)
            add(im, me, f"sub_{ln['line_id']}", cur, cur + dur, 0.1)
            srt_entries.append((cur, cur + dur, c))
            cur += dur

    for i, cb in enumerate(cfg.get("chat_bubbles", [])):
        im, me = plate_chat(cv, cb["text"], cb.get("side", "left"), cb.get("sender", ""), cb.get("y"), cb.get("stamp", ""))
        anim = cb.get("anim", "slide_up" if is_level2 else "fade")
        s_y = 20 if anim == "slide_up" else (-20 if anim == "slide_down" else 0)
        add(im, me, f"chat{i + 1}", cb["start"], cb["end"], 0.16, slide_y=s_y, anim_dur=0.24 if s_y else 0.0)

    for i, nt in enumerate(cfg.get("notifications", [])):
        im, me = plate_notification(cv, nt.get("title", "Thông báo mới"), nt["text"],
                                    nt.get("stamp", "vừa xong"), nt.get("y"), nt.get("style", "neutral"))
        anim = nt.get("anim", "slide_down")
        s_y = -24 if anim == "slide_down" else (20 if anim == "slide_up" else 0)
        add(im, me, f"notif{i + 1}", float(nt["start"]), float(nt["end"]), 0.18,
            slide_y=s_y, anim_dur=0.24 if s_y else 0.0)

    for i, co in enumerate(cfg.get("callouts", [])):
        im, me = plate_callout(cv, co["text"], co.get("style", "danger"), co.get("y"),
                               co.get("size", "normal"), co.get("kicker", ""))
        add(im, me, f"callout{i + 1}", co["start"], co["end"], 0.2)

    rf = cfg.get("red_flags")
    if rf:
        items, action = rf["items"], rf.get("action", "")
        s, e = float(rf["start"]), float(rf["end"])
        stagger = float(rf.get("stagger_sec", 1.2 if cv.is_landscape else 0.7))
        steps = len(items) + (1 if action else 0)
        for k in range(steps):
            st = s + k * stagger
            en = e if k == steps - 1 else s + (k + 1) * stagger
            n_vis = min(k + 1, len(items))
            im, me = plate_red_flags(cv, rf.get("title", "DẤU HIỆU NHẬN BIẾT"), items, action, n_vis, k >= len(items))
            add(im, me, f"redflags_{k}", st, en, 0.25 if k == 0 else 0.0)

    disc_cfg = {**ep.channel["disclaimer"], **(cfg.get("disclaimer") or {})}
    ds, de = float(disc_cfg.get("start", DUR - 3.0)), float(disc_cfg.get("end", DUR))
    im, me = plate_disclaimer(cv, disc_cfg["header"], disc_cfg["lines"])
    add(im, me, "disclaimer", ds, de, 0.25)

    # SRT
    ep.srt_path.write_text("\n".join(f"{i + 1}\n{srt_time(a)} --> {srt_time(b)}\n{t}\n"
                                     for i, (a, b, t) in enumerate(srt_entries)), encoding="utf-8")

    # --- QA preview timestamps ---
    qa_times = cfg.get("qa_preview_sec") or sorted(set(
        [round((sc["start"] + sc["end"]) / 2, 2) for sc in scenes]
        + collect_fx_qa_timestamps(scenes)
        + [round(float(nt["start"]) + 0.4, 2) for nt in cfg.get("notifications", [])]
        + ([round(hk.get("start", 0.3) + 1.0, 2)] if hk else [])
        + ([round(float(rf["end"]) - 0.5, 2)] if rf else [])
        + [round((ds + de) / 2, 2)]
    ))
    qa_idx = {int(round(t * FPS)): t for t in qa_times if 0 <= t < DUR}

    # --- render (strict sequential single-scene streaming + sliding-window RAM control) ---
    out_mp4 = ep.timeline_video_path
    total_frames = ep.total_frames
    frame_range = sorted(qa_idx) if preview_only else range(total_frames)
    proc = None
    if not preview_only:
        print(f" -> Render {total_frames} frames ({DUR}s @ {FPS}fps, {W}x{H}) -> {out_mp4.name}")
        proc = subprocess.Popen([FFMPEG, "-y", "-v", "error", "-f", "rawvideo", "-vcodec", "rawvideo", "-s", f"{W}x{H}",
                                 "-pix_fmt", "rgb24", "-r", str(FPS), "-i", "-", "-an", "-c:v", "libx264", "-preset", "fast",
                                 "-threads", "4", "-crf", "18", "-pix_fmt", "yuv420p", str(out_mp4)],
                                stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    previews = []
    step_log = 900 if cv.is_landscape else 300
    loaded_indices: set[int] = set()
    try:
        for fi in frame_range:
            t = fi / FPS
            # Find active scene index & whether previous scene is needed for transition_in
            idx = 0
            for i, sc_ in enumerate(scenes):
                if t >= sc_["start"]:
                    idx = i
            sc_cur = scenes[idx]
            tr = sc_cur.get("transition_in", {"type": "dissolve", "dur": 0.3})
            need_prev = idx > 0 and tr.get("type", "dissolve") != "cut" and t < sc_cur["start"] + float(tr.get("dur", 0.3))
            needed = {idx, idx - 1} if need_prev else {idx}
            # Evict any scene outside the active 1–2 scene window immediately
            for old_i in list(loaded_indices - needed):
                unload_scene_runtime(scenes[old_i])
                loaded_indices.discard(old_i)
            for req_i in sorted(needed):
                if req_i not in loaded_indices:
                    _load_scene_runtime(ep, scenes[req_i], W, H, FPS, oversample, safe_motion, fallbacks, detail_warnings)
                    loaded_indices.add(req_i)

            frame = composite_scene(scenes, t, W, H)
            for ev in events:
                if ev["start_sec"] <= t < ev["end_sec"] and ev.get("_crop") is not None:
                    fade = ev["fade_sec"]
                    a = 1.0
                    if fade > 0:
                        a = min(1.0, (t - ev["start_sec"]) / fade, (ev["end_sec"] - t) / fade)
                    px, py = ev["_pos"]
                    if ev.get("_slide_y") and ev.get("_anim_dur", 0.0) > 0:
                        dt_in = t - ev["start_sec"]
                        if dt_in < ev["_anim_dur"]:
                            py += int(round(ev["_slide_y"] * (1.0 - ease_u(dt_in / ev["_anim_dur"], "ease_out"))))
                    _paste_rgba_crop(frame, ev["_crop"], (px, py), a)
            if brand_crop is not None:
                _paste_rgba_crop(frame, brand_crop, brand_pos, 1.0)
            if t < 0.3:
                frame = Image.blend(Image.new("RGB", (W, H)), frame, smoothstep(t / 0.3))
            elif t > DUR - 0.35:
                frame = Image.blend(frame, Image.new("RGB", (W, H)), smoothstep((t - (DUR - 0.35)) / 0.35) * 0.6)
            if fi in qa_idx:
                tag = f"qa_{qa_idx[fi]:05.2f}s".replace(".", "_")
                cp, gp = prv_dir / f"{tag}_clean.jpg", prv_dir / f"{tag}_safezone.jpg"
                frame.save(cp, quality=92)
                safe_zone_guide(frame, cv).save(gp, quality=88)
                previews.append({"timestamp_sec": qa_idx[fi], "clean": rel(cp), "safezone": rel(gp)})
            if proc:
                proc.stdin.write(frame.tobytes())
                if (fi + 1) % step_log == 0:
                    print(f"    ... {fi + 1}/{total_frames}")
    finally:
        for sc in scenes:
            unload_scene_runtime(sc)
        if proc:
            try:
                proc.stdin.close()
            except Exception:
                pass
    if proc:
        err = proc.stderr.read().decode("utf-8", "replace")
        if proc.wait() != 0:
            raise GateError(f"FFmpeg lỗi: {err}")

    motion_audit = audit_episode_motion(ep)
    effective_counts = {"A": 0, "B": 0, "C": 0, "D": 0}
    for sc in scenes:
        lv = sc.get("_effective_level", "A")
        effective_counts[lv] = effective_counts.get(lv, 0) + 1

    overlays = [{k: v for k, v in ev.items() if not k.startswith("_")} for ev in events]
    manifest = {
        "episode_id": ep.id,
        "factory": ep.factory_name,
        "gate": "GATE_4_TIMELINE_SAFE_ZONE",
        "preview_only": preview_only,
        "canvas": {"width": W, "height": H, "fps": FPS, "aspect_ratio": ep.aspect_label, "total_frames": total_frames, "total_duration_sec": DUR},
        "safe_zone_rules": {**ep.safe, "all_overlays_compliant": all(o.get("safe_zone_compliant", True) for o in overlays)},
        "motion_summary": {
            "hardware_profile": HARDWARE_PROFILE,
            "safe_motion_mode": safe_motion,
            "is_level2": is_level2,
            "declared_level_counts": motion_audit["level_counts"],
            "effective_level_counts": effective_counts,
            "fallbacks": fallbacks,
            "detail_warnings": detail_warnings,
            "zoom_streaks": motion_audit["zoom_streaks"],
            "shake_scenes": motion_audit["shake_scenes"],
            "sfx_sync": motion_audit["sfx_sync"],
            "warnings": motion_audit["warnings"],
        },
        "scenes": [{k: v for k, v in sc.items() if not k.startswith("_")} for sc in scenes],
        "subtitle_srt": rel(ep.srt_path),
        "video_track_noaudio": None if preview_only else rel(out_mp4),
        "channel_branding": brand_meta,
        "overlays": overlays,
        "qa_preview_frames": previews,
    }
    save_json(ep.timeline_manifest_path, manifest)
    bad = [o["id"] for o in overlays if not o.get("safe_zone_compliant", True)]
    if bad:
        print(f" !! Overlay tràn Safe Zone: {bad}")
    print(f" -> Motion Level thực thi: A={effective_counts['A']} · B={effective_counts['B']} · C={effective_counts['C']} · D={effective_counts['D']}"
          + (f" (fallback: {len(fallbacks)})" if fallbacks else ""))
    print(f" -> {len(previews)} khung QA tại {rel(prv_dir)}")
    print(f" -> Manifest: {rel(ep.timeline_manifest_path)}")
    return manifest

