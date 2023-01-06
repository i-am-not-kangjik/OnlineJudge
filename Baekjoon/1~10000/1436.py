# 백준 1436번 문제
# 영화감독 숌
# https://www.acmicpc.net/problem/1436

import sys

n = int(sys.stdin.readline())
count = 0
i = 666

while(True):
    str_i = str(i)
    if '666' in str_i :
        count += 1
    if count == n:
        print(i)
        break
    i += 1