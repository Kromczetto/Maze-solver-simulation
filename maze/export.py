def maze_to_text(grid, start, goal):
    rows = len(grid)
    cols = len(grid[0])
    lines = []

    for r in range(rows):
        line = ""
        for c in range(cols):
            if (r, c) == start:
                line += "s"
            elif (r, c) == goal:
                line += "g"
            elif grid[r][c] == 1:
                line += "#"
            else:
                line += " "
        lines.append(line)

    return "\n".join(lines)
