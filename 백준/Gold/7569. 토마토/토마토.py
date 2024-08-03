import sys
from collections import deque

input = sys.stdin.readline

# 방향 정의
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]


# bfs 정의
def bfs():
    while queue:
        z, x, y = queue.popleft()
        # 이동 탐색
        for i in range(6):
            nz, nx, ny = z + dz[i], x + dx[i], y + dy[i]

            # 해당 위치가 범위 내에 있고, 익지 않은 토마토라면
            if (0 <= nz < H) and (0 <= nx < N) and (0 <= ny < M) and (tomatoes[nz][nx][ny] == 0):
                # 익을 때까지 걸린 일수 계산
                tomatoes[nz][nx][ny] = tomatoes[z][x][y] + 1
                queue.append((nz, nx, ny))


# M, N, H 입력
M, N, H = map(int, input().split())

# 토마토 저장 리스트 정의
tomatoes = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

# 큐 정의
queue = deque()

# 모두 익은 토마토 큐에 추가
for z in range(H):
    for x in range(N):
        for y in range(M):
            if tomatoes[z][x][y] == 1:
                queue.append((z, x, y))

# bfs로 익은 일수 계산
bfs()

# 최소 일수 계산
days = 0

# 모두 익을 수 있는지 여부 정의
impossible = False

# 익지 못한 토마토 있는지 확인
for z in range(H):
    for x in range(N):
        for y in range(M):
            # 익지 못한 토마토 있다면 불가능 표시
            if tomatoes[z][x][y] == 0:
                impossible = True
            # 다 익었다면 제일 큰 일수 구하기
            days = max(days, tomatoes[z][x][y])

# 결과 출력
if impossible:
    print(-1)
else:
    print(days - 1)