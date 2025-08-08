import sys
from collections import deque

input = sys.stdin.readline

# dfs 정의
def dfs(x, y, current_distance):
    global answer

    # 종료 조건 1 : 도착점에 도착
    if (x, y) == (end_x, end_y):
        if current_distance == K:
            answer += 1
        return  # 도착했으니 탐색 종료

    # 종료 조건 2 : 거리가 K 넘음
    if current_distance > K:
        return

    # 4방향 탐색
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        # 범위와 맵 정보 확인
        if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and map_info[nx][ny] != 'T':
            visited[nx][ny] = True
            dfs(nx, ny, current_distance+1)
            visited[nx][ny] = False


# 입력 받기
R, C, K = map(int, input().split())
map_info = [list(input().rstrip()) for _ in range(R)]

# 방문 리스트 정의
visited = [[False] * C for _ in range(R)]

# 정답 변수 초기화
answer = 0

# 이동 방향 정의
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 왼쪽 아래부터 오른쪽 위로 이동
start_x, start_y = R - 1, 0
end_x, end_y = 0, C - 1

# 시작점 방문 처리
visited[start_x][start_y] = True

# DFS 수행
dfs(start_x, start_y, 1)

# 정답 출력
print(answer)
