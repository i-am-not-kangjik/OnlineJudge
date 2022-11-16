# 백준 10845번 문제
# 큐
# https://www.acmicpc.net/problem/10845

import sys
from collections import deque


queue = deque()
n = int(sys.stdin.readline())
for _ in range(n):
    a = sys.stdin.readline().strip()
    if a[:4] == 'push':
        b, c = a.split()
        queue.append(c)
    elif a == 'pop':
        if len(queue) == 0:
            print('-1')
        else:
            tmp = queue.popleft()
            print(tmp)
    elif a == 'size':
        print(len(queue))
    elif a == 'empty':
        if len(queue) == 0:
            print('1')
        else:
            print('0')
    elif a == 'front':
        if len(queue) == 0:
            print('-1')
        else:
            print(queue[0])
    elif a == 'back':
        if len(queue) == 0:
            print('-1')
        else:
            print(queue[-1])
            