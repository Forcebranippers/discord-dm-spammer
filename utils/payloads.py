from __future__ import annotations

import itertools
import random
from pathlib import Path


_DEFAULT_PAYLOADS = [
    "hey, saw your profile — got a sec?",
    "yo, quick question for you",
    "sup — you around?",
    "hey! been meaning to ask you something",
]


class PayloadRotator:
    """Cycles through message templates. Reads payloads.txt if present."""

    def __init__(self, path: str | Path = "payloads.txt", rotate: bool = True) -> None:
        p = Path(path)
        if p.exists():
            lines = [
                ln.strip()
                for ln in p.read_text(encoding="utf-8").splitlines()
                if ln.strip() and not ln.startswith("#")
            ]
            self._pool = lines or list(_DEFAULT_PAYLOADS)
        else:
            self._pool = list(_DEFAULT_PAYLOADS)
        self._rotate = rotate
        self._cycle = itertools.cycle(self._pool)

    def next(self) -> str:
        if not self._rotate:
            return self._pool[0]
        return next(self._cycle)

    def random(self) -> str:
        return random.choice(self._pool)