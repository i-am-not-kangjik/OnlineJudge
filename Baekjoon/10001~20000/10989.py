# 백준 10989번 문제
# 수 정렬하기 3
# https://www.acmicpc.net/problem/10989
# 계수 정렬 사용

import sys


count_list = [0] * 10000 


t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    count_list[n-1] += 1 # 1일 경우 count_list[0]에 저장
    
for i in range(0, len(count_list)):
    if count_list[i] > 0:
        for j in range (0, count_list[i]):
            print(i+1) 