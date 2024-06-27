import sys

input = sys.stdin.readline

# 1. N 입력 받기
N = int(input())

# 2. N개 정수 입력 받기
nums = list(map(int, input().split()))

# 3. 공백 구분으로 출력
print(min(nums), max(nums))