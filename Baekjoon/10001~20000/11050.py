# 백준 11050번 문제
# 이항 계수 1
# https://www.acmicpc.net/problem/11050

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)

import sys

n, k = map(int, sys.stdin.readline().split())

print(factorial(n) // (factorial(n-k) * factorial(k)))


