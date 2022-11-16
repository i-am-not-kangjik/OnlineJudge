# 백준 10866번 문제
# 덱
# https://www.acmicpc.net/problem/10866

import sys
from collections import deque

deq = deque()
n = int(sys.stdin.readline())

for _ in range(n):
    a = sys.stdin.readline().strip()
    if a[:6] == 'push_f':
        b, c = a.split()
        deq.appendleft(c)
    elif a[:6] == 'push_b':
        b, c = a.split()
        deq.append(c)
    elif a[:5] == 'pop_f':
        if len(deq) == 0:
            print('-1')
        else:
            tmp = deq.popleft()
            print(tmp)
    elif a[:5] == 'pop_b':
        if len(deq) == 0:
            print('-1')
        else:
            tmp = deq.pop()
            print(tmp)
    elif a == 'size':
        print(len(deq))
    elif a == 'empty':
        if len(deq) == 0:
            print('1')
        else:
            print('0')
    elif a == 'front':
        if len(deq) == 0:
            print('-1')
        else:
            print(deq[0])
    elif a == 'back':
        if len(deq) == 0:
            print('-1')
        else:
            print(deq[-1])
            