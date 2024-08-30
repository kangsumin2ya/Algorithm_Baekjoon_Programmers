import sys
from collections import deque

input = sys.stdin.readline


def bfs(start):
    queue = deque([start])
    # 방문 리스트 정의
    visited = [0] * (N + 1)
    # 방문 처리
    visited[start] = 1
    # 이동 거리를 저장할 리스트 정의
    distance = [-1] * (N + 1)
    # 시작점 초기화
    distance[start] = 0

    while queue:
        v = queue.popleft()
        # 현재 도시에서 갈 수 있는 모든 도시 탐색
        for next_city in graph[v]:
            if not visited[next_city]:
                visited[next_city] = 1
                distance[next_city] = distance[v] + 1
                queue.append(next_city)

    return distance


# N, M, K, X 입력
N, M, K, X = map(int, input().split())

# 그래프 정의
graph = [[] for _ in range(N + 1)]


for _ in range(M):
    A, B = map(int, input().split())
    # 연결 정보 입력
    graph[A].append(B)

# bfs 수행
distances = bfs(X)

# 최단 거리 도시 번호 저장 리스트 정의
cities = [i for i in range(1, N+1) if distances[i] == K]

# 결과 출력
if cities:
    for city in sorted(cities):
        print(city)
else:
    print(-1)