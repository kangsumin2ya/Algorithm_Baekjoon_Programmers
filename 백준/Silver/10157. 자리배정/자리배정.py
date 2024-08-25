import sys

input = sys.stdin.readline

# C, R 입력
C, R = map(int, input().split())

# K 입력
K = int(input())

# 만약 K가 배정받을 자리가 없다면 바로 0 출력
if K > C * R:
    print(0)

else:
    # 격자 정의
    grid = [[0] * (C + 1) for _ in range(R + 1)]

    # 이동 방향 (이동 순서에 따라 작성)
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # 배정 인원 셀 변수 정의
    count = 1

    # 시작 위치
    x, y = 1, 1

    # 시작 방향 (위쪽)
    move = 0

    while True:
        grid[y][x] = count

        # 이동
        nx, ny = x + moves[move][0], y + moves[move][1]

        # 움직이는 방향 바꾸기
        if nx < 1 or ny < 1 or nx > C or ny > R or grid[ny][nx] != 0:
            move = (move + 1) % 4
            nx, ny = x + moves[move][0], y + moves[move][1]

        if count == K:
            # 결과 출력
            print(x, y)
            break

        # 배정 후 카운트 증가
        x, y = nx, ny
        count += 1
