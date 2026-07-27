from __future__ import annotations

from typing import Any

from tracker.deepsort_tracker import DeepSORTTracker


class TrackingService:
    def __init__(self, tracker: DeepSORTTracker) -> None:
        self._tracker = tracker

    def processar(self, detections: list[Any]) -> list[Any]:
        return self._tracker.rastrear(detections)
