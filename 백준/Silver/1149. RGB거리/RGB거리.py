import sys

input = sys.stdin.readline

# N 입력
N = int(input())

# 색칠 비용 입력
prices = [list(map(int, input().split())) for _ in range(N)]

# DP 테이블 초기화
dp = [[0] * 3 for _ in range(N)]
dp[0] = prices[0]

# DP 계산
for i in range(1, N):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + prices[i][0]  # 빨강으로 칠할 경우
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + prices[i][1]  # 초록으로 칠할 경우
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + prices[i][2]  # 파랑으로 칠할 경우

# 결과 출력
print(min(dp[N-1]))
