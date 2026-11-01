---
name: operate
description: Design or review how a system's actions are used by agents and automation (APIs, MCP tools, scripts, AI assistants) against Agent804's Operate levels - one contract for people and agents, safe by default (read-only until granted, attributed, repeats harmless), and bounded (untrusted text, outside load, a person publishes). Use when adding an API or agent tool, connecting an AI assistant to the system, or when the user asks whether their system is safe for agents to use.
---

# Operate: agents using the system

Most guidance covers agents **building** software. This covers agents **using** it: an
assistant calling your API or MCP tools, a script acting for a user. A mistake here is not a
red test; it is a wrong write in production, made at machine speed. The levels are in
`framework/rungs.md` ("Operate") and the rules are OP-1 to OP-8 in `framework/rules.md`.

**Framework files**: in Claude Code, `${CLAUDE_PLUGIN_ROOT}/framework/`; for other agents,
`../../framework/` from this file.
Read the project's `docs/security.md` and security guidance: Claude Code
`${CLAUDE_PLUGIN_ROOT}/framework/security.md`, otherwise `../../framework/security.md` from
this file. Operate levels complement SE-1 to SE-6; they do not certify production readiness.
For interface changes, follow the project's maintainability/style policies and approved
criteria. Read approval guidance: Claude Code `${CLAUDE_PLUGIN_ROOT}/framework/approvals.md`,
otherwise `../../framework/approvals.md` from here. Design approval does not grant live write
or publish authority. Use testing guidance: Claude Code
`${CLAUDE_PLUGIN_ROOT}/framework/testing.md`, otherwise `../../framework/testing.md` from here;
preserve meaningful red/green evidence, independent assertions and actual integration scope.

## O1: One contract

1. **Each action is declared once** (OP-1): name, required access, read or write, input and
   output schemas, a summary. The UI, the API and agent tools are generated from or call that
   one declaration. Business rules live behind it, never in the adapters, so the three cannot
   disagree about what is allowed.
2. **Credentials in headers** (OP-5), hashed at rest, shown once, with an expiry. Never in URLs,
   which end up in logs and browser history.

Build this from the first action. One contract retrofitted over many hand-built endpoints is the
expensive path.

## O2: Safe by default

3. **Same access, narrowed, read-only until granted** (OP-2). A call may do what its owner may
   do, narrowed by the credential: which actions, which sites or tenants, and whether it may
   write. Write is off by default and granted per credential by a person.
4. **Attribution** (OP-3). Every write records the actor, the credential if any, and the channel
   (web, API, agent), so history shows what an agent did on whose behalf.
5. **Repeats are harmless** (OP-4). Require a request ID for each logical machine write;
   retries reuse it. Scope IDs by tenant or owner and operation, bind them to validated input,
   and reject reuse with different input. Authorize every attempt, including result replay.
   Coordinate concurrent duplicates so only one executes. For database writes, commit the
   change and deduplication outcome atomically; a retry returns the saved outcome.
   State the retention window and behavior after expiry; never promise unlimited deduplication
   from a record that expires. An in-progress request must not execute again.
   External effects need downstream deduplication or durable coordination and reconciliation.
   A timeout may hide success: retry automatically only when no effect is known to have
   occurred or the downstream system guarantees deduplication. Unknown outcomes await
   reconciliation; a local request record alone cannot guarantee one print or outside write.

## O3: Bounded

6. **Untrusted text** (OP-6). Anything that came from data (comments, notes, tickets, outside
   systems) may carry instructions aimed at the agent reading it. Tools that act on such data
   get constrained credentials, destinations and write/publish authority. Record the threat
   and test planted instructions against actual tool permissions and attempted operations;
   an ADR or the agent's claimed refusal alone does not prove isolation.
7. **Definitions, not code** (OP-7). Where people or agents build things (forms, screens,
   reports, labels), they produce definitions the system interprets, never code it runs. Agents
   may draft; a person publishes.
8. **Outside load is budgeted** (OP-8). Calls the system makes to systems it does not own carry
   a budget per source, and shared reads are cached once for everyone, so an agent looping on a
   tool cannot become load on someone else's server.

## Design (new system or new interface)

Work through O1, then O2, then O3. Record the design as an ADR (`decide`), and add the
checks that enforce it (`sensor`): every action declares access; a read-only credential is
refused on every write action; sequential and concurrent duplicates produce one effect;
changed payloads are refused; tenant scopes are separate; replay rechecks access; crash and
timeout tests cover outcome recovery and reconciliation; expired IDs follow the documented
policy; an outside source over budget is refused before the call is sent.
Map applicable security requirements into tests for alternate adapters, object/tenant access,
unsafe input/output and planted instructions. Use isolated resources; no production access or
live exploitation is authorized by a design or review request.

## Review (existing system)

For each interface agents can reach, grade OP-1 to OP-8 as met, partly met or not met with
evidence, then mark each level as `assess` does: `Operate O1✓ O2✓* O3◐`. The most common
findings, in order: a shared or broad token that bypasses per-user access; writes allowed by
default; no record of which channel acted; tokens accepted in URLs; no request IDs, so retries
duplicate records; no limit on what an agent can make the system ask of outside systems.
