from dataclasses import dataclass, field
from enum import IntEnum
from collections import defaultdict



def main():
    n, k = map(int, input().split())  # len, min n_units
    a = list(map(int, input().split()))
    
    l1, l2, r = -1, 0, 0
    n_units = a[0]
    while n_units < 1:
        l2 += 1
        r += 1
        n_units += a[r]

    while n_units < k:
        r += 1
        n_units += a[r]
        

    ans = 0
    print("setup", l1, l2, r, n_units, l2 - l1)
    while r < n:
        ans += (l2 - l1) 
        r += 1

        if r == n:
            break
        if a[r] == 1:
            l1 = l2
            l2 += 1
            while a[l2] == 0:
                l2 += 1

    print(ans)  # amount of subarrays containing at least k units
        
    
    


if __name__ == '__main__':
    main()