# Dependency tracks

> A modular Python dependency catalog for installing only the capability required by the current work.

**English** | [Português](README.pt-BR.md)

[Project](../README.md) · [Documentation](../docs/README.md) · [Technical tracks](../docs/tracks/README.md)

## Purpose

This directory separates dependencies by domain to keep environments smaller, reduce conflicts, and make each experiment's intent explicit. A file does not claim that every listed library is already used; it defines a candidate set for a specific module or laboratory.

The current executable backend environment uses the pinned [`backend/requirements.txt`](../backend/requirements.txt). Tracks in this directory are unpinned exploratory sets and do not replace an application lock file.

## Principles

- Install only the tracks required by the task.
- Use separate virtual environments for incompatible experimental stacks.
- Keep a dependency in the smallest track consistent with its use.
- Allow repetition across tracks; remove repetition inside one file.
- Do not list Python standard-library modules.
- Use `-r` only for intentional, documented composition.
- Pin versions in an application environment or lock file, not reflexively in every track.

## Installation

Create and activate a virtual environment before installation. Run commands from the repository root.

```bash
python -m venv .venv
# Activate the environment for your shell
python -m pip install --upgrade pip
python -m pip install -r requirements/core.txt
```

Multiple tracks can be combined explicitly:

```bash
python -m pip install \
  -r requirements/core.txt \
  -r requirements/data.txt \
  -r requirements/statistics.txt
```

## Example profiles

| Profile | Suggested files |
|---|---|
| Backend development | `core.txt`, `dev.txt`, `code_quality.txt`, `advanced_testing.txt` |
| Statistical analysis | `data.txt`, `statistics.txt`, `visualization.txt`, `notebooks.txt` |
| ML experiment | `data.txt`, `statistics.txt`, `ml.txt`, `mlops.txt` |
| RAG/agent prototype | `document_intelligence.txt`, `generative_ai.txt`, `agents.txt` |
| Operational automation | `scripting.txt`, `automation.txt`, `observability.txt` |
| Local cloud and delivery | `devops.txt`, `cloud_orchestration.txt`, `security.txt` |
| IoT experiment | `iot.txt`, `hardware_protocols.txt`, `observability.txt` |

## Complete catalog

### Foundation and development

Base libraries, development tooling, architecture, automation, and maintainability.

| File | Primary use |
|---|---|
| [`core.txt`](core.txt) | Tabular and analytical base used by small data workflows. |
| [`dev.txt`](dev.txt) | Tests, formatting, typing, hooks, and local development support. |
| [`support.txt`](support.txt) | Machine diagnostics, inventory, Windows integration, and support CLIs. |
| [`scripting.txt`](scripting.txt) | CLI construction, task automation, reports, HTTP calls, and logging. |
| [`automation.txt`](automation.txt) | Schedulers, workflow tools, workers, and file-system automation. |
| [`oop.txt`](oop.txt) | Data models, typing, serialization, and dependency-injection experiments. |
| [`software_design.txt`](software_design.txt) | Dependency injection, plugins, state machines, validation, and architecture support. |
| [`plugins.txt`](plugins.txt) | Plugin discovery, configuration, validation, and extension mechanisms. |
| [`refactoring.txt`](refactoring.txt) | AST tooling, formatters, type checks, dead-code analysis, and complexity. |
| [`code_quality.txt`](code_quality.txt) | Linting, static typing, security checks, documentation quality, and hooks. |

### Data and analytics

Collection-ready tabular work, statistics, numerical analysis, reporting, and large-scale processing.

| File | Primary use |
|---|---|
| [`data.txt`](data.txt) | General dataframe, Arrow, DuckDB, and spreadsheet work. |
| [`data_engineering.txt`](data_engineering.txt) | SQL access, ORM models, migrations, and analytical connectors. |
| [`big_data.txt`](big_data.txt) | Distributed and out-of-core processing with Spark, Dask, Ray, and Modin. |
| [`statistics.txt`](statistics.txt) | Scientific statistics, regression, tests, and symbolic support. |
| [`bayesian.txt`](bayesian.txt) | Bayesian modeling, inference, and posterior diagnostics. |
| [`optimization.txt`](optimization.txt) | Operations research and mathematical optimization models. |
| [`simulation.txt`](simulation.txt) | Discrete-event and process simulation. |
| [`time_series.txt`](time_series.txt) | Forecasting frameworks and temporal-model experiments. |
| [`anomaly_detection.txt`](anomaly_detection.txt) | Outlier, drift, change-point, streaming, and monitoring analysis. |
| [`visualization.txt`](visualization.txt) | Static, interactive, declarative, and word-cloud visualization. |
| [`notebooks.txt`](notebooks.txt) | Jupyter authoring, execution, conversion, versioning, reports, and caching. |
| [`bi.txt`](bi.txt) | Data access, dashboards, profiling, Excel, reports, and geospatial BI. |
| [`powerbi.txt`](powerbi.txt) | Power BI, Fabric, Microsoft authentication, tabular data, and notebooks. |
| [`geospatial.txt`](geospatial.txt) | Vector, raster, mapping, geocoding, and street-network analysis. |
| [`game_data.txt`](game_data.txt) | Statistical and visual analysis for game telemetry. |

