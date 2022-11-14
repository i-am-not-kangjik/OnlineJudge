# 백준 1085번 문제
# 직사각형에서 탈출
# https://www.acmicpc.net/problem/1085

import sys

x, y, w, h = map(int, sys.stdin.readline().split())

li = []
li.append(x - 0)
li.append(y - 0)
li.append(w - x)
li.append(h - y)

print(min(li))