import sys

input = sys.stdin.readline

# 5개의 수 입력
nums = []

for _ in range(5):
    nums.append(int(input()))

# 평균 출력
nums_avg = sum(nums) // 5
print(nums_avg)

# 중앙값 출력
nums.sort()
print(nums[2])