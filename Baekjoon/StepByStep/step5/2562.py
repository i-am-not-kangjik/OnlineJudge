# 백준 2562번 문제
# 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램
# https://www.acmicpc.net/problem/2562

a = []
for i in range(0, 9):
    b = int(input())
    a.append(b)

c = max(a)
for i in range(0, 9):
    if a[i] == c:
        print(a[i])
        print(i+1)
        break
    