### Artificial intelligence and machine learning

Classical and neural models, language, vision, agents, policies, and model operations.

| File | Primary use |
|---|---|
| [`ai.txt`](ai.txt) | Dependency-free umbrella that directs users to focused AI tracks. |
| [`ml.txt`](ml.txt) | Classical ML, boosting, imbalance handling, features, and tuning. |
| [`deep_learning.txt`](deep_learning.txt) | TensorFlow, Keras, PyTorch, Lightning, and experiment dashboards. |
| [`mlops.txt`](mlops.txt) | Experiment tracking, model monitoring, and data validation. |
| [`nlp.txt`](nlp.txt) | Text processing, embeddings, Transformers, datasets, and tokenization. |
| [`computer_vision.txt`](computer_vision.txt) | Image processing, augmentation, detection, and OCR support. |
| [`document_intelligence.txt`](document_intelligence.txt) | Document parsing, PDF extraction, and layout understanding. |
| [`ocr.txt`](ocr.txt) | Tesseract and neural OCR engines. |
| [`generative_ai.txt`](generative_ai.txt) | LLM providers, orchestration, vector stores, and local models. |
| [`agents.txt`](agents.txt) | Focused agent frameworks and typed agent development. |
| [`autonomous_systems.txt`](autonomous_systems.txt) | Agent workflows, state machines, scheduling, APIs, and validation. |
| [`policy_agents.txt`](policy_agents.txt) | Composite agents, policy engine, and decision-system installation. |
| [`policy_engine.txt`](policy_engine.txt) | Rules engines, JSON logic, validation, configuration, and auditing support. |
| [`decision_system.txt`](decision_system.txt) | Decision models, optimization, state, RL, data, and visualization. |
| [`mobile_ai.txt`](mobile_ai.txt) | ONNX, TensorFlow Lite, vision, and lightweight mobile inference. |
| [`games_ai.txt`](games_ai.txt) | Reinforcement learning, multi-agent environments, pathfinding, and evolution. |

### Cloud, distribution, and operations

Infrastructure providers, delivery automation, networks, messaging, reliability, and security.

| File | Primary use |
|---|---|
| [`cloud.txt`](cloud.txt) | Minimal multi-cloud storage, analytics, and identity SDK set. |
| [`aws.txt`](aws.txt) | AWS SDK, CLI, IaC, testing, deployment, security, and observability. |
| [`cloud_orchestration.txt`](cloud_orchestration.txt) | AWS, GCP, Azure, Pulumi, Terraform, Ansible, Docker, and Kubernetes. |
| [`devops.txt`](devops.txt) | Remote automation, configuration management, containers, and forge APIs. |
| [`networking.txt`](networking.txt) | HTTP, DNS, interfaces, packets, SSH, and speed diagnostics. |
| [`messaging.txt`](messaging.txt) | RabbitMQ, Redis workers, Kafka, and NATS clients. |
| [`distributed_system.txt`](distributed_system.txt) | Kafka, NATS, and event-stream processing experiments. |
| [`observability.txt`](observability.txt) | Structured logs, metrics, tracing, and error reporting. |
| [`resilience.txt`](resilience.txt) | Retry, circuit breakers, rate limits, health, queues, and resilience tests. |
| [`zero_downtime.txt`](zero_downtime.txt) | Serving, process control, containers, migrations, flags, and remote operations. |
| [`self_healing.txt`](self_healing.txt) | Dependency-free umbrella for resilience, observability, automation, and autonomy. |
| [`security.txt`](security.txt) | Cryptography, JWT, password hashing, and secure credential primitives. |

### Concurrency and real time

Asynchronous execution, parallelism, streams, live dashboards, and time-sensitive integration.

