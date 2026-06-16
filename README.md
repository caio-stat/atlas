# Atlas

<p align="center">
  <strong>A modular laboratory for Data, AI, Statistics, Automation, Infrastructure and Software Engineering.</strong>
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

**Atlas** is a long-term technical portfolio and learning laboratory designed to evolve as a modular ecosystem for:

* software engineering
* data engineering
* statistics
* machine learning
* deep learning
* generative AI
* automation
* support tooling
* networking
* cloud computing
* distributed systems
* web and mobile applications

The goal is not to build isolated tutorials or disconnected scripts. Atlas is being built as a real, incremental and documented ecosystem where each module demonstrates a professional skill through code, tests, architecture decisions and practical use cases.

Atlas starts as a **modular monolith** and may evolve into distributed services only when there is a clear technical reason to do so.

---

## Current Status

Atlas is in its **early foundation stage**.

The repository currently contains the initial project foundation and a growing `requirements/` directory that maps the main learning and experimentation tracks of the project.

Current focus:

* keep the repository organized and understandable
* document the long-term architectural vision
* build the backend foundation incrementally
* avoid overengineering too early
* separate dependencies by technical domain
* transform studies into portfolio-ready modules

Next immediate milestone:

```text
Atlas Core + Health API
```

This first milestone should include:

* initial FastAPI structure
* `/health` endpoint
* `/version` endpoint
* PostgreSQL connection
* basic modular organization
* first domain entity
* first use case
* initial tests with `pytest`
* first Architecture Decision Record, or ADR

---

## Project Goals

Atlas aims to integrate and demonstrate knowledge in:

* Python backend development
* Object-Oriented Programming in Python
* FastAPI and REST API design
* PostgreSQL and SQL
* data collection, web scraping and ETL
* OCR and Document Intelligence
* data engineering and analytical pipelines
* statistics, probability, inference, regression and Bayesian modeling
* numerical methods, optimization and simulation
* machine learning and experiment tracking
* deep learning with neural networks, embeddings, computer vision, NLP and Transformers
* generative AI, RAG and intelligent agents
* workflow automation with tools such as n8n
* support/helpdesk automation and diagnostic scripts
* networking, sockets and infrastructure diagnostics
* messaging, queues and asynchronous processing
* cloud computing, DevOps and observability
* geospatial analysis, epidemiology-oriented data work and public datasets
* dashboards, data visualization and storytelling
* Android development with Kotlin and offline-first applications
* Linux, security, concurrency and distributed systems
* software architecture, DDD, TDD and Design Patterns

---

## Architectural Philosophy

Atlas follows a pragmatic architecture strategy:

1. **Start simple**, with a modular monolith.
2. **Keep clear boundaries** between domain, application, infrastructure and interfaces.
3. **Use DDD pragmatically**, without turning the project into ceremonial abstraction.
4. **Apply TDD when it brings clarity and safety**.
5. **Document relevant decisions** through ADRs.
6. **Split modules into services later** only when there is a real need for scaling, independent deployment or technology isolation.
7. **Install dependencies by track**, not all at once.

The initial architectural direction is inspired by:

* Modular Monolith
* Clean Architecture
* Hexagonal Architecture
* Domain-Driven Design
* Test-Driven Development
* Event-driven architecture, when useful
* Data-oriented architecture, when useful

---

## Planned High-Level Structure

The repository may evolve toward the following organization:

