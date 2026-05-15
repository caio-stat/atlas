# Atlas

<p align="center">
  <strong>A modular laboratory for Data, AI, Statistics and Software Engineering.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-blue" alt="Python">
  <img src="https://img.shields.io/badge/FastAPI-Backend-009688" alt="FastAPI">
  <img src="https://img.shields.io/badge/PostgreSQL-Database-336791" alt="PostgreSQL">
  <img src="https://img.shields.io/badge/Docker-Containers-2496ED" alt="Docker">
  <img src="https://img.shields.io/badge/Status-Early%20Foundation-yellow" alt="Project Status">
  <img src="https://img.shields.io/badge/License-MIT-green" alt="License">
</p>

<p align="center">
  🌎 Language: English | <a href="README.pt-BR.md">Português</a>
</p>

---

## Overview

**Atlas** is a long-term technical portfolio project designed to evolve as a modular ecosystem for data engineering, statistical computing, machine learning, deep learning, generative AI, automation, web/mobile development and software architecture.

The goal of this project is not to become a random collection of tutorials, loose scripts or abandoned experiments on GitHub, that sacred landfill of unfinished enthusiasm. Atlas is being built as a real learning laboratory where each module demonstrates a professional engineering skill through code, documentation, tests and practical use cases.

Atlas starts as a **modular monolith** and may evolve into distributed services only when there is a clear technical reason to do so.

---

## Project Goals

Atlas aims to integrate and demonstrate knowledge in:

- Python backend development
- Object-Oriented Programming in Python
- FastAPI and REST API design
- PostgreSQL and SQL
- Data collection, web scraping and ETL
- Data engineering and analytical pipelines
- Statistics, probability, inference and regression
- Machine learning and model experimentation
- Deep learning with neural networks, embeddings, computer vision, NLP and Transformers
- Generative AI, RAG and intelligent agents
- Workflow automation with tools such as n8n
- Dashboards, data visualization and storytelling with React
- Android development with Kotlin and offline-first applications
- Docker, CI/CD, cloud deployment and observability
- Linux, networking, concurrency and distributed systems
- Software architecture, DDD, TDD and Design Patterns

---

## Current Status

Atlas is in its **early foundation stage**.

Current repository structure:

```text
atlas/
├── backend/
├── docker-compose.yml
├── LICENSE
└── README.md
```

Current focus:

- Establish the backend foundation
- Keep the repository clean and understandable
- Document the long-term architectural vision
- Evolve incrementally instead of overengineering too early

Next immediate milestone:

```text
Atlas Core + Health API
```

This first milestone should include:

- Initial FastAPI structure
- `/health` endpoint
- `/version` endpoint
- PostgreSQL connection
- Basic modular organization
- First domain entity
- First use case
- Initial tests with pytest
- First Architecture Decision Record, or ADR

---

## Architectural Philosophy

Atlas follows a pragmatic architecture strategy:

1. **Start simple**, with a modular monolith.
2. **Keep clear boundaries** between domain, application, infrastructure and interfaces.
3. **Use DDD pragmatically**, without turning the project into a ceremonial abstraction festival.
4. **Apply TDD when it brings clarity and safety**.
5. **Document relevant decisions** through ADRs.
6. **Extract services later** only when there is a real need for scaling, independent deployment or technology isolation.

The initial architectural direction is inspired by:

- Modular Monolith
- Clean Architecture
- Hexagonal Architecture
- Domain-Driven Design
- Test-Driven Development
- Event-driven thinking, when useful

---

## Planned High-Level Structure

The repository may evolve toward the following organization:

