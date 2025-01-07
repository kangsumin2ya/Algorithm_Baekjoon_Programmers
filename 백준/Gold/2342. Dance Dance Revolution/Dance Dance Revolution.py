import sys

input = sys.stdin.readline

# 드는 힘 반환하는 함수 정의
def force(start, end):
    # 중앙에서 이동
    if start == 0:
        return 2

    # 같은 지점 이동
    elif start == end:
        return 1

    # 반대편 이동
    elif abs(start - end) == 2:
        return 4

    # 인접 지점 이동
    else:
        return 3


# 지시 사항 입력
orders = list(map(int, input().split()))

# dp 테이블 정의
dp = [[[500000 for _ in range(5)] for _ in range(5)] for _ in range(100001)]

# 시작 위치 초기화
dp[0][0][0] = 0

# dp 테이블 채우기
for i in range(len(orders) - 1):
    for left in range(5):
        for right in range(5):
            # 점화식 계산
            # 왼발 이동
            dp[i + 1][orders[i]][right] = min(dp[i + 1][orders[i]][right], dp[i][left][right] + force(left, orders[i]))
            # 오른발 이동
            dp[i + 1][left][orders[i]] = min(dp[i + 1][left][orders[i]], dp[i][left][right] + force(right, orders[i]))

# 테이블에서 최소 드는 힘 구하기
answer = 500001

for left in range(5):
    for right in range(5):
        answer = min(answer, dp[len(orders)-1][left][right])

# 결과 출력
print(answer)