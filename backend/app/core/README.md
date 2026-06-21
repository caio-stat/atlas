# Atlas backend core module

> Typed configuration and narrowly scoped process-wide primitives.

**English** | [Português](README.pt-BR.md)

[Backend](../../README.md) · [Modules catalog](../../../docs/modules/README.md)

## Current status

Empty scaffold. `config.py` exists but does not yet define settings.

## Responsibilities

- Load and validate environment-backed settings
- Define application environment and feature flags
- Provide logging and telemetry configuration
- Host stable typed exceptions when truly cross-cutting
- Keep secret values out of source code

## Out of scope

- Contain domain entities or use cases
- Create database sessions during import
- Become a miscellaneous helper package
- Read configuration independently in every module

## Contracts and boundaries

- Planned immutable settings object
- Environment variable names and safe development defaults
- A single composition-root entry point for settings

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

1. Define environment, API version, database URL, and log level
2. Move the hard-coded database URL out of `database.py`
3. Add validation tests for missing or malformed settings
4. Document a `.env.example` without secrets

## Definition of done

- The module responsibility is reflected in code.
- Public contracts and errors are documented.
- Risk-proportional tests run through a documented command.
- Configuration and secrets are not coupled to source code.
- This document's status matches the repository.
