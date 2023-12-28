from collections import deque

def BFS(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # BFS를 위한 큐 생성
    queue = deque([(x, y)])

    # 방문한 집은 0으로 표시
    graph[x][y] = 0

    # 집의 개수 카운트
    count = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = 0
                count += 1

    return count

# 지도의 크기 N 입력
N = int(input())

# 지도 정보 저장할 리스트
graph = []

# 지도 정보 입력
for _ in range(N):
    graph.append(list(map(int, input().rstrip())))

# 각 단지 내 집의 수 담을 리스트
house_count = []

# 전체 지도 탐색
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            house_count.append(BFS(i, j))

# 단지 수 출력
print(len(house_count))

# 단지 내 집의 수 오름차순 출력
house_count.sort()

for count in house_count:
    print(count)

