"""Self-check for the Agent804 repository: the kit is held to its own rules (CK-1)."""

import json
import py_compile
import re
import runpy
import sys
import tomllib
import unittest
from pathlib import Path

from check_skill_resources import check_resources

ROOT = Path(__file__).resolve().parent.parent
PORTABLE_KEYS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
BUDGETS = {"SKILL.md": 200, "AGENTS.md": 100}
FRAMEWORK_BUDGET = 200
RULE_ID = re.compile(r"\b(IN|CK|ST|AP|GR|SK|TS|AR|SE|MT|WK|DC|RV|MS|OP)-\d+\b")
LINK = re.compile(r"\[[^\]]*\]\(([^)#\s]+)(?:#[^)]*)?\)")
PLUGIN_PATH = re.compile(r"\$\{CLAUDE_PLUGIN_ROOT\}/([\w./-]+)")


def frontmatter(text: str) -> dict[str, str] | None:
    """Parse the flat `key: value` frontmatter the skills use; None if absent."""
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None
    fields = {}
    for line in text[4:end].splitlines():
        if line.strip() and not line.startswith(" "):
            key, _, value = line.partition(":")
            fields[key.strip()] = value.strip()
    return fields


def private_name_hits(root: Path, names: list[str]) -> list[str]:
    """Files that mention a private project name; the names live only in a git-ignored list."""
    if not names:
        return []
    pattern = re.compile(r"\b(" + "|".join(re.escape(n) for n in names) + r")\b", re.IGNORECASE)
    hits = []
    for path in sorted(root.rglob("*")):
        if not path.is_file() or ".git" in path.parts or "__pycache__" in path.parts:
            continue
        if path.name.endswith(".local.md"):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for number, line in enumerate(text.splitlines(), 1):
            if pattern.search(line):
                rel = path.relative_to(root).as_posix()
                hits.append(f"{rel}:{number}: names a private project; say 'a reference project'")
    return hits


def main() -> int:
    errors: list[str] = []
    errors.extend(check_resources(ROOT))
    names_file = ROOT / "private-names.local.md"
    if names_file.exists():
        names = [n.strip() for n in names_file.read_text(encoding="utf-8").splitlines()]
        errors.extend(private_name_hits(ROOT, [n for n in names if n and not n.startswith("#")]))
    rules_text = (ROOT / "framework" / "rules.md").read_text(encoding="utf-8")
    defined = set(re.findall(r"^\| ((?:[A-Z]{2})-\d+) \|", rules_text, re.MULTILINE))

    for md in sorted(ROOT.rglob("*.md")):
        if ".git" in md.parts:
            continue
        rel = md.relative_to(ROOT).as_posix()
        text = md.read_text(encoding="utf-8")
        lines = text.count("\n") + 1

        budget = BUDGETS.get(md.name) or (FRAMEWORK_BUDGET if rel.startswith("framework/") else 0)
        if budget and lines > budget:
            errors.append(f"{rel}: {lines} lines, budget {budget}")

        for target in LINK.findall(text):
            if "://" in target or target.startswith("mailto:"):
                continue
            if not (md.parent / target).exists():
                errors.append(f"{rel}: link to missing file {target}")

        for target in PLUGIN_PATH.findall(text):
            if not (ROOT / target.rstrip(".")).exists():
                errors.append(f"{rel}: ${{CLAUDE_PLUGIN_ROOT}}/{target} does not exist")

        if rel.startswith(("skills/", "templates/", "framework/")):
            for match in RULE_ID.finditer(text):
                if match.group(0) not in defined:
                    errors.append(f"{rel}: cites {match.group(0)}, not in framework/rules.md")

        if md.name == "SKILL.md":
            fields = frontmatter(text)
            if fields is None:
                errors.append(f"{rel}: no frontmatter")
                continue
            extra = set(fields) - PORTABLE_KEYS
            if extra:
                errors.append(f"{rel}: non-portable frontmatter keys {sorted(extra)}")
            if fields.get("name") != md.parent.name:
                errors.append(f"{rel}: name {fields.get('name')!r} != folder {md.parent.name!r}")
            if not fields.get("description"):
                errors.append(f"{rel}: no description")

    for js in sorted(ROOT.rglob("*.json")):
        if ".git" in js.parts:
            continue
        try:
            json.loads(js.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"{js.relative_to(ROOT).as_posix()}: invalid JSON ({exc})")

    # Claude Code reads .claude-plugin/plugin.json and Codex the root plugin.json: keep in step.
    claude = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
    codex = json.loads((ROOT / "plugin.json").read_text(encoding="utf-8"))
    for field in ("name", "version", "description", "author", "license"):
        if claude.get(field) != codex.get(field):
            errors.append(f"plugin.json: {field} differs from .claude-plugin/plugin.json")

    for name in ("codex-config.toml", "grok-project.toml", "grok-user-config.toml"):
        try:
            tomllib.loads((ROOT / "templates" / name).read_text(encoding="utf-8"))
        except tomllib.TOMLDecodeError as exc:
            errors.append(f"templates/{name}: {exc}")

    for name in ("stop_check.py", "codex_stop_check.py", "grok_stop_check.py", "check_approvals.py"):
        try:
            py_compile.compile(str(ROOT / "templates" / name), doraise=True)
        except py_compile.PyCompileError as exc:
            errors.append(f"templates/{name}: {exc.msg}")

    approval_validator = runpy.run_path(str(ROOT / "templates" / "check_approvals.py"))["validate"]
    errors.extend(approval_validator(ROOT / "templates" / "approval.json", ROOT))

    suite = unittest.defaultTestLoader.discover(str(ROOT / "scripts"), pattern="test_*.py")
    if not unittest.TextTestRunner(verbosity=1).run(suite).wasSuccessful():
        errors.append("Behavioral regression tests failed; fix the cause rather than bypassing the tests")

    for error in errors:
        print(error)
    print(f"{len(errors)} problem(s)" if errors else "check passed")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
