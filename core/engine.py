from __future__ import annotations

import asyncio
import random

import discord
from loguru import logger

from config import AppConfig
from models.target import Target
from services.rate_limiter import RateLimiter
from services.state_store import StateStore
from utils.payloads import PayloadRotator


class SpamEngine:
    """Orchestrates the DM loop across a list of targets."""

    def __init__(
        self,
        client: discord.Client,
        cfg: AppConfig,
        store: StateStore,
        limiter: RateLimiter,
        rotator: PayloadRotator,
    ) -> None:
        self.client = client
        self.cfg = cfg
        self.store = store
        self.limiter = limiter
        self.rotator = rotator
        self._consecutive_failures = 0

    async def _send_one(self, target: Target, body: str) -> bool:
        try:
            user = await self.client.fetch_user(target.user_id)
            await user.send(body)
            logger.info(f"sent -> {target.user_id} ({len(body)} chars)")
            return True
        except discord.Forbidden:
            logger.warning(f"forbidden -> {target.user_id} (closed DMs?)")
        except discord.HTTPException as exc:
            logger.error(f"http {exc.status} -> {target.user_id}: {exc.text}")
        except Exception as exc:  # noqa: BLE001
            logger.exception(f"unexpected error -> {target.user_id}: {exc}")
        return False

    async def run(self, targets: list[Target]) -> dict[str, int]:
        stats = {"ok": 0, "failed": 0, "skipped": 0}
        for target in targets:
            if self.cfg.targets.skip_messaged and self.store.was_messaged(target.user_id):
                stats["skipped"] += 1
                continue
            for _ in range(self.cfg.spam.repeat):
                payload = self.rotator.next()
                ok = await self._send_one(target, payload)
                if ok:
                    stats["ok"] += 1
                    self._consecutive_failures = 0
                    self.store.mark_messaged(target.user_id)
                else:
                    stats["failed"] += 1
                    self._consecutive_failures += 1
                    if self._consecutive_failures >= self.cfg.spam.max_consecutive_failures:
                        logger.error("aborting: too many consecutive failures")
                        return stats
                jitter = random.uniform(0, self.cfg.discord.jitter_seconds)
                await self.limiter.wait(self.cfg.discord.delay_seconds + jitter)
        return stats