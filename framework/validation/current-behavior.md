# Current behavior workflow (0.6)

The developer reported that historical specs and decisions obscured current behavior in
reference projects, and requested folding useful OpenSpec ideas into Agent804. This is a
workflow design responding to that report, not a measured comparison of the frameworks.

| Sources consulted (2026-11-05) | Reinforced | Agent804 choice |
|---|---|---|
| OpenSpec [concepts](https://github.com/Fission-AI/OpenSpec/blob/main/docs/concepts.md), current-spec/change separation | A maintained behavior description separate from proposed changes and history (IN-5) | Reuse existing guides or a small area document; code/tests establish observed behavior and mismatches remain explicit |
| OpenSpec [commands](https://github.com/Fission-AI/OpenSpec/blob/main/docs/commands.md), update/sync/archive | Reconcile delivered changes into maintained descriptions | Fold reconciliation into spec, implementation and review; no CLI dependency, copied command set or automatic acceptance |
| GitHub Spec Kit [bug-fixing reference](https://github.github.com/spec-kit/reference/agentic-bugfix.html) | Scoped assess/fix/verify is available independently of feature SDD | Correct the outdated regeneration-only comparison in the validation index; no effectiveness comparison follows |

IN-5 now explicitly covers discoverable current behavior without reconstructing history.
It remains a reported core practice; gate membership and module triggers are unchanged.
Accepted ADR text and dated evidence retain their existing preservation rules. The new
description cannot approve a changed requirement, bless a defect or establish deployed state
from repository-only checks.

## Verification boundary and pending trials

Existing kit checks cover references, budgets, metadata and rule alignment. A scoped review
can inspect small-project reuse, partial delivery, revision scope and disagreement handling;
neither establishes agent execution or semantic accuracy on a real application.

Trial with a fresh human/agent answering a current-behavior question after several changes,
including a superseded ADR, a regression, a pending feature and a deployment behind the repo.
Also try incremental adoption with unknown areas and a small fix using an existing README.
Record correctness, history needed, missed constraints, drift and maintenance overhead.
These trials remain pending; no real-project effectiveness or deployment is claimed.
