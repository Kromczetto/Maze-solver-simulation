from maze.cell import Cell
from maze.robot_map import RobotMap

DIRECTIONS = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
]

def edge(a, b):
    return frozenset((a, b))

def manhattan(a, b):
    return abs(a.row - b.row) + abs(a.col - b.col)


def tremaux(maze, start, goal):
    robot_map = RobotMap(maze.height, maze.width)

    current = start
    edge_marks = {}
    came_from = {}   # Cell -> edge (do cofania)

    robot_map.set_free(current)
    yield current, set(), robot_map

    while True:
        if current == goal:
            return

        neighbors = []

        # zbierz sąsiadów
        for dr, dc in DIRECTIONS:
            nr, nc = current.row + dr, current.col + dc
            if not maze.in_bounds(nr, nc):
                continue

            neighbor = Cell(nr, nc)
            if maze.is_wall(nr, nc):
                robot_map.set_wall(neighbor)
                continue

            robot_map.set_free(neighbor)
            e = edge(current, neighbor)
            mark = edge_marks.get(e, 0)

            neighbors.append((neighbor, e, mark, manhattan(neighbor, goal)))

        # 1️⃣ preferuj NIEODWIEDZONE krawędzie + Manhattan
        candidates = [
            (n, e, d) for (n, e, m, d) in neighbors if m == 0
        ]

        if candidates:
            # deterministycznie: najbliżej celu
            candidates.sort(key=lambda x: x[2])
            next_cell, e, _ = candidates[0]

            edge_marks[e] = 1
            came_from[next_cell] = e
            current = next_cell
            yield current, set(), robot_map
            continue

        # 2️⃣ brak nowych → COFANIE
        if current not in came_from:
            return  # nie ma skąd wracać → koniec

        e = came_from[current]
        edge_marks[e] = 2
        a, b = tuple(e)
        next_cell = a if current == b else b

        if next_cell == current:
            return

        current = next_cell
        yield current, set(), robot_map
