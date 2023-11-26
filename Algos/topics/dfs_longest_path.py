# dataclass
from dataclasses import dataclass, field
from collections import deque, defaultdict


def dfs(v):
    global d, ans, children
    
    if d[v] != 0:
        return d[v]
    
    d[v] = 1
    for u in children[v]:
        son_depth = dfs(u)
        d[v] = max(d[v], son_depth + 1)
    ans = max(ans, d[v])
    return d[v]


def main():
    n, m = map(int, input().split())
    global children
    children = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        children[a].append(b)
    
    global d, ans
    ans = 0
    d = [0] * n
    for v in range(n):
        dfs(v)
    print(ans - 1)

if __name__ == '__main__':
    main()