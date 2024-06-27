import sys

input = sys.stdin.readline

# 1. N, X 입력받기
N, X = map(int, input().split())

# 2. N개의 수열 A 입력받기
A = list(map(int, input().split()))

# 3. X보다 작은 수 찾기
answer = []

for a in A:
    if a < X:
        answer.append(a)

# 4. 출력하기
print(' '.join(map(str, answer)))