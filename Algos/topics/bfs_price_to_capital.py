# dataclass
from dataclasses import dataclass, field
from collections import deque, defaultdict




def main():
    n, s, m = map(int, input().split())
    ch = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        ch[b - 1].append(a - 1)

    d = [-1] * n
    d[s - 1] = 0
    q = deque([s - 1])
    while q:
        v = q.popleft()
        for u in ch[v]:
            if d[u] == -1:
                d[u] = d[v] + 1
                q.append(u)
    
    for el in d:
        print(el, end=' ')
    
    

if __name__ == '__main__':
    main()