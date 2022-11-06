# 백준 10872번 문제
# 재귀 팩토리얼
# https://www.acmicpc.net/problem/10872

def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)

import sys

n = int(sys.stdin.readline())
print(factorial(n))