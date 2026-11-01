# -*- coding: utf-8 -*-
"""
Core utilities for the VCH Scam-Exposé production engine.

Kế thừa hạ tầng 6-Gate từ dự án borderWarSW779, nhưng tổng quát hóa:
mọi thông số của một tập phim nằm trong `factory/materialAndDraft/<EP>/episode.json`,
không còn hardcode timestamp / câu thoại / đường dẫn trong script.
"""
from __future__ import annotations

import json
import os
import shutil
import sys
from pathlib import Path
from typing import Any

ENGINE_DIR = Path(__file__).resolve().parent
FACTORY_DIR = ENGINE_DIR.parent
PROJECT_ROOT = FACTORY_DIR.parent
HARNESS_DIR = PROJECT_ROOT / "00_HARNESS_GUIDELINES"
CAST_FILE = PROJECT_ROOT / "02_CAST" / "cast.json"
CHANNEL_CONFIG_FILE = ENGINE_DIR / "channel_config.json"
POLICY_WORDLIST_FILE = HARNESS_DIR / "policy_wordlists.json"
TEMPLATE_DIR = FACTORY_DIR / "_templates" / "EPISODE"
RENDERED_DIR = PROJECT_ROOT / "06_RENDERED_SHORTS"

# HaizFlow runtime (đã dùng ở dự án 779) – ưu tiên nếu có, fallback PATH.
HAIZFLOW_ROOT = Path(os.environ.get("HAIZFLOW_ROOT", r"C:\projects\HaizFlow-main"))


def utf8_stdout() -> None:
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")


def find_bin(name: str) -> str:
    """Locate ffmpeg/ffprobe: HaizFlow runtime first, then system PATH."""
    candidate = HAIZFLOW_ROOT / "runtime" / "bin" / f"{name}.exe"
    if candidate.is_file():
        return str(candidate)
    found = shutil.which(name)
    if found:
        return found
    raise FileNotFoundError(f"Không tìm thấy '{name}'. Cài FFmpeg hoặc đặt biến HAIZFLOW_ROOT.")


FFMPEG = find_bin("ffmpeg")
try:
    FFPROBE: str | None = find_bin("ffprobe")
except FileNotFoundError:
    FFPROBE = None


def load_json(path: Path) -> Any:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def save_json(path: Path, data: Any) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def rel(path: Path) -> str:
    """Project-relative POSIX path (for manifests & reports)."""
    try:
        return Path(path).resolve().relative_to(PROJECT_ROOT).as_posix()
    except ValueError:
        return Path(path).as_posix()


def file_link(path: Path) -> str:
    return "file:///" + Path(path).resolve().as_posix()


class GateError(RuntimeError):
    """Raised when a gate's preconditions or checks fail."""


class Episode:
    """Resolved view over one episode's config, folders and shared channel settings."""

    def __init__(self, episode_id: str):
        self.id = episode_id
        self.material_dir = FACTORY_DIR / "materialAndDraft" / episode_id
        self.staging_dir = FACTORY_DIR / "staging" / episode_id
        self.production_dir = FACTORY_DIR / "production" / episode_id
        self.config_path = self.material_dir / "episode.json"
        if not self.config_path.is_file():
            raise GateError(f"Chưa có {rel(self.config_path)}. Tạo tập bằng: run.py new {episode_id}")
        self.cfg: dict = load_json(self.config_path)
        self.channel: dict = load_json(CHANNEL_CONFIG_FILE)
        self.cast: dict = load_json(CAST_FILE).get("speakers", {}) if CAST_FILE.is_file() else {}
        self.policy: dict = load_json(POLICY_WORDLIST_FILE) if POLICY_WORDLIST_FILE.is_file() else {}

    # ---- canvas -----------------------------------------------------------
    @property
    def canvas(self) -> dict:
        return self.channel["canvas"]

    @property
    def width(self) -> int:
        return int(self.canvas["width"])

    @property
    def height(self) -> int:
        return int(self.canvas["height"])

    @property
    def fps(self) -> int:
        return int(self.canvas["fps"])

    @property
    def duration(self) -> float:
        return float(self.cfg.get("duration_sec", self.channel["format"]["default_duration_sec"]))

    @property
    def total_frames(self) -> int:
        return int(round(self.duration * self.fps))

    @property
    def safe(self) -> dict:
        return self.channel["safe_zone"]

    # ---- folders ----------------------------------------------------------
    @property
    def assets_dir(self) -> Path:
        return self.material_dir / "assets"

    @property
    def tts_dir(self) -> Path:
        return self.material_dir / "audio" / "tts"

    @property
    def sfx_dir(self) -> Path:
        return self.material_dir / "audio" / "sfx"

    @property
    def bgm_dir(self) -> Path:
        return self.material_dir / "audio" / "bgm"

    @property
    def mix_dir(self) -> Path:
        return self.material_dir / "audio" / "mix"

    @property
    def clearance_dir(self) -> Path:
        return self.material_dir / "clearance"

    # ---- naming -----------------------------------------------------------
    @property
    def slug(self) -> str:
        return self.cfg.get("slug", "Untitled")

    @property
    def file_stem(self) -> str:
        return f"{self.id}_{self.slug}_{int(round(self.duration))}s"

    @property
    def title(self) -> str:
        return self.cfg.get("title", self.id)

    # ---- manifests --------------------------------------------------------
    @property
    def tts_manifest_path(self) -> Path:
        return self.tts_dir / "tts_manifest_gate2.json"

    @property
    def audio_manifest_path(self) -> Path:
        return self.mix_dir / "audio_manifest_gate3.json"

    @property
    def master_audio_path(self) -> Path:
        return self.mix_dir / f"master_audio_{self.id}.wav"

    @property
    def timeline_manifest_path(self) -> Path:
        return self.staging_dir / "timeline_manifest_gate4.json"

    @property
    def timeline_video_path(self) -> Path:
        return self.staging_dir / "timeline_video_gate4.mp4"

    @property
    def srt_path(self) -> Path:
        return self.staging_dir / "subtitles" / f"{self.id}.srt"

    @property
    def staging_mp4_path(self) -> Path:
        return self.staging_dir / f"{self.file_stem}_staging.mp4"

    @property
    def qa_json_path(self) -> Path:
        return self.staging_dir / "qa_audit_report_gate5.json"

    @property
    def human_signoff_path(self) -> Path:
        return self.clearance_dir / "human_qa_signoff.json"

    def resolve_asset(self, p: str) -> Path:
        """Resolve a path from episode.json: relative to the episode folder, else project root."""
        cand = self.material_dir / p
        if cand.exists():
            return cand
        cand2 = PROJECT_ROOT / p
        if cand2.exists():
            return cand2
        return cand

    def speaker(self, speaker_id: str) -> dict:
        if speaker_id not in self.cast:
            raise GateError(f"Speaker '{speaker_id}' chưa khai báo trong 02_CAST/cast.json")
        return self.cast[speaker_id]
