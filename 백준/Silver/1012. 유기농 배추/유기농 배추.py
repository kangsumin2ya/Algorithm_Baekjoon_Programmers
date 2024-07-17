import sys
from collections import deque

input = sys.stdin.readline

# 1. 배추 확인 위해 4가지 방향 이동 방법 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 2. BFS 정의
def bfs(x, y):
    queue = deque([(x, y)])
    # 2-1. 방문 처리
    graph[x][y] = 0

    while queue:
        x, y = queue.popleft()

        # 2-2. 4가지 방향 이동
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 2-3. 영역 내에 있는 배추가 있는 땅이면서 방문하지 않은 땅이 있으면 탐색
            if 0 <= nx < M and 0 <= ny < N and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))

# 정답 저장 리스트
answer = []

# 3. 테스트케이스 T 입력
T = int(input())

# 4. 테스트케이스 만큼 반복
for _ in range(T):
    # 4-1. M, N, K 입력
    M, N, K = map(int, input().split())

    # 4-2. K번 반복해 배추 위치 X, Y 입력
    graph = [[0] * N for _ in range(M)]

    for _ in range(K):
        x, y = map(int, input().split())
        graph[x][y] = 1

    # 4-3. 배추흰지렁이 셀 변수 정의
    count = 0

    # 4-4. N*M에서 BFS 수행
    for i in range(M):
        for j in range(N):
              if graph[i][j] == 1:
                   bfs(i, j)
                   count += 1

    # 4-5. T개의 정답 저장
    answer.append(count)

# 5. 원하는 형식으로 출력
for count in answer:
    print(count)