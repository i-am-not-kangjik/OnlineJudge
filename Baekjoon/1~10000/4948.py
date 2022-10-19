# 백준 4948번 문제
# 베르트랑 공준
# https://www.acmicpc.net/problem/4948

import sys

def countPrime(num):
    count = 0
    for i in primeList:
        if i > n and i <= 2 * n:
            count+=1
    return count

primeList = []
for i in range(2, (123456*2) + 1):
    if i < 4:
        primeList.append(i)
        continue
    for j in range(2, int(i**0.5) +1):
        if i% j == 0:
            break
        elif j == int(i**0.5):
            primeList.append(i)


                

while(True):
    n = int(sys.stdin.readline())
    if n == 0:
        break
    else:
        print(countPrime(n))
