# 백준 2739번 문제
# N을 입력받은 뒤, 구구단 N단을 출력
# https://www.acmicpc.net/problem/2739

a = int(input())
for i in range(1, 10):
    print(a, "*", i, "=", a * i)
