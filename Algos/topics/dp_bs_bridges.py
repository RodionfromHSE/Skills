from dataclasses import dataclass, field
from enum import IntEnum

def check_width(width):
    # (n, x, y)
    dp = [[[-int(10e9)] * (y + 1) for _ in range(x + 1)] for _ in range(n + 1)]
    dp[0][0][0] = 0
    for ln in range(n):
        for x_take in range(x + 1):
            for y_take in range(y + 1):
                state = dp[ln][x_take][y_take]
                if state < 0:
                    continue
                if x_take < x:
                    if state + a >= width:
                        dp[ln + 1][x_take + 1][y_take] = 0
                    dp[ln][x_take + 1][y_take] = state + a
                if y_take < y:
                    if state + b >= width:
                        dp[ln + 1][x_take][y_take + 1] = 0
                    dp[ln][x_take][y_take + 1] = state + b
    return dp[n][x][y] >= 0

def main():
    global x, a, y, b, n
    x, a, y, b, n = map(int, input().split())
    left, right = 0, 10 ** 6 + 1
    while right - left > 1:
        mid = (left + right) // 2
        if check_width(mid):
            left = mid
        else:
            right = mid
    print(left)
    


if __name__ == '__main__':
    main()