import sys
import heapq

input = sys.stdin.readline

# 무한 의미
INF = int(1e9)


# 다익스트라 구현
def dijkstra(start, end):
    queue = []
    heapq.heappush(queue, (0, start))
    costs[start] = 0

    while queue:
        cost, city = heapq.heappop(queue)

        if costs[city] < cost:
            continue

        for next_city, next_cost in graph[city]:
            new_cost = cost + next_cost
            if new_cost < costs[next_city]:
                costs[next_city] = new_cost
                prev[next_city] = city
                heapq.heappush(queue, (new_cost, next_city))

    # 경로 저장
    path = []
    now = end
    while now != -1:
        path.append(now)
        now = prev[now]
    path.reverse()

    return costs[end], path


# 입력 받기
n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    start, end, cost = map(int, input().split())
    graph[start].append([end, cost])

want_start, want_end = map(int, input().split())

# 최소 비용 저장할 리스트 정의
costs = [INF] * (n + 1)

# 경로 저장 리스트 정의
prev = [-1] * (n + 1)

# 다익스트라 실행
min_cost, path = dijkstra(want_start, want_end)

# 출력하기
print(min_cost)
print(len(path))
print(*path)
