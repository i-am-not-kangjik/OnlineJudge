# 백준 10816번 문제
# 숫자 카드 2
# https://www.acmicpc.net/problem/10816

import sys
from collections import Counter


n = int(sys.stdin.readline())
n_li = list(map(int, sys.stdin.readline().split())) # N개의 수를 담은 리스트
m = int(sys.stdin.readline())
m_li = list(map(int, sys.stdin.readline().split())) # M개의 수를 담은 리스트
# 탐색에 용이하게 정렬
# n_li = sorted(n_li) 

# n_li의 원소와, 그 원소의 개수를 맵핑
# dic = {n_li[i] : n_li.count(n_li[i]) for i in range(len(n_li))} 
dic = Counter(n_li)

for i in range(len(m_li)):
    if m_li[i] in dic:
        if i != len(m_li) - 1:
            print(dic[m_li[i]], end=' ')
        else:
            print(dic[m_li[i]])
    else:
        if i != len(m_li) -1:
            print('0', end=' ')
        else:
            print('0')

