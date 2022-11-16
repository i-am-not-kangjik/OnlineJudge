# 백준 1018번 문제
# 체스판 다시 칠하기
# https://www.acmicpc.net/problem/1018

import sys

white_li = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']] * 4
black_li = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']] * 4

n, m = map(int, sys.stdin.readline().split())
chess_li = []
for _ in range(n):
    tmp = list(sys.stdin.readline().strip())
    chess_li.append(tmp)

white_min = 64
blakc_min = 64

for i in range(0, n-7):
    for j in range(0, m-7):
        white_diff = 0 
        black_diff = 0        
        for k in range(0, 8):
            for l in range(0, 8):
                if white_li[k][l] != chess_li[k+i][l+j]:
                    white_diff += 1
                if black_li[k][l] != chess_li[k+i][l+j]:
                    black_diff += 1
        if white_diff < white_min:
            white_min = white_diff
        if black_diff < blakc_min:
            blakc_min = black_diff
            
if blakc_min <= white_min:
    print(blakc_min)
else:
    print(white_min)


