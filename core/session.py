from __future__ import annotations

import discord
from loguru import logger


class DiscordSession:
    """Thin wrapper around a self-bot client with login/logout helpers."""

    def __init__(self, token: str) -> None:
        self.token = token
        self.client = discord.Client()
        self._ready_event = None

    async def start(self) -> discord.Client:
        logger.info("logging in as self-bot")
        await self.client.login(self.token)
        await self.client.connect()
        if not self.client.is_ready():
            raise RuntimeError("client failed to become ready")
        me = self.client.user
        logger.success(f"authenticated as {me} ({me.id})")
        return self.client

    async def close(self) -> None:
        if not self.client.is_closed():
            await self.client.close()
            logger.info("session closed")