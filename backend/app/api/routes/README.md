# Atlas API route modules

> Thin HTTP handlers grouped by resource and operational concern.

**English** | [Português](README.pt-BR.md)

[Backend](../../../README.md) · [Modules catalog](../../../../docs/modules/README.md)

## Current status

Empty scaffold. `health.py` exists but contains no route; health and version handlers remain in `app/main.py`.

## Responsibilities

- Declare route paths, methods, status codes, and schemas
- Resolve application dependencies
- Call one application use case per operation when practical
- Map known errors to documented responses
- Keep handler behavior small and reviewable

## Out of scope

- Encode business decisions
- Construct global infrastructure inside handlers
- Perform ad hoc SQL
- Silently swallow application failures

## Contracts and boundaries

- `health.py` should own liveness and readiness routes
- Future resource files should expose FastAPI `APIRouter` objects
- Routers should be mounted centrally with explicit prefixes and tags

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

1. Implement an `APIRouter` for `/health` and `/version`
2. Preserve current response bodies during extraction
3. Add a separate `/ready` contract before checking PostgreSQL
4. Test router inclusion from the application factory

## Definition of done

- The module responsibility is reflected in code.
- Public contracts and errors are documented.
- Risk-proportional tests run through a documented command.
- Configuration and secrets are not coupled to source code.
- This document's status matches the repository.
