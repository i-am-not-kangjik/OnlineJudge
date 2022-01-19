# 백준 2675번 문제
# 문자열 반복
# https://www.acmicpc.net/problem/2675



import sys

def string_cycle():
    count_list = []
    text_list = []
    times = int(input())

    for i in range(0, times):
        a, b = map(str, sys.stdin.readline().split())
        count_list.append(int(a))
        text_list.append(b)

    for i in range(0, times):
        for j in range(0, len(text_list[i])):
            if j != len(text_list[i]) - 1:
                print(text_list[i][j] * count_list[i], end='')
            else:
                print(text_list[i][j] * count_list[i])

string_cycle()