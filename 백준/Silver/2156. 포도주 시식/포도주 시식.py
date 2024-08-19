import sys

input = sys.stdin.readline

# n 입력
n = int(input())

# glasses 입력
glasses = [int(input()) for _ in range(n)]

# dp 테이블 초기화
dp = [0] * n

# dp 테이블 채우기
dp[0] = glasses[0]

if n > 1:
    dp[1] = glasses[0] + glasses[1]

if n > 2:
    dp[2] = max(glasses[2] + glasses[1], glasses[2] + glasses[0], dp[1])

if n > 3:
    for i in range(3, n):
        dp[i] = max(dp[i-3] + glasses[i-1] + glasses[i], dp[i-2] + glasses[i], dp[i-1])

# 정답 출력
print(dp[n-1])