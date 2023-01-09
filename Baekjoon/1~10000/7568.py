# 백준 7568번 문제
# 덩치
# https://www.acmicpc.net/problem/7568

import sys

n = int(sys.stdin.readline())
li = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    li.append([x, y])

# 현재 인덱스보다 키와 몸무게 둘 다 큰 것이 있을경우 rank += 1
for i in range(n):
    rank = 1
    for j in range(n):
        if li[j][0] > li[i][0] and li[j][1] > li[i][1]:
            rank += 1
    li[i].append(rank)
    
for item in li:
    print(item[2], end=' ')
        
    