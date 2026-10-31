# Quality scenarios

What must always be true of the whole system, measurably (DC-5). These are the architecturally
significant requirements: each ADR's Context cites the scenarios it serves, and each spec cites
the scenarios it touches, with at least one criterion that exercises them.

- **Measured by** names the spec in `docs/specs/` whose tests prove the scenario, or "No spec
  yet". **Now** changes only when those tests pass, and says which part is met.
- A scenario that no longer applies is marked retired, never renumbered or reused.
- Add one only when a requirement applies across the system and would shape the architecture;
  most requirements are spec criteria.

| ID | When | The system | Measured by | Served by | Now |
|---|---|---|---|---|---|
| QS-1 | <a situation: a source of load, a failure, a change> | <the required response, measurable> | No spec yet | <ADR numbers> | Not yet |
