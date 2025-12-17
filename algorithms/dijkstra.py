import heapq

def dijkstra(robot_map, start, goal):
    robot_map.set_free(start)
    robot_map.set_free(goal)

    pq = []
    heapq.heappush(pq, (0, start))

    dist = {start: 0}
    came_from = {start: None}

    while pq:
        current_dist, current = heapq.heappop(pq)

        if current == goal:
            break

        if current_dist > dist[current]:
            continue

        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            r, c = current.row + dr, current.col + dc
            if 0 <= r < robot_map.height and 0 <= c < robot_map.width:
                neighbor = type(current)(r, c)
                if not robot_map.is_free(neighbor):
                    continue

                new_dist = current_dist + 1
                if neighbor not in dist or new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    came_from[neighbor] = current
                    heapq.heappush(pq, (new_dist, neighbor))

    path = []
    cur = goal
    while cur:
        path.append(cur)
        cur = came_from.get(cur)

    return path[::-1]
