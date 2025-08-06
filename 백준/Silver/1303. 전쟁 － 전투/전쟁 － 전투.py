import sys

input = sys.stdin.readline


# 원하는 병력 찾는 dfs 구현
def dfs(power, x, y):
    stack = [(x, y)]
    # 방문 표시
    knight_info[x][y] = 'N'
    # 병사 수 계산
    num = 1

    while stack:
        x, y = stack.pop()

        # 인접 병사 탐색
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 범위 내이면서 원하는 병령이면 스택에 넣고 탐색
            if 0 <= nx < M and 0 <= ny < N and knight_info[nx][ny] == power:
                stack.append((nx, ny))
                knight_info[nx][ny] = 'N'
                num += 1

    return num**2


# 입력 받기
N, M = map(int, input().split())

# 병사 정보 입력
knight_info = [list(input()) for _ in range(M)]

# 이동 방향 정의
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


# 각 병력 초기화
W_power = 0
B_power = 0

# white 찾기
for i in range(M):
    for j in range(N):
        if knight_info[i][j] == 'W':
            W_power += dfs('W', i, j)
# black 찾기
for i in range(M):
    for j in range(N):
        if knight_info[i][j] == 'B':
            B_power += dfs('B', i, j)

print(W_power, B_power)
