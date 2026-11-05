# Plan: <feature>

- **Spec:** `docs/specs/<file>.md`, or the criteria themselves for a small change
- **Branch and checkout:** <branch; worktree path if several write at once>
- **State:** active | done | abandoned
- **Agreed:** <what the person agreed, where, and on which version of the criteria>

The next session resumes from this file and the git log, not from chat. Keep it current.

## Steps

- [ ] 1. Acceptance tests written from the criteria in a separate context; they fail for the right reason.
- [ ] 2.
- [ ] 3. After green: refactor where it helps, or note "none needed".
- [ ] 4. Full check green.
- [ ] 5. Current behavior description reconciled with verified scope and evidence (IN-5).

## Increments and integration

<!-- Only for work spanning several changes. Reuse an existing tracker if it already holds
these facts. Use stable IDs; map every criterion, identify dependencies and verification,
and distinguish pending/blocked/active/verified. Prerequisites name their consumer and check.
Omit this section for a small change. -->

| ID | Outcome / criteria | Depends on | Responsible session/person | Verification / evidence | Status |
|---|---|---|---|---|---|
| I1 | <observable outcome; AC IDs> | <IDs or none> | <name or unassigned> | <planned check; actual results when run> | pending |

<!-- State shared contracts, safe intermediate states and integration checkpoints. Record
combined revisions/patches and journey/full-check results; individual green increments do
not establish that their combination works. Note required migration/deployment authorization
and recovery decisions where relevant. A plan or proposed next action is not consent. -->

## Resume here

<!-- Next action; open questions; the exact commit or patch handed over; what was run and its
result. A summary is not evidence that something ran. -->

## Evidence

- Red: <command and the failure, before the code>
- Green: <command and result, after>
- Full check: <command; tests found, run and skipped>

## Decisions made while building

<!-- Small ones here. Anything hard to reverse becomes an ADR. -->

## Progress notes

<!-- Date, what changed, what surprised you. Newest last. -->
