import sys

input = sys.stdin.readline

# 테스트케이스 입력
T = int(input())

for _ in range(T):
    # 정수 입력
    n = int(input())

    # dp 테이블 정의
    dp = [0] * 12

    # 점화식 초기화
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    # 그 이상은 점화식 통해 값 채우기
    for i in range(4, 11):
        dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

    # 결과 출력
    print(dp[n])