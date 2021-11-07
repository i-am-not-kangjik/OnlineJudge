a = int(input())
b = input().split()
for i in range (0, a):
    b[i] = int(b[i])

print(min(b), max(b))