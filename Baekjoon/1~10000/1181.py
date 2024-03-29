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

# li.sort() # 사전 순 정렬
# li.sort(key=len) # 길이가 짧은 것 부터

li.sort(key = lambda x : (len(x), x)) # 길이가 짧은 순, 길이가 같으면 사전순 정렬하는 Lambda식 표현


for item in li:
    print(item)