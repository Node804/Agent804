# The rungs

Agent804 has two halves. **Build** is how agents build the software: eight rungs, below.
**Operate** is how agents use the software once it runs: three levels, at the end of this
page. A project is scored on both when agents, scripts or AI assistants will use what it
builds.

## Build: eight rungs

Rungs 1–4 are the **harness**: guides that steer the agent before it
acts and sensors that check its work after (Böckeler's terms, see `validation.md`). They are
climbed in order, because each one is useless without the ones below it: architecture checks
nobody runs protect nothing. Rungs 5–8 are the **loop** that keeps the harness honest as the
project grows. They are independent practices, adopted in whatever order the project needs.

`assess` scores a repository against this page; `start` puts a new project on rung 4 before its
first feature.

| # | Rung | Prevents | Gating rules | On it when |
|---|---|---|---|---|
| 0 | Chat and paste | — | — | (where most people start) |
| 1 | Instructions in the repo | The agent reinventing conventions every session | IN-1, IN-3, CK-2 | One instructions file every agent reads, within budget, naming the check command or saying there is none yet |
| 2 | One check command | "Looks done" code; inconsistent style, complexity and unchecked security | CK-1, ST-1, MT-2, SE-2, TS-10, TS-12 | Each language has a formatter and linter the check runs without rewriting files; isolated tests and complete execution/discovery evidence exist; one command and CI cover their intended scope and applicable checks; missing/stale results remain gaps and triggers have dispositions |
| 3 | Guardrails | Irreversible actions, exposed secrets/data, untrusted inputs and invented consent | GR-1 to GR-4, AP-1 to AP-3, SE-1, SE-3 | Threats/requirements and dependency sources are reviewed; valid scoped human decisions are traceable and reused; safe task checkouts and blocking checks operate |
| 4 | Walking skeleton and CI | Unsafe defaults, undocumented contracts, unreviewed merges and machine drift | SK-1, SK-2, CK-8, RV-1, MT-1, SE-4, SE-6, TS-11 | Skeleton exercises an actual product integration boundary and refusal checks pass independently; human review covers merged changes; contracts and response ownership work. Deployment readiness remains separate |
| 5 | Tests before code | Tests that only confirm the implementation or miss approved requirements | TS-1 to TS-3, TS-8, TS-9 where bug fixes apply, AP-4, SE-5 | At least two features since adoption trace approved criteria to tests, implementation and results; a separate acceptance context preserves meaningful pre-change failure evidence; green is followed by justified refactoring |
| 6 | Architecture and maintainability as checks | Slow drift; duplicated rules; obsolete implementations | AR-1, AR-3, CK-4, MT-3; AR-2, AR-4, AR-5 where they apply | Access, boundaries and project invariants fail the build with useful messages; duplicate and retirement findings have evidence-backed dispositions; TS-13 sensitivity trials reported as a practice |
| 7 | Decisions with evidence | Re-arguing settled choices; losing the reason | DC-1 to DC-5 | Quality scenarios with stable IDs; ADRs with Proposed / Validated / Accepted / Rejected, citing the scenarios they serve and linking append-only records in `docs/evidence/`, accepted by the owners |
| 8 | Measure and garden | Believing you are faster when you are busier; stale docs and structural decay | MS-1, MS-2 | Delivery, test reliability and maintainability trends tracked; a scheduled pass proposes reviewed fixes or retention decisions; maintenance exercises are reported as a practice |

Every other rule in `rules.md` is a **practice**: reported in the assessment, but not gating a
rung. The OP rules gate the Operate levels instead.
Maintainability starts in the foundation; it does not wait for rung 6. MS-4 remains a practice
pending real-project trials. See [maintainability.md](maintainability.md).
MT-4 verified refactoring is also reported as a rung 6 practice, not a gate; existing
maintainability and review gates still apply to structural changes.
Security starts in the foundation too. The [security baseline](security.md) distinguishes
development isolation, application controls and actual production-readiness evidence.
[Traceable approvals](approvals.md) gate rung 3; requirement traceability gates rung 5 and
owner decision evidence strengthens rung 7. Review before merge (RV-1) now gates rung 4.
Use the [host capability checklist](agents/README.md) as well as a stack profile: instructions,
skills, check execution, trust/guardrails, worktrees and independent contexts need actual
evidence. Documented configuration or a model name cannot establish these mechanisms.
[Model routing](model-routing.md) is optional: WK-7 and MS-5 are conditional practices,
reported when used, with no rung gate or penalty for one model or one family. Separate
contexts, execution evidence and human review remain required where their rules apply.

[Testing guidance](testing.md) starts in the foundation. TS-13 sensitivity trials remain a
reported practice at rung 6, not a gate; no universal mutation or coverage score is required.

[Context management](context-management.md) clarifies navigation, freshness and recoverable
handoffs. IN-8/WK-8 are reported practices without new gates; MS-4 context trials stay pending.
Neither context size, a summary nor retrieved snippets alone establish complete verification.

[Technical debt](technical-debt.md) connects discovery, deferral and verified closure.
MT-5 is reported as a practice, not a gate; existing exceptions/security/test rules still apply.

## Scoring

Grade each gating rule **met**, **partly met** (the protection exists but has a hole) or **not
met** (the protection is missing), using the Check column in `rules.md`. Then mark each rung:

| Mark | Rung status | Means |
|---|---|---|
| `✓` | Met | Every gating rule met |
| `✓*` | Met with holes | No gating rule is missing; some are partly met. The holes are listed |
| `◐` | Started | Some gating rules met or partly met, at least one missing |
| `✗` | Absent | No gating rule met or partly met |
| `–` | Above target | Not required for this kind of project |

An assessment reports two things, and a third when agents use the built system:

- **Foundation**: count up from rung 1 and stop at the first harness rung that is neither met
  nor met with holes; the foundation is the rung below it. A missing protection is a real hole, however good the rest is; a protection
  with a gap is a hole to close, not a missing rung.
- **Coverage**: one mark per rung, for example `1✓* 2✓* 3◐ 4◐ 5◐ 6✓* 7◐ 8✗`. This shows how
  far the work has got above the foundation. Foundation 2 with `6✓*` is strong work with cheap
  holes underneath; foundation 0 with nothing above `◐` has barely started.
- **Operate**: the Operate levels, marked the same way (`Operate O1✓ O2✓* O3◐`), or
  `Operate –` when only people use the system.

Counting rules:
- A rule is required even when its mechanism in the stack profile is marked draft (†); the
  marking says the *mechanism* is unproven, not that the rule is optional.
- "Documented but never exercised" is not met: a workflow nobody has used, a CI file that
  has never run. A mechanism that runs and has been shown to work counts even if it is uncommitted.
- Score the working tree as it stands. Uncommitted work counts, and the report says which
  findings depend on it.
- Existing projects may adopt a reviewed, scoped maintainability baseline: new work cannot
  introduce unapproved violations or worsen existing ones. Specific reviewed debt does not
  by itself fail a rung; blanket exclusions, missing checks and unreviewed triggers do.
- Exclude a not-applicable rule from a rung only with a concrete reason (for example MT-3
  before anything has been replaced). Record it explicitly; missing mechanisms for an
  applicable rule are not "not applicable". The rung's other gates still apply.
- Only the repository counts: git-ignored or user-level personal settings do not protect the
  next developer or the next agent. No committed agent settings means GR-2 is not met.
- **Not verifiable** is only for facts that live outside the repository (host branch
  protection, who reviewed a pull request, the contents of a file the assessor may not read).
  It does not fail a rung; the report states it as an assumption, with the evidence used
  instead (docs, scripts, examples), for example "foundation 3, assuming branch protection".
- Security findings are not automatically accepted through a maintainability baseline.
  Record their risk decisions under SE-6. Assumed external controls may qualify a Build score,
  but cannot establish production readiness; missing evidence remains pending or blocked.
- Approval-record validation proves structure/content relationships, not human consent.
  Unavailable original source or reviewer authority remains an explicit assumption/gap,
  never an agent-created approval. If no changes have merged, RV-1 reports that history is
  absent and distinguishes configured enforcement from an exercised human review workflow.

## How much a project needs

`start` asks two questions and sets the target:

| | Prototype (will be thrown away) | Production |
|---|---|---|
| Breaks nothing important (personal tool) | Foundation 3 | Foundation 4, plus 5 |
| Internal business use | Foundation 4, plus 5 and 7 for what carries forward | Foundation 4, plus 5–8 |
| Customer data, money, safety, or writes into other systems of record | Foundation 4, plus 5 and 7 | Foundation 4, plus 5–8, and red-zone review (RV-3) |

"Writes into other systems of record" means anything hard to undo outside the project: an ERP,
a ticketing system, a machine or controller, a regulated document. Printing a label is not;
changing an order is.

A prototype that will be thrown away still writes **acceptance scenarios and decisions**: they
survive into the rebuild, and code is the cheap part. "Plus 5 and 7 for what carries forward"
means TS-1, TS-6, DC-1 to DC-3 and DC-5, not the whole rungs.

## Production security readiness

A Build score is a development-workflow assessment, not a security certificate or deployment
authorization. Before production use, regardless of the target rung, review all applicable
SE-1 to SE-6 requirements and deployed-control evidence for the release and environment.
Report readiness separately as **pending**, **blocked**, or **verified for the stated scope**,
with open risks and any explicit human acceptance. Undeployed controls stay pending; documented
settings alone cannot verify a deployment. Unaccepted blocking risks or expired acceptance
block readiness. Local skeleton evidence can satisfy the development portion of SE-4 while
production verification is still pending. See `security.md` for the evidence and decision rules.

## Operate: three levels

These apply when agents, scripts or AI assistants will use the built system: an API, MCP
tools, automation. Most guidance stops at agents *building* software; these levels cover
agents *using* it, where a mistake is a wrong write in production, not a red test.

| # | Level | Prevents | Gating rules | At it when |
|---|---|---|---|---|
| O1 | One contract | The UI, the API and agent tools disagreeing about what is allowed | OP-1, OP-5 | Every action is declared once and served to people and agents with the same access rules; credentials never travel in URLs |
| O2 | Safe by default | An agent with too much power, an unattributed change, a retry that doubles a record | OP-2 to OP-4 | Agent access is read-only until a person grants write, scoped to what it needs; every write records who acted and through which channel; a repeated request changes nothing |
| O3 | Bounded | An agent acting on planted instructions, overloading a system you do not own, or shipping code nobody reviewed | OP-6 to OP-8 | Text from data is treated as untrusted where agents read it; load on outside systems has a budget; agents draft definitions and a person publishes them |

Levels are marked like the rungs and climbed in order: O2 means little without O1. If agents
will use the system, a prototype targets O1 and O2, and production all three. Start O1 with
the first action: one contract retrofitted over many hand-built endpoints is the expensive
path.

## Scaling to the change

The process scales with the size of a change, not only the project. A typo fix needs no spec; a
new feature in a red zone needs the full interview. `spec` decides, so a small bug never becomes
sixteen acceptance criteria.
