from __future__ import annotations

from typing import Any, Dict, List

from .object_detector import ObjectDetector
from .yolo_detector import YoloPeopleDetector


class PeopleDetector(ObjectDetector):
    def __init__(self, impl: YoloPeopleDetector | None = None) -> None:
        self._impl = impl or YoloPeopleDetector()

    def detectar(self, frame: Any) -> List[Dict[str, Any]]:
        """Retorna lista de detecções padronizadas.

        Cada detecção é um dict com chaves: bbox, score, class_id, class_name.
        """
        return self._impl.detectar(frame)
