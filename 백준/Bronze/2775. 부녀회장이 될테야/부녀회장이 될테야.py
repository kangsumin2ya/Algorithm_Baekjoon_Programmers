import sys

input = sys.stdin.readline

# 1. T 입력
T = int(input())

# 2. T만큼 k, n을 한 줄씩 입력
for _ in range(T):
    k = int(input())
    n = int(input())
    # 3. dp 테이블 초기화
    dp = [[0] * 15 for _ in range(15)]

    # 4. dp 테이블 채우기
    # 4-1. 0층 채우기
    for i in range(1, 15):
        dp[0][i] = i

    # 4-2. k층의 1호 채우기
    for i in range(1, 15):
        dp[i][1] = 1

    # 4-3. 점화식에 따라 채우기
    for x in range(1, 15):
        for y in range(2, 15):
            dp[x][y] = dp[x][y-1] + dp[x-1][y]

    # 5. 원하는 형식으로 출력
    print(dp[k][n])