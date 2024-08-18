import sys

input = sys.stdin.readline

# N 입력
N = int(input())

# A 입력
A = list(map(int, input().split()))

# dp 테이블 초기화
dp = [1] * N

# dp 테이블 채우기
for i in range(1, N):
    for j in range(i):
        if A[j] > A[i]:
            dp[i] = max(dp[i], dp[j] + 1)

# 결과 출력
print(max(dp))
