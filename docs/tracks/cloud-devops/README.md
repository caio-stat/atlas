# Atlas Cloud and DevOps Lab

> Repeatable environments, cloud experiments, delivery automation, and cost-aware operations.

**English** | [Português](README.pt-BR.md)

[Tracks index](../README.md) · [Documentation](../../README.md) · [Project](../../../README.md)

## Mission

The Cloud and DevOps Lab evolves Atlas from local execution to repeatable delivery. Infrastructure must be reviewable, least-privilege, observable, cost-bounded, and removable without leaving undocumented resources behind.

## Expected outcomes

- Turn study into executable, tested, and demonstrable software.
- Record assumptions, decisions, limitations, and evidence reproducibly.
- Deliver integrable components without unnecessary coupling.
- Produce portfolio material that explains the result and the reasoning.

## Technical scope

- Docker and Compose environments
- Cloud SDK and local-cloud experiments
- Infrastructure as code
- CI/CD and quality gates
- Secrets and environment management
- Deployment, rollback, and zero downtime
- Cost tagging, budgets, and cleanup

## Reference deliverables

- A reproducible local development stack
- A CI pipeline for tests and static checks
- A LocalStack or sandbox cloud exercise
- An infrastructure plan with teardown steps
- A deployment and rollback runbook

## Architectural approach

- Start with a small vertical slice containing input, rule, output, and test.
- Separate domain logic from frameworks, storage, and external interfaces.
- Prefer explicit contracts and replaceable adapters.
- Add infrastructure only when a concrete use case requires it.
- Document irreversible or high-impact decisions through ADRs.

## Dependency tracks

- [`cloud.txt`](../../../requirements/cloud.txt)
- [`aws.txt`](../../../requirements/aws.txt)
- [`cloud_orchestration.txt`](../../../requirements/cloud_orchestration.txt)
- [`devops.txt`](../../../requirements/devops.txt)
- [`zero_downtime.txt`](../../../requirements/zero_downtime.txt)
- [`security.txt`](../../../requirements/security.txt)

## Integration with Atlas

- Hosts Atlas API and data services
- Supplies environments for every executable track
- Provides deployment metadata to Observability

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
