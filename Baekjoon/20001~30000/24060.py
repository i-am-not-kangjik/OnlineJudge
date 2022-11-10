# 백준 24060번 문제
# 재귀를 이용한 병합정렬
# https://www.acmicpc.net/problem/24060


def merge_sort(a, p, r):
    if p < r:
        q = int((p + r) / 2)
        merge_sort(a, p, q)
        merge_sort(a, q + 1, r)
        merge(a, p, q, r)
        
def merge(a, p, q, r):
    global count, k, ans
    i = p
    j = q + 1
    tmp = []
    while i <= q and j <= r:
        if a[i] <= a[j]:
            tmp.append(a[i])
            i += 1
        else:
            tmp.append(a[j])
            j += 1
    while i <= q:
        tmp.append(a[i])
        i += 1
    while j <= r:
        tmp.append(a[j])
        j += 1
    i = p
    t = 0
    while i <= r:
        a[i] = tmp[t]
        count += 1
        if count == k:
            ans = a[i]
            break
        i += 1
        t += 1        
        


import sys

ans = -1
count = 0
n, k = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))

merge_sort(li, 0, len(li)-1)

print(ans)