from __future__ import annotations

from time import perf_counter


class FPSCounter:
    def __init__(self) -> None:
        self._inicio = perf_counter()
        self._quadros = 0

    def incrementar(self) -> None:
        self._quadros += 1

    def calcular(self) -> float:
        tempo_decorrido = perf_counter() - self._inicio
        if tempo_decorrido <= 0:
            return 0.0
        return self._quadros / tempo_decorrido
