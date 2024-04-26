from collections import deque
import sys

input = sys.stdin.readline

# 1. N과 M을 입력받는다.
N, M = map(int, input().split())

# 2. graph 변수를 정의한다.
graph = []

# 3. 지도 정보를 for문을 통해 입력받아 graph에 저장한다.
for _ in range(N):
    graph.append(list(map(int, input().rstrip())))

# print(graph)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 4. BFS를 구현한다.
def BFS(x, y):

    queue = deque()

    queue.append((x, y, 1))

    # 방문 처리
    graph[x][y] = 0

    while queue:
        x, y, count = queue.popleft()

        if x == N - 1 and y == M - 1:  # 목적지에 도착한 경우
            return count

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                queue.append((nx, ny, count + 1))
                graph[nx][ny] = 0

    return count

# 5. 최소 칸 수를 출력한다.
print(BFS(0, 0))