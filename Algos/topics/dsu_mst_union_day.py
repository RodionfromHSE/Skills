from dataclasses import dataclass, field

@dataclass
class Point:
    x: int
    y: int

    def dist_to(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
    
@dataclass(order=True)
class Edge:
    v: int = field(compare=False)
    u: int = field(compare=False)
    weight: float
    

def get_full_graph_edges(points):
    n = len(points)
    edges = []
    for v in range(n):
        for u in range(v + 1, n):
            e = Edge(v, u, points[v].dist_to(points[u]))
            edges.append(e)
    return edges

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def get(self, v):
        if v == self.parent[v]:
            return v
        self.parent[v] = self.get(self.parent[v])
        return self.parent[v]

    def join(self, v, u):
        v = self.get(v)
        u = self.get(u)

        if v == u:
            return

        if self.rank[v] < self.rank[u]:
            v, u = u, v

        self.parent[u] = v
        if self.rank[v] == self.rank[u]:
            self.rank[v] += 1

def main():
    n = int(input())
    
    cities = []
    for _ in range(n):
        x, y = map(int, input().split())
        cities.append(Point(x, y))

    edges = get_full_graph_edges(cities)
    edges.sort()

    dsu = DSU(n)
    ans = 0
    for e in edges:
        if dsu.get(e.v) != dsu.get(e.u):
            dsu.join(e.v, e.u)
            ans += e.weight
    
    print(ans)

if __name__ == '__main__':
    main()
    