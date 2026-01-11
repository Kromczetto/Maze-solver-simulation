# Maze Exploration Algorithms

This document describes the maze exploration algorithms implemented in the
**Maze Explorer** project. Each algorithm is presented from both a theoretical
and an implementation-oriented perspective.

The goal of this document is to explain:
- how each algorithm works,
- how it is implemented in code,
- what guarantees (or limitations) it provides,
- and how it behaves in practice during simulation.

---

## General Assumptions

All algorithms operate under the following assumptions:

- The maze is represented as a 2D grid.
- Cells are either **free** or **walls**.
- Movement is allowed only in four directions:
  - up, down, left, right.
- The start and goal cells are known.
- Algorithms discover the maze incrementally and update an internal robot map.
- Each algorithm is implemented as a **Python generator** and yields its state
  step by step for visualization and analysis.

---

## Common Data Structures

### Cell
Represents a single position in the maze:
- `row`
- `col`

Cells are immutable and hashable, allowing safe use in sets and dictionaries.

---

### RobotMap
Represents the robot’s internal knowledge of the maze:
- UNKNOWN – cell not yet observed
- FREE – cell confirmed as free
- WALL – cell confirmed as a wall

The robot map is updated dynamically during exploration.

---

## 1. Depth-First Search (DFS)

### Algorithm Overview

Depth-First Search is a classic graph traversal algorithm.
It explores as deeply as possible along each branch before backtracking.

In the context of maze exploration:
- the maze is treated as an implicit graph,
- each free cell is a node,
- edges exist between adjacent free cells.

---

### Core Characteristics

- Uses a **stack** to store the exploration path
- Marks cells as visited to avoid repetition
- Guarantees finding a path if one exists
- Does **not** guarantee the shortest path

---

### Implementation Strategy

- Maintain a stack of cells to explore
- At each step:
  - inspect neighboring cells,
  - mark walls and free cells in the robot map,
  - choose the first unvisited free neighbor,
  - backtrack if no unvisited neighbors remain

---


---

### Properties

- **Completeness:** Yes
- **Optimality:** No
- **Memory Usage:** Low
- **Behavior:** Deep exploration with late backtracking

---

## 2. Trémaux Algorithm

### Algorithm Overview

Trémaux’s algorithm is a classical maze-solving method originally designed
for human navigation.

It works by marking corridors:
- unvisited paths are preferred,
- visited paths are marked,
- fully explored paths are avoided.

---

### Core Characteristics

- Marks **edges**, not just cells
- Each corridor can be traversed at most twice
- Prevents infinite loops
- Suitable for unknown mazes

---

### Implementation Strategy

- Represent corridors as unordered edges between cells
- Assign marks:
  - 0 – unvisited
  - 1 – visited once
  - 2 – visited twice
- Prefer unvisited edges
- Backtrack only when no unvisited edges remain

---

---

### Properties

- **Completeness:** Yes
- **Optimality:** No
- **Memory Usage:** Moderate
- **Behavior:** Structured exploration with explicit backtracking

---

## 3. Wall Follower Algorithm

### Algorithm Overview

The Wall Follower algorithm follows a simple rule:
**always keep one hand on the wall** (left or right).

In simply connected mazes, this guarantees reaching the exit.

---

### Core Characteristics

- Orientation-dependent
- Requires a heading direction
- Very low memory usage
- Can fail in mazes with loops or isolated regions

---

### Implementation Strategy

- Track both:
  - current cell,
  - current direction.
- At each step:
  - try turning left,
  - then forward,
  - then right,
  - finally backward.
- Avoid revisiting the same `(cell, direction)` state.

---

---

### Loop Prevention

To avoid infinite loops:
- visited states are stored as `(cell, direction)`
- a maximum step limit is enforced

---

### Properties

- **Completeness:** Only for specific maze types
- **Memory Usage:** Very low
- **Behavior:** Deterministic, wall-oriented movement

---

## 4. Maze Routing (Heuristic-Based Exploration)

### Algorithm Overview

Maze Routing is a heuristic-driven exploration strategy inspired by
robot navigation techniques.

It combines:
- local sensing,
- directional memory,
- heuristic evaluation using Manhattan distance.

---

### Core Characteristics

- Maintains a heading direction
- Uses Manhattan distance as a heuristic
- Avoids revisiting `(cell, direction)` states
- Employs controlled backtracking

---

### Implementation Strategy

- From the current cell:
  - detect all free neighboring cells,
  - compute Manhattan distance to the goal,
  - select the best unvisited candidate.
- If no candidate exists, backtrack using a move stack.

---


---

### Properties

- **Completeness:** Yes
- **Optimality:** No (heuristic-guided)
- **Memory Usage:** Moderate
- **Behavior:** Goal-oriented exploration

---

## Algorithm Comparison Summary

| Algorithm       | Complete | Memory Usage | Heuristic |
|-----------------|----------|--------------|-----------|
| DFS             | Yes      | Low          | No        |
| Trémaux         | Yes      | Moderate     | Partial   |
| Wall Follower   | No*      | Very Low     | No        |
| Maze Routing    | Yes      | Moderate     | Yes       |

\* Wall Follower completeness depends on maze topology.

---

## Educational Value

The implemented algorithms represent different paradigms:
- uninformed search (DFS),
- rule-based exploration (Wall Follower),
- classical maze-solving (Trémaux),
- heuristic-guided navigation (Maze Routing).

This allows meaningful comparison of:
- exploration efficiency,
- path behavior,
- robustness,
- and algorithmic trade-offs.

---

## Conclusion

The Maze Explorer project provides a unified framework for studying
maze exploration algorithms in a controlled and visual environment.
Each algorithm highlights different aspects of navigation, decision-making,
and state management in grid-based environments.





