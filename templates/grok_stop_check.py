"""Draft Grok Build Stop adapter; install beside stop_check.py in .grok/hooks/.

Uses the newer upstream Stop contract, not older public passive-Stop documentation.
Fixture-tested protocol is not evidence the installed host dispatches or enforces it.
"""

import json
import subprocess
import sys
from pathlib import Path


def main() -> int:
    try:
        event = json.load(sys.stdin)
        if not isinstance(event, dict) or event.get("hookEventName") not in ("stop", "Stop"):
            raise ValueError("expected a native Grok Stop event object")
        if not isinstance(event.get("cwd"), str) or not event["cwd"]:
            raise ValueError("Stop event requires cwd")
        if not isinstance(event.get("stopHookActive", False), bool):
            raise ValueError("stopHookActive must be boolean")
        # Reject a Claude/Codex-shaped flag rather than silently losing the retry bound.
        if "stop_hook_active" in event:
            raise ValueError("native Grok adapter requires stopHookActive, not stop_hook_active")
        if event.get("stopHookActive"):
            print("Check not rerun after continuation; report any unresolved failure. "
                  "This is not a passing check.", file=sys.stderr)
            return 0

        from stop_check import check

        return check(Path(event["cwd"]))
    except (ImportError, OSError, subprocess.SubprocessError, ValueError) as exc:
        detail = exc.stderr.decode("utf-8", errors="replace") if isinstance(
            exc, subprocess.CalledProcessError
        ) and isinstance(exc.stderr, bytes) else str(exc)
        print(f"Cannot verify the check: {detail.strip()}. Fix setup or report the failure; "
              "do not claim completion.", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
