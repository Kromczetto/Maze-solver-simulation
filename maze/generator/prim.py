import random

def generate_maze_prim(rows, cols):
    grid = [[1 for _ in range(cols)] for _ in range(rows)]

    def in_bounds(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def neighbors(r, c):
        for dr, dc in [(-2,0),(2,0),(0,-2),(0,2)]:
            nr, nc = r + dr, c + dc
            if in_bounds(nr, nc):
                yield nr, nc, r + dr//2, c + dc//2

    start = (1, 1)
    grid[1][1] = 0
    frontier = []

    for n in neighbors(*start):
        frontier.append(n)

    while frontier:
        r, c, wr, wc = frontier.pop(random.randrange(len(frontier)))
        if grid[r][c] == 1:
            grid[r][c] = 0
            grid[wr][wc] = 0
            for n in neighbors(r, c):
                if grid[n[0]][n[1]] == 1:
                    frontier.append(n)

    return grid
