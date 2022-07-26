# 백준 10250번 문제
# ACM 호텔
# https://www.acmicpc.net/problem/10250

import sys

def solve():
    people = int(sys.stdin.readline())
    info = []
    for i in range(0, people):
        H, W, N = map(int, sys.stdin.readline().split())
        if H == 1:
            floor = H * 100
            number = N
            info.append(floor + number)
        elif N % H == 0:
            floor = H * 100
            number = int(N / H)
            info.append(floor + number)
        else:
            floor = (N % H) * 100
            number = (N // H) + 1
            info.append(floor + number)
    for i in range(0, people):
        print(info[i])

solve()
