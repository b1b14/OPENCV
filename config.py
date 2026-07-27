from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import os


BASE_DIR = Path(__file__).resolve().parent


@dataclass(frozen=True, slots=True)
class AppSettings:
    app_name: str
    app_version: str
    log_level: str
    camera_source: str
    base_dir: Path
    assets_dir: Path
    camera_dir: Path
    detector_dir: Path
    tracker_dir: Path
    counter_dir: Path
    models_dir: Path
    services_dir: Path
    ui_dir: Path
    utils_dir: Path
    outputs_dir: Path
    images_output_dir: Path
    videos_output_dir: Path
    yolov11_model_path: Path
    haarcascade_model_path: Path


_SETTINGS = AppSettings(
    app_name="PeopleDetectionAI",
    app_version="0.1.0",
    log_level=os.getenv("PEOPLE_DETECTION_LOG_LEVEL", "INFO").upper(),
    camera_source=os.getenv("PEOPLE_DETECTION_CAMERA_SOURCE", "1"),
    base_dir=BASE_DIR,
    assets_dir=BASE_DIR / "assets",
    camera_dir=BASE_DIR / "camera",
    detector_dir=BASE_DIR / "detector",
    tracker_dir=BASE_DIR / "tracker",
    counter_dir=BASE_DIR / "counter",
    models_dir=BASE_DIR / "models",
    services_dir=BASE_DIR / "services",
    ui_dir=BASE_DIR / "ui",
    utils_dir=BASE_DIR / "utils",
    outputs_dir=BASE_DIR / "outputs",
    images_output_dir=BASE_DIR / "outputs" / "images",
    videos_output_dir=BASE_DIR / "outputs" / "videos",
    yolov11_model_path=BASE_DIR / "models" / "yolov11n.pt",
    haarcascade_model_path=BASE_DIR / "models" / "haarcascade_frontalface_default.xml",
)


def get_settings() -> AppSettings:
    return _SETTINGS
