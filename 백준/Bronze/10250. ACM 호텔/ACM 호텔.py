import sys

input = sys.stdin.readline

# 1. 테스트케이스 수 입력
T = int(input())

# 2. H(호텔 층 수), W(각 층의 방 수), N(손님 순서) 입력 받기
hotels = [list(map(int, input().split())) for _ in range(T)]

# 3. 테스트케이스마다 N번째 손님의 방 번호 출력
for hotel in hotels:
    H, W, N = hotel[0], hotel[1], hotel[2]

    # 3-1. 층 수 계산
    floor = N % H
    # 3-2. 방 번호 계산
    room = N // H + 1

    # 3-1. 층 수가 0이 나오면 꼭대기 층이기 때문에 방 번호는 한 칸 줄어야 한다.
    if floor == 0:
        floor = H
        room -= 1

    print(floor * 100 + room)