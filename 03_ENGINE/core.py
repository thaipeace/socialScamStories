# -*- coding: utf-8 -*-
"""
Shared Core Service (`03_ENGINE/core.py`) dùng chung cho cả hai nhà máy:
  - `factory619` (Short dọc 9:16 – 1080x1920, ~55–70s)
  - `factory196` (Phim dài ngang 16:9 – 1920x1080, từ 5 phút / 300s trở lên)

Mọi thông số định dạng đặc thù của từng nhà máy nằm trong `<factory>/_engine/channel_config.json`,
còn thông số của từng tập phim nằm trong `<factory>/materialAndDraft/<EP>/episode.json`.
"""
from __future__ import annotations

import json
import os
import shutil
import sys
from pathlib import Path
from typing import Any

SERVICE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SERVICE_DIR.parent
HARNESS_DIR = PROJECT_ROOT / "00_HARNESS_GUIDELINES"
CAST_FILE = PROJECT_ROOT / "02_CAST" / "cast.json"
POLICY_WORDLIST_FILE = HARNESS_DIR / "policy_wordlists.json"

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


def resolve_factory_dir(factory: str | Path | None = None) -> Path:
    """Resolve factory directory from a path, short code ('196', '619', 'factory196', 'factory619'), or env."""
    if factory is None:
        env_f = os.environ.get("VCH_FACTORY_DIR")
        if env_f:
            return Path(env_f).resolve()
        raise GateError("Chưa chỉ định nhà máy (factory196 hoặc factory619).")
    if isinstance(factory, Path):
        return factory.resolve()
    s = str(factory).strip()
    if s in ("196", "factory196", "16:9", "19:6"):
        return PROJECT_ROOT / "factory196"
    if s in ("619", "factory619", "9:16", "6:19"):
        return PROJECT_ROOT / "factory619"
    cand = Path(s)
    if cand.is_dir():
        return cand.resolve()
    cand2 = PROJECT_ROOT / s
    if cand2.is_dir():
        return cand2.resolve()
    raise GateError(f"Không tìm thấy thư mục nhà máy: {factory}")


class Episode:
    """Resolved view over one episode's config, folders and factory channel settings."""

    def __init__(self, episode_id: str, factory_dir: str | Path | None = None):
        self.id = episode_id
        self.factory_dir = resolve_factory_dir(factory_dir)
        self.factory_name = self.factory_dir.name
        self.channel_config_file = self.factory_dir / "_engine" / "channel_config.json"
        self.template_dir = self.factory_dir / "_templates" / "EPISODE"
        self.material_dir = self.factory_dir / "materialAndDraft" / episode_id
        self.staging_dir = self.factory_dir / "staging" / episode_id
        self.production_dir = self.factory_dir / "production" / episode_id
        self.config_path = self.material_dir / "episode.json"
        if not self.config_path.is_file():
            raise GateError(
                f"Chưa có {rel(self.config_path)}. Tạo tập bằng: "
                f"python {self.factory_name}/_engine/run.py new {episode_id}"
            )
        self.cfg: dict = load_json(self.config_path)
        self.channel: dict = load_json(self.channel_config_file)
        self.cast: dict = load_json(CAST_FILE).get("speakers", {}) if CAST_FILE.is_file() else {}
        self.policy: dict = load_json(POLICY_WORDLIST_FILE) if POLICY_WORDLIST_FILE.is_file() else {}

    # ---- canvas & format --------------------------------------------------
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
    def is_landscape(self) -> bool:
        return self.width > self.height

    @property
    def aspect_label(self) -> str:
        return self.canvas.get("aspect_ratio", "16:9" if self.is_landscape else "9:16")

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

    @property
    def rendered_dir(self) -> Path:
        rdir = self.channel["format"].get(
            "rendered_dir",
            "06_RENDERED_VIDEOS" if self.is_landscape else "06_RENDERED_SHORTS",
        )
        return PROJECT_ROOT / rdir

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


class PreventSleep:
    """Context manager báo cho Windows (SetThreadExecutionState) giữ CPU/hệ thống thức
    trong suốt lúc đang thu TTS, mix âm thanh hoặc render video; tự nhả về bình thường khi xong."""

    ES_CONTINUOUS = 0x80000000
    ES_SYSTEM_REQUIRED = 0x00000001
    ES_AWAYMODE_REQUIRED = 0x00000040

    def __enter__(self):
        if sys.platform == "win32":
            try:
                import ctypes
                ctypes.windll.kernel32.SetThreadExecutionState(
                    self.ES_CONTINUOUS | self.ES_SYSTEM_REQUIRED | self.ES_AWAYMODE_REQUIRED
                )
            except Exception:
                pass
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if sys.platform == "win32":
            try:
                import ctypes
                ctypes.windll.kernel32.SetThreadExecutionState(self.ES_CONTINUOUS)
            except Exception:
                pass
        return False


