from maze.cell import Cell

def robot_explore(maze, start: Cell, goal: Cell):

    stack = [start]
    visited = {start}

    while stack:
        current = stack[-1]

        yield current, visited.copy()

        if current == goal:
            return

        moved = False
        for neighbor in maze.get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
                moved = True
                break

        if not moved:
            stack.pop()
