"""
Disjoint Set (Union-Find) with path compression.
Description: Efficiently track connected components.
Real-life analogy: Social groups merging.
"""
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return
        if self.rank[xr] < self.rank[yr]:
            self.parent[xr] = yr
        else:
            self.parent[yr] = xr
            if self.rank[xr] == self.rank[yr]:
                self.rank[xr] += 1
# Example usage:
# uf = UnionFind(5)
# uf.union(0,1)
# print(uf.find(1))  # 0 or 1 