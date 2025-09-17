from __future__ import annotations

import re

from ariadne.cli import run


def test_cli_greeting(capsys):
    code = run(["--name", "Dani"])
    captured = capsys.readouterr()
    assert code == 0
    assert re.search(r"Hello, Dani! I'm Ariadne\.", captured.out)
