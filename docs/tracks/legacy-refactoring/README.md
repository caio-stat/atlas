# Atlas Legacy and Refactoring Lab

> Characterization, safe modernization, architecture recovery, and technical-debt evidence.

**English** | [Português](README.pt-BR.md)

[Tracks index](../README.md) · [Documentation](../../README.md) · [Project](../../../README.md)

## Mission

The Legacy and Refactoring Lab demonstrates how real systems improve without rewriting blindly. It preserves observable behavior, creates safety nets, measures structural problems, and migrates responsibilities in reviewable steps.

## Expected outcomes

- Turn study into executable, tested, and demonstrable software.
- Record assumptions, decisions, limitations, and evidence reproducibly.
- Deliver integrable components without unnecessary coupling.
- Produce portfolio material that explains the result and the reasoning.

## Technical scope

- Characterization and approval tests
- Static analysis and complexity measurement
- Dependency and architecture recovery
- Incremental refactoring patterns
- Adapters and Strangler Fig migrations
- Technical-debt records and prioritization
- Compatibility, deprecation, and rollback

## Reference deliverables

- An intentionally flawed legacy fixture
- A characterization-test safety net
- A measured refactoring case study
- An adapter-based migration
- A before-and-after architecture report

## Architectural approach

- Start with a small vertical slice containing input, rule, output, and test.
- Separate domain logic from frameworks, storage, and external interfaces.
- Prefer explicit contracts and replaceable adapters.
- Add infrastructure only when a concrete use case requires it.
- Document irreversible or high-impact decisions through ADRs.

## Dependency tracks

- [`refactoring.txt`](../../../requirements/refactoring.txt)
- [`code_quality.txt`](../../../requirements/code_quality.txt)
- [`advanced_testing.txt`](../../../requirements/advanced_testing.txt)
- [`software_design.txt`](../../../requirements/software_design.txt)
- [`oop.txt`](../../../requirements/oop.txt)

## Integration with Atlas

- Modernizes modules without breaking contracts
- Feeds quality policy into CI/CD
- Produces ADRs and migration runbooks

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
