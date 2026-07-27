from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class ObjectDetector(ABC):
    @abstractmethod
    def detectar(self, frame: Any) -> list[Any]:
        raise NotImplementedError
