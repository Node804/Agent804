# Core levels

Agent804 has a **core** and [modules](modules.md). Four cumulative levels describe how a
project is developed. Modules add protections when their triggers apply, including Operate
for MCP servers, agent APIs and embedded model features. They are scored separately.

## The four levels

Each level adds requirements to every earlier level. This table is an overview; the practice
table below is the sole gate-membership authority. Properties and checks live in [rules.md](rules.md).

| # | Level | Prevents | At it when |
|---|---|---|---|
| 1 | Guided | Reinvented conventions and unchecked work | Repository instructions guide agents; one check, also run by CI, reports style, complexity, security and isolated test results without rewriting files |
| 2 | Controlled | Irreversible actions, exposed secrets and unreviewed merges | Guardrails are exercised; a fresh clone boots; a representative end-to-end test and the check run in CI and block red merges; people review changes and public contracts explain behavior |
| 3 | Verified | Self-confirming tests, architectural drift and lost decisions | Agreed behavior has independent red/green evidence; architecture and maintainability properties are enforced; decisions retain their reasons and append-only evidence |
| 4 | Sustained | Undetected rework, stale guidance and structural decay | Results are measured over time and a scheduled gardening pass produces reviewed fixes or explicit decisions |

Level 0 means no core level earned yet. It is not a practice or a target.
`start` targets Level 2 before the first feature; `assess` reports the level actually supported.
The levels group protections for adoption, not an instruction to delay decisions or tests
until Level 2. Work within or above the next level can happen in any useful order.

## Practices behind the level

This table assigns each gate to one practice and introduction level. Eight named practices
explain progress without creating a second score:

| Practice | Introduced at | Gating rules |
|---|---|---|
| Instructions in the repository | Level 1 | IN-1, IN-3, CK-2 |
| One check command | Level 1 | CK-1, ST-1, MT-2, SE-2, TS-10, TS-12 |
| Guardrails | Level 2 | GR-1 to GR-4, GR-7, SE-3 |
| Walking skeleton and CI | Level 2 | SK-1, SK-2, CK-8, RV-1, MT-1 |
| Tests before code | Level 3 | TS-1 to TS-4, TS-8, TS-9 where bug fixes apply |
| Architecture and maintainability as checks | Level 3 | AR-1, AR-3, AR-6, CK-4, MT-3; AR-2, AR-4 where they apply |
| Decisions with evidence | Level 3 | DC-1 to DC-3 |
| Measure and garden | Level 4 | MS-1, MS-2 |

Every other core rule is a reported practice, not a gate. Module rules gate their module,
never a core level. [Testing](testing.md), [maintainability](maintainability.md),
[security](security.md) and the [host checklist](agents/README.md) explain the protections.
GR-4 requires truthful current verification evidence, not a hook. Automatic completion
checks belong to the opt-in Trial module (GR-8); missing/unsupported automation does not
block a core level. A configured host control is not evidence it runs.

## Scoring

Grade each applicable gate **met**, **partly met** (a protection has a hole), or **not met**
(missing protection), using the Check column in `rules.md`.

The **level earned** is the highest level for which every applicable gate introduced at
that level or any earlier level in the practice table is met. A partly met or not-met gate
blocks advancement. There is no
averaging or compensation from stronger work elsewhere. No gate met at Level 1 means Level 0;
some Level 1 gates met also means Level 0 until all are met.

Use these words for each named practice: **Met**, **Partial**, **Missing**, or **Not verified**.
Partial means some protection exists but at least one applicable gate is partly or not met;
Missing means none exists; Not verified means evidence is unresolved and no known gap exists.
List unresolved evidence alongside known gaps when both occur. Practice statuses explain the
gates; they never change the earned level, add requirements or create another aggregate score.
Individual gate grades determine the earned level, independently of practice-status labels.

An assessment reports:

- **Core: Level 2 — Controlled. Target: Level 3 — Verified.** Give the earned level first,
  then the target and any additional requirements. Never call a project its target level.
- **Progress toward Level 3:** name the practice statuses and the gates blocking advancement.
  Include lower-level blockers first and report useful strengths above the earned level.
  At Level 4, report remaining practice and module gaps without inventing a fifth level.
  When the target and its additions are met, say so; further advancement is optional.
