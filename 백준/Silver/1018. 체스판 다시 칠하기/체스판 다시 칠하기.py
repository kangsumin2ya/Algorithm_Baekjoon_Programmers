import sys

input = sys.stdin.readline

# N, M 입력
N, M = map(int, input().split())

# 체스판 입력
chess = [input().rstrip() for _ in range(N)]

# 체스판의 두 가지 패턴 정의
white_first = [
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW'
]
# 최소 덧칠 횟수 정의
min_paint = 64

# 보드판 자르기
for j in range(N-7):
    for i in range(M-7):
        # 덧칠 횟수 초기화
        count = 0

        # 8*8 보드 확인
        for row in range(8):
            for col in range(8):
                if chess[j + row][i + col] != white_first[row][col]:
                    count += 1

        # 덧칠 횟수가 더 작은 것을 선택
        min_paint = min(min_paint, count, 64-count)

# 원하는 형태로 출력
print(min_paint)