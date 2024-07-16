import sys
from collections import deque

input = sys.stdin.readline

# 1. N, M, V 입력
N, M, V = map(int, input().split())

# 2. 연결 정보 저장
graph = [[] for _ in range(N+1)]

for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

# 정점별 연결 정점 오름차순 정렬
for i in range(N+1):
    graph[i].sort()

# 3. DFS/BFS 정의
def dfs(graph, start, visited):
    # 방문 처리
    visited[start] = 1
    # 결과 출력
    print(start, end=' ')
    # 연결된 방문 안한 정점 방문
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    # 방문 처리
    visited[start] = 1
    while queue:
        v = queue.popleft()
        # 결과 출력
        print(v, end=' ')
        # 연결된 방문 안한 정점 방문
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1

# 4. 방문 처리 리스트 정의 후, DFS/BFS 수행하며 원하는 결과 출력
visited = [0] * (N+1)
dfs(graph, V, visited)

print()

visited = [0] * (N+1)
bfs(graph, V, visited)