import sys

input = sys.stdin.readline

# 1. 9개 숫자 입력받기
nums = [int(input()) for _ in range(9)]

# 2. 최댓값 찾기
max_num = max(nums)

# 3. 인덱스 찾기
max_num_idx = nums.index(max_num)

# 4. 출력
print(max_num)
print(max_num_idx+1)    # 몇번째 값인지를 출력