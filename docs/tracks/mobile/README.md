# Atlas Mobile Lab

> Offline-first mobile clients, field support tools, and on-device intelligence.

**English** | [Português](README.pt-BR.md)

[Tracks index](../README.md) · [Documentation](../../README.md) · [Project](../../../README.md)

## Mission

The Mobile Lab brings Atlas capabilities to constrained and intermittently connected devices. The initial product, Atlas Pocket, should consume the existing API before adding local persistence, synchronization, camera workflows, notifications, and mobile inference.

## Expected outcomes

- Turn study into executable, tested, and demonstrable software.
- Record assumptions, decisions, limitations, and evidence reproducibly.
- Deliver integrable components without unnecessary coupling.
- Produce portfolio material that explains the result and the reasoning.

## Technical scope

- Kotlin and Jetpack Compose clients
- REST integration with Retrofit and OkHttp
- Room and DataStore persistence
- Offline-first synchronization
- Background work and notifications
- Camera, QR code, and OCR flows
- On-device and remote AI inference
- Automated Android testing

## Reference deliverables

- Atlas Pocket health and version screen
- A local cache with explicit sync states
- A field-support checklist prototype
- A QR or document capture flow
- An automated mobile smoke-test suite

## Architectural approach

- Start with a small vertical slice containing input, rule, output, and test.
- Separate domain logic from frameworks, storage, and external interfaces.
- Prefer explicit contracts and replaceable adapters.
- Add infrastructure only when a concrete use case requires it.
- Document irreversible or high-impact decisions through ADRs.

## Dependency tracks

- [`mobile.txt`](../../../requirements/mobile.txt)
- [`mobile_ai.txt`](../../../requirements/mobile_ai.txt)
- [`mobile_testing.txt`](../../../requirements/mobile_testing.txt)

## Integration with Atlas

- Consumes Atlas API rather than remote databases
- Caches BI and Support information for field use
- Calls AI services or runs approved lightweight models

## Quality and evidence

- Unit tests for deterministic rules and transformations.
- Integration tests at external boundaries.
- Versioned data, seeds, and configuration when required.
- Technical and product metrics appropriate to the experiment.
- README, examples, and limitations updated with the code.
- No committed secrets or personal data.

## Incremental roadmap

### 1. Foundation

Define the glossary, initial use case, contract, and minimum test.

### 2. Applied prototype

Run a real use case with controlled data or infrastructure.

### 3. Integration

Connect the result to another module through an explicit contract.

### 4. Maturity

Add observability, operational documentation, and risk assessment.

## Definition of done

- The primary use case runs from clean setup instructions.
- Relevant behaviors have tests proportional to risk.
- Inputs, outputs, errors, and limitations are documented.
- Dependencies belong to the declared tracks.
- Integration respects Atlas boundaries.
- A short demonstration exists for technical review.

## Status

Planned track. This documentation defines the evolution contract; implementation should progress incrementally and reflect the repository's real state.
