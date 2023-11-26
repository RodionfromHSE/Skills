from dataclasses import dataclass, field
from collections import defaultdict
import heapq

@dataclass
class Element:
    w: int
    p: int

    def __lt__(self, other):
        return self.w + self.p < other.w + other.p


def main():
    n = int(input())
    els = []
    for _ in range(n):
        w, p = map(int, input().split())
        els.append(Element(w, p))
    els.sort()
    
    MAX_INF = int(1e9)
    dp = [[MAX_INF] * (n + 1) for _ in range(n + 1)]

    for viewed in range(n + 1):
        dp[viewed][0] = 0

    for viewed in range(1, n + 1):
        for taken in range(1, viewed + 1):
            if els[viewed - 1].p >= dp[viewed - 1][taken - 1]:
                dp[viewed][taken] = min(dp[viewed][taken], dp[viewed - 1][taken - 1] + els[viewed - 1].w)
    
    for taken in range(n, -1, -1):
        if dp[n][taken] != MAX_INF:
            print(taken)
            break
    
    

if __name__ == '__main__':
    main()
