# 백준 1427번 문제
# 소트인사이드
# https://www.acmicpc.net/problem/1427

import sys

str = list(sys.stdin.readline().rstrip())
str.sort(reverse=True)

for n in str:
    print(n, end='')