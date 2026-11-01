"""Codex Stop adapter; install beside stop_check.py under .codex/hooks/.

Uses the shared Git/check engine, not Claude environment or output semantics.
Exit 0 always emits JSON; exit 2 requests continuation with a stderr reason.
Host trust, loading, timeouts and actual continuation must be verified separately.
"""

import json
import subprocess
import sys
from pathlib import Path


def main() -> int:
    try:
        event = json.load(sys.stdin)
        if not isinstance(event, dict) or event.get("hook_event_name") != "Stop":
            raise ValueError("expected a Codex Stop event object")
        if not isinstance(event.get("cwd"), str) or not event["cwd"]:
            raise ValueError("Stop event requires cwd")
        if not isinstance(event.get("stop_hook_active", False), bool):
            raise ValueError("stop_hook_active must be boolean")
        if event.get("stop_hook_active"):
            print(json.dumps({"systemMessage": "Check not rerun after continuation; report "
                              "any unresolved failure. This is not a passing check."}))
            return 0

        # Both files are copied together. Import errors must request continuation too.
        from stop_check import check

        result = check(Path(event["cwd"]))
        if result == 0:
            print("{}")
        return result
    except (ImportError, OSError, subprocess.SubprocessError, ValueError) as exc:
        detail = exc.stderr.decode("utf-8", errors="replace") if isinstance(
            exc, subprocess.CalledProcessError
        ) and isinstance(exc.stderr, bytes) else str(exc)
        print(f"Cannot verify the check: {detail.strip()}. Fix the hook/check setup or "
              "report the unresolved failure; do not claim completion.", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
