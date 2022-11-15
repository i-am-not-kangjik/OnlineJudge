# 백준 2798번 문제
# 블랙잭
# https://www.acmicpc.net/problem/2798

import sys

n, target = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))
li.sort()
ans = 0

for i in range(0, n-2):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if li[i] + li[j] + li[k] == target:
                ans = target
                break
            elif li[i] + li[j] + li[k] < target and li[i] + li[j] + li[k] > ans:
                ans = li[i] + li[j] + li[k]
            elif li[i] + li[j] + li[k] > target:
                continue
            
print(ans)