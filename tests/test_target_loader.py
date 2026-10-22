from __future__ import annotations

from pathlib import Path

from handlers.target_loader import load_targets


def test_parses_plain_ids(tmp_path: Path) -> None:
    f = tmp_path / "targets.txt"
    f.write_text("123456789\n# a comment\n\n987654321\n", encoding="utf-8")
    targets = load_targets(f)
    assert [t.user_id for t in targets] == [123456789, 987654321]


def test_parses_mentions(tmp_path: Path) -> None:
    f = tmp_path / "targets.txt"
    f.write_text("<@!555>\n<@666>\n", encoding="utf-8")
    targets = load_targets(f)
    assert [t.user_id for t in targets] == [555, 666]


def test_skips_garbage(tmp_path: Path) -> None:
    f = tmp_path / "targets.txt"
    f.write_text("not-an-id\n111\n", encoding="utf-8")
    targets = load_targets(f)
    assert len(targets) == 1
    assert targets[0].user_id == 111