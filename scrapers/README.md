# Atlas data collection module

> Responsible source adapters for web, document, and public-data acquisition.

**English** | [Português](README.pt-BR.md)

[Project](../README.md) · [Modules](../docs/modules/README.md)

## Current status

**Empty scaffold.** The directory exists but contains no implementation beyond this documentation.

## Purpose

The scrapers module should implement source-specific collection behind common operational contracts. Collection must respect authorization, source policies, rate limits, provenance, and reproducibility.

## Inside the boundary

- HTTP and browser source adapters
- HTML, JSON, PDF, and document extraction
- Rate limiting, retries, and incremental checkpoints
- Collection manifests and provenance
- Fixtures for parser and failure tests

## Outside the boundary

- Unauthorized access or policy bypass
- Credentials committed with collectors
- Unbounded crawling
- Silent schema changes
- Transformation logic that belongs to ETL

## Proposed structure

```text
sources/
parsers/
manifests/
fixtures/
tests/
```

The structure is directional. Create subdirectories only when a real deliverable needs them.

## Workflow

1. Define one problem and a small acceptance criterion.
2. Choose inputs, outputs, and contract before tools.
3. Implement an executable slice with a test.
4. Record configuration, risks, and limitations.
5. Connect the module through an explicit contract and update status.

## Related dependencies

- [`scraping.txt`](../requirements/scraping.txt)
- [`document_intelligence.txt`](../requirements/document_intelligence.txt)
- [`ocr.txt`](../requirements/ocr.txt)
- [`resilience.txt`](../requirements/resilience.txt)

## Related tracks

- [data-mining](../docs/tracks/data-mining/README.md)
- [data-engineering](../docs/tracks/data-engineering/README.md)
- [observability](../docs/tracks/observability/README.md)

## Quality, security, and operations

- Add risk-proportional tests before integration.
- Keep configuration outside source and never commit secrets.
- Document expected failures, retries, rollback, and ownership where applicable.
- Use minimal, public, or anonymized data in examples.
- Measure cost and resources before expanding the solution.

## Next steps

1. Select one stable, public, permitted source
2. Write a source policy and expected schema
3. Capture fixtures before live collection
4. Implement bounded collection with provenance

## First-deliverable definition of done

- A small executable use case exists.
- Setup and verification work from a clean checkout.
- Contracts, errors, and limitations are documented.
- Tests and evidence demonstrate behavior.
- This README has been updated to reflect real code.
