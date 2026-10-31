# <Project name>: agent instructions

<One paragraph: what this is, who uses it, what happens if it breaks.>

This file is the single source of instructions for every agent. Tool-specific files only point
here. It holds what you cannot find by reading the code; keep it under 200 lines (the check
enforces it).

## Check

```bash
<check command>          # everything CI runs; must be green before you say a task is done
<single test command>    # one test file or test
<bootstrap command>      # fresh clone to running app; safe to rerun
<run command>
```

## Rules

<!-- Only rules an agent would otherwise get wrong. When you correct the same thing twice, add it
here; when it can be checked mechanically, move it into the check and delete the line. -->

- Access: every entry point declares who may use it; the check fails otherwise.
- <Boundary rule: how modules may talk to each other.>
- <Where writes go, and what they record.>
- <Outside systems: where they are reached from, read-only or not.>
- Scripts that change data are dry-run unless given `--commit`.

## Working here

- Work on a branch. Never commit, push, deploy or migrate unless asked in chat.
- New behaviour starts from acceptance criteria in `docs/specs/` (the `spec` skill sizes them)
  and tests written first and seen to fail.
- Never skip, weaken or delete a failing test to get green; fix the cause or say it fails.
- Non-trivial work has a plan in `docs/plans/` with progress notes; update it as you go.
- Risk zones are in `docs/risk-zones.md`. In a red zone, stop and ask before changing behaviour.
- **Done** means: acceptance criteria met, tests written and passing, the check green, a
  changelog entry, docs and this file updated if behaviour changed. Report the commands you ran
  and their result; never claim a check you did not run.

## Decisions

Hard-to-reverse decisions are ADRs in `docs/adr/`. Read the ones on a topic before changing it.
