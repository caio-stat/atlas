# Atlas application use cases

> Application orchestration that coordinates domain behavior and external ports.

**English** | [Português](README.pt-BR.md)

[Backend](../../README.md) · [Modules catalog](../../../docs/modules/README.md)

## Current status

Empty scaffold. `register_data_source.py` exists but has no implementation.

## Responsibilities

- Represent one user or system intention per use case
- Validate application-level preconditions
- Coordinate domain objects and repository ports
- Define transaction and idempotency boundaries
- Return transport-neutral results and typed errors

## Out of scope

- Read FastAPI request objects
- Return framework response classes
- Embed SQLAlchemy queries
- Choose environment configuration dynamically

## Contracts and boundaries

- Planned `register_data_source` input and result
- Repository dependency supplied through construction
- Explicit duplicate and validation failure behavior

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

1. Write the use-case contract before the route
2. Inject a minimal repository protocol
3. Implement success and duplicate behavior
4. Test with an in-memory fake before SQLAlchemy

## Definition of done

- The module responsibility is reflected in code.
- Public contracts and errors are documented.
- Risk-proportional tests run through a documented command.
- Configuration and secrets are not coupled to source code.
- This document's status matches the repository.
