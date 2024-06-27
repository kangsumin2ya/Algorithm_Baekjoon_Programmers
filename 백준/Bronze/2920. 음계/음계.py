import sys

input = sys.stdin.readline

# 1. 음계 리스트를 선언한다.
ascend = [1, 2, 3, 4, 5, 6, 7, 8]
descend = [8, 7, 6, 5, 4, 3, 2, 1]

# 2. 8개의 숫자를 입력받아 리스트에 저장
nums = list(map(int, input().split()))

# 3. 조건에 따라 출력
if nums == ascend:
    print('ascending')

elif nums == descend:
    print('descending')

else:
    print('mixed')