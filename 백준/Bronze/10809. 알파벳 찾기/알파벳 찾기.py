import sys

input = sys.stdin.readline

# 1. S 입력
S = list(input().rstrip())

# 2. alphabets 정의
alphas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# 3. answer 정의
answer = []

# 4. 있는지 확인 후 위치를 answer에 추가
for alpha in alphas:
    if alpha in S:
        answer.append(S.index(alpha))
    else:
        answer.append(-1)

# 5. 출력
print(' '.join(map(str, answer)))