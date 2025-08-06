import sys
from collections import deque

input = sys.stdin.readline


# bfs로 해당 쓰레기 크기 구하기
def bfs(x, y):
    queue = deque([(x, y)])
    # 방문 처리
    trash_info[x][y] = 0
    # 쓰레기 크기 초기화
    area = 1

    # 이어진 쓰레기 크기 확인
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and trash_info[nx][ny] == 1:
                trash_info[nx][ny] = 0
                area += 1
                queue.append((nx, ny))

    return area


# 입력 받기
N, M, K = map(int, input().split())

# 쓰레기 정보 받을 리스트 정의
trash_info = [[0] * M for _ in range(N)]

for _ in range(K):
    r, c = map(int, input().split())
    # 쓰레기 정보 입력
    trash_info[r-1][c-1] = 1

# 이동 방향 정의
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 최대 쓰레기 크기 초기화
max_area = 0

# 쓰레기 탐색
for i in range(N):
    for j in range(M):
        if trash_info[i][j] == 1:
            area = bfs(i, j)
            max_area = max(max_area, area)

# 결과 출력
print(max_area)