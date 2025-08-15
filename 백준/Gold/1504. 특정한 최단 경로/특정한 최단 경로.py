import sys
import heapq

input = sys.stdin.readline

# 최댓값 정의
INF = int(1e9)


# 우선순위 큐로 구현한 dijkstra 정의
def dijkstra(start, end):
    # 최단 경로 거리 저장 리스트 정의
    distances = [INF] * (N + 1)
    queue = []
    # 시작 노드이므로 거리 0
    distances[start] = 0
    heapq.heappush(queue, (0, start))

    while queue:
        # 최단 경로 탐색 시작
        now_distance, now_node = heapq.heappop(queue)
        # 지금 거리가 더 크면 무시
        if distances[now_node] < now_distance:
            continue

        # 연결 노드와 거리 계산
        for next_node, next_distance in graph[now_node]:
            # 누적 거리 계산
            new_distance = now_distance + next_distance
            # 다음 노드까지의 거리가 현재보다 작으면 조건 만족
            if new_distance < distances[next_node]:
                # 거리 추가
                distances[next_node] = new_distance
                # 힙 삽입
                heapq.heappush(queue, (new_distance, next_node))

    # 최종 이동 거리 반환
    return distances[end]


# 입력
N, E = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    # 양방향 그래프이므로 양쪽으로 연결 내용 추가
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

# 이동 경로마다 dijkstra 수행
# 1 -> v1 -> v2 -> N 이동
distance_start_v1 = dijkstra(1, v1)
distance_v1_v2 = dijkstra(v1, v2)
distance_v2_end = dijkstra(v2, N)

# 1 -> v2 -> v1 -> N 이동
distance_start_v2 = dijkstra(1, v2)
distance_v2_v1 = dijkstra(v2, v1)
distance_v1_end = dijkstra(v1, N)

# 최단 경로 길이 계산
min_distance = min(distance_start_v1 + distance_v1_v2 + distance_v2_end, distance_start_v2 + distance_v2_v1 + distance_v1_end)

# 최단 경로 리스트가 초기값과 동일하면 경로가 없다는 의미이므로 경우에 따라 출력
print(min_distance if min_distance < INF else -1)
