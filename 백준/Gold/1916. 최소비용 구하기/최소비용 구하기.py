import sys
import heapq

input = sys.stdin.readline

# 무한 의미
INF = int(1e9)

# N 입력
N = int(input())

# M 입력
M = int(input())

# 버스 정보 저장할 그래프 정의
graph = [[] for _ in range(N + 1)]

# 최단 거리 저장할 리스트 정의
distances = [INF] * (N + 1)

# M개의 버스 정보 입력
for _ in range(M):
    start, end, weight = map(int, input().split())
    # 단방향 그래프
    graph[start].append((end, weight))


# 다익스트라 구현하기
def dijkstra(start):
    queue = []
    # 시작 도시 최단 거리 0
    heapq.heappush(queue, (0, start))
    distances[start] = 0

    # 큐 빌 때까지 반복
    while queue:
        # 값이 가장 작은 도시 선택
        distance, city = heapq.heappop(queue)
        # 방문한 적 있는 도시면 무시
        if distances[city] < distance:
            continue

        # 연결 도시 확인
        for next_city, weight in graph[city]:
            new_distance = distance + weight

            # 더 짧은 거리 있으면 갱신
            if new_distance < distances[next_city]:
                distances[next_city] = new_distance
                heapq.heappush(queue, (new_distance, next_city))


# A, B 입력
A, B = map(int, input().split())

# 다익스트라 수행
dijkstra(A)

# B 최단 거리 출력
print(distances[B])