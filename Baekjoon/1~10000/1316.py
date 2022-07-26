# 백준 1316번 문제
# 그룹 단어 체커
# https://www.acmicpc.net/problem/1316

def group_check(a):
    if len(a) == 2:
        return True
    else:
        for i in range(0, len(a)):
            for j in range(len(a)-1, i+1, -1):
                if a[i+1] != a[i] and a[i] == a[j]:
                    return False
    return True

def solve():
    words = []
    num = int(input())
    count = 0
    for i in range(0, num):
        word = input()
        words.append(word)

    for i in range(0, len(words)):
        if group_check(words[i]):
            count += 1
    print(count)

solve()
