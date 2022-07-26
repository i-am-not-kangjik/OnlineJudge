# 백준 8958번 문제
# OX퀴즈 채점하기
# https://www.acmicpc.net/problem/8958

a = int(input())
test = []
score = []
for i in range(0, a):
    s = input()
    test.append(s)

for i in range(0, a):
    sum = 0
    count = 1
    for j in range(0, len(test[i])):
        if test[i][j] == 'O':
            sum += count
            count += 1
        else:
            count = 1
    score.append(sum)

for i in range(0, len(score)):
    print(score[i])
    