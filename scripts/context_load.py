"""Report explicit kit read recipes; this is not a live context profiler."""

import argparse
import json
import math
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HOSTS = ("codex", "claude-code", "grok-build", "chatgpt")
RULE_ROW = re.compile(r"^\| ([A-Z]{2}-\d+) \|")


def headings(lines: list[str]) -> list[tuple[int, int, str]]:
    """Return real ATX headings, excluding fenced examples."""
    found = []
    fence = None
    for index, line in enumerate(lines):
        marker = re.match(r"^ {0,3}(`{3,}|~{3,})", line)
        if marker:
            token = marker[1]
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
            continue
        if fence:
            continue
        match = re.match(r"^(#{1,6})[ \t]+(.+?)(?:[ \t]+#+)?[ \t]*$", line.rstrip("\n"))
        if match:
            found.append((index, len(match[1]), match[2]))
    return found


def selected_lines(lines: list[str], selector: str | None) -> set[int]:
    if selector is None:
        return set(range(len(lines)))
    outline = headings(lines)
    if selector.startswith("rule:"):
        rule = selector.removeprefix("rule:")
        matches = [i for i, line in enumerate(lines) if (m := RULE_ROW.match(line)) and m[1] == rule]
        if len(matches) != 1:
            raise ValueError(f"Missing or ambiguous rule: {rule}")
        row = matches[0]
        families = [i for i, level, _ in outline if level == 2]
        preceding = [i for i in families if i < row]
        if not preceding:
            raise ValueError(f"Rule has no family context: {rule}")
        start = preceding[-1]
        end = next((i for i in families if i > row), len(lines))
        # Include opening definitions and every family qualification, without other rows.
        return set(range(families[0])) | {
            i for i in range(start, end) if i == row or not RULE_ROW.match(lines[i])
        }
    matches = [(i, level) for i, level, title in outline if title == selector]
    if len(matches) != 1:
        raise ValueError(f"Missing or ambiguous heading: {selector}")
    start, level = matches[0]
    end = next((i for i, depth, _ in outline if i > start and depth <= level), len(lines))
    return set(range(start, end))


def totals(counts: dict[str, int]) -> dict:
    characters = sum(counts.values())
    return {
        "characters": characters,
        "estimated_tokens": math.ceil(characters / 4),
        "files": [
            {"path": path, "characters": count, "estimated_tokens": math.ceil(count / 4)}
            for path, count in sorted(counts.items())
        ],
    }


def measure(root: Path, selections: list[tuple[str, str | None]]) -> dict:
    """Count normalized characters, deduplicating overlapping reads of the same file."""
    root = root.resolve()
    content: dict[str, list[str]] = {}
    selected: dict[str, set[int]] = {}
    for relative, selector in selections:
        path = (root / relative).resolve()
        if not path.is_relative_to(root):
            raise ValueError(f"Resource is outside kit: {relative}")
        key = path.relative_to(root).as_posix()
        if key not in content:
            content[key] = path.read_text(encoding="utf-8").splitlines(keepends=True)
            selected[key] = set()
        # Validate every selector even if a previous whole-file read covers it.
        selected[key].update(selected_lines(content[key], selector))
    return totals({path: sum(len(content[path][i]) for i in indices)
                   for path, indices in selected.items()})


