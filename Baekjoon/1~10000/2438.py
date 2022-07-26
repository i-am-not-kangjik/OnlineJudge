# 백준 2438번 문제
# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍기
# https://www.acmicpc.net/problem/2438

import sys
n = int(sys.stdin.readline())

for i in range(0, n):
    print("*" * (i+1))
    