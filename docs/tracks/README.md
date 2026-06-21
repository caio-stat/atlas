# Atlas technical tracks

> Detailed execution guides for the learning and implementation domains that compose Atlas.

**English** | [Português](README.pt-BR.md)

[Documentation hub](../README.md) · [Project README](../../README.md) · [Dependency catalog](../../requirements/README.md)

## How to use this catalog

Each track README defines a mission, technical scope, reference deliverables,
dependency files, integration boundaries, quality evidence, an incremental
roadmap, and a definition of done. A track is a product direction, not proof
that every listed capability already exists.

Use the catalog in this order:

1. Choose one track and one small deliverable.
2. Install only its declared dependency files.
3. Build a vertical slice with tests and documentation.
4. Integrate through explicit contracts with another Atlas module.
5. Update status and evidence when the implementation changes.

## Foundation and interfaces

| Track | Responsibility | Current state |
|---|---|---|
| [Atlas Core](core/README.md) | Domain language, use cases, and shared contracts | Foundation scaffold |
| [Atlas API](api/README.md) | HTTP contracts and application composition | Initial endpoints available |
| [Legacy and Refactoring](legacy-refactoring/README.md) | Safe modernization and technical-debt evidence | Planned |

## Data, mathematics, and intelligence

| Track | Responsibility | Current state |
|---|---|---|
| [Data Mining](data-mining/README.md) | Responsible collection, scraping, OCR, and documents | Planned |
| [ETL and Data Engineering](data-engineering/README.md) | Ingestion, storage, lineage, and data quality | Foundation scaffold |
| [Statistical Lab](statistics/README.md) | Inference, uncertainty, regression, and forecasting | Planned |
| [Calculus and Numerical Methods](numerical-methods/README.md) | Numerical reliability, optimization, and simulation | Planned |
| [Machine Learning](machine-learning/README.md) | Classical ML and reproducible evaluation | Planned |
| [Deep Learning](deep-learning/README.md) | Neural models and accountable training | Planned |
| [AI Lab](ai/README.md) | RAG, LLMs, agents, tools, and policy controls | Planned |
| [BI and Storytelling](bi-storytelling/README.md) | Metrics, dashboards, reports, and data communication | Planned |

## Operations and runtime systems

| Track | Responsibility | Current state |
|---|---|---|
| [Automation](automation/README.md) | Scheduled, event-driven, and operational workflows | Planned |
| [Support](support/README.md) | Diagnostics, inventory, and helpdesk evidence | Planned |
| [Networking](networking/README.md) | Connectivity diagnostics and protocol experiments | Planned |
| [Messaging and Real-Time](messaging-real-time/README.md) | Queues, streams, workers, and live interfaces | Planned |
| [Cloud and DevOps](cloud-devops/README.md) | Environments, delivery, cloud, and infrastructure | Local Compose foundation |
| [Observability](observability/README.md) | Logs, metrics, traces, and operational insight | Planned |
| [Systems](systems/README.md) | Concurrency, distribution, security, and resilience | Planned |

## Devices and interactive applications

| Track | Responsibility | Current state |
|---|---|---|
| [Mobile](mobile/README.md) | Atlas Pocket, offline-first clients, and mobile AI | Stack specified |
| [Embedded, IoT, and Autonomous Systems](embedded-iot-autonomous/README.md) | Devices, protocols, control, and edge behavior | Planned |
| [Games and Simulation](games-simulation/README.md) | Interactive simulations, agents, and telemetry | Planned |

## Status vocabulary

- **Planned:** scope is documented, but no representative implementation exists.
- **Foundation scaffold:** supporting code or structure exists but the first full slice is incomplete.
- **Prototype:** one runnable vertical slice demonstrates the track.
- **Integrated:** the track communicates with another module through a tested contract.
- **Operational:** runbooks, telemetry, reliability checks, and maintenance ownership exist.

## Documentation rule

Track documents must remain honest. Planned architectures should be labeled as
planned; implemented behavior should link to source, tests, examples, or
operational evidence. When a track becomes code, place its module README near
the implementation and link it back to this catalog.
