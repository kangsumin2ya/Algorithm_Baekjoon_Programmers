import sys

input = sys.stdin.readline

# 1. 10개의 숫자를 입력받는다.
nums = [int(input()) for _ in range(10)]

# 2. 각 숫자를 42로 나눈 나머지를 리스트에 저장
remainder = []
for num in nums:
    remainder.append(num%42)

# 3. 나머지 리스트 중복 제거
remainder = list(set(remainder))

# 4. 리스트 개수 출력
print(len(remainder))