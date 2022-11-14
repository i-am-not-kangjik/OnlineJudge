# 백준 15829번 문제
# hashing
# https://www.acmicpc.net/problem/15829

import sys
n = int(sys.stdin.readline())
sentence = sys.stdin.readline()

li = []

for i in range(n):
    li.append(ord(sentence[i]) - 96)



for i in range(n):
    li[i] = li[i] * (31 ** i)
    
result = sum(li) % 1234567891
print(result)