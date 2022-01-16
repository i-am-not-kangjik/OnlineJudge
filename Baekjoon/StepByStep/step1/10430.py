# 백준 10430번 문제
# 세 수 A, B, C가 주어졌을 때, 나머지 연산을 구하는 프로그램
# https://www.acmicpc.net/problem/10430

a, b, c = input().split()
A = int(a)
B = int(b)
C = int(c)
print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B) % C)
print(((A%C) * (B%C))%C)