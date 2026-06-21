# Atlas ETL and Data Engineering

> Reproducible ingestion, transformation, storage, and data-quality pipelines.

**English** | [Português](README.pt-BR.md)

[Tracks index](../README.md) · [Documentation](../../README.md) · [Project](../../../README.md)

## Mission

This track owns the path from raw assets to trusted analytical datasets. Pipelines should be rerunnable, observable, schema-aware, and explicit about lineage and quality expectations.

## Expected outcomes

- Turn study into executable, tested, and demonstrable software.
- Record assumptions, decisions, limitations, and evidence reproducibly.
- Deliver components that can integrate with the ecosystem without unnecessary coupling.
- Produce portfolio material that explains both the result and the reasoning.

## Technical scope

- Batch and incremental ingestion
- Schema validation and evolution
- SQL modeling and migrations
- Data cleaning and normalization
- Lineage, partitioning, and retention
- Data-quality checks and quarantine
- Local analytical storage and warehouse patterns

## Reference deliverables

- Raw-to-processed pipeline templates
- PostgreSQL data-source persistence
- DuckDB analytical examples
- Quality reports with rejected-row reasons
- A documented dataset contract

## Architectural approach

- Start with a small vertical slice containing input, rule, output, and test.
- Separate domain logic from frameworks, storage, and external interfaces.
- Prefer explicit contracts and replaceable adapters over global dependencies.
- Add infrastructure only when a concrete use case requires it.
- Document irreversible or high-impact decisions through ADRs.

## Dependency tracks

- [`data.txt`](../../../requirements/data.txt)
- [`data_engineering.txt`](../../../requirements/data_engineering.txt)
- [`big_data.txt`](../../../requirements/big_data.txt)
- [`cloud.txt`](../../../requirements/cloud.txt)

## Integration with Atlas

- Consumes Data Mining outputs
- Supplies Statistics, ML, BI, and AI
- Publishes execution signals to Messaging and Observability

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
