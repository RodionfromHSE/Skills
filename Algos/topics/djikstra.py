# dataclass
from dataclasses import dataclass, field
from collections import deque, defaultdict
import heapq

@dataclass
class Edge:
    to: int
    w: int

    def __iter__(self):
        return iter((self.to, self.w))



def main():
    n, m = map(int, input().split())
    s, e = map(int, input().split())
    s -= 1; e -= 1

    ch = [[] for _ in range(n)]
    for _ in range(m):
        a, b, w = map(int, input().split())
        a -= 1; b -= 1
        ch[a].append(Edge(b, w))
        ch[b].append(Edge(a, w))

    MAX_INF = int(1e9)
    d = [MAX_INF] * n
    d[s] = 0
    q = [(0, s)]
    while q:
        _, v = q.pop(0)
        for to, w in ch[v]:
            if d[to] == MAX_INF or d[to] > d[v] + w:
                d[to] = d[v] + w
                heapq.heappush(q, (d[to], to))
    
    print(d[e])
    
    

if __name__ == '__main__':
    main()