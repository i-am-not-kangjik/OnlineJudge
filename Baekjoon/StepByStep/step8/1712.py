# 백준 1712번 문제
# 손익분기점
# https://www.acmicpc.net/problem/1712

import sys


def solve():
    a, b, c  = map(int, sys.stdin.readline().split())
    count = 0
    if b >= c:
        print(-1)
    else:
        d = c - b
        e = int(a / d + 1)
        print(e)

solve()
