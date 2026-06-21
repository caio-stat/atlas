# Atlas backend

> FastAPI and PostgreSQL foundation for the first executable Atlas vertical slices.

**English** | [Português](README.pt-BR.md)

[Project README](../README.md) · [Modules catalog](../docs/modules/README.md) · [API track](../docs/tracks/api/README.md)

## Current state

The backend is an early foundation, not a complete modular monolith. It
currently provides a FastAPI application with three synchronous endpoints,
a SQLAlchemy engine configured for the local PostgreSQL container, and two API
tests. Several packages exist as empty scaffolds for the intended architecture.

Implemented today:

- `GET /` returns `{"message": "Atlas conectado"}`;
- `GET /health` returns `{"status": "ok"}`;
- `GET /version` returns the API name and version `0.1.0`;
- SQLAlchemy exposes `engine` and `SessionLocal`;
- pytest verifies health and version responses;
- Docker Compose defines the local PostgreSQL service.

Not implemented yet:

- database-backed routes or a session dependency;
- typed settings in `app/core/config.py`;
- the `DataSource` domain entity;
- the `register_data_source` use case;
- versioned routers under `app/api/routes`;
- migrations, authentication, structured logging, readiness, or metrics;
- a completed modular-monolith ADR.

## Directory map

```text
backend/
├── app/
│   ├── api/
│   │   └── routes/                 # Planned HTTP route modules
│   ├── core/                       # Planned settings and cross-cutting primitives
│   ├── domain/
│   │   └── entities/               # Planned domain entities
│   ├── use_cases/                  # Planned application use cases
│   ├── database.py                 # Current SQLAlchemy engine and session factory
│   └── main.py                     # Current FastAPI app and endpoints
├── tests/
│   └── test_health.py              # Current API behavior tests
├── 0001-monolito-modular.md        # ADR placeholder; currently empty
├── pytest.ini
└── requirements.txt                # Pinned backend environment
```

Detailed module documentation:

- [Application package](app/README.md)
- [API interface](app/api/README.md)
- [Route modules](app/api/routes/README.md)
- [Core configuration](app/core/README.md)
- [Domain](app/domain/README.md)
- [Domain entities](app/domain/entities/README.md)
- [Use cases](app/use_cases/README.md)
- [Tests](tests/README.md)

## Local setup

Run the following commands from the repository root unless a step says
otherwise.

### 1. Create and activate a virtual environment

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

### 2. Install backend dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r backend/requirements.txt
```

### 3. Start PostgreSQL

```bash
docker compose up -d postgres
docker compose ps
```

The development service uses database `atlas_db`, user `atlas`, password
`atlas123`, and host port `5432`. These are repository-local development
credentials and must not be reused in shared or production environments.

### 4. Start the API

```bash
cd backend
python -m uvicorn app.main:app --reload
```

Useful URLs:

- API root: `http://127.0.0.1:8000/`
- health: `http://127.0.0.1:8000/health`
- version: `http://127.0.0.1:8000/version`
- OpenAPI UI: `http://127.0.0.1:8000/docs`

### 5. Run tests

From `backend/`:

```bash
python -m pytest
```

## Request flow today

```text
HTTP request
    ↓
FastAPI app in app/main.py
    ↓
Route function
    ↓
Static JSON response
```

The database module is imported independently and is not part of the current
endpoint flow. Documentation and future refactoring should not imply that the
health endpoint verifies PostgreSQL until a readiness check is implemented.

## Target request flow

```text
HTTP request
    ↓
API router and validation
    ↓
Application use case
    ↓
Domain rules
    ↓
Port
    ↓
SQLAlchemy or external-service adapter
```

This target is a direction, not the current state. The first useful migration
is to extract existing endpoints into routers without adding unnecessary
abstraction, then implement one complete data-source use case.

## Configuration

`app/database.py` currently contains a hard-coded development URL:

```text
postgresql://atlas:atlas123@localhost:5432/atlas_db
```

The next configuration step should move it to an environment-backed typed
settings object in `app/core/config.py`. Expected settings include environment,
API version, database URL, log level, and optional telemetry flags. Defaults
may support local development, but secrets must come from environment or a
secret manager outside development.

## Testing strategy

The existing tests use FastAPI `TestClient` and validate response status and
body. As behavior grows, separate tests by purpose:

- unit tests for entities and use cases without FastAPI or PostgreSQL;
- API contract tests for validation, status codes, and error formats;
- integration tests for SQLAlchemy repositories and migrations;
- readiness tests for external dependency checks;
- architecture tests for dependency direction.

Tests should verify observable behavior, not framework implementation details.

## Security and operations

- Treat Compose credentials as local-only.
- Never commit production database URLs, tokens, or personal data.
- Add timeouts and explicit failure handling at external boundaries.
- Keep `/health` cheap and process-local; use `/ready` for dependency readiness.
- Redact credentials and sensitive payloads from logs.
- Add correlation IDs before workflows span queues or external services.
- Define migration and rollback procedures before persistent schemas evolve.

## Next implementation slice

1. Add typed environment settings.
2. Extract health and version handlers into an API router.
3. Define a minimal `DataSource` entity with explicit invariants.
4. Define a repository port and `register_data_source` use case.
5. Implement a SQLAlchemy adapter and migration.
6. Expose one versioned route with unit and integration tests.
7. Complete ADR 0001 with context, decision, alternatives, and consequences.

## Definition of done for the foundation milestone

- A clean checkout starts PostgreSQL and the API from documented commands.
- `/health`, `/version`, and the first domain route have tests.
- Database configuration comes from typed settings.
- Schema changes use a reproducible migration.
- Domain and use-case tests do not require FastAPI or PostgreSQL.
- Logs contain request correlation without exposing secrets.
- English and Portuguese module documentation match implemented behavior.
