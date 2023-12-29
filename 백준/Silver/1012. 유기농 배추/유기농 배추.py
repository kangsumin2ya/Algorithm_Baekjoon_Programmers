import sys
sys.setrecursionlimit(10000) # 재귀 깊이 설정

def DFS(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 현재 위치를 방문 처리
    graph[x][y] = 0

    # 상하좌우 위치 확인
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < M and 0 <= ny < N and graph[nx][ny] == 1:
            DFS(nx, ny)

# 테스트케이스 개수 T 입력
T = int(input())

# 각 테스트케이스 별 필요한 지렁이 수 저장
answer = []

for _ in range(T):
    # 배추밭 정보 M, N, K 입력
    M, N, K = map(int, input().split())

    # 지도 정보 저장할 리스트
    graph = [[0] * N for _ in range(M)]

    # 지도 정보 입력
    for _ in range(K):
        x, y = map(int, input().split())
        graph[x][y] = 1

    # 배추흰지렁이의 수 초기화
    count = 0

    # 전체 지도 탐색
    for i in range(M):
        for j in range(N):
            if graph[i][j] == 1:
                # 배추가 심어져 있는 곳에서 DFS 수행
                DFS(i, j)
                count += 1

    answer.append(count)

# 각 테스트케이스 별 필요한 배추흰지렁이 수 출력
for count in answer:
    print(count)