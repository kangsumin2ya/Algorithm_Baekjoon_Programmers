import sys

input = sys.stdin.readline

# 1. 테스트케이스 수 T를 입력받는다.
T = int(input())


for _ in range(T):
    # 2. T번 반복하여 n을 입력받는다.
    n = int(input())

    # 3. dp테이블을 정의한다.
    dp = [0] * (n+1)

    # 4. 점화식 계산이 필요 없는 경우를 고려하여 미리 계산해준다.
    for i in range(1, n + 1):
        if i == 1:
            dp[i] = 1

        elif i == 2:
            dp[i] = 2

        elif i == 3:
            dp[i] = 4

        # 5. 점화식을 정의한다.
        else:
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    # 6. d[n]을 출력한다.
    print(dp[n])