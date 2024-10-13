import sys

input = sys.stdin.readline

# N, M 입력
N, M = map(int, input().split())

# 듣도 못한 사람 입력
no_heard = set(input().rstrip() for _ in range(N))

# 보도 못한 사람 입력
no_saw = set(input().rstrip() for _ in range(M))

# 교집합 구하기
no_heard_saw = no_heard & no_saw

# 정렬 후 출력
answer = sorted(list(no_heard_saw))

print(len(answer))

for a in answer:
    print(a)