import sys
from collections import deque

input = sys.stdin.readline

# n, m 입력
n, m = map(int, input().split())

# 지도 입력
map_info = [list(map(int, input().split())) for _ in range(n)]

# 거리 저장 배열 정의
distances = [[-1] * m for _ in range(n)]

# 이동 방향 정의
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


# bfs 정의
def bfs(x, y):
    queue = deque([(x, y)])
    # 방문 처리
    distances[x][y] = 0

    while queue:
        x, y = queue.popleft()
        # 4가지 방향 이동
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # 범위 내이고 방문하지 않은 땅이 있다면
            if 0 <= nx < n and 0 <= ny < m and map_info[nx][ny] == 1 and distances[nx][ny] == -1:
                distances[nx][ny] = distances[x][y] + 1
                # bfs 탐색 지속
                queue.append((nx, ny))


# 지도 탐색
for i in range(n):
    for j in range(m):
        if map_info[i][j] == 2:
            bfs(i, j)

# 결과 출력
for i in range(n):
    for j in range(m):
        # 갈 수 없는 땅이면
        if map_info[i][j] == 0:
            print(0, end=' ')
        # 갈 수 있는 땅이면
        else:
            print(distances[i][j], end=' ')

    print()