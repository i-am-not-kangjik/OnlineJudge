# 백준 11022번 문제
# 두 정수 A와 B를 입력받은 다음, A+B를 출력
# https://www.acmicpc.net/problem/11022

import sys
t = int(sys.stdin.readline())

for i in range(1, t+1):
    a, b = map(int, sys.stdin.readline().split())
    print("Case #{0}: {1} + {2} = {3}".format(i, a, b, a+b))

