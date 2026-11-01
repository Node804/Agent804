---
name: garden
description: Find instruction files, docs, plans and decisions that no longer match the code, and drift from the project's rules, then propose small fixes. Use on a schedule (weekly) or when the user suspects the docs are stale.
---

# Garden the repository

Docs go stale the moment code changes, and agents copy whatever patterns exist, good or bad
(OAI). This pass finds drift and proposes small fixes (MS-2, MS-3). It changes files only when
the user asks; otherwise it reports.
Read the project's records where they exist: `docs/maintainability.md`
and `docs/security.md` (finding decisions follow SE-6; security evidence goes stale).

Review flaky failures, retry rates, quarantine owners/expiry, skipped suites, unexpected
discovery changes and obsolete fixtures (MS-2, TS-10, TS-12). Propose reviewed corrections;
never silently skip a failure or change acceptance outcomes without affected criteria review.

## Steps

1. **Instruction files** (`AGENTS.md` and nested ones):
   - every command named still runs; every path named exists;
   - each rule is still true of the code (spot-check two or three per file);
   - rules now enforced by a check can be shortened to a pointer;
   - line budgets hold; history or file-layout descriptions have not crept in (IN-2).
2. **Decisions**: ADRs whose Consequences name a check that does not exist; Proposed ADRs older
   than a month with nothing built; Validated or Rejected ADRs with no evidence record (DC-2); contradictory evidence awaiting
   owner review. Never rewrite frozen ADRs.
3. **Plans**: plans marked active with no commit on their branch for two weeks; done plans
   still marked active.
4. **Specs**: specs marked Agreed whose feature shipped (set Built) or was dropped.
5. **Drift in code**: patterns `AGENTS.md` forbids that appeared anyway (grep for them);
   duplicated helpers where a shared one exists; new `skip` or `xfail` markers. Inspect
   structural trends, changed dependency directions, obsolete paths and exceptions whose
   review condition has arrived (MT-2, MT-3). Trace dynamic registration and external consumers
   before proposing removal. Record retained items and why; never delete from a report alone.
6. **Instructions vs models**: rules that exist to work around an old model's habits. List them
   for the user to try removing (MS-3); do not remove them yourself.
7. **Contracts and references** (MT-1, IN-5): review changed public behavior against docs and
   examples, run safe reference/example checks, and distinguish current guidance from history.
8. **Maintenance exercises** (MS-4): report recorded obstacles and unresolved follow-up. Suggest
   a representative task if none has been trialled; do not run implementation work without
   authorization. This is a practice, not a score gate.
9. **Security drift**: review advisories/support status, config changes, current scanner
   coverage and failed/stale reports, due remediation and expiring risk acceptances. Propose
   fixes or accountable human decisions; never silently renew exceptions or treat existing
   findings as permitted exposure. Do not read secrets or inspect live systems without authorization.

10. **Style drift** (ST-1): a new language with no formatter, editor and CI versions that
    disagree, or broad suppressions. Propose scoped fixes; never run a bulk reformat unasked.

11. **Agreement drift** (GR-7): specs whose criteria changed after agreement with no sign the
    person saw them again, and statuses an agent set. Agents cannot renew a person's decision.

## Report

Review the project's debt record (MT-5). Triage candidates, missing owners, due dates/events, changed exposure and stale closure evidence.
Propose repayment or accountable deferral review; never silently renew exceptions or acquire
authority by creating tickets. Urgent security/defect follow-up keeps its own response clock.

Inspect context drift: stale maps/indexes/working notes, lost
constraints or summaries that promote hypotheses to decisions. Propose scoped fixes; do not
generate a second code inventory or claim recall/recovery effectiveness without trial evidence.

For restructuring candidates, identify concrete maintenance friction and affected scope;
hand authorized implementation to the refactor playbook: Claude Code
`${CLAUDE_PLUGIN_ROOT}/skills/refactor/SKILL.md`, otherwise `../refactor/SKILL.md` from here.
This gardening pass does not itself authorize broader cleanup or behavior changes (MT-4).

A short list of findings, each with the file and a proposed fix, grouped as **fix now** (stale
facts, broken commands), **decide** (rules or ADRs that need an owner's call) and **sensor
candidates** (drift a check could catch; hand them to `sensor`). If the user agrees, make each
fix as its own small change.
