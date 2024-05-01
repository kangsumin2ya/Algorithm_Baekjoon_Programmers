import sys

input = sys.stdin.readline

# 1. N 입력
N = int(input())

# 2. 변수 정의
num_pos_dict = {}

count = 0

# 3. 소 번호 - 소 위치 입력
for _ in range(N):
    num, pos = map(int, input().split())

    if num not in num_pos_dict:
        num_pos_dict[num] = pos

    else :
        if num_pos_dict[num] != pos:
            count += 1
            num_pos_dict[num] = pos

print(count)