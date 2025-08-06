from collections import deque
import sys

input = sys.stdin.readline

def bfs(x, y):
    queue = deque([(x, y)])
    map_info[y][x] = 1
    area = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and map_info[ny][nx] == 0:
                map_info[ny][nx] = 1
                queue.append((nx, ny))
                area += 1

    return area

# 입력
M, N, K = map(int, input().split())
map_info = [[0] * N for _ in range(M)]

# 직사각형 채우기
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())

    for y in range(y1, y2):
        for x in range(x1, x2):
            map_info[y][x] = 1  # ✅ 그대로 좌표 씀

# 방향 벡터
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = []

# 탐색
for j in range(M):
    for i in range(N):
        if map_info[j][i] == 0:
            result.append(bfs(i, j))

# 오름차순 정렬
result.sort()

# 결과 출력
print(len(result))

for i in result:
    print(i, end=' ')
