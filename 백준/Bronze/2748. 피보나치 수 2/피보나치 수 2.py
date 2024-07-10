import sys

input = sys.stdin.readline

# 1. n 입력
n = int(input())

# 2. dp 테이블 정의
dp = [0] * (n+1)

# 2-1. n 값에 따라 dp 테이블 초기화
dp[1] = 1

if n > 1:
    dp[2] = 1

# 3. 피보나치 수 계산해 dp 테이블 채우기
for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]

# 4. 원하는 형식으로 출력
print(dp[n])