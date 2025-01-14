import sys

input = sys.stdin.readline


# 주사위 면 변화 함수
def move_dice(order):
    if order == 1:  # 동쪽
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]
    elif order == 2:    # 서쪽
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]
    elif order == 3:    # 북쪽
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]
    else:   # 남쪽
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]


# N, M, x, y, K 입력
N, M, x, y, K = map(int, input().split())

# 지도에 쓰여 있는 수 입력
map_info = [list(map(int, input().split())) for _ in range(N)]

# 이동 명령 입력
orders = list(map(int, input().split()))

# 각 면의 값 초기화
dice = [0, 0, 0, 0, 0, 0]

# 이동 방향
moves = [(0, 1), (0, -1), (-1, 0), (1, 0)]

# 명령 수행
for order in orders:
    # 이동
    nx = x + moves[order - 1][0]
    ny = y + moves[order - 1][1]
    # 범위 내 이동
    if 0 <= nx < N and 0 <= ny < M:
        x, y = nx, ny
        # 주사위 면 변화
        move_dice(order)

        # 주사위 숫자 변화
        if map_info[x][y] == 0:
            map_info[x][y] = dice[5]
        else:
            dice[5] = map_info[x][y]
            map_info[x][y] = 0

        # 결과 출력
        print(dice[0])
