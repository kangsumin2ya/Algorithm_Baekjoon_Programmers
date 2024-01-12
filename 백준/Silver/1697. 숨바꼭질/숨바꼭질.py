from collections import deque
import sys

input = sys.stdin.readline

N, K = map(int, input().split())

def BFS(N, K):
    # 방문 여부 리스트 정의
    visited = [False] * 100001

    # 큐에 현 위치와 시간 저장
    queue = deque([(N, 0)])

    while queue:
        # 큐에서 현 위치, 시간 가져오기
        cur_position, cur_time = queue.popleft()

        if cur_position == K:
            return cur_time

        if cur_position - 1 >= 0 and not visited[cur_position - 1]:
            queue.append([cur_position - 1, cur_time + 1])
            visited[cur_position - 1] = True

        if cur_position + 1 <= 100000 and not visited[cur_position + 1]:
            queue.append([cur_position + 1, cur_time + 1])
            visited[cur_position + 1] = True

        if cur_position * 2 <= 100000 and not visited[cur_position * 2]:
            queue.append([cur_position * 2, cur_time + 1])
            visited[cur_position * 2] = True

time = BFS(N, K)

print(time)