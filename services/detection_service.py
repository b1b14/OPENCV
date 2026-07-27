from __future__ import annotations

from typing import Any

from detector.object_detector import ObjectDetector


class DetectionService:
    def __init__(self, detector: ObjectDetector) -> None:
        self._detector = detector

    def processar(self, frame: Any) -> list[Any]:
        return self._detector.detectar(frame)
