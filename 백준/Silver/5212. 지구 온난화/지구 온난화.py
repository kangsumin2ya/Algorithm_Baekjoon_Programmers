import sys

input = sys.stdin.readline

# R, C 입력
R, C = map(int, input().split())

# 지도 입력
current_map = [list(input().rstrip()) for _ in range(R)]

# 동일한 크기의 바다 지도 만들기
future_map = [['.'] * C for _ in range(R)]

# 확인할 4가지 방향 정의
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# 섬의 바다와 접하는 면 세기
for x in range(R):
    for y in range(C):
        sea = 0
        if current_map[x][y] == 'X':
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= R or ny < 0 or ny >= C or current_map[nx][ny] == '.':
                    sea += 1
            # 접하는 면이 3면 미만이면 잠기지 않음
            if sea < 3:
                future_map[x][y] = 'X'

# 최대 최소 인덱스 정의
min_row, min_col = R, C
max_row, max_col = 0, 0

# 최소 직사각형 찾기
for x in range(R):
    for y in range(C):
        if future_map[x][y] == 'X':
            min_row = min(min_row, x)
            max_row = max(max_row, x)
            min_col = min(min_col, y)
            max_col = max(max_col, y)

# 결과 출력
for i in range(min_row, max_row + 1):
    print(''.join(future_map[i][min_col:max_col + 1]))