```text
atlas/
├── apps/
│   ├── web/                    # React dashboards and portfolio interface
│   ├── mobile/                 # Kotlin Android app, offline-first
│   └── desktop/                # Future desktop experiments
│
├── services/
│   ├── atlas_api/              # Main FastAPI application
│   ├── atlas_worker/           # Workers and background tasks
│   ├── atlas_ai/               # RAG, agents and LLM integrations
│   ├── atlas_scraper/          # Web scraping and data collection
│   ├── atlas_stats/            # Statistics, probability and regression
│   └── atlas_automation/       # n8n, WhatsApp and social automation
│
├── packages/
│   ├── atlas_core/             # Entities, value objects and use cases
│   ├── atlas_shared/           # Shared schemas, DTOs and utilities
│   └── atlas_plugins/          # Pluggable providers and integrations
│
├── data/
│   ├── raw/
│   ├── processed/
│   ├── warehouse/
│   └── samples/
│
├── notebooks/
│   ├── statistics/
│   ├── machine_learning/
│   ├── deep_learning/
│   ├── calculus/
│   └── experiments/
│
├── infra/
│   ├── docker/
│   ├── postgres/
│   ├── monitoring/
│   └── github_actions/
│
├── docs/
│   ├── architecture/
│   ├── adr/
│   ├── roadmap/
│   ├── modules/
│   └── portfolio/
│
├── tests/
│   ├── unit/
│   ├── integration/
│   ├── e2e/
│   └── load/
│
├── docker-compose.yml
├── pyproject.toml
├── README.md
└── LICENSE
```

This structure represents a planned direction, not a promise that all directories already exist today.

---

## Main Modules

### Atlas Core

The domain foundation of the system.

Planned responsibilities:

- Entities
- Value objects
- Use cases
- Repository interfaces
- Domain events
- Business rules
- Pure Python logic

Examples of future entities:

- `DataSource`
- `Dataset`
- `Pipeline`
- `PipelineRun`
- `Experiment`
- `ModelRun`
- `StatisticalTest`
- `Agent`
- `Workflow`
- `Report`

---

### Atlas API

The HTTP layer of the project.

Planned responsibilities:

- FastAPI routes
- Request and response schemas
- Dependency injection
- Authentication experiments
- Automatic API documentation
- Integration with domain use cases

Initial endpoints:

```text
GET /health
GET /version
```

---

### Atlas Data Mining

Responsible for data collection and web intelligence.

Planned topics:

- Web scraping
- API-based data collection
- Asynchronous scraping
- HTML parsing
- Browser automation
- Monitoring page changes
- Responsible scraping practices
- Public data collection

Possible use cases:

- Public job and civil service exam monitoring
- Government datasets
- News intelligence
- Technology trend radar
- Social media intelligence

---

### Atlas ETL

Responsible for transforming raw data into usable data.

Planned topics:

- Extraction
- Cleaning
- Validation
- Transformation
- Loading into PostgreSQL
- Data quality checks
- Incremental loads
- Pipeline logs
- Data versioning experiments

General flow:

```text
External Source
    ↓
Extractor
    ↓
Raw Data
    ↓
Validator
    ↓
Transformer
    ↓
PostgreSQL / DuckDB
    ↓
Analytics / ML / RAG
    ↓
API / Dashboard / Report
```

---

### Atlas Statistical Lab

A module focused on connecting academic statistics with real software.

Planned topics:

- Descriptive statistics
- Probability distributions
- Sampling
- Monte Carlo simulation
- Bootstrap
- Confidence intervals
- Hypothesis testing
- Linear regression
- Regression diagnostics
- Time series experiments
- Numerical methods
- Calculus foundations applied to optimization

The goal is to implement statistical concepts in Python before hiding everything behind high-level libraries.

---

### Atlas Machine Learning Lab

A module for classical machine learning and supervised/unsupervised experimentation.

Planned topics:

- Linear regression
- Logistic regression
- KNN
- Decision trees
- Random Forest
- Gradient Boosting
- Clustering
- PCA
- Cross-validation
- Evaluation metrics
- Feature engineering
- Reproducible experiments
- Comparison between manual implementations and established libraries

---

