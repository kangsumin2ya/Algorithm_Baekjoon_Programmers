import sys
from collections import deque

input = sys.stdin.readline

# 상하좌우 이동 방법 정의
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y, color):
    # 큐 생성
    queue = deque([(x, y)])
    # 방문 처리
    visited[x][y] = 0
    # 현재 색
    current_color = graph[x][y]
    # 큐 빌 때까지 반복
    while queue:
        x, y = queue.popleft()

        # 상하좌우 확인해 같은 색상 찾기
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                # 적록색약이 맞다면
                if color:
                    if current_color in 'RG' and graph[nx][ny] in 'RG':
                        queue.append((nx, ny))
                        visited[nx][ny] = 1

                    elif current_color == 'B' and graph[nx][ny] in 'B':
                        queue.append((nx, ny))
                        visited[nx][ny] = 1
                # 적록색약이 아니라면
                else:
                    if graph[nx][ny] == current_color:
                        queue.append((nx, ny))
                        visited[nx][ny] = 1


# N 입력
N = int(input())

# 그래프 변수 정의
graph = []

# 그림 입력
for _ in range(N):
    graph.append(list(input().rstrip()))

# 적록 색약 아닌 경우의 구역 수 세기
normal_count = 0
visited = [[0] * N for _ in range(N)]

# 적록 색약 아닌 경우 탐색
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j, color=False)
            normal_count += 1

# 적록 색약 아닌 경우의 구역 수 세기
count = 0
visited = [[0] * N for _ in range(N)]

# 적록 색약인 경우 탐색
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j, color=True)
            count += 1

# 결과 출력
print(normal_count, count)