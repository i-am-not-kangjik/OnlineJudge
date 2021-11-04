import sys
n = int(sys.stdin.readline())

for i in range(0, n):
    a = ""
    for j in range(n, i+1, -1):
        a += " "
    for k in range(0, i+1):
        a += "*"
    print(a)