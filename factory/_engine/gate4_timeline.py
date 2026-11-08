# -*- coding: utf-8 -*-
"""
GATE 4 – Dựng timeline 9:16, chuyển động camera, đồ họa chữ trong Safe Zone.

Kế thừa từ 779 (assemble_timeline_gate4.py): branding VCH, Ken Burns sub-pixel,
camera shake tắt dần, cross-dissolve, kiểm tra Safe Zone, khung QA preview.

Mới cho kênh Bóc Trần Lừa Đảo (tất cả cấu hình trong episode.json):
  * "scenes"      – số cảnh tùy ý, mỗi cảnh có motion / shakes / transition_in.
  * "hook"        – tít mở đầu.
  * Phụ đề        – tự sinh từ manifest Gate 2 (chia nhỏ theo "subtitle" hoặc dấu câu).
  * "chat_bubbles"– bong bóng tin nhắn giả lập (KHÔNG mô phỏng giao diện app thật).
  * "callouts"    – băng chữ cảnh báo giữa video (danger / info / safe).
  * "red_flags"   – thẻ DẤU HIỆU NHẬN BIẾT, các ý hiện lần lượt.
  * "disclaimer"  – lưu ý hư cấu (mặc định lấy từ channel_config.json).
"""
from __future__ import annotations

import math
import re
import subprocess
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from core import FFMPEG, PROJECT_ROOT, Episode, GateError, load_json, rel, save_json

# ----------------------------------------------------------------------------
# Fonts & text helpers
# ----------------------------------------------------------------------------
_FONT_CACHE: dict = {}


def font(size: int, bold: bool = True) -> ImageFont.FreeTypeFont:
    key = (size, bold)
    if key in _FONT_CACHE:
        return _FONT_CACHE[key]
    cands = ([r"C:\Windows\Fonts\segoeuib.ttf", r"C:\Windows\Fonts\arialbd.ttf", r"C:\Windows\Fonts\tahomabd.ttf"]
             if bold else [r"C:\Windows\Fonts\segoeui.ttf", r"C:\Windows\Fonts\arial.ttf", r"C:\Windows\Fonts\tahoma.ttf"])
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
        s = ep.safe
        self.L, self.R, self.MAXY, self.TOPY = s["left_x"], s["right_x"], s["max_y"], s["top_hook_y"]
        self.pal = ep.channel["palette"]
        self.ch = ep.channel["channel"]

    def blank(self) -> Image.Image:
        return Image.new("RGBA", (self.W, self.H), (0, 0, 0, 0))

    def compliant(self, x0, y0, x1, y1) -> bool:
        return x0 >= self.L and x1 <= self.R and y1 <= self.MAXY and y0 >= 0


# ----------------------------------------------------------------------------
# Overlay plate renderers
# ----------------------------------------------------------------------------

def plate_branding(cv: Canvas) -> tuple[Image.Image, dict]:
    img = cv.blank()
    d = ImageDraw.Draw(img)
    base = min(cv.W, cv.H)
    badge_h = max(24, round(base * 0.032))
    lf = font(max(14, round(badge_h * 0.62)))
    lt = cv.ch["logo_text"]
    lb = d.textbbox((0, 0), lt, font=lf)
    tw, th = lb[2] - lb[0], lb[3] - lb[1]
    pad = round(badge_h * 0.45)
    bw, m = tw + pad * 2, round(base * 0.028)
    d.rounded_rectangle((m, m, m + bw, m + badge_h), radius=max(4, round(badge_h * 0.22)),
                        fill=(*cv.ch["logo_color_rgb"], round(255 * cv.ch["logo_opacity"])))
    d.text((m + (bw - tw) / 2 - lb[0], m + (badge_h - th) / 2 - lb[1]), lt, font=lf, fill=(255, 255, 255, 255))
    # series tag cạnh logo
    sf = font(max(12, round(badge_h * 0.5)))
    d.text((m + bw + 12, m + badge_h / 2), cv.ch.get("series_name", ""), font=sf, anchor="lm",
           fill=(255, 255, 255, 200), stroke_width=2, stroke_fill=(0, 0, 0, 160))
    wt = cv.ch["watermark_text"]
    wf = font(max(16, round(base * 0.024)))
    wb = d.textbbox((0, 0), wt, font=wf)
    wx, wy = cv.W - (wb[2] - wb[0]) - int(base * 0.06), int(cv.H * 0.742)
    a = cv.ch["watermark_opacity"]
    d.text((wx + 2, wy + 2), wt, font=wf, fill=(0, 0, 0, round(255 * a * 0.65)))
    d.text((wx, wy), wt, font=wf, fill=(255, 255, 255, round(255 * a)))
    return img, {"type": "channel_branding", "logo_text": lt, "watermark_text": wt, "safe_zone_compliant": True}


