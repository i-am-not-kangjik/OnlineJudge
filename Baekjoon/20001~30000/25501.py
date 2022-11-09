# 백준 25501번 문제
# 재귀의 귀재
# https://www.acmicpc.net/problem/25501

def recursion(s, l, r):
    global count
    count += 1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    global count
    count = 0
    return recursion(s, 0, len(s)-1)


import sys

t = int(sys.stdin.readline())
li = []

for _ in range(t):
    sentence = sys.stdin.readline().rstrip()
    li.append(sentence)

for item in li:
    print(isPalindrome(item), count)
