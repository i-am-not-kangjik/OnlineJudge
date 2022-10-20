# 백준 9020번 문제
# 골드바흐의 추측
# https://www.acmicpc.net/problem/9020

import sys


def solve(n):
    c = 10000
    for i in primeList:
        if i >= int(n/2) and i < n:
            if int(n/2) in primeList:
                a = int(n/2)
                b = int(n/2)
                print(a, b)
                return
            elif n-i in primeList and abs((n - i) - i) < c:
                a = n - i
                b = i
                c = abs((n - i) - i)
    print(a, b)  
                
                
            
primeList = []

for i in range(2, 10000):
    if i < 4:
        primeList.append(i)
        continue
    for j in range(2, int(i ** 0.5)+ 1):
        if i % j == 0:
            break
        if j == int(i ** 0.5):
            primeList.append(i)


t = int(sys.stdin.readline()) 
               
for _ in range(t):
    n = int(sys.stdin.readline())
    solve(n)

    
""" for i in range(0, len(primeList)):
        if n / 2 in primeList:
            print(int(n/2), int(n/2))
            return
        elif n - primeList[i] in primeList:
            if abs(primeList[i] - (n - primeList[i])) < c:
                a = primeList[i]
                b = n - primeList[i]
                c = abs(primeList[i] - (n - primeList[i]))
        elif int(primeList[i]) > n / 2:
            print(a,b)
            return """        