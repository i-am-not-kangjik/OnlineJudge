# 백준 1546번 문제
# 세준이의 성적 조작하기
# https://www.acmicpc.net/problem/1546

a = int(input())
b = input()
c = b.split()

for i in range(0, a):
    c[i] = int(c[i])

maxc = max(c)
sum = 0

for i in range(0, a):
    c[i] = c[i] / maxc * 100
    sum += c[i]

avg = sum / a
print(avg)
