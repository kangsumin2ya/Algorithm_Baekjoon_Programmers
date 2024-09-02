import sys

input = sys.stdin.readline

# N, M 입력
N, M = map(int, input().split())

# 교환 방법
changes = [list(map(int, input().split())) for _ in range(M)]

# 공 저장
balls = [i for i in range(1, N+1)]

# 교환하기
for change in changes:
    i, j = change[0], change[1]

    temp = balls[i-1]
    balls[i-1] = balls[j-1]
    balls[j - 1] = temp

# 결과 출력
print(' '.join(map(str, balls)))