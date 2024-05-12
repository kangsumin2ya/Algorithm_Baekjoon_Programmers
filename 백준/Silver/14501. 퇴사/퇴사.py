import sys

input = sys.stdin.readline

# 0. 변수를 정의한다.
T = []
P = []
max_profit = 0

# 1. 퇴사까지 남은 날 N을 입력받는다.
N = int(input())

# 2. dp 테이블을 정의한다.
dp = [0] * 16

# 3. N번 반복하여 T, P를 입력받는다.
for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

# 4. dp 테이블에 점화식 따라 값을 채워넣는다.
for i in range(N-1, -1, -1):
    date = i + T[i]

    # 4-1. 상담 기간이 마지막 날을 넘지 않는지 체크
    if date <= N:
        dp[i] = max(P[i] + dp[date], max_profit)
        max_profit = dp[i]

    else:
        dp[i] = max_profit

# 5. dp[N]을 출력한다.
print(max_profit)