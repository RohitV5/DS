"""
Graph using adjacency list.
Description: Each node has a list of neighbors.
Real-life analogy: Social network friends list.
"""
class GraphAdjList:
    def __init__(self):
        self.graph = dict()
    def add_edge(self, u, v):
        self.graph.setdefault(u, []).append(v)
        self.graph.setdefault(v, []).append(u)  # For undirected
# Example usage:
# g = GraphAdjList()
# g.add_edge(1,2)
# g.add_edge(2,3) 