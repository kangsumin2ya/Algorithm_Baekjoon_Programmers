import sys
from collections import deque

input = sys.stdin.readline

# 1. N 입력
N = int(input())

# 2. N번 반복해 높이 정보 저장
heights = [list(map(int, input().split())) for _ in range(N)]

# 3. 잠기는 높이 리스트 정의
max_height = max(max(height) for height in heights)

# 4. 최대 안전 지역 개수 초기화
max_safe_zones = 0

# 5. 상하좌우 이동 방법 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 4. bfs 구현
def bfs(x, y, visited, heights, limit):
    queue = deque([(x, y)])
    # 방문 처리
    visited[x][y] = 1
    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        # 4가지 방향 확인
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 범위 내에서 방문 처리 안된 곳이 있는지 확인
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and heights[nx][ny] > limit:
                visited[nx][ny] = 1
                queue.append((nx, ny))


# 6. N*N에서 bfs 수행해 최대 개수 찾기
for limit in range(max_height + 1):
    visited = [[0] * N for _ in range(N)]
    safe_zones = 0

    for i in range(N):
        for j in range(N):
            if heights[i][j] > limit and not visited[i][j]:
                bfs(i, j, visited, heights, limit)
                safe_zones += 1

    max_safe_zones = max(max_safe_zones, safe_zones)

# 7. 원하는 형식으로 출력
print(max_safe_zones)
