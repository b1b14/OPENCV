from __future__ import annotations

from typing import Any

from .object_detector import ObjectDetector


class FaceDetector(ObjectDetector):
    def detectar(self, frame: Any) -> list[Any]:
        raise NotImplementedError("Sprint 5 implementará a detecção facial")
