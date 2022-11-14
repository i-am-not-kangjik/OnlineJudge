# 백준 4153번 문제
# 직각삼각형
# https://www.acmicpc.net/problem/4153

def isRight(a, b, c):
    li = [a, b, c]
    li.sort()
    if (li[0] ** 2) + (li[1] ** 2) == (li[2] ** 2):
        print('right')
    else:
        print('wrong')

import sys

while(True):
    a, b, c = map(int,sys.stdin.readline().split())
    if a == 0 and b == 0 and c == 0:
        break
    else:
        isRight(a, b, c)