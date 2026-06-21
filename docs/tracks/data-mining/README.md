# Atlas Data Mining

> Responsible acquisition of public, web, image, and document data.

**English** | [Português](README.pt-BR.md)

[Tracks index](../README.md) · [Documentation](../../README.md) · [Project](../../../README.md)

## Mission

The Data Mining track turns heterogeneous external sources into traceable raw assets. It emphasizes source policy, reproducibility, provenance, throttling, and failure handling before extraction volume.

## Expected outcomes

- Turn study into executable, tested, and demonstrable software.
- Record assumptions, decisions, limitations, and evidence reproducibly.
- Deliver components that can integrate with the ecosystem without unnecessary coupling.
- Produce portfolio material that explains both the result and the reasoning.

## Technical scope

- HTTP collection and browser automation
- HTML and structured-data parsing
- PDF extraction and document layout
- OCR for scanned images
- Source provenance and collection manifests
- Rate limiting, retries, and incremental collection
- Ethical and legal collection constraints

## Reference deliverables

- A source-adapter protocol
- A reproducible public-data collector
- Raw-data manifests with hashes and timestamps
- OCR and PDF extraction comparison
- Failure fixtures and respectful retry policies

## Architectural approach

- Start with a small vertical slice containing input, rule, output, and test.
- Separate domain logic from frameworks, storage, and external interfaces.
- Prefer explicit contracts and replaceable adapters over global dependencies.
- Add infrastructure only when a concrete use case requires it.
- Document irreversible or high-impact decisions through ADRs.

## Dependency tracks

- [`scraping.txt`](../../../requirements/scraping.txt)
- [`ocr.txt`](../../../requirements/ocr.txt)
- [`document_intelligence.txt`](../../../requirements/document_intelligence.txt)
- [`data.txt`](../../../requirements/data.txt)

## Integration with Atlas

- Feeds ETL ingestion zones
- Provides documents to AI retrieval pipelines
- Exposes collection status to Observability

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
