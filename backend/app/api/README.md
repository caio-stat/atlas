# Atlas API interface module

> HTTP transport boundary for validation, routing, serialization, and status codes.

**English** | [Português](README.pt-BR.md)

[Backend](../../README.md) · [Modules catalog](../../../docs/modules/README.md)

## Current status

Scaffold. The package exists, but current endpoints are still defined directly in `app/main.py`.

## Responsibilities

- Organize versioned FastAPI routers
- Validate request and response schemas
- Translate application errors into HTTP responses
- Apply transport concerns such as pagination and request IDs
- Publish accurate OpenAPI metadata

## Out of scope

- Contain domain invariants or persistence queries
- Open unmanaged database sessions
- Return internal exceptions or secret configuration
- Couple use cases to FastAPI request objects

## Contracts and boundaries

- Planned versioned router mounted by `app.main`
- Pydantic request and response schemas
- Consistent error representation
- Health, readiness, and version interface

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
- Do not add an abstraction without at least one concrete consumer.
- Update both README languages with contract changes.
- Record cross-cutting or costly-to-reverse decisions in an ADR.

## Next steps

1. Extract existing endpoints without changing behavior
2. Add router-level tests
3. Define error and versioning conventions
4. Add the first data-source endpoint

## Definition of done

- The module responsibility is reflected in code.
- Public contracts and errors are documented.
- Risk-proportional tests run through a documented command.
- Configuration and secrets are not coupled to source code.
- This document's status matches the repository.
