# 백준 10773번 문제
# 제로
# https://www.acmicpc.net/problem/10773

import sys
k = int(sys.stdin.readline()) # 입력 받을 수
li = [] # 리스트 초기화
sum = 0 # 합계를 구할 수

for _ in range(k):
    n = int(sys.stdin.readline())
    if n == 0:
        li.pop()
    else:
        li.append(n)
        
if len(li) == 0:
    print(sum)
else:
    for num in li:
        sum += num
    print(sum)
