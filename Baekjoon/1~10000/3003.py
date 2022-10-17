# 백준 3003번 문제
# 체스말 개수
# https://www.acmicpc.net/problem/3003

import sys
a = [1, 1, 2, 2, 2, 8]
b = sys.stdin.readline().split()
for i in range(0, len(b)):
    b[i] = int(b[i])

for i in range(0, len(a)):
    b[i] = a[i] - b[i]
    print(b[i], end=' ')