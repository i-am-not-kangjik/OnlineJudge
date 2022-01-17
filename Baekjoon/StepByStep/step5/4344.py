# 백준 4344번 문제
# 평균 구하기
# https://www.acmicpc.net/problem/4344

a = int(input())
list = []
for i in range(0, a):
    b = input()
    b = b.split()
    list.append(b)
avg = []
for i in range(0, a):
    for j in range(0, len(list[i])):
        list[i][j] = int(list[i][j])

for i in range(0, a):
    sum = 0
    for j in range(1, len(list[i])):
        sum += list[i][j]
    avg.append(sum/list[i][0])
percentage = []

for i in range(0, a):
    count = 0
    for j in range(1, len(list[i])):
        if list[i][j] > avg[i]:
            count += 1
    percentage.append(count/list[i][0])

for i in range(0, len(percentage)):
    percentage[i] = percentage[i] * 100

for i in range(0, a):
    print("%0.3f%%" % percentage[i] )
