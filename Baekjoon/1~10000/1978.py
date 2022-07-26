# 백준 1978번 문제
# 소수 찾기
# https://www.acmicpc.net/problem/1978

import sys

    
MAX_NUM = 1000
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
    count = 0
    
    n = int(sys.stdin.readline())
    a = sys.stdin.readline().split()
    for i in range(0, n):
        if int(a[i]) in prime_list:
            count +=1
    
    print(count)
    
solve()

