import sys
from collections import deque

input = sys.stdin.readline


# BFS 정의
def bfs(x, y):
    queue = deque([(x, y)])
    # 방문 처리
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()

        # 이동시키기
        for i in range(8):
            nx, ny = x + directions[i][0], y + directions[i][1]

            # 이동 위치가 범위 내이고 방문하지 않았으며 땅이라면 탐색 지속
            if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and graph[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = 1


# 8가지 이동 방향 정의
directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

while True:
    # w, h 입력
    w, h = map(int, input().split())

    # 입력에 0, 0 들어올 때까지 반복
    if w == 0 and h == 0:
        break

    else:
        # 지도 정보 입력
        graph = [list(map(int, input().split())) for _ in range(h)]

        # 방문 리스트 만들기
        visited = [[0] * w for _ in range(h)]

        # 섬 개수 초기화
        count = 0

        # 전체 지도 탐색
        for i in range(h):
            for j in range(w):
                # 땅을 찾았다면 BFS 수행
                if graph[i][j] == 1 and not visited[i][j]:
                    bfs(i, j)
                    # 탐색 종료 후 개수 증가
                    count += 1

        # 결과 출력
        print(count)
