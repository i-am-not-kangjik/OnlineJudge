def hansu():
    list = []
    n = int(input())
    if n <= 99:
        print(n)
        
    elif n >= 100:
        for i in range(1, 100):
            list.append(i)
        for i in range(101, n+1):
            a = i // 100
            b = (i // 10) % 10
            c = i % 10
            if a - b == b - c:
                list.append(i)
        print(len(list))
        
hansu()