from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import cv2

from .camera import Camera


@dataclass(frozen=True, slots=True)
class DroidCamConfig:
    source: str


def normalizar_fonte_video(source: str) -> int | str:
    source_normalizada = source.strip()
    if not source_normalizada:
        raise ValueError("A fonte de vídeo não pode estar vazia")

    if source_normalizada.isdigit():
        return int(source_normalizada)

    return source_normalizada


class DroidCamCamera(Camera):
    def __init__(self, config: DroidCamConfig) -> None:
        self._config = config
        self._capture: Any = None

    def abrir(self) -> None:
        fonte_video = normalizar_fonte_video(self._config.source)
        self._capture = cv2.VideoCapture(fonte_video)

        if not self._capture.isOpened():
            self._capture = None
            raise RuntimeError(f"Não foi possível abrir a fonte de vídeo: {self._config.source}")

    def ler_frame(self) -> tuple[bool, Any]:
        if self._capture is None:
            return False, None

        return self._capture.read()

    def liberar(self) -> None:
        if self._capture is not None:
            self._capture.release()
            self._capture = None
