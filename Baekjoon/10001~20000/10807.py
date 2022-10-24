# 백준 10807번 문제
# 개수 세기
# https://www.acmicpc.net/problem/10807

import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
target = int(sys.stdin.readline())
count = 0

for num in nums:
    if num == target:
        count += 1

print(count)