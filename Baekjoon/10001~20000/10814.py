# 백준 10814번 문제
# 나이순 정렬
# https://www.acmicpc.net/problem/10814

import sys

t = int(sys.stdin.readline())
li = []

for _ in range(t):
    a, b = sys.stdin.readline().split()
    li.append([int(a), b])
    
li.sort(key=lambda x : x[0])

for item in li:
    print(item[0], item[1])