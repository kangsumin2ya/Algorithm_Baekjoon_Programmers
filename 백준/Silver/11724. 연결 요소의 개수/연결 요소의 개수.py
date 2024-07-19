import sys
from collections import deque

input = sys.stdin.readline


# BFS 정의
def bfs(x):
    queue = deque([x])
    # 방문 처리
    visited[x] = 1
    # 큐가 빌 때까지 반복
    while queue:
        y = queue.popleft()
        for i in graph[y]:
            if not visited[i]:
                # 방문 처리
                visited[i] = 1
                queue.append(i)


# N, M 입력
N, M = map(int, input().split())

# 그래프 정의
graph = [[] for _ in range(N+1)]

# M번 반복해 u, v 입력받아 그래프에 저장
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 방문 리스트 정의
visited = [0] * (N+1)

# 연결 요소 세는 변수 정의
count = 0

# BFS 수행
for i in range(1, N+1):
    if not visited[i]:
        bfs(i)
        count += 1

# 정답 출력
print(count)