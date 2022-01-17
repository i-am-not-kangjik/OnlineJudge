# 백준 8393번 문제
# n이 주어졌을 때, 1부터 n까지 합을 구하기
# https://www.acmicpc.net/problem/8393

n = int(input())
sum = 0
for i in range(1, n + 1):
    sum += i
print(sum)