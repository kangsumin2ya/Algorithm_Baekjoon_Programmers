import sys

input = sys.stdin.readline

# H, W 입력
H, W = map(int, input().split())

# N 입력
N = int(input())

# 스티커 크기 저장할 리스트 정의
stickers = []

# N번 반복해 R, C 입력
for _ in range(N):
    R, C = map(int, input().split())
    stickers.append((R, C))

# 최대 넓이 변수 정의
max_area = 0

# 전체 스티커 수 정의 (제외한 스티커 크기가 있기 때문에 따로 계산)
n = len(stickers)

for i in range(n):
    # 첫번째 스티커
    R1, C1 = stickers[i]
    for j in range(i + 1, n):
        # 두번째 스티커
        R2, C2 = stickers[j]
        # 위아래 붙이기
        if (R1 + R2 <= H and max(C1, C2) <= W) \
                or (R1 + C2 <= H and max(C1, R2) <= W) \
                or (C1 + C2 <= H and max(R1, R2) <= W) \
                or (C1 + R2 <= H and max(R1, C2) <= W):
            max_area = max(max_area, R1 * C1 + R2 * C2)

        # 나란히 붙이기
        elif (R1 + R2 <= W and max(C1, C2) <= H) \
                or (R1 + C2 <= W and max(C1, R2) <= H) \
                or (C1 + C2 <= W and max(R1, R2) <= H) \
                or (C1 + R2 <= W and max(R1, C2) <= H):
            max_area = max(max_area, R1 * C1 + R2 * C2)

# 정답 출력
print(max_area)