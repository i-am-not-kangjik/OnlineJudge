# 백준 2609번 문제
# 최대공약수와 최소공배수
# https://www.acmicpc.net/problem/2609

import sys

a, b = map(int,sys.stdin.readline().split())

if a < b:
    a, b = b, a

for i in range(1, b + 1):
    if a % i == 0 and b % i == 0:
        max = i

if a % b == 0:
    min = a
else:
    for i in range(1, a * b + 1):
        tmp = b * i
        if tmp % a == 0:
            min = tmp
            break
    

print(max)
print(min)