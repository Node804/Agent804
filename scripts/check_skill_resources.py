"""Read-only check of intact/relocated kit resources; not host discovery or invocation."""

import re
import sys
from pathlib import Path

RELATIVE = re.compile(r"(?<![\w.])(?:\.\./)+[\w./-]+")
PLUGIN = re.compile(r"\$\{CLAUDE_PLUGIN_ROOT\}/([\w./-]+)")


def check_resources(kit: Path) -> list[str]:
    errors = []
    for name in ("skills", "framework", "templates"):
        if not (kit / name).is_dir():
            errors.append(f"Missing kit directory: {name}; preserve the intact kit layout")
    skills = sorted((kit / "skills").glob("*/SKILL.md"))
    if not skills:
        errors.append("No skill entry points found under skills/")
    for skill in skills:
        source = skill.read_text(encoding="utf-8")
        targets = [(skill.parent / path.rstrip(".")) for path in RELATIVE.findall(source)]
        targets += [(kit / path.rstrip(".")) for path in PLUGIN.findall(source)]
        for target in targets:
            if not target.exists():
                errors.append(f"{skill.relative_to(kit)}: unavailable resource {target}")
    return errors


if __name__ == "__main__":
    root = Path(sys.argv[1]) if len(sys.argv) == 2 else Path(__file__).resolve().parent.parent
    if len(sys.argv) > 2:
        raise SystemExit("Usage: python check_skill_resources.py [KIT_ROOT]")
    failures = check_resources(root.resolve())
    print("\n".join(failures) if failures else
          "Skill resource paths resolve; host discovery/invocation remains unverified.")
    sys.exit(bool(failures))
