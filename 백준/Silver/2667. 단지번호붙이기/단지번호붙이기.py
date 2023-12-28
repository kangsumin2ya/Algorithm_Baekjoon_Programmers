def dfs(x, y):
    # 상, 하, 좌, 우 방향 벡터 정의
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 현재 위치 방문 처리
    graph[x][y] = 0
    count = 1

    # 상, 하, 좌, 우로 인접한 노드에 대해 재귀적으로 DFS 실행
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 1:
            count += dfs(nx, ny)

    return count

N = int(input())  # 지도의 크기 N 입력
graph = []  # 지도 정보를 저장할 리스트

# 지도 정보 입력
for _ in range(N):
    graph.append(list(map(int, input().rstrip())))

# 각 단지 내 집의 수를 담을 리스트
house_count = []

# 전체 지도 탐색
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            house_count.append(dfs(i, j))

# 단지 수 출력
print(len(house_count))

# 단지 내 집의 수 오름차순 출력
house_count.sort()
for count in house_count:
    print(count)