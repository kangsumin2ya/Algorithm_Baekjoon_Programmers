import sys

input = sys.stdin.readline

# N 입력
N = int(input())

# 첫번째 입력 받기
scores = list(map(int, input().split()))

# 초기값 설정
max_dp = scores
min_dp = scores

# 최대, 최소 갱신하기
for _ in range(N-1):
    # 이후 점수 입력 받기
    scores = list(map(int, input().split()))

    # 최댓값 갱신
    max_dp = [max(max_dp[0], max_dp[1]) + scores[0], max(max_dp[0], max_dp[1], max_dp[2]) + scores[1], max(max_dp[1], max_dp[2]) + scores[2]]

    # 최솟값 갱신
    min_dp = [min(min_dp[0], min_dp[1]) + scores[0], min(min_dp[0], min_dp[1], min_dp[2]) + scores[1], min(min_dp[1], min_dp[2]) + scores[2]]

# 결과 출력
print(max(max_dp), min(min_dp))
