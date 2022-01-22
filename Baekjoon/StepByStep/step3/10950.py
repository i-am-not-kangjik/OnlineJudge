# 백준 10950번 문제
# 두 정수 A와 B를 입력받은 다음, A+B를 출력
# https://www.acmicpc.net/problem/10950

times = int(input())
list = []
for i in range(0, times):
    a, b = input().split()
    a = int(a)
    b = int(b)
    list.append(a+b)

for i in range(0, times):
    print(list[i])
    