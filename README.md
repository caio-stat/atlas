# Atlas

> A modular laboratory for data, statistics, artificial intelligence, automation, infrastructure, and software engineering.

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-foundation-009688)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-local-336791)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/Docker-Compose-2496ED)](https://www.docker.com/)
[![Status](https://img.shields.io/badge/status-foundation-yellow)](#current-status)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

**English** | [Português](README.pt-BR.md)

## Contents

- [Overview](#overview)
- [Current status](#current-status)
- [Vision and goals](#vision-and-goals)
- [Architecture](#architecture)
- [Repository map](#repository-map)
- [Technical tracks](#technical-tracks)
- [System modules](#system-modules)
- [Dependency strategy](#dependency-strategy)
- [Quick start](#quick-start)
- [API behavior](#api-behavior)
- [Development workflow](#development-workflow)
- [Testing and quality](#testing-and-quality)
- [Documentation system](#documentation-system)
- [Roadmap](#roadmap)
- [Responsible use](#responsible-use)
- [Portfolio evidence](#portfolio-evidence)
- [License](#license)
- [Author](#author)

## Overview

Atlas is a long-term technical portfolio and learning laboratory designed to
connect subjects that are often studied separately: backend engineering, data
pipelines, statistics, numerical methods, machine learning, deep learning,
generative AI, automation, support tooling, networking, cloud operations,
observability, mobile applications, embedded systems, and interactive
simulation.

The project is not intended to become a pile of unrelated scripts or a catalog
of technologies installed for appearance. Every meaningful capability should
eventually become a small product slice with a clear problem, explicit
contracts, runnable code, tests, documentation, limitations, and evidence.
Beyond technical quality, Atlas should also support clarity, trust, belonging,
and human wellbeing. The system should be designed to help users understand,
make informed choices, feel respected, and experience a sense of safety within
their social and cultural context.

Atlas begins as a **modular monolith**. Distribution, queues, cloud resources,
or independent services should appear only when an implemented use case creates
a concrete need for isolation, scaling, latency, reliability, or deployment
independence.

The central question is:

> How can a technical learner evolve from scripts and notebooks into maintainable systems, trustworthy data products, and responsible intelligent applications that also strengthen clarity, autonomy, belonging, and human wellbeing?

## Current status

Atlas is in the **foundation phase**. Documentation now defines the technical
tracks and module boundaries in detail, while executable code remains small.

| Capability | Status | Evidence |
|---|---|---|
| FastAPI process | Initial implementation | [`backend/app/main.py`](backend/app/main.py) |
| Root, health, and version endpoints | Implemented | [`backend/tests/test_health.py`](backend/tests/test_health.py) |
| PostgreSQL local service | Configured | [`docker-compose.yml`](docker-compose.yml) |
| SQLAlchemy engine and session factory | Initial scaffold | [`backend/app/database.py`](backend/app/database.py) |
| Domain entity and registration use case | Empty scaffold | [`backend/app/domain`](backend/app/domain/README.md), [`backend/app/use_cases`](backend/app/use_cases/README.md) |
| Modular-monolith decision | ADR placeholder only | [`backend/0001-monolito-modular.md`](backend/0001-monolito-modular.md) |
| Dependency tracks | 76 organized sets | [`requirements/README.md`](requirements/README.md) |
| Technical-track documentation | 21 bilingual guides | [`docs/tracks/README.md`](docs/tracks/README.md) |
| Atlas Mobile Lab | Stack specified; application not created | [`docs/modules/mobile-lab/README.md`](docs/modules/mobile-lab/README.md) |

The immediate milestone is one complete vertical slice:

```text
typed settings
    ↓
versioned API route
    ↓
register data source use case
    ↓
domain entity and repository port
    ↓
SQLAlchemy adapter and migration
    ↓
unit + contract + integration tests
```

## Vision and goals

Atlas has four simultaneous roles.

| Role | Meaning |
|---|---|
| Technical portfolio | Demonstrate applied engineering through reviewable evidence rather than skill lists. |
| Learning laboratory | Study concepts inside real modules and experiments rather than isolated snippets. |
| Modular platform | Reuse stable contracts across data, AI, automation, operations, and client applications. |
| Engineering narrative | Record how decisions, tradeoffs, quality, and system boundaries evolve over time. |

Project goals:

- build maintainable Python backend applications;
- connect data collection, ETL, statistics, ML, and reporting;
- study mathematical foundations through executable experiments;
- engineer RAG and agent workflows with evaluation and policy controls;
- automate operational and support routines safely;
- explore networks, messaging, concurrency, resilience, and observability;
- create mobile and edge clients with explicit offline and safety constraints;
- practice DDD, TDD, architecture, refactoring, and documentation pragmatically;
- publish demonstrations that explain assumptions and limitations honestly;
- design interfaces, workflows, and policies with psychological safety,
  transparency, fairness, and social awareness;
- study how perception, identity, habit, ethics, community, and narrative
  shape user behavior, trust, and wellbeing.

## Architecture

### Principles

1. Start with the simplest architecture that supports the current use case.
2. Keep domain rules independent from HTTP, SQLAlchemy, cloud SDKs, and UI frameworks.
3. Use explicit contracts at boundaries and replaceable adapters for external systems.
4. Add infrastructure in response to measured needs, not imagined future scale.
5. Prefer vertical slices over large horizontal foundations with no user-visible behavior.
6. Apply DDD and TDD when they improve language, feedback, and change safety.
7. Record cross-cutting or costly decisions through Architecture Decision Records.
8. Treat telemetry, security, privacy, rollback, and documentation as engineering work.
9. Design systems that respect autonomy, dignity, cultural context, and psychological safety.
10. Favor feedback loops that reduce confusion, support reflection, and encourage healthy user behavior.
11. Install dependencies by focused track instead of creating one universal environment.
12. Keep planned architecture clearly separate from implemented behavior.

### Current runtime

```text
Client
  ↓ HTTP
FastAPI app (`backend/app/main.py`)
  ↓
Synchronous route function
  ↓
Static JSON response

PostgreSQL container ← configured locally, not yet used by an endpoint
```

### Target modular flow

```text
Web / Mobile / Automation / Agent
                ↓
          Atlas API router
                ↓
        Application use case
                ↓
        Domain model and ports
                ↑
   SQL / queue / provider adapters
                ↓
 PostgreSQL / broker / cloud / model
```

The target flow is directional guidance. It is not permission to create every
layer before the first use case needs it.

### Boundary rules

- API modules translate transport concerns; they do not own business policy.
- Use cases coordinate one application intention and remain transport-neutral.
- Domain modules protect language and invariants without framework imports.
- Infrastructure implements ports and owns external I/O details.
- The composition root wires dependencies and process lifecycle.
- Cross-module communication uses documented contracts, not private internals.

## Repository map

```text
atlas/
├── analytics/                      # Reusable analytical code scaffold
├── apps/
│   └── mobile/                     # Atlas Pocket implementation scaffold
├── backend/
│   ├── app/
│   │   ├── api/                    # HTTP interface scaffold
│   │   ├── core/                   # Typed settings scaffold
│   │   ├── domain/                 # Domain model scaffold
│   │   ├── use_cases/              # Application use-case scaffold
│   │   ├── database.py             # SQLAlchemy development setup
│   │   └── main.py                 # Current FastAPI application
│   ├── tests/                      # Current API tests
│   ├── README.md                   # Backend operating and architecture guide
│   └── requirements.txt            # Pinned executable backend environment
├── docs/
│   ├── modules/                    # Concrete module documentation
│   ├── tracks/                     # 21 technical execution guides
│   └── README.md                   # Documentation hub
├── datasets/                       # Dataset governance scaffold
├── infra/                          # Infrastructure and runbook scaffold
├── notebooks/                      # Reproducible exploration scaffold
├── requirements/                   # 76 focused dependency sets
├── scrapers/                       # Responsible collection scaffold
├── scripts/
│   └── mobile/                     # Mobile automation scaffold
├── docker-compose.yml              # Local PostgreSQL service
├── LICENSE
├── README.md
└── README.pt-BR.md
```

Directories described in track roadmaps are planned and should be created only
when a real implementation needs them.

## Technical tracks

Atlas has 21 long-lived technical tracks. Each linked guide contains mission,
scope, deliverables, dependencies, integration points, quality evidence,
roadmap, and definition of done.

### Foundation and interfaces

- [Atlas Core](docs/tracks/core/README.md)
- [Atlas API](docs/tracks/api/README.md)
- [Legacy and Refactoring](docs/tracks/legacy-refactoring/README.md)

### Data, mathematics, and intelligence

- [Data Mining](docs/tracks/data-mining/README.md)
- [ETL and Data Engineering](docs/tracks/data-engineering/README.md)
- [Statistical Lab](docs/tracks/statistics/README.md)
- [Calculus and Numerical Methods](docs/tracks/numerical-methods/README.md)
- [Machine Learning](docs/tracks/machine-learning/README.md)
- [Deep Learning](docs/tracks/deep-learning/README.md)
- [AI Lab](docs/tracks/ai/README.md)
- [BI and Storytelling](docs/tracks/bi-storytelling/README.md)

### Operations and runtime systems

- [Automation](docs/tracks/automation/README.md)
- [Support](docs/tracks/support/README.md)
- [Networking](docs/tracks/networking/README.md)
- [Messaging and Real-Time](docs/tracks/messaging-real-time/README.md)
- [Cloud and DevOps](docs/tracks/cloud-devops/README.md)
- [Observability](docs/tracks/observability/README.md)
- [Systems](docs/tracks/systems/README.md)

### Devices and interactive applications

- [Mobile](docs/tracks/mobile/README.md)
- [Embedded, IoT, and Autonomous Systems](docs/tracks/embedded-iot-autonomous/README.md)
- [Games and Simulation](docs/tracks/games-simulation/README.md)

See the [complete tracks catalog](docs/tracks/README.md) for status definitions
and navigation.

## System modules

The module catalog documents concrete runtime units and product
specifications. Current module documentation includes:

- [Atlas backend](backend/README.md)
- [Backend application package](backend/app/README.md)
- [API interface](backend/app/api/README.md)
- [API routes](backend/app/api/routes/README.md)
- [Core configuration](backend/app/core/README.md)
- [Domain model](backend/app/domain/README.md)
- [Domain entities](backend/app/domain/entities/README.md)
- [Application use cases](backend/app/use_cases/README.md)
- [Backend tests](backend/tests/README.md)
- [Analytics](analytics/README.md)
- [Client applications](apps/README.md)
- [Atlas Pocket implementation](apps/mobile/README.md)
- [Datasets](datasets/README.md)
- [Infrastructure](infra/README.md)
- [Notebooks](notebooks/README.md)
- [Data collection](scrapers/README.md)
- [Operational scripts](scripts/README.md)
- [Mobile automation scripts](scripts/mobile/README.md)
- [Atlas Mobile Lab](docs/modules/mobile-lab/README.md)

The [modules catalog](docs/modules/README.md) distinguishes implemented modules,
partial scaffolds, and planned products.

## Dependency strategy

Atlas does not use one enormous experimental `requirements.txt`. The
[`requirements/`](requirements/README.md) directory contains focused,
unpinned sets for technical exploration, while
[`backend/requirements.txt`](backend/requirements.txt) pins the current backend
environment.

Install only the sets needed by the current task:

```bash
python -m pip install -r requirements/core.txt
python -m pip install -r requirements/dev.txt
```

Combine tracks explicitly when a module crosses domains:

```bash
python -m pip install \
  -r requirements/data.txt \
  -r requirements/statistics.txt \
  -r requirements/visualization.txt
```

Important constraints:

- track files are not lock files;
- experimental stacks may conflict and may need separate environments;
- native, cloud, device, or AI libraries may require external setup and cost;
- a listed dependency is not evidence that its feature is implemented;
- modules should document exactly which tracks they consume.

## Quick start

### Prerequisites

- Git;
- Python 3.11 or newer;
- Docker with Compose support;
- PowerShell, Bash, or an equivalent shell.

### 1. Clone and enter the repository

```bash
git clone https://github.com/caio-stat/atlas.git
cd atlas
```

### 2. Create and activate a virtual environment

PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Bash:

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install the backend environment

```bash
python -m pip install --upgrade pip
python -m pip install -r backend/requirements.txt
```

### 4. Start PostgreSQL

```bash
docker compose up -d postgres
docker compose ps
```

The Compose credentials are local-development defaults. Never reuse them in a
shared or production environment.

### 5. Run tests

```bash
cd backend
python -m pytest
```

### 6. Start the API

```bash
python -m uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000/docs` for the generated OpenAPI interface. See the
[backend guide](backend/README.md) for architecture, configuration limitations,
and next steps.

## API behavior

| Method | Path | Current response | Meaning |
|---|---|---|---|
| `GET` | `/` | `{"message":"Atlas conectado"}` | Basic process response |
| `GET` | `/health` | `{"status":"ok"}` | Process liveness only |
| `GET` | `/version` | `{"name":"Atlas API","version":"0.1.0"}` | Current API identity |

`/health` does not currently check PostgreSQL or other dependencies. A future
readiness endpoint should represent dependency availability separately.

## Development workflow

1. Choose one documented track and one small acceptance criterion.
2. Confirm the real repository state before designing abstractions.
3. Add or update tests for observable behavior.
4. Implement the smallest vertical slice that satisfies the criterion.
5. Keep domain rules separate from delivery and infrastructure details.
6. Run focused tests, then the relevant broader suite.
7. Update English and Portuguese documentation in the same change.
8. Record a decision in an ADR when it crosses boundaries or is costly to reverse.
9. Review security, privacy, failure behavior, and operational evidence.

Definition of done for a module change:

- clean setup instructions work;
- public contracts and errors are documented;
- tests are proportional to risk;
- no secrets or personal data are committed;
- planned and implemented behavior are distinguished;
- related track and module READMEs remain aligned.

## Testing and quality

The project uses pytest for the current backend checks. As the architecture
grows, quality should be layered:

| Layer | Purpose |
|---|---|
| Unit | Domain invariants, calculations, transformations, and use-case decisions |
| Contract | HTTP schemas, status codes, errors, events, files, and provider interfaces |
| Integration | PostgreSQL, migrations, queues, file systems, and controlled providers |
| End to end | A small number of critical user journeys across real module boundaries |
| Architecture | Dependency direction and forbidden framework imports |
| Operational | Health, readiness, telemetry, rollback, and recovery procedures |

Quality is not measured by coverage percentage alone. Tests should catch
meaningful regressions, remain deterministic, and explain failures. Data and AI
experiments additionally need versioned inputs, seeds, evaluation metrics,
baseline comparisons, and limitation notes.

## Documentation system

The [documentation hub](docs/README.md) defines document types, source-of-truth
rules, the bilingual policy, writing standards, and a review checklist.

Primary documentation is maintained in pairs:

- `README.md` — English;
- `README.pt-BR.md` — Brazilian Portuguese.

Both versions should have equivalent structure and technical meaning. Technical
names remain canonical, while explanations are localized. Planned work must be
labeled clearly, and implemented claims should link to code, tests, examples,
or operational evidence.

## Roadmap

### Phase 0 — Foundation

- stabilize backend setup and tests;
- complete typed configuration;
- extract versioned API routers;
- complete ADR 0001;
- implement the first domain vertical slice.

### Phase 1 — Data foundation

- register and catalog data sources;
- add migrations and repository adapters;
- collect one responsible public dataset;
- create a reproducible raw-to-processed pipeline;
- publish quality and lineage evidence.

### Phase 2 — Analytics and statistics

- define a metric dictionary;
- publish exploratory and inferential analyses;
- add regression, Bayesian, or time-series experiments;
- produce a reproducible report and dashboard.

### Phase 3 — Machine learning

- establish statistical and naive baselines;
- build one leak-resistant training pipeline;
- track experiments and produce a model card;
- expose approved inference through a stable adapter.

### Phase 4 — AI and documents

- ingest documents with provenance;
- build retrieval with citations;
- define an evaluation dataset;
- add policy-controlled tools and observable agent workflows.

### Phase 5 — Automation and operations

- add scheduled and event-triggered workflows;
- introduce structured logs, metrics, and correlation IDs;
- write runbooks for important failures;
- test retry, idempotency, rollback, and recovery.

### Phase 6 — Interfaces and edge

- create the first Atlas Pocket health screen;
- add offline-first behavior incrementally;
- prototype support, IoT, or interactive simulation clients;
- measure device, network, and resource constraints.

### Phase 7 — Selective distribution

- measure bottlenecks in the modular monolith;
- extract a worker or service only when justified;
- preserve contracts, observability, and rollback;
- document the decision and migration evidence.

## Responsible use

### Data and collection

- respect source terms, robots policies, rate limits, and applicable law;
- collect the minimum data necessary for the stated purpose;
- record provenance, timestamps, transformations, and deletion rules;
- never publish private, personal, or sensitive data as portfolio material.

### AI and automation

- identify model-generated output and preserve source traceability;
- evaluate retrieval and answers before relying on them;
- grant tools the least privilege necessary;
- require explicit approval for destructive or externally consequential actions;
- track cost, latency, fallback, and provider data-handling constraints.

### Support, network, and device tooling

- default diagnostics to read-only behavior;
- define target scope and authorization before scanning or remote access;
- separate evidence from inference and remediation;
- log changes and provide rollback where modification is allowed;
- treat physical-device and industrial actions as safety-sensitive.

### Security

- never commit secrets or production credentials;
- validate untrusted input at boundaries;
- redact logs and error messages;
- use least privilege and explicit timeouts;
- keep dependencies and deployment procedures reviewable.

## Portfolio evidence

Each completed Atlas slice should answer:

- What real problem was addressed?
- What constraints and tradeoffs shaped the design?
- Which contract separates it from other modules?
- How can another person run and verify it?
- Which tests, metrics, or comparisons support the result?
- What failed, changed, or remains limited?
- What would justify the next architectural step?

Strong evidence may include code, tests, diagrams, ADRs, dataset cards, model
cards, benchmark reports, screenshots, dashboards, runbooks, and short demos.
The goal is not maximum breadth; it is credible technical progression.

## License

Atlas is licensed under the [MIT License](LICENSE).

## Author

**Caio Costa Cavalcante**

Statistics student, data science learner, AI and Python developer, Android
developer, and support/helpdesk professional building Atlas as a long-term
technical portfolio.

GitHub: [caio-stat](https://github.com/caio-stat)
