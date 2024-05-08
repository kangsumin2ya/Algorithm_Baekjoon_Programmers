import sys

input = sys.stdin.readline

n = int(input())

# 1. dp 테이블 정의
d = [0] * (n+1)

# 2. 계단 점수 입력
scores = [0]

for _ in range(n):
    scores.append(int(input()))

if len(scores) <= 2:
    print(sum(scores))

else:
    d[1] = scores[1]
    d[2] = scores[1] + scores[2]

    for i in range(3, n+1):
        d[i] = max(d[i-3]+scores[i-1]+scores[i], d[i-2] + scores[i])

    print(d[-1])