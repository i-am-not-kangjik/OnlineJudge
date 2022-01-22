# 백준 1330번
# 두 정수 A와 B가 주어졌을 때, A와 B를 비교
# https://www.acmicpc.net/problem/1330

a, b = input().split()
a = int(a)
b = int(b)
if a < b:
    print("<")
elif a > b:
    print(">")
elif a == b:
    print("==")
    