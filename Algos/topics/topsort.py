from dataclasses import dataclass, field
from collections import deque, defaultdict

def has_cycle_dfs(children, mark, v, color):
    if mark[v] != 0:
        return mark[v] == color
    mark[v] = color
    for u in children[v]:
        if has_cycle_dfs(children, mark, u, color):
            return True
    return False

def has_cycle(children):
    n = len(children)
    mark = [0] * n
    color = 1
    for v in range(n):
        if mark[v] != 0:
            continue
        if has_cycle_dfs(children, mark, v, color):
            return True
        color += 1
    return False


def go(children, mark, v):
    if mark[v]:
        return
    mark[v] = True
    go.path.append(v)
    for u in children[v]:
        go(children, mark, u)
go.path = []

def topsort(children):
    if has_cycle(children):
        return None
    
    n = len(children)
    mark = [False] * n
    rev_res = []
    for v in range(n):
        go(children, mark, v)
        while go.path:
            rev_res.append(go.path.pop())
    return reversed(rev_res)

def main():
    n, m = map(int, input().split())
    children = [[] for _ in range(n)]
    for _ in range(m):
        v_from, v_to = map(int, input().split())
        children[v_from - 1].append(v_to - 1)

    res = topsort(children)
    if res is None:
        print(-1)
    else:
        print(*[v + 1 for v in res])


if __name__ == '__main__':
    main()