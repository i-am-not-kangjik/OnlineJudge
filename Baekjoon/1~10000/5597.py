# 백준 5597번 문제
# 과제 안 내신 사람 찾기
# https://www.acmicpc.net/problem/5597

import sys

student_list = [0] * 30
for _ in range(28):
    n = int(sys.stdin.readline())
    student_list[n-1] += 1

for i in range(0, len(student_list)):
    if student_list[i] == 0:
        print(i+1)
        
