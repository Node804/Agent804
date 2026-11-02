# Agent804: agent instructions

This file is for working **on** the kit. Projects get `templates/AGENTS.md`, not this file.

The kit is a framework (`framework/`), templates (`templates/`) and agent skills (`skills/`)
for setting up agent-ready projects. It is documentation that agents execute, so a wrong
sentence here becomes wrong behaviour in someone else's project.

## Check

```bash
python scripts/check.py        # Python 3.11+ and Git; must pass before calling a task done
```

It checks: skill frontmatter, links and `${CLAUDE_PLUGIN_ROOT}` paths, rule IDs, rule
alignment (below), line and character budgets, private names, JSON and TOML, the two plugin
manifests and the stop hooks in disposable Git repositories. It
proves the kit is consistent, not that it works in a real project.

## Two readers, one home per statement

`framework/` is written for people: why each rule exists, trade-offs and evidence. Skills and
templates are written for agents: what to do, in the fewest words. Each statement has one home.

| What | Lives in | Says |
|---|---|---|
| The rule | `framework/rules.md` row | The property and how to grade it |
| What an agent does about it | The skill that sets it up or runs it, or a template line | The instruction, citing the rule ID |
| Why | The framework page for its topic | The reason, citing the rule ID; never repeats the instruction |

When a rule changes, change all three in the same commit, plus `levels.md` or `modules.md` if
its gating or module moves, and the README and `validation.md` where they describe it.
The check enforces part of this: every rule is cited by a skill or template, and every
gating rule by one other than `assess` that sets it up (`assess` grades from the practice mapping).
Skills link only the framework tables and playbooks the check allows, within size budgets.

## Rules

- A new rule is core only if every project built with agents needs it. Otherwise it goes in a
  module with a trigger (`framework/modules.md`), and a new module starts as Trial.
- Agent804 owns what coding agents change: problems they create, make worse or make faster.
  For an engineering problem agents do not change (incident response, debt tracking, a
  security programme), state the agent-specific point in a sentence or two and link the
  established standard; do not rewrite the standard here.
- Agent804 governs development in GenAI projects: how agents build software for the developer
  directing them, and how the AI-facing parts of a product are built (MCP servers, APIs for
  agents, embedded AI features: the Operate module). Project governance (who signs off,
  audit, compliance) is that developer's responsibility; the framework does not score it.
- A rule states a property, never a tool. Stack mechanisms belong in
  `framework/profiles/<stack>.md`, added only after a real project has used it. Host
  behaviour belongs in `framework/agents/`; record what was exercised on the real host.
- Routing is written in roles and capability tiers, never model names, and works with one model.
- `framework/validation.md` lists the published work the framework was checked against, what
  each reinforced, and why Agent804 chose differently where it did. Read it before changing
  a rule; add to it when a change rests on a reference. Never cite a source nobody has read.
- Skills use only the portable frontmatter fields: `name`, `description`, `license`,
  `compatibility`, `metadata`, `allowed-tools`. Other agents reject the rest.
- Skills refer to other files as `${CLAUDE_PLUGIN_ROOT}/...` for Claude Code and as a relative
  path for other agents; keep both.
- `SKILL.md` stays under 200 lines; this file under 100; framework pages under 200.
- Never name a project, organisation or person the framework was built or trialled on,
  anywhere in the kit: say "a reference project" instead. The check fails on any name listed
  in the git-ignored `private-names.local.md`, one per line.
- Two plugin manifests: `.claude-plugin/plugin.json` (Claude Code) and the root `plugin.json`
  (Codex). Change both together; the check fails when they differ.
- Never commit or push unless asked in chat.
