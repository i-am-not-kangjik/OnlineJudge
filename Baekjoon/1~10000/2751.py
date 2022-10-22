# 백준 2751번 문제
# 수 정렬하기 2
# https://www.acmicpc.net/problem/2751

import sys

cases = int(sys.stdin.readline())
nums = []

for _ in range(cases):
    n = int(sys.stdin.readline())
    nums.append(n)
    
nums.sort()

for i in range(0, len(nums)):
    print(nums[i])