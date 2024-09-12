import sys
from collections import deque

input = sys.stdin.readline


# BFS 함수 구현
def bfs(x, y, color):
    queue = deque([(x, y)])
    # 방문 처리
    visited[x][y] = 1
    # 현재 색 확인
    current_color = grid[x][y]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + directions[i][0], y + directions[i][1]

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                # 적록색맹일 경우
                if color:
                    if current_color in 'RG' and grid[nx][ny] in 'RG':
                        queue.append((nx, ny))
                        visited[nx][ny] = 1
                    elif current_color == 'B' and grid[nx][ny] in 'B':
                        queue.append((nx, ny))
                        visited[nx][ny] = 1

                # 적록색맹 아닐 경우
                else:
                    if grid[nx][ny] == current_color:
                        queue.append((nx, ny))
                        visited[nx][ny] = 1


# 상하좌우 정의
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# N 입력
N = int(input())

# 구역 정보 입력
grid = [list(input().rstrip()) for _ in range(N)]

# 적록색맹인 사람이 봤을 때
visited = [[0] * N for _ in range(N)]
count_1 = 0

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j, color=False)
            count_1 += 1

# 적록색맹 아닌 사람이 봤을 때
visited = [[0] * N for _ in range(N)]
count_2 = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j, color=True)
            count_2 += 1

# 정답 출력
print(count_1, count_2)