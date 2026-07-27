from __future__ import annotations

from typing import Any, Dict, List
from pathlib import Path

from config import get_settings


class YoloPeopleDetector:
    """Wrapper minimalista para o modelo YOLO (Ultralytics).

    Responsabilidade: carregar o peso do modelo a partir de configuração e
    expor um método `detectar(frame)` que retorna uma lista de detecções no formato:
    [{"bbox": (x1, y1, x2, y2), "score": float, "class_id": int, "class_name": str}, ...]
    """

    def __init__(self, model_path: Path | str | None = None) -> None:
        self._model_path = model_path or get_settings().yolov11_model_path
        self._model = None

    def _carregar_modelo(self) -> None:
        try:
            from ultralytics import YOLO
        except Exception as exc:  # pragma: no cover - ambiente de dev pode não ter ultralytics
            raise RuntimeError("Pacote 'ultralytics' não está disponível. Instale via pip.") from exc

        self._model = YOLO(str(self._model_path))

    def detectar(self, frame: Any) -> List[Dict[str, Any]]:
        if self._model is None:
            self._carregar_modelo()

        # O método `predict` do ultralytics aceita frames (numpy array)
        results = self._model.predict(source=frame, imgsz=640, device='cpu', conf=0.25)

        detections: List[Dict[str, Any]] = []
        for res in results:
            boxes = getattr(res, 'boxes', None)
            if boxes is None:
                continue

            for box in boxes:
                xyxy = box.xyxy.tolist()[0]  # [[x1, y1, x2, y2]]
                score = float(box.conf.tolist()[0])
                cls = int(box.cls.tolist()[0])
                # Ultralytics não fornece nome de classe direto aqui sem a lista
                detections.append(
                    {
                        "bbox": (int(xyxy[0]), int(xyxy[1]), int(xyxy[2]), int(xyxy[3])),
                        "score": score,
                        "class_id": cls,
                        "class_name": str(cls),
                    }
                )

        return detections
