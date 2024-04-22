import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


N = int(input())

graph = []

parents = [0] * (N+1)

for _ in range(N+1):
    graph.append([])

for _ in range(N-1):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

def DFS(v):
    for i in graph[v]:
        if not parents[i]:
            parents[i] = v
            DFS(i)

DFS(1)

for i in range(2, N+1):
    print(parents[i])