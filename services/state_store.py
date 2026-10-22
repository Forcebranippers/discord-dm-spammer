from __future__ import annotations

from pathlib import Path

import aiosqlite


_SCHEMA = """
CREATE TABLE IF NOT EXISTS messaged (
    user_id INTEGER PRIMARY KEY,
    first_sent_at TEXT NOT NULL DEFAULT (datetime('now')),
    last_sent_at TEXT NOT NULL DEFAULT (datetime('now'))
);
"""


class StateStore:
    def __init__(self, path: str | Path) -> None:
        self.path = Path(path)
        self._db: aiosqlite.Connection | None = None

    async def init(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._db = await aiosqlite.connect(self.path)
        await self._db.executescript(_SCHEMA)
        await self._db.commit()

    def was_messaged(self, user_id: int) -> bool:
        # synchronous fast-path so the engine doesn't await per-target
        import sqlite3

        with sqlite3.connect(self.path) as conn:
            row = conn.execute(
                "SELECT 1 FROM messaged WHERE user_id = ?", (user_id,)
            ).fetchone()
        return row is not None

    def mark_messaged(self, user_id: int) -> None:
        import sqlite3

        with sqlite3.connect(self.path) as conn:
            conn.execute(
                "INSERT INTO messaged(user_id) VALUES(?) "
                "ON CONFLICT(user_id) DO UPDATE SET "
                "last_sent_at = datetime('now')",
                (user_id,),
            )
            conn.commit()

    async def close(self) -> None:
        if self._db is not None:
            await self._db.close()
            self._db = None