import sys

input = sys.stdin.readline

# N 입력
N = int(input())

# dp 테이블 정의
dp = [[[0 for _ in range(1024)] for _ in range(10)] for _ in range(N+1)]

# dp 테이블 초기화
for i in range(1, 10):
    dp[1][i][1 << i] = 1

# dp 테이븛 채우기
for i in range(2, N+1):
    for j in range(10):
        for k in range(1024):
            if j > 0:
                dp[i][j][k | (1 << j)] = (dp[i][j][k | (1 << j)] + dp[i-1][j-1][k]) % 1000000000
            if j < 9:
                dp[i][j][k | (1 << j)] = (dp[i][j][k | (1 << j)] + dp[i-1][j+1][k]) % 1000000000

# 결과 계산
answer = sum(dp[N][j][1023] for j in range(10)) % 1000000000

# 결과 출력
print(answer)