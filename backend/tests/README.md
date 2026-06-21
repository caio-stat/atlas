# Atlas backend tests

> Executable evidence for backend contracts, domain behavior, and integration boundaries.

**English** | [Português](README.pt-BR.md)

[Backend](../README.md) · [Modules catalog](../../docs/modules/README.md)

## Current status

Initial coverage exists in `test_health.py` for `/health` and `/version`. The test name `test_root_endpoint` currently exercises `/health`, which should be renamed for clarity.

## Responsibilities

- Verify public behavior and error contracts
- Protect domain invariants during refactoring
- Exercise persistence and migration integration
- Provide deterministic regression evidence
- Keep slow or external tests clearly marked

## Out of scope

- Depend on test execution order
- Call uncontrolled production services
- Hide flaky behavior through unconditional retries
- Assert private implementation details without need

## Contracts and boundaries

- `python -m pytest` from `backend/`
- FastAPI `TestClient` for current endpoint tests
- Future unit, integration, contract, and architecture test layers

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

1. Rename the health test to match its behavior
2. Add a test for `GET /`
3. Add invalid-path and OpenAPI smoke tests
4. Create domain tests before implementing persistence
5. Introduce integration fixtures when migrations exist

## Definition of done

- The module responsibility is reflected in code.
- Public contracts and errors are documented.
- Risk-proportional tests run through a documented command.
- Configuration and secrets are not coupled to source code.
- This document's status matches the repository.
