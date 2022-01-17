# 백준 10952번 문제
# 두 정수 A와 B를 입력받은 다음, A+B를 출력
# https://www.acmicpc.net/problem/10952

import sys
while(True):
    a, b = map(int, sys.stdin.readline().split())
    if a == 0 and b == 0:
        break
    else:
        print(a+b)