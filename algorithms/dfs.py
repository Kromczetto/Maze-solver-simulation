from maze.cell import Cell

def dfs_explore(maze, start: Cell, goal: Cell):
    stack = [start]
    visited = set([start])

    while stack:
        current = stack[-1]
        yield current, visited  

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
