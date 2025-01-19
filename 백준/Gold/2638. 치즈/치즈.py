import sys
from collections import deque

input = sys.stdin.readline


# bfs 수행
def bfs():
    # 큐 정의
    queue = deque([(0, 0)])
    # 방문 처리
    visited[0][0] = 1
    # 치즈 주변 공기 접촉 횟수 저장할 딕셔너리 정의
    air = {}

    while queue:
        x, y = queue.popleft()

        # 4가지 방향 확인
        for i in range(4):
            nx, ny = x + directions[i][0], y + directions[i][1]

            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                # 치즈가 아닌 경우 찾기
                if board[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                # 치즈인 경우 공기 접촉면 세기
                else:
                    if (nx, ny) not in air:
                        air[(nx, ny)] = 1
                    else:
                        # 횟수 추가
                        air[(nx, ny)] += 1
    return air


# N, M 입력
N, M = map(int, input().split())

# 치즈 정보 입력
board = [list(map(int, input().split())) for _ in range(N)]

# 4면 접근 방향
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# 시간 초기화
t = 0

# 치즈가 다 없어질 때까지 bfs 반복
while True:
    # 방문 리스트 정의
    visited = [[0] * M for _ in range(N)]
    air = bfs()

    if not air:  # 녹을 치즈가 없으면 종료
        break

    # 치즈 녹이기
    for (x, y), count in air.items():
        if count >= 2:
            board[x][y] = 0

    # 시간 추가
    t += 1

# 결과 출력
print(t)