from __future__ import annotations

from pydantic import BaseModel, Field


class Target(BaseModel):
    user_id: int = Field(..., gt=0)
    raw: str
    display_name: str | None = None

    def __repr__(self) -> str:  # pragma: no cover
        return f"<Target id={self.user_id} raw={self.raw!r}>"