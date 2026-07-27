from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Colors:
    verde: tuple[int, int, int] = (0, 255, 0)
    vermelho: tuple[int, int, int] = (0, 0, 255)
    azul: tuple[int, int, int] = (255, 0, 0)
