import sys

input = sys.stdin.readline

# 세로 크기 N, 가로 크기 M 입력
N, M = map(int, input().split())

# 바닥 장식 저장
graph = []

# 세로 크기 N만큼 바닥 장식 입력
for _ in range(N):
    graph.append(list(input()))


# 바닥 장식 유형 조건을 가지고 재귀적으로 작동하는 DFS 구현
def DFS(x, y):
    if graph[x][y] == '|':
        graph[x][y] = 0

        x_up = x + 1
        x_down = x - 1

        if 0 < x_up < N and graph[x_up][y] == '|':
            DFS(x_up, y)

        if 0 < x_down < N and graph[x_down][y] == '|':
            DFS(x_down, y)

    if graph[x][y] == '-':
        graph[x][y] = 0

        y_up = y + 1
        y_down = y - 1

        if 0 < y_up < M and graph[x][y_up] == '-':
            DFS(x, y_up)

        if 0 < y_down < M and graph[x][y_down] == '-':
            DFS(x, y_down)

count = 0

for i in range(N):
    for j in range(M):
        if graph[i][j] != 0:
            DFS(i, j)
            count += 1

print(count)
