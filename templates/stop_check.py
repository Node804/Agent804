"""Stop hook: the agent cannot finish while the files it changed leave the check red (GR-4).

Install at .claude/hooks/stop_check.py and register it under "Stop" in .claude/settings.json.
The check command is read from .agent-check (one line) at the project root, or from the
AGENT_CHECK environment variable.

The check runs only when the working tree differs from the last state that passed (remembered in
.git/agent-stop-check), so questions, reviews and a developer's own uncommitted work do not
re-run it every turn. After blocking once in a turn it lets the agent stop, so a check that
cannot be fixed now ends in a report, not a loop.

Exit 0 lets the agent stop. Exit 2 blocks it, and stderr tells it why.
"""

import hashlib
import json
import os
import shlex
import subprocess
import sys
from pathlib import Path

TAIL_LINES = 40


def git(root: Path, *args: str) -> str:
    """Run a read-only git command and return its output."""
    # git is resolved from PATH on purpose: the hook runs on every developer machine.
    result = subprocess.run(  # noqa: S603
        ["git", *args],  # noqa: S607
        cwd=root,
        capture_output=True,
        text=True,
    )
    return result.stdout


def fingerprint(root: Path) -> str:
    """Identify the working tree: HEAD, tracked changes, and untracked files' contents."""
    digest = hashlib.sha256(git(root, "rev-parse", "HEAD").encode())
    digest.update(git(root, "diff", "HEAD", "--binary").encode())
    for name in sorted(git(root, "ls-files", "--others", "--exclude-standard", "-z").split("\0")):
        path = root / name
        if name and path.is_file():
            digest.update(name.encode())
            digest.update(path.read_bytes())
    return digest.hexdigest()


def main() -> int:
    try:
        event = json.load(sys.stdin)
    except json.JSONDecodeError:
        event = {}
    if event.get("stop_hook_active"):
        return 0

    root = Path(os.environ.get("CLAUDE_PROJECT_DIR") or event.get("cwd") or ".")
    if not (root / ".git").is_dir():
        return 0
    state = root / ".git" / "agent-stop-check"
    current = fingerprint(root)
    if state.exists() and state.read_text(encoding="utf-8").strip() == current:
        return 0

    command = os.environ.get("AGENT_CHECK", "")
    check_file = root / ".agent-check"
    if not command and check_file.exists():
        command = check_file.read_text(encoding="utf-8").strip()
    if not command:
        print("No check command: put it in .agent-check or AGENT_CHECK.", file=sys.stderr)
        return 2

    # The command comes from the project's own .agent-check file, which is reviewed like code.
    # Windows parses a command-line string itself (no shell); elsewhere it is split into args.
    args: str | list[str] = command if os.name == "nt" else shlex.split(command)
    result = subprocess.run(  # noqa: S603
        args,
        cwd=root,
        capture_output=True,
        text=True,
    )
    if result.returncode == 0:
        state.write_text(current, encoding="utf-8")
        return 0
    tail = "\n".join((result.stdout + result.stderr).splitlines()[-TAIL_LINES:])
    print(
        f"The check failed (`{command}`, exit {result.returncode}). Fix it before finishing, "
        f"or tell the user plainly that it fails and why.\n{tail}",
        file=sys.stderr,
    )
    return 2


if __name__ == "__main__":
    sys.exit(main())
