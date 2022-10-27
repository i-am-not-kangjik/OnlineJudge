# 백준 2566번 문제
# 2차원 배열에서 최댓값 찾기
# https://www.acmicpc.net/problem/2566

import sys

a = []
for _ in range(9):
    b = list(map(int, sys.stdin.readline().split()))
    a.append(b)


max_x = 1
max_y = 1
max_xy = 0
for i in range(0, len(a)):
    if max_xy < max(a[i]):
        max_xy = max(a[i])
        max_x = i+1
        max_y = a[i].index(max(a[i])) + 1
print(max_xy)
print(max_x, max_y)