# Technical debt

Tracking debt is ordinary engineering management, and Agent804 does not redefine it. Use the
project's issue tracker, or a small `docs/debt.md` from the [template](../templates/debt.md),
and whatever practice the team already has. For the idea itself, see Fowler's
[Technical Debt Quadrant](https://martinfowler.com/bliki/TechnicalDebtQuadrant.html) and the
SEI's guidance on [identifying debt items](https://www.sei.cmu.edu/library/managing-technical-debt-identify-technical-debt-items/).

What agents change, and what MT-5 asks for because of it:

- **Agents create debt faster.** Duplicated logic, a workaround beside the real fix, an old
  path left next to the new one. Review and `garden` look for these; MT-2 and MT-3 catch
  some mechanically.
- **Agents also invent debt.** A scanner warning or an agent's "this could be cleaner" is a
  candidate until someone confirms a real consequence: slower changes, repeated workarounds,
  failures. Don't fill a tracker with style preferences, and a new project needs no entries.
- **A debt record never waives anything.** It cannot make a failing check pass, accept a
  security finding, excuse a defect or stand in for an unmet acceptance criterion. Those keep
  their own rules (SE-6, TS-4, MT-2).
- **Only a person defers debt.** An agent may record an item and propose what to do, but the
  decision to live with it is a person's (GR-7), with a reason and a date or event to look
  at it again.
- **Agents expand scope.** Repay debt in its own scoped change, through
  [`refactor`](../skills/refactor/SKILL.md), not as cleanup slipped into a feature.
- **Closing needs evidence of the outcome.** "Done" means the stated problem is gone (the
  consumer migrated, the old path removed), shown by results, not that some code changed. A
  rename or move never closes an item.

MT-5 belongs to the Maintenance module, which is a trial: `assess` reports it without a mark.
