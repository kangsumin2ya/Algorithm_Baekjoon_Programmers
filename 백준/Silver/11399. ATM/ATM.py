import sys

input = sys.stdin.readline

# N 입력
N = int(input())

# 시간 입력
P = list(map(int, input().split()))

# 정렬
P.sort()

# 시간 세기
answer = 0

for i in range(N):
    for j in range(0, i+1):
        answer += P[j]

# 정답 출력
print(answer)
