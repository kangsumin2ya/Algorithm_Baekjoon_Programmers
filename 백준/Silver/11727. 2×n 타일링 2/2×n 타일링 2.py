import sys

input = sys.stdin.readline

# 1. 직사각형의 가로 길이 n을 입력받는다.
n = int(input())
# 2. dp 테이블을 정의한다.
dp = [0] * 1001

# 3. 점화식 계산이 필요 없는 경우를 고려하여 미리 계산해준다.
dp[1] = 1
dp[2] = 3

# 4. 점화식을 정의한다.
for i in range(3, n+1):
    dp[i] = (dp[i-1] + 2 * dp[i-2]) % 10007

# 5. dp[n]을 출력한다.
print(dp[n])