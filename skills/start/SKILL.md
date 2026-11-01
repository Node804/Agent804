---
name: start
description: Set up a new project from an empty or near-empty repository with an agent harness before any feature is built - instructions file, one check command, guardrails, walking skeleton, CI, decisions and risk zones. Use only when the user asks to start or set up a new project. For a repository that already has code, use assess instead.
---

# Start a project

Put a new project on foundation 4 (the whole harness) before its first feature: a running app, a
green check and exercised completion controls, or explicit gaps against that target. Nothing is committed
unless the user asks.

**Framework files**: in Claude Code, `${CLAUDE_PLUGIN_ROOT}/framework/` and
`${CLAUDE_PLUGIN_ROOT}/templates/`; for other agents, `../../framework/` and `../../templates/`
from this file. Read `framework/rungs.md` first.

## 1. Check the starting point

- List the folder. If it holds application code, stop and suggest `assess`: this skill is for
  new projects.
- Initialize Git if needed. Independently inspect the branch and working-tree changes before
  writing: reuse an appropriate task branch or create one (for example `setup`). An existing
  empty repository on its default branch still needs a task branch. Preserve existing changes;
  never reset or stash them automatically. Do not commit or push without authorization.
- For concurrent writers, follow the worktree playbook in `framework/worktrees.md`: in Claude
  Code `${CLAUDE_PLUGIN_ROOT}/framework/worktrees.md`, otherwise `../../framework/worktrees.md`
  from this file. Before a baseline commit exists, use sequential sessions in the initial
  checkout; do not create an implicit commit to enable parallel work.

## 2. Interview, one question at a time

Ask, wait, then ask the next. Accept short answers; offer a default for each.

1. **What is it, and for whom?** One paragraph.
2. **What happens if it breaks?** Personal tool / internal business use / customer data,
   money, safety, or writes into other systems of record (see `rungs.md`).
3. **Prototype or production?** A prototype will be thrown away; say so in the README.
4. **Stack?** If the user has no preference, recommend one that has a profile in
   `framework/profiles/` and is boring, typed and well known. Explain in one line why.
5. **Who reviews changes, and can they read code in this stack?** If nobody can, say plainly
   that the harness lowers the skill needed but does not remove the need for a reviewer, and
   suggest red-zone areas be kept small.
6. **Will agents, scripts or AI assistants use this system?** An API, MCP tools,
   automation. If yes, the target includes Operate O1 and O2 (all three in production), and
   the skeleton's first action is built through one contract (`operate`).

Set the **target** from the table in `framework/rungs.md` (a foundation plus the loop rungs
the project needs, and Operate levels if agents will use it). Tell the user the target and what it costs in one or two sentences.

## 3. Load the stack profile

Read the support matrix and selection guidance: Claude Code
`${CLAUDE_PLUGIN_ROOT}/framework/profiles/README.md`, otherwise
`../../framework/profiles/README.md` from this file. Select the actual framework profile and
read its parents/shared baseline first: Laravel extends PHP; WPF/WinForms extend .NET.
C# maps to `dotnet.md`, JS/TS to `node-typescript.md`. Resolve inherited and overridden
mechanisms in the project's `docs/stack-profile.md` before generating recipes; do not run
competing formatters or duplicate parent tasks. Draft guidance is not running protection.
If none exists, copy `_template.md` as the project profile, fill it in with the user and mark
it Draft. List unmapped rules, actual required versions and missing mechanisms as gaps.
Never treat shared recommendations or a style starter as a complete stack profile.
Read the maintainability guidance: Claude Code `${CLAUDE_PLUGIN_ROOT}/framework/maintainability.md`,
otherwise `../../framework/maintainability.md` from this file. Agree enforced complexity limits,
review triggers, public-interface scope and exception handling before implementing the skeleton.
Read security guidance: Claude Code `${CLAUDE_PLUGIN_ROOT}/framework/security.md`, otherwise
`../../framework/security.md` from this file. Identify the accountable owner, assets, data,
identities, interfaces and trust boundaries; agree credible abuse cases, versioned security
requirements, justified exclusions, safe development data and dependency/install policy.
Record concrete finding deadlines, release-blocking policy and scoped human acceptance rules.
Read style guidance: Claude Code `${CLAUDE_PLUGIN_ROOT}/framework/style.md`, otherwise
`../../framework/style.md` from this file. Inspect existing configurations before choosing.
Preserve project choices, apply user preferences, or offer our optional defaults: Claude Code
`${CLAUDE_PLUGIN_ROOT}/framework/recommendations/style-defaults.md`, otherwise
`../../framework/recommendations/style-defaults.md`. Starter assets are in Claude Code
`${CLAUDE_PLUGIN_ROOT}/templates/style/`, otherwise `../../templates/style/` from this file.
Record the agreed language/grammar matrix in the project profile or style document, including
versions, configs, check/fix commands, authored tests/scripts, UI/template scope and exclusions.
Framework-specific starters supplement their base language; they are not full stack profiles.
Read approvals guidance: Claude Code `${CLAUDE_PLUGIN_ROOT}/framework/approvals.md`, otherwise
`../../framework/approvals.md` from this file. Agree owner/reviewer authority, required stage
decisions, independence and original-source verification. Reuse existing scoped consent;
group related decisions when their subjects were presented clearly. Never invent missing
approval evidence or infer commit/push/deployment permission from feature agreement.

