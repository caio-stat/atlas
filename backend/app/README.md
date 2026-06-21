# Atlas backend application package

> Composition boundary for the FastAPI process and its architectural modules.

**English** | [Português](README.pt-BR.md)

[Backend](../README.md) · [Modules catalog](../../docs/modules/README.md)

## Current status

Partially implemented. `main.py` and `database.py` contain executable code; API, core, domain, and use-case packages are mostly empty scaffolds.

## Responsibilities

- Create and configure the FastAPI application
- Connect interface adapters to application use cases
- Own process startup and shutdown wiring
- Expose infrastructure factories at the composition root
- Keep dependency direction visible

## Out of scope

- Implement business rules directly in route handlers
- Turn shared helpers into an unbounded utility layer
- Let domain code import FastAPI or SQLAlchemy
- Hide environment configuration in module globals

## Contracts and boundaries

- ASGI application `app.main:app`
- HTTP endpoints currently declared in `main.py`
- SQLAlchemy `engine` and `SessionLocal` in `database.py`

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

1. Move routes into the API package
2. Move configuration into typed core settings
3. Implement one domain entity and use case
4. Add repository and transaction boundaries

## Definition of done

- The module responsibility is reflected in code.
- Public contracts and errors are documented.
- Risk-proportional tests run through a documented command.
- Configuration and secrets are not coupled to source code.
- This document's status matches the repository.
