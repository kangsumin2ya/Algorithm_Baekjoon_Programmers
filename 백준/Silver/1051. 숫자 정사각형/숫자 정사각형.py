import sys

input = sys.stdin.readline

N, M = map(int, input().split())

rect_num = []

for _ in range(N):
    rect_num.append(list(map(int, input().rstrip())))

answer = 1

max_move = min(N, M)

for i in range(N):
    for j in range(M):
        for k in range(max_move):
            if (i + k) < N and (j + k) < M and rect_num[i][j] == rect_num[i+k][j] == rect_num[i][j+k] == rect_num[i+k][j+k]:
                answer = max(answer, k+1)

print(answer**2)