from maze.robot_map import RobotMap
from simulation.robot_sensors import sense

def micromouse_explore(real_maze, start, goal):
    robot_map = RobotMap(real_maze.height, real_maze.width)

    stack = [start]
    visited = set()
    robot_map.set_free(start)

    while stack:
        current = stack[-1]
        visited.add(current)

        yield current, visited.copy(), robot_map

        if current == goal:
            return robot_map

        sensed = sense(real_maze, current)
        moved = False

        for cell, state in sensed.items():
            if state == "WALL":
                robot_map.set_wall(cell)
            else:
                robot_map.set_free(cell)
                if cell not in visited:
                    stack.append(cell)
                    moved = True
                    break

        if not moved:
            stack.pop() 
