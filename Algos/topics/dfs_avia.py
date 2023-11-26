# dataclass
from dataclasses import dataclass, field
from collections import deque, defaultdict

def dfs(v, mid):
    global mark, d, n
    if mark[v]:
        return
    mark[v] = True
    for u in range(n):
        if d[v][u] <= mid:
            dfs(u, mid)

def check(mid):
    global mark, n
    mark = [False] * n
    dfs(0, mid)
    return all(mark)


def main():
    global n, d
    n = int(input())
    d = [[int(10e6)] * n for _ in range(n)]
    for i in range(n):
        row = list(map(int, input().split()))
        for j, elem in enumerate(row):
            if i == j:
                continue
            d[i][j] = elem
    
    l, r = 0, int(10e6)
    while l + 1 < r:
        mid = (l + r) // 2
        if check(mid):
            r = mid
        else:
            l = mid
    print(r)

if __name__ == '__main__':
    main()