| File | Primary use |
|---|---|
| [`async_programming.txt`](async_programming.txt) | Async runtimes, HTTP, WebSockets, files, databases, messaging, and APIs. |
| [`concurrency.txt`](concurrency.txt) | Async IO, event systems, workers, scheduling, profiling, and tests. |
| [`parallel_computing.txt`](parallel_computing.txt) | Process parallelism, distributed execution, acceleration, and benchmarks. |
| [`real_time.txt`](real_time.txt) | WebSockets, SSE, pub/sub, brokers, async databases, and serialization. |
| [`realtime_programming.txt`](realtime_programming.txt) | Event-driven code, devices, industrial protocols, control, and simulation. |
| [`hard_realtime_integration.txt`](hard_realtime_integration.txt) | Native bindings, RPC, messaging, binary data, and runtime monitoring. |
| [`real_time_dashboard.txt`](real_time_dashboard.txt) | Live dataframes, charting, dashboard frameworks, APIs, and metrics. |

### Hardware, edge, and industry

Device software, protocols, telemetry, control, industrial systems, and robotics.

| File | Primary use |
|---|---|
| [`embedded.txt`](embedded.txt) | Serial, IoT, Modbus, BLE, CAN, data, and device-side utilities. |
| [`embedded_linux.txt`](embedded_linux.txt) | Monitoring, GPIO, networking, messaging, APIs, data, and logs at the edge. |
| [`micropython.txt`](micropython.txt) | MicroPython deployment, serial communication, and command-line support. |
| [`fpga.txt`](fpga.txt) | HDL testing, hardware description, simulation, binary data, and plotting. |
| [`hardware_protocols.txt`](hardware_protocols.txt) | Serial, Modbus, CAN, MQTT, BLE, OPC-UA, binary parsing, and networking. |
| [`iot.txt`](iot.txt) | Focused MQTT, serial, Modbus, BLE, and OPC-UA clients. |
| [`industrial.txt`](industrial.txt) | Industrial protocols, networking, messaging, data, and monitoring. |
| [`robotics.txt`](robotics.txt) | Math, control, simulation, hardware buses, vision, and visualization. |
| [`control_system.txt`](control_system.txt) | Numerical control, PID, simulation, and plotting. |

### Applications and tests

Web collection, mobile applications, game development, and higher-assurance testing.

| File | Primary use |
|---|---|
| [`scraping.txt`](scraping.txt) | HTTP and browser collection, HTML parsing, crawling, PDF extraction. |
| [`mobile.txt`](mobile.txt) | Python mobile prototypes, device APIs, networking, QR, and images. |
| [`mobile_testing.txt`](mobile_testing.txt) | Appium, ADB, UI automation, pytest, reports, and API checks. |
| [`games.txt`](games.txt) | 2D/3D frameworks, physics, math, assets, audio, and CLI tools. |
| [`games_engines.txt`](games_engines.txt) | Godot parsing, glTF assets, meshes, OpenGL, and windowing. |
| [`advanced_testing.txt`](advanced_testing.txt) | pytest ecosystem, property, mutation, fixtures, time, HTTP mocks, and reports. |
| [`safety_testing.txt`](safety_testing.txt) | Tests, static analysis, validation, reporting, and fault-injection support. |

## Composition and umbrella files

`policy_agents.txt` is an installable composition that includes `agents.txt`, `policy_engine.txt`, and `decision_system.txt` through `-r` directives. Included paths are relative to this directory.

`ai.txt` and `self_healing.txt` are intentionally dependency-free umbrella guides. They point to possible combinations without forcing a broad installation.

## Adding or changing a track

1. Confirm that the library exists in the package index and supports the adopted Python version.
2. Choose the most specific file; create another only for a clear technical boundary.
3. Add section comments when the list contains conceptual groups.
4. Avoid redundant alternatives unless the reason is documented.
5. Check duplicates, trailing whitespace, stale names, and broken includes.
6. Update this catalog and the related technical-track README.
7. Test installation in a clean environment before using it in a module.

## Recommended validation

```text
- every file uses snake_case and the .txt extension
- no entry is duplicated inside a file
- every -r directive points to an existing file
- no standard-library module is listed
- the catalog contains every track
- the consuming module declares which tracks it installs
```

## Limitations

- These lists are not lock files and may resolve different versions over time.
- Some stacks have native dependencies, operating-system requirements, or framework conflicts.
- Cloud, AI, and automation libraries may require accounts, credentials, or external cost.
- A library's presence in a track does not authorize data collection, device access, or external mutations.
