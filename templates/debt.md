# Technical debt record

<!-- Use this as docs/debt.md for a small project, or adapt each item to the existing tracker.
Choose one authority; other docs link to it. Do not invent debt to fill the template. -->

- Authoritative location: <this file OR tracker/project location>
- Triage/review owner and cadence: <actual role/person and project-selected interval>
- Links to specialist records: <maintainability baseline/exceptions, security, tests, ADRs>

## <DEBT-n>: <concrete problem>

- State: Candidate | Open | Deferred | In progress | Resolved | Rejected
- Scope/location/consumers: <actual symbols/paths/components and compatibility users>
- Evidence: <finding/reproduction and revision/patch; facts versus uncertainty>
- Consequence: <observed change/operating cost, failures or limits; estimates labelled>
- Owner: <actual responsible role/person; unknown is a triage gap>
- Origin/related work: <introduced/discovered/inherited; issue/plan/PR links>
- Impact/exposure: <frequency, planned changes, support/expiry events, uncertainty>
- Disposition/deferral reason: <repay now, schedule, retain; benefit and future consequence>
- Decision/source: <actual human approval covering deferral where required; none/pending is not consent>
- Review date/event: <date with timezone where material, or concrete trigger and responsible owner>
- Repayment deadline: <only if explicitly required/agreed; distinguish from review date>
- Linked exceptions/security findings: <canonical IDs, scope/expiry or none; no waiver granted here>
- Repayment approach and dependencies: <small bounded work; scope/authority still applies>
- Completion criteria: <specific verifiable outcomes, not merely "code changed">
- Closure evidence/review: <actual revision, commands/results or other applicable evidence, reviewer; pending until real>
- History: <dated discovery/decision/review/scope change/closure; preserve prior entries>

Candidate findings need confirmation. Defects, security findings, missing requirements and
test gaps keep their applicable rules; a debt label does not declare them acceptable.
Never close from a rename/move or renew an exception automatically. Partial repayment keeps
remaining scope open with links. Store sensitive evidence separately with safe references.
