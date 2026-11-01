# Profile: WinForms

- **Status:** Draft extension; no Windows designer/UI application trial.
- **Applies to:** Supported pinned Windows/.NET WinForms projects, authored C# and resources.
- **Extends:** [C# / .NET](dotnet.md) and the [shared baseline](README.md#shared-baseline).

## Baseline and explicit additions

Keep the parent's C# compiler, dependencies, service tests and architecture mechanisms. Add
a reviewed Windows UI automation harness, for example pinned FlaUI, with stable automation
IDs and an isolated interactive runner. Separate forms/presentation from application services;
event handlers delegate behavior instead of replicating rules in each form.

## Check, bootstrap and skeleton

Extend the parent check with the declared resource/XML policy, Windows build, presentation/
service tests and one real form/action acceptance scenario. Split fast/headless and UI tasks
for feedback but require both where applicable. Bootstrap/doctor verify SDK/Windows targets,
desktop session inputs, isolated app state/backend resources and reviewed tools.
Create one runnable form, one authoritative action and authorized/refused tests. Verify a
Visual Studio designer save/build round-trip; a source formatter alone cannot establish it.
Do not run tests against the developer's live settings, registry entries or production backend.

## Rule mapping additions/overrides

| Rules | WinForms mechanism to generate |
|---|---|
| ST-1 to ST-3 | Parent C# policy and [resource guidance](../../templates/style/winforms/.editorconfig); identify actual designer-owned files, keep authored partials/events covered and choose an authored XML check |
| SK-1, SK-2 | Real Windows launch/form interaction acceptance and bootstrap/doctor; pure service tests do not establish UI behavior |
| MT-1 to MT-3 | Public presenter/service contracts, event-handler complexity limits and investigated obsolete handlers/resources; designer references are real consumers |
| AR-1, AR-2 | Form actions declare access and call shared authorized application services; invoking a handler/service directly must preserve refusal behavior |
| AR-3 | Project/namespace contracts isolate presentation from domain/integration internals; no cross-form duplication of business rules |
| AR-4 to AR-6 | Actor/history services, one integration boundary and validated file/clipboard/dialog/backend input and output |
| WK-6 | Isolated or serialized Windows UI sessions, per-checkout config/state/registry or storage scopes and backend resources |
| SE-4, SE-5 | Test local/backend principal, storage/credential/update boundaries and refused direct service calls without prohibited effects; disabled UI alone is insufficient |
| OP-1 to OP-8 | Agent/API adapters use the same operations and scoped authority; automation must not gain a privileged backend credential |

## Testing evidence (draft)

Apply [testing guidance](../testing.md) (TS-7 to TS-12); exercise this mapping before claiming it met.
Inherit .NET runner/discovery evidence. Identify Windows, message-loop/apartment and
interactive desktop prerequisites; isolate UI processes/resources and clean up failed runs.
Exercise actual form journeys; report unavailable UI/designer coverage rather than passing it.

## Gaps and gotchas

Select actual generated-file ownership, XML checker, UI tool/session, local resource isolation
and packaging/update verification. Do not blanket-exclude `.Designer.cs`, all partials or a
forms folder without checking provenance. Do not hand-reformat designer-owned outputs.
Check event wiring, resources/localization, dialogs and UI-thread behavior on Windows.
Cross-compilation and ordinary unit tests do not prove designer compatibility. A Windows
runner existing is not evidence it has the interactive desktop required by the selected UI
tests. All remaining .NET/shared obligations apply and still require adoption evidence.

## Sources

- [WinForms overview](https://learn.microsoft.com/en-us/dotnet/desktop/winforms/overview/)
- [FlaUI](https://github.com/FlaUI/FlaUI)
- [Style starter guidance](../../templates/style/README.md)
