# Atlas mobile application

> Implementation location for Atlas Pocket and future Android field tools.

**English** | [Português](README.pt-BR.md)

[Project](../../README.md) · [Modules](../../docs/modules/README.md)

## Current status

**Empty scaffold.** The directory exists but contains no implementation beyond this documentation.

## Purpose

This directory is reserved for the Android application described by the Mobile Lab. It is currently empty; architecture and stack choices are documented, but no Gradle project exists yet.

## Inside the boundary

- Kotlin and Jetpack Compose source
- Gradle build and Android configuration
- Remote and local data sources
- Offline synchronization and device features
- Android unit, integration, and UI tests

## Outside the boundary

- Python mobile prototype as the primary production client
- Direct PostgreSQL connectivity
- Hard-coded private endpoints or tokens
- Room, AI, or camera complexity before the health slice

## Proposed structure

```text
app/src/main/
app/src/test/
app/src/androidTest/
gradle/
docs/
```

The structure is directional. Create subdirectories only when a real deliverable needs them.

## Workflow

1. Define one problem and a small acceptance criterion.
2. Choose inputs, outputs, and contract before tools.
3. Implement an executable slice with a test.
4. Record configuration, risks, and limitations.
5. Connect the module through an explicit contract and update status.

## Related dependencies

- [`mobile.txt`](../../requirements/mobile.txt)
- [`mobile_ai.txt`](../../requirements/mobile_ai.txt)
- [`mobile_testing.txt`](../../requirements/mobile_testing.txt)

## Related tracks

- [mobile](../../docs/tracks/mobile/README.md)
- [api](../../docs/tracks/api/README.md)
- [observability](../../docs/tracks/observability/README.md)

## Quality, security, and operations

- Add risk-proportional tests before integration.
- Keep configuration outside source and never commit secrets.
- Document expected failures, retries, rollback, and ownership where applicable.
- Use minimal, public, or anonymized data in examples.
- Measure cost and resources before expanding the solution.

## Next steps

1. Create the Gradle project with an explicit supported SDK
2. Implement health and version API models
3. Render loading, success, offline, and error states
4. Add unit and UI smoke tests

## First-deliverable definition of done

- A small executable use case exists.
- Setup and verification work from a clean checkout.
- Contracts, errors, and limitations are documented.
- Tests and evidence demonstrate behavior.
- This README has been updated to reflect real code.
