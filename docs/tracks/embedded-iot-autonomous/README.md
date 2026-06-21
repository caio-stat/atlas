# Atlas Embedded, IoT and Autonomous Systems Lab

> Edge devices, industrial protocols, control, robotics, and autonomous behavior.

**English** | [Português](README.pt-BR.md)

[Tracks index](../README.md) · [Documentation](../../README.md) · [Project](../../../README.md)

## Mission

This track connects software to physical devices and constrained runtimes. Safety, deterministic behavior, protocol correctness, simulation, and graceful degradation take priority over feature breadth.

## Expected outcomes

- Turn study into executable, tested, and demonstrable software.
- Record assumptions, decisions, limitations, and evidence reproducibly.
- Deliver integrable components without unnecessary coupling.
- Produce portfolio material that explains the result and the reasoning.

## Technical scope

- Embedded Linux and MicroPython
- Serial, Modbus, CAN, MQTT, BLE, and OPC-UA
- Sensors, telemetry, and edge storage
- Control loops and simulation
- Robotics and actuator boundaries
- FPGA and native-runtime integration
- Device health and autonomous recovery
- Industrial and hard real-time integration

## Reference deliverables

- A simulated telemetry pipeline
- A protocol adapter with recorded fixtures
- A PID or control-system simulation
- A device-health monitor
- A safe edge-inference experiment

## Architectural approach

- Start with a small vertical slice containing input, rule, output, and test.
- Separate domain logic from frameworks, storage, and external interfaces.
- Prefer explicit contracts and replaceable adapters.
- Add infrastructure only when a concrete use case requires it.
- Document irreversible or high-impact decisions through ADRs.

## Dependency tracks

- [`embedded.txt`](../../../requirements/embedded.txt)
- [`embedded_linux.txt`](../../../requirements/embedded_linux.txt)
- [`micropython.txt`](../../../requirements/micropython.txt)
- [`fpga.txt`](../../../requirements/fpga.txt)
- [`hardware_protocols.txt`](../../../requirements/hardware_protocols.txt)
- [`iot.txt`](../../../requirements/iot.txt)
- [`industrial.txt`](../../../requirements/industrial.txt)
- [`robotics.txt`](../../../requirements/robotics.txt)
- [`control_system.txt`](../../../requirements/control_system.txt)
- [`hard_realtime_integration.txt`](../../../requirements/hard_realtime_integration.txt)
- [`autonomous_systems.txt`](../../../requirements/autonomous_systems.txt)

## Integration with Atlas

- Sends telemetry through Messaging
- Stores measurements through Data Engineering
- Uses Observability for device health and alerting

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
