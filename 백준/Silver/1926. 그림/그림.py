import sys
from collections import deque

input = sys.stdin.readline


# bfs 수행
def bfs(x, y):
    queue = deque([(x, y)])
    # 방문 처리
    picture_info[x][y] = 0

    # 현재 그림 넓이
    current_area = 1

    # 이어진 부분 찾기
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and picture_info[nx][ny] == 1:
                picture_info[nx][ny] = 0
                queue.append((nx, ny))
                current_area += 1

    return current_area


# 입력 받기
n, m = map(int, input().split())
picture_info = [list(map(int, input().split())) for _ in range(n)]

# 그림 최대 크기 초기화
max_area = 0

# 그림 개수 초기화
num_pictures = 0

# 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 그림 크기 세기
for i in range(n):
    for j in range(m):
        if picture_info[i][j] == 1:
            # 그림 개수 추가
            num_pictures += 1
            # bfs 수행해 넓이 계산
            current_area = bfs(i, j)
            # 더 큰 것으로 갱신
            max_area = max(max_area, current_area)

# 결과 출력
print(num_pictures)
print(max_area)