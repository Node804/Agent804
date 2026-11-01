# Traceable human approval

An approval is a durable human decision about an identified subject and scope. It answers
what was reviewed, by whom, under which authority and conditions, and whether it still applies.
AP-1 to AP-4 in [rules.md](rules.md) extend the existing workflow; no extra rung is added.

## Different decisions, reusable scope

| Decision | Human question |
|---|---|
| Feature scope | Is this the intended problem, value and boundary? |
| Spec/criteria | Are observable success, refusal and failure outcomes correct? |
| Architecture | Are the approach, constraints and consequential tradeoffs acceptable? |
| Implementation | Does the reviewed change satisfy criteria and project rules? |
| Restricted action | May this particular commit, push, migration, deployment or other action proceed? |

A human may approve several named decisions together when they were clearly presented.
Record that grouped scope once and link it rather than requesting the same permission again.
Implementation within approved scope may continue. Feature approval does not itself permit
commit/push/deploy; an explicit authorization may cover a named sequence without repeated
prompts. Release readiness and risk acceptance retain their own conditions and expiry.

Set the reviewer policy in `docs/approvals/README.md`: who owns requirements, architecture,
review and action authority; required independent review; how decisions are sourced; and
which revisions/actions each stage requires. A small project may use one owner for several
roles, but must state the independence limits rather than inventing another reviewer.

## Preserve decisions and subjects

Use existing host reviews as authoritative evidence where available. Repository records can
index them; do not duplicate private conversations or sensitive artifacts unnecessarily.
The portable starter is [approval.json](../templates/approval.json), copied as a unique flat
`docs/approvals/APP-<id>.json`. It begins Pending and grants no authority. The
[policy template](../templates/approvals.md) records stage requirements and source verification.

Each completed decision identifies its kind, subjects/revisions, scope, reviewer identity and
role, timestamp with timezone, original source, conditions, dependencies and any supersession
or revocation. Ordinary approvals need no arbitrary expiry; risk acceptance requires one.
Retain decisions append-only. Revocation/replacement uses a new sourced record pointing back
to the old decision; never quietly rewrite a past approval to cover changed requirements.

Keep review snapshots outside the live subject and approval record. A commit/path or retained
snapshot can identify the content shown; a hash alone neither preserves it nor proves consent.
Preserve uncommitted content or a patch with its base, including new files and relevant
dependencies. A patch must be regenerated/compared through trusted project integration before
it can establish what the current code change contains. A stable filename is not a revision.

An Accepted ADR remains frozen except its permitted metadata. Predeclare an approval-index
link before acceptance or index the frozen ADR externally in `docs/approvals/README.md`;
do not reopen it merely to add an approval link. An approved status transition is a derived
workflow update, not a request to renegotiate the decision.

## Human provenance, not self-approval

Agents may prepare records and accurately index real decisions, but cannot manufacture
reviewers, timestamps, links, message IDs or approval. An agent review is not a human review.
A status field or reviewer name is not proof. Verify the original source and reviewer's
authority, including any latest-change/independence policy, before dependent work.

When a conversation is the source, retain its real locator/export where available and the
subject presented with it. If no independently retrievable source exists, label that limit;
do not invent one or claim authenticated provenance. Existing explicit authorization in the
current conversation still governs work within scope, but a later audit must distinguish
session evidence from an independently verifiable record. Do not ask again just to fill a
missing metadata field; record the limitation and follow the project's assurance policy.

Use host permissions and protected review/check rules where supported. A human-readable
record editable by the agent cannot enforce its own integrity or authenticate its author.
Signatures/attestations may strengthen evidence in higher-assurance projects, but are not a
universal requirement or a substitute for explicit decision meaning. This is not a claim of
compliance with a signing or supply-chain standard.

## Freshness and changes

Before dependent work, check original evidence, required scope, subjects and approval
dependencies, conditions, revocation and any expiry. Unrelated file edits do not stale an
approval for a specific spec. Implementation review follows the actual reviewed change and
host/project latest-review policy, not a blanket permission from earlier feature agreement.

