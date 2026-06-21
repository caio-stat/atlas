# Atlas Machine Learning Lab

> Reproducible classical machine-learning experiments and model evaluation.

**English** | [Português](README.pt-BR.md)

[Tracks index](../README.md) · [Documentation](../../README.md) · [Project](../../../README.md)

## Mission

The Machine Learning Lab turns curated datasets into measured predictive experiments. Baselines, leakage prevention, feature provenance, cross-validation, and reproducibility matter more than headline scores.

## Expected outcomes

- Turn study into executable, tested, and demonstrable software.
- Record assumptions, decisions, limitations, and evidence reproducibly.
- Deliver components that can integrate with the ecosystem without unnecessary coupling.
- Produce portfolio material that explains both the result and the reasoning.

## Technical scope

- Supervised classification and regression
- Clustering and dimensionality reduction
- Feature engineering and selection
- Cross-validation and metric design
- Class imbalance and calibration
- Hyperparameter optimization
- Experiment tracking and model packaging

## Reference deliverables

- A baseline-first experiment template
- A classification pipeline with leakage checks
- A regression benchmark with residual analysis
- Tracked experiments and model cards
- An inference adapter with a stable contract

## Architectural approach

- Start with a small vertical slice containing input, rule, output, and test.
- Separate domain logic from frameworks, storage, and external interfaces.
- Prefer explicit contracts and replaceable adapters over global dependencies.
- Add infrastructure only when a concrete use case requires it.
- Document irreversible or high-impact decisions through ADRs.

## Dependency tracks

- [`ml.txt`](../../../requirements/ml.txt)
- [`data.txt`](../../../requirements/data.txt)
- [`statistics.txt`](../../../requirements/statistics.txt)
- [`mlops.txt`](../../../requirements/mlops.txt)

## Integration with Atlas

- Consumes versioned analytical datasets
- Compares results with Statistical Lab baselines
- Exposes approved inference through Atlas API

## Quality and evidence

- Unit tests for deterministic rules and transformations.
- Integration tests at database, network, file, or provider boundaries.
- Versioned data, seeds, and configuration whenever reproduction depends on them.
- Technical and product metrics appropriate to the experiment.
- README, usage examples, and limitation notes updated with the code.
- No secrets, personal data, or heavy artifacts committed without justification.

## Incremental roadmap

### 1. Foundation

Define the glossary, initial use case, contract, and minimum test.

### 2. Applied prototype

Run a real use case with controlled data or infrastructure.

### 3. Integration

Connect the result to at least one other module through an explicit contract.

### 4. Maturity

Add observability, operational documentation, and risk assessment.

## Definition of done

- The primary use case runs from clean setup instructions.
- Relevant behaviors have tests proportional to their risk.
- Inputs, outputs, errors, and limitations are documented.
- Used dependencies belong to the declared tracks.
- Integration does not violate Atlas architectural boundaries.
- A short, understandable demonstration is available for technical review.

## Status

Planned track. This documentation defines the evolution contract; implementations should be added incrementally and must reflect the repository's real state.
