# 백준 2908번 문제
# 상수
# https://www.acmicpc.net/problem/2908

def solve():
    a, b = input().split()
    c, d = "", ""
    for i in range(2, -1, -1):
        c += a[i]
        d += b[i]
    c = int(c)
    d = int(d)
    if c > d:
        print(c)
    else:
        print(d)

solve()
