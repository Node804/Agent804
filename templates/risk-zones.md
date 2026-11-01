# Risk zones

A person draws this map; agents follow it. Zones follow how much damage a change could do and how
hard it is to undo, never how confident the agent is.

| Zone | What an agent may do | Review |
|---|---|---|
| Green | Change freely within the plan | Normal review |
| Yellow | Change behaviour only with acceptance criteria agreed first | Review against the criteria, line by line |
| Red | Propose; stop and ask before changing behaviour | Named reviewer, every line; tests for the refusal paths |

## Map

| Path or area | Zone | Why |
|---|---|---|
| <auth, permissions, tokens> | Red | Mistakes expose data to the wrong people |
| <anything that writes to an outside system, money, or equipment> | Red | Hard or impossible to undo |
| <security policy/tests, CI gates, approval mechanisms, deployment controls> | Red | Changes can remove protection; explicit human review of scope and revision |
| <database migrations> | Yellow | Reversible, but data loss is possible |
| <feature modules> | Green | |
| <ordinary docs, tests, tooling with no security-enforcement impact> | Green | Reassess by consequences; security controls are not green because of their directory |

An agreed scope authorizes covered work; do not repeatedly ask for the same approved change.
Material changes to risk or scope need renewed review. Record review through the project's
normal mechanism; a zone map alone cannot enforce host permissions or protected CI gates.
Do not infer commit, push or deployment authority from agreement on a feature or a zone.
