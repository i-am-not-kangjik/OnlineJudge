a = int(input())
b = int(input())
c = int(input())
d = str(a * b * c)
e = []
count = []

for i in range(0, 10):
    e.append(str(i))

for i in range(0, 10):
    count.append(int(0))

for i in range(0, len(d)):
    for j in range(0,len(e)):
        if d[i] == e[j]:
            count[j] += 1

for i in range(0, len(count)):
    print(count[i])