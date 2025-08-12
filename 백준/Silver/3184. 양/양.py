import sys
from collections import deque

input = sys.stdin.readline

# bfs 구현
def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = 1

    # 양, 늑대 수 초기화
    sheep = 0
    wolf = 0

    # 초기 점 양인지 늑대인지 확인
    if field[x][y] == 'o':
        sheep += 1
    elif field[x][y] == 'v':
        wolf += 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 범위 내 인지, 방문 여부, 울타리 여부 확인
            if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and field[nx][ny] != '#':
                queue.append((nx, ny))
                visited[nx][ny] = 1
                # 양인지 늑대인지 확인
                if field[nx][ny] == 'o':
                    sheep += 1
                elif field[nx][ny] == 'v':
                    wolf += 1

    return sheep, wolf


# 입력받기
R, C = map(int, input().split())
field = [list(input().rstrip()) for _ in range(R)]

# 수평, 수직 이동방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 방문 리스트 정의
visited = [[0] * C for _ in range(R)]

# 살아있는 양, 늑대 수 초기화
sheep_live, wolf_live = 0, 0

# 탐색
for i in range(R):
    for j in range(C):
        # 울타리도 아니고 방문한 적 없으면 탐색
        if field[i][j] != '#' and not visited[i][j]:
            sheep, wolf = bfs(i, j)

            # 누가 더 많은지 확인
            if sheep > wolf:
                wolf = 0
            else:
                sheep = 0
            # 누적합 계산
            sheep_live += sheep
            wolf_live += wolf

# 결과 출력
print(sheep_live, wolf_live)