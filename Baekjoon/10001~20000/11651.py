# 백준 11651번 문제
# 좌표 정렬하기 2
# https://www.acmicpc.net/problem/11651

import sys


t = int(sys.stdin.readline())
li = []

for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    temp_li = [b, a]
    li.append(temp_li)

li.sort()

for item in li:
    print(item[1], item[0])