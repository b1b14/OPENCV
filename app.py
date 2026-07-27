from __future__ import annotations

import cv2

from camera.droidcam import DroidCamCamera, DroidCamConfig
from detector.detector_factory import DetectorFactory
from services.detection_service import DetectionService
from ui.drawing import Drawing
from config import get_settings
from utils.logger import configurar_logger


def executar_aplicacao() -> None:
    settings = get_settings()
    logger = configurar_logger(settings.log_level)
    camera = DroidCamCamera(DroidCamConfig(source=settings.camera_source))
    detector = DetectorFactory.criar_detector_de_pessoas()
    detection_service = DetectionService(detector)
    drawing = Drawing()

    logger.info("%s iniciado com sucesso", settings.app_name)
    logger.info("Versão: %s", settings.app_version)

    try:
        camera.abrir()
        logger.info("Captura de vídeo iniciada a partir de %s", settings.camera_source)

        while True:
            sucesso, frame = camera.ler_frame()
            if not sucesso or frame is None:
                logger.warning("Falha ao ler frame da câmera")
                continue

            detections = detection_service.processar(frame)
            frame_com_deteccoes = drawing.desenhar_deteccoes(frame, detections)

            cv2.imshow("PeopleDetectionAI - Captura e Detecção", frame_com_deteccoes)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    except RuntimeError as erro:
        logger.error("%s", erro)
    finally:
        camera.liberar()
        cv2.destroyAllWindows()
        logger.info("Aplicação finalizada com segurança")


def main() -> None:
    executar_aplicacao()


if __name__ == "__main__":
    main()