### Atlas Deep Learning Lab

A module dedicated to the study and implementation of deep neural networks, connecting mathematical foundations, statistics, optimization and modern AI applications.

Planned topics:

- Artificial neural networks from scratch
- Perceptron and multilayer perceptron, or MLP
- Activation functions
- Loss functions
- Gradient descent
- Backpropagation
- Regularization
- Dropout
- Batch normalization
- Optimizers such as SGD, RMSProp and Adam
- Convolutional Neural Networks, or CNNs
- Recurrent Neural Networks, LSTM and GRU
- Autoencoders
- Embeddings
- NLP models
- Attention mechanism
- Transformers
- Fine-tuning pre-trained models
- PyTorch experiments
- Future experiments with TensorFlow and Keras

Possible applications:

- Text classification
- Sentiment analysis
- Image classification
- Pattern detection in time series
- Embeddings for semantic search
- Comparison between classical models and neural models

This module should avoid treating neural networks as black boxes. The idea is to first study the foundations, implement simple versions and only then use modern frameworks with more technical awareness and less religious devotion to `fit()`.

---

### Atlas AI Lab

A module for generative AI and agent-based systems.

Planned topics:

- LLM integrations
- Ollama for local models
- Replicate and cloud-based models
- Embeddings
- RAG pipelines
- Vector search
- AI agents
- Multi-agent workflows
- Prompt evaluation
- Guardrails
- Tool calling
- Model fallback strategies

Possible future flow:

```text
User
 ↓
Chat / API / WhatsApp
 ↓
Agent Router
 ↓
Retriever
 ↓
Tool Executor
 ↓
LLM Provider
 ↓
Response Validator
 ↓
Answer + Logs + Metrics
```

---

### Atlas Automation

A module for workflow automation and external integrations.

Planned topics:

- n8n workflows
- Email alerts
- WhatsApp integration
- Social media automation
- Automated reports
- Scheduled tasks
- Event-based workflows

Example flow:

```text
New data collected
    ↓
Pipeline processes data
    ↓
AI summarizes findings
    ↓
Statistical module validates patterns
    ↓
Dashboard is updated
    ↓
Automation sends report or alert
```

---

### Atlas Web

A future React interface for dashboards, storytelling and portfolio presentation.

Planned features:

- Landing page
- Interactive project map
- Data dashboards
- Statistical visualizations
- Pipeline monitoring
- Experiment history
- RAG playground
- Gamified learning interface

---

### Atlas Mobile

A future Android application built with Kotlin.

Planned features:

- Offline-first access
- Local cache with Room/SQLite
- API synchronization
- Notifications
- Simplified dashboards
- Chatbot access
- Mobile data collection experiments

---

### Atlas Infrastructure

The operational foundation of the project.

Planned topics:

- Docker
- Docker Compose
- PostgreSQL
- Redis experiments
- GitHub Actions
- Cloud deployment
- Logs
- Health checks
- Monitoring
- Backups
- Zero-downtime deployment experiments

---

### Atlas Systems Lab

A module for lower-level systems knowledge.

Planned topics:

- Linux fundamentals
- Processes and threads
- Asynchronous programming
- Sockets
- TCP/UDP experiments
- P2P communication
- Cryptography basics
- Concurrency issues
- Fault tolerance
- Load testing

---

### Atlas Legacy Lab

A future module for practicing maintenance and modernization of legacy systems.

Planned topics:

- Messy legacy scripts
- Characterization tests
- Refactoring
- Adapters
- Strangler Fig Pattern
- Technical debt documentation

This module exists because real software rarely arrives clean, documented and emotionally available.

---

## Technology Stack

### Current / Initial

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy or SQLModel
- Pydantic
- Docker
- Docker Compose
- pytest
- Git and GitHub

### Planned / Experimental

