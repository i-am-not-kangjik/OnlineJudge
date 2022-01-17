# 백준 15596번 문제
# 정수 n개의 합을 구하는 함수
# https://www.acmicpc.net/problem/15596

def solve(a):
    sum = 0
    for i in range(0, len(a)):
        sum += a[i]
    return sum
    