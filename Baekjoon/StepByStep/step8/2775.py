# 백준 2775번 문제
# 부녀회장이 될테야
# https://www.acmicpc.net/problem/2775

import sys
sys.setrecursionlimit

def answer(n):
    if n >= 0 and n <= 14:
        return n
    elif n % 14 == 1:
        return 1
    else:
        return answer(n - 1) + answer(n - 14)

def solve():
    times = int(sys.stdin.readline())
    for i in range(0, times):
        k = int(sys.stdin.readline())
        n = int(sys.stdin.readline())
        if n == 1:
            print(n)
        else:
            print(answer((k * 14) + n))
    

solve()
