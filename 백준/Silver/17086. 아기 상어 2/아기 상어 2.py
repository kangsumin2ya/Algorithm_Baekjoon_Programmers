import sys
from collections import deque

input = sys.stdin.readline


# BFS 구현
def bfs(shark):
    # 이동 칸수 변수
    max_distance = 0
    queue = deque(shark)
    while queue:
        x, y, distance = queue.popleft()

        for direction in directions:
            nx, ny = x + direction[0], y + direction[1]
            # 공간 내 방문 안한 칸이라면 탐색 지속
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                # 방문 처리 = 해당 칸까지의 이동 칸 수 저장
                graph[nx][ny] = distance + 1
                # 큐 저장
                queue.append((nx, ny, distance + 1))
                # 최대 거리 갱신
                max_distance = max(max_distance, distance + 1)
    return max_distance


# 8가지 방향 정의
directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

# N, M 입력
N, M = map(int, input().split())

# 그래프 초기화
graph = []

# 공간 상태 입력
for _ in range(N):
    graph.append(list(map(int, input().split())))

# 상어 위치 찾기
shark = []

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            # 상어 위치부터 시작할 것이므로 거리 0 추가
            shark.append((i, j, 0))

# 결과 출력
print(bfs(shark))