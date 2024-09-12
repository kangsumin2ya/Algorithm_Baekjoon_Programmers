import sys
from collections import deque

input = sys.stdin.readline


def bfs(not_tomatoes):
    # 최소 일수 계산 변수 초기화
    days = -1

    while queue:
        # 일수 증가
        days += 1
        # 큐에 있는 익은 토마토 모두 확인
        for _ in range(len(queue)):
            x, y = queue.popleft()

            # 상하좌우에 익지 않은 토마토 확인
            for direction in directions:
                nx, ny = x + direction[0], y + direction[1]

                # 범위 내 익지 않은 토마토 있다면
                if 0 <= nx < N and 0 <= ny < M and tomatoes[nx][ny] == 0:
                    queue.append((nx, ny))
                    # 토마토 익히기
                    tomatoes[nx][ny] = 1
                    # 안익은 토마토 수 감소
                    not_tomatoes -= 1

    return days, not_tomatoes


# 4방향 정의
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# M(가로), N(세로) 입력
M, N = map(int, input().split())

# 토마토 상태 입력
tomatoes = [list(map(int, input().split())) for _ in range(N)]

# 익은 토마토들 좌표를 저장하는 큐
queue = deque()

# 안익은 토마토 개수 세기
not_tomatoes = 0

for i in range(N):
    for j in range(M):
        # 익은 토마토 위치 저장
        if tomatoes[i][j] == 1:
            queue.append((i, j))
        # 안익은 토마토 개수 세기
        elif tomatoes[i][j] == 0:
            not_tomatoes += 1

# 1. 처음부터 모든 토마토가 익어있는 상태면 0 출력
if not_tomatoes == 0:
    print(0)
# 2. 아니라면 BFS 수행
else:
    days, not_tomatoes = bfs(not_tomatoes)
    # 익지 않은 토마토 있다면
    if not_tomatoes > 0:
        print(-1)
    else:
        print(days)
