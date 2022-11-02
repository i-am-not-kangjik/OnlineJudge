# 백준 11650번 문제
# 좌표 정렬하기
# https://www.acmicpc.net/problem/11650

import sys

t = int(sys.stdin.readline())
li = []

for _ in range(t):
    xy = list(map(int, sys.stdin.readline().split()))
    li.append(xy)


li.sort()    
for item in li:
    print(item[0], item[1])