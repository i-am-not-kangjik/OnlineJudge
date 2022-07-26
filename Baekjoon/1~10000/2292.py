# 백준 2292번 문제
# 벌집
# https://www.acmicpc.net/problem/2292


import sys

def solve():
    a = int(sys.stdin.readline())
    count = 1
    comp = 1
    for i in range(0, 1000000001, 6) :
        comp += i
        if a <= comp:
            print(count)
            return
        else:
            count += 1

solve()
