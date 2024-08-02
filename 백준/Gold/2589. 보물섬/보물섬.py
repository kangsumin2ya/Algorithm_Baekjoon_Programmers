import sys
from collections import deque

input = sys.stdin.readline


# bfs 정의
def bfs(x, y):
    queue = deque([(x, y)])
    visited = [[-1] * w for _ in range(h)]
    # 방문 처리
    visited[x][y] = 0
    # 최장 거리 정의
    max_distance = 0
    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            # 상하좌우 이동
            nx, ny = x + dx[i], y + dy[i]
            # 만약 범위 내의 육지이면서 방문하지 않은 곳이라면 탐색
            if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 'L' and visited[nx][ny] == -1:
                # 이동 거리 계산
                visited[nx][ny] = visited[x][y] + 1
                # 최장 거리 갱신
                max_distance = max(max_distance, visited[nx][ny])
                queue.append((nx, ny))

    return max_distance


# 이동 방향 정의
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 세로, 가로 입력
h, w = map(int, input().split())

# graph 저장
graph = [list(input().strip()) for _ in range(h)]

# 최장 거리 찾기
result = 0

for i in range(h):
    for j in range(w):
        if graph[i][j] == 'L':
            result = max(result, bfs(i, j))

# 결과 출력
print(result)