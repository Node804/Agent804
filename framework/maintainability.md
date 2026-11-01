# Maintainability

A maintainer unfamiliar with a change can locate its behavior, understand its contract,
modify it within clear boundaries and verify the result using repository-held information.
This applies to experienced developers and agents. It is not a limit on total repository size,
but each file or module stays small enough to be read whole (MT-2).

The rules are MT-1 to MT-5, supported by IN-4, IN-5, AR-2, AR-3, SK-3, TS-2, MS-1 and MS-2
in [rules.md](rules.md). Limits and mechanisms belong in the [stack profiles](profiles/README.md).

## Find the relevant context

Keep a short navigation path from the root instructions to each meaningful area's purpose,
public interfaces, permitted dependencies and test command (IN-4). Add local guidance only
where declarations and existing docs do not explain enough. Do not reproduce a directory tree
or maintain a second inventory of every function. A small project may need only its README.

For a change, inspect the affected area and its callers before proposing a new implementation.
Search for an existing business rule, helper or stack capability. Record relevant reuse or a
reason to differ in the plan or review, not a transcript of every search.

Use [context management](context-management.md) to inspect enough source/caller/config/test
context and preserve evidence freshness. No search hits is not proof of no consumers;
truncation/index drift stays an explicit gap. Keep recovery state in existing plans.

## MT-1: Understandable contracts

Document what callers cannot reliably infer: valid input constraints, return meaning, failure
behavior, side effects, actor requirements, transaction boundaries and retry behavior where
applicable. Public includes internal module interfaces, commands and configuration consumed by
other areas, not only internet APIs. Small interfaces need small descriptions.

Explain why unusual constraints and workarounds exist. Prefer precise names and types to
comments that restate an assignment. Do not require a comment ratio or a docstring on every
private helper. Boilerplate that repeats a signature does not establish a useful contract.

Maintained links, configuration examples and runnable examples are checked where practical
(IN-5). Mark historical records explicitly; a frozen ADR describing an old state is not a
current operating guide. Update maintained descriptions with behavior and review them against
implementation and tests. Presence can be checked; accuracy still needs judgment.

## MT-2: Controlled complexity

Before new implementation, choose stack-appropriate enforceable limits and review thresholds
in `docs/maintainability.md`, using the project template. A missing mechanism is a gap to
report, not permission to declare the rule met. Unsupported checks stay explicit in profiles.

| Signal | Treatment |
|---|---|
| Function control-flow complexity | An enforceable limit selected for the stack |
| Nesting and excessive branching | An enforced limit where reliable, otherwise a documented review trigger |
| File or module size and dependency spread | Review triggers; inspect responsibility and coupling |
| Duplicate blocks | Investigate whether they express the same business rule |
| Unused code or dependencies | Investigate runtime use before removal |

A limit breach fails the check unless covered by a narrow, reviewed exception. A review
threshold requires a recorded disposition; it is not an automatic demand to split a file.
If threshold reports do not block CI, review must still resolve new reports before merge.
Generated and vendored code can be excluded by precise paths with reasons; authored wrappers,
tests and scripts remain in scope unless separately justified.

An exception identifies the rule or signal, exact scope, reason, reviewer and review date or
event. When that condition occurs, resolve or renew it explicitly. Do not disable a check for
a whole package to suppress one function's finding. Add an ADR only for a hard-to-reverse
decision; routine exceptions belong in the maintainability record.

## Reuse, boundaries and refactoring

AR-2 assigns an authoritative home to each business rule. When a rule changes, find its other
representations. Derive them where practical; retain independent copies only for an explicit
reason, such as independently changing domains. Similar syntax alone does not justify a
shared abstraction. Test setup may intentionally repeat to keep cases understandable.

AR-3 requires cohesive responsibilities and declared dependency directions. Splitting a large
file into tightly coupled fragments does not improve the boundary. Unapproved dependency
cycles fail the check. Review whether an ordinary change forces unrelated modules to change.

SK-3 applies to dependencies and custom code alike: identify the requirement, existing
capabilities, alternatives and maintenance cost. Do not implement a custom parser or framework
merely to avoid a dependency; do not add one merely to avoid a small, clear function.

After tests turn green, inspect structure and duplication (TS-2). Make justified refactoring
separate from behavior changes where practical, and keep tests green. Record "no refactor
needed" when appropriate; the process must not invent unrelated cleanup work.

