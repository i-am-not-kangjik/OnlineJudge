# 백준 1157번 문제
# 가장 많이 사용된 알파벳 찾기
# https://www.acmicpc.net/problem/1157

def solve():
    a = input()
    count_list = [] # 알파벳별 개수
    text_list = [] # 입력받은 문자를 ascii코드로 변환하여 저장
    answer_list = [] # 가장 많은 빈도수를 가진 알파벳을 저장하는 리스트
    for i in range(0, 26):
        count_list.append(0)
    for i in range(0, len(a)):
        text_list.append(ord(a[i]))
    for i in range(0, len(a)):
        if text_list[i] > 96:
            text_list[i] -= 32
        counter = text_list[i] - 65
        count_list[counter] += 1
    max_freq = max(count_list)
    for i in range(0, 26):
        if count_list[i] == max_freq:
            answer_list.append(chr(i+65))

    if len(answer_list) == 1:
        print(answer_list[0])
    else:
        print("?")

solve()