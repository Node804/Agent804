---
name: sensor
description: Turn a mistake an agent keeps making, or a review comment that keeps recurring, into an automated check (lint rule, structural or architecture test, type, framework check or hook) whose failure message tells the agent how to fix it. Use when the user says the agent did something wrong again, or when a rule exists only as prose.
---

# Add a sensor

A rule that exists only as prose is a check not yet written (CK-5). This skill writes it, so the
next session cannot repeat the mistake, and so nobody has to fix the same diff by hand again
(RV-4).

**Framework files**: in Claude Code, `${CLAUDE_PLUGIN_ROOT}/framework/`; for other agents,
`../../framework/` from this file. The stack's mechanisms are in `profiles/<stack>.md`.

## 1. State the invariant

Write one sentence that is true of every correct change and false of the bad one. Name the
property, not the implementation: "every view declares an access rule", not "every view
inherits LoginRequiredMixin". If you cannot write it, the problem is judgement, not a rule:
add a line to `AGENTS.md` instead and stop.

## 2. Pick the cheapest mechanism that catches it

In this order, from the stack profile:

1. **An existing tool's rule**: a linter rule that is off, a stricter type setting.
2. **A configuration contract**: architecture or import rules.
3. **A structural test**: a test that walks the code or the running app (all routes, all
   models) and asserts the invariant.
4. **A framework check**: the framework's own startup or system checks, where it has them.
5. **A custom lint rule**: only when nothing above can see it.
6. **A hook**: for things about the agent's actions rather than the code (files it may not
   touch, commands it must run).

Deterministic checks beat AI review (CK-3). Do not add a hook for a preference (CK-7).

## 3. Write the failure message for the agent

It says what is wrong, where, and how to fix it, in one or two sentences, with the rule's name
and where to read more. Example: "View `OrderList` declares no access rule. Add a module access
mixin or mark it public with the login-not-required decorator. See AGENTS.md, Access."

## 4. Prove it catches the mistake

1. Run the check on the current code. If it fails on existing code, list the failures for the
   user; fix them or record them as known exceptions with a reason, never by weakening the
   check.
2. Reintroduce the original mistake (or write a small fixture with it) and confirm the check
   fails with your message. Remove it.
3. Make sure the check runs inside the project's one check command and CI.

## 5. Clean up the prose

If `AGENTS.md` stated this rule, shorten it to a pointer ("the check enforces X") or remove it.
Add a changelog entry. Report: the invariant, the mechanism, proof it fails on the mistake, and
any existing violations found.
