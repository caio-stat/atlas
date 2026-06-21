# Atlas domain entities

> Identity-bearing domain objects that protect lifecycle rules and invariants.

**English** | [Português](README.pt-BR.md)

[Backend](../../../README.md) · [Modules catalog](../../../../docs/modules/README.md)

## Current status

Empty scaffold. `data_source.py` exists but has no class or behavior.

## Responsibilities

- Represent identity and lifecycle transitions
- Validate domain invariants at construction or mutation
- Use precise domain types instead of unrelated primitives
- Expose behavior-oriented methods
- Remain serializable only through external mappers when possible

## Out of scope

- Mirror database tables mechanically
- Contain HTTP request or response schemas
- Open sessions or call external services
- Accumulate formatting and presentation helpers

## Contracts and boundaries

- Planned `DataSource` identity
- Planned source name, location/type, and lifecycle status
- Explicit validation errors for invalid construction

## Dependency direction

```text
HTTP / framework
      ↓
application use cases
      ↓
domain contracts
      ↑
infrastructure adapters
```

The module should depend on more stable contracts and receive external details through composition. Imports that reverse this direction require architectural justification.

## Testing strategy

- Test public behavior rather than framework details.
- Use unit tests for pure rules and contract tests at boundaries.
- Cover success, validation, known failures, and security behavior.
- Keep fixtures small, deterministic, and free of sensitive data.

## Evolution rules

- Implement one vertical slice before generalizing.
- Do not add an abstraction without a concrete consumer.
- Update both README languages with contract changes.
- Record cross-cutting or costly-to-reverse decisions in an ADR.

## Next steps

1. Decide the minimum fields from a concrete registration use case
2. Model identity and invariants
3. Add equality and lifecycle tests
4. Keep persistence mapping outside the entity

## Definition of done

- The module responsibility is reflected in code.
- Public contracts and errors are documented.
- Risk-proportional tests run through a documented command.
- Configuration and secrets are not coupled to source code.
- This document's status matches the repository.
