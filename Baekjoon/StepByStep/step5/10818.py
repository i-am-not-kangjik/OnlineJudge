# 백준 10818번 문제
# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램
# https://www.acmicpc.net/problem/10818

a = int(input())
b = input().split()
for i in range (0, a):
    b[i] = int(b[i])

print(min(b), max(b))