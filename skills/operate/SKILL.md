---
name: operate
description: Design or review MCP servers, agent APIs, and embedded model features (chat, assistants, classifiers, generators) against Agent804 Operate levels. One contract, a designed tool list, read-only until a person grants write, attributed idempotent writes, tokens issued for this server, untrusted content, and model output that cannot approve or publish. Use when adding or changing an MCP server, agent tool, or in-product AI feature, or when asked whether that surface is safe.
---

# Operate: build the AI-facing surface

This is development work: an MCP server, an API or tools agents call, or a model feature
inside the product. Build it with the same criteria, tests, and human review as any other
feature. A mistake here is a wrong write at machine speed. Levels are in
`framework/modules.md` ("Operate"); rules are OP-1 to OP-11.

**Framework files**: in Claude Code, `${CLAUDE_PLUGIN_ROOT}/framework/`; for other agents,
`../../framework/` from this file.
Read the project's `docs/security.md` if it exists. These levels are not a security
certificate. Agreement on a design grants no live write or publish. Tests assert outcomes
across the real interface. If the project has none of these surfaces, stop and say so.

## O1: One contract

1. **Each action is declared once** (OP-1): name, access, read or write, input and output,
   summary. The UI, the API, and agent tools come from that declaration. Business rules stay
   behind it.
2. **The model-facing list is designed** (OP-9). For each exposed action record a stable
   name, when to use it and when not to, an input schema, a maximum result size, and an
   effect (read, write, or destructive). Expose the actions a task needs. A wrapper per
   internal function is a failed design. A declared read must not write, send, delete, or
   spend. Bound results and strip secrets. Enforce the effect on the server. A person can
   refuse a write or destructive call before it takes effect. Do not require a prompt on
   every read.
3. **Credentials in headers** (OP-5), hashed at rest, shown once, with an expiry. Never in
   URLs.

Build this from the first action.

## O2: Safe by default

4. **Same access, narrowed, read-only until granted** (OP-2). Write is off until a person
   grants it for that credential.
5. **Attribution** (OP-3). Every write records actor, credential, and channel.
6. **Repeats are harmless** (OP-4). Request IDs are scoped by owner or tenant and operation,
   bound to validated input; reject reuse with different input. Authorize every attempt,
   including replay of a saved result. Coordinate concurrent duplicates. Commit database
   effects and their deduplication outcome atomically; recover interrupted requests without
   repeating effects. State retention and behavior after expiry. For external effects use
   downstream deduplication or durable coordination and reconciliation. A timeout with an
   unknown outcome is not a blind retry.
7. **Credentials match this server** (OP-11). Accept only tokens issued for this endpoint.
   Do not forward a token issued for somewhere else. Do not treat a session id as
   authentication. A local process gets no production credential and no privilege beyond
   its actions. A server calling a third-party API uses a credential issued for that API.
   If it acts as an OAuth proxy, obtain the person's consent for that specific client before
   forwarding to third-party authorization. Do not reuse another client's consent.

## O3: Bounded

8. **Untrusted text** (OP-6). Data may contain instructions. Constrain the tool's
   credential, destination, and write authority. Test planted instructions against real
   permissions.
9. **Embedded model features** (OP-10). If the product calls a model, put the instructions,
   allowed actions, accepted inputs, and output effects in the repository. Specify and test
   them like any behavior, with a person's review. Model output cannot grant access,
   publish, approve, or bypass a check. Plant instructions in user and retrieved content and
   show no forbidden effect. No such feature: say OP-10 is not applicable.
10. **Definitions, not code** (OP-7). Forms, screens, and labels are data the system
    interprets. Agents may draft; a person publishes.
11. **Outside load is budgeted** (OP-8). A budget per outside source, and shared reads
    cached once.

## Design

Work O1, then O2, then O3. Record an ADR (`decide`). Add checks (`sensor`): an undeclared
action fails; a read-only credential is refused on every write; a declared read performs
no write; a foreign token is refused; sequential and concurrent duplicates produce one
effect; changed input and cross-tenant ID reuse cannot replay another request; replay
rechecks access, including after revocation; crashes and timeouts recover without duplicate
effects; expired IDs follow the documented expiry policy. For an OAuth proxy, prove
one client's consent cannot authorize another. Planted instructions do nothing forbidden;
an over-budget outside call is refused before it is sent. No production access.

## Review

Grade OP-1 to OP-11 with evidence. Mark levels as `assess` does: `Operate O1✓ O2✓* O3◐`.
Common findings: one tool per function; a shared write token; no channel on writes; tokens
in URLs; retries that duplicate; a passed-through foreign token; a prompt that can publish
without a person; no limit on outside calls.
