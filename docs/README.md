# Atlas documentation hub

> The navigation layer for architecture, technical tracks, executable modules, and portfolio evidence.

**English** | [Português](README.pt-BR.md)

[Project README](../README.md) · [Backend](../backend/README.md) · [Dependencies](../requirements/README.md)

## Purpose

Atlas documentation is part of the product. It explains what exists, what is
planned, why a decision was made, how to run a capability, and what evidence
supports a technical claim. This directory separates detailed material from
the root README so the project landing page can remain navigable.

## Documentation map

| Area | Contents | Entry point |
|---|---|---|
| Technical tracks | Mission, scope, deliverables, dependencies, quality, and roadmap for 21 domains | [Tracks catalog](tracks/README.md) |
| System modules | Documentation next to executable or specified modules | [Modules catalog](modules/README.md) |
| Backend | FastAPI foundation and application-layer boundaries | [Backend README](../backend/README.md) |
| Dependency tracks | Focused Python installation sets and maintenance rules | [Requirements README](../requirements/README.md) |
| Architecture decisions | Context, decision, alternatives, and consequences | [ADR 0001](../backend/0001-monolito-modular.md) |

## Document types

### Project README

The root README is the public landing page. It describes the product vision,
current state, architecture at a high level, quick start, documentation map,
roadmap, and contribution expectations. It should link to detail instead of
duplicating every module specification.

### Track README

A track document describes a long-lived technical direction such as Data
Engineering, Statistics, AI, or Observability. It may exist before code, but it
must label planned work honestly and define evidence required for progress.

### Module README

A module document lives close to an implementation or a concrete product
specification. It explains responsibilities, public contracts, dependencies,
runtime behavior, testing, extension rules, and current limitations.

### Architecture Decision Record

An ADR captures a decision that affects several modules or is expensive to
reverse. It records context, chosen option, alternatives, consequences, and
follow-up actions. ADRs describe decisions; READMEs explain usage and scope.

### Runbook

A runbook is operational: symptoms, checks, commands, safe remediation,
rollback, escalation, and evidence to collect. Planned systems do not need
fictional runbooks; operational modules do.

## Source-of-truth rules

- Runtime behavior is defined by code and tests; documentation explains it.
- Public contracts belong in module documentation and API schemas.
- Cross-cutting decisions belong in ADRs.
- Dependency membership belongs in `requirements/*.txt` and its catalog.
- Planned capability must be marked **planned**, not described as available.
- A status claim should link to code, tests, an example, or operational evidence.

## Bilingual policy

Every primary project, track, and module README has two versions:

- `README.md` for English;
- `README.pt-BR.md` for Brazilian Portuguese.

Both versions must preserve the same section structure and technical meaning.
A content change is complete only when both documents are updated. Library,
class, protocol, and command names remain in their canonical technical form.

## Writing standard

Good Atlas documentation should answer:

1. What problem does this component solve?
2. What is inside and outside its boundary?
3. What contracts does it expose or consume?
4. How can a new contributor run and verify it?
5. Which failures, risks, and limitations matter?
6. What is implemented now and what is only planned?
7. What evidence demonstrates quality?

Prefer concrete examples, relative links, explicit status, and short diagrams.
Avoid unsupported promises, copied marketing language, unexplained acronyms,
and architecture descriptions that do not match the repository.

## Review checklist

- [ ] English and Portuguese versions are structurally aligned.
- [ ] Relative links resolve from the document location.
- [ ] Commands match the current repository layout.
- [ ] Planned and implemented behavior are clearly distinguished.
- [ ] Inputs, outputs, errors, security, and privacy are covered when relevant.
- [ ] Tests or evidence are linked for implemented behavior.
- [ ] No secret, credential, personal data, or private endpoint appears.
- [ ] The owning track and integrated modules are linked.

## Adding documentation

1. Place overview content in the nearest module README.
2. Add a track document only for a durable technical direction.
3. Create an ADR when a decision crosses module boundaries or is costly to reverse.
4. Add both language versions in the same change.
5. Link the new document from this hub or the appropriate catalog.
6. Validate Markdown links and compare headings between languages.

## Current documentation status

The documentation architecture is established. Most technical tracks are
planned; the FastAPI backend has initial executable endpoints; PostgreSQL is
available through Docker Compose; and the Mobile Lab has a detailed stack
specification but no application code yet.
