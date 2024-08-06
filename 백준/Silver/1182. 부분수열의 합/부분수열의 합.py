import sys
from itertools import combinations

input = sys.stdin.readline

# N, S 입력
N, S = map(int, input().split())

# N개의 정수 입력받아 리스트 저장
nums = list(map(int, input().split()))

# 합이 S인 부분 수열의 개수 저장하는 변수 정의
count = 0

# 정수들로 만들 수 있는 모든 조합 확인
for i in range(1, N+1):
    for j in combinations(nums, i):
        if sum(j) == S:
            count += 1

print(count)