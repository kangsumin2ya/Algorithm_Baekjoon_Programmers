import sys

input = sys.stdin.readline

# N, M 입력
N, M = map(int, input().split())

# K 입력
K = int(input())

# 공사 도로 저장
no_enter = set()
for _ in range(K):
    a, b, c, d = map(int, input().split())
    no_enter.add((a, b, c, d))
    no_enter.add((c, d, a, b))

# 지도 정보 입력
map_info = [[0] * (M + 1) for _ in range(N + 1)]
map_info[0][0] = 1

for m in range(M + 1):
    for n in range(N + 1):
        # 범위 내에 있는 직전 점 찾아 dp값 계산
        if n > 0 and (n - 1, m, n, m) not in no_enter:
            map_info[n][m] += map_info[n - 1][m]

        if m > 0 and (n, m - 1, n, m) not in no_enter:
            map_info[n][m] += map_info[n][m - 1]

print(map_info[N][M])