# 백준 4673번 문제
# 셀프 넘버 구하기
# https://www.acmicpc.net/problem/4673

def d(n):
    list = []

    for i in range(0, 10001):
        j = i
        if j < 10:
            k = j
            k = k + j
            if k not in list:
                list.append(k)
        elif j > 9 and j < 100:
            k = j
            k = k + (j % 10)
            k = k + (j // 10)
            if k not in list:
                list.append(k)
        elif j > 99 and j < 1000:
            k = j
            k = k + (j // 100)
            k = k + ((j % 100) // 10)
            k = k + (j % 10)
            if k not in list:
                list.append(k)
        elif j > 999 and j < 10000:
            k = j
            k = k + (j // 1000)
            k = k + ((j % 1000) // 100)
            k = k + ((j % 100) // 10)
            k = k + (j % 10)
            if k not in list:
                list.append(k)
            
    for i in range(0, n+1):
        if i not in list:
            print(i)
            

d(10000)
