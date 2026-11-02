# Security

Agent804 is not a security standard. For what to require, use
[OWASP ASVS](https://asvs.owasp.org/) (versioned application requirements); for development
practices, [NIST SSDF](https://csrc.nist.gov/projects/ssdf); for building a security
programme over time, [OWASP SAMM](https://owaspsamm.org/). This page covers what coding agents
change about security, and which rules hold a project to it.

SE-2 and SE-3 are core, at levels 1 and 2. SE-1 and SE-4 to SE-6 form the Security
[module](modules.md#security), scored when a breach would hurt someone other than the
developer. Keep the project's record in `docs/security.md` from the
[template](../templates/security.md); keep secrets and incident details out of it.

## Core

**SE-2: scanners in the check, and an honest result.** Secret detection, static analysis
and dependency checks run in the one check and CI, mapped in the stack profile. Agents treat
"no output" as "clean". A scanner that errored, was skipped, or ran on a stale advisory feed
is a gap, never a pass: an unchanged tree or a cached stop-hook success does not refresh
vulnerability data. Plant a harmless fixture once to prove each scanner fails, then remove it.

**SE-3: reviewed dependencies.** Agents add packages freely, including plausible names that
do not exist and can be registered by an attacker. Before installing, verify the publisher and
the package identity; registry presence and a familiar name prove nothing. Review install
hooks, build plugins and CI actions before adding them; an audit command can itself run
package code. Lock versions with integrity hashes, and build cleanly with scoped credentials.
No production credentials or sensitive production data enter agent sessions, and none
enter install jobs (GR-1). When production is the only source to develop against, GR-1
allows one development credential: decided by a person, read-only and limited to
non-sensitive data by the source itself, rate-limited, and separate from production's own.

**Protect the harness.** An agent stuck on a red check will be tempted to weaken the check.
Changes to security checks and tests, CI gates, permissions, approval policy and deployment
controls need explicit human review (GR-2, RV-3), judged by consequence, not by file type:
a Markdown instruction file can change behaviour as much as code.

## Security module

**SE-1: write the threat model down, where agents read it.** An agent builds what it is
asked, quickly, and does not know which data is sensitive or which boundary matters unless
the repository says so. Record the assets, users, trust boundaries and credible abuse cases in
`docs/security.md`, linked from `AGENTS.md`. Include the agents themselves: outside text an
agent reads may carry instructions (OP-6), and installing or building runs code. Select
requirements from a versioned standard such as ASVS, keep their version in the identifiers,
and record exclusions with a reason. Selecting some requirements is not compliance with the
standard. Assign an owner, and revisit when exposure or data changes.

**SE-4: safe defaults, enforced in the application.** Agents copy insecure defaults from
examples (debug on, wildcard hosts, permissive cross-origin settings), write their own
authentication or cryptography, and put access checks only in the UI. Use the framework's own
mechanisms; enforce access server-side, including object and tenant checks, on every path
(alternate APIs, background jobs, direct URLs). Missing production configuration fails safe.
Production controls are verified in the real environment by an authorized person or
deployment check; an agent never acquires production secrets to do it.

**SE-5: abuse tests written first.** Security-affecting changes get refusal criteria in the
spec, and the separate test context writes tests for them like any other criteria: the
unauthorized attempt fails, and nothing was written, disclosed or sent. For agent tools,
plant instructions in test data and show the tool's real permissions hold; an agent saying it
ignored the text proves nothing.

**SE-6: owned findings, and decisions only a person makes.** Every finding has an owner, a
deadline and a recorded outcome. An agent may propose accepting a risk but cannot accept it
(GR-7); a suppression comment is not an accepted risk, and a risk acceptance has a scope and
an expiry. Removing a leaked secret from the source does not revoke it: rotate it. Responding to an
incident follows the organisation's own procedure. A security record never authorizes an agent
to access production or send messages.

