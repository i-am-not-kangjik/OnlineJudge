# 백준 2439번 문제
# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
# https://www.acmicpc.net/problem/2439

import sys
n = int(sys.stdin.readline())

for i in range(0, n):
    a = ""
    for j in range(n, i+1, -1):
        a += " "
    for k in range(0, i+1):
        a += "*"
    print(a)
    