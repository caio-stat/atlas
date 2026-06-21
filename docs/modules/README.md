# Atlas system modules

> Documentation for concrete executable modules and product specifications.

**English** | [Português](README.pt-BR.md)

[Documentation hub](../README.md) · [Technical tracks](../tracks/README.md) · [Project README](../../README.md)

## Catalog

| Module | Role | Implementation state | Documentation |
|---|---|---|---|
| Atlas backend | FastAPI application and PostgreSQL foundation | Initial endpoints and connection scaffold | [Backend](../../backend/README.md) |
| Application package | Composition of API, core, domain, and use cases | Partial scaffold | [Application](../../backend/app/README.md) |
| API interface | HTTP transport and route organization | Initial routes live in `main.py` | [API](../../backend/app/api/README.md) |
| Core configuration | Settings and cross-cutting application primitives | Empty scaffold | [Core](../../backend/app/core/README.md) |
| Domain model | Business entities and invariants | Empty scaffold | [Domain](../../backend/app/domain/README.md) |
| Use cases | Application orchestration | Empty scaffold | [Use cases](../../backend/app/use_cases/README.md) |
| Backend tests | Executable API behavior checks | Health and version tests | [Tests](../../backend/tests/README.md) |
| Analytics | Reusable statistics, ML evaluation, and reporting code | Empty scaffold | [Analytics](../../analytics/README.md) |
| Client applications | Container for deployable user interfaces | Empty scaffold | [Applications](../../apps/README.md) |
| Android application | Implementation location for Atlas Pocket | Empty scaffold | [Mobile application](../../apps/mobile/README.md) |
| Datasets | Samples, metadata, provenance, and schemas | Empty scaffold | [Datasets](../../datasets/README.md) |
| Infrastructure | Environments, deployment, telemetry, and runbooks | Empty scaffold | [Infrastructure](../../infra/README.md) |
| Notebooks | Reproducible exploration and analytical narratives | Empty scaffold | [Notebooks](../../notebooks/README.md) |
| Data collection | Responsible web, document, and public-data adapters | Empty scaffold | [Scrapers](../../scrapers/README.md) |
| Operational scripts | Thin entry points for repeatable tasks | Empty scaffold | [Scripts](../../scripts/README.md) |
| Mobile automation | ADB, Appium, fixtures, logs, and smoke-test helpers | Empty scaffold | [Mobile scripts](../../scripts/mobile/README.md) |
| Atlas Mobile Lab | Atlas Pocket and field-client specification | Planned; stack documented | [Mobile Lab](mobile-lab/README.md) |

## Module documentation contract

Every implemented module should document:

- its responsibility and explicit non-responsibilities;
- public functions, endpoints, messages, files, or schemas;
- dependencies and configuration;
- runtime flow and failure behavior;
- commands for local execution and verification;
- test strategy and current coverage boundaries;
- security, privacy, and operational considerations;
- extension rules and known limitations;
- implementation status backed by repository evidence.

## Relationship with tracks

Tracks define long-lived areas of learning and product development. Modules are
concrete units that implement part of one or more tracks. For example, the
backend API module implements parts of Atlas Core, Atlas API, Data Engineering,
Cloud/DevOps, and Observability. A module may serve several tracks, but it should
have one clear runtime responsibility.

## Status rule

An empty package is a scaffold, not an implemented module. Documentation may
describe its intended boundary, but its status must remain explicit until code,
tests, and a runnable example exist.
