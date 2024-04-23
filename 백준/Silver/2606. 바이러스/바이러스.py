import sys

input = sys.stdin.readline

N = int(input())

M = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    start, end = map(int, input().split())

    graph[start].append(end)
    graph[end].append(start)

# 1부터 N까지 저장 -> [0,1,2,3,...,N]
visited = [0] * (N+1)

def DFS(v):
    for i in graph[v]:
        if not visited[i]:
            visited[i] = 1
            DFS(i)

DFS(1)

count = 0

for j in visited:
    # if visited[j] == 1:
    if visited[j]:
       count += 1

if count == 0:
    print(0)
else:
    print(count-1)
