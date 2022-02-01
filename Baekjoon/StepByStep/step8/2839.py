# 백준 2839번 문제
# 설탕 배달
# https://www.acmicpc.net/problem/2839

import sys

def solve():
    n = int(sys.stdin.readline())
    count = 0
    while n >= 0:
        if n % 5 == 0:
            count += int(n / 5)
            print(count)
            return
        n -= 3
        count += 1
    else:
        print(-1)

solve()
