from dataclasses import dataclass, field
from enum import IntEnum
from collections import defaultdict



def main():
    n, k = map(int, input().split())  # len, min n_unique
    a = list(map(int, input().split()))
    pref = [0] * (n + 1)
    for i in range(n):
        pref[i + 1] = pref[i] + a[i]

    n_unique = 0
    cnt = defaultdict(int)
    ans = -int(1e10)
    l, r = 0, 0
    min_pref = int(1e10)
    while r < n:
        cnt[a[r]] += 1
        if cnt[a[r]] == 1:
            n_unique += 1

        while n_unique >= k:
            cnt[a[l]] -= 1
            if cnt[a[l]] == 0:
                n_unique -= 1
            
            min_pref = min(min_pref, pref[l])
            l += 1

        ans = max(ans, pref[r + 1] - min_pref)
        r += 1

    print(ans)
    
    


if __name__ == '__main__':
    main()