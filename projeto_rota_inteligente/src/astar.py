
import heapq

def astar(graph, start, goal, heuristic):
    queue = []
    heapq.heappush(queue, (0, start))

    came_from = {}
    cost = {node: float('inf') for node in graph}
    cost[start] = 0

    while queue:
        _, current = heapq.heappop(queue)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return list(reversed(path))

        for neighbor, weight in graph[current]:
            new_cost = cost[current] + weight

            if new_cost < cost[neighbor]:
                cost[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor, goal)
                heapq.heappush(queue, (priority, neighbor))
                came_from[neighbor] = current

    return None
