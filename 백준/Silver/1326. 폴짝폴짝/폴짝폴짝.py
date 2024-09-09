import sys
from collections import deque

input = sys.stdin.readline


# bfs 구현
def bfs(start, end):
    # 큐 정의
    queue = deque([(start, 0)])
    # 방문 처리
    visited[start] = 1
    # 큐가 빌 때까지 반복
    while queue:
        v, count = queue.popleft()

        # 도착하면 종료
        if v == end:
            return count

        # 적힌 숫자만큼 오른쪽 이동하면서 탐색
        for i in range(v + nums[v], N, nums[v]):
            # 방문 처리
            if not visited[i]:
                visited[i] = 1
                queue.append((i, count + 1))

        # 적힌 숫자만큼 왼쪽 이동하면서 탐색
        for i in range(v - nums[v], -1, -nums[v]):
            # 방문 처리
            if not visited[i]:
                visited[i] = 1
                queue.append((i, count + 1))
    # 도착하지 못한 경우
    return 0

# N 입력
N = int(input())

# 숫자 입력
nums = list(map(int, input().split()))

# 출발, 도착 입력
a, b = map(int, input().split())

# 방문 리스트 정의
visited = [0] * N

# bfs 수행 (리스트는 인덱스 0부터 시작하므로 1 빼주기)
result = bfs(a - 1, b - 1)

# 결과 출력
if result == 0:
    print(-1)
else:
    print(result)