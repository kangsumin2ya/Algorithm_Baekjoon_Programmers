# 시도 1 : 최단 거리를 구해야 하는데 모든 흰색 지점을 탐색하도록 잘못 구현
# 변경 1 : 시작부분에서 bfs 시작, 지도의 각 칸에 이동 거리 계산해 저장

from collections import deque

def solution(maps):
    
    # n, m 구하기
    n, m = len(maps), len(maps[0])
    
    # 방문 리스트 정의
    # visited = [[0] * n for _ in range(m)]
    
    return bfs(maps, n, m)

# bfs
def bfs(maps, n, m):
    
    # 이동 방향 정의
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # 큐 정의 : 시작점에서 출발
    queue = deque([(0, 0)]) # 튜플로 묶기
    
    # # 지도의 흰색을 검은색으로 바꿔서 방문 처리
    # maps[x][y] = 0
    
    # # 거리 계산
    # dist = 0
    
    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        
        # 이동
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            # 범위 벗어나면 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            # 벽이면 무시
            if maps[nx][ny] == 0:
                continue
            
            # 범위 내에서 방문하지 않았고 흰칸이라면
            if maps[nx][ny] == 1:
                # 거리 누적합
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))
                
                # # 거리 추가
                # dist += 1 
    
    # 도달 못했다면 -1 반환
    return maps[n-1][m-1] if maps[n-1][m-1] != 1 else -1