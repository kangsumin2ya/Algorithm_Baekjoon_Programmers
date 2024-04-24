from collections import deque
import sys

input = sys.stdin.readline

dx = [1, -1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]

def BFS(x, y):
    # BFS를 위해 queue 생성
    queue = deque()
    queue.append([x, y])

    # 방문한 집 0으로 변환
    graph[y][x] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < w and 0 <= ny < h and graph[ny][nx] == 1:
                queue.append([nx, ny])
                graph[ny][nx] = 0

while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    graph = []

    total_count = 0

    for i in range(h):
        graph.append(list(map(int, input().split())))

    for j in range(h):
        for k in range(w):
            if graph[j][k] == 1:
                BFS(k, j)
                total_count += 1
    print(total_count)

