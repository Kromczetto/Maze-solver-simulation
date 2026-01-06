
---

# `docs/ARCHITECTURE.md`

```md
# System Architecture

The Maze Explorer project follows a modular, layered architecture.

---

## High-Level Overview

Layers:
1. User Interface (PyQt5)
2. Simulation Engine
3. Algorithm Layer
4. Maze Model
5. Visualization and Analysis

---

## Control Flow

1. User selects algorithm and maze
2. Algorithm explores maze step by step
3. Simulator records each step
4. Visualization renders exploration
5. Analysis modules process results

---

## Design Principles

- Separation of concerns
- Deterministic simulation
- Stateless visualization
- Reproducible experiments

---

## Architectural Patterns

- Generator-based control flow
- Model–View separation
- Event-driven simulation
