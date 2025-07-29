"""
Topological sort for DAGs.
"""
class TopologicalSort:
    @staticmethod
    def sort(graph):
        visited, stack = set(), []
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbor in graph.get(node, []):
                dfs(neighbor)
            stack.append(node)
        for node in graph:
            dfs(node)
        return stack[::-1]
# Example usage:
# graph = {5:[2,0], 4:[0,1], 2:[3], 3:[1], 0:[], 1:[]}
# print(TopologicalSort.sort(graph)) 