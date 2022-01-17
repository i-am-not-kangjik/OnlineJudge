# 백준 3052번 문제
# 수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램
# https://www.acmicpc.net/problem/3052

a = []
for i in range(0, 10):
    b = int(input())
    a.append(b)
count = 1
comp = []
comp.append(a[0] % 42)

for i in range(1, 10):
    for j in range(0, len(comp)):
        if a[i] % 42 != comp[j] and a[i] % 42 not in comp:
            count += 1
            comp.append(a[i] % 42)

print(len(comp))