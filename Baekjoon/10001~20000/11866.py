# 백준 11866번 문제
# 요세푸스 문제 0
# https://www.acmicpc.net/problem/11866

import sys

n, k = map(int, sys.stdin.readline().split())
li = []
for i in range(n):
    li.append(i+1)

tmp_num = k
print('<', end='')

while(len(li) != 0):
    if len(li) == 1:
        tmp = li.pop()
        print('{}>'.format(tmp))
    elif tmp_num <= len(li):
        tmp = li.pop(tmp_num-1)
        print(tmp, end=', ')
        tmp_num = tmp_num + k - 1
    else:
        if tmp_num > len(li):
            while(tmp_num > len(li)):
                tmp_num -= len(li)
        tmp = li.pop(tmp_num-1)
        print(tmp, end=', ')
        tmp_num = tmp_num + k - 1
    
