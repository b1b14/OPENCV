from __future__ import annotations

from .face_detector import FaceDetector
from .people_detector import PeopleDetector


class DetectorFactory:
    @staticmethod
    def criar_detector_de_pessoas() -> PeopleDetector:
        return PeopleDetector()

    @staticmethod
    def criar_detector_facial() -> FaceDetector:
        return FaceDetector()
