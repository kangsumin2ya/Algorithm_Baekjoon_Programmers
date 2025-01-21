import sys
from collections import deque

input = sys.stdin.readline

# 4가지 이동 방향
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]


# bfs 함수 정의
def bfs():
    # 방문 리스트 정의
    visited = [[0] * (w + 2) for _ in range(h + 2)]

    # 훔칠 수 있는 문서 개수 저장 변수 정의
    count = 0

    # 큐 정의
    queue = deque([(0, 0)])
    # 방문 처리
    visited[0][0] = 1

    # 큐 빌 때까지 수행
    while queue:
        x, y = queue.popleft()
        visited[x][y] = 1

        # 4가지 방향 확인
        for i in range(4):
            nx, ny = x + moves[i][0], y + moves[i][1]

            # 범위 내이고 벽이 아니면서 방문한 적 없는 곳이라면 이동
            if 0 <= nx < h+2 and 0 <= ny < w+2 and map_info[nx][ny] != "*" and not visited[nx][ny]:
                # 빈 공간이면 계속 이동
                if map_info[nx][ny] == ".":
                    queue.append((nx, ny))
                    visited[nx][ny] = 1

                # 얻은 적 없는 문서라면 개수 세기
                elif map_info[nx][ny] == "$":
                    # 찾은 문서 개수 증가
                    count += 1
                    # 방문 처리
                    visited[nx][ny] = 1
                    # 빈공간으로 변경
                    map_info[nx][ny] = "."
                    # 계속 이동
                    queue.append((nx, ny))

                # 문 발견
                elif "A" <= map_info[nx][ny] <= "Z":
                    # 키가 있다면 지나가기
                    if map_info[nx][ny].lower() in keys:
                        # 빈 공간 변경
                        map_info[nx][ny] = "."
                        # 방문 처리
                        visited[nx][ny] = 1
                        # 계속 이동
                        queue.append((nx, ny))

                # 키 발견
                elif "a" <= map_info[nx][ny] <= "z":
                    # 없는 키라면
                    if map_info[nx][ny] not in keys:
                        # 가지고 있는 키 리스트에 추가
                        keys.append(map_info[nx][ny])
                        # 계속 이동
                        queue.append((nx, ny))
                        # 방문리스트 초기화해 새로 탐색
                        visited = [[0] * (w + 2) for _ in range(h + 2)]
                        # 큐도 초기화
                        queue = deque([(nx, ny)])
                    # 있는 키라면 방문 처리 후 지나가기
                    else:
                        # 계속 이동
                        queue.append((nx, ny))

                    # 빈 공간 변경
                    map_info[nx][ny] = "."
                    # 방문 처리
                    visited[nx][ny] = 1

    return count


# 테스트 케이스 수 입력
T = int(input())

# 정답 모두 저장할 리스트 정의
answer = []

# 테스트 케이스마다 반복
for _ in range(T):
    # h, w 입력
    h, w = map(int, input().split())

    # 빌딩 입력
    map_info = [['.'] * (w + 2)] + [["."] + list(map(str, input().rstrip())) + ["."] for _ in range(h)] + [['.'] * (w + 2)]

    # 가지고 있는 키 입력
    keys = list(map(str, input().rstrip()))

    # bfs 수행 후 결과 추가
    answer.append(bfs())

# 결과 출력
for a in answer:
    print(a)