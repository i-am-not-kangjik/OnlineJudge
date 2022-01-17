# 백준 2742번 문제
# 자연수 N이 주어졌을 때, N부터 1까지 한 줄에 하나씩 출력
# https://www.acmicpc.net/problem/2742

import sys
n = int(sys.stdin.readline())
for i in range(n, 0, -1):
    print(i)