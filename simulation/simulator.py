from simulation.step import Step

def simulate(explorer, speed=1.0, max_steps=20000):
    steps = []
    step_index = 0

    for _ in range(max_steps):
        try:
            cell, visited, robot_map = next(explorer)

            steps.append(
                Step(
                    cell=cell,
                    visited=visited,
                    robot_map=robot_map,
                    step_index=step_index,
                    time_sec=step_index / speed
                )
            )

            step_index += 1

        except StopIteration:
            break

    return steps
