# Atlas Messaging and Real-Time Lab

> Queues, events, streams, background workers, and live interfaces.

**English** | [Português](README.pt-BR.md)

[Tracks index](../README.md) · [Documentation](../../README.md) · [Project](../../../README.md)

## Mission

This track studies temporal coupling and delivery guarantees. Technology choices must follow workload needs such as ordering, throughput, latency, durability, replay, and operational complexity.

## Expected outcomes

- Turn study into executable, tested, and demonstrable software.
- Record assumptions, decisions, limitations, and evidence reproducibly.
- Deliver integrable components without unnecessary coupling.
- Produce portfolio material that explains the result and the reasoning.

## Technical scope

- Work queues and background workers
- Publish/subscribe messaging
- Event streams and replay
- WebSockets and Server-Sent Events
- Async API and database access
- Scheduling and delayed delivery
- Delivery semantics, idempotency, and backpressure

## Reference deliverables

- A background job with retry and dead-letter handling
- A pub/sub status feed
- A FastAPI WebSocket or SSE endpoint
- A small event-streaming benchmark
- A live pipeline-monitoring dashboard

## Architectural approach

- Start with a small vertical slice containing input, rule, output, and test.
- Separate domain logic from frameworks, storage, and external interfaces.
- Prefer explicit contracts and replaceable adapters.
- Add infrastructure only when a concrete use case requires it.
- Document irreversible or high-impact decisions through ADRs.

## Dependency tracks

- [`messaging.txt`](../../../requirements/messaging.txt)
- [`real_time.txt`](../../../requirements/real_time.txt)
- [`real_time_dashboard.txt`](../../../requirements/real_time_dashboard.txt)
- [`async_programming.txt`](../../../requirements/async_programming.txt)
- [`concurrency.txt`](../../../requirements/concurrency.txt)

## Integration with Atlas

- Decouples Automation and Data Engineering workloads
- Powers live API and BI updates
- Exports queue and consumer metrics to Observability

## Quality and evidence

- Unit tests for deterministic rules and transformations.
- Integration tests at external boundaries.
- Versioned data, seeds, and configuration when required.
- Technical and product metrics appropriate to the experiment.
- README, examples, and limitations updated with the code.
- No committed secrets or personal data.

## Incremental roadmap

### 1. Foundation

Define the glossary, initial use case, contract, and minimum test.

### 2. Applied prototype

Run a real use case with controlled data or infrastructure.

### 3. Integration

Connect the result to another module through an explicit contract.

### 4. Maturity

Add observability, operational documentation, and risk assessment.

## Definition of done

- The primary use case runs from clean setup instructions.
- Relevant behaviors have tests proportional to risk.
- Inputs, outputs, errors, and limitations are documented.
- Dependencies belong to the declared tracks.
- Integration respects Atlas boundaries.
- A short demonstration exists for technical review.

## Status

Planned track. This documentation defines the evolution contract; implementation should progress incrementally and reflect the repository's real state.
