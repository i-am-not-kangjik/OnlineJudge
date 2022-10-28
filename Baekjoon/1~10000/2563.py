# 백준 2563번 문제
# 색종이
# https://www.acmicpc.net/problem/2563

def black(x, y):
    global white
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            if white[i][j] == 0:
                white[i][j] += 1
        
        



import sys

white = [[0] * 101 for _ in range(101)] # 0으로 채워진 2차원 배열 초기화

t = int(sys.stdin.readline())
for _ in range(t):
    x, y = map(int, sys.stdin.readline().split())
    black(x, y)

cnt = 0

for i in range(0, 101):
    for j in range(0, 101):
        if white[i][j] == 1:
            cnt += 1
print(cnt)