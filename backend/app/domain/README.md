# Atlas domain module

> Business language, invariants, and stable contracts independent of frameworks.

**English** | [Português](README.pt-BR.md)

[Backend](../../README.md) · [Modules catalog](../../../docs/modules/README.md)

## Current status

Empty scaffold. The package tree exists, but no domain behavior is implemented.

## Responsibilities

- Model Atlas business concepts explicitly
- Protect invariants through entities and value objects
- Define domain errors and stable repository contracts
- Express behavior without transport or persistence concerns
- Provide terminology shared across modules

## Out of scope

- Import FastAPI, SQLAlchemy, or provider SDKs
- Validate HTTP-specific payload details
- Own environment configuration
- Perform network, file, or database I/O

## Contracts and boundaries

- Planned `DataSource` aggregate or entity
- Repository ports defined in domain or application scope
- Typed domain errors with no HTTP status knowledge

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

1. Write a domain glossary
2. Define the smallest useful `DataSource` model
3. Add invariant-focused unit tests
4. Introduce a repository protocol only when the use case needs it

## Definition of done

- The module responsibility is reflected in code.
- Public contracts and errors are documented.
- Risk-proportional tests run through a documented command.
- Configuration and secrets are not coupled to source code.
- This document's status matches the repository.
