"""Self-check for the Agent804 repository: the kit is held to its own rules (CK-1)."""

import json
import py_compile
import re
import sys
import tomllib
import unittest
from pathlib import Path

from check_skill_resources import check_resources

ROOT = Path(__file__).resolve().parent.parent
PORTABLE_KEYS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
BUDGETS = {"SKILL.md": 200, "AGENTS.md": 100}
FRAMEWORK_BUDGET = 200
RULE_ID = re.compile(r"\b(IN|CK|ST|GR|SK|TS|AR|SE|MT|WK|DC|RV|MS|OP)-\d+\b")
LINK = re.compile(r"\[[^\]]*\]\(([^)#\s]+)(?:#[^)]*)?\)")
PLUGIN_PATH = re.compile(r"\$\{CLAUDE_PLUGIN_ROOT\}/([\w./-]+)")
# framework/ is written for people. Skills may send agents only to the tables and playbooks
# they execute; everything else an agent needs is said in the skill itself.
FRAMEWORK_REF = re.compile(r"framework/([\w./-]+\.md)")
AGENT_PAGES = re.compile(r"(rules|rungs|modules|worktrees)\.md|(profiles|agents)/[\w.-]+\.md")
# Characters, about four to a token. Agents read a skill whole each time it runs.
SKILL_CHARS = 8000
SETUP_SKILL_CHARS = 14000  # assess and start run once per project
TEMPLATE_AGENTS_CHARS = 3000  # every project's AGENTS.md starts here and loads every session


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


def agent_read_problems(root: Path) -> list[str]:
    """What skills and the AGENTS.md template make agents read beyond their budget.

    Agents pay for every character they load; the framework's explanations are for people.
    """
    problems = []
    for skill in sorted(root.glob("skills/*/SKILL.md")):
        rel = skill.relative_to(root).as_posix()
        text = skill.read_text(encoding="utf-8")
        budget = SETUP_SKILL_CHARS if skill.parent.name in ("assess", "start") else SKILL_CHARS
        if len(text) > budget:
            problems.append(f"{rel}: {len(text)} characters, budget {budget}")
        for page in sorted(set(FRAMEWORK_REF.findall(text))):
            if not AGENT_PAGES.fullmatch(page):
                problems.append(
                    f"{rel}: sends agents to framework/{page}, which is written for people; "
                    "say what to do in the skill"
                )
    template = root / "templates" / "AGENTS.md"
    if template.exists():
        text = template.read_text(encoding="utf-8")
        if len(text) > TEMPLATE_AGENTS_CHARS:
            problems.append(
                f"templates/AGENTS.md: {len(text)} characters, budget {TEMPLATE_AGENTS_CHARS}"
            )
        if "<!--" in text:
            problems.append("templates/AGENTS.md: HTML comments load into every session")
    return problems


RANGE = re.compile(r"\b([A-Z]{2})-(\d+) (?:to|–) (?:\1-)?(\d+)\b")


def cited_ids(text: str) -> set[str]:
    """Rule IDs a text cites, with ranges such as `TS-1 to TS-3` expanded."""
    ids = {m.group(0) for m in RULE_ID.finditer(text)}
    for family, first, last in RANGE.findall(text):
        ids.update(f"{family}-{n}" for n in range(int(first), int(last) + 1))
    return ids


def gating_ids(rungs_text: str) -> set[str]:
    """Rule IDs in the gating column of the rung table in `rungs.md`."""
    ids: set[str] = set()
    for line in rungs_text.splitlines():
        cells = [c.strip() for c in line.split("|")]
        if len(cells) > 5 and cells[1].isdigit():
            ids |= cited_ids(cells[4])
    return ids


def rule_alignment_gaps(root: Path) -> list[str]:
    """Rules that no agent-facing file acts on.

    A rule only an explanation page mentions is one no agent is told to follow. Every rule
    needs a skill or template citing it. `assess` grades gating rules from the rungs table,
    so a gating rule also needs a skill or template other than `assess` that sets it up.
    """
    rules_text = (root / "framework" / "rules.md").read_text(encoding="utf-8")
    defined = re.findall(r"^\| ((?:[A-Z]{2})-\d+) \|", rules_text, re.MULTILINE)
    gating = gating_ids((root / "framework" / "rungs.md").read_text(encoding="utf-8"))
    cited: dict[str, set[str]] = {}
    for path in sorted(root.glob("skills/*/SKILL.md")) + sorted(root.glob("templates/*.md")):
        cited[path.relative_to(root).as_posix()] = cited_ids(path.read_text(encoding="utf-8"))
    assess = cited.get("skills/assess/SKILL.md", set())
    gaps = []
    for rule in defined:
        setters = [f for f, ids in cited.items() if rule in ids and f != "skills/assess/SKILL.md"]
        if rule in gating and not setters:
            gaps.append(f"{rule}: gating rule cited by no skill or template that sets it up")
        elif not setters and rule not in assess:
            gaps.append(f"{rule}: cited by no skill or template")
    return gaps


def main() -> int:
    errors: list[str] = []
    errors.extend(check_resources(ROOT))
    errors.extend(agent_read_problems(ROOT))
    errors.extend(rule_alignment_gaps(ROOT))
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

    for name in ("stop_check.py", "codex_stop_check.py", "grok_stop_check.py"):
        try:
            py_compile.compile(str(ROOT / "templates" / name), doraise=True)
        except py_compile.PyCompileError as exc:
            errors.append(f"templates/{name}: {exc.msg}")


    suite = unittest.defaultTestLoader.discover(str(ROOT / "scripts"), pattern="test_*.py")
    if not unittest.TextTestRunner(verbosity=1).run(suite).wasSuccessful():
        errors.append("Behavioral regression tests failed; fix the cause rather than bypassing the tests")

    for error in errors:
        print(error)
    print(f"{len(errors)} problem(s)" if errors else "check passed")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
