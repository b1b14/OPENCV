from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class Camera(ABC):
    @abstractmethod
    def abrir(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def ler_frame(self) -> tuple[bool, Any]:
        raise NotImplementedError

    @abstractmethod
    def liberar(self) -> None:
        raise NotImplementedError
