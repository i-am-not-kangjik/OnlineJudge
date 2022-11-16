# 백준 9012번 문제
# 괄호
# https://www.acmicpc.net/problem/9012

def isPS(str):
    deq = deque()
    for i in range(len(str)):
        if str[i] == '(':
            deq.append(1)
        elif str[i] == ')':
            if len(deq) >= 1:
                deq.pop()
            else:
                print('NO')
                return
    if len(deq) == 0:
        print('YES')
    else:
        print('NO')

import sys
from collections import deque

n = int(sys.stdin.readline())
li = []

for _ in range(n):
    tmp = sys.stdin.readline().rstrip()
    li.append(tmp)

for i in range(n):
    isPS(li[i])