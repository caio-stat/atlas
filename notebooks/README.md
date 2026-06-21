# Atlas notebooks module

> Reproducible exploration, education, and analytical narratives.

**English** | [Português](README.pt-BR.md)

[Project](../README.md) · [Modules](../docs/modules/README.md)

## Current status

**Empty scaffold.** The directory exists but contains no implementation beyond this documentation.

## Purpose

Notebooks are interfaces for investigation and communication, not the final home of reusable business logic. Each notebook should state its question, inputs, environment, execution order, outputs, and limitations.

## Inside the boundary

- Exploratory data analysis
- Statistical and numerical demonstrations
- Model experiments and diagnostics
- Reproducible report narratives
- Small visual explanations and teaching material

## Outside the boundary

- Secrets, personal data, or unrestricted raw datasets
- Reusable logic that lacks tests
- Hidden manual state required for execution
- Large embedded outputs committed without purpose

## Proposed structure

```text
statistics/
machine_learning/
deep_learning/
numerical_methods/
experiments/
reports/
```

The structure is directional. Create subdirectories only when a real deliverable needs them.

## Workflow

1. Define one problem and a small acceptance criterion.
2. Choose inputs, outputs, and contract before tools.
3. Implement an executable slice with a test.
4. Record configuration, risks, and limitations.
5. Connect the module through an explicit contract and update status.

## Related dependencies

- [`notebooks.txt`](../requirements/notebooks.txt)
- [`data.txt`](../requirements/data.txt)
- [`statistics.txt`](../requirements/statistics.txt)
- [`visualization.txt`](../requirements/visualization.txt)

## Related tracks

- [statistics](../docs/tracks/statistics/README.md)
- [machine-learning](../docs/tracks/machine-learning/README.md)
- [deep-learning](../docs/tracks/deep-learning/README.md)
- [bi-storytelling](../docs/tracks/bi-storytelling/README.md)

## Quality, security, and operations

- Add risk-proportional tests before integration.
- Keep configuration outside source and never commit secrets.
- Document expected failures, retries, rollback, and ownership where applicable.
- Use minimal, public, or anonymized data in examples.
- Measure cost and resources before expanding the solution.

## Next steps

1. Choose one public sample and one analytical question
2. Create a clean, restart-and-run notebook
3. Move reusable transformations into `analytics/`
4. Export a lightweight report without large cell outputs

## First-deliverable definition of done

- A small executable use case exists.
- Setup and verification work from a clean checkout.
- Contracts, errors, and limitations are documented.
- Tests and evidence demonstrate behavior.
- This README has been updated to reflect real code.
