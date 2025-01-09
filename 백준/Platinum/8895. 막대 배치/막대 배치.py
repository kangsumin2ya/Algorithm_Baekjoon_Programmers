import sys

input = sys.stdin.readline

# 테스트케이스 입력
T = int(input())

# 테스트케이스마다 반복
for _ in range(T):
    # n, l, r 입력
    n, l, r = map(int, input().split())

    # dp 테이블 정의
    dp = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]

    # dp 테이블 초기화
    dp[1][1][1] = 1

    # dp 테이블 채우기
    for i in range(2, 21):
        for j in range(1, l + 1):
            for k in range(1, r + 1):
                dp[i][j][k] += dp[i-1][j-1][k]
                dp[i][j][k] += dp[i - 1][j][k - 1]
                dp[i][j][k] += dp[i - 1][j][k] * (i - 2)

    # 결과 출력
    print(dp[n][l][r])
