# 백준 1181번 문제
# 단어 정렬
# https://www.acmicpc.net/problem/1181

import sys

t = int(sys.stdin.readline())
li = []
li = set(li)

for _ in range(t):
    word = sys.stdin.readline().rstrip()
    li.add(word)
    
li = list(li)

li.sort() # 사전 순 정렬
li.sort(key=len) # 길이가 짧은 것 부터


for item in li:
    print(item)