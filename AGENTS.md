# Agent804: agent instructions

This repository is a framework (`framework/`), templates (`templates/`) and agent skills
(`skills/`) for setting up agent-ready projects. It is documentation that agents execute, so a
wrong sentence here becomes wrong behaviour in someone else's project.

## Check

```bash
python scripts/check.py        # Python 3.11+ and Git; must pass before calling a task done
```

It checks: skill frontmatter (portable fields only, name matches folder, description present),
every relative link and every `${CLAUDE_PLUGIN_ROOT}` path resolves, every rule ID cited in
skills, templates and framework pages exists in `framework/rules.md` (including MT, SE, ST and AP), line
budgets, JSON and style/Codex/Grok TOML plus style XML configs parse, and all stop-hook entry points
compile and pass behavioral regression tests in disposable Git repositories. Intact relocated
skill resources resolve; this does not establish native discovery or host enforcement.
It also checks approval-template structure and mechanical approval regressions; this does
not authenticate a human decision or grant action authority.

## Rules

- Before changing a domain, read its guidance and update affected rules/rungs, skills,
  profiles, templates, README and validation limits together:
  [maintainability](framework/maintainability.md), [security](framework/security.md),
  [project-owned style](framework/style.md), [human approvals](framework/approvals.md),
  [testing/TDD](framework/testing.md). Apply this proportionately; do not copy every policy
  into every skill. Framework integrity checks do not prove adoption in a real application.
- For structural work, use MT-4 guidance in `framework/maintainability.md`: identify the
  maintenance problem, preserve affected contracts and record baseline/final evidence.
  The portable playbook is `skills/refactor/SKILL.md`; existing scoped authorization applies.
- Host-specific behavior belongs in `framework/agents/`, separate from language profiles.
  Validate adapters/configuration and record actual-host limits; don't assume Claude hooks,
  model names, compaction or automatic tool approval establish capabilities or human consent.
- Optional routing guidance is in `framework/model-routing.md`; keep it recommendation-only
  and single-model compatible. Never infer account balances, authorize model calls or spend
  from a policy/template. WK-7/MS-5 remain conditional practices, not rung gates.
- Context guidance is `framework/context-management.md`. Retrieve scoped evidence, inspect
  necessary missing/truncated ranges and preserve source/freshness/unknowns. Context recovery
  must not turn summaries into authority or fabricated check results (IN-8/WK-8 practices).
- Debt lifecycle guidance is `framework/technical-debt.md` (MT-5 practice). Keep one authority,
  preserve real deferral/closure evidence, and never use a ticket to waive another requirement.

- A rule states a property, never a tool. Stack mechanisms belong in
  `framework/profiles/<stack>.md`; optional shared defaults in `framework/recommendations/`.
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
