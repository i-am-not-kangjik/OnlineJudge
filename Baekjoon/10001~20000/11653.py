# 백분 11653번 문제
# 소인수분해
# https://www.acmicpc.net/problem/11653

import sys



def solve():
    n = int(sys.stdin.readline())
    a = []


    while(n != 1):
        for i in range(2, n+1):
            if n % i == 0:
                a.append(i)
                n = int(n / i)
                break
    for i in range(0, len(a)):
        print(a[i])

solve()