import sys

input = sys.stdin.readline

# 1. N 입력 받기
N = int(input())

# 2. N개 정수 입력 받기
nums = list(map(int, input().split()))

# 3. 최솟값, 최댓값 구하기
min_num = min(nums)
max_num = max(nums)

# 4. 공백 구분으로 출력
print(f'{min_num} {max_num}')