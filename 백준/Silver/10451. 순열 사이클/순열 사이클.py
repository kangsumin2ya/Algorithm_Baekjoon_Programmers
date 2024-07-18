import sys
from collections import deque

input = sys.stdin.readline


# 1. BFS 정의
def bfs(x):
    queue = deque([x])
    # 방문 처리
    visited[x] = 1
    # 큐가 빌 때까지 반복
    while queue:
        v = queue.popleft()
        # 해당 노드 연결 정보 확인
        for i in graph[v]:
            # 방문 안했다면
            if not visited[i]:
                visited[i] = 1
                queue.append(i)


# 1. 정답 저장 리스트
answer = []

# 2. T 입력
T = int(input())

for _ in range(T):
    # 3. N 입력
    N = int(input())

    # 4. 그래프 정의
    graph = [[] for _ in range(N + 1)]

    # 5. N개 숫자 순열 입력
    nums = list(map(int, input().split()))

    # 6. 그래프에 저장
    for i in range(1, N + 1):
        graph[i].append(nums[i - 1])

    # 7. 방문 리스트 정의
    visited = [0] * (N + 1)

    # 8. 횟수 변수 정의
    count = 0

    # 8. 그래프 돌면서 BFS 수행
    for i in range(1, N + 1):
        if not visited[i]:
            # bfs 수행
            bfs(i)
            # 횟수 세기
            count += 1
    # 9. 정답 저장
    answer.append(count)

# 10. 원하는 형식으로 출력
for count in answer:
    print(count)