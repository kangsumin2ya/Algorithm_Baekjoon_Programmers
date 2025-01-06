import sys

input = sys.stdin.readline

# dp 테이블 정의
dp = [0] * 5001

# dp 테이블 초기화
dp[0] = 1

# 점화식으로 짝수에만 dp 테이블 채우기
for n in range(2, 5001, 2):
    for i in range(2, n + 1, 2):
        dp[n] += dp[i - 2] * dp[n - i]

        # 1000000007로 나눈 값 저장
        dp[n] %= 1000000007


# 테스트케이스 개수 입력
T = int(input())

# 테스트케이스만큼 반복
for _ in range(T):
    # L 입력
    L = int(input())
    
    # 결과 출력
    print(dp[L])