# 백준 4949번 문제
# 균형잡힌 세상
# https://www.acmicpc.net/problem/4949

import sys

while(True):
    sentence = sys.stdin.readline().rstrip()    # 개행 문자 제거
    if sentence == ".":
        break
    else:
        s1 = []
        validation = True    # 유효성
        for i in range(len(sentence)):
            if sentence[i] == "(":
                s1.append(sentence[i])
            elif sentence[i] == ")":
                if len(s1) != 0 and s1[-1] == "(":    # 스택이 비어있지 않으며, 마지막 요소가 같은 괄호인지 판별
                    s1.pop()
                else:
                    validation = False
                    s1.append(sentence[i])
            elif sentence[i] == "[":
                s1.append(sentence[i])
            elif sentence[i] == "]":
                if len(s1) != 0 and s1[-1] == "[": # 스택이 비어있지 않으며, 마지막 요소가 같은 괄호인지 판별
                    s1.pop()
                else:
                    validation = False
                    s1.append(sentence[i]) 
        if validation == True and len(s1) == 0:
            print("yes")
        else:
            print("no")
