from collections import deque

def solution(n, computers):
    answer = 0
    # 방문 리스트 정의
    visited = [0] * n
    

            
    def bfs(start):
        # 큐 정의
        queue = deque([start])
        # 방문 처리
        visited[start] = 1

        # 큐 빌 때까지 탐색
        while queue:
            node = queue.popleft()

            for i in range(n):
                if computers[node][i] == 1 and not visited[i]:
                    visited[i] = 1
                    queue.append(i)
    # bfs 수행
    for i in range(n):
        if not visited[i]:
            bfs(i)
            answer += 1
            
    return answer

