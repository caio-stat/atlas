# Atlas Games and Simulation Lab

> Interactive systems, agent behavior, game telemetry, and real-time simulation.

**English** | [Português](README.pt-BR.md)

[Tracks index](../README.md) · [Documentation](../../README.md) · [Project](../../../README.md)

## Mission

The Games and Simulation Lab uses interactive environments to make algorithms, probability, agents, and real-time constraints visible. Projects should emphasize measurable behavior and educational value rather than engine breadth.

A larger flagship project in this track should be a mobile-first game that demonstrates both gameplay depth and engineering discipline: clear rules, readable telemetry, repeatable testing, and performance awareness for phones. It can also use references from psychology and philosophy to challenge attention, decision-making, ambiguity tolerance, emotional resilience, self-control, and the player's very sense of identity. The goal is to create a mental-training and existential-reflection experience where the user must think quickly, revise assumptions, tolerate controlled frustration, adapt behavior under pressure, and confront different ways of interpreting reality.

## Expected outcomes

- Turn study into executable, tested, and demonstrable software.
- Record assumptions, decisions, limitations, and evidence reproducibly.
- Deliver integrable components without unnecessary coupling.
- Produce portfolio material that explains the result and the reasoning.

## Technical scope

- 2D and lightweight 3D prototypes
- Mobile-first touch controls and responsive layouts
- Game loops, timing, and frame-budget analysis
- Physics and discrete simulation
- Pathfinding and agent behavior
- Progression systems, economy, and persistence
- Behavioral psychology and attention design
- Cognitive, humanistic, psychoanalytic, existential, and neuroscientific frameworks
- Cognitive load, uncertainty, controlled stress, and decision-making
- Reward loops, habit formation, motivation, and adaptive feedback
- Philosophies of perception, freedom, ethics, and consequence
- Reinforcement-learning environments
- Game telemetry and analytics
- Interactive probability visualization

## Proposed flagship concept

A strong portfolio direction is a mobile-ready game such as **Atlas Run**: a 2D action/arcade experience with short sessions, procedural challenges, upgrade choices, lightweight AI opponents, and scenarios that force the player to interpret ambiguous signals, moral dilemmas, and patterns of behavior. The project should prioritize:

- one clear core loop that works well on touch screens;
- deterministic gameplay rules that are easy to test;
- controlled psychological pressure, such as uncertainty, tight timing, meaningful trade-offs, rapid context reading, and choices that reveal personal preference;
- telemetry for retention, session length, error rate, hesitation, pause patterns, strategy shifts, and difficulty balance;
- offline-friendly progression or save-state behavior;
- feedback design that encourages attention, working memory, self-correction, choice review, learning from mistakes, and reflection on behavior;
- a clean handoff between gameplay logic, UI, analytics, and behavioral experiments.

## Psychological dimension of the project

The game can use references from psychology and philosophy to provoke reflection and learning, for example:

- the classic stimulus-response tension, with variations in reinforcement and reward;
- the influence of attention, memory, and perception on player choice;
- the tension between freedom, determinism, and responsibility;
- the distinction between useful pain, constructive frustration, and emotional blockage;
- the comparison between behaviorist, cognitivist, humanistic, existentialist, psychoanalytic, and neuroscientific perspectives;
- the way narrative, symbols, and moral dilemmas shape interpretation and decision.

## Historical reference map

The project can be designed to engage major traditions across intellectual history:

- Psychology: structuralism, functionalism, behaviorism, Gestalt, psychoanalysis, cognitivism, humanism, social psychology, developmental psychology, positive psychology, and neuroscience.
- Philosophy: Socrates, Plato, and Aristotle; Stoicism, skepticism, and Epicureanism; rationalism and empiricism; Kant; pragmatism; phenomenology; existentialism; utilitarianism; virtue ethics; analytic and continental philosophy.
- Cross-cutting themes: mind and body, perception and reality, morality, intention, habit, fear, guilt, freedom, suffering, and purpose.

These mechanisms should be used transparently, with clear purpose and ethical guardrails rather than arbitrary deception or coercion.

## Reference deliverables

- A deterministic agent simulation
- A pathfinding visualizer
- A mobile-first game prototype with touch controls
- A game-telemetry analysis pipeline
- An interactive probability experiment
- A reinforcement-learning benchmark with baselines

## Architectural approach

- Start with a small vertical slice containing input, rule, output, and test.
- Separate domain logic from frameworks, storage, and external interfaces.
- Prefer explicit contracts and replaceable adapters.
- Add infrastructure only when a concrete use case requires it.
- Document irreversible or high-impact decisions through ADRs.

## Dependency tracks

- [`games.txt`](../../../requirements/games.txt)
- [`games_engines.txt`](../../../requirements/games_engines.txt)
- [`games_ai.txt`](../../../requirements/games_ai.txt)
- [`game_data.txt`](../../../requirements/game_data.txt)
- [`simulation.txt`](../../../requirements/simulation.txt)
- [`realtime_programming.txt`](../../../requirements/realtime_programming.txt)
- [`mobile.txt`](../../../requirements/mobile.txt)
- [`mobile_testing.txt`](../../../requirements/mobile_testing.txt)

## Integration with Atlas

- Uses Statistical and Numerical methods
- Streams telemetry through Real-Time infrastructure
- Provides controlled environments for AI experiments

## Quality and evidence

- Unit tests for deterministic rules and transformations.
- Integration tests at external boundaries.
- Versioned data, seeds, and configuration when required.
- Technical and product metrics appropriate to the experiment.
- Behavioral metrics on focus, error, review, pause, recovery, and strategy shifts.
- Explicit documentation of the psychological and philosophical references used in art, narrative, and game systems.
- README, examples, and limitations updated with the code.
- No committed secrets or personal data.
- Ethical design: the player should be able to recognize, understand, and, where appropriate, control the stimuli used.

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
