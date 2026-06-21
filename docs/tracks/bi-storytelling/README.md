# Atlas BI and Storytelling Lab

> Decision-ready dashboards, analytical reports, and responsible data communication.

**English** | [Português](README.pt-BR.md)

[Tracks index](../README.md) · [Documentation](../../README.md) · [Project](../../../README.md)

## Mission

The BI and Storytelling Lab turns trusted data into understandable decisions. It should define audiences and questions before charts, preserve metric definitions, expose uncertainty, and keep a traceable path from visual claims to source data.

## Expected outcomes

- Turn study into executable, tested, and demonstrable software.
- Record assumptions, decisions, limitations, and evidence reproducibly.
- Deliver integrable components without unnecessary coupling.
- Produce portfolio material that explains the result and the reasoning.

## Technical scope

- Metric and KPI definition
- Exploratory and explanatory visualization
- Interactive dashboards
- Power BI and Microsoft Fabric experiments
- Notebook-to-report pipelines
- Accessible chart and color design
- Narrative structure and source traceability

## Reference deliverables

- A metric dictionary
- An analytical dashboard with documented filters
- A notebook-generated report
- A Power BI integration experiment
- A public portfolio story backed by reproducible data

## Architectural approach

- Start with a small vertical slice containing input, rule, output, and test.
- Separate domain logic from frameworks, storage, and external interfaces.
- Prefer explicit contracts and replaceable adapters.
- Add infrastructure only when a concrete use case requires it.
- Document irreversible or high-impact decisions through ADRs.

## Dependency tracks

- [`bi.txt`](../../../requirements/bi.txt)
- [`powerbi.txt`](../../../requirements/powerbi.txt)
- [`visualization.txt`](../../../requirements/visualization.txt)
- [`notebooks.txt`](../../../requirements/notebooks.txt)
- [`data.txt`](../../../requirements/data.txt)

## Integration with Atlas

- Consumes Data Engineering datasets
- Uses Statistical Lab interpretations
- Publishes summaries through web, mobile, or automated reports

## Quality and evidence

- Unit tests for deterministic rules and transformations.
- Integration tests at external boundaries.
- Versioned data, seeds, and configuration when required.
- Technical and product metrics appropriate to the experiment.
- README, examples, and limitations updated with the code.
- No committed secrets or personal data.

## Incremental roadmap

### 1. Foundation

Define the glossary, initial use case, contract, and minimum test.

### 2. Applied prototype

Run a real use case with controlled data or infrastructure.

### 3. Integration

Connect the result to another module through an explicit contract.

### 4. Maturity

Add observability, operational documentation, and risk assessment.

## Definition of done

- The primary use case runs from clean setup instructions.
- Relevant behaviors have tests proportional to risk.
- Inputs, outputs, errors, and limitations are documented.
- Dependencies belong to the declared tracks.
- Integration respects Atlas boundaries.
- A short demonstration exists for technical review.

## Status

Planned track. This documentation defines the evolution contract; implementation should progress incrementally and reflect the repository's real state.
