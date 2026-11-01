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
   automation. If yes, the Operate module applies, and the skeleton's first action is built
   through one contract (`operate`).
7. **Who must sign off, and how many write at once?** If someone other than the author must
   approve (owners, a regulated process, a customer), the Approvals module applies. If several
   agents or people will write at the same time, Parallel work applies.

Set the **target** from the table in `framework/rungs.md`, and list the modules whose
triggers in `framework/modules.md` are true; question 2 also decides Security. Tell the user
the target and the modules, and what they cost, in two or three sentences.

## 3. Load the stack profile

Read Claude Code `${CLAUDE_PLUGIN_ROOT}/framework/profiles/README.md`, otherwise
`../../framework/profiles/README.md` from this file. If the kit has a profile for the stack,
use it. Otherwise copy `_template.md` to the project's `docs/stack-profile.md`, fill it in
with the user using the table in the profiles README, and mark it Draft. List unmapped
rules, actual versions and missing mechanisms as gaps.
Agree enforced complexity limits, what counts as a public interface, and how exceptions are
approved, before building the skeleton (MT-2).
Every project gets security scanners in the check and a dependency review policy (SE-2,
SE-3). If the Security module applies, agree with the user the owner, assets, trust
boundaries, credible abuse cases and versioned requirements (SE-1), and how findings get
deadlines (SE-6).
For style, use the ecosystem's standard formatter and linter (for example Ruff, Prettier and
ESLint, gofmt, rustfmt, `dotnet format`, Pint) unless the user prefers others, and record them
in the profile's Style table. Offer `templates/editorconfig` and `templates/gitattributes` for
line endings and encoding.
If the Approvals module applies, agree who has authority to approve what and where those
decisions are recorded. Never invent approval evidence or infer
commit, push or deployment permission from agreement on a feature.

## 4. Build the harness, in this order

Select actual hosts via Claude Code `${CLAUDE_PLUGIN_ROOT}/framework/agents/README.md`,
otherwise `../../framework/agents/README.md` from here. Record client/version/capabilities
in `docs/agent-host.md` from `templates/agent-host.md`; missing facilities stay gaps.
Choose one place debt is tracked; a new project has none to record. Only if the user opts in
to model routing, copy `templates/model-routing.md`; don't launch models or spend to set it up.

Each step ends with something you can run.

1. **Baseline tools** from the profile: package manager with a lock file, formatter, linter,
   type checker, test runner and complexity checks (MT-2). Pin versions. Add the profile's
   documentation, example, duplicate and unused-code checks; keep judgment-based reports
   visible for review instead of presenting them as proof of correctness. Add applicable
   security checks (SE-2), with report freshness, safe detection fixtures and explicit
   error/skip handling. Review dependency sources, build execution and reproducible inputs
   before installing new packages (SE-3); an audit is not permission to run untrusted code.
   The check runs the formatter and linter in report mode; a separate command fixes (ST-1).
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
   Show an allowed and a refused request, the refused one with no effect (AR-1). If the
   Security module applies, also demonstrate safe initial defaults (SE-4).
4. **`AGENTS.md`** from the template, with real commands. Agents read every line of it in
   every session, so it holds only what an agent would otherwise get wrong; no explanations
   for people, no HTML comments. Add one line per module that applies, naming its record:
   Security (`docs/security.md`), Approvals (`docs/approvals/README.md`), Parallel work
   (`docs/worktrees.md`), and model routing if opted in (`docs/model-routing.md`). Tell the
   user how it grows: a correction given twice becomes a line; a line the check can enforce
   moves into the check and is deleted. Area rules go in nested files where that area lives.
   For Claude Code add `CLAUDE.md` containing `@AGENTS.md`; verify selected hosts' discovery.
5. **Guardrails** (GR-1 to GR-4, GR-7): `AGENTS.md` says only a person approves, and an
   approved plan is not a request to commit. Production credentials never go in the `.env`, except a GR-1 exception the
   developer decides and records in `docs/security.md`;
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
   from the profile. If the Parallel work module applies, copy `framework/worktrees.md` to
   `docs/worktrees.md` and fill in the actual bootstrap, resource and cleanup commands.
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
- Exercise a representative security detection with a safe fixture (SE-2) and restore the
  real configuration. If the Security module applies, run a safe response tabletop (SE-6)
  without accessing production or sending messages.
- Add a formatting violation: the check fails without changing the file, the fix command
  repairs it, and a second run changes nothing (ST-1).
- If the Approvals module applies, exercise the approval record checks and document where
  the real human decisions live (AP-1 to AP-3); a metadata check never proves review (RV-1).

- Exercise test discovery and failure propagation, including an unexpectedly empty suite;
  show isolated fixtures and actual integration at the skeleton boundary (TS-10 to TS-12).
  Record command/environment/revision, counts, skips/exclusions and results. New mechanisms
  remain untrialled until exercised.

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