```text
atlas/
├── apps/
│   ├── web/                         # React dashboards and portfolio interface
│   ├── mobile/                      # Kotlin Android app, offline-first
│   └── desktop/                     # Future desktop experiments
│
├── services/
│   ├── atlas_api/                   # Main FastAPI application
│   ├── atlas_worker/                # Workers and background tasks
│   ├── atlas_ai/                    # RAG, agents and LLM integrations
│   ├── atlas_scraper/               # Web scraping and data collection
│   ├── atlas_stats/                 # Statistics, probability and regression
│   ├── atlas_support/               # Support/helpdesk diagnostics
│   ├── atlas_networking/            # Networking experiments and diagnostics
│   └── atlas_automation/            # n8n, WhatsApp, reports and workflows
│
├── packages/
│   ├── atlas_core/                  # Entities, value objects and use cases
│   ├── atlas_shared/                # Shared schemas, DTOs and utilities
│   └── atlas_plugins/               # Pluggable providers and integrations
│
├── requirements/
│   ├── core.txt
│   ├── dev.txt
│   ├── data.txt
│   ├── statistics.txt
│   ├── ml.txt
│   ├── deep_learning.txt
│   ├── generative_ai.txt
│   ├── scraping.txt
│   ├── ocr.txt
│   ├── document_intelligence.txt
│   ├── support.txt
│   ├── networking.txt
│   ├── cloud.txt
│   ├── messaging.txt
│   └── ...
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

## Requirements Tracks

The `requirements/` directory is organized by technical domain. This avoids installing a huge and fragile environment before each module actually needs it.

| File                                     | Purpose                                                                  |
| ---------------------------------------- | ------------------------------------------------------------------------ |
| `requirements/core.txt`                  | Core data tools: arrays, dataframes, tables and local analytical storage |
| `requirements/dev.txt`                   | Developer tools for formatting, linting, tests and local quality checks  |
| `requirements/data.txt`                  | General data analysis and manipulation                                   |
| `requirements/visualization.txt`         | Charts, dashboards and storytelling                                      |
| `requirements/statistics.txt`            | Descriptive statistics, inference and statistical modeling               |
| `requirements/bayesian.txt`              | Bayesian modeling and probabilistic programming                          |
| `requirements/ml.txt`                    | Classical machine learning                                               |
| `requirements/deep_learning.txt`         | Neural networks and deep learning frameworks                             |
| `requirements/nlp.txt`                   | Natural language processing                                              |
| `requirements/computer_vision.txt`       | Image processing and computer vision                                     |
| `requirements/generative_ai.txt`         | LLMs, embeddings and generative AI workflows                             |
| `requirements/ai.txt`                    | General AI utilities and integrations                                    |
| `requirements/agents.txt`                | Agentic workflows and multi-agent experiments                            |
| `requirements/scraping.txt`              | Web scraping, crawling and browser automation                            |
| `requirements/ocr.txt`                   | OCR for images and scanned documents                                     |
| `requirements/document_intelligence.txt` | PDF parsing, document layout and structured extraction                   |
| `requirements/data_engineering.txt`      | SQL, ORM, migrations and data pipelines                                  |
| `requirements/big_data.txt`              | Big data and distributed data processing experiments                     |
| `requirements/mlops.txt`                 | Model tracking, deployment and ML lifecycle                              |
| `requirements/time_series.txt`           | Time series analysis and forecasting                                     |
| `requirements/geospatial.txt`            | Maps, geospatial data and location intelligence                          |
| `requirements/optimization.txt`          | Operations research and mathematical optimization                        |
| `requirements/simulation.txt`            | Discrete-event simulation and stochastic experiments                     |
| `requirements/automation.txt`            | Workflow automation and task orchestration                               |
| `requirements/support.txt`               | Support/helpdesk automation and machine diagnostics                      |
| `requirements/networking.txt`            | Network diagnostics, DNS, SSH, sockets and scanning                      |
| `requirements/cloud.txt`                 | AWS, Google Cloud and Azure SDK experiments                              |
| `requirements/devops.txt`                | Infrastructure automation and deployment tooling                         |
| `requirements/observability.txt`         | Logging, metrics, traces and monitoring                                  |
| `requirements/messaging.txt`             | Queues, workers and asynchronous processing                              |
| `requirements/distributed_system.txt`    | Distributed systems and service coordination experiments                 |
| `requirements/iot.txt`                   | IoT and hardware communication experiments                               |
| `requirements/security.txt`              | Cryptography, authentication and security utilities                      |

Recommended usage:

```bash
# Start with the minimal/base track
pip install -r requirements/core.txt
pip install -r requirements/dev.txt

