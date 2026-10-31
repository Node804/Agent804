---
name: assess
description: Audit an existing repository against the Agent804 rungs and rules, read-only, and report its foundation and coverage with evidence and the next three steps. Use when the user asks how their project or agent setup measures up, where to start improving it, or before adopting the framework on existing code.
---

# Assess a repository

Score a repository against `framework/rungs.md` and `framework/rules.md`, with evidence for
every claim. Read-only: never edit, commit or install anything.

**Framework files**: in Claude Code, `${CLAUDE_PLUGIN_ROOT}/framework/`; for other agents,
`../../framework/` from this file.

## Steps

1. **Read the framework**: `rungs.md`, `rules.md`, and the profile for the stack if one exists
   (`profiles/`). Identify the stack from the lock files and dependency manifests.
2. **Read the repository's own instructions**: `AGENTS.md`, `CLAUDE.md`, `.cursor/rules/`,
   `.github/copilot-instructions.md`, nested instruction files, agent settings and hooks.
   Read `.env.example` (or its equivalent) and its comments: it says which settings hold
   secrets and which sources need none. Only what is in the repository counts; git-ignored
   personal settings do not. Uncommitted
   work counts, and the report says which findings depend on it.
3. **Find the check.** Look for a single check command in the instructions, task runner and CI.
   Run it if it only reads and tests. Tests that create and drop their own throwaway database
   count as testing, unless the user said strictly read-only. If it needs credentials or a
   service that is not available, or running it could write to data the user asked you not
   to touch, run the steps that are safe, name the exact commands you would have run, and do
   not work around it. Test runners that use an in-memory or throwaway database are safe;
   anything that opens the project's own database file is not, when told read-only.
4. **Go through the gating rules rung by rung** (the table in `rungs.md`), then the other
   rules as practices. For each rule: **met**, **partly
   met**, **not met**, **not verifiable** (history cannot show it), **not applicable**, or
   **above target** (not required for this kind of project), with the file and line or command
   output that shows it. Do not mark a rule met because a document says it is done; find the
   mechanism.
5. **Look at history** for what documents cannot show: `git log` for change size, merge
   commits, branch use, whether tests arrive before or with code, whether there is a remote.
6. **Score it** using "Scoring" in `rungs.md`: grade each gating rule, mark each rung, then
   the foundation and the coverage line. If agents, scripts or assistants use the built system,
   score the Operate levels the same way. List any not-verifiable rule as an assumption.

## Report

1. **Score**: foundation, the coverage line, the holes in rungs marked `✓*`, and the target
   for this kind of project. Ask the two questions in `rungs.md` if you can; when nobody can
   answer (a subagent, an unattended run), assume from the brief and state the assumption.
   Then the Operate levels (`Operate O1✓ O2✓* O3◐`, or `Operate –`).
2. **Strengths**: rules met well, with evidence. Be specific; no praise without a file reference.
3. **Gaps**, most serious first: rule ID, what is missing, what goes wrong because of it.
   Distinguish "designed but not running" (documented, never exercised) from "absent".
4. **Next three steps**: the smallest changes that raise the foundation first, then close the
   gap to the target, each with the rule IDs it satisfies and a rough size (an hour, a day).
5. **Not checked**: anything you could not verify and why.

Put the score, the top three gaps and the next three steps in the first 15 lines, so a reader
can stop there; evidence follows. Plain statements; do not soften findings, and do not invent
ones you could not confirm.
