# Atlas datasets module

> Governed workspace for small, reproducible data samples and dataset metadata.

**English** | [Português](README.pt-BR.md)

[Project](../README.md) · [Modules](../docs/modules/README.md)

## Current status

**Empty scaffold.** The directory exists but contains no implementation beyond this documentation.

## Purpose

The datasets directory defines how Atlas references data without turning Git into a data lake. Small public samples and metadata may be versioned; large, private, licensed, or generated datasets belong in external storage with reproducible retrieval instructions.

## Inside the boundary

- Dataset cards and source provenance
- Small public samples required by tests or demos
- Schemas, checksums, and retrieval manifests
- Licensing, retention, and sensitivity notes
- Documented raw-to-processed boundaries

## Outside the boundary

- Secrets or personal data
- Large binaries without an artifact strategy
- Unlicensed copies of third-party data
- Manual edits without lineage
- Model outputs mixed with source data

## Proposed structure

```text
raw/ (ignored or external)
processed/ (reproducible)
samples/ (small and public)
schemas/
README cards per dataset
```

The structure is directional. Create subdirectories only when a real deliverable needs them.

## Workflow

1. Define one problem and a small acceptance criterion.
2. Choose inputs, outputs, and contract before tools.
3. Implement an executable slice with a test.
4. Record configuration, risks, and limitations.
5. Connect the module through an explicit contract and update status.

## Related dependencies

- [`data.txt`](../requirements/data.txt)
- [`data_engineering.txt`](../requirements/data_engineering.txt)

## Related tracks

- [data-mining](../docs/tracks/data-mining/README.md)
- [data-engineering](../docs/tracks/data-engineering/README.md)
- [statistics](../docs/tracks/statistics/README.md)

## Quality, security, and operations

- Add risk-proportional tests before integration.
- Keep configuration outside source and never commit secrets.
- Document expected failures, retries, rollback, and ownership where applicable.
- Use minimal, public, or anonymized data in examples.
- Measure cost and resources before expanding the solution.

## Next steps

1. Select one legally reusable public dataset
2. Write its dataset card and source URL
3. Add a checksum and retrieval procedure
4. Create a tiny test sample and schema

## First-deliverable definition of done

- A small executable use case exists.
- Setup and verification work from a clean checkout.
- Contracts, errors, and limitations are documented.
- Tests and evidence demonstrate behavior.
- This README has been updated to reflect real code.
