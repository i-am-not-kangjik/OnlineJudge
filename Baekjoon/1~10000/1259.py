# 백준 1259번 문제
# 팰린드롬수
# https://www.acmicpc.net/problem/1259

def isPalin(n):
    n = str(n)
    mid = len(n) // 2
    for i in range(0, mid):
        if n[i] != n[-i-1]:
            print('no')
            return
    print('yes')
                

import sys

while(True):
    n = int(sys.stdin.readline())
    if n == 0:
        break
    else:
        isPalin(n)
        