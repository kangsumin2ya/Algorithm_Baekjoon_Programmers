import sys
from collections import deque

input = sys.stdin.readline

# BFS 정의
def bfs(v):
    queue = deque([v])
    # 방문 리스트 초기화
    visited = [-1] * (N + 1)
    # 방문 처리
    visited[v] = 0

    # 큐 빌 때까지 반복
    while queue:
        start = queue.popleft()

        for i in graph[start]:
            # 방문하지 않았다면
            if visited[i] == -1:
                # 방문 처리하고 거치는 단계 수 계산
                visited[i] = visited[start] + 1
                queue.append(i)
    # 케빈 베이컨 수 합 반환
    return sum(visited)


# N, M 입력
N, M = map(int, input().split())

# 관계 저장
graph = [[] for _ in range(N + 1)]

# M번 반복
for _ in range(M):
    # 친구 관계 입력
    A, B = map(int, input().split())
    # 친구 관계 저장
    graph[A].append(B)
    graph[B].append(A)

# 케빈 베이컨 수 저장할 리스트
kevin = []

# 각 노드마다 BFS를 수행하여 케빈 베이컨 수를 계산
for i in range(1, N+1):
    kevin_sum = bfs(i)
    # 케빈 베이컨 수, 노드 번호 함께 저장
    kevin.append((kevin_sum, i))

# 케빈 베이컨 제일 작은 사람 찾기
kevin.sort()
print(kevin[0][1])