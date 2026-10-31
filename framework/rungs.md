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
| 2 | One check command | "Looks done" code that does not run | CK-1 | One command runs format, lint, types and tests; the agent runs it and it is green |
| 3 | Guardrails | Irreversible actions, leaked production secrets | GR-1 to GR-4 | No production secret within the agent's reach; commit, push and deploy ask; work happens on branches; the agent cannot finish with the check red |
| 4 | Walking skeleton and CI | Every session rediscovering how to run things; drift between machines | SK-1, SK-2, CK-8 | The app boots from one command, one end-to-end test passes, and the check has run independently of the author's working tree before a change merged |
| 5 | Tests before code | Tests that only confirm what the agent built | TS-1 to TS-3 | Every feature since the workflow was adopted, at least two, starts from agreed acceptance criteria; tests are written by another context and seen failing first |
| 6 | Architecture as checks | Slow drift; the same fact copied into many places | AR-1, AR-3, CK-4; AR-2, AR-4, AR-5 where they apply | Access, boundaries and the project's own invariants fail the build when broken, with messages that say how to fix it |
| 7 | Decisions with evidence | Re-arguing settled choices; losing the reason | DC-1 to DC-5 | Quality scenarios with stable IDs; ADRs with Proposed / Validated / Accepted / Rejected, citing the scenarios they serve, with evidence lines, accepted by the owners |
| 8 | Measure and garden | Believing you are faster when you are busier; stale docs | MS-1, MS-2 | Lead time, interventions, first-pass CI rate and escaped defects tracked; a scheduled pass fixes stale docs |

Every other rule in `rules.md` is a **practice**: reported in the assessment, but not gating a
rung. The OP rules gate the Operate levels instead.

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
- Only the repository counts: git-ignored or user-level personal settings do not protect the
  next developer or the next agent. No committed agent settings means GR-2 is not met.
- **Not verifiable** is only for facts that live outside the repository (host branch
  protection, who reviewed a pull request, the contents of a file the assessor may not read).
  It does not fail a rung; the report states it as an assumption, with the evidence used
  instead (docs, scripts, examples), for example "foundation 3, assuming branch protection".

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
