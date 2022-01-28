# 백준 1193번 문제
# 분수 찾기
# https://www.acmicpc.net/problem/1193

import sys

def solve():
    a = int(sys.stdin.readline())
    line = 0
    count = 0
    while count < a:
        line += 1
        count += line

    diff = count - a

    if line % 2 == 0:
        x = line - diff
        y = diff + 1
    else:
        x = diff + 1
        y = line - diff
    
    print("{0}/{1}".format(x, y))

solve()