- Pandas
- NumPy
- scikit-learn
- PyTorch
- TensorFlow / Keras
- DuckDB
- Redis
- React
- TypeScript
- Kotlin Android
- Room / SQLite
- n8n
- LangChain / LangGraph
- Flowise
- Ollama
- Replicate
- PGVector or another vector database
- Grafana / Prometheus
- GitHub Actions

---

## Roadmap

### Phase 0: Foundation

- [ ] Organize the backend structure
- [ ] Create `/health` endpoint
- [ ] Create `/version` endpoint
- [ ] Connect FastAPI to PostgreSQL
- [ ] Add basic tests
- [ ] Add initial documentation
- [ ] Create the first ADR

### Phase 1: Atlas Core

- [ ] Create domain entities
- [ ] Create use cases
- [ ] Create repository interfaces
- [ ] Add unit tests
- [ ] Document domain decisions

### Phase 2: Data Mining and ETL

- [ ] Create the first data source
- [ ] Build the first scraper
- [ ] Store raw data
- [ ] Validate collected data
- [ ] Transform and load data into PostgreSQL
- [ ] Expose data through the API

### Phase 3: Statistical Lab

- [ ] Add a descriptive statistics module
- [ ] Add probability simulations
- [ ] Add sampling experiments
- [ ] Add confidence interval examples
- [ ] Add hypothesis testing examples
- [ ] Add regression experiments

### Phase 4: Machine Learning

- [ ] Add initial ML experiments
- [ ] Add model evaluation metrics
- [ ] Add simple reproducible experiment tracking
- [ ] Compare manual implementations with library-based models

### Phase 5: Deep Learning

- [ ] Implement a simple neural network from scratch
- [ ] Implement gradient descent and backpropagation in a didactic example
- [ ] Create an MLP experiment with PyTorch
- [ ] Create a text classification experiment
- [ ] Create an initial embeddings experiment
- [ ] Compare a classical model with a neural network on the same problem

### Phase 6: AI Lab

- [ ] Add embeddings
- [ ] Create a RAG prototype
- [ ] Integrate a local model with Ollama
- [ ] Add agent-based tools
- [ ] Add response evaluation and logging

### Phase 7: Web and Storytelling

- [ ] Build a React dashboard
- [ ] Add visual reports
- [ ] Create a visual portfolio map
- [ ] Add statistical visualizations

### Phase 8: Automation

- [ ] Add n8n workflows
- [ ] Add alerts
- [ ] Automate reports
- [ ] Create WhatsApp or email integration experiments

### Phase 9: Infrastructure and Resilience

- [ ] Add a CI/CD pipeline
- [ ] Create a deployment environment
- [ ] Add monitoring
- [ ] Add load tests
- [ ] Add chaos engineering experiments

---

## Running Locally

This section will expand as the project foundation is implemented.

Expected future flow:

```bash
git clone https://github.com/caio-stat/atlas.git
cd atlas

docker compose up -d
```

Future backend command:

```bash
cd backend
uvicorn main:app --reload
```

Future test command:

```bash
pytest
```

---

## Learning Strategy

Atlas is designed to grow through small, documented cycles.

Each cycle should produce:

- Working code
- Tests
- Documentation
- A clear architectural decision
- A portfolio-ready explanation
- A connection with data, statistics, AI or software engineering

The project should not try to become complete all at once. It should evolve like real software: incrementally, with some inevitable suffering and fewer illusions each week.

---

## Portfolio Value

Atlas is intended to demonstrate the ability to:

- Design modular systems
- Build APIs
- Work with databases
- Collect and process data
- Apply statistics to real problems
- Build machine learning experiments
- Study and implement deep learning models
- Use generative AI responsibly
- Automate workflows
- Document technical decisions
- Think about scalability, resilience and maintainability

---

## License

This project is licensed under the MIT License.

---

## Author

Developed by **Caio Costa Cavalcante** as a long-term technical portfolio and learning laboratory in Data, AI, Statistics and Software Engineering.

