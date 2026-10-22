from __future__ import annotations

import tomllib
from pathlib import Path
from typing import Any

from pydantic import BaseModel, Field


class DiscordSection(BaseModel):
    token: str
    delay_seconds: float = Field(default=4.5, ge=0.5)
    jitter_seconds: float = Field(default=2.0, ge=0.0)


class SpamSection(BaseModel):
    repeat: int = Field(default=1, ge=1, le=50)
    rotate_payloads: bool = True
    max_consecutive_failures: int = Field(default=5, ge=1)


class TargetsSection(BaseModel):
    source_file: str = "targets.txt"
    skip_messaged: bool = True


class LoggingSection(BaseModel):
    level: str = "INFO"
    file: str = "logs/spammer.log"


class AppConfig(BaseModel):
    discord: DiscordSection
    spam: SpamSection = SpamSection()
    targets: TargetsSection = TargetsSection()
    logging: LoggingSection = LoggingSection()


def load_config(path: str | Path = "config/settings.toml") -> AppConfig:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(
            f"config not found at {p}. copy config/settings.example.toml first."
        )
    with p.open("rb") as fh:
        raw: dict[str, Any] = tomllib.load(fh)
    return AppConfig(**raw)