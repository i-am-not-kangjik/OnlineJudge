import sys
times = int(sys.stdin.readline())
list = []
for i in range(0, times):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)