# Technical-debt references and adoption limits

| Reference consulted | Reinforced | Limits and framework choice |
|---|---|---|
| [Fowler: Technical Debt Quadrant](https://martinfowler.com/bliki/TechnicalDebtQuadrant.html) | Deliberate/inadvertent and prudent/reckless debt, future interest and sometimes justified retention inform explicit tradeoff/deferral | A metaphor, not an objective accounting formula. No universal repayment deadline, score or sprint percentage |
| [SEI: Identify Technical Debt Items](https://www.sei.cmu.edu/library/managing-technical-debt-identify-technical-debt-items/), overview/abstract | Concrete inventory, consequences and impact over time inform ownership, prioritization and lifecycle records | Agent804 uses an existing tracker or small document, linking specialist records rather than requiring duplicate backlogs or claiming SEI conformance |

MT-5 is a reported practice pending trials, not a rung gate. Existing MT-2/MT-3, SE-6,
testing and approval obligations remain. Candidate discovery does not confirm debt; a debt
record does not authorize an exception, accept risk or make a failed check pass. The policy
and template define a proposed lifecycle and verification contract, not an implemented tracker.

Repository integrity checks verify rule references, links, portable metadata and budgets;
they do not establish human deferral decisions, economic benefit, correct prioritization or
actual repayment. Trials remain pending: confirm/reject a candidate, reuse a scoped deferral,
review an overdue/triggered item, repay through a feature/refactor, preserve identity after
renaming/partial closure and verify resolution without hiding a defect/security/test failure.
Record actual scope, ownership/authority, evidence, consequences and remaining gaps. No
external issues were created, messages sent or project debt accepted by this documentation.
