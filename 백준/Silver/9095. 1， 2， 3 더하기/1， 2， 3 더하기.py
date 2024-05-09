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
    if n == 1:
        print(1)

    elif n == 2:
        print(2)

    elif n == 3:
        print(4)

    # 5. 점화식을 정의한다.
    else:
        dp[1] = 1   # 1
        dp[2] = 2   # 1+1, 2
        dp[3] = 4   # 1+1+1, 1+2, 2+1, 3

        for i in range(4, n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

        # 6. d[n]을 출력한다.
        print(dp[n])