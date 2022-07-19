class DisjointSet:

    def __init__(self, n):        
        self.ranks = [1 for _ in range(n)]
        self.roots = [i for i in range(n)]

    def find(self, u):
        if self.roots[u] != u:
            self.roots[u] = self.find(u)
        return self.roots[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if self.ranks[root_u] > self.ranks[v]:
            self.roots[root_v] = root_u
        elif self.ranks[root_v] > self.ranks[root_u]:
            self.roots[root_u] = root_v
        else:
            self.roots[root_v] = root_u
            self.ranks[root_u] += 1

    