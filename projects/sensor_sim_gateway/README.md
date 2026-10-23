# Python AI + IoT — Lesson 1 (Project Setup)

## Goal
Start an engineering-grade Python project for IoT + AI:
- sensor data generation (simulated)
- gateway that reads telemetry
- basic testing setup

## What was done
- Created project structure: `src/`, `tests/`, `docs/`
- Created Python virtual environment (`.venv`)
- Installed dependencies:
  - `pytest` for tests
  - `numpy` for numerical processing (future ML features)
  - `pyserial` for UART/USB communication (future STM32 integration)
  - `paho-mqtt` for MQTT messaging (future IoT pipeline)

## How to run
### 1) Activate environment
```bash
source .venv/bin/activate

