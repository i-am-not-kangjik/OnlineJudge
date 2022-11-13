# 백준 2475번 문제
# 검증수
# https://www.acmicpc.net/problem/2475

import sys

li = list(map(int, sys.stdin.readline().split()))
ans = 0

for i in range(len(li)):
    li[i] = li[i] ** 2
    ans += li[i]
    
print(ans%10)