a = []
for i in range(0, 9):
    b = int(input())
    a.append(b)

c = max(a)
for i in range(0, 9):
    if a[i] == c:
        print(a[i])
        print(i+1)
        break