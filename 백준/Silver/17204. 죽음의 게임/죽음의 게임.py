import sys
from collections import deque

input = sys.stdin.readline


# BFS 정의
def BFS(x):
    queue = deque([x])
    visited[x] = 1
    M = 0

    while queue:
        y = queue.popleft()

        if graph[y] == K:
            return M + 1  # K에 도달한 시점의 M 값 반환
        next_node = graph[y]
        if not visited[next_node]:
            visited[next_node] = 1
            queue.append(next_node)
            M += 1
    return -1


# N, K 입력
N, K = map(int, input().split())

# 그래프 저장
graph = [int(input()) for _ in range(N)]

# 방문 리스트 정의
visited = [0] * N

# BFS 수행
result = BFS(0)

# 원하는 결과 출력
print(result)