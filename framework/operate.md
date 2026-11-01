# Operate

Building an MCP server, an API or tool surface for agents, or an embedded model feature is
development work. It takes the same criteria, tests, review, and checks as any other feature.
Operate is scored when the project builds that surface, and it costs nothing when the project
has none. The levels and triggers are in [modules.md](modules.md); the properties are OP-1 to
OP-11 in [rules.md](rules.md).

A mistake here is a wrong write or a leaked secret at machine speed. A library that speaks
the protocol is not a design.

## The gap

MCP tools are model-controlled: the model discovers the list and invokes a tool, and the
result goes back into the model. That fails in a repeated way when the server exposes one
tool per internal function, describes it vaguely, and returns an unbounded payload. The model
picks badly, the context fills with copies of the system, and a tool marked "read" still
writes. Embedded assistants fail differently: the prompt and the allowlist live outside the
spec, model output is treated as permission, and the feature never gets the refusal tests
the rest of the product uses.

## Designed surface (OP-9)

Each model-facing action has a stable name, a description of when to use it and when not to,
a validated input schema, a bounded result that omits secrets, and a declared effect: read,
write, or destructive. The list is the set a task needs. The server enforces the effect. A
hint on the tool is not the control, and a declared read does not write, send, delete, or spend.

A person can refuse a write or a destructive call before it takes effect. The MCP tools
specification asks for a human who can deny invocations. Agent804 requires that refusal for
writes and destructive effects. A confirmation on every read is the project's choice when the
data is sensitive; it is not a universal gate.

Build the list from the first action. Wrapping an existing API one function at a time is the
expensive path.

## Safe retries (OP-4)

A request ID alone cannot make a retry safe. Access may have been revoked since the original
call, so even a saved result needs authorization. Reusing an ID with changed input must not
silently return an unrelated outcome. Atomic persistence of database effects and the saved
outcome closes the crash window between a successful write and its deduplication record.
Outside effects need their own deduplication or reconciliation, and an expired record cannot
promise indefinite protection. Concurrency, crash, timeout, and expiry tests expose these gaps.

## Credentials (OP-11)

Accept only a credential that was issued for this endpoint. Do not forward a token that was
issued for somewhere else: the MCP security guidance forbids that passthrough, because it
skips the server's own limits and audit. A session identifier is not authentication.

A server that calls another system's API uses its own credential. Where that call is an OAuth
proxy, record the person's consent for the specific client before sending them on. Do not
reuse another client's consent.

A local process runs with the privileges of the user who started it. It does not receive
production credentials (GR-1) and does not hold more privilege than its actions need. A
one-click install shows the exact command and waits for the person.

## Embedded model features (OP-10)

A chat, assistant, classifier, or generator inside the product is a feature. Its instructions,
allowed actions, accepted inputs, and output effects live in the repository. Model output is
data. It cannot grant access, publish, approve, or bypass a check. Tests plant instructions
in user content and in retrieved content, and show no forbidden effect.

The MCP specification does not cover this in-product case. OP-10 exists so an embedded model
is not a side door around the tool rules. No such feature means OP-10 is not applicable; it
is not a pass earned by silence when the feature exists.

## Same loop as any other feature

Agree the criteria first, including the effect, what a refused caller sees, and what the
action must not return or change. A separate context writes the tests and shows them failing
for that reason. The check goes green without weakening those tests. A person reviews the
change and can explain it. Guidance: [testing.md](testing.md) and [security.md](security.md).

Map the abuse cases that apply: another tenant, a direct call that skips the UI, a read that
writes, a foreign token, a planted instruction, an over-budget call to a system the project
does not own. Security-module projects still select versioned requirements (SE-1) and keep
findings owned (SE-6). Operate does not replace that, and neither score is a certificate or
permission to deploy.

## What stays a mechanism

Which SDK, transport, or schema dialect is the stack profile's choice. HTTP authorization,
when the project uses it, follows the MCP authorization specification for that transport.
Stdio takes credentials from the environment; those credentials are still development
credentials. Agent804 does not implement an OAuth product and does not require dynamic client
registration.

## Evidence

OP-1 to OP-8 describe one reference project's built design. The `operate` skill has not been
run. OP-9 to OP-11 are untrialled. Sources and the choices above are in
[validation/operate.md](validation/operate.md).
