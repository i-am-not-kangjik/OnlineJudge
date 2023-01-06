# 백준 11729번 문제
# 하노이 탑 이동 순서
# https://www.acmicpc.net/problem/11729

import sys

def solve(n, a, b, c):    # a 출발, b 남는기둥, c 목적지
    if n == 1:    # 마지막 이동
        print(a, c)
    else:
        solve(n-1, a, c, b)    # n-1을 남는 기둥에 옮기기
        print(a, c)            # n에 해당하는 가장 큰 원판을 옮기기
        solve(n-1, b, a, c)    # 남는 기둥에 옮긴 n-1을 다시 목적지에 옮기기

n = int(sys.stdin.readline())
print(2 ** n -1)    # 실행 횟수는 2의 n승 -1
solve(n, 1, 2, 3)    #n개의 탑을 1에서 3으로 이동
    
    