a = []
for i in range(0, 10):
    b = int(input())
    a.append(b)
count = 1
comp = []
comp.append(a[0] % 42)

for i in range(1, 10):
    for j in range(0, len(comp)):
        if a[i] % 42 != comp[j] and a[i] % 42 not in comp:
            count += 1
            comp.append(a[i] % 42)

print(len(comp))