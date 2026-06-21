# Atlas API

> The HTTP interface that exposes Atlas capabilities through stable, observable contracts.

**English** | [Português](README.pt-BR.md)

[Tracks index](../README.md) · [Documentation](../../README.md) · [Project](../../../README.md)

## Mission

Atlas API is the primary entry point for clients during the foundation phase. It should translate HTTP concerns into application calls, keep business rules outside route handlers, make operational state visible through health, version, and future readiness endpoints, and support trust, transparency, and informed interaction for every user and client.

## Expected outcomes

- Turn study into executable, tested, and demonstrable software.
- Record assumptions, decisions, limitations, and evidence reproducibly.
- Deliver components that can integrate with the ecosystem without unnecessary coupling.
- Produce portfolio material that explains both the result and the reasoning.

## Technical scope

- FastAPI application composition
- REST resource and error conventions
- Request and response validation
- Health, readiness, and version endpoints
- OpenAPI documentation and examples
- Authentication and authorization boundaries
- Pagination, idempotency, and correlation IDs
- Clear error semantics, consent signals, and accessibility-friendly responses

## Reference deliverables

- Documented `/`, `/health`, and `/version` behavior
- Versioned routers for data-source operations
- Consistent problem-detail error responses
- API contract and integration tests
- Operational middleware for logs and request IDs

## Architectural approach

- Start with a small vertical slice containing input, rule, output, and test.
- Separate domain logic from frameworks, storage, and external interfaces.
- Prefer explicit contracts and replaceable adapters over global dependencies.
- Add infrastructure only when a concrete use case requires it.
- Document irreversible or high-impact decisions through ADRs.

## Dependency tracks

- [`dev.txt`](../../../requirements/dev.txt)
- [`data_engineering.txt`](../../../requirements/data_engineering.txt)
- [`security.txt`](../../../requirements/security.txt)
- [`observability.txt`](../../../requirements/observability.txt)

## Integration with Atlas

- Calls Atlas Core use cases
- Persists through Data Engineering adapters
- Serves web, mobile, automation, and agent clients

## Quality and evidence

- Unit tests for deterministic rules and transformations.
- Integration tests at database, network, file, or provider boundaries.
- Versioned data, seeds, and configuration whenever reproduction depends on them.
- Technical and product metrics appropriate to the experiment.
- Behavioral and trust metrics such as clarity of responses, recovery from failures, and user confidence.
- README, usage examples, and limitation notes updated with the code.
- No secrets, personal data, or heavy artifacts committed without justification.

## Incremental roadmap

### 1. Foundation

Define the glossary, initial use case, contract, and minimum test.

### 2. Applied prototype

Run a real use case with controlled data or infrastructure.

### 3. Integration

Connect the result to at least one other module through an explicit contract.

### 4. Maturity

Add observability, operational documentation, and risk assessment.

## Definition of done

- The primary use case runs from clean setup instructions.
- Relevant behaviors have tests proportional to their risk.
- Inputs, outputs, errors, and limitations are documented.
- Used dependencies belong to the declared tracks.
- Integration does not violate Atlas architectural boundaries.
- A short, understandable demonstration is available for technical review.

## Status

Planned track. This documentation defines the evolution contract; implementations should be added incrementally and must reflect the repository's real state.
