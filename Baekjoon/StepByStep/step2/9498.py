# 백준 9498번 문제
# 시험 점수를 입력받아 등급을 출력
# https://www.acmicpc.net/problem/9498

score = int(input())
if score > 89 and score < 101:
    print("A")
elif score > 79 and score < 90:
    print("B")
elif score > 69 and score < 80:
    print("C")
elif score > 59 and score < 70:
    print("D")
else:
    print("F")
    