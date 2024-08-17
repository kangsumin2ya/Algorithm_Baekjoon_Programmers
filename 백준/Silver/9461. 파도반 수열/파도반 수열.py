import sys

input = sys.stdin.readline

# dp 테이블 만들기
dp = [0] * 101

dp[1], dp[2], dp[3] = 1, 1, 1
dp[4], dp[5] = 2, 2

for i in range(6, 101):
    dp[i] = dp[i-3] + dp[i-2]

# 테스트케이스 수 입력
T = int(input())

# 정답 저장 리스트
answer = []

for _ in range(T):
    # N 입력
    N = int(input())

    # 정답 찾기
    answer.append(dp[N])

# 정답 출력
for a in answer:
    print(a)