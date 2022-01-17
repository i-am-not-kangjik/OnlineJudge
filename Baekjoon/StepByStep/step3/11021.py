# 백준 11021번 문제
# 두 정수 A와 B를 입력받은 다음, A+B를 출력
# https://www.acmicpc.net/problem/11021

import sys
t = int(sys.stdin.readline())
list = []
for i in range(1, t+1):
    a, b = map(int, sys.stdin.readline().split())
    list.append(a+b)

for i in range(0, t):
    print("Case #{0}: {1}".format(i+1, list[i]))