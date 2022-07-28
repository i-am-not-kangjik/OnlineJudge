# 백준 1929번 문제
# 소수 구하기
# https://www.acmicpc.net/problem/1929

import sys

    
def print_prime_list(num1, num2):
    if num1 == 1:
        num1 += 1
    elif num2 == 2:
        print(2)
        return
    for i in range(num1, num2+1):
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break
        else:
            print(i)
    return


def solve():
    a, b = map(int, sys.stdin.readline().split())
    prime_list = print_prime_list(a, b)



solve()
