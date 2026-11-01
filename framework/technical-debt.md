# Accountable technical debt

Manage known compromises and maintenance friction through evidence and explicit dispositions.
Debt may be deliberate, inherited or discovered as understanding improves. The aim is to
control its consequences, not eliminate every imperfection or maximize a debt score. Some
rarely touched debt may reasonably remain. MT-5 is a reported practice pending trials, not
a new rung gate; existing maintainability, security, testing and review gates still apply.

## One authoritative record

Use the project's issue tracker or a small `docs/debt.md` based on the
[template](../templates/debt.md). Existing plan/PR notes can hold a small scoped item when
they remain discoverable. Choose one authoritative location and link to specialist records;
don't maintain conflicting tracker and Markdown backlogs. No records need be invented for a
clean new project. Scanner reports and agent suggestions are candidates until confirmed.

Each confirmed actionable item has a stable ID, scope/location, evidence/revision, concrete
consequence, owner, disposition and review condition. Include deferral reason/authority where
applicable, proposed repayment and verifiable completion criteria. Unknown facts stay unknown
with a triage gap; an agent must not invent an owner, approval or precise cost estimate.
Several items may share a scoped decision when its subjects and consequences were reviewed.

Keep security reports/incident details in appropriate restricted records. Link from the
general inventory using non-sensitive references; don't copy credentials, private evidence
or exploit details merely to make the inventory comprehensive.

## Classify before accepting

| Observation | Treatment |
|---|---|
| Known compromise with future change/operating cost | Confirm debt, impact and disposition |
| Scanner warning or speculative redesign | Candidate; verify impact before accepting work |
| Confirmed broken promised behavior | Defect under existing acceptance requirements; may link related debt |
| Authorization bypass or other security finding | Security record and SE-6 response; debt label grants no acceptance |
| Feature never agreed or built | Product backlog, not a completed feature with a debt waiver |
| Flaky/quarantined test | Testing requirements and visible protection gap; link debt without erasing failures |
| Retained compatibility path | Record actual consumers, reason and review condition (MT-3) |

A debt record describes a problem; an exception permits a specified departure under the
relevant policy. They are different. Recording debt cannot grant an exception, accept risk,
change criteria or make a failing check green. Keep exception IDs and their scope/expiry
linked to the debt item; SE-6, TS-4/TS-10 and MT-2 requirements are not replaced.

## Lifecycle and deferral

Use these meanings or equivalent tracker states:

1. **Candidate:** unconfirmed finding; collect evidence or reject with a reason.
2. **Open:** confirmed consequence, owner and completion criteria; prioritize and choose a
   disposition. An untriaged/open item is not permission to introduce its violation.
3. **Deferred:** the responsible human's applicable decision covers scope, tradeoff, reason,
   and review date/event. Identify separate exceptions needed; reuse valid scoped decisions.
4. **In progress:** authorized scoped repayment with plan/tests proportional to risk.
5. **Resolved:** completion criteria verified against actual revision/results, required review
   present and linked exceptions/retained paths reconciled. Preserve the record/history.
6. **Rejected:** not substantiated, duplicate or no longer applicable, with reason/evidence and
   canonical link if duplicated. Not a way to hide confirmed unresolved risk.

Newly introduced compromises need review of benefit and future consequence before relying
on deferral; don't add a ticket after the fact and declare acceptance satisfied. Existing
baselines may cover known findings within scope; don't silently expand them or worsen debt.
Creating a candidate needs no claim of human agreement. Agents may propose dispositions and
record real decisions but cannot manufacture acceptance or silently renew an expired waiver.

When the review date/event occurs, revisit impact and select repayment, continued deferral
under applicable authority, or justified rejection. Retain prior decisions. A review date
is not automatically a repayment deadline; explicit deadlines and security exceptions keep
their separate meaning. Overdue review prompts triage/escalation, not automatic renewal.
Urgent defects and security exposure follow their own response clocks immediately.

## Prioritize by consequences and exposure

Record observed friction separately from estimates: repeated workarounds, failures, blocked
tests, slow changes, unsupported technology, dependency spread or operational burden. Ask
whether planned work will touch the area, whether support/exception conditions are changing,
what repayment costs/risks are, and what happens if it remains. Cite examples rather than
claiming every large file or stylistic preference creates debt.

No universal debt score or fixed sprint percentage is required. Projects may choose capacity
policies and bounded repayment work. Estimates of hypothetical clean-code effort are uncertain;
do not present them as measured interest. Keep aged low-impact items distinct from items whose
consequences are growing. A low count or closed-ticket total alone proves no improvement.

## Work in the affected area

Before a feature/refactor, inspect relevant debt and choose a disposition in the plan/PR:
repay within authorized scope, schedule separate work, or retain with a reason and review
condition. Don't expand a feature into unrelated cleanup. Link authoritative records rather
than copying their status into multiple documents. Long-lived decisions may need ADRs;
ordinary debt items do not each need an ADR or a full feature spec.

Use [refactoring guidance](maintainability.md) for structural repayment and [testing](testing.md)
for behavior changes and bug fixes. Preserve required consumer compatibility, validate
uncertain usage before removal, and separate structural from behavior changes. Agents don't
get commit/push/deploy permission from a repayment plan. Follow the project's style/security
rules and original human approval/freshness requirements.

## Verify closure and keep identity

Resolve an item when its stated outcome is demonstrated: for example a consumer migrated,
obsolete path removed, boundary enforced or flaky test repaired with appropriate repeat-run
evidence. Include actual revision/patch, commands/environment, scope/results and limitations;
not every debt type has an executable test, but it still needs reviewable completion evidence.
Changed code or a passing subset alone does not establish the specific completion criterion.

Reconcile dependent debt, exceptions, documentation and retained compatibility paths. Renames,
moves, ticket splitting or replacing a workaround preserve the original identity/history
through links; they don't erase the underlying consequence. If criteria are only partly met,
leave the remainder explicitly open or split with traceable remaining scope. Reopen a
recurring item or link a new item with evidence; never silently rewrite prior resolution.

## Integrate without another skill

- `assess`: inspect real evidence, ownership and dispositions; report MT-5 as a practice.
- `spec`: identify relevant debt before planning; separate agreed behavior from debt deferral.
- `garden`: triage candidates, due review events, changed exposure and stale closure evidence;
  propose reviewed work rather than automatically rewriting code or accepting risk.
- `refactor`: perform authorized repayment and show preserved behavior/actual improvement.
- `review`: reject hidden new debt, invalid exceptions and unsupported closure claims.
- `measure`: track consequence/aging/ownership/review follow-up with comparable scope and
  uncertainty, not a raw ticket-count target. MS-1/MS-2 already cover this cadence.

The [research and limits](validation/debt.md) explain the basis. No tracker integration,
automatic exception approval or debt-lifecycle application trial is shipped by these docs.
