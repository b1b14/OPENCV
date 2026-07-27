from __future__ import annotations

from typing import Any, Dict, List

from detector.object_detector import ObjectDetector


class DetectionService:
    """Serviço de detecção: coordena detector e retorna detecções normalizadas."""

    def __init__(self, detector: ObjectDetector) -> None:
        self._detector = detector

    def processar(self, frame: Any) -> List[Dict[str, Any]]:
        """Processa frame e retorna lista de detecções.

        Cada detecção é um dict com: bbox, score, class_id, class_name.
        """
        return self._detector.detectar(frame)
