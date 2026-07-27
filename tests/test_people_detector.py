from __future__ import annotations

import unittest
from unittest.mock import MagicMock, patch

import numpy as np

from detector.people_detector import PeopleDetector


class TestPeopleDetector(unittest.TestCase):
    def test_people_detector_delega_para_yolo(self) -> None:
        fake_frame = np.zeros((480, 640, 3), dtype=np.uint8)

        fake_impl = MagicMock()
        fake_impl.detectar.return_value = [
            {"bbox": (10, 20, 100, 200), "score": 0.9, "class_id": 0, "class_name": "person"}
        ]

        detector = PeopleDetector(impl=fake_impl)
        detections = detector.detectar(fake_frame)

        fake_impl.detectar.assert_called_once()
        self.assertIsInstance(detections, list)
        self.assertEqual(detections[0]["class_name"], "person")

    def test_yolo_wrapper_called_when_no_impl(self) -> None:
        # Apenas valida que _carregar_modelo é chamado; usamos patch para substituir ultralytics.YOLO
        # Evita importar 'ultralytics' durante o teste; mockamos o carregador interno
        mock_model = MagicMock()
        mock_result = MagicMock()
        mock_box = MagicMock()
        mock_box.xyxy.tolist.return_value = [[10.0, 20.0, 100.0, 200.0]]
        mock_box.conf.tolist.return_value = [0.85]
        mock_box.cls.tolist.return_value = [0]
        mock_result.boxes = [mock_box]
        mock_model.predict.return_value = [mock_result]

        def fake_load(self) -> None:
            setattr(self, "_model", mock_model)

        with patch("detector.yolo_detector.YoloPeopleDetector._carregar_modelo", new=fake_load):
            detector = PeopleDetector()
            import numpy as np

            frame = np.zeros((480, 640, 3), dtype=np.uint8)
            detections = detector.detectar(frame)

            self.assertIsInstance(detections, list)
            self.assertGreaterEqual(len(detections), 1)


if __name__ == "__main__":
    unittest.main()
