# Agent804: agent instructions

This repository is a framework (`framework/`), templates (`templates/`) and agent skills
(`skills/`) for setting up agent-ready projects. It is documentation that agents execute, so a
wrong sentence here becomes wrong behaviour in someone else's project.

## Check

```bash
python scripts/check.py        # everything; must pass before you say a task is done
```

It checks: skill frontmatter (portable fields only, name matches folder, description present),
every relative link and every `${CLAUDE_PLUGIN_ROOT}` path resolves, every rule ID a skill cites
exists in `framework/rules.md`, line budgets, JSON files parse, and the stop-hook template
compiles.

## Rules

- A rule states a property, never a tool. Tools belong in `framework/profiles/<stack>.md`.
- `framework/validation.md` lists the published work the framework was checked against, what
  each reinforced, and why Agent804 chose differently where it did. Read it before changing
  a rule; add to it when a change rests on a reference. Never cite a source nobody has read.
- Skills use only the portable frontmatter fields: `name`, `description`, `license`,
  `compatibility`, `metadata`, `allowed-tools`. Other agents reject the rest.
- Skills refer to other files as `${CLAUDE_PLUGIN_ROOT}/...` for Claude Code and as a relative
  path for other agents; keep both.
- `SKILL.md` stays under 200 lines; this file under 100; framework pages under 200.
- No organisation, product or person names from Node 804's projects in examples.
- Two plugin manifests: `.claude-plugin/plugin.json` (Claude Code) and the root `plugin.json`
  (Codex). Change both together; the check fails when they differ.
- Never commit or push unless asked in chat.
