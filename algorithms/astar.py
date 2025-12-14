import heapq
from itertools import count
from maze.cell import Cell


def heuristic(a: Cell, b: Cell) -> int:
    return abs(a.row - b.row) + abs(a.col - b.col)


def astar_explore(maze, start: Cell, goal: Cell):
    open_set = []
    counter = count()

    heapq.heappush(open_set, (0, next(counter), start))

    came_from = {start: None}
    g_score = {start: 0}
    visited = set()

    while open_set:
        _, _, current = heapq.heappop(open_set)

        if current in visited:
            continue

        visited.add(current)

        yield current, visited.copy()

        if current == goal:
            break

        for neighbor in maze.get_neighbors(current):
            tentative_g = g_score[current] + 1

            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                g_score[neighbor] = tentative_g
                f = tentative_g + heuristic(neighbor, goal)
                heapq.heappush(
                    open_set,
                    (f, next(counter), neighbor)
                )
                came_from[neighbor] = current

    path = []
    if goal in came_from:
        cur = goal
        while cur is not None:
            path.append(cur)
            cur = came_from[cur]
        path.reverse()

    return path
