# 백준 10816번 문제
# 숫자 카드 2
# https://www.acmicpc.net/problem/10816

import sys
from collections import Counter


n = int(sys.stdin.readline())
n_li = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
m_li = list(map(int, sys.stdin.readline().split()))
# n_li = sorted(n_li)

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

