"""
Graph using adjacency matrix.
Description: 2D matrix to represent edges.
Real-life analogy: City map with direct routes.
"""
class GraphAdjMatrix:
    def __init__(self, n):
        self.matrix = [[0]*n for _ in range(n)]
    def add_edge(self, u, v):
        self.matrix[u][v] = 1
        self.matrix[v][u] = 1  # For undirected
# Example usage:
# gm = GraphAdjMatrix(3)
# gm.add_edge(0,1)
# gm.add_edge(1,2) 