# 백준 10871번 문제
# 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력
# https://www.acmicpc.net/problem/10871

import sys
a, b = map(int, sys.stdin.readline().split())
l = list(map(int, input().split()))
for i in range(0, a):
    if l[i] < b:
        print(l[i], end=' ')