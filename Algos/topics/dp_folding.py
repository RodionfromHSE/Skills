from dataclasses import dataclass, field
from enum import IntEnum

def relax(dp, p, idx, length, val, word):
    if dp[idx][length] > val:
        dp[idx][length] = val
        p[idx][length] = word

def is_repeated(s, idx, length, piece_len):
    if length % piece_len != 0:
        return False
    piece = s[idx:idx+piece_len]
    for i in range(idx+piece_len, idx+length, piece_len):
        if s[i:i+piece_len] != piece:
            return False
    return True

def main():
    s = input()
    n = len(s)
    dp = [[float('inf') for _ in range(n+1)] for _ in range(n+1)]
    p = [[None for _ in range(n+1)] for _ in range(n+1)]
    if n < 5:
        print(s)
        return
    
    for length in range(5):
        for idx in range(n-length+1):
            relax(dp, p, idx, length, length, s[idx:idx+length])

    for length in range(5, n+1):
        for idx in range(n-length+1):
            relax(dp, p, idx, length, length, s[idx:idx+length])
            for mid in range(1, length):
                relax(dp, p, idx, length, 
                        dp[idx][mid]+dp[idx+mid][length-mid], 
                        p[idx][mid]+p[idx+mid][length-mid])
            for piece_len in range(1, length):
                if is_repeated(s, idx, length, piece_len):
                    relax(dp, p, idx, length, 
                          dp[idx][piece_len]+2+len(str(length//piece_len)), 
                          str(length//piece_len) +'('+p[idx][piece_len]+')')
    
    print(p[0][n])

if __name__ == '__main__':
    main()