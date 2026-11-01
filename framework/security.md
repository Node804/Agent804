# Security baseline

Security covers three different things: the agent's development environment, the application
it builds, and the released system in its real environment. A sandbox protects the first;
it does not prove the other two safe. SE-2 and SE-3 are core, at rungs 2 and 3. SE-1 and
SE-4 to SE-6 form the Security [module](modules.md#security), scored when a breach would hurt
someone other than the developer. Neither is a certification.

Keep the project's scope, requirements, evidence and finding decisions in `docs/security.md`
from the project template. Keep secrets and sensitive incident details out of this record;
link to restricted evidence where necessary. A small tool can have a short record.

## SE-1: Requirements and threats

Before substantive implementation, identify assets and data sensitivity, users and operators,
machine identities, interfaces, trust boundaries, dependencies and credible abuse cases.
Consider build/install execution and agents consuming outside text as well as runtime input.
Assign an accountable human owner. Revisit the model when exposure, data or behavior changes.

Use NIST SSDF 1.1 to select development practices and OWASP ASVS 5.0.0 for applicable web
application requirements, or another justified baseline for a different product. Read the
selected requirements, pin their version and identifiers, and map them to controls, criteria,
verification and owners. ASVS identifiers include their version; unversioned IDs can drift.
Do not infer compliance with an entire standard or level from a selected subset.

| Area | Select controls appropriate to the product |
|---|---|
| Identity and access | Authentication, server-side authorization, object/tenant isolation and least privilege |
| Input and output | Validation, safe queries/commands, contextual output handling and serialization |
| Sessions and browsers | Session lifecycle, cookie protection, CSRF and cross-origin policy |
| Files and network | Upload/path controls, outbound destinations, SSRF defenses and resource limits |
| Sensitive data | Established cryptography, appropriate transport/storage protection, rotation and retention |
| Errors and audit | Useful security events without leaking secrets, sensitive data or diagnostics |
| Availability | Request size, expensive operations, concurrency and retry limits |
| Supply chain and development | Dependency identity, install/build authority, safe test data and protected CI |

Record requirements as applicable or excluded with a concrete reason and reviewer. Missing
implementation is not an exclusion. Local tools and internal applications still assess their
real exposure; being private or a prototype is not a blanket exemption.

## SE-2: Verification and findings

The stack profile maps applicable secret detection, static analysis, dependency checks,
configuration checks and security tests into the project's one check and CI. Define scope,
versions, feed/report freshness, expected coverage, blocking policy and report handling.
Use harmless isolated fixtures to confirm representative failures, then remove them.

Distinguish findings from tool errors, skipped coverage and unavailable feeds. None means
"clean". Required unavailable or stale checks fail verification or remain explicit gaps;
never hide their exit status or silently drop a step to obtain green. Retain redacted reports
with revision, command, time, tool/feed version and limitations. Manual evidence supplements
automation where a control cannot be proven mechanically.

Time-dependent checks need current evidence: an unchanged tree or cached stop-hook success
does not refresh vulnerability advisories. Configure fresh CI/release verification and the
refresh cadence. Offline reports are usable only within the declared freshness policy and
coverage; a disconnected scanner is not evidence of no vulnerabilities.

## SE-3: Dependencies and builds

Verify the intended publisher/source and package identity before installation, including
transitive and build dependencies where practical. Registry presence and a familiar name do
not establish trust. Review new dependency sources, install hooks, build backends, plugins,
CI actions and generated execution before introducing them. Resolution and audit commands
can execute package code; do not assume an audit tool makes untrusted installation safe.

Resolve reproducibly using locked versions and integrity information supported by the stack;
record origins and immutable references for build inputs and release artifacts where
applicable. Keep scanners/build tools supported and pinned too. Exercise a clean build with
scoped credentials, restricted authority and reviewed network access. No production data or
production credentials enter agent sessions, install jobs or untrusted contributor CI.
Sensitive test data must be synthetic or reviewed sanitized data (GR-1).

## SE-4: Runtime and deployment

The skeleton demonstrates safe initial defaults and refusal behavior before more features
are added. Each later feature preserves the applicable requirements. Use established stack
security mechanisms rather than custom authentication or cryptography without justification.
Enforce access in the application, including object/tenant checks; a login wall alone is not
authorization. Inspect alternate adapters, background jobs, direct URLs and error paths.

Define environment-specific settings, least-privilege service/database accounts, secret
provisioning, network exposure, transport protection and safe logging. Development exceptions
must be explicit and cannot silently carry into production. Missing required production
configuration fails safely. A credential-free exposed production service is still a security
finding even when there is no secret for an agent to leak.

Before production use, verify applicable controls in the actual target environment using an
authorized operator or deployment check; agents do not acquire production secrets to do so.
Record release/artifact identity, environment, verifier, time, tests, results and open risks.
Local settings checks and deployment-shaped tests are useful but are not deployed evidence.

## SE-5: Acceptance and abuse cases

Specs cite the applicable security requirements and define observable refusal outcomes.
Tests cover realistic bypasses and assert both the response and absence of prohibited writes,
disclosure or external effects. Include cross-user/object/tenant attempts, malformed inputs,
alternate paths, concurrency, timeouts or resource limits where the threat model calls for
them. Verify positive authorized behavior too; a system refusing everything is not correct.

For agent tools, model planted instructions in data and prove restricted authority holds
(OP-6). A threat ADR or an agent saying it ignored the text is insufficient: inspect actual
permissions and attempted actions. Use isolated test resources, never live victims or data.
When the Security module applies, the skeleton carries initial refusal evidence, and later
security-affecting features get abuse tests written first like any other criteria.

## SE-6: Ownership and response

Every finding records affected scope, exposure, exploitability, impact, severity and evidence,
owner, response deadline, disposition and verification of resolution. Define concrete
project-specific deadlines and escalation for urgent exposure; severity alone is insufficient.
Re-evaluate when advisories, exposure, mitigations or supported versions change.

Disposition is remediation, justified false positive/not affected, or explicit human risk
acceptance. Acceptance identifies accountable approver, scope, reason, compensating controls,
expiry and review triggers. Agents can propose it but cannot accept it. Expiry restores the
blocking decision until remediation or explicit renewal. Suppressions must link to the
decision; an ignored scanner finding is not an accepted risk.
Apply [approval provenance and freshness](approvals.md) to these human decisions. Link the
authoritative risk decision/source rather than maintaining competing approvals in two places.

Unlike a maintainability baseline, recording existing security debt does not authorize its
continued exposure. Apply the release-blocking policy to existing and new findings. Do not
weaken controls to unblock unrelated work; report blockers and continue unaffected work.

Define suspected-exposure steps: notify the responsible person, contain within authorization,
revoke/rotate compromised credentials, preserve appropriate restricted evidence, assess impact,
remediate and verify recovery. Removing a secret from source does not revoke it. Exercise the
procedure safely with a tabletop or isolated fixture before claiming it works; include
recovery verification appropriate to the product. A security record does not authorize agents
to send messages, access production or make disruptive changes.

## Protect the harness

Changes to security checks/tests, CI gates, approval policy, deployment controls and permissions
need explicit human review, proportionate to scope (GR-2, RV-3). Zone by consequences, not
extension or directory: documentation may execute as instructions and tests may enforce access.
Protect required reviews/gates at the host or administrative boundary where possible; prose or
a check editable by its own author is insufficient protection. Existing authorization for the
specific change need not be requested repeatedly; record the reviewed scope and revision.

## Report readiness separately

| Status | Evidence |
|---|---|
| Pending | Required evidence or human decision is missing, including undeployed controls |
| Blocked | Release policy rejects a finding, required verification failed, or acceptance expired |
| Verified for the stated scope | Applicable controls have current evidence, or permitted scoped human decisions identify specific gaps, for the release/environment; all open risks and acceptances are listed |

All applicable production requirements need evidence or a permitted scoped human risk decision
regardless of Build target. An assumption about an external control cannot verify readiness.
Risk acceptance records a gap and its consequences; it never relabels an untested control as
verified or establishes conformance with a standard whose requirements have not been met.
Recheck material changes and evidence expiry. This status is not deployment authorization,
a guarantee of security, or certification to a standard. The new gates and profile mechanisms
remain untrialled until exercised on a real project.

## References

- [NIST SSDF](https://csrc.nist.gov/projects/ssdf): development lifecycle and response practices.
- [OWASP ASVS](https://asvs.owasp.org/): versioned application security requirements.
