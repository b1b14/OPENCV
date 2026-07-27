from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Dashboard:
    titulo: str = "PeopleDetectionAI"
