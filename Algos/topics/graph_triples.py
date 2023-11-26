# dataclass
from dataclasses import dataclass, field
from collections import deque, defaultdict


def main():
    n, m = map(int, input().split())
    d = [defaultdict(bool) for _ in range(n)]
    edges = set()
    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        d[a][b] = d[b][a] = True
        edges.add((min(a, b), max(a, b)))
    
    ans = 0
    for v, u in edges:
        for i in range(n):
            if d[v][i] and d[u][i]:
                ans += 1
    print(ans // 3)

if __name__ == '__main__':
    main()