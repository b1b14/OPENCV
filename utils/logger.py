from __future__ import annotations

import logging


def configurar_logger(nivel: str) -> logging.Logger:
    logging.basicConfig(
        level=getattr(logging, nivel, logging.INFO),
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )
    return logging.getLogger("PeopleDetectionAI")
