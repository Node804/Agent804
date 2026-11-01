# Technical-debt references and adoption limits

| Reference consulted | Reinforced | Limits and framework choice |
|---|---|---|
| [Fowler: Technical Debt Quadrant](https://martinfowler.com/bliki/TechnicalDebtQuadrant.html) | Deliberate/inadvertent and prudent/reckless debt, future interest and sometimes justified retention inform explicit tradeoff/deferral | A metaphor, not an objective accounting formula. No universal repayment deadline, score or sprint percentage |
| [SEI: Identify Technical Debt Items](https://www.sei.cmu.edu/library/managing-technical-debt-identify-technical-debt-items/), overview/abstract | Concrete inventory, consequences and impact over time inform ownership, prioritization and lifecycle records | Agent804 uses an existing tracker or small document, linking specialist records rather than requiring duplicate backlogs or claiming SEI conformance |

In 0.3 Agent804 defined its own debt lifecycle: six states, prioritisation and closure
procedure. Since 0.4 it keeps only what agents change (they create debt faster, invent
candidates, expand scope and must not defer debt themselves) and leaves tracking to the
project's existing tracker and practice. MT-5 is in the Maintenance module, a trial: nothing
here has run on a real project yet.
