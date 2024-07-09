# N, M 입력
N, M = map(int, input().split())

# # 행렬 입력 받기
A = []
B = []

for _ in range(N):
    A.append(list(map(int, input().split())))

for _ in range(N):
    B.append(list(map(int, input().split())))

# 더하기 연산
for i in range(M):
    for j in range(N):
        A[j][i] += B[j][i]

# 원하는 형태로 출력
for row in A:
    print(*row)