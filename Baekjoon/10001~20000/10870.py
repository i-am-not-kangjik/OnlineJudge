# 백준 10870번 문제
# 재귀 피보나치
# https://www.acmicpc.net/problem/10870

def fibo(n):
    if n == 0:
        return 0 
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
    
import sys

n = int(sys.stdin.readline())
print(fibo(n))