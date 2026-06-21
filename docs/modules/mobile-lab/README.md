# Atlas Mobile Lab

> Product and architecture guide for Atlas Pocket and future field-support clients.

**English** | [Português](README.pt-BR.md)

[Modules catalog](../README.md) · [Mobile track](../../tracks/mobile/README.md) · [Project README](../../../README.md)

## Current status

The Mobile Lab is **specified but not implemented**. The repository contains a
detailed stack study in [`stack.md`](stack.md), while no Android application
directory or build configuration exists yet. The first implementation should
therefore remain deliberately small.

## Product direction

The primary planned application is **Atlas Pocket**, an Android client that
connects to Atlas services and remains useful under intermittent connectivity.
Its first responsibility is to show backend health and version information.
Later releases may add dataset summaries, reports, alerts, support workflows,
document capture, QR codes, and AI-assisted features.

## First vertical slice

The first release should:

1. create a Kotlin Android project;
2. render one Jetpack Compose status screen;
3. call `GET /health` and `GET /version` through Retrofit/OkHttp;
4. represent loading, online, offline, timeout, and malformed-response states;
5. expose the API base URL through development configuration;
6. include unit tests and at least one integration or UI smoke test;
7. document emulator and physical-device setup.

It should not add authentication, Room, background synchronization, push
notifications, camera workflows, or embedded ML until this slice is reliable.

## Planned architecture

```text
Compose UI
    ↓
ViewModel
    ↓
Use cases
    ↓
Repository
    ├── Remote data source → Atlas API
    └── Local data source  → Room / DataStore
```

The application must communicate with Atlas through API contracts. It must not
connect directly to the remote PostgreSQL database.

## Capability roadmap

### Phase 1 — API connection

- health and version screen;
- network-state handling;
- basic automated tests.

### Phase 2 — Offline-first foundation

- Room cache and DataStore preferences;
- explicit synchronization state;
- WorkManager jobs with safe retry behavior.

### Phase 3 — Data and reports

- dataset and indicator summaries;
- cached reports;
- accessible charts suitable for small screens.

### Phase 4 — Field support

- service checklist;
- equipment registration and photographs;
- QR identification;
- offline incident records and later synchronization.

### Phase 5 — AI capabilities

- remote agent chat with transparent connectivity state;
- document summaries and cited answers;
- approved OCR or lightweight on-device models.

## Quality requirements

- Offline behavior is designed, not treated as an exception.
- Sync conflicts and retries have explicit states.
- Sensitive data is minimized and protected at rest and in transit.
- Accessibility covers labels, contrast, scalable text, and touch targets.
- Network calls have timeouts and observable errors.
- Mobile tests cover domain logic, repositories, and critical UI flows.
- Battery, storage, bandwidth, and model size are measured before mobile AI ships.

## Python support tooling

Python remains useful for Appium tests, ADB automation, screenshot collection,
QR generation, API contract checks, and HTML test reports. These tools support
the Android client; they do not replace the Kotlin application architecture.

Relevant dependency files:

- [`mobile.txt`](../../../requirements/mobile.txt)
- [`mobile_ai.txt`](../../../requirements/mobile_ai.txt)
- [`mobile_testing.txt`](../../../requirements/mobile_testing.txt)

## Definition of done for the first release

- A clean checkout can build and launch the app from documented steps.
- The screen correctly represents successful and failed API calls.
- Tests run locally and in the selected CI environment.
- No production secret or hard-coded private endpoint is committed.
- The README reflects the implemented screens and architecture.
