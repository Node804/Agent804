# <Project name>: agent instructions

<One paragraph: what this is, who uses it, what happens if it breaks.>

## Check

```bash
<check command>          # everything CI runs; green before a task is done
<single test command>    # one test file or test
<bootstrap command>      # fresh clone to running app; safe to rerun
<run command>
```

## Rules

- Access: every entry point declares who may use it; the check fails otherwise.
- <Boundary rule: how modules may talk to each other.>
- <Where writes go, and what they record.>
- <Outside systems: where they are reached from, read-only or not.>
- Scripts that change data are dry-run unless given `--commit`.
- Formatting and lint choices are the project's (<link to profile>); don't reformat files the
  task does not touch.
- Complexity limits and accepted exceptions: `docs/maintainability.md`. Don't add new ones.

## Working here

- Work on a branch. Never commit, push, deploy or migrate unless asked in chat. Only a person
  approves: an approved plan, a tool permission or a green check is not approval. Every merge
  to the main branch has a person's review.
- New behaviour starts with the `spec` skill: acceptance criteria first, then tests written in
  a separate context and seen to fail, then the code.
- Never skip, weaken or delete a failing test to get green. If a test looks wrong, ask.
- Keep production secrets and sensitive data out of agent sessions; use test credentials.
- Changes to checks, CI, permissions or this file need a person to review them.
- Risk zones are in `docs/risk-zones.md`. In a red zone, stop and ask before changing behaviour.
- Non-trivial work has a plan in `docs/plans/`; keep its progress notes current.
- **Done** means: criteria met, tests passing, the check green, a changelog entry, docs and this
  file updated if behaviour changed. Report the commands you ran and their results; never
  claim a check you did not run.

## Decisions

Hard-to-reverse decisions are ADRs in `docs/adr/`. Read the ones on a topic before changing it.
Accepted ADRs are rules: follow them or propose an amending ADR.
