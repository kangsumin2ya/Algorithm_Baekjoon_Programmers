import sys

input = sys.stdin.readline

# 계단 수 입력
n = int(input())

# 계단 점수 입력
scores = [int(input()) for _ in range(n)]

# dp 테이블 정의
dp = [0] * (n + 1)

if n == 1:
    print(scores[0])
elif n == 2:
    print(scores[0] + scores[1])
else:
    # dp 초기값 채우기
    dp[1] = scores[0]
    dp[2] = scores[0] + scores[1]

    # dp 값 채우기
    for i in range(3, n + 1):
        dp[i] = max(dp[i - 2] + scores[i - 1], dp[i - 3] + scores[i - 2] + scores[i - 1])

    print(dp[-1])
