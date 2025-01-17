import sys
from collections import deque

input = sys.stdin.readline

# 4가지 이동 방향 정의 (0 : 오른쪽, 1 : 왼쪽, 2 : 위, 3 : 아래)
moves = [(0, 1), (0, -1), (-1, 0), (1, 0)]


# 온도 증가 함수
def temp_up(r, c, dir):
    visited = [[False] * C for _ in range(R)]
    queue = deque([(r + moves[dir][0], c + moves[dir][1], 5)])

    while queue:
        r, c, temp = queue.popleft()
        room[r][c] += temp

        if temp > 1:  # 온도가 1보다 클 경우, 인접 칸에 온도 전달
            nr, nc = r + moves[dir][0], c + moves[dir][1]
            if 0 <= nr < R and 0 <= nc < C:
                if not wall[dir][r][c] and not visited[nr][nc]:
                    queue.append((nr, nc, temp - 1))
                    visited[nr][nc] = True

                if dir >= 2:  # 위/아래 방향 추가 탐색
                    if c - 1 >= 0 and not wall[1][r][c] and not wall[dir][r][c - 1] and not visited[nr][c - 1]:
                        queue.append((nr, c - 1, temp - 1))
                        visited[nr][c - 1] = True
                    if c + 1 < C and not wall[0][r][c] and not wall[dir][r][c + 1] and not visited[nr][c + 1]:
                        queue.append((nr, c + 1, temp - 1))
                        visited[nr][c + 1] = True
                else:  # 좌/우 방향 추가 탐색
                    if r - 1 >= 0 and not wall[2][r][c] and not wall[dir][r - 1][c] and not visited[r - 1][nc]:
                        queue.append((r - 1, nc, temp - 1))
                        visited[r - 1][nc] = True
                    if r + 1 < R and not wall[3][r][c] and not wall[dir][r + 1][c] and not visited[r + 1][nc]:
                        queue.append((r + 1, nc, temp - 1))
                        visited[r + 1][nc] = True


# 온도 조절 함수
def control_temp():
    new_room = [[room[r][c] for c in range(C)] for r in range(R)]
    for r in range(R):
        for c in range(C):
            for k in [0, 3]:  # 오른쪽과 아래 방향
                nr, nc = r + moves[k][0], c + moves[k][1]
                if 0 <= nr < R and 0 <= nc < C and not wall[k][r][c]:
                    # 온도 차이 계산
                    diff = abs(room[r][c] - room[nr][nc]) // 4
                    # 온도 조절
                    if room[r][c] > room[nr][nc]:
                        new_room[r][c] -= diff
                        new_room[nr][nc] += diff
                    else:
                        new_room[r][c] += diff
                        new_room[nr][nc] -= diff
    return new_room


# 바깥쪽 칸 온도 감소 함수
def temp_down():
    for i in range(C):
        if room[0][i] > 0:
            room[0][i] -= 1
        if room[R - 1][i] > 0:
            room[R - 1][i] -= 1
    for i in range(1, R - 1):
        if room[i][0] > 0:
            room[i][0] -= 1
        if room[i][C - 1] > 0:
            room[i][C - 1] -= 1


# R, C, K 입력
R, C, K = map(int, input().split())

# 방 정보 입력
room = []
heater = []  # 온풍기 위치
check_temp = []  # 온도 조사 위치

for i in range(R):
    row = list(map(int, input().split()))
    for j in range(C):
        if row[j] == 5:
            check_temp.append((i, j))  # 온도 조사할 구간 추가
        elif row[j] > 0:
            heater.append((i, j, row[j]))  # 온풍기 위치 추가
    room.append([0] * C)  # 온도 저장에 이용

# 벽의 개수 입력
W = int(input())

# 벽 정보 입력
wall = [[[False] * C for _ in range(R)] for _ in range(4)]

for _ in range(W):
    x, y, t = map(int, input().split())
    x -= 1
    y -= 1

    if t == 0:  # 위/아래 벽
        wall[2][x][y] = True
        wall[3][x - 1][y] = True
    else:  # 왼쪽/오른쪽 벽
        wall[0][x][y] = True
        wall[1][x][y + 1] = True

# 초콜릿 개수 저장 변수 정의
choco = 0

# 성능 테스트 시작
while True:
    # 1. 온풍기 작동
    for r, c, dir in heater:
        temp_up(r, c, dir - 1)

    # 2. 온도 조절
    room = control_temp()

    # 3. 바깥쪽 칸 온도 감소
    temp_down()

    # 4. 초콜릿 추가
    choco += 1

    # 5. 온도 조사 위치 확인
    all_good = True
    for r, c in check_temp:
        if room[r][c] < K:
            all_good = False
            break

    # 종료 조건
    if all_good or choco > 100:
        break

# 결과 출력
print(choco)