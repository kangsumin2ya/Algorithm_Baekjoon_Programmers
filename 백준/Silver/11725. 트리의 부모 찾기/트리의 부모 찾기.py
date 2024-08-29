import sys
from collections import deque

input = sys.stdin.readline

def bfs(v):
    # 큐 정의
    queue = deque([v])
    # 큐 빌 때까지 반복
    while queue:
        v = queue.popleft()
        # 연결 정보 확인하면서 부모 노드 채우기
        for i in graph[v]:
            if parents[i] == 0:
                parents[i] = v
                queue.append(i)


# N 입력
N = int(input())

# 부모 노드 저장할 리스트 정의
parents = [0] * (N+1)

# 그래프 정의
graph = [[] for _ in range(N+1)]

# 연결 정보 저장
for _ in range(N-1):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

# bfs 수행
bfs(1)

# 2번째 노드부터 부모 노드 출력
for i in range(2, N+1):
    print(parents[i])
