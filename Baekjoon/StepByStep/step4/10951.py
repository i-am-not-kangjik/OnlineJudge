# 백준 10951번 문제
# 두 정수 A와 B를 입력받은 다음, A+B를 출력
# https://www.acmicpc.net/problem/10951

while True:
    try:
        A, B = map(int, input().split())
        print(A+B)
    except EOFError:
        break