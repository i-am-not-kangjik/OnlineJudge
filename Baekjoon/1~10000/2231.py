# 백준 2231번 문제
# 분해합
# https://www.acmicpc.net/problem/2231

import sys


n = int(sys.stdin.readline())

def solve(n):
    for i in range(1, n+1):
        if i < 10:
            if i + i == n:
                return(i)
        elif i >= 10 and i < 100:
            if i + (i // 10) + (i % 10) == n:
                return(i)
        elif i >= 100 and i < 1000:
            if i + (i // 100) + (i % 100 // 10) + (i % 10) == n:
                return(i)
        elif i >= 1000 and i < 10000:
            if i + (i // 1000) + (i % 1000 // 100) + (i % 100 // 10) + (i % 10) == n:
                return(i)
        elif i >= 10000 and i < 100000:
            if i + (i // 10000) + (i % 10000 // 1000) + (i % 1000 // 100) + (i % 100 // 10) + (i % 10) == n:
                return(i)
        elif i >= 100000 and i < 1000000:
            if i + (i // 100000) + (i % 100000 // 10000) + (i % 10000 // 1000) + (i % 1000 // 100) + (i % 100 // 10) + (i % 10) == n:
                return(i)
        elif i == n:
            return 0
    return 0

print(solve(n))

