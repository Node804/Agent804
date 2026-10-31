# Changelog

## 0.2.0 - 2026-10-31

From three assessment rounds on two repositories and one full-flow feature trial.

### Added
- A Codex manifest (root `plugin.json`) beside the Claude Code one, so Codex shows Node 804 as
  the publisher; the check keeps the two in step.
- **Validation** (`framework/validation.md`) replaces the sources page: how Agent804 was
  checked against published practice, what each reference reinforced, and why it chose
  differently where it did.
  Rules no longer carry per-rule source codes.
- **Operate**, the framework's second half: how agents *use* the built system. Levels O1 (one
  contract), O2 (safe by default) and O3 (bounded) over the OP rules, scored like the rungs;
  `start` asks whether agents will use the system; `assess` reports the level; the `operate`
  skill is organised by level. New rule OP-8: load on outside systems is budgeted.
- Licensed: MIT, with `templates/` under MIT No Attribution so they can be copied into any
  project without a notice.
- Renamed from Agent Factory to **Agent804**; commands are now `/agent804:<skill>`.
- Authorship stated plainly: the framework comes from Node 804's own experience building
  agentic apps, later compared with published practice.
- **Quality scenarios (DC-5)**: system-wide requirements as measurable scenarios with stable
  `QS-n` IDs, above ADRs and specs. `templates/quality-scenarios.md`; specs and ADRs cite them;
  `decide` explains the three layers; `start` seeds the first scenarios.
- **TS-7**: acceptance tests pass the project's own lint and type checks before handover, so the
  only failures are the intended ones.
- **WK-6**: parallel agent sessions each get their own worktree and test database.
- **CK-8**: the check runs from committed state in a clean environment before a merge; CI is the
  standard mechanism, a clean-clone script counts as partly met.
- `spec` offers a tests-only commit (the only evidence for TS-2) and ends by recording evidence.

### Changed
- **Scoring**: foundation (rungs 1-4, strict) plus a coverage line, with each rung met, met with
  holes, started or absent. A partly met rule is a hole to close, not a missing rung. Rungs 5-8
  are independent practices.
- Rung 5 counts features since the workflow was adopted, at least two.
- **GR-1** judges impact: production secrets within the agent's reach fail it; production
  reachable with no credential at all is an outside risk, not a failure. Never infer a secret
  from a placeholder.
- Gating rules are listed per rung; any file over the instruction budget fails IN-3; several
  checks gained explicit partly-met wording (CK-1, CK-2, GR-2 to GR-4, TS-2, WK-1, AR-3, RV-1).
- `assess` reads `.env.example`, counts uncommitted work, ignores personal settings, and states
  assumptions when it cannot verify something.

## 0.1.0 - 2026-10-31

First version: rungs, rules with sources, Django profile, templates, nine skills, plugin
manifest and self-check.
