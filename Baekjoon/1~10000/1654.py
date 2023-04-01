# 백준 1654번 문제
# 랜선 자르기
# https://www.acmicpc.net/problem/1654

import sys

k, n = map(int, sys.stdin.readline().split())
li = []

for _ in range(k):
    tmp = int(sys.stdin.readline())
    li.append(tmp)
li.sort()

min_n = 1
min_n_2 = 2
max_n = (2e31) - 1

while(True):
    min_count = 0
    min_count2 = 0
    max_count = 0
    for i in range(k):
        min_count += li[i] // min_n
        min_count2 += li[i] // min_n_2
        max_count += li[i] // max_n
    if max_count == n:
        print(max_n)
        break
    elif min_count == n and min_count2 != n:
        print(min_n)
        break
    else:
        min_n += 1
        min_n_2 += 1
        max_n -= 1
        

    