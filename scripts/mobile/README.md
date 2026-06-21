# Atlas mobile automation scripts

> Python and ADB helpers for building, testing, inspecting, and demonstrating mobile clients.

**English** | [Português](README.pt-BR.md)

[Project](../../README.md) · [Modules](../../docs/modules/README.md)

## Current status

**Empty scaffold.** The directory exists but contains no implementation beyond this documentation.

## Purpose

This module supports the Android application with repeatable automation. It may orchestrate emulators, ADB, Appium, screenshots, logs, QR fixtures, and API checks, while remaining separate from application behavior implemented in Kotlin.

## Inside the boundary

- ADB device and emulator inspection
- APK installation and smoke-test entry points
- Appium and UI automation
- Screenshot and log collection
- QR and test-fixture generation
- Mobile API contract checks

## Outside the boundary

- Primary Android application logic
- Bypassing device authorization or locks
- Hard-coded device serials and private endpoints
- Destructive device commands without confirmation
- Unredacted personal data in artifacts

## Proposed structure

```text
adb/
appium/
fixtures/
reports/
tests/
```

The structure is directional. Create subdirectories only when a real deliverable needs them.

## Workflow

1. Define one problem and a small acceptance criterion.
2. Choose inputs, outputs, and contract before tools.
3. Implement an executable slice with a test.
4. Record configuration, risks, and limitations.
5. Connect the module through an explicit contract and update status.

## Related dependencies

- [`mobile_testing.txt`](../../requirements/mobile_testing.txt)
- [`mobile.txt`](../../requirements/mobile.txt)
- [`scripting.txt`](../../requirements/scripting.txt)

## Related tracks

- [mobile](../../docs/tracks/mobile/README.md)
- [automation](../../docs/tracks/automation/README.md)
- [support](../../docs/tracks/support/README.md)

## Quality, security, and operations

- Add risk-proportional tests before integration.
- Keep configuration outside source and never commit secrets.
- Document expected failures, retries, rollback, and ownership where applicable.
- Use minimal, public, or anonymized data in examples.
- Measure cost and resources before expanding the solution.

## Next steps

1. Add a device-discovery command with no mutation
2. Define emulator and physical-device prerequisites
3. Create a health-screen smoke test after the app exists
4. Store artifacts under ignored, timestamped output directories

## First-deliverable definition of done

- A small executable use case exists.
- Setup and verification work from a clean checkout.
- Contracts, errors, and limitations are documented.
- Tests and evidence demonstrate behavior.
- This README has been updated to reflect real code.
