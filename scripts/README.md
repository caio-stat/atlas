# Atlas operational scripts

> Small entry points for repeatable development, maintenance, and support tasks.

**English** | [Português](README.pt-BR.md)

[Project](../README.md) · [Modules](../docs/modules/README.md)

## Current status

**Empty scaffold.** The directory exists but contains no implementation beyond this documentation.

## Purpose

Scripts should make a bounded operation easier to repeat. They are not a shortcut around module boundaries, tests, configuration, or safety. Complex logic should move into an importable module and leave the script as a thin entry point.

## Inside the boundary

- Development setup and verification commands
- Data retrieval and report entry points
- Safe support diagnostics
- Migration and maintenance wrappers
- Mobile and device automation helpers

## Outside the boundary

- Long-lived business logic
- Hard-coded credentials or machine-specific paths
- Destructive defaults
- Unlogged external mutations
- Scripts with no owner or usage documentation

## Proposed structure

```text
development/
data/
support/
operations/
mobile/
```

The structure is directional. Create subdirectories only when a real deliverable needs them.

## Workflow

1. Define one problem and a small acceptance criterion.
2. Choose inputs, outputs, and contract before tools.
3. Implement an executable slice with a test.
4. Record configuration, risks, and limitations.
5. Connect the module through an explicit contract and update status.

## Related dependencies

- [`scripting.txt`](../requirements/scripting.txt)
- [`automation.txt`](../requirements/automation.txt)
- [`support.txt`](../requirements/support.txt)

## Related tracks

- [automation](../docs/tracks/automation/README.md)
- [support](../docs/tracks/support/README.md)
- [cloud-devops](../docs/tracks/cloud-devops/README.md)

## Quality, security, and operations

- Add risk-proportional tests before integration.
- Keep configuration outside source and never commit secrets.
- Document expected failures, retries, rollback, and ownership where applicable.
- Use minimal, public, or anonymized data in examples.
- Measure cost and resources before expanding the solution.

## Next steps

1. Choose one repeated manual repository task
2. Implement a dry-run or read-only default
3. Add `--help`, exit codes, and structured output
4. Test core logic outside the CLI wrapper

## First-deliverable definition of done

- A small executable use case exists.
- Setup and verification work from a clean checkout.
- Contracts, errors, and limitations are documented.
- Tests and evidence demonstrate behavior.
- This README has been updated to reflect real code.
