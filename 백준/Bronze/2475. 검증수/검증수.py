import sys

input = sys.stdin.readline

# 1. 5자리 숫자 입력받기
nums = list(map(int, input().split()))

# 2. 검증수 계산 = (5개의 숫자 각각 제곱한 수의 합) / 10 나눈 나머지
answer = 0

for num in nums:
    answer += num**2

# 3. 검증수 출력
print(answer % 10)