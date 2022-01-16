# 백준 2753번 문제
# 연도가 주어졌을 때, 윤년이면 1, 아니면 0을 출력
# https://www.acmicpc.net/problem/2753

a = int(input())
if a % 400 == 0:
    print(1)
elif a % 4 == 0 and a % 100 != 0:
    print(1)
else:
    print(0)