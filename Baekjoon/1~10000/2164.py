# 백준 2164번 문제
# 카드 2
# https://www.acmicpc.net/problem/2164

import sys
from collections import deque


n = int(sys.stdin.readline())
li = [x + 1 for x in range(n)]
deq = deque(li)
count = 1

while(True):
    if len(deq) == 1:
        tmp = deq.pop()
        print(tmp)
        break
    if count % 2 == 1:
        deq.popleft()
        count += 1
        continue
    elif count % 2 == 0:
        tmp = deq.popleft()
        deq.append(tmp)
        count += 1
        continue