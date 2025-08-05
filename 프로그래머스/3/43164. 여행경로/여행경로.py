# from collections import deque

# def solution(tickets):
#     answer = []
    
#     target = len(tickets) 
    
#     return answer

        
def solution(tickets):
    graph = {}

    # 그래프 구성
    for start, depart in tickets:
        if start in graph:
            graph[start].append(depart)
        else:
            graph[start] = [depart]

    # 목적지 리스트를 알파벳 순 정렬 (뒤집어서 pop 시 알파벳 순으로 방문)
    for key in graph:
        graph[key].sort(reverse=True)

    route = []

    def dfs(current):
        while current in graph and graph[current]:
            next_dest = graph[current].pop()
            dfs(next_dest)
        route.append(current)

    dfs("ICN")
    return route[::-1]
