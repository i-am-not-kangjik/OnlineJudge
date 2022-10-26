# 백준 2738번 문제
# 행렬 덧셈
# https://www.acmicpc.net/problem/2738

import sys

n, m = map(int, sys.stdin.readline().split())
a, b = [], []

for i in range(n):
    items = list(map(int, sys.stdin.readline().split()))
    a.append(items)
    
for i in range(n):
    items = list(map(int, sys.stdin.readline().split()))
    b.append(items)
    
    
    
for i in range(0, n):
    for j in range(0, m):
        a[i][j] += b[i][j]
        
for i in range(0, n):
    for j in range(0, m):
        if j < m-1:
            print(a[i][j], end=" ")
        else:
            print(a[i][j])
              