# 백준 5622번 문제
# 다이얼
# https://www.acmicpc.net/problem/5622

def solve():
    a = input()
    count = 0
    for i in range(0, len(a)):
        b = ord(a[i])
        if b >= 65 and b <= 67:
            count += 3
        elif b >= 68 and b <= 70:
            count += 4
        elif b >= 71 and b <= 73:
            count += 5
        elif b >= 74 and b <= 76:
            count += 6
        elif b >= 77 and b <= 79:
            count += 7
        elif b >= 80 and b <= 83:
            count += 8
        elif b >= 84 and b <= 86:
            count += 9
        elif b >= 87 and b <= 90:
            count += 10
    print(count)

solve()
