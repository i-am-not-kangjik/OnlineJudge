# 백준 2587번 문제
# 대표값2
# https://www.acmicpc.net/problem/2587

import sys

nums = []
sum = 0

for _ in range(5):
    n = int(sys.stdin.readline())
    nums.append(n)
    sum += n    

nums.sort()
print(int(sum/5))
print(nums[2])
