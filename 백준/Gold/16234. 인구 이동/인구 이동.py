import sys
from collections import deque

input = sys.stdin.readline


# bfs 구현
def bfs(x, y):
    queue = deque([(x, y)])
    # 연합 저장
    union = [(x, y)]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 범위 내 방문 여부 확인
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                # 인구 차이 확인
                if L <= abs(A[x][y] - A[nx][ny]) <= R:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                    union.append((nx, ny))
    return union


# 입력 받기
N, L, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

# 정답 초기화
answer = 0

# 인접 방향 확인
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 인구 이동 필요 없을 때까지 반복
while True:
    # 방문 리스트 정의
    visited = [[0 for _ in range(N)] for _ in range(N)]
    # 연합 유무 확인
    union_flag = 0
    # bfs 수행
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = 1
                union = bfs(i, j)

                # 연합 있으면 인구수 분배
                if len(union) > 1:
                    union_flag = 1
                    population = sum(A[x][y] for x, y in union) // len(union)
                    # 인구수 갱신
                    for x, y in union:
                        A[x][y] = population
    # 연합 없으면 인구 이동 종료
    if union_flag == 0:
        print(answer)
        break
    # 아니면 날짜 추가 후 계속 반복
    answer += 1
