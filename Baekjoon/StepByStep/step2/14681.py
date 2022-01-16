# 백준 14681번 문제
# 좌표를 입력받아 어느 사분면에 속하는지 출력
# https://www.acmicpc.net/problem/14681

x = int(input())
y = int(input())
if x > 0 and y > 0:
    print("1")
elif x < 0 and y > 0:
    print("2")
elif x < 0 and y < 0:
    print("3")
elif x > 0 and y < 0:
    print("4")
