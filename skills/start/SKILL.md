---
name: start
description: Set up a new project from an empty or near-empty repository with an agent harness before any feature is built - instructions file, one check command, guardrails, walking skeleton, CI, decisions and risk zones. Use only when the user asks to start or set up a new project. For a repository that already has code, use assess instead.
---

# Start a project

Put a new project on foundation 4 (the whole harness) before its first feature: a running app, a
green check, and an agent that cannot finish with the check red. Nothing here is committed
unless the user asks.

**Framework files**: in Claude Code, `${CLAUDE_PLUGIN_ROOT}/framework/` and
`${CLAUDE_PLUGIN_ROOT}/templates/`; for other agents, `../../framework/` and `../../templates/`
from this file. Read `framework/rungs.md` first.

## 1. Check the starting point

- List the folder. If it holds application code, stop and suggest `assess`: this skill is for
  new projects.
- If it is not a git repository, `git init` and create a branch (`setup`), so nothing lands on
  the main branch unreviewed.

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

Read `framework/profiles/<stack>.md`. If none exists, copy `_template.md` to the project as
`docs/stack-profile.md`, fill it in with the user, mark it Draft, and list every rule you could
not map under Gaps. Never drop a rule silently.

## 4. Build the harness, in this order

Each step ends with something you can run.

1. **Baseline tools** from the profile: package manager with a lock file, formatter, linter,
   type checker, test runner. Pin versions.
2. **The check command** (CK-1): one command that runs everything. Write it to `.agent-check`
   (one line) for the stop hook.
3. **Walking skeleton** (SK-1, SK-2): the smallest app that boots, one page or endpoint behind
   access control, a bootstrap command that takes a fresh clone to running, and one end-to-end
   test. If the target includes AR-1, add the check that fails on an entry point with no access
   rule. If agents will use the system (O1, O2), the skeleton's one action is declared once and
   served to the page and to the API or agent tools with the same access rule, read-only for
   machine credentials.
4. **`AGENTS.md`** from `templates/AGENTS.md`, filled in with the real commands. A `CLAUDE.md`
   containing only `@AGENTS.md`.
5. **Guardrails** (GR-1 to GR-4): production credentials never go in the project's `.env`;
   development uses its own database and test or scoped credentials. Copy
   `templates/claude-settings.json` to `.claude/settings.json` and `templates/stop_check.py` to
   `.claude/hooks/stop_check.py`. Add the profile's commands to
   the allow list and its migrate/deploy commands to the ask list. A format-on-edit hook if the
   profile has one.
6. **CI** running the same check command, and a pull request template from
   `templates/pull_request_template.md`.
7. **Docs**: `docs/adr/` with `templates/adr.md` as `0000-template.md`, and ADR 0001 recording
   the interview answers, stack and target (Status: Proposed). `docs/specs/`,
   `docs/plans/`, `docs/risk-zones.md` from the template with the first zones drawn with the
   user, and `docs/quality-scenarios.md` from the template with two or three scenarios drawn
   from the interview's "what happens if it breaks" answer (DC-5). A changelog mechanism
   from the profile.
8. **README**: what it is, prototype or production, how to bootstrap, how to check.

## 5. Prove it

- Run the bootstrap command and the check. Both must pass. Show the output.
- If AR-1 is in place: add an entry point with no access rule, run the check, confirm it fails
  with a message that says how to fix it, then remove it.
- Run `git status` and confirm `.env` or other secrets are ignored.

## 6. Report

- What exists, as a short list, and the rung reached against the target.
- What was not verified (for example: CI has not run on a server yet; branch protection must be
  set on the host by the user).
- Next step: describe the first feature and run `spec`.

Ask before the first commit. Suggest the message "Project harness: check, guardrails, walking
skeleton".
