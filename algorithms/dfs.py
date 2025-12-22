from maze.robot_map import RobotMap

def dfs(maze, start, goal):
    robot_map = RobotMap(maze.height, maze.width)
    visited = set()
    path = [start]

    robot_map.set_free(start)
    visited.add(start)

    yield start, visited.copy(), robot_map

    while path:
        current = path[-1]

        if current == goal:
            return

        # znajdź nieodwiedzonego sąsiada
        next_cell = None
        for neighbor in maze.get_neighbors(current):
            if neighbor not in visited:
                next_cell = neighbor
                break

        if next_cell:
            visited.add(next_cell)
            robot_map.set_free(next_cell)
            path.append(next_cell)

            yield next_cell, visited.copy(), robot_map
        else:
            # BACKTRACK – cofanie się
            path.pop()

            if path:
                yield path[-1], visited.copy(), robot_map
