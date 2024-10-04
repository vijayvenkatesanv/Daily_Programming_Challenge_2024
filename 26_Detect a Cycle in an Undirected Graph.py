class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])  # Path compression
        return self.parent[node]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u == root_v:
            return False  # Cycle detected
        if self.rank[root_u] > self.rank[root_v]:
            self.parent[root_v] = root_u
        elif self.rank[root_u] < self.rank[root_v]:
            self.parent[root_u] = root_v
        else:
            self.parent[root_v] = root_u
            self.rank[root_u] += 1
        return True

def has_cycle(V, edges):
    uf = UnionFind(V)
    
    for u, v in edges:
        if not uf.union(u, v):
            return True  # Cycle detected
    return False

# Test Cases
print(has_cycle(5, [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]]))  # True
print(has_cycle(3, [[0, 1], [1, 2]]))  # False
print(has_cycle(1, []))  # False
print(has_cycle(4, [[0, 1], [1, 2], [2, 3]]))  # False

# User Input
V = int(input("Enter the number of vertices: "))
E = int(input("Enter the number of edges: "))
edges = []

print("Enter the edges (format: vertex1 vertex2):")
for _ in range(E):
    u, v = map(int, input().split())
    if u < 0 or u >= V or v < 0 or v >= V:
        print(f"Error: vertices {u} and {v} must be in the range [0, {V-1}].")
    else:
        edges.append((u, v))

result = has_cycle(V, edges)
print("Does the graph contain a cycle?", result)
