# 백준 2588번 문제
# 세 자리 자연수의 곱셈 과정 출력하기
# https://www.acmicpc.net/problem/2588

a = input()
b = input()
A = int(a)
third = A * int(b[2])
print(third)
fourth = A * int(b[1])
print(fourth)
fifth = A * int(b[0])
print(fifth)
sixth = third + fourth * 10 + fifth * 100
print(sixth)
