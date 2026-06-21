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
- [Human experience and interaction](#human-experience-and-interaction)
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

## Human experience and interaction

Atlas should be technically rigorous and humanly inhabitable. Experience is not a cosmetic layer applied after backends, models, and automations are finished; it is a cross-cutting property of contracts, messages, response times, navigation patterns, documentation, data policies, help mechanisms, and opportunities for contestation. A correct system that produces avoidable anxiety, confusion, shame, a sense of surveillance, or loss of control is still incomplete.

The intended human outcome is for each person to feel **welcomed without being infantilized, guided without being controlled, stimulated without being overloaded, and respected without having to earn that respect**. Atlas should awaken curiosity, exploratory pleasure, calibrated trust, and a desire to keep interacting because the interaction delivers value, responds clearly, and recognizes user autonomy—never because it exploits compulsion, fear of loss, guilt, or vulnerability.

### Desired affective and cognitive qualities

- **Welcome:** the first interaction should communicate “you can start here.” Language, examples, and defaults should reduce threat, anticipate questions, and make it safe to admit a lack of knowledge.
- **Pleasantness:** legibility, rhythm, visual coherence, timely responses, restrained microinteractions, and humane messages should create comfort without concealing relevant complexity.
- **Curiosity:** the system should offer cues, examples, previews, useful questions, and progressive paths that invite exploration without turning discovery into a confusing search for features.
- **Competence:** each action should produce feedback that helps people understand what happened, why it happened, and what next step is possible. Users should perceive genuine growth in mastery.
- **Autonomy:** recommendations must remain recommendations. Alternatives, consequences, reversal, export, cancellation, and exit should remain visible and practical.
- **Belonging:** cultural, linguistic, cognitive, sensory, and technical differences should be treated as a normal part of the audience, not inconvenient exceptions.
- **Calibrated trust:** Atlas should acknowledge uncertainty, limitations, sources, failures, and the real implementation state. Emotional safety must not be confused with false certainty.
- **Reflective stimulation:** beyond completing tasks, the system may invite users to compare hypotheses, revisit decisions, understand tradeoffs, and perceive relationships among technology, society, and consequence.
- **Recovery:** errors should be reversible whenever possible. After failure, interruption, or overload, the system should provide a short path back while preserving context and completed work.

### Psychology applied to experience

Atlas may draw from a broad psychological repertoire, provided that each mechanism has an explicit purpose, proportionate evidence, and safeguards:

- **Behaviorism and learning:** reinforcement, modeling, shaping, immediate feedback, deliberate practice, active recall, spaced repetition, and habit formation can support learning and continuity. They must not create opaque variable rewards, punishment for absence, coercive streaks, or behavioral dependency.
- **Gestalt and perceptual psychology:** proximity, similarity, continuity, closure, common fate, and figure-ground should guide hierarchy, grouping, and focus. Contrast, salience, and movement should highlight relevance rather than hijack attention.
- **Cognitivism:** intrinsic, extraneous, and germane load; working memory; chunking; recognition over recall; mental models; dual coding; selective attention; and metacognition should ground information architecture. Complexity should be disclosed progressively without hiding consequences.
- **Constructivism and cultural-historical theory:** examples, scaffolding, the zone of proximal development, shared language, and situated learning should let beginners advance with support and experts remove that support without friction.
- **Humanism:** congruence, positive regard, listening, empathy, and the tendency toward actualization inspire messages that preserve dignity. An error belongs to the interaction and learning process; it is not a moral defect in the user.
- **Phenomenological and existential psychologies:** lived experience, ambiguity, responsibility, choice, and meaning-making matter as much as completion rates. The system should return agency rather than reduce a person to telemetry events.
- **Psychoanalyses and depth psychology:** desire, resistance, projection, repetition, idealization, shadow, fantasy, and defense mechanisms can support a critical reading of relationships between users and technology. They are interpretive and artistic lenses, never remote diagnoses.
- **Social psychology:** reciprocity, social proof, authority, conformity, comparison, group identity, stigma, the bystander effect, diffusion of responsibility, and stereotype threat help predict how interfaces shape conduct. These phenomena should be made legible, not silently exploited.
- **Self-determination theory:** autonomy, competence, and relatedness should sustain intrinsic motivation. Goals, indicators, and celebrations are healthy only when they help users recognize progress they themselves value.
- **Decision science:** framing, anchoring, availability, loss aversion, sunk costs, overconfidence, temporal discounting, and decision fatigue require safe defaults, honest comparisons, and comprehensible consequences.
- **Positive psychology and wellbeing:** curiosity, realistic hope, character strengths, gratitude, flow, and meaning can enrich the experience, provided that they do not become toxic positivity or conceal structural problems.
- **Ecological, embodied, enactive, and distributed approaches:** cognition occurs among body, tool, environment, and other people. Atlas should account for device, connectivity, interruptions, mobility, physical context, and collaboration, not only an abstract mind facing a perfect screen.
- **Neuropsychology and neuroergonomics:** fatigue, vigilance, task switching, inhibitory control, sensory processing, and attentional rhythms should constrain density, notifications, and sequence length. Neuroscientific terms must not be used as a veneer of authority.
- **Trauma-informed practices:** predictability, consent, choice, safety, collaboration, and the ability to pause reduce unnecessary reactivation. Sensitive content should have proportionate notices, intensity controls, and alternative paths.

Atlas does not diagnose personality, mental health, intent, morality, or cognitive ability from clicks, response time, or language. Behavioral inferences should be minimal, contestable, and connected to a clear purpose.

### Applied philosophy: from the pre-Socratics to contemporary schools

The experience should carry centuries of philosophical questions without becoming an ornamental encyclopedia. Traditions operate as lenses for concrete product decisions:

- From the **pre-Socratics**, Heraclitus inspires systems that make change and process intelligible; Parmenides demands clarity about identity and persistence; atomists, pluralists, and Pythagoreans invite thought about composition, measure, chance, necessity, and order.
- **Socratic** inquiry inspires questions that help without humiliating; Plato warns about appearance, representation, and the power of mediation; Aristotle offers habit, practical wisdom, causality, virtue, community, and flourishing as criteria for judging a good interaction.
- **Stoicism, Epicureanism, skepticism, and Cynicism** distinguish control from the uncontrollable, pleasure from excess, certainty from suspended judgment, and convention from authentic life. The system should reduce operational anxiety, communicate uncertainty, and avoid manufacturing desires that only it promises to satisfy.
- **Medieval, Jewish, and Islamic traditions** contribute debates about intention, responsibility, care, community, interpretation, and the limits of reason. **Buddhist, Hindu, Jain, Daoist, and Confucian schools** add impermanence, interdependence, nonviolence, attention, harmony, relational duty, and self-cultivation.
- **African, Afro-diasporic, and Indigenous American philosophies**, including Ubuntu and relational perspectives, challenge the isolated individual as the universal unit of design and emphasize reciprocity, ancestry, territory, community, and a plurality of worlds.
- **Rationalism** demands consistency and explainability; **empiricism** requires observation and testing; Hume reminds us of the roles of habit and affect; **social-contract theory** asks which rules could be accepted; Kant demands autonomy, dignity, and people treated as ends rather than means.
- **Utilitarianism, virtue ethics, deontology, pragmatism, and care ethics** offer criteria that may diverge: aggregate consequences, character, duty, practical effects, and relational responsibility. UX decisions should record which criterion they prioritize and who bears the cost.
- **Hegel, Marx, and critical traditions** show that recognition, labor, alienation, ideology, class, and structure shape experience. An “efficient” workflow may merely shift labor, obscure exploitation, or adapt users to an unjust condition.
- **Phenomenology, hermeneutics, and existentialism** place body, temporality, situation, interpretation, freedom, anxiety, and meaning at the center. Metrics do not replace descriptions of lived experience.
- **Nietzsche, genealogy, and psychoanalysis** invite us to ask what values, desires, and relations of force an interface produces—not only whether users click it.
- **Analytic philosophy, philosophy of language, and pragmatics** demand precise concepts, honest speech acts, messages without accidental ambiguity, and distinctions among assertion, recommendation, prediction, and command.
- **Critical theory, structuralism, post-structuralism, and deconstruction** help reveal ideology, discipline, normalization, binaries, silences, and exclusions inscribed in categories, forms, and algorithms.
- **Feminisms, care ethics, queer theory, critical race studies, postcolonialism, and decolonial thought** require presumed universality, neutrality, and the “default” user to be continually examined.
- **Philosophies of technology, information, and mind**, posthumanism, transhumanism, new materialism, environmental ethics, and AI ethics extend the questions to distributed agency, automation, surveillance, technical dependency, sustainability, and coexistence between humans and intelligent systems.

The goal is not to declare one school the winner. Atlas should make tensions visible: efficiency versus care, personalization versus privacy, smoothness versus deliberation, autonomy versus protection, individual freedom versus collective consequence, and simple explanation versus fidelity to complexity.

### Sociology applied to experience

Users do not enter the system as abstract individuals. They arrive shaped by class, race, gender, generation, territory, language, education, disability, profession, institutions, and histories of technological trust or exclusion.

- Comte, Marx, Durkheim, Weber, and Simmel offer problems of order, conflict, solidarity, anomie, rationalization, bureaucracy, authority, and metropolitan life.
- Symbolic interactionism, social dramaturgy, social phenomenology, and ethnomethodology show how identity, normality, and meaning are negotiated in small encounters—including fields, messages, and permission prompts.
- Goffman helps examine presentation of self, stigma, face, and institutions; labeling and self-fulfilling prophecy warn against categories that begin producing the behavior they claim merely to describe.
- The Frankfurt School, Gramsci, Habermas, and cultural studies interrogate the culture industry, hegemony, the public sphere, instrumental rationality, and communication.
- Foucault makes discipline, surveillance, examination, normalization, governmentality, and biopolitics visible; Bourdieu adds habitus, field, and economic, cultural, social, and symbolic capital.
- Feminisms and intersectionality show that power and disadvantage operate simultaneously; studies of race, disability, coloniality, and subalternity reveal costs hidden by aggregate averages.
- Systems theory, actor-network theory, and science and technology studies treat documents, models, APIs, metrics, and devices as participants that reorganize action and responsibility.
- Contemporary sociology contributes network society, platform capitalism, datafication, invisible labor, precarity, the attention economy, epistemic bubbles, disinformation, liquid modernity, risk society, social acceleration, and the Anthropocene.

Applying sociology means asking: who can enter, who understands the language, who appears in the data, who is misclassified, who performs additional labor, who can contest a decision, who receives the benefit, and who absorbs the risk. Global metrics should be examinable by context without creating surveillance or exposure for vulnerable groups.

### Concrete interaction contract

| Moment | Desired experience | System requirement |
|---|---|---|
| First contact | Safety and curiosity | Clear value proposition, immediate example, inclusive language, and a start without unnecessary configuration |
| Onboarding | Orientation with autonomy | Progressive disclosure, ability to skip and resume, and a choice of help level |
| Data entry | Trust | Explained purpose, minimal collection, validation near the field, and preservation of completed input |
| Waiting | Predictability | Visible state, honest estimate when possible, cancellation, and no animation that simulates false progress |
| Success | Competence | Specific confirmation, verifiable result, and an optional next step without disproportionate celebration |
| Error | Recovery without shame | Non-accusatory language, comprehensible cause, preserved data, actionable correction, and a support identifier |
| AI recommendation | Calibrated trust | Sources, uncertainty, alternatives, distinction between fact and inference, and the ability to reject or edit |
| Sensitive action | Deliberation | Consequences before confirmation, explicit scope, meaningful approval, idempotency, and rollback when possible |
| Return to the system | Continuity | Restored context, summary of changes, and no punishment for time away |
| Exit | Respect | Simple cancellation, comprehensible export and deletion, and no guilt, obstruction, or surprise loss |

### Ethical persuasion, welcome, and boundaries

Every interface influences: it organizes options, sets defaults, distributes attention, and frames consequences. Atlas may use encouraging microcopy, visible progress, user-chosen goals, configurable reminders, local personalization, relevant examples, and adaptive feedback to stimulate interaction. Influence, however, should expand competence and future freedom. A good stimulus makes users less dependent on the system to understand what they are doing.

The following are incompatible with the project: dark patterns; false urgency; guilt for absence; visually hidden refusal options; presumed consent; insistent notifications; random rewards aimed at compulsion; anthropomorphism that simulates emotional attachment to obtain data or payment; artificial difficulty designed to sell relief; vanity metrics used as pressure; personalization based on emotional fragility; and interfaces that deliberately blur recommendation, advertising, and obligation.

Welcome also requires boundaries. The system must not pretend to possess emotions, consciousness, friendship, clinical authority, or certainty it does not have. It can be warm, attentive, and pleasant without deceiving users about its nature. When medical, legal, financial, psychological, or physical risk is present, the experience should slow down, state limitations, and route toward qualified human judgment.

### Evaluation and experience evidence

Success will not be measured only through retention, frequency, screen time, or click volume. Those numbers may indicate value, confusion, obligation, or dependency and require interpretation. Each significant flow should combine:

- effectiveness: completion, correctness, reversibility, and time to value;
- cognitive efficiency: perceived load, errors, backtracking, abandonment, and need for help;
- affective quality: safety, comfort, curiosity, calibrated trust, and sense of competence;
- autonomy: understanding of options, reversal rate, ease of refusal, export, and exit;
- accessibility and fairness: performance with assistive technologies, different devices, languages, experience levels, and connectivity conditions;
- trust: understanding of sources, uncertainty, data purpose, and automation limits;
- longitudinal wellbeing: absence of compulsive pressure, avoidable fatigue, guilt, dependency, and excessive notifications;
- qualitative evidence: interviews, contextual observation, usability tests, incident reports, and language analysis without reducing human experience to a single score.

Every persuasive, adaptive, or emotionally intense feature should document its hypothesis, expected human benefit, affected groups, risk, safeguard, metric, contestation mechanism, and stopping condition. The final criterion is that people finish the interaction more capable, oriented, and free than when they began.

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
