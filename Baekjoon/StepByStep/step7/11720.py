# 백준 11720번 문제
# N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력
# https://www.acmicpc.net/problem/11720

import sys

def num_sum():
    sum = 0
    times = int(sys.stdin.readline())
    num = sys.stdin.readline()
    for i in range(0, times):
        sum += int(num[i])    
    print(sum)

num_sum()