from __future__ import annotations

import unittest
from unittest.mock import MagicMock, patch

from camera.droidcam import DroidCamCamera, DroidCamConfig, normalizar_fonte_video


class TestDroidCamCamera(unittest.TestCase):
    def test_normalizar_fonte_video_converte_indice_em_inteiro(self) -> None:
        self.assertEqual(normalizar_fonte_video("1"), 1)

    def test_normalizar_fonte_video_mantem_url(self) -> None:
        self.assertEqual(
            normalizar_fonte_video("http://192.168.1.10:8080/video"),
            "http://192.168.1.10:8080/video",
        )

    def test_abrir_lanca_erro_quando_video_capture_falha(self) -> None:
        mock_capture = MagicMock()
        mock_capture.isOpened.return_value = False

        with patch("camera.droidcam.cv2.VideoCapture", return_value=mock_capture):
            camera = DroidCamCamera(DroidCamConfig(source="1"))

            with self.assertRaises(RuntimeError):
                camera.abrir()

    def test_liberar_descarta_recursos_quando_capture_existe(self) -> None:
        mock_capture = MagicMock()
        mock_capture.isOpened.return_value = True

        with patch("camera.droidcam.cv2.VideoCapture", return_value=mock_capture):
            camera = DroidCamCamera(DroidCamConfig(source="1"))
            camera.abrir()
            camera.liberar()

        mock_capture.release.assert_called_once()


if __name__ == "__main__":
    unittest.main()
