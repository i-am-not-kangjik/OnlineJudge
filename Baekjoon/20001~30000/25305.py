# 백준 25305번 문제
# 커트라인
# https://www.acmicpc.net/problem/25305

import sys

n, cutline = map(int, sys.stdin.readline().split())

every = list(map(int, sys.stdin.readline().split()))

every.sort(reverse=True)
print(every[cutline-1])
