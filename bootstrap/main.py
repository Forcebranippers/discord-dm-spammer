from __future__ import annotations

import sys

from loguru import logger

from config import load_config
from handlers.cli_handler import run_cli
from utils.console import banner


def _setup_logging() -> None:
    try:
        cfg = load_config()
        logger.remove()
        logger.add(sys.stderr, level=cfg.logging.level)
        logger.add(cfg.logging.file, level="DEBUG", rotation="5 MB", retention=3)
    except FileNotFoundError:
        logger.remove()
        logger.add(sys.stderr, level="INFO")
        logger.warning("config not found — falling back to defaults")


def main() -> int:
    banner()
    _setup_logging()
    try:
        run_cli()
    except KeyboardInterrupt:
        logger.warning("interrupted by user")
        return 130
    return 0


if __name__ == "__main__":
    raise SystemExit(main())