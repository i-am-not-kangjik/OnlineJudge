# 백준 25304번 문제
# 영수증
# https://www.acmicpc.net/problem/25304

import sys

total = int(sys.stdin.readline())
num = int(sys.stdin.readline())
count = 0

for i in range(num):
    a = input()
    b, c = a.split()
    b = int(b)
    c = int(c)
    count += b*c
    
if count == total:
    print('Yes')
else:
    print('No')