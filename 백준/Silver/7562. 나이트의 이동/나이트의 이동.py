import sys
from collections import deque

input = sys.stdin.readline

# 8가지 이동 방법 정의
dx = [-2, -1, -2, -1, 2, 1, 2, 1]
dy = [1, 2, -1, -2, 1, 2, -1, -2]

# 정답 저장 리스트 정의
answer = []


# bfs 정의
def bfs(x, y, move_x, move_y):
    queue = deque([(x, y, 0)])
    # 방문 처리 리스트 정의
    visited = [[0] * l for _ in range(l)]
    # 현재 노드 방문 처리
    visited[x][y] = 1
    # 큐가 빌 때까지 반복
    while queue:
        x, y, count = queue.popleft()
        # 목적지에 도착하면 이동 횟수 리턴
        if x == move_x and y == move_y:
            return count
        # 8가지 방향으로 이동
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            # 영역 내
            if 0 <= nx < l and 0 <= ny < l and not visited[nx][ny]:
                visited[nx][ny] = 1
                queue.append((nx, ny, count + 1))
    return -1


# 테스트케이스 입력
T = int(input())

for _ in range(T):
    # 체스판 한 변 길이 입력
    l = int(input())

    # 나이트가 있는 칸 입력
    start_x, start_y = map(int, input().split())

    # 이동하려는 칸 입력
    end_x, end_y = map(int, input().split())

    # BFS 수행
    result = bfs(start_x, start_y, end_x, end_y)

    # 결과 저장
    answer.append(result)

# 결과 출력
for a in answer:
    print(a)