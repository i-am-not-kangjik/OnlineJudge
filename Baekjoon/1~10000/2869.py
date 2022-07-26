# 백준 2869번 문제
# 달팽이는 올라가고 싶다
# https://www.acmicpc.net/problem/2869

import sys
import math

def solve():
    A, B, V = map(int, sys.stdin.readline().split())
    days = (V - B) / ( A - B)
    if type(days) == int:
        print(days)
    else:
        print(math.ceil(days))
solve()