## 4. Build the harness, in this order

Select actual hosts via Claude Code `${CLAUDE_PLUGIN_ROOT}/framework/agents/README.md`,
otherwise `../../framework/agents/README.md` from here. Record client/version/capabilities
in `docs/agent-host.md` from `templates/agent-host.md`; missing facilities stay gaps.
Use context guidance: Claude Code `${CLAUDE_PLUGIN_ROOT}/framework/context-management.md`,
otherwise `../../framework/context-management.md`; keep recovery state in existing plan/PR notes.
For actual debt, use Claude Code `${CLAUDE_PLUGIN_ROOT}/framework/technical-debt.md`, otherwise
`../../framework/technical-debt.md`; choose a canonical tracker/record, inventing no clean-project debt.
Only if opted in, use Claude Code `${CLAUDE_PLUGIN_ROOT}/framework/model-routing.md`, otherwise
`../../framework/model-routing.md`; offer the optional template without requiring extra models
or subscriptions. Defaults are disabled/recommend-only; don't launch or spend by setting it up.

Each step ends with something you can run.

1. **Baseline tools** from the profile: package manager with a lock file, formatter, linter,
   type checker, test runner and complexity checks (MT-2). Pin versions. Add the profile's
   documentation, example, duplicate and unused-code checks; keep judgment-based reports
   visible for review instead of presenting them as proof of correctness. Add applicable
   security checks (SE-2), with report freshness, safe detection fixtures and explicit
   error/skip handling. Review dependency sources, build execution and reproducible inputs
   before installing new packages (SE-3); an audit is not permission to run untrusted code.
   Adopt selected style assets by merging existing files, not overwriting project conventions.
   Separate non-mutating checks from fixes; align editor/local/CI and disable conflicting
   layout rules. Pin reviewed tool/runtime versions before claiming ST-1 to ST-3 met.
2. **The check command** (CK-1): one command that runs everything. Write it to `.agent-check`
   (one line) for the stop hook.
3. **Walking skeleton** (SK-1, SK-2): the smallest app that boots, one page or endpoint behind
   access control, a bootstrap command that takes a fresh clone to running, and one end-to-end
   test. If the target includes AR-1, add the check that fails on an entry point with no access
   rule. If agents will use the system (O1, O2), the skeleton's one action is declared once and
   served to the page and to the API or agent tools with the same access rule, read-only for
   machine credentials.
   Document the public contracts, failures and side effects the declarations cannot explain
   (MT-1); provide a short navigation path to the area and its test command (IN-4).
   Demonstrate secure initial defaults and an authorized and refused path with no prohibited
   effect/disclosure (SE-4). Do not wait for rung 5 to protect the first interface.
4. **`AGENTS.md`** from the template, with real commands and scoped additions where needed.
   For Claude Code add `CLAUDE.md` containing `@AGENTS.md`; verify selected hosts' discovery.
5. **Guardrails** (GR-1 to GR-4): production credentials never go in the project's `.env`;
   development uses isolated test resources/credentials. Follow the selected host recipe:
   Claude settings/stop hook, Codex config/hooks, or Grok native config/hooks with its adapter;
   follow the selected recipe's paired engine, native event/continuation contract and reviewed
   command policy. Render actual paths per checkout; merge existing settings, preserve host
   restrictions and verify load/trust. Other hosts need real equivalents or explicit gaps.
