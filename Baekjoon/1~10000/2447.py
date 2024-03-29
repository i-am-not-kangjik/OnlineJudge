# 백준 2447번 문제
# 재귀를 이용한 별 찍기
# https://www.acmicpc.net/problem/2447

def make_star(n):
    global ans
    
    if n == 3:
        ans[0][:3], ans[2][:3] = ['*', '*', '*'], ['*', '*', '*']
        ans[1][:3] = ['*', ' ', '*']
        return
    a = n//3
    make_star(a)
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            for k in range(a):
                ans[a*i+k][a*j:a*j+a] = ans[k][0:a]

import sys

n = int(sys.stdin.readline())

ans = [[' ' for i in range(n)] for i in range(n)]

make_star(n)

for i in ans:
    for j in i:
        print(j, end='')
    print('')


# n이 9일때(a가 3일때) 
# ans[0][0:3] = ans[0][0:3] 부터
# ans[1][0:3] = ans[1][0:3]
# ans[2][0:3] = ans[2][0:3]
# ans[0][3:6] = ans[0][0:3]
# ans[1][3:6] = ans[1][0:3]
# ans[2][3:6] = ans[2][0:3]
# ans[0][6:9] = ans[0][0:3]
# ans[1][6:9] = ans[1][0:3]
# ans[2][6:9] = ans[2][0:3]
# ans[3][0:3] = ans[0][0:3]
# ans[4][0:3] = ans[1][0:3]
# ans[5][0:3] = ans[2][0:3]

# 1
# *

# 3
# ***
# * *
# ***

# 9
# *********
# * ** ** *
# *********
# ***   ***
# * *   * *
# ***   ***
# *********
# * ** ** *
# *********

# 27
# ***************************
# * ** ** ** ** ** ** ** ** *
# ***************************
# ***   ******   ******   ***
# * *   * ** *   * ** *   * *
# ***   ******   ******   ***
# ***************************
# * ** ** ** ** ** ** ** ** *
# ***************************
# *********         *********
# * ** ** *         * ** ** *
# *********         *********
# ***   ***         ***   ***
# * *   * *         * *   * *
# ***   ***         ***   ***
# *********         *********
# * ** ** *         * ** ** *
# *********         *********
# ***************************
# * ** ** ** ** ** ** ** ** *
# ***************************
# ***   ******   ******   ***
# * *   * ** *   * ** *   * *
# ***   ******   ******   ***
# ***************************
# * ** ** ** ** ** ** ** ** *
# ***************************

# 81
# ******
# *    *
# *    *
# *    *
# *    *
# ******