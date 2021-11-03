import sys
a, b = map(int, sys.stdin.readline().split())
l = list(map(int, input().split()))
for i in range(0, a):
    if l[i] < b:
        print(l[i], end=' ')