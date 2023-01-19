# 백준 1966번 문제
# 프린터 큐
# https://www.acmicpc.net/problem/1966

import sys

k = int(sys.stdin.readline())

for _ in range(k):
    length, position = map(int, sys.stdin.readline().split())    # length 는 길이, position은 target의 위치
    rank_li = list(map(int, sys.stdin.readline().split()))       
    if length == 1:    # 길이가 1 이면 첫번째로 출력
        print("1")
    else:
        count = 0
        for i in range(length):    # 이중 리스트로 target이면 [중요도, True], 아니면 [중요도, False]로 변환 
            if i == position:    
                rank_li[i] = [rank_li[i], True]
            else:
                rank_li[i] = [rank_li[i], False]
        while(True):
            if(max(rank_li)[0] == rank_li[0][0] and rank_li[0][1] == True):    # 중요도가 제일 높으면서 target인 경우 
                count += 1
                print(count)
                break
            elif(max(rank_li)[0] == rank_li[0][0] and rank_li[0][1] == False):    # 중요도가 제일 높지만 target이 아닌 경우
                rank_li.pop(0)
                count += 1
            else:
                rank_li.append(rank_li.pop(0))    # 인덱스 0의 값을 맨 뒤로 이동
            
        
        
# 6 0
# 1 1 9 1 1 1 -> 9 1 1 1 1 1
# 6 - 0 - 1 = 5

# 6 3
# 1 1 9 1 1 1 -> 9 1 1 1 1 1
# 6 - 3 - 1 = 2

# 6 3
# 1 2 9 2 1 1 -> 9 2 2 1 1 1

# a.append(a.pop(0))
