import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())

    D = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

    for j in range(1, M+1):
        D[1][j] = j
        D[0][j] = 1

    for i in range(2, N+1):
        for j in range(i, M+1):
            D[i][j] = D[i-1][j-1] + D[i][j-1]

    print(D[N][M])