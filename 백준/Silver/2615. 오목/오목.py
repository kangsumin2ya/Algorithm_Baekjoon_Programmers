import sys
from collections import deque

input = sys.stdin.readline

# 4가지 방향 정의 : 가로, 세로, 대각선 아래, 대각선 위
directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]


def bfs(x, y):
    # 색 저장
    color = stones[x][y]

    # 탐색
    for direction in directions:
        queue = deque([(x, y)])
        count = 1
        answer_x, answer_y = x, y

        while queue:
            cx, cy = queue.popleft()
            nx, ny = cx + direction[0], cy + direction[1]

            # 바둑판 범위 안에 있고 같은 색이면 탐색
            if 0 <= nx < 19 and 0 <= ny < 19 and stones[nx][ny] == color:
                count += 1
                queue.append((nx, ny))

                # 6개 이상인지 확인
                if count == 5:
                    # 육목 체크
                    if 0 <= x - direction[0] < 19 and 0 <= y - direction[1] < 19 and stones[x - direction[0]][y - direction[1]] == color:
                        break
                    if 0 <= nx + direction[0] < 19 and 0 <= ny + direction[1] < 19 and stones[nx + direction[0]][ny + direction[1]] == color:
                        break

                    # 5개면 승리이므로 원하는 결과 출력
                    print(color)
                    return answer_x + 1, answer_y + 1
    # 승리 아무도 못함
    return -1, -1


# 바둑 상태 입력
stones = [list(map(int, input().split())) for _ in range(19)]

# 바둑알 위치 확인
answer_x, answer_y = -1, -1
for i in range(19):
    for j in range(19):
        if stones[i][j] != 0:
            answer_x, answer_y = bfs(i, j)
            if answer_x != -1 and answer_y != -1:
                break
    if answer_x != -1 and answer_y != -1:
        break

# 결과 출력
if answer_x == -1 and answer_y == -1:
    print(0)
else:
    print(answer_x, answer_y)
