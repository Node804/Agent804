"""Stop hook: the agent cannot finish while the files it changed leave the check red (GR-4).

Install at .claude/hooks/stop_check.py and register it under "Stop" in .claude/settings.json.
The check command is read from .agent-check (one line) at the project root, or from the
AGENT_CHECK environment variable.

After the first commit, successful checks are cached against the tree and check command in
the worktree's private Git directory. Before the first commit, every eligible stop checks.
Ignored files and external services are outside the cache: remove its state file to force a
fresh check after changing them. After blocking once in a turn it lets the agent stop, so a
check that cannot be fixed now ends in a report, not a loop.

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


def git(root: Path, *args: str) -> bytes:
    """Run a read-only Git command; a failure must never become a successful cache key."""
    # git is resolved from PATH on purpose: the hook runs on every developer machine.
    result = subprocess.run(  # noqa: S603
        ["git", "--no-optional-locks", *args],  # noqa: S607
        cwd=root,
        capture_output=True,
        check=True,
    )
    return result.stdout


def fingerprint(root: Path, command: str) -> str:
    """Identify the working tree: HEAD, tracked changes, and untracked files' contents."""
    digest = hashlib.sha256(command.encode("utf-8") + b"\0")
    digest.update(git(root, "rev-parse", "HEAD"))
    digest.update(git(root, "diff", "--no-ext-diff", "--no-textconv", "HEAD", "--binary"))
    for name in sorted(git(root, "ls-files", "--others", "--exclude-standard", "-z").split(b"\0")):
        path = root / os.fsdecode(name)
        if name and path.is_file():
            digest.update(name + b"\0")
            digest.update(hashlib.sha256(path.read_bytes()).digest())
    return digest.hexdigest()


def main() -> int:
    try:
        event = json.load(sys.stdin)
    except json.JSONDecodeError:
        event = {}
    if event.get("stop_hook_active"):
        return 0

    try:
        return check(Path(os.environ.get("CLAUDE_PROJECT_DIR") or event.get("cwd") or "."))
    except (OSError, subprocess.SubprocessError, ValueError) as exc:
        detail = exc.stderr.decode("utf-8", errors="replace") if isinstance(
            exc, subprocess.CalledProcessError
        ) and isinstance(exc.stderr, bytes) else str(exc)
        print(f"Cannot verify the check: {detail.strip()}. Fix Git, the check command, or "
              "filesystem access; report this failure if it cannot be fixed.", file=sys.stderr)
        return 2


def check(start: Path) -> int:
    """Discover the checkout through Git, including linked worktrees and subdirectories."""
    root = Path(os.fsdecode(git(start, "rev-parse", "--show-toplevel")).strip())
    git_dir = Path(os.fsdecode(git(root, "rev-parse", "--absolute-git-dir")).strip())
    state = git_dir / "agent-stop-check"

    command = os.environ.get("AGENT_CHECK", "")
    check_file = root / ".agent-check"
    if not command and check_file.exists():
        command = check_file.read_text(encoding="utf-8").strip()
    if not command:
        print("No check command: put it in .agent-check or AGENT_CHECK.", file=sys.stderr)
        return 2

    try:
        git(root, "rev-parse", "--verify", "--quiet", "HEAD")
    except subprocess.CalledProcessError as exc:
        if exc.returncode != 1:
            raise
        current = None  # No first commit: staged files must not disappear from the cache key.
    else:
        current = fingerprint(root, command)
    if current is not None and state.exists() and state.read_text(encoding="utf-8").strip() == current:
        return 0

    # Never retain a previous success after a failed or interrupted attempt.
    state.unlink(missing_ok=True)

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
        if current is not None and fingerprint(root, command) == current:
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
