import sys
from collections import deque

input = sys.stdin.readline

# A, B 입력
A, B = map(int, input().split())


# BFS 구현
def bfs(x):
    queue = deque([(x, 1)])
    # 큐가 빌 때까지 반복
    while queue:
        x, count = queue.popleft()

        if x == A:
            return count

        if x < A:
            continue

        if x % 2 == 0:
            queue.append((x // 2, count + 1))

        if str(x)[-1] == '1':
            x = int(str(x)[0:-1])
            queue.append((x, count + 1))

    return -1


# BFS 수행
result = bfs(B)

# 결과 출력
print(result)
