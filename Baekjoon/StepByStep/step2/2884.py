# 백준 2884번 문제
# 45분 더 일찍 일어나는 알람시계
# https://www.acmicpc.net/problem/2884

a, b = input().split()
a = int(a)
b = int(b)

if(b >= 45):
    b = b - 45
    print(a, b)
elif b < 45:
    if a >= 1:
        a = a - 1
        b = b + 15
        print(a, b)
    elif a == 0:
        a = 23
        b = b + 15
        print(a, b)