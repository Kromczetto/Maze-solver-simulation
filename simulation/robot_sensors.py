from maze.cell import Cell

def sense(real_maze, cell):
    sensed = {}

    for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
        r, c = cell.row + dr, cell.col + dc
        if not real_maze.in_bounds(r, c):
            continue

        neighbor = Cell(r, c)
        if real_maze.is_wall(r, c):
            sensed[neighbor] = "WALL"
        else:
            sensed[neighbor] = "FREE"

    return sensed
