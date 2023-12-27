from collections import deque

import sys

input = sys.stdin.readline

N, M, V = map(int, input().split())

graph = []

for _ in range(N+1):
    graph.append([])

for _ in range(M):
    start, end = map(int, input().split())

    graph[start].append(end)
    graph[end].append(start)

for i in range(N+1):
    graph[i].sort()

def DFS(graph, start, visited):

    visited[start] = True

    print(start, end=' ')

    for i in graph[start]:
        if not visited[i]:
            DFS(graph, i, visited)

def BFS(graph, start, visited):
    queue = deque([start])

    visited[start] = True

    while queue:
        start = queue.popleft()
        print(start, end=' ')

        for i in graph[start]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

visited = [False] * (N + 1)
DFS(graph, V, visited)

print()

visited = [False] * (N + 1)
BFS(graph, V, visited)