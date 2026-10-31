---
name: garden
description: Find instruction files, docs, plans and decisions that no longer match the code, and drift from the project's rules, then propose small fixes. Use on a schedule (weekly) or when the user suspects the docs are stale.
---

# Garden the repository

Docs go stale the moment code changes, and agents copy whatever patterns exist, good or bad
(OAI). This pass finds drift and proposes small fixes (MS-2, MS-3). It changes files only when
the user asks; otherwise it reports.

## Steps

1. **Instruction files** (`AGENTS.md` and nested ones):
   - every command named still runs; every path named exists;
   - each rule is still true of the code (spot-check two or three per file);
   - rules now enforced by a check can be shortened to a pointer;
   - line budgets hold; history or file-layout descriptions have not crept in (IN-2).
2. **Decisions**: ADRs whose Consequences name a check that does not exist; Proposed ADRs older
   than a month with nothing built; Validated ADRs with no evidence line.
3. **Plans**: plans marked active with no commit on their branch for two weeks; done plans
   still marked active.
4. **Specs**: specs marked Agreed whose feature shipped (set Built) or was dropped.
5. **Drift in code**: patterns `AGENTS.md` forbids that appeared anyway (grep for them);
   duplicated helpers where a shared one exists; new `skip` or `xfail` markers.
6. **Instructions vs models**: rules that exist to work around an old model's habits. List them
   for the user to try removing (MS-3); do not remove them yourself.

## Report

A short list of findings, each with the file and a proposed fix, grouped as **fix now** (stale
facts, broken commands), **decide** (rules or ADRs that need an owner's call) and **sensor
candidates** (drift a check could catch; hand them to `sensor`). If the user agrees, make each
fix as its own small change.
