import sys

input = sys.stdin.readline

# N 입력
N = int(input())

# A 입력
A_list = list(map(int, input().split()))

# dp 테이블 정의
dp = [1001] * N

# dp 테이블 초기화
dp[0] = 0

for i in range(N):
    # 점프할 수 있는 범위 탐색
    for j in range(1, A_list[i] + 1):
        # 범위 내인지 확인
        if i + j < N:
            # 최소 점프 횟수 갱신
            dp[i + j] = min(dp[i + j], dp[i] + 1)

# 도달 여부 확인
if dp[N-1] == 1001:
    print(-1)
else:
    print(dp[N-1])
