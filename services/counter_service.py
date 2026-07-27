from __future__ import annotations

from typing import Any

from counter.people_counter import PeopleCounter


class CounterService:
    def __init__(self, counter: PeopleCounter) -> None:
        self._counter = counter

    def processar(self, tracked_objects: list[Any]) -> int:
        return self._counter.contar(tracked_objects)
