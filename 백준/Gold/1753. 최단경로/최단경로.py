import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distances[start] = 0

    while queue:
        weight, now_node = heapq.heappop(queue)
        # 더 큰 가중치이면 무시
        if distances[now_node] < weight:
            continue

        for next_node, next_weight in graph[now_node]:
            # 누적 가중치 계산
            new_weight = weight + next_weight
            # 다음 노드의 가중치가 현재보다 작으면 조건 만족
            if new_weight < distances[next_node]:
                distances[next_node] = new_weight
                # 힙 삽입
                heapq.heappush(queue, (new_weight, next_node))


# 입력
V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

# 최단 경로 저장 리스트 정의
distances = [INF] * (V + 1)

# 다익스트라 실행
dijkstra(K)

# 출력
for i in range(1, V+1):
    if distances[i] == INF:
        print('INF')
    else:
        print(distances[i])
