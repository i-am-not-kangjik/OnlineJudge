a = int(input())
b = input()
c = b.split()

for i in range(0, a):
    c[i] = int(c[i])

maxc = max(c)
sum = 0

for i in range(0, a):
    c[i] = c[i] / maxc * 100
    sum += c[i]

avg = sum / a
print(avg)
