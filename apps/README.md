# Atlas client applications

> Container for user-facing web, mobile, and future desktop products.

**English** | [Português](README.pt-BR.md)

[Project](../README.md) · [Modules](../docs/modules/README.md)

## Current status

**Empty scaffold.** The directory exists but contains no implementation beyond this documentation.

## Purpose

The apps directory hosts deployable user interfaces that consume Atlas contracts. Each application should own its presentation and client-side state while relying on the backend for shared business capabilities and remote persistence.

## Inside the boundary

- Client application source and build configuration
- Presentation, navigation, and local state
- API adapters and client-side caching
- Accessibility and device-specific behavior
- Application-level tests and release notes

## Outside the boundary

- Direct access to the remote database
- Shared backend domain implementation
- Unversioned secrets or production endpoints
- Cross-application code copied without ownership

## Proposed structure

```text
mobile/
web/ (planned)
desktop/ (planned)
shared/ (only after real reuse)
```

The structure is directional. Create subdirectories only when a real deliverable needs them.

## Workflow

1. Define one problem and a small acceptance criterion.
2. Choose inputs, outputs, and contract before tools.
3. Implement an executable slice with a test.
4. Record configuration, risks, and limitations.
5. Connect the module through an explicit contract and update status.

## Related dependencies

- [`mobile.txt`](../requirements/mobile.txt)
- [`mobile_testing.txt`](../requirements/mobile_testing.txt)

## Related tracks

- [mobile](../docs/tracks/mobile/README.md)
- [api](../docs/tracks/api/README.md)
- [bi-storytelling](../docs/tracks/bi-storytelling/README.md)

## Quality, security, and operations

- Add risk-proportional tests before integration.
- Keep configuration outside source and never commit secrets.
- Document expected failures, retries, rollback, and ownership where applicable.
- Use minimal, public, or anonymized data in examples.
- Measure cost and resources before expanding the solution.

## Next steps

1. Implement the first Atlas Pocket status screen
2. Document API environment selection
3. Add client contract tests
4. Create other application directories only when work starts

## First-deliverable definition of done

- A small executable use case exists.
- Setup and verification work from a clean checkout.
- Contracts, errors, and limitations are documented.
- Tests and evidence demonstrate behavior.
- This README has been updated to reflect real code.
