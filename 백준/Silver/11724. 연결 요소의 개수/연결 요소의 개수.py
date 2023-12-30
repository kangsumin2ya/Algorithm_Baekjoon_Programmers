import sys

sys.setrecursionlimit(10000) # 재귀 깊이 설정

input = sys.stdin.readline

def DFS(graph, start, visited):

    visited[start] = True

    for i in graph[start]:
        if not visited[i]:
            DFS(graph, i, visited)

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())

    graph[u].append(v)
    graph[v].append(u)

count = 0

visited = [False] * (N + 1)

for i in range(1, N+1):
    if not visited[i]:
        DFS(graph, i, visited)
        count += 1

print(count)