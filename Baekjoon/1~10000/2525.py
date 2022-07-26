# 백준 2525번 문제
# 오븐 시계
# https://www.acmicpc.net/problem/2525

import sys

def solve():
    a, b = map(int, sys.stdin.readline().split())
    c = int(sys.stdin.readline())

    b += c
    while(b >= 60):
        a += 1
        b -= 60
    
    if a >= 24:
        a -= 24
    print(a, b)
solve()