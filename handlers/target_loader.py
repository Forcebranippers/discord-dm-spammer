from __future__ import annotations

from pathlib import Path

from loguru import logger

from models.target import Target


def _parse_line(line: str) -> Target | None:
    raw = line.strip()
    if not raw or raw.startswith("#"):
        return None
    if raw.isdigit():
        return Target(user_id=int(raw), raw=raw)
    if raw.startswith("<@") and raw.endswith(">"):
        inner = raw[2:-1].lstrip("!")
        if inner.isdigit():
            return Target(user_id=int(inner), raw=raw)
    logger.warning(f"skipping unparseable target: {raw!r}")
    return None


def load_targets(path: str | Path) -> list[Target]:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"target file missing: {p}")
    targets: list[Target] = []
    for line in p.read_text(encoding="utf-8").splitlines():
        t = _parse_line(line)
        if t is not None:
            targets.append(t)
    logger.info(f"loaded {len(targets)} targets from {p}")
    return targets