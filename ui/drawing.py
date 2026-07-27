from __future__ import annotations

from typing import Any, Dict, List

import cv2

from utils.colors import Colors


class Drawing:
    """Desenha detecções (bounding boxes e scores) em um frame."""

    def __init__(self, colors: Colors | None = None) -> None:
        self._colors = colors or Colors()

    def desenhar_deteccoes(self, frame: Any, detections: List[Dict[str, Any]]) -> Any:
        """Desenha bounding boxes e scores para cada detecção.

        Args:
            frame: imagem (numpy array) onde desenhar.
            detections: lista de dicts com chaves bbox, score, class_name.

        Returns:
            frame com desenhos aplicados.
        """
        resultado = frame.copy()

        for det in detections:
            bbox = det.get("bbox")
            score = det.get("score", 0.0)
            class_name = det.get("class_name", "Unknown")

            if bbox is None:
                continue

            x1, y1, x2, y2 = bbox

            # Desenhar bounding box (verde)
            cv2.rectangle(resultado, (x1, y1), (x2, y2), self._colors.verde, 2)

            # Desenhar label com score (fundo vermelho, texto branco)
            label = f"{class_name} {score:.2f}"
            (text_w, text_h), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 2)
            cv2.rectangle(
                resultado,
                (x1, y1 - text_h - 10),
                (x1 + text_w + 5, y1),
                self._colors.vermelho,
                -1,
            )
            cv2.putText(
                resultado,
                label,
                (x1 + 2, y1 - 5),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (255, 255, 255),
                2,
            )

        return resultado

    def desenhar(self, frame: Any) -> Any:
        """Compatibilidade com interface anterior; retorna frame sem modificação."""
        return frame
