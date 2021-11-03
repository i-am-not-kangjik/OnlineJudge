times = int(input())
list = []
for i in range(0, times):
    a, b = input().split()
    a = int(a)
    b = int(b)
    list.append(a+b)

for i in range(0, times):
    print(list[i])