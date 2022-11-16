# 백준 1920번 문제
# 수 찾기
# https://www.acmicpc.net/problem/1920

def binarySearch(l, r, li, target):
    if l > r:
        print('0')
        return
    mid = (l + r) // 2
    if li[mid] == target:
        print('1')
        return
    elif li[mid] > target:
        binarySearch(l, mid-1, li, target)
    elif li[mid] < target:
        binarySearch(mid+1, r, li, target)

import sys

sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))

a = sorted(a)

for item in b:
    binarySearch(0, len(a)-1, a, item)