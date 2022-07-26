# 백준 2941번 문제
# 크로아티아 알파벳
# https://www.acmicpc.net/problem/2941

def solve():
    count = 0
    croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
    input_string = input()
    a = []
    for i in range(0, len(input_string)):
        a.append(input_string[i])
    for i in range(0, len(a)-2): # "dz="을 "dz=", "z=" 으로 두번 카운트해서 빼주기
        if a[i] + a[i+1] + a[i+2] == "dz=":
            count -= 1
    for i in range(0, len(a)-1):
        if a[i] + a[i+1] in croatia:
            count += 1
            a[i], a[i+1] = "5", "5"
    for i in range(0, len(a)):
        if a[i] != "5":
            count += 1
    print(count)

solve()

