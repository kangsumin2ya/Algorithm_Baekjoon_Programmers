import sys
from collections import deque

input = sys.stdin.readline

def bfs(start, end):
    # 시작점, 가중치(거리) 추가
    queue = deque([(start, 0)])
    # 방문 리스트 초기화
    visited = [0] * (N + 1)
    # 방문 처리
    visited[start] = 1
    # 큐 빌 때까지 반복
    while queue:
        # 현재 노드, 해당 가중치 꺼내기
        v, distance = queue.popleft()
        # 현재 노드가 목표 노드와 같다면 그때까지 누적된 거리 반환
        if v == end:
            return distance
        # 해당 노드와 연결된 노드 확인
        for i, d in graph[v]:
            # 방문 안했으면 탐색
            if not visited[i]:
                visited[i] = 1
                # 누적된 가중치 추가
                queue.append((i, d + distance))


# N, M 입력
N, M = map(int, input().split())

# 그래프 정의
graph = [[] for _ in range(N + 1)]

# 연결 정보와 거리(가중치) 입력
for _ in range(N - 1):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

# 정답 저장 리스트
answer = []

# M개의 결과 확인
for _ in range(M):
    a, b = map(int, input().split())
    answer.append(bfs(a, b))

# 결과 출력
for a in answer:
    print(a)