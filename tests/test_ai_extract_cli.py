"""Offline CLI regression for scripts/test_ai_extract.py (Round 14 S05).

The script is a unittest entry point (``if __name__ == '__main__': unittest.main()``),
so the CLI contract is: running it as a program exits 0, reports OK, and
needs no network or credentials. Both tests scrub credential env vars, matching
conftest's offline fixture, and the second additionally disables sockets.
"""

import os
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = REPO_ROOT / "scripts" / "test_ai_extract.py"

CREDENTIAL_VARS = (
    "AI_PROVIDER", "GROQ_API_KEY", "GEMINI_API_KEY", "GOOGLE_API_KEY",
    "GEMINI_MODEL", "GEMINI_CLI", "GMAIL_USER", "GMAIL_APP_PASSWORD",
    "JSOSIF_APPROVED_SEND",
)


def _scrubbed_env():
    env = dict(os.environ)
    for name in CREDENTIAL_VARS:
        env.pop(name, None)
    return env


def test_cli_exits_zero_and_reports_ok():
    result = subprocess.run(
        [sys.executable, str(SCRIPT), "-v"],
        cwd=REPO_ROOT, env=_scrubbed_env(),
        capture_output=True, text=True, timeout=120,
    )
    output = result.stdout + result.stderr
    assert result.returncode == 0, output[-2000:]
    assert "OK" in output
    assert re.search(r"Ran \d+ tests?", output), output[-2000:]
    assert "Traceback" not in output


def test_cli_succeeds_with_network_disabled():
    bootstrap = (
        "import runpy, socket, sys\n"
        "sys.path.insert(0, 'scripts')\n"
        "_script = sys.argv[1]\n"
        "sys.argv = [_script]\n"
        "def _blocked(*a, **k): raise AssertionError('network call in offline CLI test')\n"
        "socket.socket.connect = _blocked\n"
        "socket.create_connection = _blocked\n"
        "try:\n"
        "    runpy.run_path(_script, run_name='__main__')\n"
        "except SystemExit as e:\n"
        "    sys.exit(e.code if isinstance(e.code, int) else 1)\n"
    )
    result = subprocess.run(
        [sys.executable, "-c", bootstrap, str(SCRIPT)],
        cwd=REPO_ROOT, env=_scrubbed_env(),
        capture_output=True, text=True, timeout=120,
    )
    output = result.stdout + result.stderr
    assert result.returncode == 0, output[-2000:]
    assert "OK" in output
