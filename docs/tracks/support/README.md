# Atlas Support Lab

> Practical diagnostics, inventory, health checks, and support reporting.

**English** | [Português](README.pt-BR.md)

[Tracks index](../README.md) · [Documentation](../../README.md) · [Project](../../../README.md)

## Mission

The Support Lab converts helpdesk routines into safe, explainable tools. Diagnostics should collect only necessary data, distinguish evidence from inference, avoid destructive remediation by default, and generate reports that another technician can review.

## Expected outcomes

- Turn study into executable, tested, and demonstrable software.
- Record assumptions, decisions, limitations, and evidence reproducibly.
- Deliver integrable components without unnecessary coupling.
- Produce portfolio material that explains the result and the reasoning.

## Technical scope

- CPU, memory, disk, and process diagnostics
- Service and endpoint health checks
- Hardware and software inventory
- Windows and Linux support probes
- Network and DNS diagnostics
- Markdown, HTML, and JSON reports
- Consent, privacy, and safe remediation

## Reference deliverables

- A read-only support diagnostics CLI
- A machine inventory snapshot
- A disk and memory health report
- A service availability checker
- A redacted incident evidence bundle

## Architectural approach

- Start with a small vertical slice containing input, rule, output, and test.
- Separate domain logic from frameworks, storage, and external interfaces.
- Prefer explicit contracts and replaceable adapters.
- Add infrastructure only when a concrete use case requires it.
- Document irreversible or high-impact decisions through ADRs.

## Dependency tracks

- [`support.txt`](../../../requirements/support.txt)
- [`automation.txt`](../../../requirements/automation.txt)
- [`scripting.txt`](../../../requirements/scripting.txt)
- [`networking.txt`](../../../requirements/networking.txt)

## Integration with Atlas

- Feeds operational evidence to Observability
- Uses Networking probes for connectivity issues
- Can surface summaries through Atlas API and Mobile

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
