from __future__ import annotations

import asyncio

import questionary
from loguru import logger

from config import load_config
from core.engine import SpamEngine
from core.session import DiscordSession
from handlers.target_loader import load_targets
from services.rate_limiter import RateLimiter
from services.state_store import StateStore
from utils.payloads import PayloadRotator


async def _run_async() -> None:
    cfg = load_config()
    targets = load_targets(cfg.targets.source_file)
    if not targets:
        logger.error("no targets to process")
        return

    confirm = await questionary.confirm(
        f"about to DM {len(targets)} users with repeat={cfg.spam.repeat}. proceed?",
        default=False,
    ).ask_async()
    if not confirm:
        logger.info("aborted by user")
        return

    store = StateStore("state/messaged.sqlite3")
    await store.init()
    limiter = RateLimiter()
    rotator = PayloadRotator()

    session = DiscordSession(cfg.discord.token)
    try:
        client = await session.start()
        engine = SpamEngine(client, cfg, store, limiter, rotator)
        stats = await engine.run(targets)
        logger.info(f"done: {stats}")
    finally:
        await session.close()
        await store.close()


def run_cli() -> None:
    asyncio.run(_run_async())