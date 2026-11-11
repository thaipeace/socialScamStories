# -*- coding: utf-8 -*-
"""Thin CLI entrypoint cho nhà máy Short 9:16 (`factory619`) – ủy quyền toàn bộ logic cho `03_ENGINE/`."""
from __future__ import annotations

import sys
from pathlib import Path

FACTORY_DIR = Path(__file__).resolve().parent.parent
SERVICE_DIR = FACTORY_DIR.parent / "03_ENGINE"
sys.path.insert(0, str(SERVICE_DIR))

from cli import main  # noqa: E402

if __name__ == "__main__":
    main(default_factory=FACTORY_DIR)
