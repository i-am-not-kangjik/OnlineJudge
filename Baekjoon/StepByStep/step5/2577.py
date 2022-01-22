# 백준 2577번 문제
# 세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램
# https://www.acmicpc.net/problem/2577

a = int(input())
b = int(input())
c = int(input())
d = str(a * b * c)
e = []
count = []

for i in range(0, 10):
    e.append(str(i))

for i in range(0, 10):
    count.append(int(0))

for i in range(0, len(d)):
    for j in range(0,len(e)):
        if d[i] == e[j]:
            count[j] += 1

for i in range(0, len(count)):
    print(count[i])
    