def build_report(root: Path, host: str = "codex") -> dict:
    if host not in HOSTS:
        raise ValueError(f"Unknown host: {host}")
    skill_paths = sorted(p.relative_to(root).as_posix() for p in root.glob("skills/*/SKILL.md"))
    if not skill_paths:
        raise ValueError("No skills found")
    metadata = {}
    for path in skill_paths:
        text = (root / path).read_text(encoding="utf-8")
        header = re.match(r"\A---\n(.*?)\n---(?:\n|$)", text, re.DOTALL)
        if not header:
            raise ValueError(f"Missing skill metadata: {path}")
        fields = re.findall(r"^(?:name|description): .+$", header[1], re.MULTILINE)
        if len(fields) != 2:
            raise ValueError(f"Missing skill name/description: {path}")
        metadata[path] = sum(len(field) + 1 for field in fields)
    metadata["templates/AGENTS.md"] = len((root / "templates/AGENTS.md").read_text(encoding="utf-8"))
    startup = totals(metadata)
    startup["assumptions"] = "All skill names/descriptions plus the unfilled project instruction template."

    def whole(*paths: str) -> list[tuple[str, None]]:
        return [(path, None) for path in paths]

    host_reads = whole("framework/agents/README.md", f"framework/agents/{host}.md")
    levels = "framework/levels.md"
    modules = "framework/modules.md"
    rules = "framework/rules.md"
    # Recipes describe concrete scenarios, not automatic expansion of Markdown links.
    recipes = {
        "small-fix": (
            whole("skills/spec/SKILL.md"),
            "Clear non-red-zone fix; existing area docs and criteria in plan/PR; no new template or host setup.",
        ),
        "check-adoption": (
            whole("skills/adopt/SKILL.md")
            + [(levels, "How much a project needs"), (modules, "The modules")]
            + [(rules, f"rule:{rule}") for rule in
               ("CK-1", "CK-2", "CK-8", "ST-1", "MT-2", "SE-2", "TS-1", "TS-4", "TS-10", "TS-12",
                "GR-1", "GR-3", "GR-4", "GR-7")],
            "Wrap existing check commands; known stack mappings and project record; no new style/scanner/host/CI mechanism. "
            "Rule-row dependencies and family qualifications included; other increments add their applicable rules/resources.",
        ),
        "full-assessment": (
            whole("skills/assess/SKILL.md", levels, modules, rules) + host_reads,
            "Full core and all module triggers, one selected host; add applicable stack profile and triggered playbooks. "
            "No completion opt-in or concurrent writers in this recipe.",
        ),
        "resumed-planning": (
            whole("skills/context/SKILL.md", "skills/plan/SKILL.md"),
            "Resume already-agreed dependent increments in an existing plan; no new criteria, decisions, template or workers. "
            "New product uncertainty returns to spec; implementation/test/review handoffs add their own reads.",
        ),
        "new-project": (
            whole("skills/start/SKILL.md", "framework/profiles/README.md")
            + [(levels, heading) for heading in ("Practices behind the level", "Scoring", "How much a project needs")]
            + [(modules, "The modules")] + host_reads
            + whole("templates/AGENTS.md", "templates/agent-host.md", "templates/adr.md", "templates/evidence.md",
                    "templates/risk-zones.md", "templates/maintainability.md", "templates/security.md",
                    "templates/pull_request_template.md"),
            "Core setup with existing README for current behavior; no optional modules/routing/completion. "
            "Add chosen stack profile or draft template, selected host settings and chosen editor/changelog resources.",
        ),
    }
    workflows = {}
    for name, (selections, assumptions) in recipes.items():
        workflows[name] = measure(root, selections)
        workflows[name]["assumptions"] = assumptions
        workflows[name]["reads"] = [{"path": path, "selector": selector} for path, selector in selections]
    return {
        "limits": "Character/4 estimates of explicit kit read recipes, not live tokens, dependency closure or attention. "
                  "Workflow sizes exclude startup (shown separately), project code/records, host/system instructions, "
                  "history, chat, logs and tool output. Conditional additions are named per recipe. "
                  "Overlapping reads count once per workflow; repeated live reads can cost more. No aggregate thresholds.",
        "startup": startup,
        "skills": {Path(path).parent.name: measure(root, [(path, None)]) for path in skill_paths},
        "workflows": workflows,
    }


def format_report(report: dict, detailed: bool = True) -> str:
    lines = ["Context load: characters / estimated tokens (4 characters per token)", report["limits"]]
    lines.append(f"Startup model: {report['startup']['characters']} / {report['startup']['estimated_tokens']}")
    lines.append("Skills (whole files):")
    for name, size in report["skills"].items():
        lines.append(f"  {name}: {size['characters']} / {size['estimated_tokens']}")
    lines.append("Workflow recipes (incremental kit reads):")
    for name, size in report["workflows"].items():
        lines.append(f"  {name}: {size['characters']} / {size['estimated_tokens']}")
        if detailed:
            for entry in size["files"]:
                lines.append(f"    {entry['path']}: {entry['characters']} / {entry['estimated_tokens']}")
            lines.append(f"    Assumes: {size['assumptions']}")
    if not detailed:
        lines.append("Recipe assumptions and per-file detail: python scripts/context_load.py [--host HOST] [--json]")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", choices=HOSTS, default="codex")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    try:
        report = build_report(ROOT, args.host)
    except (OSError, ValueError) as exc:
        parser.exit(1, f"Cannot measure context load: {exc}\n")
    print(json.dumps(report, indent=2) if args.json else format_report(report))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
