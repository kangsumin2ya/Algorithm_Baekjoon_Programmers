import sys

input = sys.stdin.readline

# 0. 필요 변수 선언
want = [1, 2, 3, 4, 5]

# 1. `nums` 입력
nums = list(map(int, input().split()))

# 2. while문으로 종료조건(원하는 배열 리스트가 될 때) 작성
while True:
    if nums == want:
        break

    # 3. 리스트 요소 확인해 배열 위치 조정
    for i in range(1, 5):
        if nums[i-1] > nums[i]:
            nums[i-1], nums[i] = nums[i], nums[i-1]
            print(' '.join(map(str, nums)))