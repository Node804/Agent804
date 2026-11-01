# Profile: WPF

- **Status:** Draft extension; no Windows designer/UI application trial.
- **Applies to:** Supported pinned Windows/.NET WPF projects and their authored XAML/C#.
- **Extends:** [C# / .NET](dotnet.md) and the [shared baseline](README.md#shared-baseline).

## Baseline and explicit additions

Keep the parent's C# compiler, dependency, test and architecture mechanisms. Add a pinned
XAML Styler local tool for authored XAML and a Windows UI acceptance harness, for example
reviewed FlaUI with stable automation IDs. Prefer a view-model/application-service boundary;
do not let code-behind become the only home for business rules or access policy.

## Check, bootstrap and skeleton

Extend the parent's one check with XAML passive formatting, authored-XAML structural checks,
Windows build, view-model/service tests and at least one real UI acceptance scenario.
Generate separate fast/headless and UI tasks but keep the full check responsible for all
required stages. UI tests require an appropriate isolated interactive Windows session;
unavailable UI execution is a gap, not a skipped-success result.
Bootstrap verifies SDK/Windows targets and reviewed local tools, then isolated test/dev
resources. Doctor reports missing desktop/session/workload inputs. The skeleton opens one
window, invokes an application action and verifies authorized and refused outcomes; choose
the local or backend principal explicitly. Review a designer/build/resource round-trip.

## Rule mapping additions/overrides

| Rules | WPF mechanism to generate |
|---|---|
| ST-1 to ST-3 | Parent C# policy plus [XAML settings](../../templates/style/wpf/Settings.XamlStyler), pinned passive/check and write pipeline; select authored roots rather than `obj` |
| SK-1, SK-2 | Actual Windows launch/UI action test and bootstrap/doctor; the parent's CLI/HTTP scenario alone does not satisfy UI acceptance |
| MT-1, MT-2 | Public view-model/command contracts and complexity review; check bindings/resources and service responsibilities |
| AR-1, AR-2 | Commands/actions declare access; authoritative services enforce it even when commands are invoked without UI. Disabled buttons alone are not authorization |
| AR-3 | UI/view models depend on declared application/domain interfaces; enforce project/namespace boundaries and exercise violations |
| AR-4 to AR-6 | Parent services/history/integration boundaries; validate file/dialog/clipboard and backend data, cancellation and output handling |
| WK-6 | Separate UI sessions or serialized UI workers, local state/config, temp paths and backend namespaces; no shared real user profile/data |
| SE-4, SE-5 | Verify effective local/backend identity and resource rights, configuration/update trust, sensitive logging and direct command/service refusal tests |
| OP-1 to OP-8 | If exposed to agents, tool adapters call the same application operations; UI automation is not a privileged authorization bypass |

## Testing evidence (draft)

Apply [testing guidance](../testing.md) (TS-7 to TS-12); exercise this mapping before claiming it met.
Inherit .NET runner/discovery evidence. Identify Windows, dispatcher/apartment and desktop
session prerequisites; isolate UI processes/resources and close them on failure. Exercise
representative actual UI journeys; headless tests do not establish UI execution. Report gaps.

## Gaps and gotchas

Select and pin the UI harness, runner/session setup, auth/backend model and packaging/update
verification. Test actual bindings, resources, focus, dialogs and dispatcher/thread behavior;
unit tests and XAML compilation alone cannot prove these. Reflection/resource references may
look unused to static tools. Generated `obj` code is not hand-edited; authored code-behind
remains covered. Client-side code cannot protect a backend that trusts the client blindly.
All .NET/shared obligations not explicitly overridden remain; full profile adoption is untrialled.

## Sources

- [WPF overview](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/overview/)
- [FlaUI](https://github.com/FlaUI/FlaUI)
- [XAML Styler CLI](https://github.com/Xavalon/XamlStyler/wiki/Script-Integration)
