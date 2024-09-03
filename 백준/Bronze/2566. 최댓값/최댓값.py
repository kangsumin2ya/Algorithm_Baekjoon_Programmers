import sys

input = sys.stdin.readline

# 숫자 입력
grid = [list(map(int, input().split())) for _ in range(9)]

# 최댓값에 대한 초기화
max_num = 0
max_idx_i = 0
max_idx_j = 0

# 격자 탐색
for i in range(9):
    for j in range(9):
        # 최댓값 갱신
        if grid[i][j] > max_num:
            max_num = grid[i][j]
            max_idx_i = i
            max_idx_j = j

# 결과 출력
print(max_num)
print(max_idx_i + 1, max_idx_j + 1)