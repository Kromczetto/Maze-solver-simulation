from collections import deque
from maze.cell import Cell

def bfs_explore(maze, start: Cell, goal: Cell):
    queue = deque([start])
    visited = {start}
    parent = {start: None}

    while queue:
        current = queue.popleft()
        yield current, visited.copy()

        if current == goal:
            break

        for neighbor in maze.get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)

    path = []
    if goal in parent:
        cur = goal
        while cur:
            path.append(cur)
            cur = parent[cur]
        path.reverse()

    return path
