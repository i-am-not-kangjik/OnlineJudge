# 백준 10809번 문제
# 알파벳 찾기
# https://www.acmicpc.net/problem/10809

def find_alpha():
    word = input()
    word_list = []
    list = []
    for i in range(0, len(word)):
        word_list.append(ord(word[i]) - 97)
    
    for i in range(0, 26):
        list.append(int(-1))    

    for i in range(0, len(word_list)):
        if list[word_list[i]] == -1:
            list[word_list[i]] = i
    
    for i in range(0, len(list)-1):
        print(list[i], end = ' ')
    
    print(list[-1])

find_alpha()