# Add only the track you are currently studying
pip install -r requirements/statistics.txt
pip install -r requirements/scraping.txt
pip install -r requirements/support.txt
```

Some tracks may require external system dependencies. For example, OCR, browser automation, geospatial libraries and deep learning frameworks can require additional operating system packages, drivers or model downloads.

---

## Main Modules

### Atlas Core

The domain foundation of the system.

Planned responsibilities:

* entities
* value objects
* use cases
* repository interfaces
* domain events
* business rules
* pure Python logic

Examples of future entities:

* `DataSource`
* `Dataset`
* `Pipeline`
* `PipelineRun`
* `Experiment`
* `ModelRun`
* `StatisticalTest`
* `Agent`
* `Workflow`
* `Report`
* `SupportCheck`
* `NetworkProbe`

---

### Atlas API

The HTTP layer of the project.

Planned responsibilities:

* FastAPI routes
* request and response schemas
* dependency injection
* authentication experiments
* automatic API documentation
* integration with domain use cases

Initial endpoints:

```text
GET /health
GET /version
```

---

### Atlas Data Mining

Responsible for data collection and web intelligence.

This area includes:

* **Atlas Web Scraping Lab**
* **Atlas OCR Lab**
* **Atlas Document Intelligence Lab**

Planned topics:

* API-based data collection
* HTML parsing
* asynchronous scraping
* browser automation
* responsible scraping practices
* OCR for scanned documents
* PDF extraction and layout analysis
* document chunking for RAG
* public data collection

Possible use cases:

* public job and civil service exam monitoring
* government datasets
* DATASUS and public health data
* UFBA and academic information
* public reports, decrees, notices and PDFs
* technology trend radar

---

### Atlas ETL and Data Engineering

Responsible for transforming raw data into usable data.

Planned topics:

* extraction
* cleaning
* validation
* transformation
* loading into PostgreSQL
* data quality checks
* incremental loads
* pipeline logs
* data versioning experiments
* analytical storage with DuckDB
* ORM and migrations with SQLAlchemy, SQLModel and Alembic

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

* descriptive statistics
* probability distributions
* sampling
* Monte Carlo simulation
* bootstrap
* confidence intervals
* hypothesis testing
* linear regression
* regression diagnostics
* Bayesian modeling
* time series experiments
* numerical methods
* calculus foundations applied to optimization

The goal is to implement statistical concepts in Python before hiding everything behind high-level libraries.

---

### Atlas Machine Learning Lab

A module for classical machine learning and supervised/unsupervised experimentation.

Planned topics:

* linear regression
* logistic regression
* KNN
* decision trees
* Random Forest
* Gradient Boosting
* clustering
* PCA
* cross-validation
* evaluation metrics
* feature engineering
* reproducible experiments
* comparison between manual implementations and established libraries

---

### Atlas Deep Learning Lab

A module dedicated to the study and implementation of deep neural networks, connecting mathematical foundations, statistics, optimization and modern AI applications.

Planned topics:

* artificial neural networks from scratch
* perceptron and multilayer perceptron, or MLP
* activation functions
* loss functions
* gradient descent
* backpropagation
* regularization
* dropout
* batch normalization
* optimizers such as SGD, RMSProp and Adam
* Convolutional Neural Networks, or CNNs
* Recurrent Neural Networks, LSTM and GRU
* autoencoders
* embeddings
* NLP models
* attention mechanism
* Transformers
* fine-tuning pre-trained models
* PyTorch experiments
* TensorFlow and Keras experiments

This module should avoid treating neural networks as black boxes. The idea is to first study the foundations, implement simple versions and only then use modern frameworks with more technical awareness.

---

### Atlas AI Lab

A module for generative AI, RAG and agent-based systems.

Planned topics:

* LLM integrations
* Ollama for local models
* Replicate and cloud-based models
* embeddings
* vector search
* RAG pipelines
* AI agents
* multi-agent workflows
* prompt evaluation
* guardrails
* tool calling
* memory experiments
* model fallback strategies

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

### Atlas Automation Lab

A module for workflow automation and external integrations.

Planned topics:

* n8n workflows
* scheduled tasks
* event-based workflows
* email alerts
* WhatsApp integration
* social media automation
* automated reports
* portfolio automation
* academic automation

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

### Atlas Support Lab

A module inspired by real support/helpdesk work.

Planned topics:

* machine diagnostics
* CPU, RAM and disk reports
* process and service inspection
* Windows automation experiments
* WMI-based inventory
* support reports in Markdown or HTML
* portable diagnostic scripts
* health checks for workstations

Possible use cases:

* generate a local machine diagnostic report
* check CPU, RAM, disk and network information
* create a support checklist for Windows machines
* collect basic inventory data for troubleshooting

---

### Atlas Networking Lab

A module for network diagnostics and infrastructure experiments.

Planned topics:

* ping and latency checks
* DNS resolution
* interface inspection
* SSH automation
* local network scanning
* sockets
* TCP and UDP experiments
* bandwidth testing
* API and endpoint health checks

Possible use cases:

* test DNS, gateway and internet connectivity
* diagnose latency and packet loss
* scan reachable hosts in a local network
* monitor internal endpoints

---

### Atlas Messaging Lab

A module for queues, workers and asynchronous processing.

Planned topics:

* Redis queues
* RabbitMQ experiments
* Celery workers
* background jobs
* retry policies
* event-driven workflows
* asynchronous task processing

Possible use cases:

* process scraper jobs in the background
* queue document extraction tasks
* send report generation jobs to workers
* connect automation events to pipelines

---

### Atlas Cloud, DevOps and Observability

The operational foundation of the project.

Planned topics:

* Docker
* Docker Compose
* PostgreSQL
* Redis experiments
* GitHub Actions
* cloud deployment
* AWS, Google Cloud and Azure SDK experiments
* infrastructure automation
* logs
* metrics
* traces
* health checks
* monitoring
* backups
* zero-downtime deployment experiments

---

### Atlas Systems Lab

A module for lower-level systems knowledge.

Planned topics:

* Linux fundamentals
* processes and threads
* asynchronous programming
* sockets
* TCP/UDP experiments
* P2P communication
* distributed systems
* cryptography basics
* concurrency issues
* fault tolerance
* load testing
* IoT experiments

---

### Atlas Web

A future React interface for dashboards, storytelling and portfolio presentation.

Planned features:

* landing page
* interactive project map
* data dashboards
* statistical visualizations
* pipeline monitoring
* experiment history
* RAG playground
* support diagnostics dashboard
* gamified learning interface

---

### Atlas Mobile

A future Android application built with Kotlin.

Planned features:

* offline-first access
* local cache with Room/SQLite
* API synchronization
* notifications
* simplified dashboards
* chatbot access
* mobile data collection experiments
* support checklist access
* field diagnostics experiments

---

### Atlas Legacy Lab

A future module for practicing maintenance and modernization of legacy systems.

Planned topics:

* messy legacy scripts
* characterization tests
* refactoring
* adapters
* Strangler Fig Pattern
* technical debt documentation

This module exists because real software rarely arrives clean, documented and emotionally available.

---

## Technology Stack

### Current / Initial

* Python
* FastAPI
* PostgreSQL
* SQLAlchemy or SQLModel
* Pydantic
* Docker
* Docker Compose
* pytest
* Git and GitHub

### Planned / Experimental

* NumPy
* Pandas
* Polars
* PyArrow
* DuckDB
* OpenPyXL
* scikit-learn
* statsmodels
* PyMC
* PyTorch
* TensorFlow / Keras
* Hugging Face ecosystem
* LangChain / LangGraph
* Flowise
* Ollama
* Replicate
* ChromaDB, Qdrant, FAISS or PGVector
* BeautifulSoup, Scrapy, Playwright and Selenium
* PyMuPDF, pdfplumber, Unstructured and LayoutParser
* pytesseract and EasyOCR
* Redis, Celery and RabbitMQ experiments
* psutil, WMI and support automation tools
* networking tools such as dnspython, scapy, paramiko and ping utilities
* boto3, Google Cloud SDKs and Azure SDKs
* Grafana, Prometheus and OpenTelemetry
* React and TypeScript
* Kotlin Android and Room / SQLite
* n8n

---

## Roadmap

### Phase 0: Foundation

* [ ] Organize the backend structure
* [ ] Create `/health` endpoint
* [ ] Create `/version` endpoint
* [ ] Connect FastAPI to PostgreSQL
* [ ] Add basic tests
* [ ] Add initial documentation
* [ ] Create the first ADR

### Phase 1: Atlas Core

* [ ] Create domain entities
* [ ] Create use cases
* [ ] Create repository interfaces
* [ ] Add unit tests
* [ ] Document domain decisions

### Phase 2: Data Mining, Scraping and ETL

* [ ] Create the first data source
* [ ] Build the first scraper
* [ ] Store raw data
* [ ] Validate collected data
* [ ] Transform and load data into PostgreSQL
* [ ] Expose data through the API

### Phase 3: OCR and Document Intelligence

* [ ] Extract text from PDFs
* [ ] Extract text from scanned images
* [ ] Structure document sections
* [ ] Prepare chunks for RAG
* [ ] Build a small document question-answering prototype

### Phase 4: Statistical Lab

* [ ] Add a descriptive statistics module
* [ ] Add probability simulations
* [ ] Add sampling experiments
* [ ] Add confidence interval examples
* [ ] Add hypothesis testing examples
* [ ] Add regression experiments
* [ ] Add Bayesian modeling experiments

### Phase 5: Machine Learning

* [ ] Add initial ML experiments
* [ ] Add model evaluation metrics
* [ ] Add simple reproducible experiment tracking
* [ ] Compare manual implementations with library-based models

### Phase 6: Deep Learning

* [ ] Implement a simple neural network from scratch
* [ ] Implement gradient descent and backpropagation in a didactic example
* [ ] Create an MLP experiment with PyTorch
* [ ] Create a text classification experiment
* [ ] Create an initial embeddings experiment
* [ ] Compare a classical model with a neural network on the same problem

### Phase 7: AI, RAG and Agents

* [ ] Add embeddings
* [ ] Create a RAG prototype
* [ ] Integrate a local model with Ollama
* [ ] Add agent-based tools
* [ ] Add response evaluation and logging

### Phase 8: Support and Networking

* [ ] Create a machine diagnostic script
* [ ] Generate a support report in Markdown or HTML
* [ ] Add DNS and latency checks
* [ ] Add endpoint health checks
* [ ] Add simple network inventory experiments

### Phase 9: Automation and Messaging

* [ ] Add n8n workflows
* [ ] Add alerts
* [ ] Automate reports
* [ ] Add a queue/worker experiment
* [ ] Create WhatsApp or email integration experiments

### Phase 10: Web, Storytelling and Portfolio

* [ ] Build a React dashboard
* [ ] Add visual reports
* [ ] Create a visual portfolio map
* [ ] Add statistical visualizations
* [ ] Add support/network dashboards

### Phase 11: Cloud, DevOps and Observability

* [ ] Add a CI/CD pipeline
* [ ] Create a deployment environment
* [ ] Add structured logging
* [ ] Add metrics and traces
* [ ] Add monitoring
* [ ] Add load tests

### Phase 12: Systems, Security and Distributed Experiments

* [ ] Add socket experiments
* [ ] Add distributed system prototypes
* [ ] Add cryptography examples
* [ ] Add IoT experiments
* [ ] Add chaos/resilience experiments when the foundation is mature

---

## Running Locally

This section will expand as the project foundation is implemented.

Expected future flow:

```bash
git clone https://github.com/caio-stat/atlas.git
cd atlas

python -m venv .venv
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install only the tracks needed for the current task:

```bash
pip install -r requirements/core.txt
pip install -r requirements/dev.txt
```

Example for a specific study track:

```bash
pip install -r requirements/statistics.txt
```

Future Docker flow:

```bash
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

* working code
* tests
* documentation
* a clear architectural decision
* a portfolio-ready explanation
* a connection with data, statistics, AI, infrastructure or software engineering

The project should not try to become complete all at once. It should evolve like real software: incrementally, with some inevitable suffering and fewer illusions each week.

---

## Portfolio Value

Atlas is intended to demonstrate the ability to:

* design modular systems
* build APIs
* work with databases
* collect and process data
* apply statistics to real problems
* build machine learning experiments
* study and implement deep learning models
* use generative AI responsibly
* automate workflows
* build support and networking diagnostic tools
* organize cloud, DevOps and observability experiments
* document technical decisions
* think about scalability, resilience and maintainability

---

## License

This project is licensed under the MIT License.

---

## Author

Developed by **Caio Costa Cavalcante** as a long-term technical portfolio and learning laboratory in Data, AI, Statistics, Automation, Infrastructure and Software Engineering.