- **Modules:** report separately using [modules.md](modules.md#reporting). A core level
  does not imply a module is met or grant permission to deploy.

For example, a local personal production tool could report:

> **Core: Level 2 — Controlled. Target: Level 3 — Verified.**
>
> Progress: tests before code — Partial; architecture checks — Met; decisions — Partial.
>
> Top gaps: acceptance tests share the implementation context (TS-3); decisions lack
> evidence records (DC-2). These block Level 3 even though architecture checks are met.
>
> Next: use a separate acceptance-test context for the next feature (TS-3).
> Optional follow-up: link decision evidence (DC-2).
> Modules: Operate – · Security – · Parallel – (triggers checked and absent).

Counting rules:
- A draft (†) mechanism does not make its rule optional.
- Documented but never exercised is not met. Running, demonstrated mechanisms count even
  if uncommitted; identify findings that depend on the working tree.
- A reviewed, scoped maintainability baseline may retain specific debt, but cannot waive
  missing checks, unreviewed triggers or new/worsening findings. Security is never waived
  through this baseline.
- Exclude a not-applicable gate only with a concrete reason, such as MT-3 before anything
  has been replaced. Keep its exclusion explicit; a missing applicable mechanism is a gap.
- For multi-mechanism rules, such as SE-2, all mechanisms must run for met; some running is
  partly met, none running is not met. Name missing mechanisms.
- Grade a missing piece once: a check without complexity enforcement is an MT-2 gap, not
  another CK-1 gap; a secret scan run only in pre-commit is an SE-2 gap.
- Tests that cannot run protect nothing: dependent execution rules are not met and the
  cause is the first gap. History-based TS-4 is not verifiable while no tests can run.
- Tests-before-code gates judge features since harness adoption (the commit introducing
  instructions or the check). With no such feature, mark TS-1 to TS-4, TS-8 and TS-9
  **not verifiable**; do not fail them based on pre-adoption code or invent retroactive
  red/green evidence. Unverified gates support only a provisional level, as below.
- Only repository-held protections count. User-level or ignored settings do not protect
  the next developer; no committed agent settings means GR-2 is not met.
- **Not verifiable** covers inaccessible external facts (branch protection, a reviewer's
  identity, restricted files) and the unexercised-history cases above. Do not count these
  as proved or missing. Report the highest level supported entirely by verified gates and,
  if higher, a **provisional level** assuming each named unresolved gate is met. Partial or
  not-met gates still block even the provisional level. Cite substitute evidence and the
  question that settles each assumption. For example: **Core: Level 1 — Guided;
  provisional Level 2 — Controlled, assuming CK-8 branch protection.**
  With no merged changes, RV-1 remains unexercised; configuration alone does not prove review.
- The target does not cap the earned level. Above-target gates graded **met** count normally
  under the cumulative rule. Unassessed gates cannot support advancement; mark them **Not
  assessed (above target)**. Examining above-target work does not make its gaps required
  target work. A target does not lower the standard for claiming a higher level.

## How much a project needs

`start` asks impact and prototype/production, then sets the target:

| | Prototype (will be thrown away) | Production |
|---|---|---|
| Breaks nothing important (personal tool) | Level 2, plus acceptance scenarios and decisions for what carries forward | Level 3 |
| Internal business use | Level 2, plus acceptance scenarios and decisions for what carries forward | Level 4 |
| Customer data, money, safety, or writes into other systems of record | Level 2, plus tests-before-code gates and decisions | Level 4, plus red-zone review (RV-3) |

Acceptance scenarios and decisions for what carries forward means TS-1, TS-6 and DC-1 to DC-3.
Tests-before-code gates means TS-1 to TS-4, TS-8 and TS-9 where bug fixes apply; decisions
means DC-1 to DC-3. These additions do not imply Level 3 without its remaining gates.
Every disposable prototype retains scenarios and decisions for anything carried into a rebuild.

Writing to another system of record means hard-to-undo external changes: orders, tickets,
machines or regulated documents. Generating a report does not count. Use the most demanding
row when several apply. Modules follow their triggers, not this table.

Compared with 0.4, personal prototypes now require the whole controlled harness, and personal
production tools also require architecture checks and decision evidence. Business and
high-impact production targets retain all former required gates. No old score converts
directly: regrouping, partial gates and unresolved evidence require reassessment.

In 0.6, core gate IDs remain unchanged, but GR-4 grades current completion evidence rather
than mandatory host blocking. Automatic completion checking is opt-in Trial GR-8. Reassess
prior hook-related findings; do not automatically promote levels without actual GR-4 evidence.

## Scaling to the change

The process scales with the change: a typo needs no spec; a new feature in a red zone needs
the full interview. `spec` sizes it. A core level describes exercised development protections,
not product correctness, security certification or deployment approval.
