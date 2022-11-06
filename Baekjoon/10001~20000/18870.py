# 백준 18870번 문제
# 좌표 압축
# https://www.acmicpc.net/problem/18870



# li = [1000, 999, 1000, 999, 1000. 999]
# print("li = ", li)

# li_set = set(li) # li를 집합으로 만들어서 중복 제거
# print("li_set = ",li_set)

# li_set_li = list(li_set) # li를 다시 리스트로
# print("li_set_li = ",li_set_li)

# li_set_li_sorted = sorted(li_set_li) # li를 정렬
# print("li_set_li_sorted = ",li_set_li_sorted)

# dic = {li_set_li_sorted[i] : i for i in range(len(li_set_li_sorted))} # li를 인덱스 맵핑한 딕셔너리
# print('dic = ', dic)   

import sys

t = int(sys.stdin.readline())

li = list(map(int, sys.stdin.readline().split()))

li2 = sorted(list(set(li)))

dic = {li2[i] : i for i in range(len(li2))}

for i in li:
    print(dic[i], end = ' ')    