## MT-3: Complete retirement

Trace what the new implementation replaces: callers, old execution paths, configuration,
dependencies, documentation and examples. Remove what is obsolete within the change's scope.
Retain compatibility code only with its consumers, reason and review condition recorded.

Unused-code reports are leads, not deletion instructions. Investigate dynamic registration,
plugins, external consumers, operations scripts and migrations. Historical migrations and
supported public contracts may be required even when static searches find no current caller.
If usage is uncertain, preserve the item, record the uncertainty and propose investigation.

## MT-4: Verified refactoring (practice)

Refactoring changes internal structure while preserving observable behavior. State the
maintenance problem and affected preservation contract before restructuring: relevant APIs,
outputs/errors, side effects, security controls, configuration/serialized formats, transactions
and performance constraints. Analyze consumers, including dynamic and external ones.

Establish baseline checks first. Where protection is weak, add focused characterization tests
that document observed behavior before restructuring. They may pass immediately; no artificial
red failure is needed. Record known bugs as defects, not approved requirements. Passing tests
support only their exercised scope and never prove complete equivalence. Record missing
compatibility evidence and constrain the change accordingly.

Make small transformations, verify incrementally, and run the full check on the combined
result. Behavioral or material architecture changes follow the existing criteria/ADR/approval
process, separately from structural work. Update consumers and contracts; apply MT-3 to retired
paths. Routine in-scope refactoring requires no new permission for every extraction.

The [refactor playbook](../skills/refactor/SKILL.md) covers standalone and substantial
preparatory work; ordinary red/green/refactor remains part of development. Use existing
plan/PR evidence rather than a mandatory new artifact. Record the maintenance improvement,
baseline/final results, affected contracts, consumers and verification limits. MT-4 is reported
as a practice at rung 6 pending application trials; it adds no rung or scoring gate.

## MT-5: Accountable debt disposition (practice)

Use the [debt lifecycle](technical-debt.md) for confirmed maintenance consequences and
justified deferral: one authoritative record, owner, evidence, disposition, review condition
and verifiable closure. Candidate reports need confirmation. Link existing MT-2 baselines,
MT-3 retention records and specialist security/test obligations; don't duplicate authorities.
A ticket alone grants no exception or acceptance. MT-5 is reported, not a rung gate.

## Adopt in an existing project

1. Run the available checks and inspect the affected architecture and documentation.
2. Record specific existing findings against an exact revision or preserved patch. Each has
   a location, observed value where applicable, reason, reviewer and review condition.
3. Enforce no new unapproved violations or worsening findings. A renamed or moved finding
   keeps its identity and history; moving code does not erase debt. Review each new trigger.
4. Fix relevant problems within a change's scope. Schedule broader improvements separately;
   do not require a repository-wide rewrite before useful work can continue.

A baseline records reviewed debt; it does not waive controls. Blanket exclusions, missing
checks, stale exceptions and undisposed new triggers are gaps. For assessment, MT-1 needs
useful current contracts, MT-2 needs exercised checks and reviewed dispositions, and MT-3
needs evidence from actual replacement changes or an exercised replacement fixture. A new
skeleton with nothing retired can have MT-3 not applicable yet; say so rather than invent use.

## Measure and exercise

MS-1 tracks comparable complexity, duplication and aging-exception trends alongside test
reliability. Record tool versions, scope and baseline changes so numbers are interpretable. A
change in a metric is a signal to investigate, not proof of a cause or a developer ranking.
MS-2 reviews structural drift and retention decisions during gardening.

For example, change one validation rule using the area's public interfaces and local tests.
Success means the behavior is understood, modified and verified without unexplained coupling.
Choose suitable expectations for the task; do not impose a universal time or context budget.
Record exercises in `docs/metrics/maintenance-exercises.md`. A request to report metrics alone
does not authorize implementation changes as part of an exercise.

## References

- [PEP 8 comments and documentation](https://peps.python.org/pep-0008/#comments)
- [GitClear's maintainability analysis](https://www.gitclear.com/the_ai_code_quality_maintainability_gap)

The first informs accurate, useful comments; the second is vendor observational research
supporting investigation of duplication, reuse and churn, not proof that a particular agent
caused a defect. The maintainability gates remain to be trialled on projects.
