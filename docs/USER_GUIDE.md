# User Guide

This document describes how to use the **Maze Explorer** application
from the perspective of an end user.

---

## Application Overview

Maze Explorer enables users to:

- Explore mazes using multiple exploration algorithms
- Visualize the exploration process step by step
- Compare algorithm performance and efficiency
- Design and edit custom mazes
- Export results for further analysis

---

## Selecting an Algorithm

The application provides several built-in maze exploration algorithms:

- **Wall Follower**
- **Depth-First Search (DFS)**
- **Trémaux Algorithm**
- **Maze Routing (heuristic-based)**

The desired algorithm can be selected using the radio buttons
in the algorithm selection panel.

---

## Maze Editor

The maze editor allows interactive creation and modification of maze layouts.
The following controls are available:

- **Left Mouse Button** – place a wall
- **Right Mouse Button** – remove a wall
- **Shift + Click** – set the start position
- **Ctrl + Click** – set the goal position

---

## Running a Simulation

To start maze exploration, click the **Run** button.
The algorithm will explore the maze incrementally, and the progress
will be animated cell by cell in the visualization panel.

---

## Test Mode

The **Tests** tab provides tools for automated evaluation:

- Automatic execution of all available algorithms
- Comparison of step count and execution time
- Export of results to **TXT** and **Excel** formats
- Visualization of distance-to-goal metrics over time

---

## Exporting Results

Simulation results can be exported in the following formats:

- **TXT** – saves the maze layout and numeric results
- **Excel** – stores performance metrics in tabular form
- **Plot Data** – exports Manhattan distance values over time

