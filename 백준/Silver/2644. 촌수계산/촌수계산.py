import sys

input = sys.stdin.readline

n = int(input())

start, end = map(int, input().split())

m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())

    graph[x].append(y)
    graph[y].append(x)

visited = [0] * (n+1)

def DFS(v, count):
    visited[v] = 1

    if v == end:
        return count

    for i in graph[v]:
        if not visited[i]:
            result = DFS(i, count + 1)

            if result is not None:
                return result

count = DFS(start,0)

if count == None:
    print(-1)

else:
    print(count)