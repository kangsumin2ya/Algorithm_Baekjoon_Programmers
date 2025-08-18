import sys
from collections import deque

input = sys.stdin.readline

# 최댓값 정의
INF = int(1e9)

# 입력
M, N = map(int, input().split())
maze_info = [list(map(int, input().strip())) for _ in range(N)]

# 이동 방향 정의
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 부순 벽 개수 저장
dist = [[INF] * M for _ in range(N)]
dist[0][0] = 0

# 0-1 BFS
q = deque()
q.append((0, 0))

while q:
    x, y = q.popleft()

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            # 벽을 부수지 않아도 되는 경우 (비용 0)
            if maze_info[nx][ny] == 0 and dist[nx][ny] > dist[x][y]:
                dist[nx][ny] = dist[x][y]
                q.appendleft((nx, ny))  # 0이면 앞에 넣기

            # 벽을 부숴야 하는 경우 (비용 1)
            elif maze_info[nx][ny] == 1 and dist[nx][ny] > dist[x][y] + 1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))  # 1이면 뒤에 넣기

# 출력 (도착 지점의 최소 벽 부순 개수)
print(dist[N-1][M-1])
