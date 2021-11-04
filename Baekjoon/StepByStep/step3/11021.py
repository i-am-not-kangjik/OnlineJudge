import sys
t = int(sys.stdin.readline())
list = []
for i in range(1, t+1):
    a, b = map(int, sys.stdin.readline().split())
    list.append(a+b)

for i in range(0, t):
    print("Case #{0}: {1}".format(i+1, list[i]))