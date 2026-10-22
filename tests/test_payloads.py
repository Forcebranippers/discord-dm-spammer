from __future__ import annotations

from pathlib import Path

from utils.payloads import PayloadRotator


def test_rotates_through_pool(tmp_path: Path) -> None:
    f = tmp_path / "payloads.txt"
    f.write_text("a\nb\nc\n", encoding="utf-8")
    r = PayloadRotator(f, rotate=True)
    assert [r.next() for _ in range(4)] == ["a", "b", "c", "a"]


def test_no_rotate_returns_first(tmp_path: Path) -> None:
    f = tmp_path / "payloads.txt"
    f.write_text("first\nsecond\n", encoding="utf-8")
    r = PayloadRotator(f, rotate=False)
    assert r.next() == "first"
    assert r.next() == "first"
</final_file_content>