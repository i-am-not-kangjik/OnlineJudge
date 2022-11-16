# 백준 10828번 문제
# 스택
# https://www.acmicpc.net/problem/10828

import sys
from collections import deque


stack = deque()
n = int(sys.stdin.readline())
for _ in range(n):
    a = sys.stdin.readline().strip()
    if a[:4] == 'push':
        b, c = a.split()
        stack.appendleft(c)
    elif a == 'pop':
        if len(stack) == 0:
            print('-1')
        else:
            tmp = stack.popleft()
            print(tmp)
    elif a == 'size':
        print(len(stack))
    elif a == 'empty':
        if len(stack) == 0:
            print('1')
        else:
            print('0')
    elif a == 'top':
        if len(stack) == 0:
            print('-1')
        else:
            print(stack[0])
            