Material changes to requirements, criteria, architecture, security exposure or action scope
renew affected approvals. Conditions not yet satisfied keep the dependent action pending;
silence, elapsed time and passing tests are not acceptance. Revocation or expired acceptance
blocks covered actions until resolved by an authorized human.

Content changes trigger a freshness review, not automatic semantic revocation. Define narrow
permitted administrative transitions in policy, such as recording Agreed/Built or Accepted
after the relevant decision/evidence. Record old/new revision, reason, policy and original
authorization without inventing another human decision. Never classify changed criteria or
expanded access as cosmetic. Unapproved material changes need a new decision.

## Portable mechanical validator

Copy [check_approvals.py](../templates/check_approvals.py) into the project's scripts directory.
It uses only Python 3.11+ in the supported starter environment; another stack may implement
the same record contract natively rather than add Python. The project check validates the
index; before a stage, its trusted integration selects the exact required IDs. Example:

```text
python scripts/check_approvals.py --root . --records docs/approvals
python scripts/check_approvals.py --root . --records docs/approvals --require APP-0001
```

The default validates flat JSON records, preserved snapshot hashes, relations and dependency cycles,
including historical decisions. Required-ID checks additionally inspect approved/active
decisions, current subject bytes, dependencies, conditions/expiry and current trace paths.
Record subject objects as `path`, separate `snapshot` and raw-byte `sha256`; use portable
root-relative paths. Source objects contain `kind`, actual `reference` and optional local
`evidence`. Reviewer objects contain `identity` and `role`; these are claims to verify.
Condition objects contain `text`, `status` (pending/satisfied) and verification `evidence`.

This starter supports byte-for-byte local-file freshness, not Git-host authentication,
automatic materiality, test execution, deleted-file semantics or arbitrary revision adapters.
It conservatively flags status/format changes too. A project needing permitted administrative
transitions or host-reviewed changes must add a narrowly reviewed native adapter/disposition
check, or retain an independently versioned decision-content subject with mutable lifecycle
metadata elsewhere. Do not reapprove already-authorized work merely because a byte checker
cannot interpret it, silently rewrite its reviewed hash, or bypass the mismatch without the
policy/source evidence. Report unsupported integration as a gap.

A zero exit proves mechanical checks only. It does not authenticate a human, prove their
authority, evaluate condition truth, identify all relevant files or authorize any action.
`--require` IDs come from trusted stage policy, not an agent choosing its own easiest record.
Source verification and scope checks remain mandatory even after a mechanical pass.

## Trace requirements to outcomes

AP-4 uses stable requirement and criterion IDs: requirement -> agreed criterion -> tests ->
reviewed implementation -> actual verification result. A small fix can use issue/plan/PR
IDs; do not require separate feature/spec/ADR documents for every change.

Record the trace in the plan/PR or implementation decision and link it. Portable JSON trace
rows contain `requirement`, `criterion`, and lists of `tests`, `implementation` and `evidence`
references; test references may use `path::test-name`. Paths alone do not prove test coverage.
Early feature/spec approval may have no implementation trace yet; never invent future tests
or passing evidence. Append a later implementation record/trace, preserving the earlier
decision and citing it through dependencies. Resolve missing coverage and unrequested
behavior before acceptance. Actual revision/results, not checkbox completion, are evidence.

## Prove and assess

Exercise valid scoped reuse, an unrelated edit, changed criteria, missing source, pending
conditions, revocation/supersession, expired risk acceptance and changed approval dependencies.
Fresh sessions must recover valid consent without asking again. Test host stale-review and
independence enforcement with authorized fixtures; never forge a real human review.

AP-1 to AP-3 gate rung 3, AP-4 rung 5; RV-1 gates rung 4 and owner-source evidence strengthens
DC-4 at rung 7. Missing provenance stays a gap/assumption, not a proven approval. An empty
merge history distinguishes configured enforcement from exercised human review. Gardening
reports missing evidence, stale stages and unresolved conditions, preserving history.

## References and trial status

- [Protected reviews and freshness](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)
- [Authenticated statements and artifact identity](https://slsa.dev/spec/v1.2/attestation-model)

The supplied tests exercise mechanical fixtures, not actual human provenance. Full project,
host-review and cross-session adoption under these gates remain to be trialled.