def plate_hook(cv: Canvas, title: str, kicker: str = "") -> tuple[Image.Image, dict]:
    img = cv.blank()
    d = ImageDraw.Draw(img)
    fm, fk = font(46), font(24)
    max_w = cv.R - cv.L - 60
    lines = wrap(d, title, fm, max_w, 4)
    lh = 56
    box_h = 26 + (38 if kicker else 0) + lh * len(lines) + 14
    box_w = min(cv.R - cv.L, max([text_w(d, ln, fm, 4) for ln in lines] + [text_w(d, kicker, fk, 2)]) + 56)
    cx = (cv.L + cv.R) // 2
    x0, y0 = max(cv.L, cx - box_w // 2), cv.TOPY
    x1, y1 = min(cv.R, x0 + box_w), cv.TOPY + box_h
    danger = tuple(cv.pal["danger_rgb"])
    d.rounded_rectangle([x0, y0, x1, y1], radius=16, fill=(10, 12, 18, 125), outline=(*danger, 210), width=3)
    y = y0 + 16
    if kicker:
        kw = text_w(d, kicker, fk, 0) + 24
        d.rounded_rectangle([cx - kw // 2, y - 2, cx + kw // 2, y + 32], radius=8, fill=(*danger, 230))
        d.text((cx, y + 15), kicker, font=fk, anchor="mm", fill=(255, 255, 255, 255))
        y += 44
    for ln in lines:
        d.text((cx, y + lh // 2 - 4), ln, font=fm, anchor="mm", fill=(255, 255, 255, 255), stroke_width=4, stroke_fill=(0, 0, 0, 255))
        y += lh
    return img, {"type": "text_hook", "text": f"{kicker} — {title}".strip(" —"), "bbox_px": [x0, y0, x1, y1],
                 "safe_zone_compliant": cv.compliant(x0, y0, x1, y1)}


def plate_subtitle(cv: Canvas, text: str, color: tuple, speaker_label: str = "") -> tuple[Image.Image, dict]:
    """Phụ đề điện ảnh thuần túy (không hộp đen, không nhãn tên người nói): chữ có bóng đổ & viền đen sắc nét ở cạnh dưới Safe Zone."""
    img = cv.blank()
    d = ImageDraw.Draw(img)
    f = font(44)
    lines = wrap(d, text, f, cv.R - cv.L - 40, 5)
    lh = 56
    box_h = lh * len(lines)
    box_w = min(cv.R - cv.L, max(text_w(d, ln, f, 5) for ln in lines) + 20)
    cx = (cv.L + cv.R) // 2
    x0 = max(cv.L, cx - box_w // 2)
    x1 = min(cv.R, x0 + box_w)
    y1 = 1380
    y0 = y1 - box_h
    y = y0
    for ln in lines:
        cy = y + lh // 2
        d.text((cx + 3, cy + 4), ln, font=f, anchor="mm", fill=(0, 0, 0, 180), stroke_width=6, stroke_fill=(0, 0, 0, 180))
        d.text((cx, cy), ln, font=f, anchor="mm", fill=(*color, 255), stroke_width=5, stroke_fill=(0, 0, 0, 255))
        y += lh
    return img, {"type": "subtitle", "lines": lines, "bbox_px": [x0, y0, x1, y1],
                 "safe_zone_compliant": cv.compliant(x0, y0, x1, y1)}


def plate_chat(cv: Canvas, text: str, side: str = "left", sender: str = "", y_top: int = 520,
               stamp: str = "") -> tuple[Image.Image, dict]:
    """Bong bóng tin nhắn trung tính (không logo, không giao diện app thật)."""
    img = cv.blank()
    d = ImageDraw.Draw(img)
    f = font(38, bold=False)
    max_w = int((cv.R - cv.L) * 0.78)
    lines = wrap(d, text, f, max_w - 56)
    lh = 50
    bw = max(text_w(d, ln, f) for ln in lines) + 56
    bh = lh * len(lines) + 36 + (34 if sender else 0)
    if side == "right":
        x1 = cv.R
        x0 = x1 - bw
        fill, txt = (0, 132, 255, 240), (255, 255, 255, 255)
    else:
        x0 = cv.L
        x1 = x0 + bw
        fill, txt = (245, 245, 247, 245), (20, 20, 24, 255)
    y0, y1 = y_top, y_top + bh
    d.rounded_rectangle([x0 + 4, y0 + 6, x1 + 4, y1 + 6], radius=28, fill=(0, 0, 0, 90))
    d.rounded_rectangle([x0, y0, x1, y1], radius=28, fill=fill)
    y = y0 + 18
    if sender:
        d.text((x0 + 28, y + 12), sender, font=font(26), anchor="lm",
               fill=(230, 40, 45, 255) if side == "left" else (220, 235, 255, 255))
        y += 34
    for ln in lines:
        d.text((x0 + 28, y + lh // 2), ln, font=f, anchor="lm", fill=txt)
        y += lh
    if stamp:
        d.text((x1 - 18, y1 + 18), stamp, font=font(22, bold=False), anchor="rm", fill=(255, 255, 255, 210),
               stroke_width=2, stroke_fill=(0, 0, 0, 200))
    return img, {"type": "chat_bubble", "text": text, "sender": sender, "bbox_px": [x0, y0, x1 + 4, y1 + 30],
                 "safe_zone_compliant": cv.compliant(x0, y0, x1 + 4, y1 + 30)}


def _warn_icon(d: ImageDraw.ImageDraw, cx: int, cy: int, r: int, color) -> None:
    d.polygon([(cx, cy - r), (cx + r, cy + int(r * 0.8)), (cx - r, cy + int(r * 0.8))], fill=color)
    d.text((cx, cy + int(r * 0.15)), "!", font=font(int(r * 1.1)), anchor="mm", fill=(20, 20, 20, 255))


def plate_callout(cv: Canvas, text: str, style: str = "danger", y_center: int = 185) -> tuple[Image.Image, dict]:
    """Tag ghi chú gọn nhẹ ôm sát chữ ở mép trên (không làm hộp đen che giữa màn hình)."""
    img = cv.blank()
    d = ImageDraw.Draw(img)
    color = {"danger": cv.pal["danger_rgb"], "safe": cv.pal["safe_rgb"], "info": cv.pal["accent_rgb"], "warn": cv.pal["accent_rgb"]}.get(style, cv.pal["danger_rgb"])
    f = font(32)
    lines = wrap(d, text, f, cv.R - cv.L - 110, 3)
    lh = 42
    bh = lh * len(lines) + 22
    text_max_w = max(text_w(d, ln, f, 3) for ln in lines)
    bw = min(cv.R - cv.L, text_max_w + 96)
    cx = (cv.L + cv.R) // 2
    x0 = max(cv.L, cx - bw // 2)
    x1 = min(cv.R, x0 + bw)
    y0 = max(130, min(cv.MAXY - bh, y_center - bh // 2))
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
    x0, x1 = cv.L, cv.R
    y0 = 420
    ft, fi, fa = font(42), font(34), font(32)
    inner_w = x1 - x0 - 130
    item_lines = [wrap(d, it, fi, inner_w, 3) for it in items]
    action_lines = wrap(d, action, fa, x1 - x0 - 80, 3) if action else []
    h_items = sum(len(ls) * 44 + 24 for ls in item_lines)
    h_action = (len(action_lines) * 42 + 54) if action else 0
    y1 = y0 + 96 + h_items + h_action + 24
    d.rounded_rectangle([x0, y0, x1, y1], radius=22, fill=(14, 16, 24, 195), outline=(*danger, 230), width=4)
    d.rounded_rectangle([x0, y0, x1, y0 + 80], radius=22, fill=(*danger, 235))
    d.rectangle([x0, y0 + 50, x1, y0 + 80], fill=(*danger, 235))
    _warn_icon(d, x0 + 52, y0 + 40, 22, (255, 220, 60, 255))
    d.text(((x0 + x1) // 2 + 20, y0 + 40), title, font=ft, anchor="mm", fill=(255, 255, 255, 255))
    y = y0 + 100
    for k, ls in enumerate(item_lines):
        if k >= n_visible:
            break
        cy = y + 22
        d.ellipse([x0 + 28, cy - 22, x0 + 72, cy + 22], fill=(*danger, 255))
        d.text((x0 + 50, cy), str(k + 1), font=font(28), anchor="mm", fill=(255, 255, 255, 255))
        for ln in ls:
            d.text((x0 + 92, y + 22), ln, font=fi, anchor="lm", fill=(255, 255, 255, 255))
            y += 44
        y += 24
    if action and show_action:
        y = y0 + 100 + h_items
        ay1 = y + len(action_lines) * 42 + 40
        box_fill = tuple(int(0.28 * c + 0.72 * b) for c, b in zip(safe, (14, 16, 24))) + (255,)
        d.rounded_rectangle([x0 + 20, y, x1 - 20, ay1], radius=14, fill=box_fill, outline=(*safe, 255), width=2)
        yy = y + 20
        for ln in action_lines:
            d.text(((x0 + x1) // 2, yy + 18), ln, font=fa, anchor="mm", fill=(255, 255, 255, 255))
            yy += 42
    return img, {"type": "red_flags", "title": title, "lines": items + ([action] if action else []),
                 "bbox_px": [x0, y0, x1, y1], "safe_zone_compliant": cv.compliant(x0, y0, x1, y1)}


def plate_disclaimer(cv: Canvas, header: str, lines: list[str]) -> tuple[Image.Image, dict]:
    img = cv.blank()
    d = ImageDraw.Draw(img)
    fh, fb = font(22), font(26)
    wrapped = [w for ln in lines for w in wrap(d, ln, fb, cv.R - cv.L - 60, 3)]
    x0, x1 = cv.L, cv.R
    y0 = 210
    y1 = y0 + (54 + 38 * len(wrapped))
    acc = tuple(cv.pal["accent_rgb"])
    d.rounded_rectangle([x0, y0, x1, y1], radius=14, fill=(10, 14, 22, 160), outline=(*acc, 180), width=2)
    cx = (x0 + x1) // 2
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
        if self._proc is None or idx < self._cur_idx:
            self.close()
            self._proc = subprocess.Popen([
                FFMPEG, "-v", "error", "-i", str(self.vpath),
                "-vf", f"scale={self.W}:{self.H}:force_original_aspect_ratio=increase,crop={self.W}:{self.H},fps={self.fps}",
                "-f", "rawvideo", "-pix_fmt", "rgb24", "-"
            ], stdout=subprocess.PIPE)
            self._cur_idx = -1
        while self._cur_idx < idx:
            buf = self._proc.stdout.read(self.frame_sz)
            if len(buf) < self.frame_sz:
                break
            self._cur_idx += 1
            if self._cur_idx == idx or self._cur_img is None:
                self._cur_img = Image.frombytes("RGB", (self.W, self.H), buf)
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
    u = smoothstep((max(s, min(e, t)) - s) / max(e - s, 1e-4))
    if sc.get("_vreader"):
        vr: SceneVideoReader = sc["_vreader"]
        lin_u = max(0.0, min(1.0, (t - s) / max(e - s, 1e-4)))
        v_idx = min(vr.n_frames - 1, max(0, int(round(lin_u * (vr.n_frames - 1)))))
        return vr.get_frame(v_idx)
    m = sc.get("motion", {})
    s0, s1 = m.get("scale", [1.03, 1.12])
    (fx0, fy0), (fx1, fy1) = m.get("focus", [[0.5, 0.5], [0.5, 0.5]])
    scale = s0 + (s1 - s0) * u
    fx, fy = fx0 + (fx1 - fx0) * u, fy0 + (fy1 - fy0) * u
    ax, fqx, ay, fqy = WOBBLE.get(m.get("wobble", "calm"), WOBBLE["calm"])
    lt = t - s
    dx = ax * math.sin(2 * math.pi * fqx * lt) + (ax * 0.5 * math.cos(2 * math.pi * fqx * 2.1 * lt) if ax else 0)
    dy = ay * math.cos(2 * math.pi * fqy * lt)
    for sh in sc.get("shakes", []):
        dt = t - float(sh["at"])
        if 0.0 <= dt <= 0.7:
            amp = float(sh.get("amp", 30))
            dec = math.exp(-dt * float(sh.get("decay", 8.5)))
            dx += amp * dec * math.sin(2 * math.pi * 24 * dt)
            dy += amp * 0.75 * dec * math.cos(2 * math.pi * 31 * dt)
    return camera_frame(sc["_img"], W, H, scale, fx, fy, dx, dy)


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
    d.rectangle([cv.R, 0, cv.W, cv.H], fill=(220, 40, 40, 60))
    d.rectangle([0, 1440, cv.W, cv.H], fill=(220, 40, 40, 60))
    d.rectangle([cv.L, 120, cv.R, cv.MAXY], outline=(40, 235, 120, 220), width=3)
    return Image.alpha_composite(out, ov).convert("RGB")


def srt_time(sec: float) -> str:
    ms = int(round(sec * 1000))
    return f"{ms // 3600000:02d}:{ms % 3600000 // 60000:02d}:{ms % 60000 // 1000:02d},{ms % 1000:03d}"


def split_subtitle(text: str, custom: list[str] | None) -> list[str]:
    if custom:
        return custom
    parts = [p.strip() for p in re.split(r"(?<=[.!?…])\s+|(?<=\.\.\.)\s*", text) if p and p.strip()]
    merged: list[str] = []
    for p in parts:
        if merged and len(merged[-1]) + len(p) < 26:
            merged[-1] = f"{merged[-1]} {p}"
        else:
            merged.append(p)
    return merged or [text]


# ----------------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------------

def run(ep: Episode, preview_only: bool = False) -> dict:
    print(f"=== GATE 4: TIMELINE & SAFE ZONE – {ep.id} ===")
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

    # --- scenes ---
    scenes = []
    for sc in cfg["scenes"]:
        sc2 = dict(sc)
        sc2["start"], sc2["end"] = float(sc["start"]), float(sc["end"])
        vpath = ep.resolve_asset(sc["video"]) if sc.get("video") else None
        if vpath and vpath.is_file():
            dur_s = max(0.5, sc2["end"] - sc2["start"])
            n_vf = max(2, int(round(dur_s * FPS)))
            sc2["_vreader"] = SceneVideoReader(vpath, W, H, FPS, n_vf)
            scenes.append(sc2)
            continue
        p = ep.resolve_asset(sc["image"])
        if not p.is_file():
            raise GateError(f"Thiếu ảnh cảnh: {rel(p)}")
        img = Image.open(p).convert("RGB")
        if abs(img.width / img.height - W / H) > 0.02:
            # crop giữa về 9:16 nếu ảnh lệch tỉ lệ
            tw = int(img.height * W / H)
            if tw <= img.width:
                img = img.crop(((img.width - tw) // 2, 0, (img.width - tw) // 2 + tw, img.height))
            else:
                th = int(img.width * H / W)
                img = img.crop((0, (img.height - th) // 2, img.width, (img.height - th) // 2 + th))
        sc2["_img"] = img.resize((int(W * 1.3333), int(H * 1.3333)), Image.Resampling.LANCZOS)
        scenes.append(sc2)
    scenes.sort(key=lambda s: s["start"])
    if abs(scenes[0]["start"]) > 1e-3 or abs(scenes[-1]["end"] - DUR) > 0.05:
        raise GateError(f"Cảnh phải phủ kín 0 → {DUR}s (hiện {scenes[0]['start']} → {scenes[-1]['end']}).")

    # --- overlays ---
    events: list[dict] = []

    def add(img: Image.Image, meta: dict, name: str, start: float, end: float, fade: float = 0.15):
        path = ovl_dir / f"{len(events):02d}_{name}.png"
        img.save(path)
        events.append({"id": path.stem, "start_sec": round(start, 3), "end_sec": round(end, 3), "fade_sec": fade,
                       "png_path": rel(path), "image": img, **meta})

    brand_img, brand_meta = plate_branding(cv)
    brand_img.save(ovl_dir / "branding.png")

    hk = cfg.get("hook")
    if hk:
        im, me = plate_hook(cv, hk["title"], hk.get("kicker", ""))
        add(im, me, "hook", hk.get("start", 0.3), hk.get("end", 4.5), 0.3)

    srt_entries = []
    sub_rgb = tuple(ep.channel["palette"]["subtitle_rgb"])
    for ln in tts["lines"]:
        chunks = split_subtitle(ln["text"], ln.get("subtitle"))
        s, e = ln["timeline_start_sec"], ln["timeline_end_sec"]
        total_chars = sum(len(c) for c in chunks)
        cur = s
        spk = ep.cast.get(ln["speaker"], {})
        color = tuple(spk.get("subtitle_rgb", sub_rgb))
        for c in chunks:
            dur = (e - s) * len(c) / max(total_chars, 1)
            im, me = plate_subtitle(cv, c, color, spk.get("label_short", ""))
            add(im, me, f"sub_{ln['line_id']}", cur, cur + dur, 0.1)
            srt_entries.append((cur, cur + dur, c))
            cur += dur

    for i, cb in enumerate(cfg.get("chat_bubbles", [])):
        im, me = plate_chat(cv, cb["text"], cb.get("side", "left"), cb.get("sender", ""), int(cb.get("y", 520)), cb.get("stamp", ""))
        add(im, me, f"chat{i + 1}", cb["start"], cb["end"], 0.15)

    for i, co in enumerate(cfg.get("callouts", [])):
        im, me = plate_callout(cv, co["text"], co.get("style", "danger"), int(co.get("y", 185)))
        add(im, me, f"callout{i + 1}", co["start"], co["end"], 0.2)

    rf = cfg.get("red_flags")
    if rf:
        items, action = rf["items"], rf.get("action", "")
        s, e = float(rf["start"]), float(rf["end"])
        stagger = float(rf.get("stagger_sec", 0.7))
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
        + ([round(hk.get("start", 0.3) + 1.0, 2)] if hk else [])
        + ([round(float(rf["end"]) - 0.5, 2)] if rf else [])
        + [round((ds + de) / 2, 2)]
    ))
    qa_idx = {int(round(t * FPS)): t for t in qa_times if t < DUR}

    # --- render ---
    out_mp4 = ep.timeline_video_path
    total_frames = ep.total_frames
    frame_range = sorted(qa_idx) if preview_only else range(total_frames)
    proc = None
    if not preview_only:
        print(f" -> Render {total_frames} frames ({DUR}s @ {FPS}fps) -> {out_mp4.name}")
        proc = subprocess.Popen([FFMPEG, "-y", "-v", "error", "-f", "rawvideo", "-vcodec", "rawvideo", "-s", f"{W}x{H}",
                                 "-pix_fmt", "rgb24", "-r", str(FPS), "-i", "-", "-an", "-c:v", "libx264", "-preset", "fast",
                                 "-crf", "18", "-pix_fmt", "yuv420p", str(out_mp4)], stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    previews = []
    for fi in frame_range:
        t = fi / FPS
        frame = composite_scene(scenes, t, W, H).convert("RGBA")
        for ev in events:
            if ev["start_sec"] <= t < ev["end_sec"]:
                fade = ev["fade_sec"]
                a = 1.0
                if fade > 0:
                    a = min(1.0, (t - ev["start_sec"]) / fade, (ev["end_sec"] - t) / fade)
                ov = ev["image"]
                if a < 0.99:
                    r, g, b, al = ov.split()
                    ov = Image.merge("RGBA", (r, g, b, al.point(lambda p, a=a: int(p * a))))
                frame = Image.alpha_composite(frame, ov)
        frame = Image.alpha_composite(frame, brand_img).convert("RGB")
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
            if (fi + 1) % 300 == 0:
                print(f"    ... {fi + 1}/{total_frames}")
    if proc:
        proc.stdin.close()
        err = proc.stderr.read().decode("utf-8", "replace")
        if proc.wait() != 0:
            raise GateError(f"FFmpeg lỗi: {err}")

    for sc in scenes:
        if sc.get("_vreader"):
            sc["_vreader"].close()

    overlays = [{k: v for k, v in ev.items() if k != "image"} for ev in events]
    manifest = {
        "episode_id": ep.id,
        "gate": "GATE_4_TIMELINE_SAFE_ZONE",
        "preview_only": preview_only,
        "canvas": {"width": W, "height": H, "fps": FPS, "total_frames": total_frames, "total_duration_sec": DUR},
        "safe_zone_rules": {**ep.safe, "all_overlays_compliant": all(o.get("safe_zone_compliant", True) for o in overlays)},
        "scenes": [{k: v for k, v in sc.items() if k not in ("_img", "_vframes", "_vreader")} for sc in scenes],
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
    print(f" -> {len(previews)} khung QA tại {rel(prv_dir)}")
    print(f" -> Manifest: {rel(ep.timeline_manifest_path)}")
    return manifest
