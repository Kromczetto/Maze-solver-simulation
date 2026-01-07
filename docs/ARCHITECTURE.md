# System Architecture

The **Maze Explorer** project follows a modular, layered architecture designed to ensure
clear separation of concerns, deterministic execution, and reproducible experimentation.

---

## High-Level Overview

The system is composed of the following logical layers:

1. **User Interface (PyQt5)**  
   Responsible for user interaction, configuration of experiments, and control of execution.

2. **Simulation Engine**  
   Manages the lifecycle of a simulation, including initialization, step-wise execution,
   and synchronization between components.

3. **Algorithm Layer**  
   Contains maze exploration algorithms implemented as step-based or generator-driven
   processes.

4. **Maze Model**  
   Defines the maze structure, state representation, and domain-specific constraints.

5. **Visualization and Analysis**  
   Handles rendering of the exploration process and post-simulation analysis of results.

---

## Control Flow

The typical execution flow of the system is as follows:

1. The user selects a maze and an exploration algorithm via the user interface.
2. The selected algorithm explores the maze in a step-by-step manner.
3. The simulation engine records each step and updates the global state.
4. The visualization module renders the current exploration state.
5. Analysis modules process collected data and generate metrics or summaries.

---

## Design Principles

The architecture is guided by the following principles:

- **Separation of Concerns**  
  Each layer has a clearly defined responsibility and minimal coupling to other layers.

- **Deterministic Simulation**  
  Given the same inputs and configuration, the system produces identical results.

- **Stateless Visualization**  
  Visualization components derive their state exclusively from simulation data.

- **Reproducible Experiments**  
  All experiments can be replayed and analyzed under identical conditions.

---

## Architectural Patterns

The system employs several architectural and design patterns:

- **Generator-Based Control Flow**  
  Algorithms yield execution steps, enabling fine-grained simulation control.

- **Model–View Separation**  
  Core domain logic is strictly separated from presentation and visualization layers.

- **Event-Driven Simulation**  
  State changes propagate through well-defined events, enabling extensibility.

