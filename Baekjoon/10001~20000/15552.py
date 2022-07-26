# 백준 15552번 문제
# 빠른 A+B
# https://www.acmicpc.net/problem/15552

import sys
times = int(sys.stdin.readline())
list = []
for i in range(0, times):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)
    