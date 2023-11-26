# dataclass
from dataclasses import dataclass, field
from collections import deque, defaultdict
import heapq


def main():
    n, m = map(int, input().split())
    MAX_INF = int(1e9)
    
    ch = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        ch[a-1].append(b-1)
        ch[b-1].append(a-1)
    
    ans = 0
    for start in range(n):
        dp = [MAX_INF] * n 
        dp[start] = 0
        q = deque([start])
        while q:
            v = q.popleft()
            for u in ch[v]:
                if dp[u] == MAX_INF:
                    dp[u] = dp[v] + 1
                    q.append(u)
        ans += sum(dp)

    
    print(ans // 2)

if __name__ == '__main__':
    main()