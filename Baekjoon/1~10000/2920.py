# 백준 2920번 문제
# 음계
# https://www.acmicpc.net/problem/2920

import sys
li = list(map(int, sys.stdin.readline().split()))

# print(li)

if li == sorted(li):
    print('ascending')
elif li == sorted(li, reverse=True):
    print('descending')
else:
    print('mixed')