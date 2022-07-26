# 백준 2581번 문제
# 소수
# https://www.acmicpc.net/problem/2581


import sys

    
MAX_NUM = 10000
def make_prime_list(num):
    list = [2]
    for i in range(1, num+1):
        for j in range(2, i):
            if i % j == 0:
                break
            elif j == i-1:
                list.append(i)
    return list


def solve():
    prime_list = make_prime_list(MAX_NUM)
    a = int(sys.stdin.readline())
    b = int(sys.stdin.readline())
    c = []
    for i in range(a, b+1):
        if i in prime_list:
            c.append(i)
    if len(c) == 0:
        print(-1)
    else:
        print(sum(c))
        print(min(c))
    
solve()
