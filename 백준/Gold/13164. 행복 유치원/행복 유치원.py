import sys

input = sys.stdin.readline

# N, K 입력
N, K = map(int, input().split())

# 키 입력
heights = list(map(int, input().split()))

# 각 키의 차이 계산
d = []
for i in range(1, N):
    d.append(heights[i] - heights[i-1])

# 차이 정렬
d.sort()

# 끝에서 K-1개 제외
d = d[:N - K]

# 차이 합 계산
print(sum(d))
