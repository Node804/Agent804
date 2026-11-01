# The rungs

Agent804 has a **core** and **modules**. The core is eight rungs, below: what every project
built with agents needs. [Modules](modules.md) cover problems a project has only in some
situations (agents calling the system, sensitive data, several writers at once) and are
scored only when their trigger applies. The largest is **Operate**: how the AI-facing parts of
a product are built, such as MCP servers and APIs for agents.

## The eight rungs

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
| 2 | One check command | "Looks done" code; inconsistent style, unchecked complexity and security | CK-1, ST-1, MT-2, SE-2, TS-10, TS-12 | One command, also run by CI, runs the formatter and linter without rewriting files, complexity limits, security scanners and isolated tests, and shows how many tests ran. A check that could not run is a gap, never a pass |
| 3 | Guardrails | Irreversible actions, exposed secrets, untrusted dependencies | GR-1 to GR-4, GR-7, SE-3 | No production secret within the agent's reach beyond a recorded read-only exception; commit, push, deploy and migrate need a person, and only a person gives approval; every change on a branch; the agent cannot finish with the check red; new dependencies are reviewed |
| 4 | Walking skeleton and CI | Unreviewed merges, undocumented contracts, works-on-my-machine | SK-1, SK-2, CK-8, RV-1, MT-1 | A fresh clone boots with one command; an end-to-end test runs in CI from committed state and blocks a red merge; a person reads every change before merge; public interfaces say what they do |
| 5 | Tests before code | Tests that only confirm the implementation; tests weakened to get green | TS-1 to TS-4, TS-8, TS-9 where bug fixes apply | At least two features since adoption have agreed criteria, tests written in a separate context and shown failing first, then passing; no test is weakened, skipped or deleted to get green; bug fixes keep a test that failed before the fix |
| 6 | Architecture and maintainability as checks | Slow drift; duplicated rules; obsolete code; injection | AR-1, AR-3, AR-6, CK-4, MT-3; AR-2, AR-4 where they apply | Access, boundaries and project invariants fail the build with messages that say how to fix them; input is parsed at the boundary and encoded for each destination; replaced code is removed or its retention is recorded |
| 7 | Decisions with evidence | Re-arguing settled choices; losing the reason | DC-1 to DC-3 | ADRs with Proposed / Validated / Accepted / Rejected, each with an append-only evidence record, accepted by a person (GR-7) |
| 8 | Measure and garden | Agent work that does not hold; stale docs and structural decay | MS-1, MS-2 | Corrections, rework, escaped defects, test reliability and maintainability trends tracked; a scheduled pass proposes reviewed fixes |

Every other core rule in `rules.md` is a **practice**: reported in the assessment, but not
gating a rung. Rules that belong to a module gate that module, never a rung; `modules.md`
lists them. Guides with the detail behind the rungs: [testing](testing.md),
[maintainability](maintainability.md), [security](security.md) and the
[host capability checklist](agents/README.md). A model name or a documented configuration
does not establish that an instruction loads or a hook runs; the checklist says what does.

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

An assessment reports three things:

- **Foundation**: count up from rung 1 and stop at the first harness rung that is neither met
  nor met with holes; the foundation is the rung below it. A missing protection is a real hole, however good the rest is; a protection
  with a gap is a hole to close, not a missing rung.
- **Coverage**: one mark per rung, for example `1✓* 2✓* 3◐ 4◐ 5◐ 6✓* 7◐ 8✗`. This shows how
  far the work has got above the foundation. Foundation 2 with `6✓*` is strong work with cheap
  holes underneath; foundation 0 with nothing above `◐` has barely started.
- **Modules**: each module whose trigger applies, marked the same way, and `–` for the rest
  (see [modules.md](modules.md#reporting)).

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
  Security findings are never accepted through that baseline.
- Exclude a not-applicable rule from a rung only with a concrete reason (for example MT-3
  before anything has been replaced). Record it explicitly; missing mechanisms for an
  applicable rule are not "not applicable". The rung's other gates still apply.
- A rule that names several mechanisms (SE-2's three scanners) is met when all of them
  run, partly met when at least one does, and not met when none does. Name the missing ones.
- Grade a missing piece once, under its own rule: a check command without a complexity
  step is an MT-2 gap, not a CK-1 gap as well.
- Tests that exist but cannot run (a broken migration, a missing service) protect nothing:
  every rule that needs a test run is not met, and the cause is the first gap reported.
- Only the repository counts: git-ignored or user-level personal settings do not protect the
  next developer or the next agent. No committed agent settings means GR-2 is not met.
- **Not verifiable** is only for facts that live outside the repository (host branch
  protection, who reviewed a pull request, the contents of a file the assessor may not read).
  It does not fail a rung; the report states it as an assumption, with the evidence used
  instead (docs, scripts, examples), for example "foundation 3, assuming branch protection".
  If no changes have merged yet, RV-1 says so rather than counting configured protection as
  an exercised review.

## How much a project needs

`start` asks two questions and sets the target:

| | Prototype (will be thrown away) | Production |
|---|---|---|
| Breaks nothing important (personal tool) | Foundation 3 | Foundation 4, plus 5 |
| Internal business use | Foundation 4, plus 5 and 7 for what carries forward | Foundation 4, plus 5–8 |
| Customer data, money, safety, or writes into other systems of record | Foundation 4, plus 5 and 7 | Foundation 4, plus 5–8, and red-zone review (RV-3) |

"Writes into other systems of record" means anything hard to undo outside the project: an ERP,
a ticketing system, a machine or controller, a regulated document. Generating a report is not;
changing an order is.

A prototype that will be thrown away still writes **acceptance scenarios and decisions**: they
survive into the rebuild, and code is the cheap part. "Plus 5 and 7 for what carries forward"
means TS-1, TS-6 and DC-1 to DC-3, not the whole rungs.

Modules come from their triggers, not from this table: the bottom row, for example, also
triggers the Security module. A Build score is never a security certificate or permission
to deploy.

## Scaling to the change

The process scales with the size of a change, not only the project. A typo fix needs no spec; a
new feature in a red zone needs the full interview. `spec` decides, so a small bug never becomes
sixteen acceptance criteria.
