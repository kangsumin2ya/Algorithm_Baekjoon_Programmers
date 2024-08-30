import sys

input = sys.stdin.readline

# N, M 입력
N, M = map(int, input().split())

# 바구니 정의
baskets = [0] * N

for _ in range(M):
    i, j, k = map(int, input().split())

    for idx in range(i - 1, j):
        baskets[idx] = k

# 결과 출력
print(" ".join(map(str, baskets)))
