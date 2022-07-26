# 백준 1110번 문제
# 더하기 사이클
# https://www.acmicpc.net/problem/1110

def countCycle(num):
    global count
    global n
    count += 1
    if num < 10:
        a = 0
        b = num
    else:
        a = num // 10
        b = num % 10
    c = a + b
    d = b * 10 + c % 10
    if d == n:
        return
    else:
        countCycle(d)

n = int(input())
count = 0
countCycle(n)
print(count)
