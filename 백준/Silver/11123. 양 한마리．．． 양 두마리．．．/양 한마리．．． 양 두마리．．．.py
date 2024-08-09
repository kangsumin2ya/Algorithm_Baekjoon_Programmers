import sys
from collections import deque

input = sys.stdin.readline

# 확인할 방향 정의
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]


# bfs 함수
def bfs(x, y):
    queue = deque([(x, y)])
    if graph[x][y] == '#':
        # 방문 처리
        graph[x][y] = '.'
        # 큐가 빌 때까지 반복
        while queue:
            x, y = queue.popleft()
            # 4가지 방향 탐색
            for direction in directions:
                nx, ny = x + direction[0],  y + direction[1]
                # 그리드 내에 있으면서 양의 위치라면 탐색 진행
                if 0 <= nx < H and 0 <= ny < W and graph[nx][ny] == '#':
                    # 방문 처리
                    graph[nx][ny] = '.'
                    # 큐에 넣기
                    queue.append((nx, ny))


# T 입력
T = int(input())

# 테스트 케이스 별 정답 저장 리스트
answer = []

# T번 반복
for _ in range(T):
    # H, W 입력
    H, W = map(int, input().split())
    # 그래프 초기화
    graph = []

    # H x W 크기의 그리드 입력
    for _ in range(H):
        grid = list(map(str, input().rstrip()))
        graph.append(grid)

    # 무리 수 카운트
    count = 0

    # BFS 탐색
    for i in range(H):
        for j in range(W):
            # 양이 있는 위치에서 탐색 진행
            if graph[i][j] == '#':
                bfs(i, j)
                count += 1

    # 정답 저장
    answer.append(count)

# 결과 출력
for a in answer:
    print(a)
