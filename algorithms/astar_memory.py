import heapq
from itertools import count

def heuristic(a, b):
    return abs(a.row - b.row) + abs(a.col - b.col)

def astar_on_memory(robot_map, start, goal):
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {start: None}
    g = {start: 0}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            break

        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            r, c = current.row + dr, current.col + dc
            if 0 <= r < robot_map.height and 0 <= c < robot_map.width:
                neighbor = type(current)(r, c)
                if not robot_map.is_free(neighbor):
                    continue

                tentative = g[current] + 1
                if neighbor not in g or tentative < g[neighbor]:
                    g[neighbor] = tentative
                    f = tentative + heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f, neighbor))
                    came_from[neighbor] = current

    path = []
    cur = goal
    while cur:
        path.append(cur)
        cur = came_from.get(cur)
    return path[::-1]
