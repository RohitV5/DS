"""
Common graph algorithms: BFS, DFS, Dijkstra, A*
"""
from queue import PriorityQueue
class GraphAlgorithms:
    @staticmethod
    def bfs(graph, start):
        visited, queue = set(), [start]
        order = []
        while queue:
            node = queue.pop(0)
            if node not in visited:
                order.append(node)
                visited.add(node)
                queue.extend(graph.get(node, []))
        return order
    @staticmethod
    def dfs(graph, start):
        visited, stack = set(), [start]
        order = []
        while stack:
            node = stack.pop()
            if node not in visited:
                order.append(node)
                visited.add(node)
                stack.extend(graph.get(node, []))
        return order
    @staticmethod
    def dijkstra(graph, start):
        dist = {node: float('inf') for node in graph}
        dist[start] = 0
        pq = PriorityQueue()
        pq.put((0, start))
        while not pq.empty():
            d, node = pq.get()
            if d > dist[node]:
                continue
            for neighbor, weight in graph[node]:
                if dist[neighbor] > dist[node] + weight:
                    dist[neighbor] = dist[node] + weight
                    pq.put((dist[neighbor], neighbor))
        return dist
    @staticmethod
    def a_star(graph, start, goal, heuristic):
        open_set = PriorityQueue()
        open_set.put((0, start))
        came_from = {}
        g_score = {node: float('inf') for node in graph}
        g_score[start] = 0
        f_score = {node: float('inf') for node in graph}
        f_score[start] = heuristic(start)
        while not open_set.empty():
            _, current = open_set.get()
            if current == goal:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(start)
                return path[::-1]
            for neighbor, weight in graph[current]:
                tentative_g = g_score[current] + weight
                if tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score[neighbor] = tentative_g + heuristic(neighbor)
                    open_set.put((f_score[neighbor], neighbor))
        return []
# Example usage:
# graph = {0: [(1,1),(2,4)], 1: [(2,2)], 2: []}
# print(GraphAlgorithms.dijkstra(graph, 0)) 