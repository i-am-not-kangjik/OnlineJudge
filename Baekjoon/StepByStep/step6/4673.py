list = []
for i in range(0, 10001):
    n = i
    if n < 10:
        j = n
        j = j + n
        if j not in list:
            list.append(j)
    elif n > 9 and n < 100:
        j = n
        j = j + (n % 10)
        j = j + (n // 10)
        if j not in list:
            list.append(j)
    elif n > 99 and n < 1000:
        j = n
        j = j + (n // 100)
        j = j + ((n % 100) // 10)
        j = j + (n % 10)
        if j not in list:
            list.append(j)
    elif n > 999 and n < 10000:
        j = n
        j = j + (n // 1000)
        j = j + ((n % 1000) // 100)
        j = j + ((n % 100) // 10)
        j = j + (n % 10)
        if j not in list:
            list.append(j)
            
for i in range(0, 10001):
    if i not in list:
        print(i)