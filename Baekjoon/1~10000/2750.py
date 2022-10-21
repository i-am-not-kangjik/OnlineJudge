# 백준 2750번 문제
# 수 정렬하기
# https://www.acmicpc.net/problem/2750

import sys

cases = int(sys.stdin.readline())
nums = []

for _ in range(cases):
    n = int(sys.stdin.readline())
    nums.append(n)
    
for i in range(0, len(nums)): # 선택정렬
    min_index = i
    for j in range(i+1, len(nums)):
        if nums[min_index] > nums[j]:
            min_index = j
    nums[i], nums[min_index] = nums[min_index], nums[i]

for i in range(0, len(nums)):
    print(nums[i])