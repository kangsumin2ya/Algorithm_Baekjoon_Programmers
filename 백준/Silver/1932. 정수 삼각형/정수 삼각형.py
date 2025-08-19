import sys

input = sys.stdin.readline

# 입력
n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]

# DP 계산
for i in range(1, n):
    for j in range(len(triangle[i])):
        # 맨 왼쪽일 경우 바로 위만 받음
        if j == 0:
            triangle[i][j] += triangle[i-1][j]
        # 맨 오른쪽일 경우 왼쪽 위만 받음
        elif j == len(triangle[i]) - 1:
            triangle[i][j] += triangle[i-1][j-1]
        # 그외엔 바로 위, 왼쪽 위 둘다 받음
        else:
            triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])

# 출력
print(max(triangle[-1]))
