from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Geometry:
    x: int
    y: int
    largura: int
    altura: int
