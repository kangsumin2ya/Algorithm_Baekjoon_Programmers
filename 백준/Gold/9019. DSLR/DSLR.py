import sys
from collections import deque

input = sys.stdin.readline

# 테스트케이스 입력
T = int(input())

# 테스트케이스만큼 반복
for _ in range(T):
    # A, B 입력
    A, B = map(int, input().split())

    # 방문리스트 정의
    visited = [False for i in range(10001)]

    # 큐 정의
    queue = deque([(A, "")])

    # 방문 처리
    visited[A] = True

    # 큐가 빌 때까지 반복
    while queue:
        n, command = queue.popleft()

        # B가 됐는지 확인
        if n == B:
            print(command)
            break

        # D 계산
        D = (n * 2) % 10000
        if not visited[D]:
            visited[D] = True
            queue.append((D, command + "D"))

        # S 계산
        if n > 0:
            S = n - 1
        else:
            S = 9999
        if not visited[S]:
            visited[S] = True
            queue.append((S, command + "S"))

        # L 계산
        L = n // 1000 + (n % 1000) * 10
        if not visited[L]:
            visited[L] = True
            queue.append((L, command + "L"))

        # R 계산
        R = (n % 10) * 1000 + n // 10
        if not visited[R]:
            visited[R] = True
            queue.append((R, command + "R"))