6. **CI** running the same check command, and a pull request template from
   `templates/pull_request_template.md`.
7. **Docs**: `docs/adr/` with `templates/adr.md` as `0000-template.md`, and ADR 0001 recording
   the interview answers, stack and target (Status: Proposed). `docs/specs/`,
   `docs/plans/`, `docs/evidence/` with `templates/evidence.md` as `0000-template.md` and a
   record for ADR 0001 linked from that ADR,
   `docs/risk-zones.md` from the template with the first zones drawn with the
   user, and `docs/quality-scenarios.md` from the template with two or three scenarios drawn
   from the interview's "what happens if it breaks" answer (DC-5). A changelog mechanism
   from the profile. Copy `framework/worktrees.md` to `docs/worktrees.md` and fill in the
   profile's actual bootstrap, resource configuration and cleanup commands, even if parallel
   work will come later.
   Create `docs/maintainability.md` from `templates/maintainability.md` with actual checks,
   thresholds, public-interface scope and scoped exceptions. A new project starts without
   legacy findings; do not invent a baseline or bulk exclusions.
   Create `docs/security.md` from `templates/security.md`: threats, requirement/control/test
   mapping, actual verification policy, dependency trust, owner/deadlines and response steps.
   Record separate development evidence and production-readiness status; undeployed controls
   stay pending. Keep secrets and sensitive incident details outside this document.
   Create `docs/approvals/README.md` from `templates/approvals.md` and arrange retained review
   subjects/source references. Offer `templates/approval.json` and `templates/check_approvals.py`
   or a native equivalent; choose required IDs through trusted stage policy. Pending templates
   grant no authority. Do not fabricate live approval records or rewrite current consent.
8. **README and instructions**: what it is, prototype or production, bootstrap/check commands
   and navigation to project maintainability, security, style and approval policies plus test
   commands/evidence locations. Keep `AGENTS.md` concise; tool-specific files point to it.
   Include independent acceptance contexts, honest red handoffs and human review before merge.

## 5. Prove it

- Run the bootstrap command and the check. Both must pass. Show the output.
- Exercise the selected host capability checklist, including skill/resource resolution,
  instruction overrides and actual control behavior; fixture passes alone do not establish it.
- If AR-1 is in place: add an entry point with no access rule, run the check, confirm it fails
  with a message that says how to fix it, then remove it.
- Run `git status` and confirm `.env` or other secrets are ignored.
- Exercise the stop hook with a failing check and confirm it blocks. If worktrees are used,
  verify each one's hook, isolated databases and other resources, and independent check state.
- Introduce a small complexity violation, confirm the check fails for that reason, then remove
  it. Review the skeleton's contracts and run maintained example checks. Report unmapped
  mechanisms and untrialled maintenance exercises as gaps, never as working protection.
- Exercise representative security detections and skeleton abuse/refusal tests with safe
  fixtures; restore the real configuration. Run a safe response tabletop/fixture (SE-6),
  recording outcomes and gaps without accessing production or sending messages on its own.
- Prove each claimed formatting pipeline with a violation/check/fix/second-pass fixture
  (ST-2), including exit handling and no source changes from check mode. Unsupported grammars
  and pending designer round-trips remain explicit gaps, not completed adoption.
- Exercise mechanical approval structure/freshness cases and document the separate human-source
  and host enforcement path (AP-1 to AP-3). Plan valid cross-session reuse and material-change
  trials; a metadata check alone does not prove human review or satisfy RV-1.

- Exercise test discovery and failure propagation, including an unexpectedly empty suite;
  show isolated fixtures and actual integration at the skeleton boundary (TS-10 to TS-12).
  Record command/environment/revision, counts, skips/exclusions and results. Read testing
  guidance: Claude Code `${CLAUDE_PLUGIN_ROOT}/framework/testing.md`, otherwise
  `../../framework/testing.md` from this file. New mechanisms remain untrialled until exercised.

## 6. Report

- What exists, as a short list, and the rung reached against the target.
- What was not verified (for example: CI has not run on a server yet; branch protection must be
  set on the host by the user).
- Next step: describe the first feature and run `spec`.
- Report production security readiness separately from the rung: pending, blocked, or verified
  for the stated release/environment. Local checks never establish actual deployed controls;
  deployment access and authorization are not granted by this setup task.

Ask before the first commit. Suggest the message "Project harness: check, guardrails, walking
skeleton".
