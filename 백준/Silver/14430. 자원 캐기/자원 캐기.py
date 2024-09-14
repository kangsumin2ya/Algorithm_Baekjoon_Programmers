import sys

input = sys.stdin.readline

# N, M 입력
N, M = map(int, input().split())

# 탐색 영역 정보 입력
search_areas = [list(map(int, input().split())) for _ in range(N)]

# dp 테이블 정의
dp = [[0] * M for _ in range(N)]

# 테이블 초기화
dp[0][0] = search_areas[0][0]

# 첫번째 열 채우기
for i in range(1, N):
    dp[i][0] = dp[i-1][0] + search_areas[i][0]

# 첫번째 행 채우기
for j in range(1, M):
    dp[0][j] = dp[0][j-1] + search_areas[0][j]

# 테이블 채우기
for i in range(1, N):
    for j in range(1, M):
        dp[i][j] = max(dp[i-1][j] + search_areas[i][j], dp[i][j-1] + search_areas[i][j])

# 결과 출력
print(dp[N-1][M-1])
