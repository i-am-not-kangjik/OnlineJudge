# 백준 2480번 문제
# 주사위 세개
# https://www.acmicpc.net/problem/2480

import sys
def solve():
    a, b, c = map(int, sys.stdin.readline().split()) 
    if a == b == c:
        result = 10000 + (a * 1000)
    elif a == b and b != c:
        result = 1000 + (a * 100)
    elif a != b and b == c:
        result = 1000 + (b * 100)
    elif a == c and b != c:
        result = 1000 + (a * 100)
    elif a != b and b != c:
        result = max(a, b, c) * 100
    print(result)

solve()