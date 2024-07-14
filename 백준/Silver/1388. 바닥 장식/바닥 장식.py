import sys

input = sys.stdin.readline

# 1. N, M 입력
N, M = map(int, input().split())

# 2. 바닥 장식 입력
floor = [list(input().rstrip()) for _ in range(N)]

# 3. DFS 함수 구현
def dfs(x, y):
    # 3-1. '-'이면 방문처리 후 범위 내의 오른쪽, 왼쪽 확인
    if floor[x][y] == '-':
        floor[x][y] = 0

        if y + 1 < M and floor[x][y + 1] == '-':
            dfs(x, y + 1)

    # 3-3. '|'이면 방문처리 후 위, 아래 확인
    elif floor[x][y] == '|':
        floor[x][y] = 0

        if x + 1 < N and floor[x + 1][y] == '|':
            dfs(x + 1, y)

# 4. 개수 저장 변수 정의
count = 0

# 5. 전체 바닥 장식 확인
for i in range(N):
    for j in range(M):
        if floor[i][j] != 0:
            dfs(i, j)
            count += 1

# 6. 원하는 형식으로 출력
print(count)