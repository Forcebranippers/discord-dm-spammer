from __future__ import annotations

import asyncio
import time


class RateLimiter:
    """Enforces a minimum gap between outbound requests."""

    def __init__(self) -> None:
        self._last_call: float = 0.0

    async def wait(self, seconds: float) -> None:
        elapsed = time.monotonic() - self._last_call
        remaining = seconds - elapsed
        if remaining > 0:
            await asyncio.sleep(remaining)
        self._last_call = time.monotonic()