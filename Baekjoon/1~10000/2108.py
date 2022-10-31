# 백준 2108번 문제
# 통계학
# acmicpc.net/problem/2108

from collections import Counter
import sys


t = int(sys.stdin.readline()) # 입력 수
nums = [] # 입력값을 저장할 배열
sum = 0 # 평균을 구하기 위한 합계

for _ in range(t):
    n = int(sys.stdin.readline())
    nums.append(n)
    sum += n    
nums.sort() # 정렬


avg = round(sum/t) # 평균
print(avg) # 평균 출력

if t % 2 == 1:
    med = int((t-1) / 2)
elif t % 2 ==0:
    med = int(t/2)
    
print(nums[med]) # 중앙값 출력


count_nums = Counter(nums).most_common() # 개수 세주는 라이브러리

if len(count_nums) > 1: # 최빈값이 두개 이상일 경우
    if count_nums[0][1] == count_nums[1][1]:  # 인덱스 0과 인덱스 1의 빈도수가 같을 경우
        print(count_nums[1][0]) # 빈도수가 같은 것 중에 두번째로 작은 수 출력
    else:
        print(count_nums[0][0]) # 빈도수가 같을 경우 빈도수가 제일 높은 수 출력
else:
    print(count_nums[0][0]) # 최빈값이 하나일경우 바로 출력


print(nums[-1] - nums[0]) # 범위 출력