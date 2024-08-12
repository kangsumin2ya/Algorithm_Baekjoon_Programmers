import sys
from collections import deque

input = sys.stdin.readline


# bfs 구현
def bfs():
    # 큐 정의
    queue = deque()
    # 초기값 입력
    queue.append((0, 0, C))
    # 방문 리스트 초기화
    visited = [[[0] * (C + 1) for _ in range(B + 1)] for _ in range(A + 1)]
    # 방문 처리
    visited[0][0][C] = 1
    # 결과 저장
    answer = set()

    while queue:
        a, b, c = queue.popleft()

        # 원하는 경우 찾았을 때 저장
        if a == 0:
            answer.add(c)

        # 물 옮기는 모든 경우 구하기 (한 물통 0 또는 다른 물통 가득)
        # 1) A → B
        if a + b > B:
            new_a, new_b = a - (B - b), B
        else:
            new_a, new_b = 0, b + a
        if not visited[new_a][new_b][c]:
            # 방문 처리
            visited[new_a][new_b][c] = 1
            # 큐에 넣기
            queue.append((new_a, new_b, c))

        # 2) A → C
        if a + c > C:
            new_a, new_c = a - (C - c), C
        else:
            new_a, new_c = 0, c + a
        if not visited[new_a][b][new_c]:
            # 방문 처리
            visited[new_a][b][new_c] = 1
            # 큐에 넣기
            queue.append((new_a, b, new_c))

        # 3) B → A
        if b + a > A:
            new_b, new_a = b - (A - a), A
        else:
            new_b, new_a = 0, b + a
        if not visited[new_a][new_b][c]:
            # 방문 처리
            visited[new_a][new_b][c] = 1
            # 큐에 넣기
            queue.append((new_a, new_b, c))

        # 4) B → C
        if b + c > C:
            new_b, new_c = b - (C - c), C
        else:
            new_b, new_c = 0, c + b
        if not visited[a][new_b][new_c]:
            # 방문 처리
            visited[a][new_b][new_c] = 1
            # 큐에 넣기
            queue.append((a, new_b, new_c))

        # 5) C → A
        if c + a > A:
            new_c, new_a = c - (A - a), A
        else:
            new_c, new_a = 0, a + c
        if not visited[new_a][b][new_c]:
            # 방문 처리
            visited[new_a][b][new_c] = 1
            # 큐에 넣기
            queue.append((new_a, b, new_c))

        # 6) C → B
        if c + b > B:
            new_c, new_b = c - (B - b), B
        else:
            new_c, new_b = 0, b + c
        if not visited[a][new_b][new_c]:
            # 방문 처리
            visited[a][new_b][new_c] = 1
            # 큐에 넣기
            queue.append((a, new_b, new_c))

    # 오름 차순 정렬해 반환
    return sorted(answer)


# A, B, C 입력
A, B, C = map(int, input().split())

# bfs 수행
answer = bfs()

# 결과 출력
print(' '.join(map(str, answer)))
