# Atlas infrastructure module

> Versioned local environments, deployment definitions, telemetry stacks, and operational configuration.

**English** | [Português](README.pt-BR.md)

[Project](../README.md) · [Modules](../docs/modules/README.md)

## Current status

**Empty scaffold.** The directory exists but contains no implementation beyond this documentation.

## Purpose

The infrastructure module should make environments repeatable and disposable. It owns deployment and runtime configuration, not business rules. The current PostgreSQL Compose definition remains at the repository root and can move only with a documented migration.

## Inside the boundary

- Container and Compose definitions
- Database initialization and migration support
- Monitoring and local telemetry stacks
- Infrastructure-as-code experiments
- CI/CD and deployment configuration
- Runbooks and teardown procedures

## Outside the boundary

- Application business logic
- Cloud resources without cost and cleanup controls
- Production secrets
- Unreviewed scripts that mutate shared infrastructure

## Proposed structure

```text
docker/
postgres/
monitoring/
cloud/
ci/
runbooks/
```

The structure is directional. Create subdirectories only when a real deliverable needs them.

## Workflow

1. Define one problem and a small acceptance criterion.
2. Choose inputs, outputs, and contract before tools.
3. Implement an executable slice with a test.
4. Record configuration, risks, and limitations.
5. Connect the module through an explicit contract and update status.

## Related dependencies

- [`devops.txt`](../requirements/devops.txt)
- [`cloud_orchestration.txt`](../requirements/cloud_orchestration.txt)
- [`observability.txt`](../requirements/observability.txt)
- [`security.txt`](../requirements/security.txt)

## Related tracks

- [cloud-devops](../docs/tracks/cloud-devops/README.md)
- [observability](../docs/tracks/observability/README.md)
- [systems](../docs/tracks/systems/README.md)

## Quality, security, and operations

- Add risk-proportional tests before integration.
- Keep configuration outside source and never commit secrets.
- Document expected failures, retries, rollback, and ownership where applicable.
- Use minimal, public, or anonymized data in examples.
- Measure cost and resources before expanding the solution.

## Next steps

1. Document ownership of the root Compose file
2. Add a database readiness check and migration workflow
3. Define local telemetry only after the API emits signals
4. Add teardown and data-retention instructions

## First-deliverable definition of done

- A small executable use case exists.
- Setup and verification work from a clean checkout.
- Contracts, errors, and limitations are documented.
- Tests and evidence demonstrate behavior.
- This README has been updated to reflect real code.
